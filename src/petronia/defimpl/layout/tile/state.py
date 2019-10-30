
"""
Tiling manager state.
"""

# TODO refine these states, and integrate them into the handler.
#   These states must be useful enough to allow other components to add chrome
#   on top of the tiling, and to provide graphical information about
#   the screen + portal state.

from typing import Sequence
from ....aid.std import (
    ComponentId,
)


class PortalState:
    """
    Describes a single portal's state.
    """


class TileScreenState:
    """
    Describes a screen's state.

    The tiling manager handles the platform events to the windows inside
    the screen.  Anything extra added on top of the tiling manager must
    be handled by the thing that adds the extra stuff.
    """
    __slots__ = (
        '__cid', '__index', '__tag',
        '__portals', '__active_portal_index',
    )

    def __init__(
            self, cid: ComponentId, index: int, tag: str, portals: Sequence[PortalState],
            active_portal_index: ComponentId
    ) -> None:
        self.__cid = cid
        self.__index = index
        self.__tag = tag
        self.__portals = tuple(portals)
        self.__active_portal_index = active_portal_index

    @property
    def index(self) -> int:
        """
        Virtual screen index.

        :return:
        """
        return self.__index


class TileState:
    """
    State for the entire tiling system.

    Each screen has its own, independently updated state.
    """
    __slots__ = (
        '__screen_component_ids',
        '__active_screen_component_id',
    )

    def __init__(
            self, screens: Sequence[TileScreenState],
            active_screen: ComponentId
    ) -> None:
        self.__screen_component_ids = tuple(screens)
        self.__active_screen_component_id = active_screen
