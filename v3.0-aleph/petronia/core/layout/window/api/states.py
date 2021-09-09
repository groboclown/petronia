
from typing import Mapping, Tuple
from .....aid.std import (
    ComponentId,
    EventBus,
    ListenerSet,
    StateWatch,
    set_state,
    create_singleton_identity,
    readonly_dict,
    EMPTY_DICT,
)


STATE_ID_LAYOUT_WINDOW = create_singleton_identity('petronia.core.layout.window.api/tile')


class WindowInTile:
    """
    Describes details for how the window lives inside the tile.

    "position" describes the way the window fits inside the tile.  This is an
    implementation-specific value.
    """
    __slots__ = ('__tile_cid', '__z_order', '__position', '__is_background',)

    def __init__(self, tile_cid: ComponentId, z_order: int, position: str, is_background: bool) -> None:
        self.__tile_cid = tile_cid
        self.__z_order = z_order
        self.__position = position
        self.__is_background = is_background

    @property
    def tile_cid(self) -> ComponentId:
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


class WindowTileAssignmentState:
    """
    Keeps track of each window handled by the implementation and which
    tile it's assigned to.  This only shows the state for the tiles in
    the currently active virtual workspace.
    """
    __slots__ = (
        '__wid', '__mapping',
    )

    def __init__(self, workspace_id: str, windows_to_tiles: Mapping[ComponentId, WindowInTile]) -> None:
        self.__wid = workspace_id
        self.__mapping = readonly_dict(windows_to_tiles)

    @property
    def workspace_id(self) -> str:
        return self.__wid

    @property
    def windows_to_tiles(self) -> Mapping[ComponentId, WindowInTile]:
        return self.__mapping


def set_window_tile_state(
        bus: EventBus, workspace_id: str, windows_to_tiles: Mapping[ComponentId, WindowInTile]
) -> None:
    set_state(bus, STATE_ID_LAYOUT_WINDOW, WindowTileAssignmentState, WindowTileAssignmentState(
        workspace_id, windows_to_tiles
    ))


INITIAL_WINDOW_TILE_ASSIGNMENT_STATE = WindowTileAssignmentState('', EMPTY_DICT)


def create_window_tile_state_watch(listeners: ListenerSet) -> StateWatch[WindowTileAssignmentState]:
    return StateWatch(listeners, STATE_ID_LAYOUT_WINDOW, INITIAL_WINDOW_TILE_ASSIGNMENT_STATE)
