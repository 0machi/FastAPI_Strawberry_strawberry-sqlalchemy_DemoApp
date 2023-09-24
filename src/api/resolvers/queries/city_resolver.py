from strawberry.types import Info

from src.api.auth.user_authenticator import authenticate_user
from src.api.resolvers.context import (
    ContextType,
    RootValueType,
    get_session,
    get_token,
)
from src.api.resolvers.stmts import city_stmt
from src.api.schema.types import GetCitiesPayload


async def get_cities(
    info: Info[ContextType, RootValueType]
) -> GetCitiesPayload:
    token = get_token(info)
    session = get_session(info)
    user = await authenticate_user(session=session, token=token)
    cities = await city_stmt.get_cities(session=session)
    return GetCitiesPayload(cities=cities, severErrors=[])  # type: ignore
