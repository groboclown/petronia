
"""
Startup the component stuff.
"""

from .....aid.simp import (
    EventBus,
)
from .....aid.bootstrap import (
    QUEUE_EVENT_HIGH,
    register_event,
    NOT_PARTICIPANT,
)
from .events import (
    EVENT_ID_CHROME_WRAPPED_WINDOW,
    ChromeWrappedWindowEvent,
)


def register_component_events(bus: EventBus) -> None:
    register_event(
        bus, EVENT_ID_CHROME_WRAPPED_WINDOW, QUEUE_EVENT_HIGH,
        ChromeWrappedWindowEvent, ChromeWrappedWindowEvent(NOT_PARTICIPANT, NOT_PARTICIPANT)
    )
