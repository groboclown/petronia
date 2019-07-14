"""
Type-safe event bus.

Includes firing events on event listener adding.
"""

from typing import Callable
from .bus import (
    EventBus, EventCallback, EventId, ListenerId,
    TARGET_WILDCARD,
    QUEUE_EVENT_NORMAL,
)
from ..participant import ParticipantId
from .event import EventRegistry
from ...util.memory import T

TypeSafeEventCallback = Callable[[str, str, T], None]


EVENT_ID_EVENT_LISTENER_ADDED = EventId('event-bus listener-add')
EVENT_ID_EVENT_LISTENER_REMOVED = EventId('event-bus listener-remove')


class EventListenerAddedEvent:
    """
    Information about the added event listener.

    The event_id value will be the target_id for the fired event.
    """
    __slots__ = ('__event_id',)
    def __init__(self, event_id: str) -> None:
        self.__event_id = event_id

    @property
    def event_id(self) -> str:
        """The event_id listened to."""
        return self.__event_id

class EventListenerRemovedEvent:
    """
    Information about the removed event listener.

    The event_id value will be the target_id for the fired event.
    """
    __slots__ = ('__event_id',)
    def __init__(self, event_id: str) -> None:
        self.__event_id = event_id

    @property
    def event_id(self) -> str:
        """The event_id listened to."""
        return self.__event_id


def register_events(evtr: EventRegistry) -> None:
    """
    Register the type-safe bus events.
    """
    evtr.register(
        EVENT_ID_EVENT_LISTENER_ADDED, QUEUE_EVENT_NORMAL,
        EventListenerAddedEvent, EventListenerAddedEvent('event')
    )
    evtr.register(
        EVENT_ID_EVENT_LISTENER_REMOVED, QUEUE_EVENT_NORMAL,
        EventListenerRemovedEvent,
        EventListenerRemovedEvent('event')
    )


class TypeSafeEventBus:
    """
    A type-safe version of the EventBus.
    """
    def __init__(self, bus: EventBus, reg: EventRegistry) -> None:
        assert isinstance(bus, EventBus)
        assert isinstance(reg, EventRegistry)
        self.__bus = bus
        self.__reg = reg

    def add_listener(self, event_id: EventId, target_id: ParticipantId, listener: TypeSafeEventCallback[T]) -> ListenerId:
        """
        Registers a type-safe event listener.  Cannot work with a wildcard event ID.

        Each event type should have a custom call function to wrap this.
        """
        self.__reg.validate_has(event_id)
        callback = lambda eid, tid, eo: self.__listener_callback(eid, tid, eo, listener) # type: ignore
        ret = self.__bus.add_listener(
            event_id,
            target_id,
            callback
        )
        self.trigger(EVENT_ID_EVENT_LISTENER_ADDED, TARGET_WILDCARD, EventListenerAddedEvent(event_id))
        return ret

    def deregister(self, event_id: EventId, listener_id: ListenerId) -> bool:
        """De-register the listener."""
        if self.__bus.deregister(listener_id):
            self.trigger(EVENT_ID_EVENT_LISTENER_REMOVED, TARGET_WILDCARD, EventListenerRemovedEvent(event_id))
            return True
        return False

    def trigger(self, event_id: EventId, target_id: ParticipantId, event_obj: T) -> None:
        """
        Triggers an event to fire.  The event priority is based upon the
        event id registration.
        """
        self.__reg.validate_event(event_id, target_id, event_obj)
        priority = self.__reg.get_event_id_priority(event_id)
        assert priority
        self.__bus.trigger(priority, event_id, target_id, event_obj)


    def __listener_callback(
            self, event_id: EventId, target_id: ParticipantId, event_obj: object, callback: EventCallback
    ) -> None:
        self.__reg.validate_event(event_id, target_id, event_obj)
        callback(event_id, target_id, event_obj)
