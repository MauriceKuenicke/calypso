from fastapi.testclient import TestClient
from calypso.main import app


def test_successfull_healthcheck() -> None:
    """Test successfull Healthcheck."""
    client = TestClient(app)
    response = client.get("/healthcheck")
    assert response.status_code == 200
