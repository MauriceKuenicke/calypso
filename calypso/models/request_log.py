from sqlalchemy import Boolean, Column, String, Float, Integer

from .base_class import Base
from .mixins import CreatedAtMixin, UUIDMixin


class RequestLogBase:
    """Base request log model class."""

    request_type = Column(
        String(length=20), nullable=False, comment="HTTP request method.", unique=False
    )

    path = Column(
        String(length=510), nullable=False, comment="HTTP request path.", unique=False
    )

    response_time_ms = Column(
        Float, nullable=False, comment="Response time in ms.", unique=False
    )

    status_code = Column(
        Integer, nullable=False, comment="Response status code.", unique=False
    )

    request_identifier = Column(
        String(length=20),
        nullable=True,
        comment="Identifier of the request",
        unique=False,
    )


class RequestLog(Base, RequestLogBase, UUIDMixin, CreatedAtMixin):
    """Table for the requests log data."""

    __tablename__ = "request_log"

    def __repr__(self) -> str:
        """Return the string representation of the log instance."""
        return (
            "<RequestLog(id='%s', request_type='%s', response_time='%s', status_code='%s', request_identifier='%s', created_at='%s')>"  # noqa: E501
            % (
                self.id,
                self.request_type,
                self.response_time,
                self.status_code,
                self.request_identifier,
                self.created_at,
            )
        )
