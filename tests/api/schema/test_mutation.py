import pytest
from httpx import AsyncClient

from src.database.session_manager import DatabaseSessionManager
from tests.api.schema.mutation import (
    add_country_mutation,
    delete_country_mutation,
    update_country_mutation,
)


@pytest.mark.asyncio
async def test_add_country(
    async_client: AsyncClient, session: DatabaseSessionManager
) -> None:
    mutation, expected = add_country_mutation()
    resp = await async_client.post(
        "/graphql",
        json={
            "query": mutation,
        },
    )
    assert resp.status_code == 200
    actual = resp.json()
    assert actual == expected


@pytest.mark.asyncio
async def test_update_country(
    async_client: AsyncClient, session: DatabaseSessionManager
) -> None:
    mutation, expected = update_country_mutation()
    resp = await async_client.post(
        "/graphql",
        json={
            "query": mutation,
        },
    )
    assert resp.status_code == 200
    actual = resp.json()
    assert actual == expected


@pytest.mark.asyncio
async def test_delete_country(
    async_client: AsyncClient, session: DatabaseSessionManager
) -> None:
    mutation, expected = delete_country_mutation()
    resp = await async_client.post(
        "/graphql",
        json={
            "query": mutation,
        },
    )
    assert resp.status_code == 200
    actual = resp.json()
    assert actual == expected
