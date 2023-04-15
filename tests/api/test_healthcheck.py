from calypso.main import app
from calypso.models import User
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session


def test_successfull_healthcheck() -> None:
    """Test successfull Healthcheck."""
    client = TestClient(app)
    response = client.get("/healthcheck")
    assert response.status_code == 200


# CURRENTLY ONLY FOR COVERAGE: REMOVE LATER
def test_models(db: Session) -> None:
    """Only here for coverage, remove later."""
    user = User()
    assert user
    assert db
    assert isinstance(user.__str__(), str)
