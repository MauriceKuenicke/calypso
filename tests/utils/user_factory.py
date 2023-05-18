from typing import Any, Optional

from calypso.models import User
from sqlalchemy.orm import Session
from tests.utils import random_bool, random_string, random_string_digits


class UserFactory:
    """Factory class responsible for the creation of User objects."""

    @classmethod
    def generate_random_user(
        cls,
        username: Optional[str] = None,
        password: Optional[str] = None,
        is_admin: Optional[bool] = None,
    ) -> User:
        """Generate a random User object.

        Args:
            username (str): Set specific username.
            Defaults to a randomly generated one.
            password (str): Set specific password hash.
            Defaults to a randomly generated one.
            is_admin (bool): Admin user flag. Defaults to a random bool.

        Returns:
            User

        """
        name: str = username or random_string()
        psw: str = password or random_string_digits(16)
        admin: bool = is_admin or random_bool()

        return User(username=name, password=psw, is_admin=admin)

    @classmethod
    def store_random_user_in_db(
        cls, db: Session, user: Optional[User] = None, **kwargs: Any
    ) -> User:
        """Generate and store a randomly generated user in the database.

        Args:
            db (Session): Database Session to user.
            user (Optional(User)): User object to store.
            A random user will be generated if none is given.

        Returns:
            User

        """
        new_user: User = user or cls.generate_random_user(**kwargs)
        db.add(new_user)
        db.commit()

        return new_user
