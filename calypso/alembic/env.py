from __future__ import with_statement

import os
from logging.config import fileConfig

from alembic import context
from calypso.models import Base  # noqa
from sqlalchemy import engine_from_config, pool

config = context.config
fileConfig(config.config_file_name)


target_metadata = Base.metadata


def get_url():
    user = os.getenv("POSTGRES_USER", "postgres")
    password = os.getenv("POSTGRES_PASSWORD", "postgrespw")
    server = os.getenv("POSTGRES_SERVER", "localhost:49154")
    db = os.getenv("POSTGRES_DB", "postgres")
    return f"postgresql://{user}:{password}@{server}/{db}"


def run_migrations_online():
    """Run migrations in 'online' mode.
    In this scenario we need to create an Engine
    and associate a connection with the context.
    """
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = get_url()
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata, compare_type=True
        )

        with context.begin_transaction():
            context.run_migrations()


run_migrations_online()
