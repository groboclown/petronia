
"""
Bootstrap the window parts.
"""

from .....aid.simp import (
    EventBus,
)
from .....aid.bootstrap import (
    register_event,
    QUEUE_EVENT_NORMAL,
    NOT_PARTICIPANT,
)
from .action_occurred import (
    EVENT_ID_NATIVE_WINDOW_CLOSED,
    NativeWindowClosedEvent,

    EVENT_ID_NATIVE_WINDOW_CREATED,
    NativeWindowCreatedEvent,

    EVENT_ID_NATIVE_WINDOW_MOVED,
    NativeWindowMovedEvent,

    EVENT_ID_NATIVE_WINDOW_FOCUSED,
    NativeWindowFocusedEvent,

    EVENT_ID_NATIVE_WINDOW_FLASHED,
    NativeWindowFlashedEvent,
)
from .action_requests import (
    EVENT_ID_REQUEST_CLOSE_NATIVE_WINDOW,
    RequestCloseNativeWindowEvent,

    EVENT_ID_REQUEST_FOCUS_NATIVE_WINDOW,
    RequestFocusNativeWindowEvent,

    EVENT_ID_REQUEST_MOVE_NATIVE_WINDOW,
    RequestMoveNativeWindowEvent,
)
from ..defs import (
    ScreenRect,
)


def register_window_events(bus: EventBus) -> None:
    """Register all the events"""
    register_event(
        bus, EVENT_ID_NATIVE_WINDOW_CLOSED, QUEUE_EVENT_NORMAL,
        NativeWindowClosedEvent, NativeWindowClosedEvent(False)
    )
    register_event(
        bus, EVENT_ID_NATIVE_WINDOW_CREATED, QUEUE_EVENT_NORMAL,
        NativeWindowCreatedEvent, NativeWindowCreatedEvent(NOT_PARTICIPANT)
    )
    register_event(
        bus, EVENT_ID_NATIVE_WINDOW_FLASHED, QUEUE_EVENT_NORMAL,
        NativeWindowFlashedEvent, NativeWindowFlashedEvent()
    )
    register_event(
        bus, EVENT_ID_NATIVE_WINDOW_FOCUSED, QUEUE_EVENT_NORMAL,
        NativeWindowFocusedEvent, NativeWindowFocusedEvent()
    )
    register_event(
        bus, EVENT_ID_NATIVE_WINDOW_MOVED, QUEUE_EVENT_NORMAL,
        NativeWindowMovedEvent, NativeWindowMovedEvent(ScreenRect(0, 0, 0, 0, 0, 0, 0, 0), True)
    )

    register_event(
        bus, EVENT_ID_REQUEST_CLOSE_NATIVE_WINDOW, QUEUE_EVENT_NORMAL,
        RequestCloseNativeWindowEvent, RequestCloseNativeWindowEvent(False)
    )
    register_event(
        bus, EVENT_ID_REQUEST_FOCUS_NATIVE_WINDOW, QUEUE_EVENT_NORMAL,
        RequestFocusNativeWindowEvent, RequestFocusNativeWindowEvent(False)
    )
    register_event(
        bus, EVENT_ID_REQUEST_MOVE_NATIVE_WINDOW, QUEUE_EVENT_NORMAL,
        RequestMoveNativeWindowEvent,
        RequestMoveNativeWindowEvent((0, 0, 0, 0,))
    )
