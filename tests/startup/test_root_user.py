from calypso.crud import CRUDUser
from calypso.models import User
from calypso.startup import add_root_user_if_not_exist, get_root_user
from sqlalchemy.orm import Session


def test_root_user_successfully_created(db: Session) -> None:
    """Creation of root user is successfull."""
    test_root_user: User = User(
        username="Testadmin", password="TopSecretPasswordHash", is_admin=True
    )
    crud_user = CRUDUser(User)
    assert not crud_user.find_by_name(db=db, username=test_root_user.username)
    add_root_user_if_not_exist(db=db, root_user=test_root_user)
    db_user: User = crud_user.find_by_name(db=db, username=test_root_user.username)  # type: ignore # noqa: E501
    assert db_user.id == test_root_user.id
    assert db_user.username == test_root_user.username


def test_cant_create_duplicate_root_users(db: Session) -> None:
    """Test creating multiple root user objects."""
    test_root_user: User = User(
        username="Testadmin", password="TopSecretPasswordHash", is_admin=True
    )
    crud_user = CRUDUser(User)
    add_root_user_if_not_exist(db=db, root_user=test_root_user)
    add_root_user_if_not_exist(db=db, root_user=test_root_user)
    add_root_user_if_not_exist(db=db, root_user=test_root_user)
    db_user: User = crud_user.find_by_name(db=db, username=test_root_user.username)  # type: ignore # noqa: E501
    assert db_user.id == test_root_user.id


def test_get_default_root_user() -> None:
    """Test getting the default root user object."""
    user: User = get_root_user()
    assert user.username == "admin"
    assert user.is_admin
