from typing import AsyncIterator

import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.main import app
from src.database.db import db
from src.database.models import Base


@pytest_asyncio.fixture()
async def db_session() -> AsyncIterator[AsyncSession]:
    db.connect()
    if db.engine is None:
        raise ValueError("engine not found.")
    async with db.engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    if db.session is None:
        raise ValueError("session not found.")
    async with db.session() as session:
        yield session
        await session.close()


@pytest.fixture()
def setup_app(db_session: AsyncSession) -> None:
    app.dependency_overrides[db.get_db_session] = lambda: db_session
