
"""
Special logic for handling shutdown events.

On shutdown requests,
"""

import sys
from petronia3.system.bus import (
    EventBus,
    EventCallback,
    EventId,
    ListenerSetup,
)
from petronia3.system.events.api.system_events import (
    TARGET_ID_SYSTEM,

    SystemHaltedEvent,
    EVENT_ID_SYSTEM_HALTED,
)
from petronia3.system.participant import ParticipantId
from petronia3.system.logging import (
    log, VERBOSE,
)
from petronia3_ext.bus.local.bus_queue import BusQueueManager


def bootstrap_halt(bus: EventBus, queue: BusQueueManager, timeout_seconds: float) -> None:
    """
    Create an event bus that listens for shutdown requests, and handles them
    internally.
    """

    def on_halt(
            event_id: EventId, # pylint: disable=unused-argument
            target_id: ParticipantId, # pylint: disable=unused-argument
            event_obj: SystemHaltedEvent # pylint: disable=unused-argument
    ) -> None:
        queue.stop(timeout_seconds)
        log(VERBOSE, bootstrap_halt, 'Petronia stopped.')
        sys.exit(0)


    # Cannot deregister this listener, because when it's no longer needed,
    # there will no longer be an event bus to run against.
    bus.add_listener(
        TARGET_ID_SYSTEM, _as_halt_listener, on_halt
    )


def _as_halt_listener(
        callback: EventCallback[SystemHaltedEvent]
) -> ListenerSetup[SystemHaltedEvent]:
    return (EVENT_ID_SYSTEM_HALTED, callback,)
