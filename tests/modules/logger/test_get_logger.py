import logging
import pytest
from calypso.modules.logger.get_logger import get_logger
from typing import Any


@pytest.fixture
def mock_timed_rotating_file_handler(mocker: Any) -> Any:
    """Return mocked TimedRotatingFileHandler."""
    return mocker.patch("logging.handlers.TimedRotatingFileHandler")


def test_get_logger_returns_logger_object() -> None:
    """Test correct return type."""
    logger = get_logger("test_logger", "test.log", "DEBUG")
    assert isinstance(logger, logging.Logger)


def test_get_logger_sets_logger_level() -> None:
    """Test correct loglevel."""
    logger = get_logger("test_logger", "test.log", "DEBUG")
    assert logger.level == logging.DEBUG
