
"""
State information for tile-based layouts.

Tiles add another abstraction beyond just windows - there is an additional concept of a
tile in which a window can reside.  The individual tile can have separate decoration
or information than the windows.
"""

from typing import Iterable, Sequence, List, Optional
from typing import cast as t_cast
from .....aid.std import (
    ComponentId,
    EventBus,
    EventCallback,
    ListenerSet,
    StateWatch,
    create_singleton_identity,
    set_state,
    EMPTY_TUPLE,
)
from .....aid.bootstrap import (
    NOT_PARTICIPANT,
)
from .....base.events import (
    ComponentCreatedEvent,
    as_component_created_listener,
    RequestNewComponentEvent,
    send_component_created_event,
)
from .....core.platform.api import (
    ScreenArea,
    ScreenUnit,
    ZERO_SCREEN_AREA,
)


STATE_ID_LAYOUT_TILE = create_singleton_identity('petronia.core.layout.tile.api/tile')


class TileState:
    """
    Abstract tile state.

    Tiles are screen regions managed by the tile layout implementation.  Other
    extensions can use the tile state to move windows into them, or add
    decoration, or any number of other functionality.

    The tiles can have tags (keys) and are assigned to a workspace (virtual
    desktop).  Windows could be assigned to multiple workspaces, but tiles can
    only exist in one workspace.
    """
    __slots__ = (
        '__cid',
        '__visible_area',
        '__usable_area',
        '__z_index',
        '__workspace_id',
        '__tags',
    )

    def __init__(
            self,
            cid: ComponentId,
            visible_area: ScreenArea,
            usable_area: ScreenArea,
            z_index: int,
            workspace_id: str,
            tags: Iterable[str]
    ) -> None:
        self.__cid = cid
        self.__visible_area = visible_area
        self.__usable_area = usable_area
        self.__z_index = z_index
        self.__workspace_id = workspace_id
        self.__tags = tuple(tags)

    @property
    def cid(self) -> ComponentId:
        return self.__cid

    @property
    def visible_area(self) -> ScreenArea:
        """
        Total screen space taken up by the tile.  This includes all contained
        windows and any tile decoration.
        """
        return self.__visible_area

    @property
    def usable_area(self) -> ScreenArea:
        """
        Screen space usable by the contained windows.  This is a subset of the
        visible area.  Tile decoration inside this area will most likely
        not be shown, or may be shown if no windows are present in the tile.
        """
        return self.__usable_area

    @property
    def z_index(self) -> int:
        return self.__z_index

    @property
    def workspace_id(self) -> str:
        return self.__workspace_id

    @property
    def tags(self) -> Sequence[str]:
        return self.__tags

    def __repr__(self) -> str:
        return (
            'TileState(cid={cid}, visible_area={visible_area}, usable_area={usable_area}, '
            'z_index={z_index}, workspace_id={workspace_id}, '
            'tags={tags})'
        ).format(
            visible_area=repr(self.__visible_area), usable_area=repr(self.__usable_area),
            z_index=repr(self.__z_index), workspace_id=repr(self.__workspace_id),
            cid=repr(self.__cid), tags=repr(self.__tags)
        )


class WorkspaceState:
    """
    A virtual workspace state.  Each workspace has an active tile.  This
    allows a memory for when that workspace becomes active.

    Workspaces are not considered their own component.  Instead, changes to
    workspace state cause LayoutTileState to change.
    """

    __slots__ = (
        '__wid',
        '__tiles',
        '__active_tile_cid'
    )

    def __init__(self, workspace_id: str, tiles: Iterable[TileState], active_tile_cid: ComponentId) -> None:
        assert active_tile_cid in [t.cid for t in tiles]
        for t in tiles:
            assert t.workspace_id == workspace_id
        self.__wid = workspace_id
        self.__tiles = tuple(tiles)
        self.__active_tile_cid = active_tile_cid

    @property
    def workspace_id(self) -> str:
        return self.__wid

    @property
    def tiles(self) -> Sequence[TileState]:
        return self.__tiles

    @property
    def active_tile_cid(self) -> ComponentId:
        return self.__active_tile_cid


def set_tile_state(bus: EventBus, tile: TileState) -> None:
    set_state(bus, tile.cid, TileState, tile)


def create_tile_state_watch(listeners: ListenerSet, tile: TileState) -> StateWatch[TileState]:
    return StateWatch(listeners, tile.cid, tile)


# Tile creation must follow the Petronia standard for object lifecycle.
# However, there is potentially nothing that requested the creation of the
# tile (it's intrinsic to a tiling window manager, but an end user could
# request the creation of a new tile), so this target ID acts as the
# notification for a new tile having been created.  Everything else about tile
# lifecycle is the same, meaning that end-user requests to create a new tile
# uses the RequestNewComponentEvent, which means the tiling implementation
# must listen to it.
TARGET_ID_TILE_CREATION = create_singleton_identity('petronia.core.layout.api/tile-creation')


def send_tile_created_event(bus: EventBus, tile_cid: ComponentId) -> None:
    send_component_created_event(
        bus,
        RequestNewComponentEvent('tile', TARGET_ID_TILE_CREATION, 0), tile_cid
    )


def add_tile_created_listener(listener_set: ListenerSet, callback: EventCallback[ComponentCreatedEvent]) -> None:
    listener_set.listen(
        TARGET_ID_TILE_CREATION,
        as_component_created_listener,
        callback
    )


# ---------------------------------------------------------------------------

class BorderSize:
    __slots__ = (
        '__n', '__e', '__s', '__w',
    )

    def __init__(self, n: ScreenUnit, e: ScreenUnit, s: ScreenUnit, w: ScreenUnit) -> None:
        assert n >= 0 and e >= 0 and w >= 0 and s >= 0
        self.__n = n
        self.__e = e
        self.__w = w
        self.__s = s

    @property
    def n(self) -> ScreenUnit:
        return self.__n

    def get_north(self) -> ScreenUnit:
        return self.__n

    @property
    def e(self) -> ScreenUnit:
        return self.__e

    def get_east(self) -> ScreenUnit:
        return self.__e

    @property
    def s(self) -> ScreenUnit:
        return self.__s

    def get_south(self) -> ScreenUnit:
        return self.__s

    @property
    def w(self) -> ScreenUnit:
        return self.__w

    def get_west(self) -> ScreenUnit:
        return self.__w

    def __repr__(self) -> str:
        return 'BorderSize(n={n}, e={e}, s={s}, w={w})'.format(
            n=repr(self.__n), e=repr(self.__e), s=repr(self.__s), w=repr(self.__w)
        )


NO_BORDER = BorderSize(0, 0, 0, 0)


class LayoutTileState:
    """
    Contains all the tiles and workspace state information.  This is a unique state for the
    entire system.
    """

    __slots__ = (
        '__workspaces',
        '__global_tile_border',
        '__active_workspace_id',
    )

    def __init__(
            self,
            workspaces: Iterable[WorkspaceState],
            global_tile_border: BorderSize,
            active_workspace_id: str
    ) -> None:
        assert active_workspace_id in [w.workspace_id for w in workspaces]
        self.__workspaces = tuple(workspaces)
        self.__global_tile_border = global_tile_border
        self.__active_workspace_id = active_workspace_id

    @property
    def workspaces(self) -> Sequence[WorkspaceState]:
        return self.__workspaces

    @property
    def active_workspace_id(self) -> str:
        return self.__active_workspace_id

    def find_workspace(self, workspace_id: str) -> Optional[WorkspaceState]:
        for w in self.__workspaces:
            if workspace_id == w.workspace_id:
                return w
        return None

    def find_active_workspace(self) -> WorkspaceState:
        w = self.find_workspace(self.__active_workspace_id)
        assert w is not None
        return w

    def find_active_tile_cid(self) -> ComponentId:
        return self.find_active_workspace().active_tile_cid

    def find_all_tiles(self) -> Sequence[TileState]:
        ret: List[TileState] = []
        for ws in self.__workspaces:
            ret.extend(ws.tiles)
        return ret

    def find_tiles_for_workspace(self, workspace_id: str) -> Sequence[TileState]:
        ws = self.find_workspace(workspace_id)
        if ws:
            return ws.tiles
        return t_cast(Sequence[TileState], EMPTY_TUPLE)

    def find_active_workspace_tiles(self) -> Sequence[TileState]:
        return self.find_tiles_for_workspace(self.__active_workspace_id)

    def find_tile_by_cid(self, tile_id: ComponentId) -> Optional[TileState]:
        for ws in self.__workspaces:
            for tile in ws.tiles:
                if tile.cid == tile_id:
                    return tile
        return None

    def find_active_tile(self) -> TileState:
        tile = self.find_tile_by_cid(self.find_active_tile_cid())
        assert tile is not None
        return tile

    def __repr__(self) -> str:
        return 'LayoutTileState(workspaces={0}, active_workspace_id={1}, global_tile_border={2})'.format(
            repr(self.__workspaces), repr(self.__active_workspace_id),
            repr(self.__global_tile_border)
        )


def set_layout_tile_state(
        bus: EventBus,
        workspaces: Iterable[WorkspaceState],
        global_tile_border: BorderSize,
        active_workspace_id: str
) -> None:
    set_state(
        bus, STATE_ID_LAYOUT_TILE, LayoutTileState,
        LayoutTileState(workspaces, global_tile_border, active_workspace_id)
    )


INITIAL_LAYOUT_TILE_STATE = LayoutTileState(
    (WorkspaceState(
        '', (
            TileState(NOT_PARTICIPANT, ZERO_SCREEN_AREA, ZERO_SCREEN_AREA, 0, '', ()),
        ), NOT_PARTICIPANT),),
    NO_BORDER,
    ''
)


def create_layout_tile_state_watch(listeners: ListenerSet) -> StateWatch[LayoutTileState]:
    return StateWatch(
        listeners,
        STATE_ID_LAYOUT_TILE,
        INITIAL_LAYOUT_TILE_STATE
    )
