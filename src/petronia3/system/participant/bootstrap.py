
"""
Bootstrap the event registration.
"""

from .events import (
    EVENT_ID_REQUEST_DISPOSE,
    RequestDisposeEvent,

    EVENT_ID_DISPOSE_COMPLETE,
    DisposeCompleteEvent,
)
from .identity import NOT_PARTICIPANT
from ..bus import (
    TypeSafeEventBus, register_event,
    QUEUE_EVENT_NORMAL,
)


def bootstrap_participant(bus: TypeSafeEventBus) -> None:
    """
    Register the events.
    """
    register_event(
        bus,
        EVENT_ID_REQUEST_DISPOSE,
        QUEUE_EVENT_NORMAL,
        RequestDisposeEvent,
        RequestDisposeEvent(NOT_PARTICIPANT)
    )
    register_event(
        bus,
        EVENT_ID_DISPOSE_COMPLETE,
        QUEUE_EVENT_NORMAL,
        DisposeCompleteEvent,
        DisposeCompleteEvent(NOT_PARTICIPANT)
    )
