
"""
State of the extension manager.
"""

from typing import Sequence, Tuple, Optional
from ....system.bus import (
    EventBus, EventCallback, ListenerSetup, ListenerId
)
from ....system.participant import create_singleton_identity
from ...state import StateStoreUpdatedEvent, as_state_change_listener
from ....util.memory import EMPTY_TUPLE

CONFIGURATION_EXTENSION_LOADER = create_singleton_identity('extension-config')


STATE_EXTENSION_LOADER = create_singleton_identity('extension-state')


class LoadedExtension:
    """
    Information about a loaded extension.
    """
    __slots__ = ('_name', '_version',)
    def __init__(self, name: str, version: Tuple[int, int, int]) -> None:
        self._name = name
        self._version = version

    @property
    def name(self) -> str:
        return self.name

    @property
    def version(self) -> Tuple[int, int, int]:
        return self._version


class ExtensionState:
    """
    All the transitive state information that other
    participants may want to know.
    """
    __slots__ = ('_loaded_extensions',)
    _loaded_extensions: Sequence[LoadedExtension]

    def __init__(self, extensions: Optional[Sequence[LoadedExtension]] = None) -> None:
        self._loaded_extensions = tuple(extensions or EMPTY_TUPLE) # type: ignore

    @property
    def loaded_extensions(self) -> Sequence[LoadedExtension]:
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
