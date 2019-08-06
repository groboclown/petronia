
"""
Basic logging infrastructure.
"""

from .level import (
    LogLevel,
    TRACE,
    DEBUG,
    VERBOSE,
    INFO,
    NOTICE,
    WARN,
    DEPRECATED,
    ERROR,
    FATAL,
)
from .handler import (
    LogHandler,
    LogHandlerId,
)
from .log import (
    log,
    logerr,
    add_log_handler,
    remove_log_handler,
)
