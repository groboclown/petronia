
"""
State of the extension manager.
"""

from typing import Sequence, Iterable, Optional
from .defs import LoadedExtension
from ....system.bus import (
    EventBus, EventCallback, ListenerSetup, ListenerId
)
from ....system.participant import create_singleton_identity
from ...state.api import StateStoreUpdatedEvent, as_state_change_listener
from ....util.memory import EMPTY_TUPLE

CONFIGURATION_EXTENSION_LOADER = create_singleton_identity('extension-config')


STATE_EXTENSION_LOADER = create_singleton_identity('extension-state')


class ExtensionState:
    """
    All the transitive state information that other
    participants may want to know.
    """
    __slots__ = ('_loaded_extensions',)
    _loaded_extensions: Sequence[LoadedExtension]

    def __init__(self, extensions: Optional[Iterable[LoadedExtension]] = None) -> None:
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
