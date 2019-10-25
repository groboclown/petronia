
from typing import Dict, Sequence, Optional
from ...arch.native_funcs import (
    HWND,
    WINDOWS_FUNCTIONS,
)
from ...arch.native_funcs.monitor import WindowsMonitor
from ......aid.std import (
    ComponentId,
    log, WARN, DEBUG, VERBOSE,
)
from ......core.platform.api.defs import (
    ScreenRect,
    NATIVE_SCREEN_AREA_X,
    NATIVE_SCREEN_AREA_Y,
    NATIVE_SCREEN_AREA_W,
    NATIVE_SCREEN_AREA_H,
)
from ......core.platform.api.window import (
    NativeWindowState,
)
from ...connect import (
    WindowsErrorMessage,
    get_monitors,
)
from ...arch.error_codes_common import (
    ERROR_ACCESS_DENIED
)
from .window_style import set_window_style


# FIXME BUG: if there are multiple monitors with different scale factors, then
#   restoring to the non-primary monitors ends up being in the primary monitor
#   scaled size, not the required size.  This is either an issue with the way
#   the window size is stored when first opened, or the way that size is
#   interpreted on restore.

def restore_windows(
        reverse_window_ids: Dict[ComponentId, HWND],
        original_window_state: Dict[int, NativeWindowState]
) -> None:
    # One time logging for missing functions.
    if not WINDOWS_FUNCTIONS.window.set_style:
        log(
            WARN, restore_windows,
            "Cannot actions known windows original style; no function set."
        )
    if not WINDOWS_FUNCTIONS.window.set_position:
        log(
            WARN, restore_windows,
            "Cannot actions known windows original position; no function set."
        )

    current_monitors_with_err = get_monitors()
    current_monitors: Sequence[WindowsMonitor] = []
    if not isinstance(current_monitors_with_err, WindowsErrorMessage):
        # Don't try to adjust for monitors.
        current_monitors = current_monitors_with_err

    # Create a copy of the list; without it, the original state can change underneath us
    # in certain conditions, which leads to an error.
    for original in tuple(original_window_state.values()):
        cid = original.component_id
        if cid not in reverse_window_ids:
            log(
                WARN, restore_windows,
                "Know about window {0}, but it has no registered HWND",
                cid
            )
            continue
        hwnd = reverse_window_ids[cid]
        if WINDOWS_FUNCTIONS.window.set_style:
            set_window_style(hwnd, original.style)
        if WINDOWS_FUNCTIONS.window.set_position:
            pos = best_restore_state(original, current_monitors)
            if pos:
                res_p = WINDOWS_FUNCTIONS.window.set_position(
                    hwnd, hwnd, pos.x, pos.y, pos.width, pos.height,
                    ["frame-changed", "no-zorder", "async-window-pos"]
                )
                if isinstance(res_p, WindowsErrorMessage):
                    # Access denied happens when the window is a message window.
                    if res_p.errno != ERROR_ACCESS_DENIED:
                        log(
                            WARN, restore_windows,
                            "Could not actions the position and size of {0}: {1}",
                            hwnd, res_p
                        )
                    else:
                        log(
                            DEBUG, restore_windows,
                            "access denied when resorting pos on {0}",
                            original
                        )
                else:
                    log(VERBOSE, restore_windows, "Restore {0} -> {1}", hwnd, pos)
    # May also want to actions focus state to how it was right before this function ran.


def best_restore_state(
        original: NativeWindowState,
        current_monitors: Sequence[WindowsMonitor]
) -> Optional[ScreenRect]:
    # If the original screens was remounted when Petronia was shut down, then
    # we need to take special care we don't move the windows way outside the
    # acceptable area.

    pos = original.bordered_rect
    if pos.width <= 0 and pos.height <= 0:
        return None

    if not current_monitors:
        return pos

    # Check if the new screens can accommodate the window.
    for monitor in current_monitors:
        screen = monitor.info
        px1 = screen.screen_size[NATIVE_SCREEN_AREA_X]
        px2 = px1 + screen.screen_size[NATIVE_SCREEN_AREA_W]
        py1 = screen.screen_size[NATIVE_SCREEN_AREA_Y]
        py2 = py1 + screen.screen_size[NATIVE_SCREEN_AREA_H]

        if pos.left >= px1 and pos.right <= px2 and pos.top >= py1 and pos.bottom <= py2:
            return pos

    # Find the best match original window size to the current screens,
    # then resize the window to fit in the screen.  The size of the
    # window should be maintained as much as possible.

    best_match_size: Optional[ScreenRect] = None
    best_match_original = -1
    for monitor in current_monitors:
        screen = monitor.info
        px1 = screen.screen_size[NATIVE_SCREEN_AREA_X]
        px2 = px1 + screen.screen_size[NATIVE_SCREEN_AREA_W]
        py1 = screen.screen_size[NATIVE_SCREEN_AREA_Y]
        py2 = py1 + screen.screen_size[NATIVE_SCREEN_AREA_H]

        if pos.left >= px1 and pos.right <= px2 and pos.top >= py1 and pos.bottom <= py2:
            return pos

        dx1 = min(abs(pos.left - px1), abs(pos.left - px2))
        dx2 = min(abs(pos.right - px1), abs(pos.right - px2))
        dy1 = min(abs(pos.top - py1), abs(pos.top - py2))
        dy2 = min(abs(pos.bottom - py1), abs(pos.bottom - py2))
        m = (dx1 + dx2) * (dy1 + dy2)
        if best_match_original < 0 or best_match_original > m:
            best_match_original = m
            nx = pos.x
            ny = pos.y
            nw = pos.width
            nh = pos.height
            if px1 > pos.left:
                nx = px1
            if py1 > pos.top:
                ny = py1
            if px2 < pos.right:
                nx = px2 - nw
                if nx < px1:
                    # too wide for the screen
                    nx = px1
                    nw = screen.screen_size[NATIVE_SCREEN_AREA_W]
            if py2 < pos.bottom:
                ny = py2 - nh
                if ny < py1:
                    # too tall for the screen
                    ny = py1
                    nh = screen.screen_size[NATIVE_SCREEN_AREA_H]
            best_match_size = ScreenRect(nx, ny, nw, nh, nx, nx + nw - 1, ny, ny + nh - 1)

    return best_match_size
