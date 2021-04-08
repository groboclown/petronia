
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
from ..arch.native_funcs.windows_common import (
    MessageCallback,
    Structure,
    LPARAM, WPARAM,
    HWND,
    RECT,
)
from ..arch import windows_constants
from ..arch.native_funcs import WINDOWS_FUNCTIONS
from ..arch.native_funcs.windows_common import WindowsErrorMessage

MessageEntry = Tuple[bool, int, MessageCallback]


def display_changed_message(callback: Callable[[], None]) -> MessageEntry:
    """Listens to display parameter change messages."""
    def handler(_source_hwnd: HWND, _message: int, _wparam: WPARAM, _lparam: LPARAM) -> bool:
        # TODO can we tease out information from the parameters?
        callback()
        return True
    return False, windows_constants.WM_DISPLAYCHANGE, handler,


def window_minimized_message(callback: Callable[[HWND, RECT], None]) -> MessageEntry:
    """Listens for windows being minimized."""

    class SHELLHOOKINFO(Structure):
        _fields_ = [
            ("hwnd", HWND),
            # FIXME What the heck is going on here?  mypy thinks RECT is Any
            ("rc", RECT),  # type: ignore
        ]

    def handler(_source_hwnd: HWND, _message: int, _wparam: WPARAM, lparam: LPARAM) -> bool:
        info = c_cast(lparam, POINTER(SHELLHOOKINFO))  # type: ignore
        target_hwnd: HWND = info.contents.hwnd
        window_rect: RECT = info.contents.rc
        callback(target_hwnd, window_rect)  # type: ignore
        return True

    return True, windows_constants.HSHELL_GETMINRECT, handler,


def window_created_message(callback: Callable[[HWND], None]) -> MessageEntry:
    """Listens for window creation messages"""
    return True, windows_constants.HSHELL_WINDOWCREATED, _window_handle_callback(callback),


def window_destroyed_message(callback: Callable[[HWND], None]) -> MessageEntry:
    """Listens for top-level window destroyed messages"""
    return True, windows_constants.HSHELL_WINDOWDESTROYED, _window_handle_callback(callback),


def shell_window_focused_message(callback: Callable[[HWND], Optional[bool]]) -> MessageEntry:
    """Listens for the shell window gaining focus."""
    return True, windows_constants.HSHELL_ACTIVATESHELLWINDOW, _window_handle_callback(callback),


def window_activated_message(callback: Callable[[HWND], Optional[bool]]) -> MessageEntry:
    """Listens for the window focus message."""
    return True, windows_constants.HSHELL_WINDOWACTIVATED, _window_handle_callback(callback),


def window_rude_activated_message(callback: Callable[[HWND], Optional[bool]]) -> MessageEntry:
    """Listens for the window focus message, sent in a rude way."""
    return True, windows_constants.HSHELL_RUDEAPPACTIVATED, _window_handle_callback(callback),


def redraw_message(callback: Callable[[HWND], None]) -> MessageEntry:
    """Listens for the window handle that needs to be redrawn."""
    return True, windows_constants.HSHELL_REDRAW, _window_handle_callback(callback),


def forced_exit_message(callback: Callable[[HWND], Optional[bool]]) -> MessageEntry:
    """Listens for a window that should be forced to exit."""
    return True, windows_constants.HSHELL_ENDTASK, _window_handle_callback(callback),


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
            t = WINDOWS_FUNCTIONS.window.get_owning_window(_source_hwnd)
            if isinstance(t, WindowsErrorMessage):
                # TODO do something smart.
                top = _source_hwnd
            else:
                top = t
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
# or other hooks. See WM_APPCOMMAND and use the GET_APPCOMMAND_LPARAM macro to retrieve this parameter.


# ---------------------------------------------------------------------------


def taskman_message(callback: Callable[[HWND], None]) -> MessageEntry:
    """Listens for.... something.  Don't know what."""
    return True, windows_constants.HSHELL_TASKMAN, _window_handle_callback(callback),


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
