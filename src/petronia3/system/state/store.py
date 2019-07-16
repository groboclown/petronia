
"""
Type-safe storage of multiple states.
"""

from typing import Dict, Sequence, Optional, Type
from ..participant import ParticipantId, is_valid_participant_identity
from ...validation import assert_formatted
from ...util.memory import T

class StateStore:
    """
    Bog-standard type-safe storage of multiple states.

    Note that each state is its own participant.  This may or may not
    directly match up with the owning component.
    """

    __state_types: Dict[ParticipantId, Type[object]]
    __states: Dict[ParticipantId, object]

    def __init__(self) -> None:
        self.__state_types = {}
        self.__states = {}

    def set_state(self, state_id: ParticipantId, state_type: Type[T], new_state: T) -> Optional[T]:
        """
        Attempt to register the state id with the given type, or update the
        existing state with the type.
        """
        StateStore.validate_state_id(state_id)
        assert issubclass(state_type, object)
        assert isinstance(new_state, state_type)
        old_state: Optional[T] = None
        if state_id in self.__state_types:
            assert_formatted(
                self.__state_types[state_id] == state_type,
                'StateStore',
                'Setting the state must match the original type',
                'state {0} has type {1}, but requested type {2}',
                state_id, self.__state_types[state_id], state_type
            )
            old_state = self.__states[state_id] # type: ignore
        self.__state_types[state_id] = state_type
        self.__states[state_id] = new_state
        return old_state

    def __contains__(self, key: ParticipantId) -> bool:
        return key in self.__state_types

    def get_state_type(self, state_id: ParticipantId) -> Optional[type]:
        """Returns the state type for the given state ID, or None if it isn't registered."""
        if state_id in self.__state_types:
            return self.__state_types[state_id]
        return None

    def get_state(self, state_id: ParticipantId) -> object:
        """Returns the state stored for the state ID.  If the state isn't registered,
        then a ValueError is raised."""
        return self.__states[state_id] # type: ignore

    @property
    def state_ids(self) -> Sequence[ParticipantId]:
        """Get all the registered state IDs"""
        return tuple(self.__state_types.keys())

    @staticmethod
    def validate_state_id(state_id: ParticipantId) -> None:
        """Ensure the state_id conforms to the standard."""

        assert_formatted(
            is_valid_participant_identity(state_id),

            'StateStore',
            'invalid state id format',
            'id {0}', state_id
        )
