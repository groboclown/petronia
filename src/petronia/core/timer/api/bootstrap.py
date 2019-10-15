
"""
Sets up the timer.
"""

from .events import (
    EVENT_ID_TIMER, GLOBAL_TIMER_EVENT,
    TimerEvent,
)
from ....aid.bootstrap import (
    EventBus,
    QUEUE_EVENT_NORMAL,
    register_event,
    CONSUME_EVENT_PROTECTION,
    ANY_VERSION,
)
from ....base.internal_.internal_extension import petronia_extension


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
        CONSUME_EVENT_PROTECTION,
        TimerEvent,
        GLOBAL_TIMER_EVENT
    )


EXTENSION_METADATA = petronia_extension({
    "name": "core.timer.api",
    "version": (1, 0, 0,),

    "type": "api",
    "depends": ({
        "extension": "core.shutdown.api",
        "minimum": ANY_VERSION,
    },),
    "defaults": ({
        "extension": "default.timer",
        "minimum": ANY_VERSION,
    },),
})
