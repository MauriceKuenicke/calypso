import uuid

from sqlalchemy import Boolean, Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from .base_class import Base


class UserBase:
    """Base user class."""

    username = Column(String(length=255), nullable=False, comment="Username")
    password = Column(String(length=100), nullable=False, comment="User Password Hash")
    is_admin = Column(Boolean, nullable=False, comment="User is Admin", default=False)


class User(Base, UserBase):  # type: ignore
    """Table user class."""

    __tablename__ = "user"

    id = Column(
        UUID(as_uuid=True),
        nullable=False,
        comment="User identification string",
        primary_key=True,
        default=uuid.uuid4,
    )
    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        comment="Timestamp of user creation",
        server_default=func.now(),
    )
    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        comment="Timestamp of user last update",
        onupdate=func.now(),
    )

    def __repr__(self) -> str:
        """Return the string representation of the user instance."""
        return "<User(username='%s', is_admin='%s')>" % (self.username, self.is_admin)


class UserCreate(UserBase):
    """User model class containing the necessary fields to create a User."""

    pass
