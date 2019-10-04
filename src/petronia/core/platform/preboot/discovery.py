
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


class ExtensionLoaderModel:
    """
    Details about how to load the extension loader extension.
    """
    __slots__ = ('name',)

    def __init__(self, name: str) -> None:
        self.name = name


class DiscoveryData:
    """
    All the data that the pre-boot platform must return.

    ext_paths: extension path structure.

    extension_sets: collections of extensions that must be loaded appart from
        each other.

    temp_dir: directory to put temporary files and directories specific to
        this execution of Petronia.

    extension_loader_module: module in charge of creating the extensions extension
        and loading the initial extension sets.

    only_secure: whether Petronia should only load extensions marked as
        "secure", and refuse to load extensions that haven't been designated
        as okay to run with wide permissions.

    event_queue_model: a place-holder until better structured information
        can be supplied to describe the construction of the event queue
        handler.

    config_dirs: directories to search for configuration.  Used when sending
        out information for the configuration extensions, if any.
    """
    __slots__ = (
        'ext_paths',
        'preboot_extensions',
        'extension_sets',
        'temp_dir',
        'only_secure',
        'event_queue_model',
        'extension_loader_module',
        'config_dirs',
        'arg_help',
    )

    def __init__(
            self,
            ext_paths: ExtensionPaths,
            preboot_extensions: Iterable[Iterable[str]],
            extension_sets: Iterable[Iterable[str]],
            temp_dir: str,
            only_secure: bool,
            extension_loader_module: ExtensionLoaderModel,
            event_queue_model: EventQueueModel,
            config_dirs: Iterable[str],
            arg_help: str
    ) -> None:
        self.ext_paths = ext_paths
        self.preboot_extensions = preboot_extensions
        self.extension_sets = extension_sets
        self.temp_dir = temp_dir
        self.only_secure = only_secure
        self.extension_loader_module = extension_loader_module
        self.event_queue_model = event_queue_model
        self.config_dirs = config_dirs
        self.arg_help = arg_help


DiscoveryFunction = Callable[[], DiscoveryData]

DISCOVERY_FUNCTION_NAME = 'discover_preboot_data'

RunSystemFunction = Callable[[EventBus], int]

RUN_SYSTEM_FUNCTION_NAME = 'run_petronia'
