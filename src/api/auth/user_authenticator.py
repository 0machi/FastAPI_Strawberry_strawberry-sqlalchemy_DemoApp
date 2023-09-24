from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from src.api.auth.token import get_access_token
from src.api.resolvers.stmts.user_stmt import get_user_by_id
from src.database.models import User


async def authenticate_user(token: str, session: AsyncSession) -> User:
    jwt = get_access_token(token=token)
    id = jwt.get("sub")
    if id is None:
        raise Exception("Could not validate credentials.")
    user = await get_user_by_id(session=session, id=UUID(id))
    if user is None:
        raise Exception("Could not validate credentials.")
    return user
