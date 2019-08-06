
"""
Sets up the timer.
"""

from .events import (
    EVENT_ID_TIMER, GLOBAL_TIMER_EVENT,
    TimerEvent,
)
from ....base.bus import (
    EventBus,
    QUEUE_EVENT_NORMAL,
    ExtensionMetadataStruct,
)
from ....base.events import (
    register_event,
)
from ....core.extensions.api import (
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
    "name": "core.timer.api",
    "version": (1, 0, 0,),

    "type": "api",
    "depends": [
        {
            "extension": "core.shutdown.api",
            "minimum": ANY_VERSION,
        }
    ],
    "defaults": [
        {
            "extension": "default.timer",
            "minimum": ANY_VERSION,
        }
    ],
    "authors": ["Petronia"],
}
