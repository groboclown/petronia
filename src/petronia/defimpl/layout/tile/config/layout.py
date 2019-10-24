
# Because mypy freaks out and starts injecting Any within the complex function.
# mypy: allow-any-expr

"""
Screen layout definition and manager.

Maintains the user configuration of the layout trees, and
matches those against the current screen list.
"""

from typing import List, Tuple, Iterable, Sequence, Set, Optional, Union
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
    SCREEN_AREA_WIDTH,
    SCREEN_AREA_HEIGHT,
)
from .....base.util.loop import permutations


class PortalLayout:
    __slots__ = (
        'name',
        'size',
        'default_fill',
    )

    def __init__(self, name: Optional[str], size: int, default_fill: str):
        self.name = name
        self.size = size
        self.default_fill = default_fill

    def __repr__(self) -> str:
        return "PortalLayout(name={0}, size={1}, default_fill={2})".format(
            repr(self.name), repr(self.size), repr(self.default_fill)
        )


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

        raw_match = (delta_x + delta_y) + 1

        # Adjust the pixel match by the screen name/index match.
        if self.name:
            if self.name.lower().strip() == screen_name.lower().strip():
                # Perfect name match - it lines up
                return raw_match
            if self.name == str(screen_index):
                # Perfect index match - it lines up
                return raw_match
        match = raw_match * (abs(screen_index - current_index) + 1)
        # print("DEBUG match == (({0} ^2 - {1} ^2) + ({2} ^2 - {3} ^2) + 3) * ({4} - {5} + 1) = {6}".format(
        #     screen[SCREEN_SIZE_WIDTH],
        #     self.size[SCREEN_SIZE_WIDTH],
        #     screen[SCREEN_SIZE_HEIGHT],
        #     self.size[SCREEN_SIZE_HEIGHT],
        #     screen_index,
        #     current_index,
        #     match
        # ))
        return match

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
        '_screen_layouts', '_name',
    )
    _screen_layouts: List[ScreenTileLayout]

    def __init__(self, name: str, screens: Iterable[ScreenTileLayout]) -> None:
        self._name = name
        self._screen_layouts = list(screens)

    @property
    def name(self) -> str:
        return self._name

    @property
    def screens(self) -> List[ScreenTileLayout]:
        return self._screen_layouts

    def __repr__(self) -> str:
        return "RootTileLayout(name={0}, screens={1})".format(repr(self._name), repr(self._screen_layouts))


def match_layouts_to_screens(
        screen_layout_combinations: Iterable[Sequence[ScreenTileLayout]],
        active_screens: Sequence[VirtualScreenArea]
) -> ResultWithErrors[Tuple[int, Sequence[Tuple[ScreenTileLayout, VirtualScreenArea]]]]:
    """
    Last-ditch effort to match a layout to the screens.  It doesn't take into account
    if the screen count matches the layout screen count.

    :param screen_layout_combinations:
    :param active_screens:
    :return: layout index chosen ; for each screen, the corresponding layout ; errors
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
    best_index = -1
    best_layout_match = -1
    best_layout: Sequence[Tuple[ScreenTileLayout, VirtualScreenArea]] = []

    # print("** Matching screens {0}".format(active_screens))

    index = -1
    for layout_map in screen_layout_combinations:
        index += 1

        # Find the layout screen to each screen match count.  If the number of screens != number of layout
        # screens, then a penalty is added.

        permutation_indices = permutations(max(len(active_screens), len(layout_map)))

        layout_screen_match_set_list: List[LayoutScreenMatchSet] = []
        for layout_screen_index in range(len(layout_map)):
            ls_match = LayoutScreenMatchSet(layout_map[layout_screen_index], layout_screen_index, [])

            for screen_index in range(len(active_screens)):
                ls_match.add_screen(active_screens[screen_index], screen_index)
            layout_screen_match_set_list.append(ls_match)

        best_screen_layout_match = -1
        # screen_index -> layout
        best_screen_layout: List[Tuple[ScreenTileLayout, VirtualScreenArea]] = []

        # Permute through each screen, using the screen permutation indicies.
        # Because the permutation_indicies list is the maximum of the two indicies,
        # then:
        #   - if screen count == layout count, it's all good.
        #   - if screen count > layout count, a fake ful-screen layout is used, and that size is a penalty.
        #   - if screen count < layout count, then each unused layout is a penalty.

        for screen_to_layout_perm in permutation_indices:
            total_match = 0
            current_layout_list: List[Tuple[ScreenTileLayout, VirtualScreenArea]] = []
            used_layout_indices: Set[int] = set()
            # print(" - Permutation " + repr(screen_to_layout_perm))
            for screen_index in range(len(active_screens)):
                screen = active_screens[screen_index]
                if screen_index >= len(layout_screen_match_set_list):
                    # Find best layout match
                    tmp_best_match = -1
                    tmp_best_layout_screen = layout_screen_match_set_list[0].layout_screen
                    for layout_screen_matcher_set in layout_screen_match_set_list:
                        match = layout_screen_matcher_set.match_screen(screen, screen_index)
                        if tmp_best_match < 0 or match < tmp_best_match:
                            tmp_best_match = match
                            tmp_best_layout_screen = layout_screen_matcher_set.layout_screen
                    current_layout_list.append((tmp_best_layout_screen, screen,))
                    total_match += screen.area[SCREEN_AREA_WIDTH] * screen.area[SCREEN_AREA_HEIGHT]
                    # print(" -- Adding extra screen {0} for penalty {1} ; {2}".format(
                    #     screen_index, screen.area[SCREEN_AREA_WIDTH] * screen.area[SCREEN_AREA_HEIGHT], total_match
                    # ))
                else:
                    # Number of screens <= number of layouts.
                    assert screen_index < len(screen_to_layout_perm)
                    layout_index = screen_to_layout_perm[screen_index]
                    assert layout_index < len(layout_screen_match_set_list)
                    layout_screen_matcher = layout_screen_match_set_list[layout_index].matches[screen_index]
                    used_layout_indices.add(layout_index)
                    current_layout_list.append((layout_screen_matcher.layout_screen, screen,))
                    total_match += layout_screen_matcher.match
                    # print(" -- Added layout {0} as screen {1} with match {2} ; {3}".format(
                    #     layout_index, screen_index, layout_screen.match, total_match
                    # ))
            for layout_screen_matcher_set in layout_screen_match_set_list:
                if layout_screen_matcher_set.layout_screen_index not in used_layout_indices:
                    total_match += layout_screen_matcher_set.missing_screen_match()
                    # print(" -- Extra layout {0} causing penalty of {1} ; {2}".format(
                    #     layout_screen.layout_screen_index, layout_screen.missing_screen_match(), total_match
                    # ))

            if best_screen_layout_match < 0 or total_match < best_screen_layout_match:
                # print(" -- >> Now the best match")
                best_screen_layout_match = total_match
                best_screen_layout = current_layout_list

        if best_layout_match < 0 or best_screen_layout_match < best_layout_match:
            best_layout = best_screen_layout
            best_layout_match = best_screen_layout_match
            best_index = index

    if not best_layout:
        errors.append(create_user_error(
            match_layouts_to_screens, 'no layouts or screens in {sc}', sc=repr(screen_layout_combinations)
        ))

    return (best_index, tuple(best_layout)), errors


class LayoutScreenMatch:
    __slots__ = (
        'layout_screen', 'monitor', 'match',
        'layout_screen_index', 'monitor_index',
    )

    def __init__(
            self,
            layout_screen: ScreenTileLayout,
            layout_screen_index: int,
            monitor: VirtualScreenArea,
            monitor_index: int,
            match: int
    ) -> None:
        self.layout_screen = layout_screen
        self.layout_screen_index = layout_screen_index
        self.monitor = monitor
        self.monitor_index = monitor_index
        self.match = match


class LayoutScreenMatchSet:
    __slots__ = (
        'layout_screen', 'layout_screen_index',
        'matches',
    )

    def __init__(
            self,
            layout_screen: ScreenTileLayout,
            layout_screen_index: int,
            matches: List[LayoutScreenMatch]
    ) -> None:
        self.layout_screen = layout_screen
        self.layout_screen_index = layout_screen_index
        self.matches = matches

    def add_screen(self, monitor: VirtualScreenArea, index: int) -> None:
        self.matches.append(LayoutScreenMatch(
            self.layout_screen, self.layout_screen_index, monitor, index,
            self.match_screen(monitor, index)
        ))

    def missing_screen_match(self) -> int:
        return self.layout_screen.size[0] * self.layout_screen.size[1]

    def match_screen(self, monitor: VirtualScreenArea, index: int) -> int:
        return self.layout_screen.match_screen(
            (monitor.area[SCREEN_AREA_WIDTH], monitor.area[SCREEN_AREA_HEIGHT]),
            monitor.name, index, self.layout_screen_index
        )
