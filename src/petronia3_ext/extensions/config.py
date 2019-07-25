
"""
State of the extension manager.
"""

from typing import Sequence, Optional
from ....system.bus import (
    EventBus, EventCallback, ListenerSetup, ListenerId
)
from ....system.participant import create_singleton_identity
from ...state import set_state, StateStoreUpdatedEvent, as_state_change_listener
from ....util.memory import EMPTY_TUPLE

CONFIGURATION_EXTENSION_LOADER = create_singleton_identity('extension-config')

class ExtensionConfiguration:
    """
    All the configured state information
    """
    __slots__ = ('_zip_dirs', '_paths')
    _zip_dirs: Sequence[str]
    _paths: Sequence[str]

    def __init__(
            self,
            zip_dirs: Optional[Sequence[str]] = None,
            paths: Optional[Sequence[str]] = None
    ) -> None:
        self._zip_dirs = tuple(zip_dirs or EMPTY_TUPLE) # type: ignore
        self._paths = tuple(paths or EMPTY_TUPLE) # type: ignore

    @property
    def zip_dirs(self) -> Sequence[str]:
        """Directories that contain zip files to be inspected for extensions.
        These directories are not checked recursively."""
        return self._zip_dirs

    @property
    def paths(self) -> Sequence[str]:
        """List of paths to search for extensions.  These are checked after zips
        in the `zip_dirs`."""
        return self._paths


def set_extension_loader_configuration(
        bus: EventBus, config: ExtensionConfiguration
) -> None:
    """Convenience function to set the loader configuration."""
    set_state(bus, CONFIGURATION_EXTENSION_LOADER, ExtensionConfiguration, config)


STATE_EXTENSION_LOADER = create_singleton_identity('extension-state')

class ExtensionState:
    """
    All the transitive state information that other
    participants may want to know.
    """
    __slots__ = ('_loaded_extensions',)
    _loaded_extensions: Sequence[str]

    def __init__(self, extensions: Optional[Sequence[str]] = None) -> None:
        self._loaded_extensions = tuple(extensions or EMPTY_TUPLE) # type: ignore

    @property
    def loaded_extensions(self) -> Sequence[str]:
        """
        All extension names loaded.
        """
        return self._loaded_extensions


def as_extension_state_listener(
        callback: EventCallback[StateStoreUpdatedEvent[ExtensionState]]
) -> ListenerSetup[StateStoreUpdatedEvent[ExtensionState]]:
    """Listener setup for the extension state changes."""
    return as_state_change_listener(callback)


def add_extension_state_listener(
        bus: EventBus,
        callback: EventCallback[StateStoreUpdatedEvent[ExtensionState]]
) -> ListenerId:
    """Add a listener for the extension loader state changes."""
    return bus.add_listener(STATE_EXTENSION_LOADER, as_extension_state_listener, callback)
