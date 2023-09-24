import pytest
from httpx import AsyncClient
from starlette.requests import Headers

from src.database.session_manager import DatabaseSessionManager
from tests.api.schema.queries.country_query import (
    countries_query,
    country_by_name_query,
)


@pytest.mark.asyncio
async def test_countries(
    async_client: AsyncClient, session: DatabaseSessionManager, token: str
) -> None:
    query, expected = countries_query()
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


@pytest.mark.asyncio
async def test_country_by_name(
    async_client: AsyncClient, session: DatabaseSessionManager, token: str
) -> None:
    query, expected = country_by_name_query()
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
