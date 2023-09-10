import pytest
from fastapi.testclient import TestClient

from src.api.main import app, schema

client = TestClient(app)


@pytest.mark.asyncio
async def test_hello() -> None:
    query = """
        query {
            hello
        }
    """

    resp = await schema.execute(query=query)
    assert resp.errors is None and resp.data is not None
    assert resp.data["hello"] == "Hello World"
