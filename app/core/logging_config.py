import logging
import os
import sys
from typing import Final

def setup_logging() -> None:
    """
    Configure the root logger once.

    • Reads LOG_LEVEL env var (defaults to INFO).
    • Adds a single StreamHandler to stdout.
    • Uses a rich, one-line formatter.
    • Guard clause prevents double-configuration when
      Uvicorn or another framework already set handlers.
    """
    root = logging.getLogger()
    if root.handlers:                        # already configured
        return

    LOG_LEVEL: Final = os.getenv("LOG_LEVEL", "INFO").upper()

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(get_formatter())

    root.setLevel(LOG_LEVEL)
    root.addHandler(handler)

    logging.info(f"Log Level: {LOG_LEVEL}")

def get_formatter() -> logging.Formatter:
    """Consistent, detail-rich log line format."""
    return logging.Formatter(
        "%(levelname)s | "
        "%(asctime)s | "
        "%(process)d:%(thread)d | "
        "%(filename)s | "
        "%(funcName)s | "
        "%(lineno)d | "
        "%(message)s"
    )