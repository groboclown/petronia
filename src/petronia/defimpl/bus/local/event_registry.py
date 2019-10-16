"""
Event helpers.
"""

from typing import Dict, Type, Optional, Iterable
from ....base.bus import (
    QueuePriority,
    EventId,

    EVENT_WILDCARD,
    QUEUE_EVENT_TYPES,
)
from ....base import (
    ParticipantId,
    log, TRACE, DEBUG,
)
from ....base.events.bus import (
    EVENT_ID_REGISTER_EVENT,
    RegisterEventEvent,
    EventProtectionModel,
)
from ....base.util import (
    optional_key,
    T,
)

from ....base.validation import (
    assert_formatted, assert_all,
)
from .basic_event_bus import (
    BasicEventBus,
)


class _EventTypeInfo:
    """
    Description about the registered event type.
    """
    __slots__ = ('type', 'priority', 'protection',)

    def __init__(self, type_obj: Type[object], priority: QueuePriority, protection: EventProtectionModel) -> None:
        self.type = type_obj
        self.priority = priority
        self.protection = protection

    def __str__(self) -> str:
        return str(self.type)


class EventRegistry:
    """
    Registration of all event IDs and the expected class types.
    """

    _types: Dict[EventId, _EventTypeInfo]

    def __init__(self) -> None:
        self._types = {}

    def register(
            self, event_id: EventId, priority: QueuePriority,
            protection: EventProtectionModel,
            event_class: Type[T], example: T
    ) -> None:
        """
        Register an event ID with an expected event class.

        An example event must be provided for proper checking of the event,
        which ensures proper coding practice.

        Because event objects are tiny and short lived, all events MUST use
        __slots__.  In the same vein, event types do not need to be

        For now, safety is higher priority than minor gains in performance.  Thus,
        members should be made read-only to prevent mis-behaving listeners from
        changing event data.
        """
        log(TRACE, EventRegistry, 'registering {0} as {1}', event_id, event_class)
        BasicEventBus.assert_event_id(event_id)
        assert_all(
            'EventRegistry',
            'event object must be valid',

            (
                event_id != EVENT_WILDCARD,
                'cannot register an event wildcard as a formal event ID'
            ),
            isinstance(example, event_class),
            # Everything is an instance of object, so that's not a valid test.
            (
                not issubclass(event_class, dict),
                'event must be an object'
            ),
            (
                priority in QUEUE_EVENT_TYPES,
                'priority must be one of {0}; found {1}',
                (priority, QUEUE_EVENT_TYPES,),
            ),
            (
                event_id not in self._types,
                'event IDs can only be registered once',
            ),
            (
                not hasattr(example, '__dict__'),
                'event classes must provide the __slots__ member for itself and all parent classes',
            )
        )
        self._types[event_id] = _EventTypeInfo(event_class, priority, protection)
        log(DEBUG, EventRegistry, 'registered event {0} as type {1}', event_id, event_class)

    def has_event_id(self, event_id: EventId) -> bool:
        """Returns True if the event_id is properly registered, otherwise False."""
        return event_id in self._types

    @property
    def event_ids(self) -> Iterable[EventId]:
        """List of all registered event ids."""
        return self._types.keys()

    def get_event_id_priority(self, event_id: EventId) -> Optional[QueuePriority]:
        """The queue priority for the event."""
        if event_id in self._types:
            return self._types[event_id].priority
        return None

    def get_event_id_protection(self, event_id: EventId) -> Optional[EventProtectionModel]:
        if event_id in self._types:
            return self._types[event_id].protection
        return None

    def validate_event_on_trigger(
            self, event_id: EventId, target_id: ParticipantId, event_object: object
    ) -> None:
        """Validates that the event object is of the correct event id type when
        a trigger happened.  This is also a backdoor for the registry to notice
        when a event register event is created and to act upon it immediately.
        In this way, the event registry doesn't need a direct listener.
        Additionally, the event must be registered immediately, and not on a
        thread later on.  It also makes invalid registration have immediate
        feedback."""
        self.validate_event(event_id, target_id, event_object)
        if event_id == EVENT_ID_REGISTER_EVENT and isinstance(event_object, RegisterEventEvent):
            self.register(
                event_object.event_id,
                event_object.priority,
                event_object.protection,
                event_object.event_class,
                event_object.example
            )

    def validate_event(
            self, event_id: EventId, target_id: ParticipantId, event_object: object
    ) -> None:
        """Validates that the event object is of the correct event id type."""

        assert_all(
            'EventRegistry',
            'event ID invalid',

            # Don't need an assertion for event_object instanceof Event, because that
            # is implicitly handled in the isinstance of the registered type.
            (
                event_id in self._types,
                'event ID {0} must be registered as a valid event',
                (event_id,)
            ),
            (
                event_id in self._types and isinstance(event_object, self._types[event_id].type),
                'event {0} for target {1} used with event type {2} ({3}), but requires {4}',
                (
                    event_id, target_id,
                    type(event_object), event_object,
                    optional_key(self._types, event_id)
                )
            )
        )

    def validate_has(self, event_id: EventId) -> None:
        """Validates that the event id is correctly registered."""
        assert_formatted(
            event_id == EVENT_WILDCARD or event_id in self._types,
            'EventRegistry',
            'event validation',
            'event ID {0} must be registered as a valid event',
            event_id
        )
