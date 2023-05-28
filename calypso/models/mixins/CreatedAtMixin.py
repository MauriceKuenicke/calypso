from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func


class CreatedAtMixin:
    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        comment="Timestamp of creation",
        server_default=func.now(),
    )
