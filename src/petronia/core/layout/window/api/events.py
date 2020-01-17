
"""
Events for window-tile-containment.

Because the Window to Tile assignment causes multiple state changes with
movements, the window assigned to tile action does not generate its own
event, but instead the entire assignment state is changed.
"""

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
    """
    __slots__ = (
        '__window_cid', '__tile_cid',
    )

    def __init__(self, window_cid: ComponentId, tile_cid: ComponentId) -> None:
        self.__window_cid = window_cid
        self.__tile_cid = tile_cid

    @property
    def window_cid(self) -> ComponentId:
        return self.__window_cid

    @property
    def tile_cid(self) -> ComponentId:
        return self.__tile_cid


def as_request_assign_window_to_tile_listener(
        callback: EventCallback[RequestAssignWindowToTileEvent]
) -> ListenerSetup[RequestAssignWindowToTileEvent]:
    return (EVENT_ID_REQUEST_ASSIGN_WINDOW_TO_TILE, callback,)


def add_request_assign_window_to_tile_listener(
        listeners: ListenerSet,
        callback: EventCallback[RequestAssignWindowToTileEvent]
) -> None:
    listeners.listen(TARGET_ID_LAYOUT_WINDOW, as_request_assign_window_to_tile_listener, callback)


def send_request_assign_window_to_tile_event(bus: EventBus, window_cid: ComponentId, tile_cid: ComponentId) -> None:
    bus.trigger(
        EVENT_ID_REQUEST_ASSIGN_WINDOW_TO_TILE, TARGET_ID_LAYOUT_WINDOW,
        RequestAssignWindowToTileEvent(window_cid, tile_cid)
    )


# ---------------------------------------------------------------------------

EVENT_ID_REQUEST_ASSIGN_ACTIVE_WINDOW_TO_TILE = EventId('core.layout.window.api/request-assign-active-window-to-tile')


class RequestAssignActiveWindowToTileEvent:
    """
    Request the window layout to move the currently active window to a tile CID.
    The tile must be in the current virtual workspace for this to work.
    """
    __slots__ = (
        '__tile_cid',
    )

    def __init__(self, tile_cid: ComponentId) -> None:
        self.__tile_cid = tile_cid

    @property
    def tile_cid(self) -> ComponentId:
        return self.__tile_cid


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

    The offset value cannot be 0.
    """
    __slots__ = ('__offset',)

    def __init__(self, offset: int) -> None:
        assert offset != 0
        self.__offset = offset

    @property
    def offset(self) -> int:
        return self.__offset


# ---------------------------------------------------------------------------

EVENT_ID_REQUEST_SET_ACTIVE_WINDOW_VISIBILITY = EventId('core.layout.window.api/request-visibility')

# FIXME