
"""
Startup the component stuff.
"""

from .....aid.bootstrap import (
    EventBus,
    QUEUE_EVENT_HIGH,
    register_event,
    NOT_PARTICIPANT,
)
from .events import (
    EVENT_ID_REQUEST_CREATE_CHROME_WRAPPER,
    RequestCreateChromeWrapperEvent,
)
from .chrome import Chrome


def register_component_events(bus: EventBus) -> None:
    register_event(
        bus, EVENT_ID_REQUEST_CREATE_CHROME_WRAPPER, QUEUE_EVENT_HIGH,
        RequestCreateChromeWrapperEvent, RequestCreateChromeWrapperEvent(NOT_PARTICIPANT, Chrome(NOT_PARTICIPANT), 0)
    )
