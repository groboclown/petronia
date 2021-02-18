"""
Debug Stuff.
"""

from typing import Any
import sys
import threading


_LOCK = threading.RLock()


LOG_TRACE = True
LOG_DEBUG = True
LOG_INFO = True


def low_print(message: str) -> None:
    """Low-level, raw printing."""
    with _LOCK:
        sys.stdout.write(message + '\n')
        sys.stdout.flush()


def info(message_text: str, **kwargs: Any) -> None:
    """Info level logging"""
    if LOG_INFO:
        low_print('[Native INFO] ' + (message_text.format(**kwargs)))


def debug(message_text: str, **kwargs: Any) -> None:
    """Debug level logging"""
    if LOG_DEBUG:
        low_print('[Native DEBUG] ' + (message_text.format(**kwargs)))


def trace(message_text: str, **kwargs: Any) -> None:
    """Trace level logging"""
    if LOG_TRACE:
        low_print('[Native TRACE] ' + (message_text.format(**kwargs)))


def error(message_text: str, **kwargs: Any) -> None:
    """Log an error message."""
    low_print('[Native ERROR] ' + (message_text.format(**kwargs)))
