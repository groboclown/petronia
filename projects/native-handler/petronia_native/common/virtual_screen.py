"""Maintains the state of the virtual screen, which divides the monitors into blocks of
virtual space relative to each other."""

from typing import List, Sequence, Tuple, Set, Optional, Any, cast
from petronia_common.util import StdRet, UserMessage, RET_OK_NONE, join_errors
from petronia_common.util import i18n as _
from . import defs
from .user_messages import TRANSLATION_CATALOG
from .events.impl import monitor


class VirtualScreenBlock:  # pylint:disable=too-many-instance-attributes
    """A single block of virtual screen space, which maps to a single monitor.
    This assumes that the monitor has already been rotated in the setup, which
    means it's a flat mapping.

    This structure has a whole bunch of instance variables.  That's to simplify lookups
    and calculations.
    """

    __slots__ = (
        'monitor_id', 'monitor_l', 'monitor_t', 'monitor_r', 'monitor_b', 'monitor_w', 'monitor_h',
        'screen_l', 'screen_t', 'screen_r', 'screen_b', 'screen_w', 'screen_h',
        'screen_to_monitor_w', 'screen_to_monitor_h',
        'monitor_to_screen_w', 'monitor_to_screen_h',
        'screen', 'monitor_area', 'monitor_rotation',
    )

    def __init__(
            self,
            monitor_area: defs.MonitorArea,
            destination: defs.ScreenArea,
            rotation: int,
    ) -> None:
        self.screen = destination
        self.monitor_area = monitor_area
        self.monitor_rotation = rotation

        # precompute all these numbers.
        self.monitor_id = monitor_area[defs.MONITOR_AREA_MONITOR_INDEX]
        self.monitor_l: defs.MonitorUnit = cast(defs.MonitorUnit, monitor_area[defs.MONITOR_AREA_X])
        self.monitor_t: defs.MonitorUnit = cast(defs.MonitorUnit, monitor_area[defs.MONITOR_AREA_Y])
        self.monitor_w: defs.MonitorUnit = cast(
            defs.MonitorUnit, monitor_area[defs.MONITOR_AREA_WIDTH],
        )
        self.monitor_h: defs.MonitorUnit = cast(
            defs.MonitorUnit, monitor_area[defs.MONITOR_AREA_HEIGHT],
        )
        self.monitor_r: defs.MonitorUnit = cast(defs.MonitorUnit, self.monitor_l + self.monitor_w)
        self.monitor_b: defs.MonitorUnit = cast(defs.MonitorUnit, self.monitor_t + self.monitor_h)
        self.screen_l: defs.ScreenUnit = destination[defs.SCREEN_AREA_X]
        self.screen_t: defs.ScreenUnit = destination[defs.SCREEN_AREA_Y]
        self.screen_w: defs.ScreenUnit = destination[defs.SCREEN_AREA_WIDTH]
        self.screen_h: defs.ScreenUnit = destination[defs.SCREEN_AREA_HEIGHT]
        self.screen_r: defs.ScreenUnit = cast(defs.ScreenUnit, self.screen_l + self.screen_w)
        self.screen_b: defs.ScreenUnit = cast(defs.ScreenUnit, self.screen_t + self.screen_h)
        self.screen_to_monitor_w = self.monitor_w / self.screen_w
        self.screen_to_monitor_h = self.monitor_h / self.screen_h
        self.monitor_to_screen_w = self.screen_w / self.monitor_w
        self.monitor_to_screen_h = self.screen_h / self.monitor_h

    def screen_to_monitor(
            self, screen_pos: defs.ScreenPosition,
    ) -> Optional[defs.MonitorPosition]:
        """Map the screen position to within this monitor region."""
        src_x = screen_pos[defs.SCREEN_POSITION_X]
        if self.screen_l <= src_x < self.screen_r:
            res_x = ((src_x - self.screen_l) * self.screen_to_monitor_w) + self.monitor_l
            src_y = screen_pos[defs.SCREEN_POSITION_Y]
            if self.screen_t <= src_y < self.screen_b:
                res_y = ((src_y - self.screen_t) * self.screen_to_monitor_h) + self.monitor_t
                return (
                    self.monitor_id,
                    cast(defs.MonitorUnit, int(res_x)), cast(defs.MonitorUnit, int(res_y)),
                )
        return None

    def screen_contains(self, screen_pos: defs.ScreenPosition) -> bool:
        """Does the screen pixels represented by this block include the position?"""
        return (
            self.screen_l <= screen_pos[defs.SCREEN_POSITION_X] < self.screen_r
            and self.screen_t <= screen_pos[defs.SCREEN_POSITION_Y] < self.screen_b
        )

    def monitor_to_screen(
            self, monitor_pos: defs.MonitorPosition,
    ) -> Optional[defs.ScreenPosition]:
        """Map the monitor position to the screen position."""
        if monitor_pos[defs.MONITOR_POSITION_MONITOR_IDENTIFIER] != self.monitor_id:
            return None
        src_x = monitor_pos[defs.MONITOR_POSITION_X]
        if self.monitor_l <= src_x < self.monitor_r:
            res_x = ((src_x - self.monitor_l) * self.monitor_to_screen_w) + self.screen_l
            src_y = monitor_pos[defs.MONITOR_POSITION_Y]
            if self.monitor_t <= src_y < self.monitor_b:
                res_y = ((src_y - self.monitor_t) * self.monitor_to_screen_h) + self.screen_t
                return (
                    cast(defs.ScreenUnit, res_x), cast(defs.ScreenUnit, res_y),
                )
        return None

    def __repr__(self) -> str:
        return (
            f'VirtualScreenBlock(mid: {repr(self.monitor_id)}, '
            f'm: {repr(self.monitor_area)}, '
            f's: {repr(self.screen)}, '
            f'r: {self.monitor_rotation})'
        )

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, VirtualScreenBlock):
            return False
        return (
            # Simplified equality...
            self.screen == other.screen
            and self.monitor_area == other.monitor_area
        )

    def __ne__(self, other: Any) -> bool:
        return not self.__eq__(other)


class VirtualScreen:
    """Maintains a virtual screen space, to allow for mapping from the virtual
    screen area into the monitor space."""

    __slots__ = ('_blocks',)

    def __init__(self, blocks: Sequence[VirtualScreenBlock]) -> None:
        # Could pre-arrange this data to make lookups faster.
        # For now, it's based on the identifier.
        self._blocks = tuple(sorted(blocks, key=lambda b: b.monitor_id))

    @property
    def blocks(self) -> Sequence[VirtualScreenBlock]:
        """Get the blocks of virtual screen space."""
        return self._blocks

    def is_overlapping(self) -> bool:
        """Is this virtual screen overlapping?  If it is, then it's invalid."""

        # This algorithm is O(n^2)

        for index1 in range(len(self._blocks)):
            block1 = self._blocks[index1]
            # Loop over blocks that haven't been compared to yet.
            for index2 in range(index1 + 1, len(self._blocks)):
                block2 = self._blocks[index2]
                if is_overlapping(block1.screen, block2.screen):
                    return True
        return False

    def primary_block(self) -> Optional[VirtualScreenBlock]:
        """Get the primary screen block, which should be considered 'monitor zero'.
        If this is a valid screen, then a block is returned."""
        for block in self._blocks:
            if block.screen_l == 0 and block.screen_t == 0:
                return block
        return None

    def get_block_at(self, screen_pos: defs.ScreenPosition) -> Optional[VirtualScreenBlock]:
        """Find the block that that screen position resides within."""
        for block in self.blocks:
            if block.screen_contains(screen_pos):
                return block
        return None

    def screen_to_monitor(self, screen_pos: defs.ScreenPosition) -> Optional[defs.MonitorPosition]:
        """Map the virtual screen pixel to a monitor position."""
        for block in self.blocks:
            ret = block.screen_to_monitor(screen_pos)
            if ret:
                return ret
        return None

    def monitor_to_screen(self, monitor_pos: defs.MonitorPosition) -> Optional[defs.ScreenPosition]:
        """Map the monitor index + position to the  virtual screen pixel."""
        for block in self.blocks:
            ret = block.monitor_to_screen(monitor_pos)
            if ret:
                return ret
        return None

    def __repr__(self) -> str:
        return f'VirtualScreen({repr(self.blocks)})'

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, VirtualScreen):
            return False
        b_len = len(self._blocks)
        if b_len != len(other.blocks):
            return False

        # Both sets of blocks should already be sorted by the monitor's identifier.
        for index in range(len(self._blocks)):
            bk1 = self._blocks[index]
            bk2 = other.blocks[index]
            if bk1 != bk2:
                return False
        return True

    def __ne__(self, other: Any) -> bool:
        return not self.__eq__(other)


def is_overlapping(screen1: defs.ScreenArea, screen2: defs.ScreenArea) -> bool:
    """Do the two screen areas overlap?"""
    # Algorithm: Two rectangles do not overlap if one of the following conditions is true.
    # 1) One rectangle is above top edge of other rectangle.
    # 2) One rectangle is on left side of left edge of other rectangle.
    r1_x1 = screen1[defs.SCREEN_AREA_X]
    r1_x2 = screen1[defs.SCREEN_AREA_X] + screen1[defs.SCREEN_AREA_WIDTH]
    r2_x1 = screen2[defs.SCREEN_AREA_X]
    r2_x2 = screen2[defs.SCREEN_AREA_X] + screen2[defs.SCREEN_AREA_WIDTH]
    r1_y1 = screen1[defs.SCREEN_AREA_Y]
    r1_y2 = screen1[defs.SCREEN_AREA_Y] + screen1[defs.SCREEN_AREA_HEIGHT]
    r2_y1 = screen2[defs.SCREEN_AREA_Y]
    r2_y2 = screen2[defs.SCREEN_AREA_Y] + screen2[defs.SCREEN_AREA_HEIGHT]

    return (
        # one rectangle is on west side of the other
        not (r1_x1 >= r2_x2 or r2_x1 >= r1_x2)

        # one rectangle is on south side of the other
        and not (r1_y1 >= r2_y2 or r2_y1 >= r1_y2)
    )


def match_monitor_def_to_active(
        monitor_def: defs.MonitorPosition,
        active_monitor: monitor.Monitor,
) -> float:
    """Finds the match value for the active monitor against the monitor definition.
    The higher the number, the better the match."""

    # This is a nice little heuristic developed awhile ago.
    rank = 0.0

    # Monitor identifier match: 2 points
    if monitor_def[defs.MONITOR_POSITION_MONITOR_IDENTIFIER] == active_monitor.identifier:
        rank += 2.0

    # Width & height match: 10 points each, based on ratio of the actual monitor vs. this monitor.
    rank += (
        10.0 * (
            1.0 - (
                abs(monitor_def[defs.MONITOR_POSITION_X] - active_monitor.real_pixel_width)
                / max(monitor_def[defs.MONITOR_POSITION_X], active_monitor.real_pixel_width)
            )
        )
    )
    rank += (
        10.0 * (
            1.0 - (
                abs(monitor_def[defs.MONITOR_POSITION_Y] - active_monitor.real_pixel_height)
                / max(monitor_def[defs.MONITOR_POSITION_Y], active_monitor.real_pixel_height)
            )
        )
    )
    return rank


def match_monitor_defs_to_active_monitors(
        monitor_defs: Sequence[defs.MonitorPosition],
        active_monitors: Sequence[monitor.Monitor],
) -> Tuple[float, List[Tuple[monitor.Monitor, Optional[defs.MonitorPosition]]]]:
    """Construct a match for the input monitor configuration against this configuration's
    monitor definition.  The higher the return value, the better the fit.

    This returns the match value and the best mapping between the active monitor to the
    monitor definition.  If the monitor count is different, then a non-match is returned.
    """

    if len(monitor_defs) != len(active_monitors):
        return -1.0, [
            (m, None)
            for m in active_monitors
        ]

    # This find the best match for each active monitor, removes that match then scans the
    # next item.  It's not 100% accurate, but is a close fit.

    rank = 0.0
    unmatched = set(range(len(monitor_defs)))
    match_list: List[Tuple[monitor.Monitor, Optional[defs.MonitorPosition]]] = []
    for active_monitor in active_monitors:
        matched_monitor: Optional[defs.MonitorPosition] = None
        best_rank = 0.0
        best_index = -1
        for monitor_index in unmatched:
            monitor_rank = match_monitor_def_to_active(
                monitor_defs[monitor_index], active_monitor,
            )
            if monitor_rank > best_rank:
                best_rank = monitor_rank
                best_index = monitor_index
        # Based on the initial assertion (lengths are equal), this if block should always
        # be entered.  However, for extra safety, the if is here.
        if best_index >= 0:  # pragma no cover
            unmatched.remove(best_index)
            rank += best_rank
            matched_monitor = monitor_defs[best_index]
        match_list.append((active_monitor, matched_monitor))
    return rank, match_list


class VirtualScreenConfig:
    """Configuration of a virtual screen to all its monitors.  Used for matching to create
    the virtual screen layout when the monitor state changes."""

    __slots__ = ('monitor_defs', 'screen', 'name', 'is_default')

    def __init__(
            self, name: str, monitors: Sequence[defs.MonitorPosition], screen: VirtualScreen,
    ) -> None:
        # MonitorPosition isn't the best construct, but, meh.
        self.monitor_defs = tuple(monitors)
        self.screen = screen
        self.name = name
        self.is_default = False

    def validate(self) -> StdRet[None]:
        """Is this definition valid?  The monitors must all have at least one screen block,
        and each screen block must be valid."""
        messages: List[UserMessage] = []
        if self.screen.is_overlapping():
            messages.append(UserMessage(
                TRANSLATION_CATALOG,
                _('configuration {name}: screen blocks overlap'),
                name=self.name,
            ))
        monitors_with_blocks: Set[int] = set()
        for block in self.screen.blocks:
            if (
                    block.screen_w < 0 or block.screen_h < 0
                    or block.monitor_w < 0 or block.monitor_h < 0
            ):
                messages.append(UserMessage(
                    TRANSLATION_CATALOG,
                    _('configuration {name} screen block ({x}, {y}): invalid size parameters'),
                    name=self.name,
                    x=block.screen_l, y=block.screen_t,
                ))
            monitors_with_blocks.add(block.monitor_id)
        for monitor_def in self.monitor_defs:
            if monitor_def[defs.MONITOR_POSITION_MONITOR_IDENTIFIER] not in monitors_with_blocks:
                messages.append(UserMessage(
                    TRANSLATION_CATALOG,
                    _('configuration {name}: no screen block for defined monitor {ident}'),
                    name=self.name,
                    ident=monitor_def[defs.MONITOR_POSITION_MONITOR_IDENTIFIER],
                ))
        if messages:
            return StdRet.pass_error(join_errors(*messages))
        return RET_OK_NONE

    def match(
            self, active: Sequence[monitor.Monitor],
    ) -> Tuple[float, List[Tuple[monitor.Monitor, Optional[defs.MonitorPosition]]]]:
        """Construct a match for the input monitor configuration against this configuration's
        monitor definition.  The higher the return value, the better the fit."""
        return match_monitor_defs_to_active_monitors(self.monitor_defs, active)

    @staticmethod
    def create_default(active: Sequence[monitor.Monitor]) -> 'VirtualScreenConfig':
        """Create the default configuration for the given monitor setup."""

        # Just horizontal layout.
        next_x = 0
        monitor_defs: List[defs.MonitorPosition] = []
        blocks: List[VirtualScreenBlock] = []
        for active_monitor in active:
            monitor_def: defs.MonitorPosition = (
                active_monitor.identifier,
                cast(defs.MonitorUnit, active_monitor.real_pixel_width),
                cast(defs.MonitorUnit, active_monitor.real_pixel_height),
            )
            monitor_defs.append(monitor_def)
            blocks.append(VirtualScreenBlock(
                monitor_area=(
                    active_monitor.identifier, defs.ZERO_MONITOR_UNIT, defs.ZERO_MONITOR_UNIT,
                    # mypy really wants this cast again, for some reason.  Probably because
                    # of the "variable" reference to the index.
                    cast(defs.MonitorUnit, monitor_def[defs.MONITOR_SIZE_WIDTH]),
                    cast(defs.MonitorUnit, monitor_def[defs.MONITOR_SIZE_HEIGHT]),
                ),
                destination=(
                    cast(defs.ScreenUnit, next_x), defs.ZERO_SCREEN_UNIT,
                    cast(defs.ScreenUnit, active_monitor.real_pixel_width),
                    cast(defs.ScreenUnit, active_monitor.real_pixel_height),
                ),
                rotation=0,
            ))
            next_x += active_monitor.real_pixel_width

        ret = VirtualScreenConfig(f'default-{len(blocks)}', monitor_defs, VirtualScreen(blocks))
        ret.is_default = True
        return ret


class VirtualScreenSettings:
    """Maintains the state of the virtual screen, which divides the monitors into blocks of
    virtual space relative to each other.

    The primary screen always has the top-left corner coordinates of (0, 0).  Everything else
    is relative to that."""

    __slots__ = ('_monitors', '_active_screen', '_configuration', '_active_config_index')

    def __init__(self) -> None:
        self._monitors: Sequence[monitor.Monitor] = ()
        self._active_screen = VirtualScreen([])
        self._configuration: List[VirtualScreenConfig] = []
        self._active_config_index = -1

    def copy(self) -> 'VirtualScreenSettings':
        """Make a copy of these settings."""
        ret = VirtualScreenSettings()
        ret._monitors = self._monitors  # pylint:disable=protected-access
        ret._active_screen = self._active_screen  # pylint:disable=protected-access
        ret._configuration = list(self._configuration)  # pylint:disable=protected-access
        ret._active_config_index = self._active_config_index  # pylint:disable=protected-access
        return ret

    def set_active_monitors(self, active: Sequence[monitor.Monitor]) -> bool:
        """Sets the active monitor configuration.  Returns True if the active screen setup
        changes.  This may create a new configuration if no match is found."""
        old_config_index = self._active_config_index

        best_config_index = -1
        best_rank = -1.0
        # best_arrangement = List[Tuple[monitor.Monitor, Optional[defs.MonitorPosition]]]
        for index in range(len(self._configuration)):
            rank, _arrangement = self._configuration[index].match(active)
            if rank > best_rank:
                best_config_index = index
                best_rank = rank
                # best_arrangement = _arrangement

        if best_config_index < 0:
            best_config_index = len(self._configuration)
            self._configuration.append(VirtualScreenConfig.create_default(active))
        self._active_config_index = best_config_index
        self._active_screen = self._configuration[best_config_index].screen
        self._monitors = tuple(active)

        return old_config_index != self._active_config_index

    def update_configuration(self, new_config: Sequence[VirtualScreenConfig]) -> bool:
        """Update the existing configuration with the new one.  Returns True if this
        triggers a change in the active screen.  This may create a new configuration
        if no match against the currently active monitors is found.  This does not
        validate the configurations; that must be done before calling this method."""
        old_screen = self._active_screen

        self._configuration = list(new_config)

        # Ignore the return code, because this call is designed around
        # a non-changing config, and so has optimizations.
        self.set_active_monitors(self._monitors)

        return old_screen != self._active_screen

    @property
    def active_screen(self) -> VirtualScreen:
        """The active virtual screen."""
        return self._active_screen

    @property
    def active_monitors(self) -> Sequence[monitor.Monitor]:
        """The active monitors."""
        return self._monitors

    @property
    def all_screen_configurations(self) -> Sequence[VirtualScreenConfig]:
        """The current list of all screen configurations."""
        return tuple(self._configuration)

    @property
    def user_screen_configurations(self) -> Sequence[VirtualScreenConfig]:
        """The non-default screen configurations."""
        ret: List[VirtualScreenConfig] = []
        for config in self._configuration:
            if not config.is_default:
                ret.append(config)
        return tuple(ret)
