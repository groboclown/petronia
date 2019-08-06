
"""
EventBus interaction for the global state.
"""

from typing import Type, Optional, Generic
from ....base import ParticipantId
from ....base.bus import (
    EventId,
    EventBus,
    EventCallback,
    ListenerSetup,
)
from ....base.util import T

EVENT_ID_UPDATE_STATE_REQUEST = EventId('core.state.api request-update')


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


EVENT_ID_UPDATED_STATE = EventId('core.state.api updated')

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


def set_state(
        bus: EventBus, state_id: ParticipantId, state_type: Type[T], state: T
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
        callback: EventCallback[StateStoreUpdatedEvent[T]],
) -> ListenerSetup[StateStoreUpdatedEvent[T]]:
    """
    Creates the event listener setup for use with add_listener.
    """
    return (EVENT_ID_UPDATED_STATE, callback,)
