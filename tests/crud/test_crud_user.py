import pytest
from calypso.crud import CRUDUser
from calypso.models import User
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from tests.utils import UserFactory


def test_user_creation_is_successfull(db: Session) -> None:
    """Creation of user is successfull."""
    crud_user = CRUDUser(User)

    test_user: User = UserFactory.generate_random_user()
    new_user = crud_user.create(db=db, user=test_user)
    assert new_user == test_user
    assert isinstance(new_user.__repr__(), str)


def test_duplicate_user_creation_throws_error(db: Session) -> None:
    """Creating a user that already exists should throw an error."""
    duplicate_name = "Spiderman"
    crud_user = CRUDUser(User)

    existing_user: User = UserFactory.store_random_user_in_db(
        db=db, username=duplicate_name
    )

    with pytest.raises(HTTPException) as exception:
        crud_user.create(db=db, user=existing_user)

    assert exception.value.status_code == 409


def test_find_user_by_name_none_input(db: Session) -> None:
    """Test the None-input behaviour for usernames."""
    crud_user = CRUDUser(User)
    assert not crud_user.find_by_name(db, username=None)
