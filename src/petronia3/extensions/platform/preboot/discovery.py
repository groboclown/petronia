
"""
Standard function that the preboot platform implementation must provide in the module.
"""

from typing import Callable, Iterable
from .directories import ExtensionPaths
from ....system.bus import EventBus

class DiscoveryData:
    """
    All the data that the pre-boot platform must return.
    """
    __slots__ = (
        'ext_paths',
        'platform_extensions',
        'io_thread_count',
        'temp_dir',
        'only_secure',
    )
    def __init__(
            self,
            ext_paths: ExtensionPaths,
            platform_extensions: Iterable[str],
            io_thread_count: int,
            temp_dir: str,
            only_secure: bool
    ) -> None:
        self.ext_paths = ext_paths
        self.platform_extensions = platform_extensions
        self.io_thread_count = io_thread_count
        self.temp_dir = temp_dir
        self.only_secure = only_secure

PREBOOT_MODULE_NAME = 'preboot'

DiscoveryFunction = Callable[[], DiscoveryData]

DISCOVERY_FUNCTION_NAME = 'discover_preboot_data'

RunSystemFunction = Callable[[EventBus], int]

RUN_SYSTEM_FUNCTION_NAME = 'run_petronia'
