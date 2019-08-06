
"""
Definition for the "log" entrypoint.

Logging is as flat and simple as possible.  Other things can add layers to it,
or it itself could be a wrapper on top of other components, but the entrypoint
for usage is trivially simple.
"""

from typing import NewType

LogLevel = NewType('LogLevel', int)

TRACE = LogLevel(0)
DEBUG = LogLevel(1)
VERBOSE = LogLevel(2)
INFO = LogLevel(3)
NOTICE = LogLevel(4)
WARN = LogLevel(5)
DEPRECATED = LogLevel(6)
ERROR = LogLevel(7)
FATAL = LogLevel(8)
