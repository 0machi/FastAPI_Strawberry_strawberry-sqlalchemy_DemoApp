import pytest
from httpx import AsyncClient

from src.database.db import DatabaseSessionManager
from tests.api.schema.query import (
    cities_query,
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
async def test_cities(
    async_client: AsyncClient, session: DatabaseSessionManager
) -> None:
    query, expected = cities_query()
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
