
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

from typing import Tuple, Optional
from .....core.platform.api import (
    ScreenArea
)
from ..arch.native_funcs.windows_common import (
    HWND, HFONT,
)
from ..arch.native_funcs import (
    WINDOWS_FUNCTIONS,
)

NativeScreenUnit = int

# x, y
NativeScreenPosition = Tuple[NativeScreenUnit, NativeScreenUnit]
NATIVE_SCREEN_POSITION_X = 0
NATIVE_SCREEN_POSITION_Y = 1

# width, height
NativeScreenSize = Tuple[NativeScreenUnit, NativeScreenUnit]

# x, y, width, height
NativeScreenArea = Tuple[NativeScreenUnit, NativeScreenUnit, NativeScreenUnit, NativeScreenUnit]
NATIVE_SCREEN_AREA_X = 0
NATIVE_SCREEN_AREA_Y = 1
NATIVE_SCREEN_AREA_W = 2
NATIVE_SCREEN_AREA_H = 3


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
            pass

        return pos_x, pos_y, width, height



    """

    if 'relative' in pos:
        relative = pos['relative'].split('-')
        if 'monitor' in pos:
            monitor_index = pos['monitor']
        else:
            monitor_index = 0

        monitors = monitor__find_monitors()
        if monitor_index < 0 or monitor_index >= len(monitors):
            monitor_index = 0

        if 'bottom' in relative:
            pos_y = monitors[monitor_index]['bottom'] - height - padding
        elif 'top' in relative:
            pos_y = monitors[monitor_index]['top'] + padding

        if 'right' in relative:
            pos_x = monitors[monitor_index]['right'] - width - padding
        elif 'left' in relative:
            pos_x = monitors[monitor_index]['left'] + padding

    if 'right' in pos:
        width = pos['right'] - pos_x
    if 'bottom' in pos:
        height = pos['bottom'] - pos_y

    return pos_x, pos_y, width, height
"""
