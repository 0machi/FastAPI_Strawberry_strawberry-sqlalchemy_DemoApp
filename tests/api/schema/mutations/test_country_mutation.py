import pytest
from httpx import AsyncClient
from starlette.requests import Headers

from src.database.session_manager import DatabaseSessionManager
from tests.api.schema.mutations.coutry_mutation import (
    add_country_mutation,
    delete_country_mutation,
    update_country_mutation,
)


@pytest.mark.asyncio
async def test_add_country(
    async_client: AsyncClient, session: DatabaseSessionManager, token: str
) -> None:
    mutation, expected = add_country_mutation()
    resp = await async_client.post(
        "/graphql",
        json={
            "query": mutation,
        },
        headers=Headers(headers={"Authorization": f"Bearer {token}"}),
    )
    assert resp.status_code == 200
    actual = resp.json()
    assert actual == expected


@pytest.mark.asyncio
async def test_update_country(
    async_client: AsyncClient, session: DatabaseSessionManager, token: str
) -> None:
    mutation, expected = update_country_mutation()
    resp = await async_client.post(
        "/graphql",
        json={
            "query": mutation,
        },
        headers=Headers(headers={"Authorization": f"Bearer {token}"}),
    )
    assert resp.status_code == 200
    actual = resp.json()
    assert actual == expected


@pytest.mark.asyncio
async def test_delete_country(
    async_client: AsyncClient, session: DatabaseSessionManager, token: str
) -> None:
    mutation, expected = delete_country_mutation()
    resp = await async_client.post(
        "/graphql",
        json={
            "query": mutation,
        },
        headers=Headers(headers={"Authorization": f"Bearer {token}"}),
    )
    assert resp.status_code == 200
    actual = resp.json()
    assert actual == expected
