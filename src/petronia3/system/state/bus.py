
"""
EventBus interaction for the global state.
"""

from typing import Type, Sequence, Optional, Generic, List
from ..bus import (
    EventRegistry, EventId,
    TypeSafeEventBus, TypeSafeEventCallback,
    EventListenerAddedEvent,
    ListenerSetup, as_listener_added_listener,
    ListenerId,
    QUEUE_EVENT_NORMAL,
    TARGET_WILDCARD,
)
from ..participant import (
    ParticipantId,
    NOT_PARTICIPANT,
)
from .store import StateStore
from ...util.memory import T

EVENT_ID_UPDATE_STATE_REQUEST = EventId('state-store request-update')
EVENT_ID_UPDATED_STATE = EventId('state-store updated')


class StateStoreUpdateRequestEvent(Generic[T]):
    """The state in the store is updated."""

    # Generic w/ slots and private (leading "__") members is still
    # an issue, even after the fix for https://bugs.python.org/issue28790
    __slots__ = ('_state_id', '_state', '_state_type')

    def __init__(self, state_id: ParticipantId, state_type: Type[T], state: T) -> None:
        self._state_id = state_id
        self._state = state
        self._state_type = state_type

    @property
    def state_id(self) -> ParticipantId:
        """The state ID."""
        return self._state_id

    @property
    def state(self) -> T:
        """The updated state object."""
        return self._state

    @property
    def state_type(self) -> Type[T]:
        """The state object's expected type.  If not already registered, it
        must match with the existing type."""
        return self._state_type


class StateStoreUpdatedEvent(Generic[T]):
    """Reports that a state value was successfully updated."""
    __slots__ = ('_state_id', '_state', '_state_type', '_previous')

    def __init__(
            self,
            state_id: ParticipantId,
            state_type: Type[T],
            state: T,
            previous: Optional[T]
    ) -> None:
        self._state_id = state_id
        self._state = state
        self._state_type = state_type
        self._previous = previous

    @property
    def state_id(self) -> ParticipantId:
        """The state ID that was updated."""
        return self._state_id

    @property
    def state(self) -> T:
        """The updated state object."""
        return self._state

    @property
    def state_type(self) -> Type[T]:
        """The state object's expected type.  If not already registered, it
        must match with the existing type."""
        return self._state_type

    @property
    def previous_state(self) -> Optional[T]:
        """The before-update version of the state.  This can be used to find
        differences, if any."""
        return self._previous


def register_events(reg: EventRegistry) -> None:
    """Register all state store events."""
    reg.register(
        EVENT_ID_UPDATE_STATE_REQUEST,
        QUEUE_EVENT_NORMAL,
        StateStoreUpdateRequestEvent,
        StateStoreUpdateRequestEvent(NOT_PARTICIPANT, object, object()) # type: ignore
    )
    reg.register(
        EVENT_ID_UPDATED_STATE,
        QUEUE_EVENT_NORMAL,
        StateStoreUpdatedEvent,
        StateStoreUpdatedEvent(NOT_PARTICIPANT, object, object(), object()) # type: ignore
    )


def set_state(
        bus: TypeSafeEventBus, state_id: ParticipantId, state_type: Type[T], state: T
) -> None:
    """
    Send a state update notice to the state store.

    For each state, a specific version of this should be used instead that
    sets the state_id, state_type and uses correct typing on the state object.
    """
    bus.trigger(
        EVENT_ID_UPDATE_STATE_REQUEST,
        state_id,
        StateStoreUpdateRequestEvent(state_id, state_type, state)
    )


def as_state_change_listener(
        callback: TypeSafeEventCallback[StateStoreUpdatedEvent[T]],
) -> ListenerSetup[StateStoreUpdatedEvent[T]]:
    """
    Creates the event listener setup for use with add_listener.
    """
    return (EVENT_ID_UPDATED_STATE, callback,)


class BusAwareStateStore:
    """
    A StateStore that correctly interacts with the EventBus.
    """
    __slots__ = ('__bus', '__store', '_listeners',)
    _listeners: List[ListenerId]

    def __init__(self, bus: TypeSafeEventBus) -> None:
        self.__bus = bus
        self.__store = StateStore()
        self._listeners = [
            bus.add_listener(
                TARGET_WILDCARD,
                _as_update_state_request_listener,
                self._on_update_request
            ),
            bus.add_listener(
                TARGET_WILDCARD, as_listener_added_listener, self._on_listener_added
            )
        ]

    def get_state_type(self, state_id: ParticipantId) -> Optional[Type[type]]:
        """Returns the state type for the given state ID, or None if it isn't registered."""
        return self.__store.get_state_type(state_id)

    def get_state(self, state_id: ParticipantId) -> object:
        """Returns the state stored for the state ID.  If the state isn't registered,
        then a ValueError is raised."""
        return self.__store.get_state(state_id)

    @property
    def state_ids(self) -> Sequence[ParticipantId]:
        """Get all the registered state IDs"""
        return self.__store.state_ids

    def dispose(self) -> None:
        """Shut-down call.  Can be safely called again."""
        for listener_id in self._listeners:
            self.__bus.remove_listener(listener_id)
        self._listeners.clear()

    def _on_update_request(
            self,
            eid: EventId, tid: ParticipantId, # pylint: disable=unused-argument
            event: StateStoreUpdateRequestEvent[T]
    ) -> None:
        old_state = self.__store.set_state(
            event.state_id, event.state_type,
            event.state
        )
        self.__bus.trigger(EVENT_ID_UPDATED_STATE, event.state_id, StateStoreUpdatedEvent(
            event.state_id, event.state_type, event.state, old_state
        ))

    def _on_listener_added(
            self,
            eid: EventId, tid: ParticipantId, # pylint: disable=unused-argument
            event: EventListenerAddedEvent
    ) -> None:
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
