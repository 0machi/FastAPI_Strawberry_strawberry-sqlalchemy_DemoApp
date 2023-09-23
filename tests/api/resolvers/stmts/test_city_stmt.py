import pytest

from src.api.resolvers.stmts.city_stmt import get_cities
from src.database.session_manager import DatabaseSessionManager
from tests.seed import cities as expected_cities


@pytest.mark.asyncio
async def test_get_cities(session: DatabaseSessionManager) -> None:
    async with session.session() as s:
        actual = await get_cities(session=s)
        assert actual == expected_cities
