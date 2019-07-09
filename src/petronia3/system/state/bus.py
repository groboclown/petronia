
"""
EventBus interaction for the global state.
"""

from ..bus import EventBus, EventRegistry, Event
from .store import StateStore

EVENT_ID_UPDATE_REQUEST_STATE = 'state-store request-update'
EVENT_ID_UPDATED_STATE = 'state-store updated'

TARGET_ID_GLOBAL_STATE = 'global-state'


class StateStoreUpdateRequestEvent(Event):
    """The state in the store is updated."""
    def __init__(self, state_id: str, state_type: type, state):
        Event.__init__(self)
        StateStore.validate_state_id(state_id)
        assert isinstance(state_type, type)
        self.__state_id = state_id
        self.__state = state
        self.__state_type = state_type

    @property
    def state_id(self):
        """The state ID."""
        return self.__state_id

    @property
    def state(self):
        """The updated state object."""
        return self.__state

    @property
    def state_type(self):
        """The state object's expected type.  If not already registered, it
        must match with the existing type."""
        return self.__state_type


class StateStoreUpdatedEvent(Event):
    """Reports that a state value was successfully updated."""
    def __init__(self, state_id: str, state_type: type, state):
        Event.__init__(self)
        self.__state_id = state_id
        self.__state = state
        self.__state_type = state_type

    @property
    def state_id(self):
        """The state ID that was updated."""
        return self.__state_id

    @property
    def state(self):
        """The updated state object."""
        return self.__state

    @property
    def state_type(self):
        """The state object's expected type.  If not already registered, it
        must match with the existing type."""
        return self.__state_type


def register_events(reg: EventRegistry):
    """Register all state store events."""
    reg.register(EVENT_ID_UPDATE_REQUEST_STATE, StateStoreUpdateRequestEvent)
    reg.register(EVENT_ID_UPDATED_STATE, StateStoreUpdatedEvent)


class BusAwareStateStore:
    def __init__(self, bus: EventBus, target_id: str):
        self.__bus = bus
        self.__id = target_id
        self.__store = StateStore()
        self.__deregister_master = bus.add_listener(
            EVENT_ID_UPDATE_REQUEST_STATE, target_id,
            lambda eid, tid, obj: self._on_update_request(obj)
        )

    def get_state_type(self, state_id):
        """Returns the state type for the given state ID, or None if it isn't registered."""
        return self.__store.get_state_type(state_id)

    def get_state(self, state_id):
        """Returns the state stored for the state ID.  If the state isn't registered,
        then a ValueError is raised."""
        return self.__store.get_state(state_id)

    @property
    def state_ids(self):
        """Get all the registered state IDs"""
        return self.__store.state_ids

    def dispose(self):
        """Shut-down call.  Can be safely called again."""
        self.__deregister_master()
        self.__deregister_master = lambda: 0

    def _on_update_request(self, event: StateStoreUpdateRequestEvent):
        self.__store.set_state(event.state_id, event.state_type, event.state)
        self.__bus.trigger(EVENT_ID_UPDATED_STATE, event.state_id, StateStoreUpdatedEvent(
            event.state_id, event.state_type, event.state
        ))
