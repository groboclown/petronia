
"""
Manages finding the monitors, their size, their scale, and virtual <->
physical pixels.

This has issues with screen scaling:

    https://docs.microsoft.com/en-us/windows/win32/winauto/uiauto-screenscaling

Specifically, with multi-DPI setups.  If the system has multiple monitors, each with
a different scaling, then the default Python application will have potential
issues around the placement of windows on different screens.  The most common issue
seen is that the program is system DPI aware, meaning that the main monitor's DPI is
used for everything, which restores the windows on other screens to the wrong size.

https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-setprocessdpiaware

https://stackoverflow.com/questions/42102688/can-i-make-movewindow-use-screen-coordinates-in-windows-10-c

https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getphysicalcursorpos

"""

from typing import List, Tuple, Sequence, Union, Optional
from .....core.platform.api import (
    ScreenArea,
    NativeScreenInfo,
    NATIVE_SCREEN_AREA_X,
    NATIVE_SCREEN_AREA_Y,
    NATIVE_SCREEN_AREA_WIDTH,
    NATIVE_SCREEN_AREA_HEIGHT,
)
from ..arch.native_funcs.windows_common import (
    HWND, HFONT,
    WindowsErrorMessage,
)
from ..arch.native_funcs.monitor import WindowsMonitor
from ..arch.native_funcs import (
    WINDOWS_FUNCTIONS,
)


def bootstrap_screens() -> Sequence[WindowsErrorMessage]:
    """
    Initialize the process for the screen settings
    """
    ret: List[WindowsErrorMessage] = []
    if WINDOWS_FUNCTIONS.monitor.set_native_dpi_awareness:
        err = WINDOWS_FUNCTIONS.monitor.set_native_dpi_awareness()
        if err:
            ret.append(err)
    return ret


class WindowPosition:
    """Options about where to place the window."""
    __slots__ = (
        'x', 'y', 'width', 'height',
        'left', 'top',
        'padding',
        'text_size', 'relative', 'right', 'bottom',
        'relative', 'monitor',
    )

    def __init__(
            self,
            x: Optional[int] = 0, y: Optional[int] = 0,
            width: Optional[int] = 100, height: Optional[int] = 100,
            left: Optional[int] = None, right: Optional[int] = None,
            top: Optional[int] = None, bottom: Optional[int] = None,
            padding: Optional[int] = 4,
            text_size: Optional[Union[int, str]] = None,
            relative: Optional[str] = None,
            monitor: Optional[int] = 0
    ):
        self.x = x or 0
        self.y = y or 0
        self.width = 100 if width is None else width
        self.height = 100 if height is None else height
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        self.padding = padding or 4
        self.text_size = text_size
        self.relative = relative
        self.monitor = monitor or 0

    def get_size(self, hwnd: Optional[HWND], hfont: Optional[HFONT] = None) -> ScreenArea:
        pos_x = self.x
        pos_y = self.y
        width = self.width
        height = self.height

        if self.left is not None:
            pos_x = self.left
        if self.top is not None:
            pos_y = self.top

        if (
                self.text_size is not None and
                hfont is not None and
                hwnd is not None
                and WINDOWS_FUNCTIONS.window.get_text_size
        ):
            text_size: str
            if isinstance(self.text_size, int):
                text_size = 'm' * self.text_size
            else:
                text_size = self.text_size
            res = WINDOWS_FUNCTIONS.window.get_text_size(hfont, text_size, hwnd, None)
            if not isinstance(res, WindowsErrorMessage):
                width, height = res

        if self.relative:
            # Adjust based on the specified monitor and relative location.
            # TODO implement
            pos_types = self.relative.split('-')
            monitors = get_monitors()
            if not isinstance(monitors, WindowsErrorMessage) and monitors:
                if len(monitors) > self.monitor:
                    monitor = monitors[self.monitor].info
                else:
                    monitor = monitors[0].info

                if 'bottom' in pos_types:
                    pos_y = (
                        # Bottom of the monitor...
                        # Note that, due to multi-monitor display properties, the Y can be non-zero.
                        (monitor.work_area[NATIVE_SCREEN_AREA_Y] + monitor.work_area[NATIVE_SCREEN_AREA_HEIGHT])
                        - height - self.padding
                    )
                elif 'top' in pos_types:
                    pos_y = (
                        # Top of the monitor...
                        monitor.work_area[NATIVE_SCREEN_AREA_Y] + self.padding
                    )

                if 'right' in pos_types:
                    pos_x = (
                        # Right of the monitor...
                        (monitor.work_area[NATIVE_SCREEN_AREA_X] + monitor.work_area[NATIVE_SCREEN_AREA_WIDTH])
                        - width - self.padding
                    )
                elif 'left' in pos_types:
                    pos_x = (
                        # Left of the monitor...
                        monitor.work_area[NATIVE_SCREEN_AREA_X] + self.padding
                    )

            if self.right is not None:
                width = self.right - pos_x
            if self.bottom is not None:
                height = self.bottom - pos_y

        return pos_x, pos_y, width, height


def get_monitors() -> Union[Sequence[WindowsMonitor], WindowsErrorMessage]:
    if WINDOWS_FUNCTIONS.monitor.find_monitors:
        return WINDOWS_FUNCTIONS.monitor.find_monitors()
    return WindowsErrorMessage('not implemented')


def from_user_to_native_screen(
        x: int, y: int, monitors: Optional[Sequence[NativeScreenInfo]] = None
) -> Tuple[int, int]:
    # If we performed screen scaling, do it here...
    return x, y,
