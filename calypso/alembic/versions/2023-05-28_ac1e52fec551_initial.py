"""initial

Revision ID: ac1e52fec551
Revises: 
Create Date: 2023-05-28 22:07:17.609626

"""
from alembic import op
import sqlalchemy as sa


revision = "ac1e52fec551"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "application_log",
        sa.Column(
            "info", sa.String(length=255), nullable=False, comment="Logged information"
        ),
        sa.Column("level", sa.String(length=20), nullable=False, comment="Log level"),
        sa.Column(
            "module", sa.String(length=255), nullable=True, comment="Module Information"
        ),
        sa.Column(
            "request_identifier",
            sa.String(length=100),
            nullable=True,
            comment="Identifier of the request",
        ),
        sa.Column(
            "id", sa.String(), nullable=False, comment="Unique identification string"
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
            comment="Timestamp of creation",
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    op.create_table(
        "request_log",
        sa.Column(
            "request_type",
            sa.String(length=20),
            nullable=False,
            comment="HTTP request method.",
        ),
        sa.Column(
            "path", sa.String(length=510), nullable=False, comment="HTTP request path."
        ),
        sa.Column(
            "response_time_ms",
            sa.Float(),
            nullable=False,
            comment="Response time in ms.",
        ),
        sa.Column(
            "status_code", sa.Integer(), nullable=False, comment="Response status code."
        ),
        sa.Column(
            "request_identifier",
            sa.String(length=20),
            nullable=True,
            comment="Identifier of the request",
        ),
        sa.Column(
            "id", sa.String(), nullable=False, comment="Unique identification string"
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
            comment="Timestamp of creation",
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    op.create_table(
        "user",
        sa.Column(
            "last_login",
            sa.DateTime(timezone=True),
            nullable=True,
            comment="Last login timestamp",
        ),
        sa.Column(
            "username", sa.String(length=255), nullable=False, comment="Username"
        ),
        sa.Column(
            "password",
            sa.String(length=100),
            nullable=False,
            comment="User Password Hash",
        ),
        sa.Column("is_admin", sa.Boolean(), nullable=False, comment="User is Admin"),
        sa.Column(
            "id", sa.String(), nullable=False, comment="Unique identification string"
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
            comment="Timestamp of creation",
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=True,
            comment="Timestamp of last update",
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
        sa.UniqueConstraint("username"),
    )


def downgrade() -> None:
    op.drop_table("user")
    op.drop_table("request_log")
    op.drop_table("application_log")
