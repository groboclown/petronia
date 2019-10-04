
"""
Generic layout events.

Each layout can have its own interpretation of these events.
For example, a tiling layout manager can interpret "move window"
to mean swap the window with another adjacent window.
"""

from ....aid.simp import (
    EventId,
    EventCallback,
    EventBus,
    create_singleton_identity,
)
from ....aid.bootstrap import (
    ListenerSetup,
)


TARGET_ID_LAYOUT = create_singleton_identity('core.layout.api/layouts')

# ---------------------------------------------------------------------------

EVENT_ID_LAYOUT_CHANGED = EventId('core.layout.api/layout-changed')


class LayoutChangedEvent:
    """
    Triggered when the current layout on the screen changed.  This does not
    necessarily always get called when a new window is created; for example,
    a one-app (always maximized) layout would only send this event when the
    layout manager starts.
    """
    __slots__ = ()

    def __init__(self):
        pass


def as_layout_changed_listener(
        callback: EventCallback[LayoutChangedEvent]
) -> ListenerSetup[LayoutChangedEvent]:
    return (EVENT_ID_LAYOUT_CHANGED, callback)


def send_layout_changed_event(
        bus: EventBus
) -> None:
    bus.trigger(EVENT_ID_LAYOUT_CHANGED, TARGET_ID_LAYOUT, LayoutChangedEvent())

# ---------------------------------------------------------------------------


EVENT_ID_REQUEST_MOVE_RESIZE_FOCUSED_WINDOW = EventId('core.layout.api/request-resize')


class RequestMoveResizeFocusedWindowEvent:
    """
    User request to move and/or resize the currently focused window.

    The interpretation of what a "change" means depends greatly upon the
    implementing layout.  See the specific layout's documentation for how
    to use this.

    If the layout decides to accept the change request, it can trigger
    window move and layout change events.  It can change multiple windows
    and other parts of the system.
    """

    __slots__ = (
        '__dx', '__dy', '__dw', '__dh',
    )

    def __init__(self, dx: int, dy: int, dw: int, dh: int) -> None:
        self.__dx = dx
        self.__dy = dy
        self.__dw = dw
        self.__dh = dh

    @property
    def dx(self) -> int:
        return self.__dx

    @property
    def dy(self) -> int:
        return self.__dy

    @property
    def dw(self) -> int:
        return self.__dw

    @property
    def dh(self) -> int:
        return self.__dh


def as_request_move_resize_focused_window_listener(
        callback: EventCallback[RequestMoveResizeFocusedWindowEvent]
) -> ListenerSetup[RequestMoveResizeFocusedWindowEvent]:
    return (EVENT_ID_REQUEST_MOVE_RESIZE_FOCUSED_WINDOW, callback)


def send_request_move_resize_focused_window_event(
        bus: EventBus,
        dx: int, dy: int, dw: int, dh: int
) -> None:
    bus.trigger(
        EVENT_ID_REQUEST_MOVE_RESIZE_FOCUSED_WINDOW, TARGET_ID_LAYOUT,
        RequestMoveResizeFocusedWindowEvent(dx, dy, dw, dh)
    )

# ---------------------------------------------------------------------------


EVENT_ID_REQUEST_SET_WINDOW_VISIBILITY = EventId('core.layout.api/request-visibility')


class RequestSetWindowVisibility:
    """
    Request to change the window's visibility.  The layout may minimize or move off
    screen or in some other way hide the window from sight.  Making a window visible
    will restore it to the window's previous visibility setting.  Following the
    successful request, the focus should be the same as before setting the visibility.
    So, a separate request focus event may be necessary.
    """

    __slots__ = (
        '__visible',
    )

    def __init__(self, visible: bool) -> None:
        self.__visible = visible
