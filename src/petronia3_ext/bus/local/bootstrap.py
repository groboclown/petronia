
"""
Bootstraps singletons and event registration.
"""

from petronia3.system.bus import (
    EventBus,
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
    register_core_events(evtr)

    ret = TypeSafeEventBus(bus, evtr)

    # The event registry does not need a listener for the register event
    # event, because it has a backdoor in the TypeSafeEventBus.

    return ret


def register_core_events(evtr: EventRegistry) -> None:
    """For internal use and test support."""
    core_events = bootstrap_core_events() # type: ignore
    for event_id, priority, event_class, event_example in core_events: # type: ignore
        evtr.register(
            event_id,
            priority,
            event_class, # type: ignore
            event_example # type: ignore
        )
