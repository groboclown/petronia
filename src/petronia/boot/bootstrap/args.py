
"""
User CLI arguments to adjust the initial behavior of Petronia.
"""

from typing import List, Sequence, Optional
import sys
from ...base.logging import (
    add_log_handler, TRACE, DEBUG, VERBOSE, INFO, WARN,
)
from ...defimpl.logging.console.handler import standard_log_message
from . import version


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
        'config_dirs',
        'unparsed_args',
        'is_help',
    )
    platform: Optional[str]
    preboot_extensions: List[str]
    extensions: List[str]
    config_dirs: List[str]
    unparsed_args: List[str]

    def __init__(self) -> None:
        self.platform = None
        self.preboot_extensions = []
        self.extensions = []
        self.only_secure = False
        self.config_dirs = []
        self.unparsed_args = []
        self.is_help = False


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
            ret.config_dirs.append(args[idx])
        elif arg == '--preboot' and idx + 1 < arg_count:
            idx += 1
            ret.preboot_extensions.append(args[idx])
        elif arg == '--debug':
            log_level = DEBUG
        elif arg == '--trace':
            log_level = TRACE
        elif arg == '--verbose':
            log_level = VERBOSE
        elif arg == '--info':
            log_level = INFO
        elif arg == '--help':
            ret.is_help = True
        elif arg == '--version':
            show_version()
        else:
            ret.unparsed_args.append(arg)
        idx += 1
    add_log_handler(log_level, '', standard_log_message)
    return ret


def cmd_help(platform_help: str) -> None:
    print('''{name}
Version {version}

Standard options:

--platform platform_name
    Forces Petronia to use the specified platform name, rather than attempting
    to auto-detect the platform.  See the platform-specific documentation for
    how to name the platform.  Standard platforms are `windows` and `posix`.
    
--config-dir directory_name
    Add an additional directory to inspect for configuration files.  These
    will be searched before the internal search path for the platform.

--preboot extension.name
    Add an additional extension to load before the platform begins execution.
    
--version
    Show the name and version of the software.

--info
    Turn on global "informative" level logging.

--verbose
    Turn on global "verbose" level logging.

--debug
    Turn on global "debug" level logging.  This will be very noisy.
    
--trace
    Turn on global "trace" level logging.  Useful primarily when debugging
    internals of Petronia, and will have a stream of information going by.
    

'''.format(
        name=version.NAME,
        program=version.PROGRAM,
        version=version.VERSION
) + platform_help)
    sys.exit(0)


def show_version() -> None:
    # print(version.NAME)
    print(version.VERSION)
    sys.exit(0)
