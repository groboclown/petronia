
"""
Generic tile-based layout events.

Each layout can have its own interpretation of these events.
For example, a tiling layout manager can interpret "move window"
to mean swap the window with another adjacent window.
"""

from .....aid.std import (
    EventId,
    EventCallback,
    EventBus,
    RequestNewComponentEvent,
    ComponentId,
    ParticipantId,
    ListenerSet,
    create_singleton_identity,
    as_request_new_component_listener,
    send_request_new_component,
)
from .....aid.bootstrap import (
    ListenerSetup,
)
from .states import (
    BorderSize,
    WorkspaceState,
    TileState,
)


TARGET_ID_LAYOUT_TILE = create_singleton_identity('core.layout.tile.api/global')

# ---------------------------------------------------------------------------
# Basic lifecycle handlers


def as_request_new_tile_listener(
        callback: EventCallback[RequestNewComponentEvent[None]]
) -> ListenerSetup[RequestNewComponentEvent[None]]:
    """The lifecycle specific version for tiles."""
    return as_request_new_component_listener(callback)


def add_request_new_tile_listener(
        listeners: ListenerSet,
        callback: EventCallback[RequestNewComponentEvent[None]]
) -> None:
    listeners.listen(TARGET_ID_LAYOUT_TILE, as_request_new_component_listener, callback)


def send_request_new_tile(
        bus: EventBus, callback_target_id: ParticipantId, request_id: int
) -> None:
    send_request_new_component(bus, TARGET_ID_LAYOUT_TILE, None, callback_target_id, request_id)


# ---------------------------------------------------------------------------


EVENT_ID_REQUEST_MOVE_RESIZE_ACTIVE_TILE = EventId('core.layout.tile.api/request-resize')


class RequestMoveResizeActiveTileEvent:
    """
    User request to move and/or resize the currently active tile.

    The interpretation of what a "change" means depends greatly upon the
    implementing layout.  See the specific layout's documentation for how
    to use this.

    If the layout decides to accept the change request, it can trigger
    tile change events and tile state changes.
    """

    __slots__ = (
        '__dx', '__dy', '__dw', '__dh', '__dz',
    )

    def __init__(self, dx: int, dy: int, dw: int, dh: int, dz: int) -> None:
        self.__dx = dx
        self.__dy = dy
        self.__dw = dw
        self.__dh = dh
        self.__dz = dz

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

    @property
    def dz(self) -> int:
        return self.__dz


def as_request_move_resize_focused_window_listener(
        callback: EventCallback[RequestMoveResizeActiveTileEvent]
) -> ListenerSetup[RequestMoveResizeActiveTileEvent]:
    return (EVENT_ID_REQUEST_MOVE_RESIZE_ACTIVE_TILE, callback)


def add_request_move_resize_focused_window_listener(
        listeners: ListenerSet,
        callback: EventCallback[RequestMoveResizeActiveTileEvent]
) -> None:
    listeners.listen(TARGET_ID_LAYOUT_TILE, as_request_move_resize_focused_window_listener, callback)


def send_request_move_resize_active_tile_event(
        bus: EventBus,
        dx: int, dy: int, dw: int, dh: int, dz: int
) -> None:
    bus.trigger(
        EVENT_ID_REQUEST_MOVE_RESIZE_ACTIVE_TILE, TARGET_ID_LAYOUT_TILE,
        RequestMoveResizeActiveTileEvent(dx, dy, dw, dh, dz)
    )

# ---------------------------------------------------------------------------


EVENT_ID_REQUEST_SET_ACTIVE_TILE = EventId('core.layout.tile.api/request-set-active')


class RequestSetActiveTileEvent:
    """
    Request to set a specific tile as the active tile.  This can implicitly cause
    a change in the active workspace.
    """

    __slots__ = (
        '__tile_cid',
    )

    def __init__(self, tile_cid: ComponentId) -> None:
        self.__tile_cid = tile_cid

    @property
    def tile_cid(self) -> ComponentId:
        return self.__tile_cid

    def __repr__(self) -> str:
        return 'RequestSetActiveTileEvent(tile_cid={0})'.format(
            repr(self.__tile_cid)
        )


def as_request_set_active_tile_listener(
        callback: EventCallback[RequestSetActiveTileEvent]
) -> ListenerSetup[RequestSetActiveTileEvent]:
    return (EVENT_ID_REQUEST_SET_ACTIVE_TILE, callback,)


def add_request_set_active_tile_listener(
        listeners: ListenerSet,
        callback: EventCallback[RequestSetActiveTileEvent]
) -> None:
    listeners.listen(TARGET_ID_LAYOUT_TILE, as_request_set_active_tile_listener, callback)


def send_request_set_active_tile_event(bus: EventBus, name: str, index: int) -> None:
    bus.trigger(
        EVENT_ID_REQUEST_SET_ACTIVE_TILE, TARGET_ID_LAYOUT_TILE,
        RequestSetActiveTileEvent(name, index)
    )

# ---------------------------------------------------------------------------


EVENT_ID_REQUEST_SET_TILE_BORDER_SIZE = EventId('core.layout.tile.api/request-set-border-size')


class RequestSetTileBorderSizeEvent:
    """
    Request to set a specific tile's border space.  This request can be rejected
    silently, such as if the border size is bigger than the tile size.  Accepted
    requests will generate a state change on the tile.
    """

    __slots__ = (
        '__border',
    )

    def __init__(self, border: BorderSize) -> None:
        self.__border = border

    @property
    def border(self) -> BorderSize:
        return self.__border

    def __repr__(self) -> str:
        return 'RequestSetTileBorderSizeEvent(border={0})'.format(
            repr(self.__border)
        )


def as_request_set_tile_border_size_listener(
        callback: EventCallback[RequestSetTileBorderSizeEvent]
) -> ListenerSetup[RequestSetTileBorderSizeEvent]:
    return (EVENT_ID_REQUEST_SET_TILE_BORDER_SIZE, callback,)


def send_request_set_tile_border_size_event(bus: EventBus, tile_cid: ComponentId, border: BorderSize) -> None:
    bus.trigger(
        EVENT_ID_REQUEST_SET_TILE_BORDER_SIZE, tile_cid,
        RequestSetTileBorderSizeEvent(border)
    )


def as_request_set_global_tile_border_size_listener(
        callback: EventCallback[RequestSetTileBorderSizeEvent]
) -> ListenerSetup[RequestSetTileBorderSizeEvent]:
    return (EVENT_ID_REQUEST_SET_TILE_BORDER_SIZE, callback,)


def add_request_set_global_active_tile_listener(
        listeners: ListenerSet,
        callback: EventCallback[RequestSetTileBorderSizeEvent]
) -> None:
    listeners.listen(TARGET_ID_LAYOUT_TILE, as_request_set_global_tile_border_size_listener, callback)


def send_request_set_global_tile_border_size_event(bus: EventBus, border: BorderSize) -> None:
    bus.trigger(
        EVENT_ID_REQUEST_SET_TILE_BORDER_SIZE, TARGET_ID_LAYOUT_TILE,
        RequestSetTileBorderSizeEvent(border)
    )

# ---------------------------------------------------------------------------


EVENT_ID_REQUEST_REMOVE_ACTIVE_TILE = EventId('core.layout.api/request-remove-active')


class RequestRemoveActiveTileEvent:
    """
    Request to remove the currently active tile.  The tile manager can refuse
    this request.
    """

    __slots__ = ()

    def __init__(self) -> None:
        pass


def as_request_remove_active_tile_listener(
        callback: EventCallback[RequestRemoveActiveTileEvent]
) -> ListenerSetup[RequestRemoveActiveTileEvent]:
    return (EVENT_ID_REQUEST_REMOVE_ACTIVE_TILE, callback,)


def add_request_remove_active_tile_listener(
        listeners: ListenerSet,
        callback: EventCallback[RequestRemoveActiveTileEvent]
) -> None:
    listeners.listen(TARGET_ID_LAYOUT_TILE, as_request_remove_active_tile_listener, callback)


def send_request_remove_active_tile(bus: EventBus, name: str) -> None:
    bus.trigger(
        EVENT_ID_REQUEST_REMOVE_ACTIVE_TILE, TARGET_ID_LAYOUT_TILE,
        RequestSetVirtualWorkspaceEvent(name)
    )

# ---------------------------------------------------------------------------


EVENT_ID_REQUEST_SET_VIRTUAL_WORKSPACE = EventId('core.layout.api/request-virtual-workspace')


class RequestSetVirtualWorkspaceEvent:
    """
    Request to switch to a virtual workspace.  This can be either relative or
    absolute.

    Some implementations may have a virtual screen per physical monitor,
    while others may have a global virtual screen..
    """

    __slots__ = (
        '__name',
    )

    def __init__(self, name: str) -> None:
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name


def as_request_set_virtual_workspace_listener(
        callback: EventCallback[RequestSetVirtualWorkspaceEvent]
) -> ListenerSetup[RequestSetVirtualWorkspaceEvent]:
    return (EVENT_ID_REQUEST_SET_VIRTUAL_WORKSPACE, callback,)


def add_request_set_virtual_workspace_listener(
        listeners: ListenerSet,
        callback: EventCallback[RequestSetVirtualWorkspaceEvent]
) -> None:
    listeners.listen(TARGET_ID_LAYOUT_TILE, as_request_set_virtual_workspace_listener, callback)


def send_request_set_virtual_workspace_event(bus: EventBus, name: str) -> None:
    bus.trigger(
        EVENT_ID_REQUEST_SET_VIRTUAL_WORKSPACE, TARGET_ID_LAYOUT_TILE,
        RequestSetVirtualWorkspaceEvent(name)
    )

# ---------------------------------------------------------------------------


EVENT_ID_ACTIVE_VIRTUAL_WORKSPACE_CHANGED = EventId('core.layout.api/active-virtual-workspace-changed')


class ActiveVirtualWorkspaceChangedEvent:
    """
    Notification that the active virtual workspace switched to another virtual workspace.
    """

    __slots__ = (
        '__state',
    )

    def __init__(self, workspace_state: WorkspaceState) -> None:
        self.__state = workspace_state

    @property
    def workspace_state(self) -> WorkspaceState:
        return self.__state


def as_active_virtual_workspace_changed_listener(
        callback: EventCallback[ActiveVirtualWorkspaceChangedEvent]
) -> ListenerSetup[ActiveVirtualWorkspaceChangedEvent]:
    return (EVENT_ID_ACTIVE_VIRTUAL_WORKSPACE_CHANGED, callback,)


def add_active_virtual_workspace_changed_listener(
        listeners: ListenerSet,
        callback: EventCallback[ActiveVirtualWorkspaceChangedEvent]
) -> None:
    listeners.listen(TARGET_ID_LAYOUT_TILE, as_active_virtual_workspace_changed_listener, callback)


def send_active_virtual_workspace_changed_event(bus: EventBus, active_workspace_state: WorkspaceState) -> None:
    bus.trigger(
        EVENT_ID_ACTIVE_VIRTUAL_WORKSPACE_CHANGED, TARGET_ID_LAYOUT_TILE,
        ActiveVirtualWorkspaceChangedEvent(active_workspace_state)
    )

# ---------------------------------------------------------------------------


EVENT_ID_ACTIVE_TILE_CHANGED = EventId('core.layout.api/active-tile-changed')


class ActiveTileChangedEvent:
    """
    Notification that the active tile switched to another tile.  This will happen
    on virtual workspace change, too.
    """

    __slots__ = (
        '__state',
    )

    def __init__(self, tile_state: TileState) -> None:
        self.__state = tile_state

    @property
    def tile_state(self) -> TileState:
        return self.__state


def as_active_tile_changed_listener(
        callback: EventCallback[ActiveTileChangedEvent]
) -> ListenerSetup[ActiveTileChangedEvent]:
    return (EVENT_ID_ACTIVE_TILE_CHANGED, callback,)


def add_active_tile_changed_listener(
        listeners: ListenerSet,
        callback: EventCallback[ActiveTileChangedEvent]
) -> None:
    listeners.listen(TARGET_ID_LAYOUT_TILE, as_active_tile_changed_listener, callback)


def send_active_tile_changed_event(bus: EventBus, active_tile_state: TileState) -> None:
    bus.trigger(
        EVENT_ID_ACTIVE_TILE_CHANGED, TARGET_ID_LAYOUT_TILE,
        ActiveTileChangedEvent(active_tile_state)
    )
