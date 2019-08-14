
"""
Type-safe storage of multiple states.
"""

from typing import Dict, Sequence, Optional, Type
from threading import Lock
from ...aid.simp import (
    ParticipantId,
    assert_formatted,
    assert_all,
    T,
    log,
    TRACE,
)
from ...core.state.api.validate import validate_state_id


class StateStore:
    """
    Bog-standard type-safe storage of multiple states.

    Note that each state is its own participant.  This may or may not
    directly match up with the owning component.
    """
    __slots__ = ('_state_types', '_states', '__lock')

    _state_types: Dict[ParticipantId, Type[object]]
    _states: Dict[ParticipantId, object]

    def __init__(self) -> None:
        self._state_types = {}
        self._states = {}
        self.__lock = Lock()

    def set_state(self, state_id: ParticipantId, state_type: Type[T], new_state: T) -> Optional[T]:
        """
        Attempt to register the state id with the given type, or update the
        existing state with the type.
        """
        validate_state_id(state_id)
        assert_all(
            'StateStore',
            'arguments must be valid',
            issubclass(state_type, object),
            isinstance(new_state, state_type),
        )
        old_state: Optional[T] = None
        with self.__lock:
            if state_id in self._state_types:
                assert_formatted(
                    self._state_types[state_id] == state_type,
                    'StateStore',
                    'Setting the state must match the original type',
                    'state {0} has type {1}, but requested type {2}',
                    state_id, self._state_types[state_id], state_type
                )
                old_state = self._states[state_id] # type: ignore
            self._state_types[state_id] = state_type
            self._states[state_id] = new_state
        return old_state

    def __contains__(self, key: ParticipantId) -> bool:
        with self.__lock:
            return key in self._state_types

    def get_state_type(self, state_id: ParticipantId) -> Optional[type]:
        """Returns the state type for the given state ID, or None if it isn't registered."""
        with self.__lock:
            if state_id in self._state_types:
                return self._state_types[state_id]
            return None

    def get_state(self, state_id: ParticipantId) -> object:
        """Returns the state stored for the state ID.  If the state isn't registered,
        then a ValueError is raised."""
        with self.__lock:
            return self._states[state_id] # type: ignore

    @property
    def state_ids(self) -> Sequence[ParticipantId]:
        """Get all the registered state IDs"""
        with self.__lock:
            return tuple(self._state_types.keys())
