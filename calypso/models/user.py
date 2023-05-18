import uuid

from sqlalchemy import Boolean, Column, DateTime, String
from sqlalchemy.sql import func

from .base_class import Base


def gen_uuid_string() -> str:
    """Generate the string representation of a UUID.

    Returns:
        string

    """
    return str(uuid.uuid4())


class UserBase:
    """Base user class."""

    username = Column(
        String(length=255), nullable=False, comment="Username", unique=True
    )
    password = Column(String(length=100), nullable=False, comment="User Password Hash")
    is_admin = Column(Boolean, nullable=False, comment="User is Admin", default=False)


class User(Base, UserBase):
    """Table user class."""

    __tablename__ = "user"

    # This is not really performant since Postgres supports the uuid type.
    # However SQLite doesn't which breaks the tests.
    id = Column(
        String,
        nullable=False,
        comment="User identification string",
        primary_key=True,
        default=gen_uuid_string,
        unique=True,
    )
    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        comment="Timestamp of user creation",
        server_default=func.now(),
    )
    last_login = Column(
        DateTime(timezone=True),
        nullable=True,
        comment="Last login timestamp",
    )
    updated_at = Column(
        DateTime(timezone=True),
        comment="Timestamp of user last update",
        onupdate=func.now(),
    )

    def __repr__(self) -> str:
        """Return the string representation of the user instance."""
        return (
            "<User(id='%s', username='%s', is_admin='%s', created_at='%s', last_login='%s')>"  # noqa: E501
            % (self.id, self.username, self.is_admin, self.created_at, self.last_login)
        )
