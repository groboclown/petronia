
"""
Native window states and notifications.
"""

from .state import (
    AllActiveWindowsState,
    NativeWindowState,
)
from .action_requests import (
    RequestMoveNativeWindowEvent,
    EVENT_ID_REQUEST_MOVE_NATIVE_WINDOW,
    as_request_move_native_window_listener,
    send_request_move_native_window_event,

    RequestFocusNativeWindowEvent,
    EVENT_ID_REQUEST_FOCUS_NATIVE_WINDOW,
    as_request_focus_native_window_listener,
    send_request_focus_native_window_event,

    RequestCloseNativeWindowEvent,
    EVENT_ID_REQUEST_CLOSE_NATIVE_WINDOW,
    as_request_close_native_window_listener,
    send_request_close_native_window_event,
)
from .action_occurred import (
    NativeWindowCreatedEvent,
    EVENT_ID_NATIVE_WINDOW_CREATED,
    as_native_window_created_listener,
    send_native_window_created_event,
    TARGET_ID_WINDOW_CREATION,

    NativeWindowClosedEvent,
    EVENT_ID_NATIVE_WINDOW_CLOSED,
    as_native_window_closed_listener,
    send_native_window_closed_event,

    NativeWindowFlashedEvent,
    EVENT_ID_NATIVE_WINDOW_FLASHED,
    as_native_window_flashed_listener,
    send_native_window_flashed_event,

    NativeWindowFocusedEvent,
    EVENT_ID_NATIVE_WINDOW_FOCUSED,
    as_native_window_focused_listener,
    send_native_window_focused_event,

    NativeWindowMovedEvent,
    EVENT_ID_NATIVE_WINDOW_MOVED,
    as_native_window_moved_listener,
    send_native_window_moved_event,
)
