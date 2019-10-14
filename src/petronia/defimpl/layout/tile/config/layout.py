
"""
Screen layout definition and manager.

Maintains the user configuration of the layout trees, and
matches those against the current screen list.
"""

from typing import List, Tuple, Iterable, Sequence, Optional, Union
from .....aid.std import (
    EMPTY_LIST,
    ResultWithErrors,
    ErrorReport,
    create_user_error,
)
from .....core.platform.api import (
    VirtualScreenArea,
    ScreenSize,
    SCREEN_SIZE_WIDTH,
    SCREEN_SIZE_HEIGHT,
)


class PortalLayout:
    __slots__ = (
        'name',
        'size',
    )

    def __init__(self, name: Optional[str], size: int):
        self.name = name
        self.size = size

    def __repr__(self) -> str:
        return "PortalLayout(name={0}, size={1})".format(repr(self.name), repr(self.size))


TileLayout = Union[PortalLayout, 'SplitTileLayout']


class SplitTileLayout:
    """
    Defines a recursive split structure.
    """

    __slots__ = (
        '_splits',
        'is_split_target',
        'name',
        'size',
    )

    _splits: List[TileLayout]

    def __init__(
            self,
            name: Optional[str],
            size: int,
            splits: Optional[Iterable[TileLayout]], is_split_target: bool = False
    ) -> None:
        self.name = name
        self.size = size
        self._splits = list(splits or EMPTY_LIST)  # type: ignore
        self.is_split_target = is_split_target

    @property
    def splits(self) -> List[TileLayout]:
        return self._splits

    def __repr__(self) -> str:
        return "SplitTileLayout(name={0}, size={1}, is_split_target={2}, splits={3})".format(
            repr(self.name), repr(self.size), repr(self.is_split_target), repr(self._splits)
        )


class ScreenTileLayout:
    """
    A single screen's tile layout.
    """

    __slots__ = (
        'direction',
        'size',
        'primary',
        'name',
        '_layout',
    )
    _layout: List[TileLayout]

    def __init__(
            self, name: Optional[str], direction: int, primary: bool, size: ScreenSize,
            layout: Optional[Iterable[TileLayout]] = None
    ) -> None:
        self.name = name
        self.direction = direction
        self.primary = primary
        self.size = size
        self._layout = list(layout or [])

    @property
    def layout(self) -> List[TileLayout]:
        return self._layout

    def match_screen(self, screen: ScreenSize, screen_name: str, screen_index: int, current_index: int) -> int:
        """
        Generates a match value indicating how close this layout is to the
        given monitor.  A lower number means a closer match.
        :return: a number greater than 0
        """

        # If we do straight pixel area comparison, then if the x and y are
        # swapped, then they won't appear as different.  So we need another
        # mechanism to detect the difference, and make pixel differences large
        # enough to matter.

        # + 1 so that, when multiplied, a 0 doesn't change any other differences to be a 0.
        delta_x = abs((screen[SCREEN_SIZE_WIDTH] ** 2) - (self.size[SCREEN_SIZE_WIDTH] ** 2)) + 1
        delta_y = abs((screen[SCREEN_SIZE_HEIGHT] ** 2) - (self.size[SCREEN_SIZE_HEIGHT] ** 2)) + 1

        raw_match = (delta_x * delta_y) + 1

        # Adjust the pixel match by the screen name/index match.
        if self.name:
            if self.name.lower() == screen_name.lower():
                # Perfect name match - it lines up
                return raw_match
            if self.name == str(screen_index):
                # Perfect index match - it lines up
                return raw_match
        return raw_match * (abs(screen_index - current_index) + 1)

    def __repr__(self) -> str:
        return "ScreenTileLayout(name={0}, direction={1}, primary={2}, size={3}, layout={4})".format(
            repr(self.name),
            repr(self.direction),
            repr(self.primary),
            repr(self.size),
            repr(self._layout)
        )


class RootTileLayout:
    """
    Top-level definition for a collection of splits.  Each of the contained splits represents a
    screen.
    """

    __slots__ = (
        '_screen_layouts',
    )
    _screen_layouts: List[ScreenTileLayout]

    def __init__(self, screens: Iterable[ScreenTileLayout]) -> None:
        self._screen_layouts = list(screens)

    @property
    def screens(self) -> List[ScreenTileLayout]:
        return self._screen_layouts

    def __repr__(self) -> str:
        return "RootTileLayout(screens={0})".format(repr(self._screen_layouts))


def match_layouts_to_screens(
        screen_layout_combinations: Iterable[Sequence[ScreenTileLayout]],
        active_screens: Sequence[VirtualScreenArea]
) -> ResultWithErrors[Sequence[Tuple[ScreenTileLayout, VirtualScreenArea]]]:
    """
    Finds the "best" user screen layout that corresponds with the current (active)
    screens.  The ordering of the active screens and layouts is important.  If the
    active screens contains more screens than the layout, then the matcher will try
    filling in a best-match for that screen from its list of layouts.

    :param screen_layout_combinations:
    :param active_screens:
    :return: for each screen, the corresponding layout.
    """

    errors: List[ErrorReport] = []

    # Issues this will try to tackle:
    #  - The layout may match except for the index position.  In this case, the
    #    layout can still work, but at a penalty to the match.
    #  - The full layout may have more screens than the active screens.  In this
    #    case, extra layouts are marked as a penalty.
    #  - There may be more screens than layouts.  In this case, match the best
    #    layout to the screen, but note that the layout index to screen index
    #    penalty will take effect.

    # These numbers can get really, really big.  Use None to avoid an issue
    # where the match number is bigger than the initial assumption of
    # too big.
    best_match: Optional[int] = None
    best_layout: Sequence[Tuple[ScreenTileLayout, VirtualScreenArea]] = []

    # print("** Matching screens {0}".format(active_screens))

    for layout_map in screen_layout_combinations:
        # print("Trying layout {0}".format(layout_map))
        # For this layout, find the best screen tile layout match for each screen.
        all_screens: List[Tuple[ScreenTileLayout, VirtualScreenArea]] = []
        all_screen_match = 0
        for screen_index in range(len(active_screens)):
            screen = active_screens[screen_index]
            # print(" - against screen {0} -> {1}".format(screen_index, screen))
            best_screen: Optional[ScreenTileLayout] = None
            best_screen_match: Optional[int] = None
            for layout_index in range(len(layout_map)):
                layout = layout_map[layout_index]
                # print(" -- layout {0} -> {1}".format(layout_index, layout))
                # Because the match is guaranteed to be > 0, the raw match can be
                # directly multiplied by the index delta, but note that the index
                # delta must itself be positive (not zero) for this to work.
                match = layout.match_screen(screen.get_size(), screen.name, screen_index, layout_index)
                # print(" -- match {0}:{1} vs {2}:{3} :: {4}".format(
                #     layout_index, layout,
                #     screen_index, screen,
                #     match
                # ))
                if best_screen_match is None or match < best_screen_match:
                    best_screen = layout
                    best_screen_match = match
            if not best_screen or not best_screen_match:
                errors.append(create_user_error(
                    match_layouts_to_screens, 'no layouts in screen {si}', si=screen_index
                ))
            else:
                all_screen_match += best_screen_match
                all_screens.append((best_screen, screen,))
        if best_match is None or all_screen_match < best_match:
            best_match = all_screen_match
            best_layout = tuple(all_screens)

    if not best_layout:
        errors.append(create_user_error(
            match_layouts_to_screens, 'no layouts or screens in {sc}', sc=repr(screen_layout_combinations)
        ))
        return [], errors

    return best_layout, errors
