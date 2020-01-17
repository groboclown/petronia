
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

# Describes the tile assignment and relative ordering in that tile.
TilePriority = Tuple[ComponentId, int]


class WindowTileAssignmentState:
    """
    Keeps track of each window handled by the implementation and which
    tile it's assigned to.  This only shows the state for the tiles in
    the currently active virtual workspace.
    """
    __slots__ = (
        '__wid', '__mapping',
    )

    def __init__(self, workspace_id: str, windows_to_tiles: Mapping[ComponentId, TilePriority]) -> None:
        self.__wid = workspace_id
        self.__mapping = readonly_dict(windows_to_tiles)

    @property
    def workspace_id(self) -> str:
        return self.__wid

    @property
    def windows_to_tiles(self) -> Mapping[ComponentId, TilePriority]:
        return self.__mapping


def set_tile_state(bus: EventBus, workspace_id: str, windows_to_tiles: Mapping[ComponentId, ComponentId]) -> None:
    set_state(bus, STATE_ID_LAYOUT_WINDOW, WindowTileAssignmentState, WindowTileAssignmentState(
        workspace_id, windows_to_tiles
    ))


def create_tile_state_watch(listeners: ListenerSet) -> StateWatch[WindowTileAssignmentState]:
    return StateWatch(listeners, STATE_ID_LAYOUT_WINDOW, WindowTileAssignmentState('', EMPTY_DICT))
