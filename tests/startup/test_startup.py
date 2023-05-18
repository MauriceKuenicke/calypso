from typing import Any

from calypso.crud import CRUDUser
from calypso.main import initialize_root_user
from calypso.models import User
from sqlalchemy.orm import Session


def test_initialize_root_user_successfull(db: Session, monkeypatch: Any) -> None:
    """Test the root user initialization startup function."""
    test_root_user = User(username="admin", password="TopSecretHash", is_admin=True)
    mock_get_root_user = lambda: test_root_user  # noqa: E731

    mock_session = lambda: db  # noqa: E731

    monkeypatch.setattr("calypso.main.get_root_user", mock_get_root_user)
    monkeypatch.setattr("calypso.main.SessionLocal", mock_session)

    crud_user = CRUDUser(User)
    assert not crud_user.find_by_name(db=db, username=test_root_user.username)
    initialize_root_user()
    db_user = crud_user.find_by_name(db=db, username=test_root_user.username)
    assert db_user.id == test_root_user.id  # type: ignore
