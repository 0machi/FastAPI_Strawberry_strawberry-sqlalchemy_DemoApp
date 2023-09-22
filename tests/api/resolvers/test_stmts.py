import pytest

from src.api.resolvers.stmts import (
    add_country,
    delete_country,
    get_cities,
    get_countries,
    get_country_by_name,
    update_country,
)
from src.database.models import Country
from src.database.session_manager import DatabaseSessionManager
from tests.seed import cities as expected_cities
from tests.seed import countries as expected_coutries
from tests.seed import us


@pytest.mark.asyncio
async def test_get_countries(session: DatabaseSessionManager) -> None:
    async with session.session() as s:
        actual = await get_countries(session=s)
        assert actual == expected_coutries


@pytest.mark.asyncio
async def test_get_cities(session: DatabaseSessionManager) -> None:
    async with session.session() as s:
        actual = await get_cities(session=s)
        assert actual == expected_cities


@pytest.mark.asyncio
async def test_get_country_by_name(session: DatabaseSessionManager) -> None:
    async with session.session() as s:
        actual = await get_country_by_name(session=s, country_name="US")
        assert actual == us


@pytest.mark.asyncio
async def test_add_country(session: DatabaseSessionManager) -> None:
    async with session.session() as s:
        country_id = 4
        country_name = "Switzerland"
        expected = (country_id, country_name)
        actual = await add_country(
            session=s,
            country=Country(
                country_id=country_id, country_name=country_name, cities=[]
            ),
        )
        assert actual == expected


@pytest.mark.asyncio
async def test_update_country(session: DatabaseSessionManager) -> None:
    async with session.session() as s:
        country_id = 3
        old_country_name = "Japan"
        new_country_name = "JP"
        expected = (country_id, new_country_name)
        actual = await update_country(
            session=s,
            old_country_name=old_country_name,
            new_country_name=new_country_name,
        )
        assert actual == expected


@pytest.mark.asyncio
async def test_delete_country(session: DatabaseSessionManager) -> None:
    async with session.session() as s:
        country_id = 3
        country_name = "Japan"
        expected = (country_id, country_name)
        actual = await delete_country(session=s, country_name=country_name)
        assert actual == expected
