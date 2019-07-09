
"""
Type-safe storage of multiple states.
"""

from ...errors import assert_state

class StateStore:
    """
    Bog-standard type-safe storage of multiple states.
    """
    def __init__(self):
        self.__state_types = {}
        self.__states = {}

    def set_state(self, state_id: str, state_type: type, initial_state):
        """
        Attempt to register the state id with the given type, or update the
        existing state with the type.
        """
        StateStore.validate_state_id(state_id)
        assert isinstance(state_type, type)
        assert isinstance(initial_state, state_type)
        if state_id in self.__state_types:
            assert_state(
                self.__state_types[state_id] == state_type,
                'StateStore',
                'Setting the state of {0} must match the original type {1}'.format(
                    state_id, self.__state_types[state_id]
                ),
                'requested state type {0}'.format(state_type)
            )
        else:
            self.__state_types[state_id] = state_type
        self.__states[state_id] = initial_state

    def __contains__(self, key):
        return key in self.__state_types

    def get_state_type(self, state_id):
        """Returns the state type for the given state ID, or None if it isn't registered."""
        if state_id in self.__state_types:
            return self.__state_types[state_id]
        return None

    def get_state(self, state_id):
        """Returns the state stored for the state ID.  If the state isn't registered,
        then a ValueError is raised."""
        return self.__states[state_id]

    @property
    def state_ids(self):
        """Get all the registered state IDs"""
        return self.__state_types.keys()

    @staticmethod
    def validate_state_id(state_id):
        """Ensure the state_id conforms to the standard."""
        assert isinstance(state_id, str)
        assert state_id
        assert not state_id.startswith('set_')
        assert not state_id.startswith('get_')
        assert state_id[0] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for cval in state_id:
            assert cval in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
