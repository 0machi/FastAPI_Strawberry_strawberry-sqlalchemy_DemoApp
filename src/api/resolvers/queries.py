from strawberry.types import Info

from src.api.context import ContextType, RootValueType, get_session
from src.api.resolvers import stmts
from src.api.types import (
    GetCitiesPayload,
    GetCountriesPayload,
    GetCountryPayload,
)


async def get_countries(
    info: Info[ContextType, RootValueType]
) -> GetCountriesPayload:
    session = get_session(info)
    countries = await stmts.get_countries(session=session)
    return GetCountriesPayload(
        countries=countries, severErrors=[]  # type: ignore
    )


async def get_cities(
    info: Info[ContextType, RootValueType]
) -> GetCitiesPayload:
    session = get_session(info)
    cities = await stmts.get_cities(session=session)
    return GetCitiesPayload(cities=cities, severErrors=[])  # type: ignore


async def get_country_by_name(
    country_name: str, info: Info[ContextType, RootValueType]
) -> GetCountryPayload:
    session = get_session(info)
    country = await stmts.get_country_by_name(
        session=session, country_name=country_name
    )
    if country is None:
        return GetCountryPayload(country=None, severErrors=[])
    return GetCountryPayload(country=country, severErrors=[])  # type: ignore
