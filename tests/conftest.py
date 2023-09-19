from typing import AsyncIterator, Callable, Generator

import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy import event
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import Session, SessionTransaction, sessionmaker

from src.api.main import app
from src.database.config import db_config
from src.database.db import db
from src.database.models import Base
from tests.seed import setup_db


@pytest_asyncio.fixture()
async def init_db() -> None:
    async_engine = create_async_engine(url=db_config.dsn)
    async with async_engine.connect() as conn:
        await conn.begin()
        await conn.begin_nested()
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        AsyncSessionLocal = sessionmaker(  # type: ignore
            bind=conn,
            class_=AsyncSession,
            autoflush=False,
            autocommit=False,
        )
        async_session = AsyncSessionLocal()

        @event.listens_for(async_session.sync_session, "after_transaction_end")
        def end_savepoint(
            session: Session, transaction: SessionTransaction
        ) -> None:
            if conn.closed:
                return
            if not conn.in_nested_transaction():
                if conn.sync_connection:
                    conn.sync_connection.begin_nested()

        def test_get_session() -> Generator[sessionmaker[Session], None, None]:
            yield AsyncSessionLocal

        app.dependency_overrides[db.get_db_session] = test_get_session
        setup_db(session=async_session)

    await async_engine.dispose()


@pytest_asyncio.fixture()
async def async_session() -> Callable[[], AsyncIterator[AsyncSession]]:
    async def test_session() -> AsyncIterator[AsyncSession]:
        db.connect()
        if db.session is None:
            raise ValueError("session not found.")
        async with db.session() as session:
            yield session
            await session.close()

    return test_session


@pytest_asyncio.fixture()
async def async_client(
    async_session: Callable[[], AsyncIterator[AsyncSession]]
) -> AsyncIterator[AsyncClient]:
    app.dependency_overrides[db.get_db_session] = async_session
    async with AsyncClient(
        app=app, base_url="http://localhost:8000"
    ) as client:
        yield client
