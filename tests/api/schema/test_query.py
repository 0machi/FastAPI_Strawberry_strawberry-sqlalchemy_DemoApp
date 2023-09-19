import pytest
from httpx import AsyncClient

from tests.api.schema.query import (
    cities_query,
    countries_query,
    country_by_name_query,
)


@pytest.mark.asyncio
async def test_countries(init_db: None, async_client: AsyncClient) -> None:
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
async def test_cities(init_db: None, async_client: AsyncClient) -> None:
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
    init_db: None, async_client: AsyncClient
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
