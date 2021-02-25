"""
Attempts to add the layer between the Petronia screen coordinates (virtual screen) and the
monitor by including Windows virtual screen pixel positions in the mix.

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

With Windows, there's an added hitch where a window can spread across multiple monitors.  The
Window reports the virtual window space size, but not the monitor size.  This module helps to
map between the window pixel value and the Petronia Screen units.


EXTRA TO DO STUFF:

There needs to be an extra message to listen to, which is the adjustment of the Windows
virtual screen.

At startup and at virtual screen changes, these calls could be made:

    unsigned int nScreenWidth = GetSystemMetrics(SM_CXVIRTUALSCREEN);
    unsigned int nScreenHeight = GetSystemMetrics(SM_CYVIRTUALSCREEN);

The call to WINDOWS_FUNCTIONS.monitors.find_monitors() includes the virtual desktop position.
"""

from typing import List, Sequence, Union, Optional, cast
import threading
from petronia_common.util import ValueHolder
from petronia_native.common import defs, virtual_screen
from .arch.native_funcs.monitor import WindowsMonitor
from .arch.native_funcs.windows_common import (
    HWND, HFONT,
    WindowsErrorMessage,
)
from .arch.native_funcs import (
    WINDOWS_FUNCTIONS,
)


DEFAULT_WINDOW_WIDTH = cast(defs.ScreenUnit, 100)
DEFAULT_WINDOW_HEIGHT = cast(defs.ScreenUnit, 100)
DEFAULT_PADDING = cast(defs.ScreenUnit, 4)


def bootstrap_screens() -> Sequence[WindowsErrorMessage]:
    """
    Initialize the process for the screen settings.

    This attempts to make the window position be low-level monitor pixel aware.  In this
    regard, the os-reported sizes *should* match up with the monitor sizes.
    """
    ret: List[WindowsErrorMessage] = []
    if WINDOWS_FUNCTIONS.monitor.set_native_dpi_awareness:
        err = WINDOWS_FUNCTIONS.monitor.set_native_dpi_awareness()
        if err:
            ret.append(err)
    return ret


class WindowsDesktopScreen:
    """The extra layer injected between Windows' window pixel locations and
    Petronia screen blocks, so it's the OsScreen translation layer.

    Each time the Windows virtual screen changes, this needs to be updated.  This
    can happen due to monitors connected or disconnected, and changing the relative
    position between monitors.

    The Petronia virtual screen block is a mapping between the Petronia screen to the
    underlying monitor.

    This is thread safe.
    """

    __slots__ = ('_petronia_screen', '_windows_monitors', '__lock')

    def __init__(
            self,
            petronia_screen: virtual_screen.VirtualScreen,
            initial_monitors: Sequence[WindowsMonitor],
    ) -> None:
        # Without the lock, very rare and strange bugs will pop up.
        self.__lock = threading.RLock()
        self._petronia_screen = petronia_screen
        self._windows_monitors = tuple(initial_monitors)

    def on_windows_monitors_changed(self, new_monitors: Sequence[WindowsMonitor]) -> None:
        """Called when a change is detected to the monitors or monitor layout in the Windows
        virtual screen."""
        with self.__lock:
            self._windows_monitors = tuple(new_monitors)

    def on_petronia_screen_changed(self, new_screen: virtual_screen.VirtualScreen) -> None:
        """Called when a change is made to the Petronia virtual screen."""
        with self.__lock:
            self._petronia_screen = new_screen

    def position_monitor_to_window(
            self, monitor_pos: defs.MonitorPosition,
    ) -> Optional[defs.OsScreenPosition]:
        """Convert the Petronia monitor position into a Windows' virtual screen position."""
        monitor_id = monitor_pos[defs.MONITOR_POSITION_MONITOR_IDENTIFIER]
        with self.__lock:
            for monitor in self._windows_monitors:
                if monitor.info.identifier == monitor_id:
                    return (
                        monitor_pos[defs.MONITOR_POSITION_X] + monitor.virtual_desktop_area.left,
                        monitor_pos[defs.MONITOR_POSITION_Y] + monitor.virtual_desktop_area.top,
                    )
            return None

    def position_window_to_screen(
            self, window_x: int, window_y: int,
    ) -> Optional[defs.ScreenPosition]:
        """Convert a Window virtual screen position into a Petronia screen position."""
        with self.__lock:
            # First, find the pixel's WindowsMonitor.
            monitor: Optional[WindowsMonitor] = None
            for try_monitor in self._windows_monitors:
                if try_monitor.is_in_virtual_desktop_area(window_x, window_y):
                    monitor = try_monitor
                    break
            if not monitor:
                return None

            # Convert the Window virtual screen pixel to a relative monitor pixel.
            mon_x = cast(defs.MonitorUnit, window_x - monitor.virtual_desktop_area.left)
            mon_y = cast(defs.MonitorUnit, window_y - monitor.virtual_desktop_area.top)

            # Convert this monitor pixel into the screen position.
            return self._petronia_screen.monitor_to_screen(
                (monitor.info.identifier, mon_x, mon_y)
            )

    def position_screen_to_window(
            self, screen_pos: defs.ScreenPosition,
    ) -> Optional[defs.OsScreenPosition]:
        """Convert a Petronia screen position into a Window virtual screen position."""
        with self.__lock:
            # Find the Petronia monitor position.
            mon_pos = self._petronia_screen.screen_to_monitor(screen_pos)
            if not mon_pos:
                return None

            return self.position_monitor_to_window(mon_pos)


class WindowPosition:  # pylint:disable=too-many-instance-attributes
    """Options about where to place the window.

    Huge to-do: this needs to
    """
    __slots__ = (
        'x', 'y', 'width', 'height',
        'left', 'right', 'top', 'bottom',
        'padding',
        'text_size', 'relative',
        'relative', 'virtual_screen',
    )

    def __init__(  # pylint:disable=too-many-arguments
            self,
            v_screen: ValueHolder[virtual_screen.VirtualScreen],
            x: defs.ScreenUnit = defs.ZERO_SCREEN_UNIT,
            y: defs.ScreenUnit = defs.ZERO_SCREEN_UNIT,
            width: defs.ScreenUnit = DEFAULT_WINDOW_WIDTH,
            height: defs.ScreenUnit = DEFAULT_WINDOW_HEIGHT,
            left: Optional[defs.ScreenUnit] = None, right: Optional[defs.ScreenUnit] = None,
            top: Optional[defs.ScreenUnit] = None, bottom: Optional[defs.ScreenUnit] = None,
            padding: defs.ScreenUnit = DEFAULT_PADDING,
            text_size: Optional[Union[int, str]] = None,
            relative: Optional[str] = None,
    ) -> None:
        self.x = x  # pylint:disable=invalid-name
        self.y = y  # pylint:disable=invalid-name
        self.width = width
        self.height = height
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        self.padding = padding
        self.text_size = text_size
        self.relative = relative
        self.virtual_screen = v_screen

    def _adjust_relative_position(
            self,
            pos_x: int,
            pos_y: int,
            width: int,
            height: int,
    ) -> defs.ScreenArea:
        """Adjust the x/y based on the relative positioning of the area.  This takes the
        OS reported units and translates them into screen positions."""

        # Huge to-do: this needs the extra translation of virtual desktop to monitor.

        if self.relative:
            # Adjust based on the relative location.

            # For now, this is based on the x,y position.  It may instead be based on the
            # relative thing.

            screen_block = self.virtual_screen.value.get_block_at((self.x, self.y))
            if screen_block:
                pos_types = self.relative.split('-')

                if 'bottom' in pos_types:
                    pos_y = (
                        # Bottom of the screen block...
                        screen_block.screen_b - height - self.padding
                    )
                elif 'top' in pos_types:
                    pos_y = (
                        # Top of the screen block...
                        screen_block.screen_t + self.padding
                    )

                if 'right' in pos_types:
                    pos_x = (
                        # Right of the screen block...
                        screen_block.screen_r - width - self.padding
                    )
                elif 'left' in pos_types:
                    pos_x = (
                        # Left of the monitor...
                        screen_block.screen_l + self.padding
                    )

                if self.right is not None:
                    width = self.right - pos_x
                if self.bottom is not None:
                    height = self.bottom - pos_y

        return (
            cast(defs.ScreenUnit, pos_x),
            cast(defs.ScreenUnit, pos_y),
            cast(defs.ScreenUnit, width),
            cast(defs.ScreenUnit, height),
        )

    def get_size(self, hwnd: Optional[HWND], hfont: Optional[HFONT] = None) -> defs.ScreenArea:
        """Get the size of the window.  For text-based windows, returns the single-line
        text size of the area."""
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
        ):
            text_size = get_text_size(hwnd, hfont, self.text_size)
            if text_size:
                width = text_size[defs.MONITOR_SIZE_WIDTH]
                height = text_size[defs.MONITOR_SIZE_HEIGHT]

        return self._adjust_relative_position(pos_x, pos_y, width, height)


def get_text_size(
        hwnd: HWND, hfont: HFONT, text_size: Union[int, str],
) -> Optional[defs.ScreenSize]:
    """Get the size of the single-line of text."""
    if not WINDOWS_FUNCTIONS.window.get_text_size:
        return None
    text_sample: str
    if isinstance(text_size, str):
        text_sample = text_size
    else:
        text_sample = 'm' * text_size
    res = WINDOWS_FUNCTIONS.window.get_text_size(hfont, text_sample, hwnd, None)
    if isinstance(res, WindowsErrorMessage):
        return None
    return (
        cast(defs.ScreenUnit, res[defs.OS_SCREEN_SIZE_WIDTH]),
        cast(defs.ScreenUnit, res[defs.OS_SCREEN_SIZE_HEIGHT]),
    )
