
"""
User CLI arguments to adjust the initial behavior of Petronia.
"""

from typing import List, Sequence, Optional
from ...base.logging import (
    add_log_handler, TRACE, DEBUG, VERBOSE, WARN,
)
from ...defimpl.logging.console.handler import standard_log_message

class UserArguments:
    """
    User passed-in arguments.

    Does not allow for augmenting the extension paths.
    """
    __slots__ = (
        'platform',
        'preboot_extensions',
        'extensions',
        'only_secure',
        'config_dir',
        'unparsed_args',
    )
    platform: Optional[str]
    preboot_extensions: List[str]
    extensions: List[str]
    config_dir: Optional[str]
    unparsed_args: List[str]

    def __init__(self) -> None:
        self.platform = None
        self.preboot_extensions = []
        self.extensions = []
        self.only_secure = False
        self.config_dir = None
        self.unparsed_args = []


def parse_args(args: Sequence[str]) -> UserArguments:
    """
    Parses the raw sys.argv values.
    """
    ret = UserArguments()
    idx = 0
    arg_count = len(args)
    log_level = WARN
    while idx < arg_count:
        arg = args[idx]
        if arg == '--platform' and idx + 1 < arg_count:
            idx += 1
            ret.platform = args[idx]
        elif arg == '--config-dir' and idx + 1 < arg_count:
            idx += 1
            ret.config_dir = args[idx]
        elif arg == '--debug':
            log_level = DEBUG
        elif arg == '--trace':
            log_level = TRACE
        elif arg == '--verbose':
            log_level = VERBOSE
        else:
            ret.unparsed_args.append(arg)
        idx += 1
    add_log_handler(log_level, '', standard_log_message)
    return ret
