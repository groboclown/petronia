
"""
API that the platform components must implement.

This defines what is expected from the platform runtime implementation.
"""

from .bootstrap import bootstrap_platform_api as start_extension
from .bootstrap import EXTENSION_METADATA


from .defs import (
    RespondsToAction,

    ColorRGBA,
    ColorStr,
    Color,

    TextFragment,
    TextDisplay,
    Text,

    Image,
    ImageLocation,
    ImageRaw,

    FontQUnit,
    ScreenUnit,

    ScreenPosition,
    SCREEN_POSITION_X,
    SCREEN_POSITION_Y,

    ScreenSize,
    SCREEN_SIZE_WIDTH,
    SCREEN_SIZE_W,
    SCREEN_SIZE_HEIGHT,
    SCREEN_SIZE_H,

    ScreenArea,
    SCREEN_AREA_X,
    SCREEN_AREA_Y,
    SCREEN_AREA_WIDTH,
    SCREEN_AREA_W,
    SCREEN_AREA_HEIGHT,
    SCREEN_AREA_H,

    NativeScreenUnit,

    NativeScreenPosition,
    NATIVE_SCREEN_POSITION_X,
    NATIVE_SCREEN_POSITION_Y,

    NativeScreenSize,
    NATIVE_SCREEN_SIZE_WIDTH,
    NATIVE_SCREEN_SIZE_W,
    NATIVE_SCREEN_SIZE_HEIGHT,
    NATIVE_SCREEN_SIZE_H,

    NativeScreenArea,
    NATIVE_SCREEN_AREA_X,
    NATIVE_SCREEN_AREA_Y,
    NATIVE_SCREEN_AREA_WIDTH,
    NATIVE_SCREEN_AREA_W,
    NATIVE_SCREEN_AREA_HEIGHT,
    NATIVE_SCREEN_AREA_H,

    ScreenRect,

    TextBiDi,
    TEXT_BIDI_LTR,
    TEXT_BIDI_RTL,

    TextRotation,
    TEXT_ROTATE_HORIZ,
    TEXT_ROTATE_90_CLOCKWISE,
    TEXT_ROTATE_90_COUNTER_CLOCKWISE,
    TEXT_ROTATE_ALL,

    TextAlignment,
    TEXT_ALIGN_UPPER_LEFT,
    TEXT_ALIGN_UPPER_RIGHT,
    TEXT_ALIGN_BOTTOM_LEFT,
    TEXT_ALIGN_BOTTOM_RIGHT,
    TEXT_ALIGN_CENTER_LEFT,
    TEXT_ALIGN_CENTER_RIGHT,
    TEXT_ALIGN_UPPER_CENTER,
    TEXT_ALIGN_BOTTOM_CENTER,
    TEXT_ALIGN_CENTER_CENTER,
    TEXT_ALIGN_ALL,

    ScreenHandle,
    NativeScreenInfo,
    VirtualScreenArea,
    VirtualScreenInfo,
)
from .screen import (
    STATE_ID_SCREENS,
    ScreenState,
    set_screen_state,
    VirtualScreenArea,
)
from .window.action_requests import (
    RequestSetNativeWindowVisibility,
    EVENT_ID_REQUEST_SET_NATIVE_WINDOW_VISIBILITY,
    as_request_set_native_window_visibility_listener,
    send_request_set_native_window_visibility_event,

    RequestSetNativeWindowStyleEvent,
    EVENT_ID_REQUEST_SET_NATIVE_WINDOW_STYLE,
    as_request_set_native_window_style_listener,
    send_request_set_native_window_style_event,

    RequestCloseNativeWindowEvent,
    EVENT_ID_REQUEST_CLOSE_NATIVE_WINDOW,
    as_request_close_native_window_listener,
    send_request_close_native_window_event,

    RequestFocusNativeWindowEvent,
    EVENT_ID_REQUEST_FOCUS_NATIVE_WINDOW,
    as_request_focus_native_window_listener,
    send_request_focus_native_window_event,

    RequestMoveNativeWindowEvent,
    EVENT_ID_REQUEST_MOVE_NATIVE_WINDOW,
    as_request_move_native_window_listener,
    send_request_move_native_window_event,
)
from .window.action_occurred import (
    NativeWindowClosedEvent,
    EVENT_ID_NATIVE_WINDOW_CLOSED,
    as_native_window_closed_listener,
    send_native_window_closed_event,

    TARGET_ID_WINDOW_CREATION,
    NativeWindowCreatedEvent,
    EVENT_ID_NATIVE_WINDOW_CREATED,
    as_native_window_created_listener,
    send_native_window_created_event,

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
from .window.state import (
    NativeWindowState,
    AllActiveWindowsState,
    STATE_ID_ACTIVE_WINDOWS,
)
from .window.match import (
    WindowMatcher,
    WINDOW_MATCH_EXACT,
    WINDOW_MATCH_PART,
    WINDOW_MATCH_GLOB,
    WINDOW_MATCH_REGEX,
    WINDOW_MATCHES,
)
