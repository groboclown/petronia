
"""
Events for the timer.
"""

from ....base import (
    EventCallback,
    EventId,
    EventBus,
    create_singleton_identity,
)
from ....base.bus import ListenerSetup

TARGET_TIMER = create_singleton_identity('core.timer.api')

EVENT_ID_TIMER = EventId('core.timer.api tick')


class TimerEvent:
    """
    The most basic timer event.  It contains no state, and so
    is only ever created once.
    """
    __slots__ = ()


def as_timer_listener(
    callback: EventCallback[TimerEvent]
) -> ListenerSetup[TimerEvent]:
    return (EVENT_ID_TIMER, callback,)


GLOBAL_TIMER_EVENT = TimerEvent()


def send_timer_event(bus: EventBus) -> None:
    bus.trigger(EVENT_ID_TIMER, TARGET_TIMER, GLOBAL_TIMER_EVENT)
