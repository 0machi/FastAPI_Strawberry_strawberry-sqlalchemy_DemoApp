from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import expression as sql

from src.database.models import City


async def get_cities(session: AsyncSession) -> list[City]:
    query = sql.select(City)
    result = await session.execute(query)
    cities = result.scalars().all()
    return list(cities)
