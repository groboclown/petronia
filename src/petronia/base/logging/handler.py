
"""
Handles a specific log message.
"""

from typing import Callable, NewType, Optional
from .level import LogLevel

LogHandler = Callable[[LogLevel, str, str, Optional[BaseException]], None]

LogHandlerId = NewType('LogHandlerId', int)
