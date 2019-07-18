
"""
Setup the system singletons.  These are required by all Petronia systems in
order to run.

Singletons must be configured through the event bus.
"""

from ..system import (
    TypeSafeEventBus
)
from ..system.bus.event_bus import QueueFunction
from ..system.bus.bootstrap import bootstrap_event_bus
from ..system.participant.bootstrap import bootstrap_participant
from ..system.registrar.bootstrap import bootstrap_registrar
from ..system.state.bootstrap import bootstrap_state_store

def create_core_system(queuer: QueueFunction) -> TypeSafeEventBus:
    """
    Create the core Petronia system, wired up to the event bus,
    to create a minimal working environment.

    After this setup, the additional configuration and platform
    specific parts can be loaded.
    """

    # Ordering here is incredibly important.
    bus = bootstrap_event_bus(queuer)
    bootstrap_participant(bus)
    bootstrap_registrar(bus)
    bootstrap_state_store(bus)

    # Note: logging does not need any bootstrapping into the singletons,
    # because the core logging system lives outside the events.

    return bus
