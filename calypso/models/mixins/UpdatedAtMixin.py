from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func


class UpdatedAtMixin:
    updated_at = Column(
        DateTime(timezone=True),
        comment="Timestamp of last update",
        onupdate=func.now(),
    )
