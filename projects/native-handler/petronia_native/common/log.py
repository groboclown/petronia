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


def info(msg: str, **kwargs: Any) -> None:
    """Info level logging"""
    if LOG_INFO:
        low_print('[Native INFO] ' + (msg.format(**kwargs)))


def debug(msg: str, **kwargs: Any) -> None:
    """Debug level logging"""
    if LOG_DEBUG:
        low_print('[Native DEBUG] ' + (msg.format(**kwargs)))


def trace(msg: str, **kwargs: Any) -> None:
    """Trace level logging"""
    if LOG_TRACE:
        low_print('[Native TRACE] ' + (msg.format(**kwargs)))


def error(msg: str, **kwargs: Any) -> None:
    """Log an error message."""
    low_print('[Native ERROR] ' + (msg.format(**kwargs)))
