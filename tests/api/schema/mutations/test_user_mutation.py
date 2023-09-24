import pytest
from httpx import AsyncClient

from src.database.session_manager import DatabaseSessionManager
from tests.api.schema.mutations.user_mutation import login_mutation


@pytest.mark.asyncio
async def test_add_country(
    async_client: AsyncClient, session: DatabaseSessionManager
) -> None:
    mutation, expected = login_mutation()
    resp = await async_client.post(
        "/graphql",
        json={
            "query": mutation,
        },
    )
    assert resp.status_code == 200
    actual = resp.json()
    assert (
        actual["data"]["login"]["tokenType"]
        == expected["data"]["login"]["tokenType"]
    )
    assert (
        actual["data"]["login"]["severErrors"]
        == expected["data"]["login"]["severErrors"]
    )
