from typing import TypeVar

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import expression as sql
from strawberry.types import Info

from src.api.types import City, Country, CountryWithCities
from src.database.models import Country as _Country
from src.libs.supabase.client import supabase_client


async def get_country() -> list[Country]:
    try:
        result = supabase_client.table("countries").select("*").execute()
        return [Country(**country) for country in result.data]
    except Exception:
        return []


async def get_countries() -> list[Country]:
    try:
        result = supabase_client.table("countries").select("*").execute()
        return [Country(**country) for country in result.data]
    except Exception:
        return []


async def get_cities() -> list[City]:
    try:
        result = supabase_client.table("cities").select("*").execute()
        return [City(**city) for city in result.data]
    except Exception:
        return []


async def get_country_with_cities() -> list[CountryWithCities]:
    try:
        result = (
            supabase_client.table("countries").select("*, cities(*)").execute()
        )
        return [
            CountryWithCities(
                country=Country(
                    country_id=row["country_id"],
                    country_name=row["country_name"],
                ),
                cities=[City(**city) for city in row["cities"]],
            )
            for row in result.data
        ]
    except Exception:
        return []


RootValueType = TypeVar("RootValueType")


def get_session(
    info: Info[dict[str, AsyncSession], RootValueType]
) -> AsyncSession:
    session = info.context.get("session")
    if session is None:
        raise ValueError("Session not found in context.")
    return session


async def get_hoge(
    info: Info[dict[str, AsyncSession], RootValueType]
) -> list[Country]:
    session = get_session(info)
    query = sql.select(_Country).where(_Country.country_id == 1)
    countries = await session.execute(query)
    country = countries.scalars().first()
    if country is None:
        return []
    return [
        Country(
            country_id=country.country_id, country_name=country.country_name
        )
    ]
