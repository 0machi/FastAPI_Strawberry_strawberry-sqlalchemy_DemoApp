from strawberry.types import Info

from src.api.resolvers.context import ContextType, RootValueType, get_session
from src.api.resolvers.stmts import country_stmt
from src.api.schema.types import GetCountriesPayload, GetCountryPayload


async def get_countries(
    info: Info[ContextType, RootValueType]
) -> GetCountriesPayload:
    session = get_session(info)
    countries = await country_stmt.get_countries(session=session)
    return GetCountriesPayload(
        countries=countries, severErrors=[]  # type: ignore
    )


async def get_country_by_name(
    country_name: str, info: Info[ContextType, RootValueType]
) -> GetCountryPayload:
    session = get_session(info)
    country = await country_stmt.get_country_by_name(
        session=session, country_name=country_name
    )
    if country is None:
        return GetCountryPayload(country=None, severErrors=[])
    return GetCountryPayload(country=country, severErrors=[])  # type: ignore
