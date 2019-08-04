
"""
The common list of event bus events.
"""

from typing import Type, Generic
from .bus_types import (
    EventId, QueuePriority,
    EventBus, EventCallback,
    ListenerSetup,
)
from .identity_types import (
    ParticipantId,
    create_singleton_identity,
)
from ...util.memory import T


# Note: not "core".
TARGET_EVENT_BUS = create_singleton_identity('petronia.bus.api')
TARGET_EVENT_REGISTRY = create_singleton_identity('petronia.bus.event-registry')

EVENT_ID_EVENT_LISTENER_ADDED = EventId('petronia.bus.event-registry listener-add')


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


EVENT_ID_REGISTER_EVENT = EventId('petronia.bus.event-registry register-event')


class RegisterEventEvent(Generic[T]):
    """
    A request to add an event to the registration.
    """
    __slots__ = ('_event_id', '_priority', '_event_class', '_example',)
    def __init__(
            self, event_id: EventId, priority: QueuePriority,
            event_class: Type[T], example: T
    ) -> None:
        self._event_id = event_id
        self._priority = priority
        self._event_class = event_class
        self._example = example

    @property
    def event_id(self) -> EventId:
        """The event_id"""
        return self._event_id

    @property
    def priority(self) -> QueuePriority:
        """The event priority"""
        return self._priority

    @property
    def event_class(self) -> Type[T]:
        """The class of the event objects."""
        return self._event_class

    @property
    def example(self) -> T:
        """An example of the event class."""
        return self._example


def as_listener_added_listener(
        callback: EventCallback[EventListenerAddedEvent]
) -> ListenerSetup[EventListenerAddedEvent]:
    """A ListenerRegistrator type."""
    return (EVENT_ID_EVENT_LISTENER_ADDED, callback,)


def register_event(
        bus: EventBus, event_id: EventId, priority: QueuePriority,
        event_class: Type[T], example: T
) -> None:
    """
    Requests the registration of a new event ID into the event bus.
    Until this is called, events of this ID will be rejected because it is
    not registered.
    """
    bus.trigger(
        EVENT_ID_REGISTER_EVENT, TARGET_EVENT_REGISTRY,
        RegisterEventEvent(event_id, priority, event_class, example)
    )

def as_register_event_listener(
        callback: EventCallback[RegisterEventEvent[T]]
) -> ListenerSetup[RegisterEventEvent[T]]:
    """A ListenerRegistraror type"""
    return (EVENT_ID_REGISTER_EVENT, callback,)
