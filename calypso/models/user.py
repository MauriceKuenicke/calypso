from sqlalchemy import Boolean, Column, DateTime, String

from .base_class import Base
from .mixins import CreatedAtMixin, UUIDMixin, UpdatedAtMixin


class UserBase:
    """Base user class."""

    username = Column(
        String(length=255), nullable=False, comment="Username", unique=True
    )
    password = Column(String(length=100), nullable=False, comment="User Password Hash")
    is_admin = Column(Boolean, nullable=False, comment="User is Admin", default=False)


class User(Base, UserBase, UUIDMixin, CreatedAtMixin, UpdatedAtMixin):
    """Table user class."""

    __tablename__ = "user"

    last_login = Column(
        DateTime(timezone=True),
        nullable=True,
        comment="Last login timestamp",
    )

    def __repr__(self) -> str:
        """Return the string representation of the user instance."""
        return (
            "<User(id='%s', username='%s', is_admin='%s', created_at='%s', last_login='%s')>"  # noqa: E501
            % (self.id, self.username, self.is_admin, self.created_at, self.last_login)
        )
