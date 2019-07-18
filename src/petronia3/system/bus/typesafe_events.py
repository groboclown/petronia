
"""
The common list of events for this module.
"""

from typing import Type, Generic
from .event_bus import EventId, QueuePriority
from ..participant import ParticipantId, create_singleton_identity
from ...util.memory import T

TARGET_EVENT_BUS = create_singleton_identity('event-bus')
TARGET_EVENT_REGISTRY = create_singleton_identity('event-registry')

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


EVENT_ID_REGISTER_EVENT = EventId('event-registry register-event')


class RegisterEventEvent(Generic[T]):
    """
    A request to add an event to the registration.
    """
    __slots__ = ('__event_id', '__priority', '__event_class', '__example',)
    def __init__(
            self, event_id: EventId, priority: QueuePriority,
            event_class: Type[T], example: T
    ) -> None:
        self.__event_id = event_id
        self.__priority = priority
        self.__event_class = event_class
        self.__example = example

    @property
    def event_id(self) -> EventId:
        """The event_id"""
        return self.__event_id

    @property
    def priority(self) -> QueuePriority:
        """The event priority"""
        return self.__priority

    @property
    def event_class(self) -> Type[T]:
        """The class of the event objects."""
        return self.__event_class

    @property
    def example(self) -> T:
        """An example of the event class."""
        return self.__example
