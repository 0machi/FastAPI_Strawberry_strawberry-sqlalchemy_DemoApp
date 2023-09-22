from contextlib import ExitStack
from typing import AsyncIterator, Generator

import asyncpg
import pytest
import pytest_asyncio
from fastapi import FastAPI
from httpx import AsyncClient
from pytest_postgresql.janitor import DatabaseJanitor
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.app import init_app
from src.database.config import db_config
from src.database.session_manager import (
    DatabaseSessionManager,
    get_db,
    sessionmanager,
)
from tests.seed import init_stmts


@pytest.fixture()
def app() -> Generator[FastAPI, None, None]:
    with ExitStack():
        yield init_app(init_db=True)


@pytest_asyncio.fixture()
async def async_client(app: FastAPI) -> AsyncIterator[AsyncClient]:
    async def get_db_override() -> AsyncIterator[AsyncSession]:
        async with sessionmanager.session() as session:
            yield session

    app.dependency_overrides[get_db] = get_db_override
    async with AsyncClient(
        app=app, base_url="http://localhost:8000"
    ) as client:
        yield client


@pytest_asyncio.fixture()
async def session() -> AsyncIterator[DatabaseSessionManager]:
    with DatabaseJanitor(
        user=db_config.user,
        host=db_config.host,
        port=db_config.port,
        dbname="test_db",
        version="15.3",
        password=db_config.password,
    ):
        sessionmanager.init(dsn=db_config.dsn)
        async with sessionmanager.connect() as connection:
            await sessionmanager.drop_all(connection)
            await sessionmanager.create_all(connection)
        conn = await asyncpg.connect(db_config.dsn.replace("+asyncpg", ""))
        for stmt in init_stmts:
            await conn.execute(stmt)
        await conn.close()
        yield sessionmanager
        await sessionmanager.close()
