
"""
Events for the timer.
"""

from ....system.participant import (
    create_singleton_identity,
)
from ....system.bus import (
    EventCallback, ListenerSetup, EventId,
)

TARGET_TIMER = create_singleton_identity('global-timer')

EVENT_ID_TIMER = EventId('timer tick')

class TimerEvent:
    """
    The most basic timer event.  It contains no state, and so
    is only ever created once.
    """
    __slots__ = tuple('name',)


def as_timer_listener(
    callback: EventCallback[TimerEvent]
) -> ListenerSetup[TimerEvent]:
    return (EVENT_ID_TIMER, callback,)


GLOBAL_TIMER_EVENT = TimerEvent()
