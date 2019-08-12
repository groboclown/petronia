
"""
Standard function that the preboot platform implementation must provide in the module.
"""

from typing import Callable, Iterable
from .directories import ExtensionPaths
from ....base import EventBus

class EventQueueModel:
    """
    Simple object that can be extended according to the different
    bootstrap extensions.

    This might be expanded upon in the future as common traits are identified,
    or to help the bootstrap process.
    """
    __slots__ = ()


class DiscoveryData:
    """
    All the data that the pre-boot platform must return.

    ext_paths: extension path structure.

    platform_extensions: extensions that the platform needs to get running
        before the platform startup.

    temp_dir: directory to put temporary files and directories specific to
        this execution of Petronia.

    only_secure: whether Petronia should only load extensions marked as
        "secure", and refuse to load extensions that haven't been designated
        as okay to run with wide permissions.

    event_queue_model: a place-holder until better structured information
        can be supplied to describe the construction of the event queue
        handler.
    """
    __slots__ = (
        'ext_paths',
        'platform_extensions',
        'temp_dir',
        'only_secure',
        'event_queue_model',
    )
    def __init__(
            self,
            ext_paths: ExtensionPaths,
            platform_extensions: Iterable[str],
            temp_dir: str,
            only_secure: bool,
            event_queue_model: EventQueueModel
    ) -> None:
        self.ext_paths = ext_paths
        self.platform_extensions = platform_extensions
        self.temp_dir = temp_dir
        self.only_secure = only_secure
        self.event_queue_model = event_queue_model

DiscoveryFunction = Callable[[], DiscoveryData]

DISCOVERY_FUNCTION_NAME = 'discover_preboot_data'

RunSystemFunction = Callable[[EventBus], int]

RUN_SYSTEM_FUNCTION_NAME = 'run_petronia'
