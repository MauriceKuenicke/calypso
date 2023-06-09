"""init

Revision ID: 7c9b0157d51a
Revises:
Create Date: 2023-04-15 18:28:55.199180

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "7c9b0157d51a"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
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
            "id", sa.String(), nullable=False, comment="User identification string"
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
            comment="Timestamp of user creation",
        ),
        sa.Column(
            "last_login",
            sa.DateTime(timezone=True),
            nullable=True,
            comment="Last login timestamp",
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=True,
            comment="Timestamp of user last update",
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
        sa.UniqueConstraint("username"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("user")
    # ### end Alembic commands ###
