"""Match up configuration settings with data."""

from typing import Sequence, List, Tuple, Iterable, Optional
import re
import fnmatch
from . import permutations
from .state import screen as screen_state
from .state import petronia_portal as portal_state
from .events import window as window_event


def get_screen_workspace(
        config_workspaces: Sequence[portal_state.WorkspaceSetup],
        blocks: Sequence[screen_state.VirtualScreenBlock],
) -> Sequence[Tuple[
    screen_state.VirtualScreenBlock,
    portal_state.LayoutSplit,
]]:
    """Map the blocks to the layout splits."""

    best_match = 0.1
    # Default layout.
    ret: Sequence[Tuple[screen_state.VirtualScreenBlock, portal_state.LayoutSplit]] = [
        (
            block,
            portal_state.LayoutSplit(1, 'horizontal', [portal_state.SplitContent(
                'portal',
                portal_state.Portal(
                    1, portal_state.WindowPortalFit(
                        'left', 'top', 'fit', 'fit',
                    ), 0, 0, 0, 0, ['default'],
                ),
            )]),
        )
        for block in blocks
    ]

    for workspace in config_workspaces:
        res = get_workspace_match(blocks, workspace.screens)
        if res is not None:
            if res[0] > best_match:
                ret = res[1]

    return ret


def match_screen_config_to_block(
        config_block: portal_state.ScreenBlock,
        screen_block: screen_state.VirtualScreenBlock,
) -> float:
    """Finds the match value for the active monitor against the monitor definition.
    The higher the number, the better the match."""

    rank = 0.0

    # Width & height match: 10 points each, based on ratio of the actual monitor vs. this monitor.
    # Include a "1" as max value, to prevent divide-by-zero.
    rank += (
        10.0 * (
            1.0 - (
                abs(config_block.width - screen_block.width)
                / max(config_block.width, screen_block.width, 1)
            )
        )
    )
    rank += (
        10.0 * (
            1.0 - (
                abs(config_block.height - screen_block.height)
                / max(config_block.height, screen_block.height, 1)
            )
        )
    )

    # X & Y position: 3 points each, based on the ratio of the two.
    # The closer the numbers, the better the match.
    rank += 3.0 * ratio(config_block.x, screen_block.nw_x_pixel)
    rank += 3.0 * ratio(config_block.y, screen_block.nw_y_pixel)
    return rank


def ratio(val1: float, val2: float) -> float:
    """Get the ratio between the two numbers."""
    val1 = abs(val1)
    val2 = abs(val2)
    if val1 == val2:
        return 1.0
    if val1 < 0.0001 or val2 < 0.0001:
        val1 += 1.0
        val2 += 1.0
    return min(val1, val2) / max(val1, val2)


def get_workspace_match(
        screen_blocks: Sequence[screen_state.VirtualScreenBlock],
        config_matchers: List[portal_state.ScreenMatcher],
) -> Optional[Tuple[float, Sequence[Tuple[
    screen_state.VirtualScreenBlock,
    portal_state.LayoutSplit,
]]]]:
    """Construct a match for the virtual screen layout against the configuration matcher's
    screen definitions.  The higher the rank value, the better the fit.
    """
    if len(screen_blocks) != len(config_matchers):
        # Screen count must match block count
        return None

    block_count = len(screen_blocks)

    best_rank = 0.0
    best_match: List[Tuple[screen_state.VirtualScreenBlock, portal_state.LayoutSplit]] = [
        # populated with the default list
        (b, portal_state.LayoutSplit(1, 'horizontal', [portal_state.SplitContent(
            'portal', portal_state.Portal(1, portal_state.WindowPortalFit(
                'left', 'top', 'fit', 'fit',
            ), 0, 0, 0, 0, ['default']),
        )]))
        for b in screen_blocks
    ]

    for config_match_permutations in permutations.permutations(block_count):
        # Match up the 0 - n screen block with the permutations[index] config.
        rank = 0.0
        match: List[Tuple[screen_state.VirtualScreenBlock, portal_state.LayoutSplit]] = []

        for i in range(block_count):
            rank += match_screen_config_to_block(
                config_matchers[config_match_permutations[i]].block,
                screen_blocks[i],
            )
            match.append(
                (screen_blocks[i], config_matchers[config_match_permutations[i]].layout)
            )
        if rank > best_rank:
            best_rank = rank
            best_match = match

    return best_rank, best_match


def is_window_match(  # pylint:disable=too-many-return-statements,too-many-branches
        window: window_event.WindowState, matcher: portal_state.WindowMatch,
) -> bool:
    """Is the window matched by the matcher?"""

    # All of the matchers must match up.
    meta_values = {
        m.key: m.value
        for m in window.meta
    }
    for match in matcher.match:
        val = meta_values.get(match.key)

        # 'glob','not-exists','exact','regex','exists'
        if match.match_type == 'exists':
            if match is None:
                return False

        elif match.match_type == 'not-exists':
            if match is not None:
                return False

        elif match.match_type == 'glob':
            if not val:
                return False
            try:
                regex = re.compile(fnmatch.translate(match.value))
                if regex.match(val) is None:
                    return False
            except re.error:
                # Ignore?  Should report this as a config issue.
                return False

        elif match.match_type == 'regex':
            if not val:
                return False
            try:
                regex = re.compile(match.value)
                if regex.match(val) is None:
                    return False
            except re.error:
                # Ignore?  Should report this as a config issue.
                return False

        elif match.match_type == 'exact':
            if match.value != val:
                return False

    # Matches all pass
    return True


def get_portal_matchers(
        portal: portal_state.Portal,
        matchers: Sequence[portal_state.WindowMatch],
) -> Iterable[portal_state.WindowMatch]:
    """Get the matchers for the portal."""
    for matcher in matchers:
        if matcher.initial_portal in portal.portal_aliases:
            yield matcher
