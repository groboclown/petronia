
"""
The events around system lifecycle.
"""

from ...internal.identity_types import (
    create_singleton_identity,
)
from ...internal.bus_types import (
    EventBus, EventId, EventCallback,
    ListenerSetup,
)

# Note: not "core".  This is not a plugin.
TARGET_ID_SYSTEM = create_singleton_identity('petronia.system')


EVENT_ID_SYSTEM_STARTED = EventId('petronia.system started')

class SystemStartedEvent:
    """
    Event to indicate that all the basic systems at boot time have finished
    running, and the system is now safe for end user actions.
    """
    __slots__ = ()

def as_system_started_listener(
        callback: EventCallback[SystemStartedEvent]
) -> ListenerSetup[SystemStartedEvent]:
    return (EVENT_ID_SYSTEM_STARTED, callback,)

# Halted events are not bubbled up to the API level, because these must be
# handled only by the core system and by a shutdown extension.
EVENT_ID_SYSTEM_HALTED = EventId('petronia.system halt')

class SystemHaltedEvent:
    """
    Stop the system immediately.
    """
    __slots__ = ()

    # TODO look at forcing a signature on this event.

def as_system_halted_listener(
    callback: EventCallback[SystemHaltedEvent]
) -> ListenerSetup[SystemHaltedEvent]:
    return (EVENT_ID_SYSTEM_HALTED, callback,)

def send_system_halted(bus: EventBus) -> None:
    bus.trigger(EVENT_ID_SYSTEM_HALTED, TARGET_ID_SYSTEM, SystemHaltedEvent())
