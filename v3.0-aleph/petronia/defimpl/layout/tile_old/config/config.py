
"""
Process the configuration.
"""

from typing import Sequence, Iterable
from .....aid.std import (
    create_singleton_identity,
)
from .layout import (
    RootTileLayout,
)
from .match import MatchWindowToPortal


CONFIG_ID_TILE_LAYOUT = create_singleton_identity('default.layout.tile/setup-configuration')


class TileLayoutConfig:
    """
    Configuration for the layout.
    """

    __slots__ = (
        '__layouts',
        '__window_matchers',
    )

    def __init__(
            self,
            layouts: Iterable[RootTileLayout],
            matchers: Iterable[MatchWindowToPortal]
    ) -> None:
        self.__layouts = tuple(layouts)
        self.__window_matchers = tuple(matchers)

    @property
    def layouts(self) -> Sequence[RootTileLayout]:
        return self.__layouts

    @property
    def matchers(self) -> Sequence[MatchWindowToPortal]:
        return self.__window_matchers

    def __repr__(self) -> str:
        return "TileLayoutConfig(layouts={0}, matchers={1})".format(repr(self.__layouts), repr(self.__window_matchers))
