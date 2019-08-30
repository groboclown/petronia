
"""
Manages finding the monitors, their size, their scale, and virtual <->
physical pixels.

At the moment, we let Windows natively handle the scaling.

    https://docs.microsoft.com/en-us/windows/win32/winauto/uiauto-screenscaling

However, this may cause pixel adjustment issues.  If that's the case, then extra
effort is needed to convert this application to be DPI aware.

https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-setprocessdpiaware

https://stackoverflow.com/questions/42102688/can-i-make-movewindow-use-screen-coordinates-in-windows-10-c

https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getphysicalcursorpos

"""

from typing import Tuple, Sequence, Union, Optional
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
from ..arch.native_funcs import (
    WINDOWS_FUNCTIONS,
)


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
            text_size: Optional[int] = None,
            relative: Optional[str] = None,
            monitor: Optional[int] = 0
    ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        self.padding = padding
        self.text_size = text_size
        self.relative = relative
        self.monitor = monitor

    def get_size(self, hwnd: Optional[HWND], hfont: Optional[HFONT] = None) -> ScreenArea:
        pos_x = self.x
        pos_y = self.y
        width = self.width
        height = self.height

        if self.left is not None:
            pos_x = self.left
        if self.top is not None:
            pos_y = self.top

        if self.text_size is not None and hfont is not None and hwnd is not None:
            width, height = WINDOWS_FUNCTIONS.window.get_text_size(hwnd, hfont, self.text_size)

        if self.relative:
            # Adjust based on the specified monitor and relative location.
            # TODO implement
            pos_types = self.relative.split('-')
            monitors = get_monitors()
            if not isinstance(monitors, WindowsErrorMessage) and monitors:
                if len(monitors) > self.monitor:
                    monitor = monitors[self.monitor]
                else:
                    monitor = monitors[0]

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


def get_monitors() -> Union[Sequence[NativeScreenInfo], WindowsErrorMessage]:
    if WINDOWS_FUNCTIONS.monitor.find_monitors:
        return WINDOWS_FUNCTIONS.monitor.find_monitors()
    return WindowsErrorMessage('not implemented')
