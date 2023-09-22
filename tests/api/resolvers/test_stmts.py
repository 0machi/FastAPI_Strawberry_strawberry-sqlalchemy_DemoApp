import pytest

from src.api.resolvers.stmts import (
    add_country,
    get_cities,
    get_countries,
    get_country_by_name,
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
        expected = (3, "Japan")
        actual = await add_country(
            session=s,
            country=Country(country_id=3, country_name="Japan", cities=[]),
        )
        assert actual == expected
