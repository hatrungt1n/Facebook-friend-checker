# src/logger.py
from datetime import datetime
from src.config import LOG_FILE

class EventLogger:
    """Handles logging unfriend events."""

    @staticmethod
    def log_event(friend):
        with open(LOG_FILE, "a") as log_file:
            log_file.write(f"{datetime.now()}: {friend} unfriended you.\n")
