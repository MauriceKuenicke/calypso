import os

from starlette.config import Config

config = Config(".env")


DATABASE_HOSTNAME = config("DATABASE_HOSTNAME", default="localhost")
DATABASE_USER = config("DATABASE_USER", default="admin")
DATABASE_PASSWORD = config("DATABASE_PASSWORD", default="admin")
DATABASE_PORT = config("DATABASE_PORT", default="5432")
DATABASE_NAME = config("DATABASE_NAME", default="calypso")


SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOSTNAME}:{DATABASE_PORT}/{DATABASE_NAME}"  # noqa: E501


ENV = config("ENV", default="local")
DEFAULT_STATIC_DIR = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    os.path.join("static", "calypso", "dist"),
)
