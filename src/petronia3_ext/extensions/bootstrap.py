
"""
Add the extensions into the system.
"""

from typing import Sequence, Set
from .loader import (
    load_extension,
)
from ..api.events import (
    TARGET_EXTENSION_LOADER,
    EVENT_ID_EXTENSION_LOADED,
    ExtensionLoadedEvent,
    EVENT_ID_REQUEST_LOAD_EXTENSION,
    RequestLoadExtensionEvent,
)
from ..api.state import (
    CONFIGURATION_EXTENSION_LOADER,
    ExtensionConfiguration,

    STATE_EXTENSION_LOADER,
    ExtensionState,
    as_extension_state_listener,
)
from ...state import (
    StateStoreUpdatedEvent,
    as_state_change_listener,
    set_state,
)
from ....system.bus import (
    EventBus,
    EventId,
    EventCallback,
    ListenerSetup,
    ListenerId,
    register_event,
    QUEUE_EVENT_IO,
    QUEUE_EVENT_NORMAL,
)
from ....system.participant import (
    ParticipantId
)

def bootstrap_extension_loader(bus: EventBus) -> None:
    """
    Adds the extension loader into the bus.
    """
    register_event(
        bus,
        EVENT_ID_REQUEST_LOAD_EXTENSION,
        # extension loading must happen in the I/O threads, because
        # it reads that information.
        QUEUE_EVENT_IO,
        RequestLoadExtensionEvent,
        RequestLoadExtensionEvent('x')
    )
    register_event(
        bus,
        EVENT_ID_EXTENSION_LOADED,
        QUEUE_EVENT_NORMAL,
        ExtensionLoadedEvent,
        ExtensionLoadedEvent('x', [])
    )

    loader = _ExtensionStatefulLoader(bus, ExtensionState(), ExtensionConfiguration())
    bus.add_listener(
        CONFIGURATION_EXTENSION_LOADER,
        _as_configuration_loaded_listener,
        loader.on_extension_config_change
    )
    bus.add_listener(
        STATE_EXTENSION_LOADER,
        as_extension_state_listener,
        loader.on_extension_state_change
    )
    bus.add_listener(
        TARGET_EXTENSION_LOADER,
        _as_request_load_extension_listener,
        loader.on_extension_load_request
    )


class _ExtensionStatefulLoader:
    __slots__ = ('__bus', '__state', '__config', '_loaded')
    _loaded = Set[str]
    def __init__(
            self,
            bus: EventBus,
            state: ExtensionState,
            config: ExtensionConfiguration
    ) -> None:
        self.__bus = bus
        self.__state = state
        self.__config = config
        self._loaded = set(state.loaded_extensions)

    def on_extension_load_request(
            self,
            event_id: EventId,
            target_id: ParticipantId,
            event_object: RequestLoadExtensionEvent
    ) -> None:
        deps = load_extension(
            event_object.extension_name,
            self.__bus,
            self.__config,
            self.__state
        )
        _send_extension_loaded_event(
            self.__bus,
            event_object.extension_name,
            deps
        )
        self._loaded = self._loaded.union(deps)
        if self._loaded != self.__state.loaded_extensions:
            _send_extension_state_change(self.__bus, ExtensionState(self._loaded))

    def on_extension_config_change(
            self,
            event_id: EventId,
            target_id: ParticipantId,
            event_object: StateStoreUpdatedEvent[ExtensionConfiguration]
    ) -> None:
        self.__config = event_object.state

    def on_extension_state_change(
            self,
            event_id: EventId,
            target_id: ParticipantId,
            event_object: StateStoreUpdatedEvent[ExtensionState]
    ) -> None:
        self.__state = event_object.state
        self._loaded = self._loaded.union(event_object.state.loaded_extensions)
        if self._loaded != event_object.loaded_extensions:
            _send_extension_state_change(self.__bus, ExtensionState(self._loaded))



def _as_request_load_extension_listener(
        callback: EventCallback[RequestLoadExtensionEvent]
) -> ListenerSetup[RequestLoadExtensionEvent]:
    return (EVENT_ID_REQUEST_LOAD_EXTENSION, callback,)

def _send_extension_loaded_event(
        bus: EventBus,
        extension_name: str,
        loaded_dependencies: Sequence[str]
) -> None:
    bus.trigger(
        EVENT_ID_EXTENSION_LOADED, TARGET_EXTENSION_LOADER,
        ExtensionLoadedEvent(extension_name, loaded_dependencies)
    )

def _as_configuration_loaded_listener(
        callback: EventCallback[StateStoreUpdatedEvent[ExtensionConfiguration]]
) -> ListenerSetup[StateStoreUpdatedEvent[ExtensionConfiguration]]:
    return as_state_change_listener(callback)

def _add_configuration_loaded_listener(
        bus: EventBus,
        callback: EventCallback[StateStoreUpdatedEvent[ExtensionConfiguration]]
) -> ListenerId:
    return bus.add_listener(
        CONFIGURATION_EXTENSION_LOADER,
        _as_configuration_loaded_listener,
        callback
    )

def _send_extension_state_change(
        bus: EventBus,
        state: ExtensionState
) -> None:
    set_state(bus, STATE_EXTENSION_LOADER, ExtensionState, state)
