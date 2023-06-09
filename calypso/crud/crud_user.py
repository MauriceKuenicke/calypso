from typing import Optional, Type

from calypso.models import User
from calypso.modules.logger import CalypsoLogger
from fastapi.exceptions import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session


class CRUDUser:
    """CRUD Implementation for the User Model."""

    def __init__(self, model: Type[User], idem: Optional[str] = "0000000000") -> None:
        """Initialize the CRUDUser instance."""
        self.model = model
        self.idem = idem

    def _throw_HTTP_Exception_if_user_already_exists(
        self, db: Session, user: User
    ) -> None:
        """Throws an HTTP exception if user already exists.

        Args:
            db (Session): Database Session
            user (User): New user instance.

        """
        error_code = 409
        error_text = "Username already exists."

        result = self.find_by_name(db=db, username=user.username)
        if result:
            CalypsoLogger.info(
                "Found duplicate entry during user creation: %s",
                result,
                extra={"idem": self.idem, "mod": __name__},
            )
            raise HTTPException(status_code=error_code, detail=error_text)
        return None

    def create(self, db: Session, user: User) -> User:
        """Create a new user entry in the database.

        Args:
            db (Session): Database Session to use.
            user (User): User object to be persisted.
            idem (str): Request Identifier string.

        Returns:
            User: Created User

        """
        self._throw_HTTP_Exception_if_user_already_exists(db=db, user=user)

        db.add(user)
        db.commit()
        CalypsoLogger.info(
            "Successfully registered new user: %s",
            user.username,
            extra={"idem": self.idem, "mod": __name__},
        )
        return user

    def find_by_name(self, db: Session, username: Optional[str]) -> Optional[User]:
        """Query a user from the database based on their username.

        Args:
            db (Session): Database Session tu use.
            username (str): Username to search for.

        Returns:
            Optional(User): User object from the database.

        """
        if not username:
            return None
        stmnt = select(User).where(User.username == username)
        result = db.execute(stmnt).scalar_one_or_none()
        if result:
            return result
        else:
            return None
