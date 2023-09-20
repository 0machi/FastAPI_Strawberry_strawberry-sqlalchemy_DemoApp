import pytest

from src.api.resolvers.stmts import (
    get_cities,
    get_countries,
    get_country_by_name,
)
from src.database.db import db
from tests.seed import cities as expected_cities
from tests.seed import countries as expected_coutries
from tests.seed import us


@pytest.mark.asyncio
async def test_get_countries(init_db: None) -> None:
    db.connect()
    if db.session is None:
        raise ValueError("session not found.")
    async with db.session() as session:
        actual = await get_countries(session=session)
        assert actual == expected_coutries


@pytest.mark.asyncio
async def test_get_cities(init_db: None) -> None:
    db.connect()
    if db.session is None:
        raise ValueError("session not found.")
    async with db.session() as session:
        actual = await get_cities(session=session)
        assert actual == expected_cities


@pytest.mark.asyncio
async def test_get_country_by_name(init_db: None) -> None:
    db.connect()
    if db.session is None:
        raise ValueError("session not found.")
    async with db.session() as session:
        actual = await get_country_by_name(session=session, country_name="US")
        assert actual == us
