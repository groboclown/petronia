
# mypy: allow-any-expr
# mypy: allow-any-explicit

"""
Definition for the "log" entry point.

Logging is as flat and simple as possible.  Other things can add layers to it,
or it itself could be a wrapper on top of other components, but the entry point
for usage is trivially simple.
"""

from typing import Tuple, Dict, Optional, Any
from .level import LogLevel
from .handler import LogHandler, LogHandlerId
from ..util import RWLock

_HANDLERS: Dict[LogHandlerId, Tuple[LogLevel, str, LogHandler]] = {}
_HANDLER_COUNT = 0
_HANDLER_LOCK = RWLock()


# logging has global, static entry points, but that is the API.

def log(  # pylint: disable=dangerous-default-value
        level: LogLevel,
        src: Any,
        format_msg: str,
        *format_vargs: Any,
        **format_kvargs: Any
) -> None:
    """
    Send a log message to the logging sub-system.

    :param level: logging verbosity of the message.
    :param src: source that produced the message.
    :param format_msg: a Python format message string, using '{}' for parameters.
    :param format_vargs: `*varg` parameters for the format message.
    :param format_kvargs: `**kvarg` parameters for the format message.
    """
    src_str = _to_src_str(src)
    _HANDLER_LOCK.acquire_read()
    try:
        formatted: Optional[str] = None
        for min_level, src_starts_with, handler in _HANDLERS.values():
            if level >= min_level and src_str.startswith(src_starts_with):
                if not formatted:
                    formatted = format_msg.format(*format_vargs, **format_kvargs)
                handler(level, src_str, formatted, None)
    finally:
        _HANDLER_LOCK.release()


def logerr(  # pylint: disable=dangerous-default-value
        level: LogLevel,
        src: Any,
        err: BaseException,
        format_msg: str,
        *format_vargs: Any,
        **format_kvargs: Any
) -> None:
    """
    Send a log message to the logging sub-system that includes an error.

    :param level: logging verbosity of the message.
    :param src: source that produced the message.
    :param err: error to log
    :param format_msg: a Python format message string, using '{}' for parameters.
    :param format_vargs: `*varg` parameters for the format message.
    :param format_kvargs: `**kvarg` parameters for the format message.
    """
    src_str = _to_src_str(src)
    _HANDLER_LOCK.acquire_read()
    try:
        formatted: Optional[str] = None
        for min_level, src_starts_with, handler in _HANDLERS.values():
            if level >= min_level and src_str.startswith(src_starts_with):
                if not formatted:
                    formatted = format_msg.format(*format_vargs, **format_kvargs)
                handler(level, src_str, formatted, err)
    finally:
        _HANDLER_LOCK.release()


def add_log_handler(
        min_level: LogLevel,
        src_starts_with: str,
        handler: LogHandler
) -> LogHandlerId:
    """
    Registers a global handler for the log message.  Returnsa a handler ID for
    use when removing the log handler.  It is up to the caller to keep track
    of the handler ID for use of future removal.
    """
    global _HANDLER_COUNT  # pylint: disable=global-statement
    global _HANDLERS  # pylint: disable=global-statement
    _HANDLER_LOCK.acquire_write()
    try:
        handler_id = LogHandlerId(_HANDLER_COUNT)
        _HANDLER_COUNT += 1
        _HANDLERS[handler_id] = (min_level, src_starts_with, handler,)
        return handler_id
    finally:
        _HANDLER_LOCK.release()


def remove_log_handler(handler_id: LogHandlerId) -> None:
    """
    Removes the registered handler from listening on log messages.
    """
    _HANDLER_LOCK.acquire_write()
    try:
        if handler_id in _HANDLERS:
            del _HANDLERS[handler_id]
    finally:
        _HANDLER_LOCK.release()


def _to_src_str(src: Any) -> str:
    if hasattr(src, '__name__'):
        if hasattr(src, '__module__'):
            return str(src.__module__) + '.' + str(src.__name__)
        return str(src.__name__)
    return str(src)
