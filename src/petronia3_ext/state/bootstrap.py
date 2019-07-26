
"""
EventBus interaction for the global state.
"""

from petronia3.extensions.state.api.events import (
    EVENT_ID_UPDATE_STATE_REQUEST,
    StateStoreUpdateRequestEvent,

    EVENT_ID_UPDATED_STATE,
    StateStoreUpdatedEvent,
)
from petronia3.system.bus import (
    EventId,
    EventBus, EventCallback,
    EventListenerAddedEvent,
    ListenerSetup, as_listener_added_listener,
    TARGET_WILDCARD,
)
from petronia3.system.participant import (
    ParticipantId,
    create_singleton_identity,
)
from petronia3.ext_help.module_bootstrap import create_module_listener_helper
from petronia3.util.memory import T
from .store import StateStore


MODULE_ID = create_singleton_identity('core.state.impl')
EXTENSION_DEPENDENCIES = ('core.state.api',)

def bootstrap_state_store(bus: EventBus) -> None:
    """Register all state store events."""
    helper = create_module_listener_helper(bus, MODULE_ID)
    store = _BusAwareStateStore(bus)
    # ListenerIds are not persisted, because this is a singleton
    # that is never disposed.
    helper.listen( # type: ignore
        TARGET_WILDCARD,
        _as_update_state_request_listener,
        store.on_update_request
    )
    helper.listen(
        TARGET_WILDCARD,
        as_listener_added_listener,
        store.on_listener_added
    )



class _BusAwareStateStore:
    """
    A StateStore that correctly interacts with the EventBus.
    """
    __slots__ = ('__bus', '__store',)

    def __init__(self, bus: EventBus) -> None:
        self.__bus = bus
        self.__store = StateStore()

    def on_update_request(
            self,
            eid: EventId, tid: ParticipantId, # pylint: disable=unused-argument
            event: StateStoreUpdateRequestEvent[T]
    ) -> None:
        """When a state is requested to be updated."""
        old_state = self.__store.set_state(
            event.state_id, event.state_type,
            event.state
        )
        self.__bus.trigger(EVENT_ID_UPDATED_STATE, event.state_id, StateStoreUpdatedEvent(
            event.state_id, event.state_type, event.state, old_state
        ))

    def on_listener_added(
            self,
            eid: EventId, tid: ParticipantId, # pylint: disable=unused-argument
            event: EventListenerAddedEvent
    ) -> None:
        """
        Whenever a new listener is added to the event bus.
        This allows new listeners to a specific state to receive the state when they
        start.
        """
        if event.event_id == EVENT_ID_UPDATED_STATE and tid in self.__store:
            # Rebroadcast the state.
            state = self.__store.get_state(tid)
            state_type = self.__store.get_state_type(tid)
            if state and state_type:
                self.__bus.trigger(EVENT_ID_UPDATED_STATE, tid, StateStoreUpdatedEvent(
                    tid, state_type, state, state
                ))

def _as_update_state_request_listener(
        callback: EventCallback[StateStoreUpdateRequestEvent[T]]
) -> ListenerSetup[StateStoreUpdateRequestEvent[T]]:
    return (EVENT_ID_UPDATE_STATE_REQUEST, callback,)
