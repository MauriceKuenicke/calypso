from calypso.config import SQLALCHEMY_DATABASE_URI  # pragma: no cover
from sqlalchemy import create_engine  # pragma: no cover
from sqlalchemy.orm import sessionmaker  # pragma: no cover

# pragma: no cover
engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    pool_pre_ping=True,
)  # pragma: no cover

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)  # pragma: no cover
