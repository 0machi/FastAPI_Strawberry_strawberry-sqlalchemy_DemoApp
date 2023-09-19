import pytest

from src.api.resolvers.stmts import get_countries
from src.database.db import db
from tests.seed import countries as expected_coutries


@pytest.mark.asyncio
async def test_get_countries(init_db: None) -> None:
    db.connect()
    if db.session is None:
        raise ValueError("session not found.")
    async with db.session() as session:
        actual = await get_countries(session=session)
        assert actual == expected_coutries