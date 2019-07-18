
"""
EventBus interaction for the global state.
"""

from .events import (
    EVENT_ID_UPDATE_STATE_REQUEST,
    StateStoreUpdateRequestEvent,

    EVENT_ID_UPDATED_STATE,
    StateStoreUpdatedEvent,
)
from ..bus import (
    EventId, register_event,
    TypeSafeEventBus, TypeSafeEventCallback,
    EventListenerAddedEvent,
    ListenerSetup, as_listener_added_listener,
    QUEUE_EVENT_NORMAL,
    TARGET_WILDCARD,
)
from ..participant import (
    ParticipantId,
    NOT_PARTICIPANT,
)
from .store import StateStore
from ...util.memory import T


def bootstrap_state_store(bus: TypeSafeEventBus) -> None:
    """Register all state store events."""
    register_event(
        bus,
        EVENT_ID_UPDATE_STATE_REQUEST,
        QUEUE_EVENT_NORMAL,
        StateStoreUpdateRequestEvent,
        StateStoreUpdateRequestEvent(NOT_PARTICIPANT, object, object()) # type: ignore
    )
    register_event(
        bus,
        EVENT_ID_UPDATED_STATE,
        QUEUE_EVENT_NORMAL,
        StateStoreUpdatedEvent,
        StateStoreUpdatedEvent(NOT_PARTICIPANT, object, object(), object()) # type: ignore
    )
    store = _BusAwareStateStore(bus)
    # ListenerIds are not persisted, because this is a singleton
    # that is never disposed.
    bus.add_listener(
        TARGET_WILDCARD,
        _as_update_state_request_listener,
        store.on_update_request
    )
    bus.add_listener(
        TARGET_WILDCARD,
        as_listener_added_listener,
        store.on_listener_added
    )



class _BusAwareStateStore:
    """
    A StateStore that correctly interacts with the EventBus.
    """
    __slots__ = ('__bus', '__store',)

    def __init__(self, bus: TypeSafeEventBus) -> None:
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
        callback: TypeSafeEventCallback[StateStoreUpdateRequestEvent[T]]
) -> ListenerSetup[StateStoreUpdateRequestEvent[T]]:
    return (EVENT_ID_UPDATE_STATE_REQUEST, callback,)
