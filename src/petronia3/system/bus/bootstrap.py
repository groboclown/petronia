
"""
Bootstraps singletons and event registration.
"""

from .event_bus import (
    EventId, QueueFunction, EventBus,
    QUEUE_EVENT_NORMAL, QUEUE_EVENT_NOW
)
from .typesafe_types import TypeSafeEventCallback, ListenerSetup
from .typesafe import TypeSafeEventBus
from .event_registry import EventRegistry
from .events import (
    TARGET_EVENT_REGISTRY,

    EVENT_ID_REGISTER_EVENT, RegisterEventEvent,

    EVENT_ID_EVENT_LISTENER_ADDED, EventListenerAddedEvent
)
from ..participant import ParticipantId


def bootstrap_event_bus(queuer: QueueFunction) -> TypeSafeEventBus:
    """
    Creates a type-safe event bus singleton, with the event registry properly
    wired into it.
    """
    bus = EventBus(queuer)
    evtr = EventRegistry()

    # In order for the event registry to not be passed around to everything, the registration
    # is handled through the bus event.  This means, though, that the registration listener
    # must be set up before anything else.
    register_event_registry_events(evtr)

    ret = TypeSafeEventBus(bus, evtr)

    add_event_registry_listener(ret, evtr)

    return ret


def register_event_registry_events(evtr: EventRegistry) -> None:
    """For internal use and test support."""
    evtr.register(
        # Registration of event tyeps is done immediately, so that there isn't conflict with
        # trying to send out events right after registering them.
        EVENT_ID_REGISTER_EVENT, QUEUE_EVENT_NOW,
        RegisterEventEvent,
        RegisterEventEvent(EVENT_ID_REGISTER_EVENT, QUEUE_EVENT_NOW, object, object())
    )

    # Because we're adding a listener here, we want to avoid an error with an un-registered
    # event by adding the event registration now.
    evtr.register(
        EVENT_ID_EVENT_LISTENER_ADDED, QUEUE_EVENT_NORMAL,
        EventListenerAddedEvent,
        EventListenerAddedEvent(EVENT_ID_EVENT_LISTENER_ADDED, TARGET_EVENT_REGISTRY)
    )


def add_event_registry_listener(bus: TypeSafeEventBus, evtr: EventRegistry) -> None:
    """For internal use and test support."""
    # Ignore the listener ID.  This listener is tightly coupled with the event bus,
    # and must stay around as long as the event bus is around.
    bus.add_listener(
        TARGET_EVENT_REGISTRY, _as_register_event_listener,
        _EventRegistryListener(evtr)
    )



def _as_register_event_listener(
        callback: TypeSafeEventCallback[RegisterEventEvent]
) -> ListenerSetup[RegisterEventEvent]:
    return (EVENT_ID_REGISTER_EVENT, callback,)


class _EventRegistryListener:
    __slots__ = ('reg',)
    def __init__(self, reg: EventRegistry) -> None:
        self.reg = reg

    def __call__(
            self, eid: EventId, tid: ParticipantId, evt: RegisterEventEvent # pylint: disable=unused-argument
    ) -> None:
        self.reg.register(
            evt.event_id, evt.priority, evt.event_class, evt.example
        )
