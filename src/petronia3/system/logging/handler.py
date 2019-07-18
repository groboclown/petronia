
"""
Handles a specific log message.
"""

from typing import Callable, NewType
from .level import LogLevel

LogHandler = Callable[[LogLevel, str, str], None]

LogHandlerId = NewType('LogHandlerId', int)
