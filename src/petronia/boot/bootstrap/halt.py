
"""
Special logic for handling shutdown events.

On shutdown requests,
"""

import sys
from ...base import (
    ParticipantId,
    log,
    INFO, DEBUG,
)
from ...base.bus import (
    EventBus,
    EventCallback,
    EventId,
    ListenerSetup,
)
from ...base.events.system_events import (
    TARGET_ID_SYSTEM,

    SystemHaltedEvent,
    EVENT_ID_SYSTEM_HALTED,
)
from ...defimpl.bus.local.bus_queue import BusQueueManager


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
        log(DEBUG, bootstrap_halt, 'Initiating Petronia halt.')
        queue.stop(timeout_seconds)
        log(INFO, bootstrap_halt, 'Petronia stopped.')
        sys.exit(0)


    # Cannot deregister this listener, because when it's no longer needed,
    # there will no longer be an event bus to run against.
    log(DEBUG, bootstrap_halt, 'Adding halt listener')
    bus.add_listener(
        TARGET_ID_SYSTEM, _as_halt_listener, on_halt
    )
    log(DEBUG, bootstrap_halt, 'Added halt listener')


def _as_halt_listener(
        callback: EventCallback[SystemHaltedEvent]
) -> ListenerSetup[SystemHaltedEvent]:
    return (EVENT_ID_SYSTEM_HALTED, callback,)
