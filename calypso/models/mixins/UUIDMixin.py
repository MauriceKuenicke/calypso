from sqlalchemy import Column, String
from ..helper import gen_uuid_string


class UUIDMixin:
    # This is not really performant since Postgres supports the uuid type.
    # However SQLite doesn't which breaks the tests.
    id = Column(
        String,
        nullable=False,
        comment="Unique identification string",
        primary_key=True,
        default=gen_uuid_string,
        unique=True,
    )
