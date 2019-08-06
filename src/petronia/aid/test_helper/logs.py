
"""Unit tests for event bus stuff"""

import traceback
from typing import List, Optional, Any
from ...base.logging import (
    TRACE, DEBUG, VERBOSE, INFO, NOTICE, WARN, DEPRECATED, ERROR, FATAL,
    LogHandlerId,
    LogLevel,
    add_log_handler,
    remove_log_handler,
)

_LOG_NAMES = {
    TRACE:   'TRACE',
    DEBUG:   'DEBUG',
    VERBOSE: 'VERBO',
    INFO:    ' INFO',
    NOTICE:  'NOTIC',
    WARN:    ' WARN',
    DEPRECATED: 'DEPRC',
    ERROR:   'ERROR',
    FATAL:   'FATAL',
}

class EnabledLogs:
    __log_ids: List[LogHandlerId]

    def __init__(self, level: LogLevel = TRACE) -> None:
        self.__level = level
        self.__log_ids = []


    def __enter__(self) -> None:
        self.__log_ids.append(
            add_log_handler(self.__level, '', self._log_it)
        )

    def __exit__(self, type_arg: Any, value: Any, etraceback: Any) -> None: # type: ignore
        for lhid in self.__log_ids:
            remove_log_handler(lhid)
        self.__log_ids = []

    def _log_it(self, level: LogLevel, src: str, msg: str, err: Optional[BaseException]) -> None:
        print("[{0}] {1:20}: {2}".format(_LOG_NAMES[level], src, msg))
        if err:
            traceback.print_exception(err.__class__, err, err.__traceback__)
