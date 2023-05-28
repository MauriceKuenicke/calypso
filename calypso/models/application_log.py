from sqlalchemy import Boolean, Column, String, Float

from .base_class import Base
from .mixins import CreatedAtMixin, UUIDMixin


class ApplicationLogBase:
    """Base log model class."""

    info = Column(
        String(length=255), nullable=False, comment="Logged information", unique=False
    )
    level = Column(String(length=20), nullable=False, comment="Log level", unique=False)
    module = Column(
        String(length=255), nullable=True, comment="Module Information", unique=False
    )
    request_identifier = Column(
        String(length=100),
        nullable=True,
        comment="Identifier of the request",
        unique=False,
    )


class ApplicationLog(Base, ApplicationLogBase, UUIDMixin, CreatedAtMixin):
    """Table for the application log data."""

    __tablename__ = "application_log"

    def __repr__(self) -> str:
        """Return the string representation of the log instance."""
        return (
            "<ApplicationLog(id='%s', level='%s', request_id='%s', info='%s', created_at='%s')>"  # noqa: E501
            % (self.id, self.level, self.request_id, self.info, self.created_at)
        )
