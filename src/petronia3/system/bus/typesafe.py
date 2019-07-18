"""
Type-safe event bus.

Includes firing events on event listener adding.
"""

from .event_bus import (
    EventBus, EventCallback, EventId, ListenerId,
    TARGET_WILDCARD,
)
from .event_registry import EventRegistry
from .typesafe_types import ListenerRegistrator, TypeSafeEventCallback
from .typesafe_events import (
    EventListenerAddedEvent,
    EVENT_ID_EVENT_LISTENER_ADDED,
)
from ..participant import ParticipantId
from ...util.memory import T



class TypeSafeEventBus:
    """
    A type-safe version of the EventBus.
    """
    __slots__ = ('_bus', '_reg')
    def __init__(self, bus: EventBus, reg: EventRegistry) -> None:
        assert isinstance(bus, EventBus)
        assert isinstance(reg, EventRegistry)
        self._bus = bus
        self._reg = reg

    def add_listener(
            self,
            target_id: ParticipantId, listener_setup: ListenerRegistrator,
            listener: TypeSafeEventCallback[T]
    ) -> ListenerId:
        """
        Registers a type-safe event listener.  Cannot work with a wildcard event ID.

        Each event type should have a custom call function to wrap this.
        """
        event_id, listener = listener_setup(listener)
        self._reg.validate_has(event_id)
        callback = lambda eid, tid, eo: self.__listener_callback(eid, tid, eo, listener) # type: ignore
        ret = self._bus.add_listener(
            event_id,
            target_id,
            callback
        )

        # Event added trigger is always sent after registration.  This means
        # that event listeners must be aware of the potential for infinite loops if written wrong.
        # This is sent after, and not before, because the threading model may just end up
        # getting this to run after the method completes anyway.
        self.trigger(EVENT_ID_EVENT_LISTENER_ADDED, TARGET_WILDCARD, EventListenerAddedEvent(event_id, target_id))

        return ret

    def remove_listener(self, listener_id: ListenerId) -> bool:
        """De-register the listener."""
        return self._bus.remove_listener(listener_id)

    def trigger(self, event_id: EventId, target_id: ParticipantId, event_obj: T) -> None:
        """
        Triggers an event to fire.  The event priority is based upon the
        event id registration.
        """
        self._reg.validate_event(event_id, target_id, event_obj)
        priority = self._reg.get_event_id_priority(event_id)
        assert priority
        self._bus.trigger(priority, event_id, target_id, event_obj)


    def __listener_callback(
            self, event_id: EventId, target_id: ParticipantId, event_obj: object, callback: EventCallback
    ) -> None:
        self._reg.validate_event(event_id, target_id, event_obj)
        callback(event_id, target_id, event_obj)
