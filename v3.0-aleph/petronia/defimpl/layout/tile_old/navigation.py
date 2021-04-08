
"""
Manages navigation through the portals.
"""

from typing import List, Sequence, Tuple, Iterable, Callable, Optional, Any, no_type_check
from .portal import Portal
from ....aid.std import ComponentId
from ....core.platform.api import (
    SCREEN_AREA_X, SCREEN_AREA_Y, SCREEN_AREA_WIDTH, SCREEN_AREA_HEIGHT,
)


class PortalNav:
    """
    Navigation tool for a single portal.
    """

    __slots__ = ('portal', 'index', 'north', 'east', 'south', 'west', 'path')

    def __init__(
            self, portal: Portal, index: int, north: int, east: int, south: int, west: int, path: Iterable[int]
    ) -> None:
        self.portal = portal
        self.index = index
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.path = tuple(path)

    @no_type_check
    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, PortalNav):
            return False
        return (
                other.portal is self.portal and
                other.index == self.index and
                other.north == self.north and
                other.east == self.east and
                other.south == self.south and
                other.west == self.west and
                other.path == self.path
        )

    @no_type_check
    def __ne__(self, other: Any) -> bool:
        return not self.__eq__(other)

    def __repr__(self) -> str:
        return "PortalNav(portal={0}, index={1}, north={2}, east={3}, south={4}, west={5}, path={6}".format(
            repr(self.portal), repr(self.index), repr(self.north), repr(self.east), repr(self.south),
            repr(self.west), repr(self.path)
        )


class Navigator:
    """
    Stateful helper for navigating through portals.

    This keeps track of the active portal and active window.

    If the list of portals or how they are positioned changes, then this needs to be
    recreated.
    """

    __slots__ = (
        '__active_nav',
        '__portals',
    )

    def __init__(
            self, active_window: Optional[ComponentId],
            portal_paths: Iterable[Tuple[Portal, Sequence[int]]], wrap_x: bool, wrap_y: bool
    ) -> None:
        self.__portals = create_navs(portal_paths, wrap_x, wrap_y)
        assert len(self.__portals) > 0
        self.__active_nav = 0
        if active_window:
            for portal_nav in self.__portals:
                if portal_nav.portal.has_window(active_window):
                    self.__active_nav = portal_nav.index
                    break

    def get_active_portal_and_path(self) -> Tuple[Portal, Sequence[int]]:
        active = self.__portals[self.__active_nav]
        return active.portal, active.path

    def get_active_portal(self) -> Portal:
        active = self.__portals[self.__active_nav]
        return active.portal

    def make_active_choice(self, decider: Callable[[Portal], bool]) -> Optional[Tuple[Portal, Sequence[int]]]:
        for portal_nav in self.__portals:
            if decider(portal_nav.portal):
                self.__active_nav = portal_nav.index
                return portal_nav.portal, portal_nav.path
        return None

    def move_north(self) -> Optional[Tuple[Portal, Sequence[int]]]:
        active = self.__portals[self.__active_nav]
        if active.north >= 0:
            self.__active_nav = active.north
            north = self.__portals[active.north]
            active.portal.set_focus(False)
            north.portal.set_focus(True)
            return north.portal, north.path
        return None

    def move_east(self) -> Optional[Tuple[Portal, Sequence[int]]]:
        active = self.__portals[self.__active_nav]
        if active.east >= 0:
            self.__active_nav = active.east
            east = self.__portals[active.east]
            active.portal.set_focus(False)
            east.portal.set_focus(True)
            return east.portal, east.path
        return None

    def move_south(self) -> Optional[Tuple[Portal, Sequence[int]]]:
        active = self.__portals[self.__active_nav]
        if active.south >= 0:
            self.__active_nav = active.south
            south = self.__portals[active.south]
            active.portal.set_focus(False)
            south.portal.set_focus(True)
            return south.portal, south.path
        return None

    def move_west(self) -> Optional[Tuple[Portal, Sequence[int]]]:
        active = self.__portals[self.__active_nav]
        if active.west >= 0:
            self.__active_nav = active.west
            west = self.__portals[active.west]
            active.portal.set_focus(False)
            west.portal.set_focus(True)
            return west.portal, west.path
        return None


MAX_POSITION = 9999999999999

WEST_X_INDEX = 0
EAST_X_INDEX = 1
NORTH_Y_INDEX = 2
SOUTH_Y_INDEX = 3
MID_X_INDEX = 4
MID_Y_INDEX = 5
MIN_X_INDEX = WEST_X_INDEX
MAX_X_INDEX = EAST_X_INDEX
MIN_Y_INDEX = NORTH_Y_INDEX
MAX_Y_INDEX = SOUTH_Y_INDEX


def get_portal_location(portal: Portal) -> Tuple[int, int, int, int, int, int]:
    area = portal.get_area()
    return (
        area[SCREEN_AREA_X],  # WEST_X_INDEX = 0
        area[SCREEN_AREA_X] + area[SCREEN_AREA_WIDTH] - 1,  # EAST_X_INDEX = 1
        area[SCREEN_AREA_Y],  # NORTH_Y_INDEX = 2
        area[SCREEN_AREA_Y] + area[SCREEN_AREA_HEIGHT] - 1,  # SOUTH_Y_INDEX = 3
        area[SCREEN_AREA_WIDTH] // 2 + area[SCREEN_AREA_X],  # MID_X_INDEX = 4
        area[SCREEN_AREA_HEIGHT] // 2 + area[SCREEN_AREA_Y],  # MID_Y_INDEX = 5
    )


def create_navs(portal_paths: Iterable[Tuple[Portal, Sequence[int]]], wrap_x: bool, wrap_y: bool) -> List[PortalNav]:
    """
    Creates a list of portals, and how they navigate between other portals.

    This uses the location within the portal to determine the movement relationship.  It finds the closest portal
    to the midpoint edge.

    :param portal_paths: list of portals to construct in the returned navigation.
    :param wrap_x: True if e/w wrapping should be enabled.  Otherwise, a -1 index indicates an end-of-navigation.
    :param wrap_y: True if n/s wrapping should be enabled.  Otherwise, a -1 index indicates an end-of-navigation.
    :return:
    """

    # Slow, simple, accurate.  Speed improvements to this O(n^2) algorithm. are sure to exist.
    portals = list(portal_paths)

    if wrap_x:
        min_x = MAX_POSITION
        max_x = -MAX_POSITION
        for portal, portal_path in portals:
            portal_area = portal.get_area()
            min_x = min(min_x, portal_area[SCREEN_AREA_X])
            max_x = max(max_x, portal_area[SCREEN_AREA_X] + portal_area[SCREEN_AREA_WIDTH] - 1)
    else:
        min_x = -MAX_POSITION
        max_x = MAX_POSITION
    if wrap_y:
        min_y = MAX_POSITION
        max_y = -MAX_POSITION
        for portal, portal_path in portals:
            portal_area = portal.get_area()
            min_y = min(min_y, portal_area[SCREEN_AREA_Y])
            max_y = max(max_y, portal_area[SCREEN_AREA_Y] + portal_area[SCREEN_AREA_HEIGHT] - 1)
    else:
        min_y = -MAX_POSITION
        max_y = MAX_POSITION

    # For each portal, find the closest portal to each other midpoint.
    # The returned list has the same portal ordering as the input.  That bit of information helps to
    # assign indices to portal directions.

    ret: List[PortalNav] = []
    for target_index in range(len(portals)):
        target, target_path = portals[target_index]
        target_loc = get_portal_location(target)

        is_target_e_edge = target_loc[MAX_X_INDEX] >= max_x
        is_target_w_edge = target_loc[MIN_X_INDEX] <= min_x
        is_target_s_edge = target_loc[MAX_Y_INDEX] >= max_y
        is_target_n_edge = target_loc[MIN_Y_INDEX] <= min_y

        best_e_index = -1
        best_e_y_dist = MAX_POSITION
        best_e_x_dist = MAX_POSITION

        best_w_index = -1
        best_w_y_dist = MAX_POSITION
        best_w_x_dist = MAX_POSITION

        best_n_index = -1
        best_n_y_dist = MAX_POSITION
        best_n_x_dist = MAX_POSITION

        best_s_index = -1
        best_s_y_dist = MAX_POSITION
        best_s_x_dist = MAX_POSITION

        for source_index in range(len(portals)):
            if source_index == target_index:
                # Don't map to yourself.  In the case of a wrap + full length portal, the no-op is the
                # correct choice, not trying to wrap to yourself.
                continue
            source, source_path = portals[source_index]
            source_loc = get_portal_location(source)

            is_source_e_edge = source_loc[MAX_X_INDEX] >= max_x
            is_source_w_edge = source_loc[MIN_X_INDEX] <= min_x
            is_source_s_edge = source_loc[MAX_Y_INDEX] >= max_y
            is_source_n_edge = source_loc[MIN_Y_INDEX] <= min_y

            # Edges should line up, but might not.  If the user navigates up through a hole, it should navigate
            # up to the nearest portal strictly above it.  Think of a checkerboard pattern.  If only the red
            # areas have portals, then the up will move diagonally.  Currently, there is no protection against
            # favored direction, which will lead to "up" being a NE or NW movement, rather than an alternating
            # east/west pattern.

            # 1. Check NORTH edge.
            if is_target_n_edge and is_source_s_edge:
                # y distance is 0.  Can't get better than that.
                x_dist = abs(source_loc[MID_X_INDEX] - target_loc[MID_X_INDEX])
                if x_dist < best_n_x_dist:
                    best_n_x_dist = x_dist
                    best_n_y_dist = 0
                    best_n_index = source_index
            else:
                y_dist = target_loc[NORTH_Y_INDEX] - source_loc[SOUTH_Y_INDEX]
                if 0 <= y_dist <= best_n_y_dist:
                    x_dist = abs(source_loc[MID_X_INDEX] - target_loc[MID_X_INDEX])
                    if x_dist < best_n_x_dist:
                        best_n_x_dist = x_dist
                        best_n_y_dist = y_dist
                        best_n_index = source_index
            # else not eligible for N edge direction.

            # 2. Check EAST edge.
            if is_target_e_edge and is_source_w_edge:
                # x distance is 0.  Can't get better than that.
                y_dist = abs(source_loc[MID_Y_INDEX] - target_loc[MID_Y_INDEX])
                if y_dist < best_e_y_dist:
                    best_e_x_dist = 0
                    best_e_y_dist = y_dist
                    best_e_index = source_index
            else:
                x_dist = source_loc[WEST_X_INDEX] - target_loc[EAST_X_INDEX]
                if 0 <= x_dist <= best_e_x_dist:
                    y_dist = abs(source_loc[MID_Y_INDEX] - target_loc[MID_Y_INDEX])
                    if y_dist < best_e_y_dist:
                        best_e_x_dist = x_dist
                        best_e_y_dist = y_dist
                        best_e_index = source_index
            # else not eligible for E edge direction

            # 3. Check SOUTH edge.
            if is_target_s_edge and is_source_n_edge:
                # y distance is 0.  Can't get better than that.
                x_dist = abs(source_loc[MID_X_INDEX] - target_loc[MID_X_INDEX])
                if x_dist < best_s_x_dist:
                    best_s_x_dist = x_dist
                    best_s_y_dist = 0
                    best_s_index = source_index
            else:
                y_dist = target_loc[SOUTH_Y_INDEX] - source_loc[NORTH_Y_INDEX]
                if 0 <= y_dist <= best_s_y_dist:
                    x_dist = abs(source_loc[MID_X_INDEX] - target_loc[MID_X_INDEX])
                    if x_dist < best_s_x_dist:
                        best_s_x_dist = x_dist
                        best_s_y_dist = y_dist
                        best_s_index = source_index
            # else not eligible for S edge direction.

            # 4. Check WEST edge.
            if is_target_w_edge and is_source_e_edge:
                # x distance is 0.  Can't get better than that.
                y_dist = abs(source_loc[MID_Y_INDEX] - target_loc[MID_Y_INDEX])
                if y_dist < best_w_y_dist:
                    best_w_x_dist = 0
                    best_w_y_dist = y_dist
                    best_w_index = source_index
            else:
                x_dist = target_loc[WEST_X_INDEX] - source_loc[EAST_X_INDEX]
                if 0 <= x_dist <= best_w_x_dist:
                    y_dist = abs(source_loc[MID_Y_INDEX] - target_loc[MID_Y_INDEX])
                    if y_dist < best_w_y_dist:
                        best_w_x_dist = x_dist
                        best_w_y_dist = y_dist
                        best_w_index = source_index
            # else not eligible for W edge direction

        ret.append(PortalNav(
            target, target_index, path=target_path,
            north=best_n_index, east=best_e_index, south=best_s_index, west=best_w_index
        ))

    return ret
