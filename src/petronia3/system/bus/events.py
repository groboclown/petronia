
"""
The common list of events for this module.
"""

from typing import Type
from .event_bus import EventId, QueuePriority
from .typesafe_types import TypeSafeEventCallback, ListenerSetup
from .typesafe_events import (
    EVENT_ID_EVENT_LISTENER_ADDED,
    EventListenerAddedEvent,

    EVENT_ID_REGISTER_EVENT,
    RegisterEventEvent,
)
from .typesafe import TypeSafeEventBus
from ..participant import create_singleton_identity
from ...util.memory import T

TARGET_EVENT_BUS = create_singleton_identity('event-bus')
TARGET_EVENT_REGISTRY = create_singleton_identity('event-registry')


def as_listener_added_listener(
        callback: TypeSafeEventCallback[EventListenerAddedEvent]
) -> ListenerSetup[EventListenerAddedEvent]:
    """A ListenerRegistrator type."""
    return (EVENT_ID_EVENT_LISTENER_ADDED, callback,)


def register_event(
        bus: TypeSafeEventBus, event_id: EventId, priority: QueuePriority,
        event_class: Type[T], example: T
) -> None:
    bus.trigger(
        EVENT_ID_REGISTER_EVENT, TARGET_EVENT_REGISTRY,
        RegisterEventEvent(event_id, priority, event_class, example)
    )
