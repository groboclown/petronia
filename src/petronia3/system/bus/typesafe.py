"""
Type-safe event bus.

Includes firing events on event listener adding.
"""

from typing import Callable, Tuple
from .bus import (
    EventBus, EventCallback, EventId, ListenerId,
    TARGET_WILDCARD,
    QUEUE_EVENT_NORMAL,
)
from ..participant import ParticipantId, NOT_PARTICIPANT
from .event import EventRegistry
from ...util.memory import T

TypeSafeEventCallback = Callable[[EventId, ParticipantId, T], None]
ListenerSetup = Tuple[EventId, TypeSafeEventCallback[T]]
ListenerRegistrator = Callable[[TypeSafeEventCallback[T]], ListenerSetup[T]]


EVENT_ID_EVENT_LISTENER_ADDED = EventId('event-bus listener-add')


class EventListenerAddedEvent:
    """
    Information about the added event listener.

    There is no event triggered for removing an event listener.
    """
    __slots__ = ('_event_id', '_target_id',)
    def __init__(self, event_id: EventId, target_id: ParticipantId) -> None:
        self._event_id = event_id
        self._target_id = target_id

    @property
    def event_id(self) -> EventId:
        """The event_id listened to."""
        return self._event_id

    @property
    def target_id(self) -> ParticipantId:
        """The target_id listened to."""
        return self._target_id


def register_events(evtr: EventRegistry) -> None:
    """
    Register the type-safe bus events.
    """
    evtr.register(
        EVENT_ID_EVENT_LISTENER_ADDED, QUEUE_EVENT_NORMAL,
        EventListenerAddedEvent, EventListenerAddedEvent(EventId('event'), NOT_PARTICIPANT)
    )


def as_listener_added_listener(
        callback: TypeSafeEventCallback[EventListenerAddedEvent]
) -> ListenerSetup[EventListenerAddedEvent]:
    """A ListenerRegistrator type."""
    return (EVENT_ID_EVENT_LISTENER_ADDED, callback,)


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
