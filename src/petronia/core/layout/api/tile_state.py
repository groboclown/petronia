
"""
State information for tile-based layouts.

Tiles add another abstraction beyond just windows - there is an additional concept of a
tile in which a window can reside.  The individual tiles can have separate decoration
or information than the windows.
"""

from typing import Iterable, Sequence
from ....aid.std import (
    ComponentId,
    EventBus,
    EventCallback,
    ListenerSet,
    StateWatch,
    create_singleton_identity,
    set_state,
)
from ....aid.bootstrap import (
    NOT_PARTICIPANT,
)
from ....base.events import (
    ComponentCreatedEvent,
    as_component_created_listener,
    RequestNewComponentEvent,
    send_component_created_event,
)
from ...platform.api import (
    ScreenArea,
)


STATE_ID_TILE = create_singleton_identity('petronia.core.layout.api/tiles')


class TileState:
    """
    Abstract tile state.
    """
    __slots__ = (
        '__cid',
        '__area',
        '__border_width',
        '__window_cids',
        '__active',
        '__tags',
    )

    def __init__(
            self,
            cid: ComponentId,
            area: ScreenArea,
            border_width: int,
            is_active: bool,
            window_cids: Iterable[ComponentId],
            tags: Iterable[str]
    ) -> None:
        self.__cid = cid
        self.__area = area
        self.__border_width = border_width
        self.__window_cids = tuple(window_cids)
        self.__active = is_active
        self.__tags = tuple(tags)

    @property
    def cid(self) -> ComponentId:
        return self.__cid

    @property
    def area(self) -> ScreenArea:
        return self.__area

    @property
    def border_width(self) -> int:
        return self.__border_width

    @property
    def window_cids(self) -> Sequence[ComponentId]:
        return self.__window_cids

    @property
    def is_active(self) -> bool:
        return self.__active

    @property
    def tags(self) -> Sequence[str]:
        return self.__tags

    def __repr__(self) -> str:
        return (
            'TileState(cid={cid}, area={area}, border_width={border_width}, '
            'is_active={is_active}, tags={tags}, window_cids={window_cids})'
        ).format(
            area=repr(self.__area), border_width=repr(self.__border_width), is_active=repr(self.__active),
            window_cids=repr(self.__window_cids),
            cid=repr(self.__cid), tags=repr(self.__tags)
        )


class AllTileState:
    """
    Contains all the tiles.
    """

    __slots__ = (
        '__tiles',
    )

    def __init__(self, tiles: Iterable[TileState]) -> None:
        self.__tiles = tuple(tiles)
        assert len(self.__tiles) > 0

    @property
    def tiles(self) -> Sequence[TileState]:
        return self.__tiles

    def find_active_tile(self) -> TileState:
        active = self.__tiles[0]
        for t in self.__tiles[1:]:
            if t.is_active:
                active = t
        return active

    def __repr__(self) -> str:
        return 'AllTileState({0})'.format(repr(self.__tiles))


def set_tile_states(bus: EventBus, states: Iterable[TileState]) -> None:
    set_state(bus, STATE_ID_TILE, AllTileState, AllTileState(states))


def create_tile_state_watch(listeners: ListenerSet) -> StateWatch[AllTileState]:
    return StateWatch(
        listeners,
        STATE_ID_TILE,
        AllTileState((TileState(NOT_PARTICIPANT, (0, 0, 0, 0), 0, False, (), ()),))
    )


# ---------------------------------------------------------------------------


# Tile creation must follow the Petronia standard for object lifecycle.  However,
# there is nothing that requested the creation of the tile (it's intrinsic to a
# tiling window manager), so this target ID acts as the notification for new
# tiles.  Everything else about tile lifecycle is the same.
TARGET_ID_TILE_CREATION = create_singleton_identity('petronia.core.layout.api/tile-creation')


def send_tile_created_event(bus: EventBus, tile_cid: ComponentId) -> None:
    send_component_created_event(
        bus,
        RequestNewComponentEvent(tile_cid, TARGET_ID_TILE_CREATION, 0), tile_cid
    )


def add_tile_created_listener(listener_set: ListenerSet, callback: EventCallback[ComponentCreatedEvent]) -> None:
    listener_set.listen(
        TARGET_ID_TILE_CREATION,
        as_component_created_listener,
        callback
    )
