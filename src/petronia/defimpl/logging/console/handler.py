
"""
The log handler.
"""

import traceback
from typing import Optional, Set
from ....aid.simp import (
    TRACE, DEBUG, VERBOSE, INFO, NOTICE, WARN, DEPRECATED, ERROR, FATAL,
    LogLevel,
)

_LOG_PREFIX = {
    TRACE:      '[TRACE] ',
    DEBUG:      '[DEBUG] ',
    VERBOSE:    '[VERBO] ',
    INFO:       '[ INFO] ',
    NOTICE:     '[NOTIC] ',
    WARN:       '[ WARN] ',
    DEPRECATED: '[DEPRC] ',
    ERROR:      '[ERROR] ',
    FATAL:      '[FATAL] ',
}

def standard_log_message(
        level: LogLevel, src: str, msg: str, err: Optional[BaseException]
) -> None:
    """
    Standard console logger.  Includes special deprecated message reporting.
    """
    if level == DEPRECATED:
        # Deprecated messages are an interesting thing.  We want to report them
        # just once.
        src_msg = src + msg
        if src_msg not in _SEEN_DEPRECATED:
            _SEEN_DEPRECATED.add(src_msg)
            print("DEPRECTATION WARNING: {0} (reported from {1})".format(
                msg, src
            ))
    else:
        print(_LOG_PREFIX[level] + "{0:20}: ".format(src) + msg)
    if err:
        traceback.print_exception(err.__class__, err, err.__traceback__)

_SEEN_DEPRECATED: Set[str] = set()
