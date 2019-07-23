
"""
Bootstraps singletons and event registration.
"""

from petronia3.system.bus import (
    EventId, EventBus,
    EventCallback, ListenerSetup,
)
from petronia3.system.participant import (
    ParticipantId,
)
from petronia3.system.events import (
    TARGET_EVENT_REGISTRY,

    EVENT_ID_REGISTER_EVENT, RegisterEventEvent,
)
from petronia3.system.events.api.bootstrap import bootstrap_core_events
from .basic_event_bus import (
    BasicEventBus, QueueFunction,
)
from .typesafe import TypeSafeEventBus
from .event_registry import EventRegistry


def bootstrap_event_bus(queuer: QueueFunction) -> EventBus:
    """
    Creates a type-safe event bus singleton, with the event registry properly
    wired into it.
    """
    bus = BasicEventBus(queuer)
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
    core_events = bootstrap_core_events()
    for event_id, priority, event_class, event_example in core_events:
        evtr.register(
            event_id,
            priority,
            event_class,
            event_example
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
        callback: EventCallback[RegisterEventEvent]
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
