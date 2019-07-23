
"""
Setup the system singletons.  These are required by all Petronia systems in
order to run.

Singletons must be configured through the event bus.
"""

from petronia3.system.bus import (
    EventBus
)
from petronia3_ext.bus.local.basic_event_bus import QueueFunction
from petronia3_ext.bus.local.bootstrap import bootstrap_event_bus

def create_core_system(queuer: QueueFunction) -> EventBus:
    """
    Create the core Petronia system, wired up to the event bus,
    to create a minimal working environment.

    After this setup, the additional configuration and platform
    specific parts can be loaded.
    """

    # Ordering here is incredibly important.
    bus = bootstrap_event_bus(queuer)


    # Note: logging does not need any bootstrapping into the singletons,
    # because the core logging system lives outside the events.

    return bus
