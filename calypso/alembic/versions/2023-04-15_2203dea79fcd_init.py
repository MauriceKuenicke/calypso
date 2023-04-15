"""Initial Database Model

Revision ID: 2203dea79fcd
Revises:
Create Date: 2023-04-15 15:38:50.146395

"""
import sqlalchemy as sa
from alembic import op

revision = "2203dea79fcd"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column(
            "id", sa.UUID(), nullable=False, comment="User identification string"
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
            comment="Timestamp of user creation",
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            comment="Timestamp of user last update",
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
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("user")
