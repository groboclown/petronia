
"""
Bootstrap the window parts.
"""

from .....aid.std import (
    EventBus,
)
from .....aid.bootstrap import (
    register_event,
    QUEUE_EVENT_NORMAL,
    QUEUE_EVENT_HIGH,
    NOT_PARTICIPANT,
    CONSUME_EVENT_PROTECTION,
    REQUEST_EVENT_PROTECTION,
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

    EVENT_ID_REQUEST_SET_NATIVE_WINDOW_VISIBILITY,
    RequestSetNativeWindowVisibility,

    EVENT_ID_REQUEST_SET_NATIVE_WINDOW_STYLE,
    RequestSetNativeWindowStyleEvent,
)
from ..defs import (
    ScreenRect,
)
from .state import (
    NativeWindowState,
)

EMPTY_SCREEN_RECT = ScreenRect(0, 0, 0, 0, 0, 0, 0, 0)


def register_window_events(bus: EventBus) -> None:
    """Register all the events"""
    # Notification of a window event is immediate.
    # This will be handled before the state change event.
    register_event(
        bus, EVENT_ID_NATIVE_WINDOW_CLOSED, QUEUE_EVENT_HIGH, CONSUME_EVENT_PROTECTION,
        NativeWindowClosedEvent, NativeWindowClosedEvent(False)
    )
    register_event(
        bus, EVENT_ID_NATIVE_WINDOW_CREATED, QUEUE_EVENT_HIGH, CONSUME_EVENT_PROTECTION,
        NativeWindowCreatedEvent, NativeWindowCreatedEvent(NOT_PARTICIPANT, NativeWindowState(
            NOT_PARTICIPANT, '', 0, {}, EMPTY_SCREEN_RECT, EMPTY_SCREEN_RECT,
            {}, False, False, False
        ))
    )
    register_event(
        bus, EVENT_ID_NATIVE_WINDOW_FLASHED, QUEUE_EVENT_HIGH, CONSUME_EVENT_PROTECTION,
        NativeWindowFlashedEvent, NativeWindowFlashedEvent()
    )
    register_event(
        bus, EVENT_ID_NATIVE_WINDOW_FOCUSED, QUEUE_EVENT_HIGH, CONSUME_EVENT_PROTECTION,
        NativeWindowFocusedEvent, NativeWindowFocusedEvent()
    )
    register_event(
        bus, EVENT_ID_NATIVE_WINDOW_MOVED, QUEUE_EVENT_HIGH, CONSUME_EVENT_PROTECTION,
        NativeWindowMovedEvent, NativeWindowMovedEvent(EMPTY_SCREEN_RECT, True)
    )

    register_event(
        bus, EVENT_ID_REQUEST_CLOSE_NATIVE_WINDOW, QUEUE_EVENT_NORMAL, REQUEST_EVENT_PROTECTION,
        RequestCloseNativeWindowEvent, RequestCloseNativeWindowEvent(False)
    )
    register_event(
        bus, EVENT_ID_REQUEST_FOCUS_NATIVE_WINDOW, QUEUE_EVENT_NORMAL, REQUEST_EVENT_PROTECTION,
        RequestFocusNativeWindowEvent, RequestFocusNativeWindowEvent(False)
    )
    register_event(
        bus, EVENT_ID_REQUEST_MOVE_NATIVE_WINDOW, QUEUE_EVENT_NORMAL, REQUEST_EVENT_PROTECTION,
        RequestMoveNativeWindowEvent,
        RequestMoveNativeWindowEvent((0, 0, 0, 0,))
    )
    register_event(
        bus, EVENT_ID_REQUEST_SET_NATIVE_WINDOW_VISIBILITY, QUEUE_EVENT_NORMAL, REQUEST_EVENT_PROTECTION,
        RequestSetNativeWindowVisibility,
        RequestSetNativeWindowVisibility(False)
    )

    # This is a high priority event, because it will need to be sent right after
    # the window is created.
    register_event(
        bus, EVENT_ID_REQUEST_SET_NATIVE_WINDOW_STYLE, QUEUE_EVENT_HIGH, REQUEST_EVENT_PROTECTION,
        RequestSetNativeWindowStyleEvent, RequestSetNativeWindowStyleEvent({})
    )
