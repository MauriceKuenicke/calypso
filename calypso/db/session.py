from sqlalchemy import create_engine  # pragma: no cover
from sqlalchemy.orm import sessionmaker  # pragma: no cover

# pragma: no cover
engine = create_engine(
    "postgresql+psycopg2://postgres:postgrespw@localhost:49154/postgres",
    pool_pre_ping=True,
)  # pragma: no cover

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)  # pragma: no cover
