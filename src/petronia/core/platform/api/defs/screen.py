
"""
Definitions for data types of the screen.
"""

from typing import Dict, Sequence, Union
from .units import ScreenArea

# A platform specific way of referencing the screen.
# This only has meaning to the platform.
ScreenHandle = Union[str, int, Sequence[str], Sequence[int]]


class VirtualScreenInfo:
    """
    Information about the screens, as viewed by a Petronia application.  The
    platform translates this to the native resolution.
    """

    __slots__ = (
        '__blocks',
    )

    def __init__(self, blocks: Sequence[ScreenArea]) -> None:
        self.__blocks = blocks


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
            screen_size: ScreenArea, work_area: ScreenArea,
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
    def screen_size(self) -> ScreenArea:
        """Native platform coordinates for the screen."""
        return self.__screen_size

    @property
    def work_area(self) -> ScreenArea:
        """Native platform coordinates for the area where the windows can appear."""
        return self.__work_area

    @property
    def name(self) -> str:
        """Screen device name."""
        return self.__name
