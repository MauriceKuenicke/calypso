import logging
import logging.handlers
import os
import time

from dotenv import load_dotenv

load_dotenv()

LOG_PATH = "calypso/logs/app.log"
NR_BACKUPS = 7
LOGLEVEL = os.getenv("LOGLEVEL", "INFO").upper()


def get_logger(name: str, filename: str, level: str) -> logging.Logger:
    """Return a new logger instance.

    Args:
        name(str): The name of the logger.
        filename(str): The name of the output file for the logger.
        level(str): The logging level for the logger.

    Returns:
        logging.Logger: A logger object with the specified name,
        logging level, and output file.

    """
    logging.Formatter.converter = time.gmtime
    formatter = logging.Formatter(
        "%(asctime)s - %(mod)s - %(levelname)s - [%(idem)s] - %(message)s",
        "%Y-%m-%d %H:%M:%S",
    )
    log_handler = logging.handlers.TimedRotatingFileHandler(
        filename=filename, when="S", interval=10, backupCount=NR_BACKUPS, utc=True
    )
    log_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(log_handler)

    return logger


CalypsoLogger = get_logger("CalypsoLogger", filename=LOG_PATH, level=LOGLEVEL)
