
# mypy: allow-any-expr
# mypy: allow-any-generics

"""
Bootstraps singletons and event registration.
"""

from .typesafe import TypeSafeEventBus
from .event_registry import EventRegistry
from ....base import (
    EventBus,
)
from ....base.events.bootstrap import bootstrap_core_events
from .basic_event_bus import (
    BasicEventBus, QueueFunction,
)


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


def register_core_events(event_reg: EventRegistry) -> None:
    """For internal use and test support."""
    core_events = bootstrap_core_events()
    for event_id, priority, protection, event_class, event_example in core_events:  # type: ignore
        event_reg.register(
            event_id,
            priority,
            protection,
            event_class,  # type: ignore
            event_example  # type: ignore
        )
