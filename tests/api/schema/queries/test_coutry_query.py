import pytest
from httpx import AsyncClient

from src.database.session_manager import DatabaseSessionManager
from tests.api.schema.queries.country_query import (
    countries_query,
    country_by_name_query,
)


@pytest.mark.asyncio
async def test_countries(
    async_client: AsyncClient, session: DatabaseSessionManager
) -> None:
    query, expected = countries_query()
    resp = await async_client.post(
        "/graphql",
        json={
            "query": query,
        },
    )
    assert resp.status_code == 200
    actual = resp.json()
    assert actual == expected


@pytest.mark.asyncio
async def test_country_by_name(
    async_client: AsyncClient, session: DatabaseSessionManager
) -> None:
    query, expected = country_by_name_query()
    resp = await async_client.post(
        "/graphql",
        json={
            "query": query,
        },
    )
    assert resp.status_code == 200
    actual = resp.json()
    assert actual == expected
