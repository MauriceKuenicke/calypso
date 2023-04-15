from typing import Generator

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool


# Prepare in-memory-database for testing
# Every Test will receive its own empty database
@pytest.fixture(scope="function", name="db")
def setup_test_database() -> Generator[sessionmaker[Session], None, None]:
    """Create a in-memory SQLite database for testing."""
    engine = create_engine(
        "sqlite://",
        poolclass=StaticPool,
        connect_args={"check_same_thread": False},
        echo=False,
    )

    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    yield session
