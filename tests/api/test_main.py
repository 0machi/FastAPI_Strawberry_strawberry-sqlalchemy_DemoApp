from fastapi.testclient import TestClient
from httpx._models import Response

from src.api.main import app

client = TestClient(app)


def test_hello() -> None:
    response: Response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
