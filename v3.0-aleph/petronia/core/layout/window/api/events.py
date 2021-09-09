
"""
Events for window-tile-containment.

Because the Window to Tile assignment causes multiple state changes with
movements, the window assigned to tile action does not generate its own
event, but instead the entire assignment state is changed.
"""

from typing import Optional
from .....aid.std import (
    EventId,
    EventCallback,
    EventBus,
    ComponentId,
    ListenerSet,
    create_singleton_identity,
)
from .....aid.bootstrap import (
    ListenerSetup,
)


TARGET_ID_LAYOUT_WINDOW = create_singleton_identity('core.layout.window.api/global')


# ---------------------------------------------------------------------------

EVENT_ID_REQUEST_ASSIGN_WINDOW_TO_TILE = EventId('core.layout.window.api/request-assign-window-to-tile')


class RequestAssignWindowToTileEvent:
    """
    Request the window layout to move a given window CID to a tile CID.
    The tile must be in the current virtual workspace for this to work.

    The "window" can be a native OS window or a Petronia managed
    window.

    The z-order is a requested z-order position within the tile's
    other windows.  If the window is also requested to be background,
    then the z-order will be such that it is always behind the
    non-background windows.

    The position is an implementation-specific description about
    where in the tile to place the window.

    If the tile_cid is None, then it requests the active tile.

    If the window_cid is None, then it requests the active window.

    There may be a situation where the user needs to move the active window
    into the active tile.  However, this generally should be considered
    a no-op, or a change to the z-order or background status.
    """
    __slots__ = (
        '__window_cid', '__tile_cid', '__z_order', '__position', '__is_background',
    )

    def __init__(
            self, window_cid: Optional[ComponentId], tile_cid: Optional[ComponentId],
            z_order: int, position: str, is_background: bool
    ) -> None:
        self.__window_cid = window_cid
        self.__tile_cid = tile_cid
        self.__z_order = z_order
        self.__position = position
        self.__is_background = is_background

    @property
    def window_cid(self) -> Optional[ComponentId]:
        return self.__window_cid

    @property
    def tile_cid(self) -> Optional[ComponentId]:
        return self.__tile_cid

    @property
    def z_order(self) -> int:
        return self.__z_order

    @property
    def position(self) -> str:
        return self.__position

    @property
    def is_background(self) -> bool:
        return self.__is_background


def as_request_assign_window_to_tile_listener(
        callback: EventCallback[RequestAssignWindowToTileEvent]
) -> ListenerSetup[RequestAssignWindowToTileEvent]:
    return (EVENT_ID_REQUEST_ASSIGN_WINDOW_TO_TILE, callback,)


def add_request_assign_window_to_tile_listener(
        listeners: ListenerSet,
        callback: EventCallback[RequestAssignWindowToTileEvent]
) -> None:
    listeners.listen(TARGET_ID_LAYOUT_WINDOW, as_request_assign_window_to_tile_listener, callback)


def send_request_assign_window_to_tile_event(
        bus: EventBus, window_cid: Optional[ComponentId], tile_cid: Optional[ComponentId],
        z_order: int, position: str, is_background: bool
) -> None:
    bus.trigger(
        EVENT_ID_REQUEST_ASSIGN_WINDOW_TO_TILE, TARGET_ID_LAYOUT_WINDOW,
        RequestAssignWindowToTileEvent(window_cid, tile_cid, z_order, position, is_background)
    )


def send_request_assign_active_window_to_tile_event(
        bus: EventBus, tile_cid: ComponentId,
        z_order: int, position: str, is_background: bool
) -> None:
    send_request_assign_window_to_tile_event(bus, None, tile_cid, z_order, position, is_background)


def send_request_assign_window_to_active_tile_event(
        bus: EventBus, window_cid: ComponentId,
        z_order: int, position: str, is_background: bool
) -> None:
    send_request_assign_window_to_tile_event(bus, window_cid, None, z_order, position, is_background)


# ---------------------------------------------------------------------------

EVENT_ID_REQUEST_SET_NEXT_WINDOW_ACTIVE = EventId('core.layout.window.api/request-set-next-window-active')


class RequestSetNextWindowActiveEvent:
    """
    Request to set the "next" window to be active, relative to the current active window.
    The meaning of "next" is up to the implementation.  The relative "next" is based on
    an offset (generally - +1 means the next window and -1 means the previous
    window).  Values other than -1 and +1 may not be directly supported, but the window
    manager should so something that reflects the perceived desire of the request.

    This can mean to move to the previously active windows, or it can mean to shuffle
    between windows in the same tile, if this is supported.

    Windows that are in the background must remain below any window that is not
    in the background of a tile.

    The offset value cannot be 0.
    """
    __slots__ = ('__offset',)

    def __init__(self, offset: int) -> None:
        assert offset != 0
        self.__offset = offset

    @property
    def offset(self) -> int:
        return self.__offset

# FIXME COMPLETE


# ---------------------------------------------------------------------------

EVENT_ID_REQUEST_SET_WINDOW_VISIBILITY = EventId('core.layout.window.api/request-visibility')


class RequestSetWindowVisibility:
    """
    Changes whether the window is visible in the tile.  This is similar to a "minimize"
    functionality.

    If the window_cid is None, then this affects the active window.
    """

    __slots__ = ('__window_cid', '__is_visible')

    def __init__(self, window_cid: Optional[ComponentId], is_visible: bool) -> None:
        self.__window_cid = window_cid
        self.__is_visible = is_visible

    @property
    def window_cid(self) -> Optional[ComponentId]:
        return self.__window_cid

    @property
    def is_visible(self) -> bool:
        return self.__is_visible


# FIXME COMPLETE


# ---------------------------------------------------------------------------

EVENT_ID_REQUEST_CHANGE_WINDOW_SETTINGS = EventId('core.layout.window.api/request-change-window-settings')


class RequestChangeWindowSettings:
    """
    Change how the window is placed in its tile.  Updates the values that
    were initially set during tile assignment.

    If the window_cid is None, then this affects the active window.
    """

    __slots__ = (
        '__window_cid', '__z_order', '__position', '__is_background',
    )

    def __init__(
            self, window_cid: Optional[ComponentId],
            z_order: int, position: str, is_background: bool
    ) -> None:
        self.__window_cid = window_cid
        self.__z_order = z_order
        self.__position = position
        self.__is_background = is_background

    @property
    def window_cid(self) -> Optional[ComponentId]:
        return self.__window_cid

    @property
    def z_order(self) -> int:
        return self.__z_order

    @property
    def position(self) -> str:
        return self.__position

    @property
    def is_background(self) -> bool:
        return self.__is_background

# FIXME COMPLETE
