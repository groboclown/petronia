
"""
Native window interactions.  The target for these events is the window
component ID.
"""

from typing import Mapping, Union
from .....aid.simp import (
    EventId,
    EventBus,
    ComponentId,
    EventCallback,
    ListenerSetup,
    readonly_dict,
)
from ..defs import (
    ScreenArea,
)

# ---------------------------------------------------------------------------
EVENT_ID_REQUEST_MOVE_NATIVE_WINDOW = EventId('core.platform.api/move-native-window')


class RequestMoveNativeWindowEvent:
    """
    Request to move or resize a window.  A value of < 0 means that it
    shouldn't change.
    """
    __slots__ = ('__area',)

    def __init__(
            self,
            area: ScreenArea
    ) -> None:
        self.__area = area

    @property
    def area(self) -> ScreenArea:
        return self.__area


def send_request_move_native_window_event(
        bus: EventBus,
        window_id: ComponentId,
        area: ScreenArea
) -> None:
    bus.trigger(
        EVENT_ID_REQUEST_MOVE_NATIVE_WINDOW, window_id,
        RequestMoveNativeWindowEvent(area)
    )


def as_request_move_native_window_listener(
        callback: EventCallback[RequestMoveNativeWindowEvent]
) -> ListenerSetup[RequestMoveNativeWindowEvent]:
    return (EVENT_ID_REQUEST_MOVE_NATIVE_WINDOW, callback,)


# ---------------------------------------------------------------------------
EVENT_ID_REQUEST_FOCUS_NATIVE_WINDOW = EventId('core.platform.api/focus-native-window')


class RequestFocusNativeWindowEvent:
    """
    Set the window as focused and optionally raised to top.  Some platforms
    may ignore the raise-to-top value.
    """

    __slots__ = ('__raise',)

    def __init__(self, raise_to_top: bool) -> None:
        self.__raise = raise_to_top

    @property
    def raise_to_top(self) -> bool:
        return self.__raise


def send_request_focus_native_window_event(
        bus: EventBus,
        window_id: ComponentId,
        raise_to_top: bool
) -> None:
    bus.trigger(EVENT_ID_REQUEST_FOCUS_NATIVE_WINDOW, window_id, RequestFocusNativeWindowEvent(raise_to_top))


def as_request_focus_native_window_listener(
        callback: EventCallback[RequestFocusNativeWindowEvent]
) -> ListenerSetup[RequestFocusNativeWindowEvent]:
    return (EVENT_ID_REQUEST_FOCUS_NATIVE_WINDOW, callback,)


# ---------------------------------------------------------------------------
EVENT_ID_REQUEST_CLOSE_NATIVE_WINDOW = EventId('core.platform.api/close-native-window')


class RequestCloseNativeWindowEvent:
    """
    Send a request to close a window.
    """

    __slots__ = ('__force',)

    def __init__(self, force: bool) -> None:
        self.__force = force

    @property
    def force(self) -> bool:
        return self.__force


def send_request_close_native_window_event(
        bus: EventBus,
        window_id: ComponentId,
        force: bool
) -> None:
    bus.trigger(EVENT_ID_REQUEST_CLOSE_NATIVE_WINDOW, window_id, RequestCloseNativeWindowEvent(force))


def as_request_close_native_window_listener(
        callback: EventCallback[RequestCloseNativeWindowEvent]
) -> ListenerSetup[RequestCloseNativeWindowEvent]:
    return (EVENT_ID_REQUEST_CLOSE_NATIVE_WINDOW, callback,)


# ---------------------------------------------------------------------------
EVENT_ID_REQUEST_SET_NATIVE_WINDOW_STYLE = EventId('core.platform.api/set-native-window-style')


class RequestSetNativeWindowStyleEvent:
    """
    Send a request to set a window's native style.  The keys and values are
    highly dependent upon the underlying OS and windowing system.
    """

    __slots__ = ('__style',)

    def __init__(self, style: Mapping[str, Union[float, bool, str]]) -> None:
        self.__style = readonly_dict(style)

    @property
    def style(self) -> Mapping[str, Union[float, bool, str]]:
        return self.__style


def send_request_set_native_window_style_event(
        bus: EventBus,
        window_id: ComponentId,
        style: Mapping[str, Union[float, bool, str]]
) -> None:
    bus.trigger(EVENT_ID_REQUEST_SET_NATIVE_WINDOW_STYLE, window_id, RequestSetNativeWindowStyleEvent(style))


def as_request_set_native_window_style_listener(
        callback: EventCallback[RequestSetNativeWindowStyleEvent]
) -> ListenerSetup[RequestSetNativeWindowStyleEvent]:
    return (EVENT_ID_REQUEST_SET_NATIVE_WINDOW_STYLE, callback,)
