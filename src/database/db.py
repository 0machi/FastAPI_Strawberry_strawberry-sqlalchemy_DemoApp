from typing import AsyncIterator, Optional

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.database.config import Config, db_config


class Database:
    def __init__(self, db_config: Config) -> None:
        self.session: Optional[async_sessionmaker[AsyncSession]] = None
        self.engine: Optional[AsyncEngine] = None
        self.db_config: Config = db_config

    def connect(self) -> None:
        self.engine = create_async_engine(url=self.db_config.dsn)

        self.session = async_sessionmaker(
            bind=self.engine,
            autocommit=False,
        )

    async def disconnect(self) -> None:
        if self.engine is None:
            raise ValueError("engine not found.")
        await self.engine.dispose()

    async def get_db_session(
        self,
    ) -> AsyncIterator[AsyncSession]:
        if self.session is None:
            raise ValueError("session not found.")
        async with self.session() as session:
            yield session


db = Database(db_config=db_config)
