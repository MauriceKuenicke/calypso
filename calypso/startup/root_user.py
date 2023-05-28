from calypso.crud import CRUDUser
from calypso.models import User
from calypso.modules import crypto
import calypso.modules.logger as logger
from sqlalchemy.orm import Session


def get_root_user() -> User:
    """Return the default root user."""
    password_hashed: str = crypto.encrypt_password("admin")
    username: str = "admin"
    return User(username=username, password=password_hashed, is_admin=True)


def add_root_user_if_not_exist(db: Session, root_user: User) -> None:
    """Create the root user object if it is not available in the database already.

    Args:
        db (Session): Database Session to use.
        root_user (User): Root User object to be persisted.

    """
    crud_user = CRUDUser(User)
    if not crud_user.find_by_name(db=db, username=root_user.username):
        user: User = crud_user.create(db=db, user=root_user)
        logger.CalypsoLogger.info(
            info=f"Root user '{user.username}' successfully created.",
            idem="STARTUP",
            module=__name__,
        )
