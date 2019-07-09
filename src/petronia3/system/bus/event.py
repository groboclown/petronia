"""
Event helpers.
"""

import datetime
from .bus import EventBus, EVENT_WILDCARD
from ...errors import assert_state, assert_contains

class Event: # pylint: disable=too-few-public-methods
    """
    Base event object.
    """
    def __init__(self):
        self.__when = datetime.datetime()

    @property
    def when(self):
        """When the event happened."""
        return self.__when

class EventRegistry:
    """
    Registration of all event IDs and the expected class types.
    """

    def __init__(self):
        self._types = {}

    def register(self, event_id: str, event_class: type):
        """
        Register an event ID with an expected event class.
        """
        EventBus.validate_event_id(event_id)
        assert event_id != EVENT_WILDCARD
        assert issubclass(event_class, Event)
        assert_state(
            event_id not in self._types,
            'EventRegistry',
            'event IDs can only be registered once'
        )
        self._types[event_id] = event_class

    def validate_event(self, event_id: str, target_id: str, event_object):
        """Validates that the event object is of the correct event id type."""
        assert_contains(
            self._types, event_id,
            'EventRegistry',
            'event ID {0} must be registered as a valid event'
        )
        assert_state(
            isinstance(event_object, self._types[event_id]),
            'EventRegistry',
            'event {0} on target {1} must be called with typed event {2}'.format(event_id, target_id, self._types[event_id]),
            'called with event type {0}: {1}'.format(type(event_object), event_object)
        )

    def validate_has(self, event_id: str):
        """Validates that the event id is correctly registered."""
        assert_contains(
            self._types, event_id,
            'EventRegistry',
            'event ID {0} must be registered as a valid event'
        )


class TypeSafeEventBus:
    """
    A type-safe version of the EventBus.
    """
    def __init__(self, bus: EventBus, reg: EventRegistry):
        assert isinstance(bus, EventBus)
        assert isinstance(reg, EventRegistry)
        self.__bus = bus
        self.__reg = reg

    def add_listener(self, event_id: str, target_id: str, listener: callable):
        """
        Registers a type-safe event listener.  Cannot work with a wildcard event ID.
        """
        self.__reg.validate_has(event_id)
        return self.__bus.add_listener(event_id, target_id, lambda eid, tid, eo: self.__listener_callback(eid, tid, eo, listener))

    def trigger(self, event_id: str, target_id: str, event_obj):
        """
        Triggers an event to fire.
        """
        self.__reg.validate_event(event_id, target_id, event_obj)
        self.__bus.trigger(event_id, target_id, event_obj)

    def trigger_now(self, event_id: str, target_id: str, event_obj):
        """
        Triggers an event to fire right now.
        """
        self.__reg.validate_event(event_id, target_id, event_obj)
        self.__bus.trigger_now(event_id, target_id, event_obj)

    def trigger_io(self, event_id: str, target_id: str, event_obj):
        """
        Triggers an event to fire in the I/O priority threads.
        """
        self.__reg.validate_event(event_id, target_id, event_obj)
        self.__bus.trigger_io(event_id, target_id, event_obj)


    def __listener_callback(self, event_id, target_id, event_obj, callback):
        self.__reg.validate_event(event_id, target_id, event_obj)
        callback(event_id, target_id, event_obj)
