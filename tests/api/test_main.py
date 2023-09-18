import pytest

from src.api.schema.schema import schema


@pytest.mark.asyncio
async def test_hello(setup_app: None) -> None:
    query = """
        query {
            hello
        }
    """

    resp = await schema.execute(query=query)
    assert resp.errors is None and resp.data is not None
    assert resp.data["hello"] == "Hello World"
