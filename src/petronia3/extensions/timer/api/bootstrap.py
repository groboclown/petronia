
"""
Sets up the timer.
"""

from .events import (
    EVENT_ID_TIMER, GLOBAL_TIMER_EVENT,
    TimerEvent,
)
from ....system.bus import (
    EventBus,
    register_event,
    ExtensionMetadataStruct,
    QUEUE_EVENT_NORMAL,
)
from ....extensions.extensions.api import (
    ANY_VERSION,
)


def bootstrap_timer_api(bus: EventBus) -> None:
    """
    Get the timer started.

    There should only ever be one timer.  It is global, and should never be
    disabled.
    """
    register_event(
        bus,
        EVENT_ID_TIMER,
        QUEUE_EVENT_NORMAL,
        TimerEvent,
        GLOBAL_TIMER_EVENT
    )


EXTENSION_METADATA: ExtensionMetadataStruct = {
    "type": "api",
    "depends": [
        {
            "name": "core.shutdown.api",
            "minimum": ANY_VERSION,
        }
    ],
    "authors": ["Petronia"],
}
