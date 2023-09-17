from typing import AsyncIterator, Optional

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.database.config import db_config


class Database:
    def __init__(self) -> None:
        self.__session: Optional[async_sessionmaker[AsyncSession]] = None
        self.__engine: Optional[AsyncEngine] = None

    def connect(self) -> None:
        self.__engine = create_async_engine(url=db_config.dsn)

        self.__session = async_sessionmaker(
            bind=self.__engine,
            autocommit=False,
        )

    async def disconnect(self) -> None:
        if self.__engine is None:
            raise ValueError("__engine not found.")
        await self.__engine.dispose()

    async def get_db(
        self,
    ) -> AsyncIterator[AsyncSession]:
        if self.__session is None:
            raise ValueError("__session not found.")
        async with self.__session() as session:
            yield session


db = Database()
