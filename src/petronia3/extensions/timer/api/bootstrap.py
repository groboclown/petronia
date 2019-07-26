
"""
Sets up the timer.
"""

from typing import Sequence
from .events import (
    EVENT_ID_TIMER, GLOBAL_TIMER_EVENT,
    TimerEvent,
)
from ....system.bus import (
    EventBus,
    register_event,
    QUEUE_EVENT_NORMAL,
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
