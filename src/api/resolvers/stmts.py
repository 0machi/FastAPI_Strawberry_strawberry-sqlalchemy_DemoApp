from sqlalchemy import Row
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy.sql import expression as sql

from src.database.models import City, Country


async def get_countries(session: AsyncSession) -> list[Country]:
    query = sql.select(Country).options(selectinload(Country.cities))
    result = await session.execute(query)
    countries = result.scalars().all()
    return list(countries)


async def get_cities(session: AsyncSession) -> list[City]:
    query = sql.select(City)
    result = await session.execute(query)
    cities = result.scalars().all()
    return list(cities)


async def get_country_by_name(
    session: AsyncSession, country_name: str
) -> Country | None:
    query = (
        sql.select(Country)
        .where(Country.country_name == country_name)
        .options(selectinload(Country.cities))
    )
    result = await session.execute(query)
    country = result.scalars().first()
    return country


async def add_country(
    session: AsyncSession,
    country: Country,
) -> Row[tuple[int, str]] | None:
    query = (
        sql.insert(Country)
        .values(
            country_id=country.country_id, country_name=country.country_name
        )
        .returning(Country.country_id, Country.country_name)
    )
    result = await session.execute(query)
    await session.commit()
    added_country = result.first()
    return added_country


async def update_country(
    session: AsyncSession,
    old_country_name: str,
    new_country_name: str,
) -> Row[tuple[int, str]] | None:
    query = (
        sql.update(Country)
        .where(Country.country_name == old_country_name)
        .values(country_name=new_country_name)
        .returning(Country.country_id, Country.country_name)
    )
    result = await session.execute(query)
    await session.commit()
    updated_country = result.first()
    return updated_country


async def delete_country(
    session: AsyncSession,
    country_name: str,
) -> Row[tuple[int, str]] | None:
    query = (
        sql.delete(Country)
        .where(Country.country_name == country_name)
        .returning(Country.country_id, Country.country_name)
    )
    result = await session.execute(query)
    await session.commit()
    deleted_country = result.first()
    return deleted_country
