
"""
Works with the `windows_hook_event` to create Python-friendly wrappers around
Windows-specific WM_* message handlers.

Every function takes the form:
    def blah_message(callback: Callable[whatever is needed]) -> Tuple(message_id, MessageCallback)

These are used for creating the dictionary that is passed to
shell__create_global_message_handler.

Callbacks should prefer standard Python types over ctypes (`int` vs UINT),
but Windows native structures (HWND, RECT) are okay, as long as they have
appropriate conversion routines.  That's for performance reasons (we don't want
to unnecessarily convert them).

See:

https://msdn.microsoft.com/en-us/library/windows/desktop/ms644991(v=vs.85).aspx
https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-registershellhookwindow
"""

from typing import Tuple, Callable, Optional
from typing import cast as t_cast
from ctypes import cast as c_cast
from ctypes import (
    POINTER,
)
from .arch.native_funcs.windows_common import (
    MessageCallback,
    Structure,
    LPARAM, WPARAM,
    HWND,
    RECT,
)
from .arch import windows_constants
from .arch.native_funcs import WINDOWS_FUNCTIONS
from .arch.native_funcs.windows_common import WindowsErrorMessage

MessageEntry = Tuple[bool, int, MessageCallback]


def display_changed_message(callback: Callable[[], None]) -> MessageEntry:
    """Listens to display parameter change messages.

    The way this API is used means it's called for any system settings change.

    You can design your application to determine the display configuration when the user starts
    it, and to detect changes after startup. You should also design the application to recheck
    the display configuration when the computer resumes from sleep."""
    def handler(_source_hwnd: HWND, _message: int, _wparam: WPARAM, _lparam: LPARAM) -> bool:
        callback()
        return True
    # Needs to hook with WM_SETTINGCHANGE with wParam == SPI_SETWORKAREA
    return False, windows_constants.WM_DISPLAYCHANGE, handler


def system_settings_changed_message(callback: Callable[[WPARAM], None]) -> MessageEntry:
    """Listens to system settings changes.

    These can happen from all different kinds of sources, but should happen
    when system properties change, which can include the display work area changing.

    See https://docs.microsoft.com/en-us/windows/win32/winmsg/wm-settingchange
    """
    def handler(_source_hwnd: HWND, _message: int, wparam: WPARAM, _lparam: LPARAM) -> bool:
        callback(wparam)
        return True
    return False, windows_constants.WM_SETTINGCHANGE, handler


def device_changed_message(callback: Callable[[WPARAM], None]) -> MessageEntry:
    """Listens to device changes, such as hot swappable devices.  This can
    include attaching a new monitor or connecting a laptop to a docking station.

    See https://docs.microsoft.com/en-us/windows/win32/devio/wm-devicechange
    """
    def handler(_source_hwnd: HWND, _message: int, wparam: WPARAM, _lparam: LPARAM) -> bool:
        callback(wparam)
        return True
    return False, windows_constants.WM_DEVICECHANGE, handler


def window_minimized_message(callback: Callable[[HWND, RECT], None]) -> MessageEntry:
    """Listens for windows being minimized."""

    def handler(_source_hwnd: HWND, _message: int, _wparam: WPARAM, lparam: LPARAM) -> bool:
        info = c_cast(lparam, POINTER(SHELLHOOKINFO))  # type: ignore
        target_hwnd: HWND = info.contents.hwnd
        window_rect: RECT = info.contents.rc
        callback(target_hwnd, window_rect)  # type: ignore
        return True

    return True, windows_constants.HSHELL_GETMINRECT, handler


def window_created_message(callback: Callable[[HWND], None]) -> MessageEntry:
    """Listens for window creation messages"""
    return True, windows_constants.HSHELL_WINDOWCREATED, _window_handle_callback(callback)


def window_destroyed_message(callback: Callable[[HWND], None]) -> MessageEntry:
    """Listens for top-level window destroyed messages"""
    return True, windows_constants.HSHELL_WINDOWDESTROYED, _window_handle_callback(callback)


def shell_window_focused_message(callback: Callable[[HWND], Optional[bool]]) -> MessageEntry:
    """Listens for the shell window gaining focus."""
    return True, windows_constants.HSHELL_ACTIVATESHELLWINDOW, _window_handle_callback(callback)


def window_activated_message(callback: Callable[[HWND], Optional[bool]]) -> MessageEntry:
    """Listens for the window focus message."""
    return True, windows_constants.HSHELL_WINDOWACTIVATED, _window_handle_callback(callback)


def window_rude_activated_message(callback: Callable[[HWND], Optional[bool]]) -> MessageEntry:
    """Listens for the window focus message, sent in a rude way."""
    return True, windows_constants.HSHELL_RUDEAPPACTIVATED, _window_handle_callback(callback)


def redraw_message(callback: Callable[[HWND], None]) -> MessageEntry:
    """Listens for the window handle that needs to be redrawn."""
    return True, windows_constants.HSHELL_REDRAW, _window_handle_callback(callback)


def forced_exit_message(callback: Callable[[HWND], Optional[bool]]) -> MessageEntry:
    """Listens for a window that should be forced to exit."""
    return True, windows_constants.HSHELL_ENDTASK, _window_handle_callback(callback)


def window_monitor_changed_message(callback: Callable[[HWND], None]) -> MessageEntry:
    """Listens for a window that moved to a different monitor.  This can mean a
    rescale is necessary."""
    return True, windows_constants.HSHELL_MONITORCHANGED, _window_handle_callback(callback)


def window_flash_message(callback: Callable[[HWND], None]) -> MessageEntry:
    """Listens for the window flashing, meaning it wants user attention."""
    return True, windows_constants.HSHELL_FLASH, _window_handle_callback(callback)


# These two occur when a window comes back from being hung
def window_replacing_message(callback: Callable[[HWND, HWND], None]) -> MessageEntry:
    """Listens for when a window is hung, and needs to be recreated.
    The first HWND will be set to the HWND of the new window handle, and
    the second is the HWND of the replaced window.

    The callback should be reused with window_replaced_message."""
    def handler(_source_hwnd: HWND, _message: int, _wparam: WPARAM, lparam: LPARAM) -> bool:
        # LPARAM stores a handle to the window replacing the top-level window.
        top = _source_hwnd
        if WINDOWS_FUNCTIONS.window.get_owning_window:
            handle = WINDOWS_FUNCTIONS.window.get_owning_window(_source_hwnd)
            if isinstance(handle, WindowsErrorMessage):
                # TODO do something smart.
                top = _source_hwnd
            else:
                top = handle
        callback(t_cast(HWND, lparam), top)
        return True
    return True, windows_constants.HSHELL_WINDOWREPLACING, handler


def window_replaced_message(callback: Callable[[HWND, HWND], None]) -> MessageEntry:
    """Listens for when a window is hung, and needs to be recreated.
    The first HWND will be set to the HWND of the new window handle, and
    the second is the HWND of the replaced window.

    The callback should be reused with window_replacing_message."""
    def handler(_source_hwnd: HWND, _message: int, _wparam: WPARAM, lparam: LPARAM) -> bool:
        # LPARAM stores a handle to the window being replaced.
        callback(t_cast(HWND, lparam), _source_hwnd)
        return True
    return True, windows_constants.HSHELL_WINDOWREPLACED, handler


# def app_command_message(callback: Callable[[HWND], None]) -> MessageEntry:
#     pass
# HSHELL_APPCOMMAND = 12  # -> The APPCOMMAND which has been unhandled by the application
# or other hooks. See WM_APPCOMMAND and use the GET_APPCOMMAND_LPARAM macro to
# retrieve this parameter.


def system_power_state_changed(callback: Callable[[bool], None]) -> MessageEntry:
    """Notifies the callback when the power state changes.  Callback argument is True
    if going into suspend mode, and False if resuming from a suspend state."""
    def handler(_source_hwnd: HWND, _message: int, wparam: WPARAM, _lparam: LPARAM) -> bool:
        if wparam == windows_constants.PBT_APMRESUMESUSPEND:
            callback(False)
        elif wparam == windows_constants.PBT_APMSUSPEND:
            callback(True)
        # The other events don't affect Petronia.
        return True
    return True, windows_constants.WM_POWERBROADCAST, handler


# ---------------------------------------------------------------------------


def taskman_message(callback: Callable[[HWND, WPARAM], None]) -> MessageEntry:
    """Listens for.... something.  Don't know what."""
    def handler(_source_hwnd: HWND, _message: int, wparam: WPARAM, lparam: LPARAM) -> bool:
        callback(t_cast(HWND, lparam), wparam)
        return True

    return True, windows_constants.HSHELL_TASKMAN, handler


# FIXME need to figure out how to implement these.
# HSHELL_LANGUAGE = 8  # -> ???
# HSHELL_SYSMENU = 9  # -> ???
# HSHELL_ACCESSIBILITYSTATE = 11  # -> ???
# We get shell message "0x35" and "0x36".  Don't know what these are.
# HSHELL_UNKNOWN_35 = 0x35
# HSHELL_UNKNOWN_36 = 0x36


# ---------------------------------------------------------------------------

def _window_handle_callback(callback: Callable[[HWND], Optional[bool]]) -> MessageCallback:
    def handler(_source_hwnd: HWND, _message: int, _wparam: WPARAM, lparam: LPARAM) -> bool:
        # LPARAM stores the HWND of the window.
        ret = callback(t_cast(HWND, lparam))
        if ret is None:
            # Default: yes, we handled it.
            return True
        return ret
    return handler


class SHELLHOOKINFO(Structure):
    """The SHELLHOOKINFO structure."""
    _fields_ = [
        ("hwnd", HWND),
        ("rc", RECT),  # type: ignore
    ]
