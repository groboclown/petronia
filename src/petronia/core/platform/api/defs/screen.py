
"""
Definitions for data types of the screen.
"""

from typing import Dict, Sequence, Union, Optional
from .units import (
    ScreenArea, NativeScreenArea, ScreenPosition,
    SCREEN_AREA_X, SCREEN_AREA_Y, SCREEN_AREA_W, SCREEN_AREA_H,
    SCREEN_POSITION_X, SCREEN_POSITION_Y,
)

# A platform specific way of referencing the screen.
# This only has meaning to the platform.
ScreenHandle = Union[str, int, Sequence[str], Sequence[int]]


class VirtualScreenArea:
    """
    Information about a sub-section of the screen, usually mapped to
    a monitor.
    """

    __slots__ = (
        '__area', '__name', '__is_primary', '__vid'
    )

    def __init__(self, name: str, area: ScreenArea, is_primary: bool) -> None:
        self.__name = name
        self.__area = (area[SCREEN_AREA_X], area[SCREEN_AREA_Y], area[SCREEN_AREA_W], area[SCREEN_AREA_H],)
        self.__is_primary = is_primary
        self.__vid = '{0}x{1}'.format(area[SCREEN_AREA_X], area[SCREEN_AREA_Y])

    @property
    def name(self) -> str:
        return self.__name

    @property
    def area(self) -> ScreenArea:
        return self.__area

    @property
    def is_primary(self) -> bool:
        return self.__is_primary

    # Not properties, because they are derived, and making them properties
    # would change how the serialization of the event works.

    def get_vid(self) -> str:
        """A 'virtual ID' of the screen area.  Should be unique enough per
        video layout to allow for configuration mappings."""
        return self.__vid

    def get_x(self) -> int:
        return self.__area[SCREEN_AREA_X]

    def get_y(self) -> int:
        return self.__area[SCREEN_AREA_Y]

    def get_w(self) -> int:
        return self.__area[SCREEN_AREA_W]

    def get_width(self) -> int:
        return self.__area[SCREEN_AREA_W]

    def get_h(self) -> int:
        return self.__area[SCREEN_AREA_H]

    def get_height(self) -> int:
        return self.__area[SCREEN_AREA_H]

    def get_left(self) -> int:
        return self.__area[SCREEN_AREA_X]

    def get_right(self) -> int:
        """Right-most pixel; still inside the screen area."""
        return self.__area[SCREEN_AREA_X] + self.__area[SCREEN_AREA_W] - 1

    def get_top(self) -> int:
        return self.__area[SCREEN_AREA_Y]

    def get_bottom(self) -> int:
        """Bottom-most pixel; still inside the screen area."""
        return self.__area[SCREEN_AREA_Y] + self.__area[SCREEN_AREA_H] - 1

    def contains(self, pos: ScreenPosition) -> bool:
        return (
            (
                self.__area[SCREEN_AREA_X] <=
                pos[SCREEN_POSITION_X] <
                (self.__area[SCREEN_AREA_X] + self.__area[SCREEN_AREA_W])
            ) and
            (
                    self.__area[SCREEN_AREA_Y] <=
                    pos[SCREEN_POSITION_Y] <
                    (self.__area[SCREEN_AREA_Y] + self.__area[SCREEN_AREA_H])
            )
        )

    def __repr__(self) -> str:
        return 'VirtualScreenArea(name={0}, area=({1},{2})x({3},{4}), is_primary: {5}, vid: {6})'.format(
            repr(self.__name),
            self.get_left(), self.get_top(), self.get_right(), self.get_bottom(),
            self.__is_primary,
            self.__vid
        )


class VirtualScreenInfo:
    """
    Information about the screens, as viewed by a Petronia application.  The
    platform translates this to the native resolution.
    """

    __slots__ = (
        '__blocks',
    )

    def __init__(self, blocks: Sequence[VirtualScreenArea]) -> None:
        assert blocks
        self.__blocks = tuple(blocks)

    @property
    def blocks(self) -> Sequence[VirtualScreenArea]:
        return self.__blocks

    def get_primary(self) -> VirtualScreenArea:
        for block in self.__blocks:
            if block.is_primary:
                return block
        return self.__blocks[0]

    def get_block_with_vid(self, vid: str) -> Optional[VirtualScreenArea]:
        for block in self.__blocks:
            if block.get_vid() == vid:
                return block
        return None

    def get_by_vid(self) -> Dict[str, VirtualScreenArea]:
        ret: Dict[str, VirtualScreenArea] = {}
        for block in self.__blocks:
            ret[block.get_vid()] = block
        return ret

    def get_screen_at(self, pos: ScreenPosition) -> Optional[VirtualScreenArea]:
        for block in self.__blocks:
            if block.contains(pos):
                return block
        return None


class NativeScreenInfo:
    """A single "screen" with its information.  This represents the screen as the underlying
    platform sees it."""

    __slots__ = (
        '__handle',
        '__screen_size', '__work_area',
        '__is_primary', '__screen_index', '__name',
    )

    def __init__(
            self,
            handle: ScreenHandle, screen_index: int, is_primary: bool,
            screen_size: NativeScreenArea, work_area: ScreenArea,
            name: str
    ) -> None:
        self.__handle = handle
        self.__screen_index = screen_index
        self.__is_primary = is_primary
        self.__screen_size = screen_size
        self.__work_area = work_area
        self.__name = name

    @property
    def handle(self) -> ScreenHandle:
        """Opaque, platform-specific handle for the screen."""
        return self.__handle

    @property
    def screen_index(self) -> int:
        """Platform-specific index for the screen."""
        return self.__screen_index

    @property
    def screen_size(self) -> NativeScreenArea:
        """Native platform coordinates for the screen."""
        return self.__screen_size

    @property
    def work_area(self) -> NativeScreenArea:
        """Native platform coordinates for the area where the windows can appear."""
        return self.__work_area

    @property
    def name(self) -> str:
        """Screen device name."""
        return self.__name

    @property
    def is_primary(self) -> bool:
        return self.__is_primary