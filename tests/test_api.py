from fastapi.testclient import TestClient

from api.app.main import app


def test_health() -> None:
    client = TestClient(app)
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_list_assets() -> None:
    client = TestClient(app)
    response = client.get("/assets")

    assert response.status_code == 200
    assert response.json()[0]["ip_address"] == "127.0.0.1"
