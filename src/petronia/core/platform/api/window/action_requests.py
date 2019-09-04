
"""
Native window interactions.  The target for these events is the window
component ID.
"""

from .....aid.simp import (
    EventId,
    EventBus,
    ComponentId,
    EventCallback,
    ListenerSetup,
)
from ..defs import (
    ScreenArea,
)

# ---------------------------------------------------------------------------
EVENT_ID_REQUEST_MOVE_NATIVE_WINDOW = EventId('core.platform.api move-native-window')


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
EVENT_ID_REQUEST_FOCUS_NATIVE_WINDOW = EventId('core.platform.api focus-native-window')


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
EVENT_ID_REQUEST_CLOSE_NATIVE_WINDOW = EventId('core.platform.api close-native-window')


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
