from strawberry.types import Info

from src.api.resolvers import stmts
from src.api.resolvers.context import ContextType, RootValueType, get_session
from src.api.schema.types import GetCitiesPayload


async def get_cities(
    info: Info[ContextType, RootValueType]
) -> GetCitiesPayload:
    session = get_session(info)
    cities = await stmts.get_cities(session=session)
    return GetCitiesPayload(cities=cities, severErrors=[])  # type: ignore
