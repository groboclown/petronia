
"""
Setup the barest core system needed by Petronia.  This involves assigning the
event bus implementation, then registering the core Petronia events and event
listeners.  No other extensions are added to the system.
"""

from ...base import (
    EventBus
)

from ...defimpl.bus.local.basic_event_bus import QueueFunction
from ...defimpl.bus.local.bootstrap import bootstrap_event_bus


def create_bus(queuer: QueueFunction) -> EventBus:
    """
    Create the core Petronia system, wired up to the event bus,
    to create a minimal working environment.

    After this setup, the additional configuration and platform
    specific parts can be loaded.
    """

    # Setup the event bus and its most basic internal registration.
    bus = bootstrap_event_bus(queuer)

    # Note: logging does not need any bootstrapping into the singletons,
    # because the core logging system lives outside the events.

    return bus
