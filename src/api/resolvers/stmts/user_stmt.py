from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import expression as sql

from src.database.models import User


async def get_user_by_id(session: AsyncSession, id: UUID) -> User | None:
    query = sql.select(User).where(User.id == id)
    result = await session.execute(query)
    user = result.scalars().first()
    return user
