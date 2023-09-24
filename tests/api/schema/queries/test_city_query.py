import pytest
from httpx import AsyncClient
from starlette.requests import Headers

from src.database.session_manager import DatabaseSessionManager
from tests.api.schema.queries.city_query import cities_query


@pytest.mark.asyncio
async def test_cities(
    async_client: AsyncClient, session: DatabaseSessionManager, token: str
) -> None:
    query, expected = cities_query()
    resp = await async_client.post(
        "/graphql",
        json={
            "query": query,
        },
        headers=Headers(headers={"Authorization": f"Bearer {token}"}),
    )
    assert resp.status_code == 200
    actual = resp.json()
    assert actual == expected
