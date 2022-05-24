
"""
Windows functions for any architecture or supported version.
"""

# Many places use Windows naming convention for things, not Python.
# pylint:disable=invalid-name,too-many-lines

from typing import Dict, Sequence, List, Iterable, Callable, Optional, Tuple, Type, Union
from typing import cast as t_cast
import atexit
import traceback
from ctypes import sizeof as c_sizeof
from ctypes import cast as c_cast
from ctypes import Union as c_Union
from ctypes import (
    CFUNCTYPE,
    POINTER,
    byref,
    c_int,
    c_uint,
    c_short,
    c_void_p,
    c_long,
    c_ulong,
    c_bool,
    create_unicode_buffer,
    Structure,
    GetLastError,
)
from petronia_common.util import T, STRING_EMPTY_TUPLE, EMPTY_TUPLE, StdRet, RET_OK_NONE
from petronia_native.common import log
from petronia_native.common.defs import (
    OsScreenRect,
    ScreenUnit,
    Color,
)
from petronia_native.common.defs.color import (
    color_to_rgba, COLOR_RGBA_ALPHA_INDEX, COLOR_RGBA_RED_INDEX, COLOR_RGBA_GREEN_INDEX,
    COLOR_RGBA_BLUE_INDEX,
)
from petronia_native.common.defs.units import OsScreenSize
from .windows_common import (
    WINFUNCTYPE, ANIMATIONINFO,
    windll, WindowsReturnError,
    LPCWSTR, LPVOID, LPRECT,
    DWORD, WORD, BOOL, BYTE, UINT, WCHAR, SHORT, LONG, LRESULT, WINTYPE_SIZE,
    COLORREF, RECT, POINT, RGB, HFONT, HDC,
    HWND, HMENU, HMODULE, HINSTANCE, HANDLE, HMONITOR,
    MSG, WPARAM, LPARAM, HHOOK, GUITHREADINFO,
    MessageCallback, NativeMessageCallback,
)
from .supported_functions import (
    Functions,
    PaintCallback,
)
from .color import color_to_native_rgb
from .window_state import (
    WindowsWindowState,
    create_windows_window_state,
    convert_rect,
)
from .monitor import WindowsMonitor
from ..windows_constants import (
    PETRONIA_CREATED_WINDOW__CLASS_PREFIX,
    MAX_CLASS_NAME_LENGTH,
    MAX_FILENAME_LENGTH,
    RDW_INTERNALPAINT, RDW_ERASE, RDW_ALLCHILDREN, RDW_FRAME, RDW_INVALIDATE,
    SW_MINIMIZE, SW_RESTORE, SW_SHOW, SW_HIDE, SW_MAXIMIZE, SW_SHOWNA,
    SW_SHOWNORMAL, SW_SHOWMINIMIZED, SW_SHOWMAXIMIZED, SW_SHOWNOACTIVATE, SW_SHOWMINNOACTIVE,
    HWND_TOPMOST, HWND_NOTOPMOST, HWND_DESKTOP, GW_OWNER,
    SWP_NOSIZE, SWP_NOMOVE,
    PROCESS_QUERY_INFORMATION, PROCESS_VM_READ,
    WM_CLOSE, WM_DESTROY, WH_SHELL, WM_SETTINGCHANGE,
    PS_SOLID, PS_GEOMETRIC, BS_NULL, HS_DIAGCROSS, OPAQUE, TRANSPARENT,
    DT_LEFT, DT_TOP, DT_NOPREFIX,
    LWA_ALPHA, COLOR_WINDOW,
    KEYEVENTF_KEYUP, INPUT_KEYBOARD,
    FW_NORMAL, FW_BOLD, DEFAULT_CHARSET, OUT_TT_PRECIS, CLIP_DEFAULT_PRECIS, PROOF_QUALITY,
    FF_DONTCARE,
    LOGPIXELSY, MONITORINFOF_PRIMARY,
    IDI_APPLICATION, IDC_ARROW, CW_USEDEFAULT,
    WS_OVERLAPPEDWINDOW, STILL_ACTIVE,
    LLHKF_UP, LLKHF_INJECTED, WH_KEYBOARD_LL,
    ERROR_INVALID_PARAMETER,
    HWND_ZORDER_MAP, SWP_FLAG_MAP, WS_EX_STYLE_BIT_MAP, WS_STYLE_BIT_MAP,
    SPI_GETFOCUSBORDERHEIGHT, SPI_SETFOCUSBORDERHEIGHT,
    SPI_GETFOCUSBORDERWIDTH, SPI_SETFOCUSBORDERWIDTH,
    SPI_GETMENUDROPALIGNMENT, SPI_SETMENUDROPALIGNMENT,
    SPI_GETMENUFADE, SPI_SETMENUFADE,
    SPI_GETMENUSHOWDELAY, SPI_SETMENUSHOWDELAY,
    SPI_GETCOMBOBOXANIMATION, SPI_SETCOMBOBOXANIMATION,
    SPI_GETCURSORSHADOW, SPI_SETCURSORSHADOW,
    SPI_GETGRADIENTCAPTIONS, SPI_SETGRADIENTCAPTIONS,
    SPI_GETHOTTRACKING, SPI_SETHOTTRACKING,
    SPI_GETLISTBOXSMOOTHSCROLLING, SPI_SETLISTBOXSMOOTHSCROLLING,
    SPI_GETMENUANIMATION, SPI_SETMENUANIMATION,
    SPI_GETMENUUNDERLINES, SPI_SETMENUUNDERLINES,
    SPI_GETSELECTIONFADE, SPI_SETSELECTIONFADE,
    SPI_GETTOOLTIPANIMATION, SPI_SETTOOLTIPANIMATION,
    SPI_GETTOOLTIPFADE, SPI_SETTOOLTIPFADE,
    SPI_GETUIEFFECTS, SPI_SETUIEFFECTS,
    SPI_GETACTIVEWINDOWTRACKING, SPI_SETACTIVEWINDOWTRACKING,
    SPI_GETACTIVEWNDTRKZORDER, SPI_SETACTIVEWNDTRKZORDER,
    SPI_GETACTIVEWNDTRKTIMEOUT, SPI_SETACTIVEWNDTRKTIMEOUT,
    SPI_GETANIMATION, SPI_SETANIMATION,
    SPI_GETBORDER, SPI_SETBORDER,
    CCHDEVICENAME,
)


def load_functions(_env: Dict[str, str], func_map: Functions) -> None:  # pylint:disable=too-many-statements
    """Load all the functions for any supported windows platform."""
    func_map.window.find_handles = window__find_handles
    func_map.window.enum_window_handles = window__enum_window_handles
    func_map.window.find_handle_for_class_title = window__find_handle_for_class_title
    func_map.window.find_handle_for_child_class_title = window__find_handle_for_child_class_title
    func_map.window.get_title = window__get_title
    func_map.window.is_visible = window__is_visible
    func_map.window.get_process_id = window__get_process_id
    func_map.window.get_class_name = window__get_class_name
    func_map.window.get_module_filename = window__get_module_filename
    func_map.window.get_thread_window_handles = window__get_thread_window_handles
    func_map.window.get_child_window_handles = window__get_child_window_handles
    func_map.window.get_owning_window = window__get_owning_window
    func_map.window.border_rectangle = window__border_rectangle
    func_map.window.client_rectangle = window__client_rectangle
    func_map.window.move_resize = window__move_resize
    func_map.window.redraw = window__redraw
    func_map.window.repaint = window__repaint
    func_map.window.wait_gui_thread_idle = window__wait_gui_thread_idle
    func_map.window.send_message = window__send_message
    func_map.window.post_message = window__post_message
    func_map.window.close = window__close
    func_map.window.maximize = window__maximize
    func_map.window.minimize = window__minimize
    func_map.window.restore = window__restore
    func_map.window.get_visibility_states = window__get_visibility_states
    func_map.window.set_position = window__set_position
    func_map.window.set_layered_attributes = window__set_layered_attributes
    func_map.window.get_active_window = window__get_active_window
    func_map.window.activate = window__activate
    func_map.window.create_message_window = window__create_message_window
    func_map.window.create_display_window = window__create_display_window
    func_map.window.get_font_for_description = window__get_font_for_description
    func_map.window.draw_border_outline = window__draw_border_outline
    func_map.window.get_text_size = window__get_text_size
    func_map.window.do_paint = window__do_paint
    func_map.window.do_draw = window__do_draw
    func_map.paint.draw_rect = paint__draw_rect
    func_map.paint.draw_text = paint__draw_text
    func_map.paint.draw_outline_text = paint__draw_outline_text
    func_map.shell.get_task_bar_window_handles = shell__get_task_bar_window_handles
    func_map.shell.is_key_pressed = shell__is_key_pressed
    func_map.shell.keyboard_hook = shell__keyboard_hook
    func_map.shell.shell_hook = shell__shell_hook
    func_map.shell.register_window_hook = shell__register_window_hook
    func_map.shell.create_global_message_handler = shell__create_global_message_handler
    func_map.shell.unhook = shell__unhook
    func_map.shell.inject_input_vks = shell__inject_input_vks
    func_map.shell.lock_workstation = shell__lock_workstation
    func_map.shell.pump_messages = shell__pump_messages
    func_map.shell.system_parameters_info = shell__system_parameters_info
    func_map.monitor.find_monitors = monitor__find_monitors
    func_map.process.get_exit_code = process__get_exit_code
    func_map.process.get_window_state = process__get_window_state
    func_map.process.get_current_pid = process__get_current_pid


# These functions are all generic, but the result type is very bit specific.

GetModuleHandleW = windll.kernel32.GetModuleHandleW
GetModuleHandleW.restype = HMODULE
GetModuleHandleW.argtypes = [LPCWSTR]

HOOK_CALLBACK_TYPE = CFUNCTYPE(c_int, c_int, HINSTANCE, POINTER(c_void_p))
SetWindowsHookExW = windll.user32.SetWindowsHookExW
SetWindowsHookExW.restype = c_int
SetWindowsHookExW.argtypes = [c_int, HOOK_CALLBACK_TYPE, HINSTANCE, DWORD]

GetMessageW = windll.user32.GetMessageW
GetMessageW.argtypes = [POINTER(MSG), HWND, c_uint, c_uint]

DispatchMessageW = windll.user32.DispatchMessageW
DispatchMessageW.argtypes = [POINTER(MSG)]

TranslateMessage = windll.user32.TranslateMessage
TranslateMessage.argtypes = [POINTER(MSG)]

CallNextHookEx = windll.user32.CallNextHookEx

UnhookWindowsHookEx = windll.user32.UnhookWindowsHookEx

GetExitCodeProcess = windll.kernel32.GetExitCodeProcess
GetExitCodeProcess.restype = BOOL

EnumDisplayMonitors = windll.user32.EnumDisplayMonitors
EnumDisplayMonitors.restype = BOOL

GetMonitorInfoW = windll.user32.GetMonitorInfoW
GetMonitorInfoW.restype = BOOL

RegisterShellHookWindow = windll.user32.RegisterShellHookWindow
RegisterShellHookWindow.argtypes = [HWND]
RegisterShellHookWindow.restype = BOOL

RegisterWindowMessageW = windll.user32.RegisterWindowMessageW
RegisterWindowMessageW.argtypes = [LPCWSTR]
RegisterWindowMessageW.restype = c_uint

RegisterClassExW = windll.user32.RegisterClassExW

CreateWindowExW = windll.user32.CreateWindowExW
CreateWindowExW.argtypes = (
    DWORD, LPCWSTR, LPCWSTR,
    DWORD, c_int, c_int, c_int, c_int, HWND, HMENU,
    HINSTANCE, LPVOID,
)
RegisterWindowMessageW.restype = HWND


DefWindowProcW = windll.user32.DefWindowProcW
DefWindowProcW.argtypes = (HWND, c_uint, WPARAM, LPARAM,)
DefWindowProcW.restype = LRESULT

SystemParametersInfoW = windll.user32.SystemParametersInfoW

SetWindowPos = windll.user32.SetWindowPos

SetActiveWindow = windll.user32.SetActiveWindow

SetForegroundWindow = windll.user32.SetForegroundWindow

SetLayeredWindowAttributes = windll.user32.SetLayeredWindowAttributes
SetLayeredWindowAttributes.argtypes = (HWND, COLORREF, BYTE, DWORD,)

WNDPROCTYPE = WINFUNCTYPE(LRESULT, HWND, c_uint, WPARAM, LPARAM)


def window__find_handles() -> Sequence[HWND]:
    """
    Find all the top-level window handles (type HWND)

    :return: list of window handles.
    """
    ret = []

    def callback(hwnd: HWND) -> bool:
        ret.append(hwnd)
        # return True to continue the enumeration
        return True

    window__enum_window_handles(callback)

    return ret


def window__enum_window_handles(callback: Callable[[HWND], bool]) -> StdRet[None]:
    """Run the callback for each window handle found."""
    # noinspection PyUnusedLocal
    def callback_wrapper(hwnd: HWND, _lparam: LPARAM) -> bool:
        return callback(hwnd)

    enum_win_proc = WINFUNCTYPE(c_bool, c_int, POINTER(c_int))
    res = windll.user32.EnumWindows(enum_win_proc(callback_wrapper), None)
    return WindowsReturnError.checked_stdret('user32.EnumWindows', res)


def window__find_handle_for_class_title(class_name: str, title: str) -> Optional[HWND]:
    """Find a window handle with the given class title."""
    return t_cast(HWND, windll.user32.FindWindowW(class_name, title))


def window__find_handle_for_child_class_title(
        hwnd_parent: HWND, hwnd_child_after: Optional[HWND], class_name: str, title: str,
) -> Optional[HWND]:
    """Find a window handle that has a child with the class title."""
    return t_cast(HWND, windll.user32.FindWindowExW(
        hwnd_parent, hwnd_child_after, class_name, title,
    ))


def window__get_title(hwnd_handle: HWND) -> str:
    """Get the window title for the window with the given handle.  Returns an empty string
    if not found."""
    length = windll.user32.GetWindowTextLengthW(hwnd_handle)
    if length > 0:
        buff = create_unicode_buffer(length + 1)
        windll.user32.GetWindowTextW(hwnd_handle, buff, length + 1)
        return buff.value
    return ""


def window__is_visible(hwnd_handle: HWND) -> bool:
    """Is the window with the handle visible?"""
    val = t_cast(int, windll.user32.IsWindowVisible(hwnd_handle))
    return val != 0


def window__get_process_id(hwnd_handle: HWND) -> DWORD:
    """Get the PID for the window with the given handle."""
    pid = DWORD()
    # thread_pid =
    windll.user32.GetWindowThreadProcessId(hwnd_handle, byref(pid))
    return pid


def window__get_class_name(hwnd_handle: HWND) -> StdRet[str]:
    """Get the class name for the window handle."""
    buff = create_unicode_buffer(MAX_CLASS_NAME_LENGTH + 1)
    size = windll.user32.GetClassNameW(hwnd_handle, buff, MAX_CLASS_NAME_LENGTH + 1)
    if size <= 0:
        return WindowsReturnError.stdret('user32.GetClassNameW')
    return StdRet.pass_ok(buff.value[:size])


def window__get_module_filename(hwnd_handle: HWND) -> StdRet[str]:
    """Get the module filename for the window with the handle."""
    buff = create_unicode_buffer(MAX_FILENAME_LENGTH + 1)
    size = windll.user32.GetWindowModuleFileNameW(hwnd_handle, buff, MAX_FILENAME_LENGTH + 1)
    if size <= 0:
        return WindowsReturnError.stdret('user32.GetWindowModuleFileNameW')
    return StdRet.pass_ok(buff.value[:size])


def window__get_thread_window_handles(thread_process_id: DWORD) -> StdRet[Sequence[HWND]]:
    """
    Get all the window handles for the thread PID.

    :param thread_process_id: thread process ID, as from window__get_thread_process_id
    :return: hwnd for all top-level windows with this thread process id.
    """
    ret: List[HWND] = []

    def callback(hwnd: HWND, _lparam: LPARAM) -> bool:
        ret.append(hwnd)
        return True

    enum_win_proc = WINFUNCTYPE(c_bool, POINTER(c_int), POINTER(c_int))
    res = windll.user32.EnumThreadWindows(thread_process_id, enum_win_proc(callback), None)
    if res == 0:
        return WindowsReturnError.stdret('user32.EnumThreadWindows')

    return StdRet.pass_ok(ret)


def window__get_child_window_handles(hwnd_parent: HWND) -> StdRet[Sequence[HWND]]:
    """Get all the child window handles for the parent handle."""
    ret: List[HWND] = []

    def callback(hwnd: HWND, _: LPARAM) -> bool:
        ret.append(hwnd)
        return True

    enum_win_proc = WINFUNCTYPE(c_bool, POINTER(c_int), POINTER(c_int))
    res = windll.user32.EnumChildWindows(hwnd_parent, enum_win_proc(callback), None)
    if res == 0:
        return WindowsReturnError.stdret('user32.EnumChildWindows')

    return StdRet.pass_ok(ret)


def window__get_owning_window(hwnd_child: HWND) -> StdRet[HWND]:
    """Get the window that owns the given child handle."""
    # "GetTopWindow" gets the top-Z level *child window* for the given window.
    # "GetWindow(..., GW_OWNER)" gets the Owning child (not parent window) for the
    # window.   Difference: "Owner Window" is the HWND for the top-most window whose
    # parent is none (e.g. the desktop).
    ret = windll.user32.GetWindow(hwnd_child, GW_OWNER)
    if ret == 0 or ret is None:
        return WindowsReturnError.stdret('user32.GetWindow')
    return StdRet.pass_ok(t_cast(HWND, ret))


def window__border_rectangle(hwnd: HWND) -> StdRet[OsScreenRect]:
    """
    The outer border size and position of the window

    :param hwnd:
    :return: a ScreenRect, or None if not found.
    """
    rect = RECT()
    res = windll.user32.GetWindowRect(hwnd, byref(rect))
    if res == 0:
        return WindowsReturnError.stdret('user32.GetWindowRect')
    return StdRet.pass_ok(convert_rect(rect))


def window__client_rectangle(hwnd: HWND) -> StdRet[OsScreenRect]:
    """
    The client-usable space within the border rectangle.  Top and Left
    are always 0.

    :param hwnd:
    :return: the rectangle structure, or None
    """
    client_rect = RECT()
    res = windll.user32.GetClientRect(hwnd, byref(client_rect))
    if res == 0:
        return WindowsReturnError.stdret('user32.GetClientRect')
    return StdRet.pass_ok(convert_rect(client_rect))


def window__move_resize(
        hwnd: HWND, x: int, y: int, width: int, height: int,
        repaint: Optional[bool] = True,
) -> bool:
    """
    Move and resize the window.
    """

    ret = t_cast(BOOL, windll.user32.MoveWindow(hwnd, x, y, width, height, repaint))

    # check that it worked correctly?

    return ret != 0


def window__redraw(hwnd: HWND, force: Optional[bool] = False) -> bool:
    """Ask the window handle to be redrawn."""
    # window__wait_gui_thread_idle(hwnd)
    # res = windll.user32.ChangeWindowMessageFilterEx(hwnd, WM_PAINT, 1, None)
    # res = windll.user32.UpdateWindow(hwnd)
    res = windll.user32.RedrawWindow(
        hwnd, None, None,
        RDW_INTERNALPAINT | RDW_ERASE | RDW_ALLCHILDREN | RDW_FRAME,
    )
    if res != 0:
        # Successful!
        return True

    # None of the above worked, probably because the process isolation doesn't allow
    # our process to send a message to another process.

    # So, try minimize then actions (if maximized, it will actions itself again)
    # This really messes up the z-ordering, though.
    if force and window__is_visible(hwnd):
        windll.user32.ShowWindow(hwnd, SW_MINIMIZE)
        windll.user32.ShowWindow(hwnd, SW_RESTORE)
        return True

    return False


def window__repaint(hwnd: HWND) -> StdRet[None]:
    """Ask the window handle to be repainted."""
    # res = windll.user32.InvalidateRect(hwnd, None, False)
    res = windll.user32.RedrawWindow(hwnd, None, None, RDW_INVALIDATE)
    return WindowsReturnError.checked_stdret('user32.RedrawWindow', res)


def window__wait_gui_thread_idle(
        hwnd: HWND, timeout: Optional[int] = 1000,
) -> StdRet[None]:
    """Wait for a handle to go idle."""

    # TODO check for more error results from WinAPI calls.

    thread_pid = window__get_process_id(hwnd)
    if thread_pid:
        hproc = windll.kernel32.OpenProcess(
            PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, thread_pid,
        )
        try:
            res = windll.user32.WaitForInputIdle(hproc, timeout)
            # == 0: wait okay.
            # == WAIT_TIMEOUT: wait timed out
            # == WAIT_FAILED: error occurred
            if res != 0:
                return WindowsReturnError.stdret('user32.WaitForInputIdle')
        finally:
            windll.kernel32.CloseHandle(hproc)
    windll.user32.WaitGuiThreadIdle(hwnd)
    return RET_OK_NONE


def window__send_message(
        hwnd: HWND, message: UINT, wparam: WPARAM, lparam: LPARAM,
) -> StdRet[LRESULT]:
    """Send a message to a window handle."""
    err = _attach_message_queue_to_thread(hwnd)
    if err.has_error:
        return err.forward()
    res = windll.user32.SendMessageW(
        hwnd, message, wparam, lparam,
    )
    log.trace(
        'send_message({hwnd:04x}, {message:04x}) = {res}',
        hwnd=hwnd, message=message.value, res=res,
    )
    return StdRet.pass_ok(t_cast(LRESULT, res))


def window__post_message(
        hwnd: HWND, message: UINT, wparam: WPARAM, lparam: LPARAM,
) -> StdRet[None]:
    """'post' a message to a window handle."""
    err = _attach_message_queue_to_thread(hwnd)
    if err.has_error:
        return err
    res = windll.user32.PostMessageW(hwnd, message, wparam, lparam)
    log.trace(
        'post_message({hwnd:04x}, {message:04x})',
        hwnd=hwnd, message=message.value,
    )
    return WindowsReturnError.checked_stdret('user32.PostMessageW', res)


def window__close(hwnd: HWND) -> StdRet[None]:
    """Close a window handle.  Just posts a message to that handle."""
    # Code modified from http://msdn.microsoft.com/msdnmag/issues/02/08/CQA/

    # Give the "must close" message to the window
    return window__post_message(
        hwnd, UINT(WM_CLOSE), WPARAM(0), LPARAM(0),
    )


def window__maximize(hwnd: HWND) -> StdRet[None]:
    """Maximize a window handle."""
    res = windll.user32.ShowWindow(hwnd, SW_MAXIMIZE)
    return WindowsReturnError.checked_stdret('user32.ShowWindow', res)


def window__minimize(hwnd: HWND) -> StdRet[None]:
    """Minimize a window handle."""
    res = windll.user32.ShowWindow(hwnd, SW_MINIMIZE)
    return WindowsReturnError.checked_stdret('user32.ShowWindow', res)


def window__restore(hwnd: HWND) -> StdRet[None]:
    """Restore a window handle."""
    # This needs to be called twice, because of the situation
    # where a window was maximized then minimized.  The first
    # actions will bring it back to visible, but maximized,
    # and the second will bring it to restored.
    # But... the first call will return:
    # "If the window was previously hidden, the return value is zero."
    # So, only call it twice if it was minimized.
    if windll.user32.ShowWindow(hwnd, SW_RESTORE) == 0:
        windll.user32.ShowWindow(hwnd, SW_RESTORE)
    return RET_OK_NONE


class WINDOWPLACEMENT(Structure):
    """The WINDOWPLACEMENT structure.
    see https://msdn.microsoft.com/en-us/library/windows/desktop/ms632611(v=vs.85).aspx"""
    _fields_ = (
        ("length", UINT),
        ("flags", UINT),
        ("showCmd", UINT),
        ("ptMinPosition", POINT),
        ("ptMaxPosition", POINT),
        ("rcNormalPosition", RECT),
    )


def window__get_visibility_states(hwnd: HWND) -> Sequence[str]:  # pylint:disable=too-many-return-statements
    """
    Returns a list of the current visibility state of the window.

    :param hwnd:
    :return: a sequence of zero or more of:
        'hidden': window is hidden
        'maximized': window is maximized
        'minimized': window is minimized
        'restored': window is in the "restored" state
        'shown': window is not hidden
        'active': window is active (should not be trusted)
        If the list is empty, then the window doesn't exist.
    """
    placement = WINDOWPLACEMENT()
    # pylint is confused by structures.
    placement.length = c_sizeof(placement)  # pylint:disable=attribute-defined-outside-init
    val = windll.user32.GetWindowPlacement(hwnd, byref(placement))
    if val is None:
        return STRING_EMPTY_TUPLE
    show_cmd = placement.showCmd
    if show_cmd == SW_HIDE:
        return ('hidden',)
    if show_cmd == SW_SHOWNORMAL:
        return 'shown', 'restored', 'active'
    if show_cmd == SW_SHOWMINIMIZED:
        return 'shown', 'minimized', 'active'
    if show_cmd == SW_MAXIMIZE:
        return 'shown', 'maximized', 'active'
    if show_cmd == SW_SHOWMAXIMIZED:
        return 'shown', 'maximized', 'active'
    if show_cmd == SW_SHOWNOACTIVATE:
        return 'shown', 'restored'
    if show_cmd == SW_SHOW:
        return 'shown', 'restored', 'active'
    if show_cmd == SW_MINIMIZE:
        return 'shown', 'minimized', 'active'
    if show_cmd == SW_SHOWMINNOACTIVE:
        return 'shown', 'minimized'
    if show_cmd == SW_SHOWNA:
        return 'shown', 'restored'
    if show_cmd == SW_RESTORE:
        return 'shown', 'restored', 'active'
    return STRING_EMPTY_TUPLE


class LOGBRUSH(Structure):
    """The LOGBRUSH structure"""
    _fields_ = (
        # VC98/Include/wingdi.h 1025
        ('lbStyle', c_uint),
        ('lbColor', DWORD),  # COLORREF
        ('lbHatch', c_long),
    )


def window__draw_border_outline(
        rect: OsScreenRect,
        color: Color,
        width: int,
        line_style: Optional[int] = PS_SOLID,
        fill_style: Optional[int] = BS_NULL,
        _parent_hwnd: Optional[HWND] = None,
) -> None:
    """
    Draws a border on the screen.  Does not need a window context.

    :param fill_style:
    :param line_style:
    :param rect: border to draw
    :param color: Petronia color
    :param width:
    :param line_style:
    :param _parent_hwnd: handle of the parent window, if any.
    :return:
    """
    pen_handle = None
    brush_handle = None
    dc_handle = None
    color_ref = color_to_native_rgb(color)

    try:
        # Pen == outside drawing definition
        pen_handle = windll.gdi32.CreatePen(line_style, width, color_ref)

        # Brush == inside
        brush_def = LOGBRUSH()
        # pylint doesn't understand structures.
        # BS_NULL so that the fill is empty
        brush_def.lbStyle = fill_style  # pylint:disable=attribute-defined-outside-init
        brush_def.lbHatch = HS_DIAGCROSS  # pylint:disable=attribute-defined-outside-init
        brush_def.lbColor = color_ref  # pylint:disable=attribute-defined-outside-init
        brush_handle = windll.gdi32.CreateBrushIndirect(byref(brush_def))

        # Create a device context to draw on
        dc_handle = windll.gdi32.CreateDCW("DISPLAY", None, None, None)
        windll.gdi32.SelectObject(dc_handle, brush_handle)
        windll.gdi32.SelectObject(dc_handle, pen_handle)

        # EXPERIMENTAL CODE
        # This doesn't work for rendering a border, because the window will clip
        # at its border, which means that it won't include the outside, where we want
        # to draw.
        # if parent_hwnd is not None:
        #     parent_hdc = windll.user32.GetDC(parent_hwnd)
        #     if parent_hdc is not None:
        #         try:
        #             h_region = wintypes.HANDLE()
        #             windll.gdi32.GetClipRgn(parent_hdc, h_region)
        #             windll.gdi32.SelectClipRgn(dc_handle, h_region)
        #         finally:
        #             windll.user32.ReleaseDC(parent_hdc)
        # EXPERIMENTAL CODE

        windll.gdi32.Rectangle(dc_handle, rect.left, rect.top, rect.right, rect.bottom)
    finally:
        if brush_handle is not None:
            windll.gdi32.DeleteObject(brush_handle)
        if pen_handle is not None:
            windll.gdi32.DeleteObject(pen_handle)
        if dc_handle is not None:
            windll.gdi32.DeleteDC(dc_handle)


def window__set_position(
        hwnd: HWND,
        hwnd_after_zorder: Union[HWND, str],
        rect: OsScreenRect,
        flags: Iterable[str],
) -> StdRet[None]:
    """Set a window's size and position."""
    zorder = hwnd_after_zorder
    if isinstance(zorder, str) and zorder in HWND_ZORDER_MAP:
        zorder = HWND_ZORDER_MAP[zorder]
    if isinstance(zorder, str):
        raise ValueError('unknown zorder type "{0}"'.format(zorder))
    uflags = 0
    for flag in flags:
        if flag in SWP_FLAG_MAP:
            uflags |= SWP_FLAG_MAP[flag]
        else:
            log.error("Unknown SWP set position flag {flag}", flag=flag)
    res = SetWindowPos(hwnd, zorder, rect.x, rect.y, rect.width, rect.height, uflags)
    return WindowsReturnError.checked_stdret('user32.SetWindowPos', res)


def window__set_layered_attributes(
        hwnd: HWND, color: Color,
) -> StdRet[None]:
    """Set layered attributes."""
    rgba = color_to_rgba(color)
    res = SetLayeredWindowAttributes(
        hwnd,
        RGB(rgba[COLOR_RGBA_RED_INDEX], rgba[COLOR_RGBA_GREEN_INDEX], rgba[COLOR_RGBA_BLUE_INDEX]),
        rgba[COLOR_RGBA_ALPHA_INDEX],
        LWA_ALPHA,
    )
    return WindowsReturnError.checked_stdret('user32.SetLayeredWindowAttributes', res)


def window__get_active_window() -> Optional[HWND]:
    """Get the active window."""
    # GetActiveWindow is only for the current thread.
    # It usually just returns None.
    hwnd = t_cast(HWND, windll.user32.GetForegroundWindow())
    if hwnd == 0:
        return None
    return hwnd


def window__activate(hwnd: HWND) -> StdRet[None]:
    """Give the window the focus."""
    # Give the window the focus.  This is the Microsoft Magic Focus Dance.
    current_hwnd = windll.user32.GetForegroundWindow()
    current_thread_id = windll.kernel32.GetCurrentThreadId()
    thread_process_id = windll.user32.GetWindowThreadProcessId(current_hwnd, None)
    if thread_process_id != current_thread_id:
        res = windll.user32.AttachThreadInput(thread_process_id, current_thread_id, True)
        # ERROR_INVALID_PARAMETER means that the two threads are already attached.
        if res == 0:
            err = WindowsReturnError('user32.AttachThreadInput')
            if err.errno != ERROR_INVALID_PARAMETER:
                # "WARN: could not attach thread input to thread
                # {thread_process_id} ({GetLastError()})"
                return StdRet.pass_error(err)
    res = windll.user32.SetWindowPos(hwnd, HWND_TOPMOST, 0, 0, 0, 0, SWP_NOSIZE | SWP_NOMOVE)
    if res == 0:
        return WindowsReturnError.stdret('user32.SetWindowPos')
    # At this point, the window hwnd is valid, so we don't need to fail out
    # if the results are non-zero.  Some of these will not succeed due to
    # attributes of the window, rather than the window not existing.
    windll.user32.SetWindowPos(hwnd, HWND_NOTOPMOST, 0, 0, 0, 0, SWP_NOSIZE | SWP_NOMOVE)
    windll.user32.AttachThreadInput(thread_process_id, current_thread_id, False)
    windll.user32.SetForegroundWindow(hwnd)
    windll.user32.SetFocus(hwnd)
    windll.user32.SetActiveWindow(hwnd)
    return RET_OK_NONE


class WNDCLASSEX(Structure):  # pylint:disable=too-many-instance-attributes
    """The WNDCLASSEX structure."""
    _fields_ = [
        ("cbSize", c_uint),
        ("style", c_uint),
        ("lpfnWndProc", WNDPROCTYPE),
        ("cbClsExtra", c_int),
        ("cbWndExtra", c_int),
        ("hInstance", HANDLE),
        ("hIcon", HANDLE),
        ("hCursor", HANDLE),
        ("hBrush", HANDLE),
        ("lpszMenuName", LPCWSTR),
        ("lpszClassName", LPCWSTR),
        ("hIconSm", HANDLE),
    ]


def window__create_message_window(
        class_name: str, message_handler: NativeMessageCallback,
) -> StdRet[HWND]:
    """
    Create a "message" window - a window that's only for posting messages
    to, and for handling other OS messages.

    However, we need some broadcast messages, like WM_DISPLAYCHANGE.
    Therefore, it needs to be a real window that is just never shown.

    :param message_handler: the handler procedure created by shell__create_global_message_handler
    :param class_name: unique class name for the window
    :return: hwnd
    """

    if not class_name.startswith(PETRONIA_CREATED_WINDOW__CLASS_PREFIX):
        class_name = PETRONIA_CREATED_WINDOW__CLASS_PREFIX + class_name

    hinst = GetModuleHandleW(None)
    if hinst is None or hinst == 0:
        return WindowsReturnError.stdret('kernel32.GetModuleHandleW')

    # A persistent pointer to a handler.  Must be persisted so it isn't
    # removed when we exit this method.
    window_proc = WNDPROCTYPE(message_handler)

    window_class = WNDCLASSEX()
    # pylint doesn't understand this structure.
    window_class.cbSize = c_sizeof(WNDCLASSEX)  # pylint:disable=attribute-defined-outside-init
    window_class.style = 0  # pylint:disable=attribute-defined-outside-init
    window_class.lpfnWndProc = window_proc  # pylint:disable=attribute-defined-outside-init
    window_class.cbClsExtra = 0  # pylint:disable=attribute-defined-outside-init
    window_class.cbWndExtra = 0  # pylint:disable=attribute-defined-outside-init
    window_class.hInstance = hinst  # pylint:disable=attribute-defined-outside-init
    window_class.hIcon = 0  # pylint:disable=attribute-defined-outside-init
    window_class.hCursor = 0  # pylint:disable=attribute-defined-outside-init
    window_class.hBrush = 0  # pylint:disable=attribute-defined-outside-init
    window_class.lpszMenuName = 0  # pylint:disable=attribute-defined-outside-init
    window_class.lpszClassName = class_name  # pylint:disable=attribute-defined-outside-init
    window_class.hIconSm = 0  # pylint:disable=attribute-defined-outside-init

    class_handle = RegisterClassExW(byref(window_class))
    if class_handle == 0:
        return WindowsReturnError.stdret('user32.RegisterClassExW')
    # Top level, never viewed, window.  Note that we set title to
    # "null" to further emphasize that this is a non-viewable window.
    # We don't use a message-only window, so that the window can
    # receive global event hooks.
    hwnd: HWND = CreateWindowExW(
        0, class_name, None,
        WS_OVERLAPPEDWINDOW, 0, 0, 0, 0, HWND_DESKTOP, None, hinst, None,
    )
    if hwnd is None or hwnd == 0:
        return WindowsReturnError.stdret('user32.CreateWindowExW')

    # Persist the pointer
    _CALLBACK_POINTERS[hwnd] = window_proc
    return StdRet.pass_ok(hwnd)


def window__create_display_window(
        class_name: str,
        title: str,
        message_handler: MessageCallback,
        style_flags: Iterable[str],
) -> StdRet[HWND]:
    """Create a window."""
    if not class_name.startswith(PETRONIA_CREATED_WINDOW__CLASS_PREFIX):
        class_name = PETRONIA_CREATED_WINDOW__CLASS_PREFIX + class_name

    if title is None:
        title = ""
        app_icon = None
        small_icon = None
        cursor_icon = None
    else:
        app_icon = windll.user32.LoadIconW(None, IDI_APPLICATION)
        small_icon = windll.user32.LoadIconW(None, IDI_APPLICATION)
        cursor_icon = windll.user32.LoadCursorW(None, IDC_ARROW)

    # A persistent pointer to a handler.  Must be persisted so it isn't
    # removed when we exit this method.
    window_proc = WNDPROCTYPE(message_handler)
    hinst = GetModuleHandleW(None)

    window_class = WNDCLASSEX()
    # pylint doesn't understand structures.
    window_class.cbSize = c_sizeof(WNDCLASSEX)  # pylint:disable=attribute-defined-outside-init
    window_class.style = 0  # pylint:disable=attribute-defined-outside-init
    window_class.lpfnWndProc = window_proc  # pylint:disable=attribute-defined-outside-init
    window_class.cbClsExtra = 0  # pylint:disable=attribute-defined-outside-init
    window_class.cbWndExtra = 0  # pylint:disable=attribute-defined-outside-init
    window_class.hInstance = hinst  # pylint:disable=attribute-defined-outside-init
    window_class.hIcon = app_icon  # pylint:disable=attribute-defined-outside-init
    window_class.hCursor = cursor_icon  # pylint:disable=attribute-defined-outside-init
    window_class.hBrush = COLOR_WINDOW + 1  # pylint:disable=attribute-defined-outside-init
    window_class.lpszMenuName = 0  # pylint:disable=attribute-defined-outside-init
    window_class.lpszClassName = class_name  # pylint:disable=attribute-defined-outside-init
    window_class.hIconSm = small_icon  # pylint:disable=attribute-defined-outside-init

    class_handle = RegisterClassExW(byref(window_class))
    if class_handle == 0:
        return WindowsReturnError.stdret('user32.RegisterClassExW')

    ex_style = 0
    for flag in style_flags:
        if flag in WS_EX_STYLE_BIT_MAP:
            ex_style |= WS_EX_STYLE_BIT_MAP[flag]
    style = 0
    for flag in style_flags:
        if flag in WS_STYLE_BIT_MAP:
            style |= WS_STYLE_BIT_MAP[flag]

    hwnd = t_cast(HWND, CreateWindowExW(
        ex_style, class_name, title,
        style,
        CW_USEDEFAULT, CW_USEDEFAULT,
        240, 120,
        None,  # was HWND_DESKTOP,
        None, hinst, None,
    ))
    if hwnd is None or hwnd == 0:
        return WindowsReturnError.stdret('user32.CreateWindowExW')
    windll.user32.ShowWindow(hwnd, SW_SHOWNORMAL)
    windll.user32.UpdateWindow(hwnd)

    _CALLBACK_POINTERS[hwnd] = window_proc
    return StdRet.pass_ok(hwnd)


_FONT_HANDLES: Dict[str, Optional[HFONT]] = {}


def window__get_font_for_description(  # pylint:disable=too-many-branches,too-many-locals
        font: str,
        hwnd: Optional[HWND] = None, base_hdc: Optional[HDC] = None,
) -> Optional[HFONT]:
    """Get the font for a font description."""
    if font in _FONT_HANDLES:
        return _FONT_HANDLES[font]
    font_details = font.split(',')
    font_name = font_details[0].strip()
    font_params = font_details[1:]
    created_hdc = None
    hdc = base_hdc
    if base_hdc is None:
        if hwnd is None:
            hdc = windll.gdi32.CreateDCW("DISPLAY", None, None, None)
            created_hdc = hdc
        else:
            hdc = windll.user32.GetDC(hwnd)
    try:
        # if windll.gdi32.FontExist(hdc, font_name) != 0:
        #     raise OSError("Unknown font {0}".format(font_name))

        point = 12
        weight = FW_NORMAL
        italic = 0
        underline = 0
        strikeout = 0

        for param in font_params:
            param = param.strip().lower()
            if param.endswith('pt'):
                point = int(param[:-2])
            elif param in ('bold', 'b'):
                weight = FW_BOLD
            elif param in ('italic', 'italics', 'i'):
                italic = 1
            elif param in ('underline', 'under', 'u'):
                underline = 1
            elif param in ('strikethrough', 'strikeout', 'strike', 's'):
                strikeout = 1

        pixels_per_point_y = windll.gdi32.GetDeviceCaps(hdc, LOGPIXELSY)
        if pixels_per_point_y <= 0:
            pixels_per_point_y = 72
        height = (point * pixels_per_point_y) // 72
        hfont: HANDLE = windll.gdi32.CreateFontW(
            -height, 0, 0, 0,
            weight, italic, underline, strikeout,
            DEFAULT_CHARSET, OUT_TT_PRECIS, CLIP_DEFAULT_PRECIS, PROOF_QUALITY, FF_DONTCARE,
            create_unicode_buffer(font_name),
        )
        if hfont == 0 or hfont is None:
            # Not found, so record this.
            _FONT_HANDLES[font] = None
            return None
        _FONT_HANDLES[font] = hfont

        atexit.register(_delete_gdi_object, hfont)

        return hfont
    finally:
        if base_hdc is None and created_hdc is None:
            windll.user32.ReleaseDC(hdc)
        if base_hdc is None and created_hdc is not None:
            windll.gdi32.DeleteDC(hdc)


def _delete_gdi_object(obj_handle: HANDLE) -> None:
    """Frees a handle to a logical pen, brush, font, bitmap, region, or palette (HGDIOBJ)."""
    windll.gdi32.DeleteObject(obj_handle)


def window__get_text_size(
        hfont: HFONT, text: str,
        hwnd: Optional[HWND] = None, base_hdc: Optional[HDC] = None,
) -> StdRet[OsScreenSize]:
    """
    Can be called within or outside a paint context.

    :param hwnd:
    :param hfont:
    :param text:
    :param base_hdc: set to the paint's hdc if within a Paint callback.
    :return: width, height
    """
    lines = text.splitlines()
    height = 0
    width = 0
    size = WINTYPE_SIZE()
    old_hfont = None
    created_hdc = None
    hdc = base_hdc
    if base_hdc is None:
        if hwnd is None:
            # hdc = windll.gdi32.CreateDCW(HWND_DESKTOP)
            hdc = windll.gdi32.CreateDCW("DISPLAY", None, None, None)
            created_hdc = hdc
        else:
            hdc = windll.user32.GetDC(hwnd)
    try:
        old_hfont = windll.gdi32.SelectObject(hdc, hfont)
        for line in lines:
            res = windll.gdi32.GetTextExtentPoint32W(
                hdc,
                create_unicode_buffer(line), len(line),
                byref(size),
            )
            if res == 0:
                return WindowsReturnError.stdret('gdi32.GetTextExtentPoint32W')
            height += size.cy.value
            width = max(width, size.cx.value)
        return StdRet.pass_ok((t_cast(ScreenUnit, width), t_cast(ScreenUnit, height)))
    finally:
        # To prevent a memory leak
        if hdc is not None and old_hfont is not None:
            windll.gdi32.SelectObject(hdc, old_hfont)
        if base_hdc is None and created_hdc is None:
            windll.user32.ReleaseDC(hdc)
        if base_hdc is None and created_hdc is not None:
            windll.gdi32.DeleteDC(hdc)


class PAINTSTRUCT(Structure):
    """The PAINTSTRUCT structure"""
    _fields_ = (
        ("hdc", HANDLE),
        ("fErase", c_bool),
        ("rcPaint", RECT),
        ("fRestore", c_bool),
        ("fIncUpdate", c_bool),
        ("rgbReserved", BYTE * 32),
    )


def window__do_paint(
        hwnd: HWND, paint_callback: PaintCallback[T],
) -> StdRet[T]:
    """
    Start the paint callback message.

    :param hwnd:
    :param paint_callback: function, takes 2 argument: the hwnd, and the hdc of the paint.
    :return: paint_callback return value
    """
    ps = PAINTSTRUCT()
    hdc = windll.user32.BeginPaint(hwnd, byref(ps))
    if hdc == 0 or hdc is None:
        return WindowsReturnError.stdret('user32.BeginPaint')
    try:
        return StdRet.pass_ok(paint_callback(hwnd, hdc))
    finally:
        windll.user32.EndPaint(hwnd, byref(ps))


def window__do_draw(hwnd: HWND, paint_callback: PaintCallback[T]) -> StdRet[T]:
    """Tell a function to draw itself, along with a callback to run on the paint."""
    hdc: HDC = windll.user32.GetDC(hwnd)
    if hdc == 0 or hdc is None:
        return WindowsReturnError.stdret('user32.GetDC')
    try:
        return StdRet.pass_ok(paint_callback(hwnd, hdc))
    finally:
        windll.user32.ReleaseDC(hdc)


def paint__draw_rect(
        hdc: HDC, area: OsScreenRect, color: Color,
) -> StdRet[None]:
    """Paint a rectangle."""
    rect = RECT()
    rect.left = c_long(area.left)
    rect.top = c_long(area.top)
    rect.right = c_long(area.right)
    rect.bottom = c_long(area.bottom)
    fill_rgb = color_to_native_rgb(color)
    fill_brush = None
    try:
        fill_brush = windll.gdi32.CreateSolidBrush(fill_rgb)
        res = windll.user32.FillRect(hdc, byref(rect), fill_brush)
        return WindowsReturnError.checked_stdret('user32.FillRect', res)
    finally:
        if fill_brush is not None:
            _delete_gdi_object(fill_brush)


def paint__draw_text(  # pylint:disable=too-many-arguments
        hdc: HDC, hfont: HFONT,
        text: str,
        pos_x: int, pos_y: int, width: int, height: int,
        fg_color: Optional[Color], bg_color: Optional[Color],
) -> StdRet[None]:
    """Draw some text."""
    old_hfont = None
    try:
        old_hfont = windll.gdi32.SelectObject(hdc, hfont)
        if fg_color:
            fg = color_to_native_rgb(fg_color)
            windll.gdi32.SetTextColor(hdc, fg)
        if bg_color:
            bg = color_to_native_rgb(bg_color)
            windll.gdi32.SetBkColor(hdc, bg)
            windll.gdi32.SetBkMode(hdc, OPAQUE)
        else:
            bg = COLORREF(RGB(0, 0, 0))
            windll.gdi32.SetBkColor(hdc, bg)
            windll.gdi32.SetBkMode(hdc, TRANSPARENT)

        rect = RECT()
        rect.left = c_long(pos_x)
        rect.top = c_long(pos_y)
        rect.right = c_long(pos_x + width)
        rect.bottom = c_long(pos_y + height)

        res = windll.user32.DrawTextW(
            hdc, create_unicode_buffer(text), len(text), byref(rect),
            DT_LEFT | DT_TOP | DT_NOPREFIX,
        )
        return WindowsReturnError.checked_stdret('user32.DrawTextW', res)
    finally:
        # To prevent a memory leak
        if old_hfont is not None:
            windll.gdi32.SelectObject(hdc, old_hfont)


def paint__draw_outline_text(  # pylint:disable=too-many-locals,too-many-arguments
        hdc: HDC, hfont: HFONT,
        text: str,
        pos_x: int, pos_y: int,
        outline_width: int, outline_color: Color, fill_color: Color, bg_color: Optional[Color],
) -> StdRet[None]:
    """

    :param hdc:
    :param hfont:
    :param text:
    :param pos_x: logical x position
    :param pos_y: logical y position
    :param outline_width:
    :param outline_color:
    :param fill_color:
    :param bg_color:
    :return:
    """
    outline_rgb = color_to_native_rgb(outline_color)
    fill_rgb = color_to_native_rgb(fill_color)
    old_hfont = None
    fill_brush = None
    outline_pen = None
    try:
        old_hfont = windll.gdi32.SelectObject(hdc, hfont)

        outline_pen = windll.gdi32.CreatePen(PS_GEOMETRIC | PS_SOLID, outline_width, outline_rgb)
        windll.gdi32.SelectObject(hdc, outline_pen)

        fill_brush = windll.gdi32.CreateSolidBrush(fill_rgb)
        windll.gdi32.SelectObject(hdc, fill_brush)

        if bg_color:
            bg = color_to_native_rgb(bg_color)
            windll.gdi32.SetBkColor(hdc, bg)
            windll.gdi32.SetBkMode(hdc, OPAQUE)
        else:
            bg = COLORREF(RGB(0, 0, 0))
            windll.gdi32.SetBkColor(hdc, bg)
            windll.gdi32.SetBkMode(hdc, TRANSPARENT)

        windll.gdi32.BeginPath(hdc)
        windll.gdi32.TextOutW(hdc, pos_x, pos_y, create_unicode_buffer(text), len(text))
        windll.gdi32.EndPath(hdc)
        res = windll.gdi32.StrokeAndFillPath(hdc)
        return WindowsReturnError.checked_stdret('gdi32.StrokeAndFillPath', res)
    finally:
        if fill_brush is not None:
            _delete_gdi_object(fill_brush)
        if outline_pen is not None:
            _delete_gdi_object(outline_pen)
        # To prevent a memory leak
        if old_hfont is not None:
            windll.gdi32.SelectObject(hdc, old_hfont)


def shell__get_task_bar_window_handles() -> Sequence[HWND]:
    """Get the handles for the task bar window."""
    ret = []

    for hwnd in window__find_handles():
        cname = window__get_class_name(hwnd)
        if cname == "Shell_TrayWnd":
            ret.append(hwnd)

    return ret


def shell__is_key_pressed(v_key: c_int) -> bool:
    """Is a key pressed?"""
    state = t_cast(SHORT, windll.user32.GetAsyncKeyState(v_key))
    return state != 0


SHELL__CANCEL_CALLBACK_CHAIN = "Cancel"


class KBDLLHOOKSTRUCT(Structure):
    """The KBDLLHOOKSTRUCT struct.
    see https://msdn.microsoft.com/en-us/library/windows/desktop/ms644967(v=vs.85).aspx"""
    _fields_ = [
        ("vkCode", DWORD),
        ("scanCode", DWORD),
        ("flags", DWORD),
        ("time", DWORD),
        ("dwExtraInfo", c_void_p),
    ]


# The callback pointers are implemented as ctypes pointers.
# Because of the way these work, if we pass the pointer to a
# windows hook then leave context, the Python object will
# be cleaned up, destroying that memory pointer.  In order to
# avoid this, we keep a list of callback pointers associated
# with their hook handles, so they are only cleaned up when
# needed, and not before.
_CALLBACK_POINTERS = {}


def shell__keyboard_hook(
        callback: Callable[[int, int, bool, bool], Optional[str]],
) -> StdRet[HHOOK]:
    """
    Adds a global keyboard hook, called when any key is pressed in any
    context (except for a few OS specific ones, like the task manager or
    login).  The callback is called directly in the thread that invoked
    this method.  It is up to the callback to be as responsive as possible.

    The callback takes the parameters (vk_code, scan_code, is_key_up, is_injected)

    If the callback explicitly returns the value "Cancel"
    (SHELL__CANCEL_CALLBACK_CHAIN), then the next hook in the chain of
    listeners will not be called.  This is made very explicit because
    most circumstances dictate that the next chained handler should be
    called.  Even then, there are circumstances in which the next hook
    will still need to be called.

    The total time for the callback MUST be less than the data entry
    specified in the LowLevelHooksTimeout value (milliseconds) in the
    registry key `HKEY_CURRENT_USER\\Control Panel\\Desktop`.  In Windows 7
    and later, if the hook goes beyond this time, the hook is silently
    removed, and the application won't know about it.

    :param callback:
    :return: hook handle
    """
    hook_id = None

    def low_level_handler(code: int, wparam: WPARAM, lparam: LPARAM) -> int:
        """Low-level keyboard handler."""
        kbd_ptr = c_cast(lparam, POINTER(KBDLLHOOKSTRUCT))[0]

        # If code is less than zero, the hook procedure must pass the message
        # to the CallNextHookEx function without further processing and should
        # return the value returned by CallNextHookEx.
        call_next = True
        try:
            if code >= 0:
                # vk_code = kbd_ptr.vkCode
                # scan_code = kbd_ptr.scanCode
                flag_bits = kbd_ptr.flags
                # time = kbd_ptr.time
                # flags = [
                #     flag_bits & LLKHF_EXTENDED == LLKHF_EXTENDED and 'extended' or None,
                #     flag_bits & LLKHF_LOWER_IL_INJECTED == LLKHF_LOWER_IL_INJECTED
                #       and 'lower-injected' or None,
                #     flag_bits & LLKHF_INJECTED == LLKHF_INJECTED and 'injected' or None,
                #     flag_bits & LLHKF_ALTDOWN == LLHKF_ALTDOWN and 'alt' or None,
                #     flag_bits & LLHKF_UP == LLHKF_UP and 'up' or 'down',
                # ]
                ret = callback(
                    kbd_ptr.vkCode,
                    kbd_ptr.scanCode,
                    flag_bits & LLHKF_UP == LLHKF_UP,
                    flag_bits & LLKHF_INJECTED == LLKHF_INJECTED,
                )
                if ret == SHELL__CANCEL_CALLBACK_CHAIN:
                    call_next = False
        except BaseException as err:  # pylint:disable=broad-except
            log.error("Error encountered while handling a keyboard event")
            traceback.print_exception(type(err), err, err.__traceback__)
        if call_next:
            # print(" - forwarding key event")
            return t_cast(int, CallNextHookEx(hook_id, code, wparam, lparam))
        # From the docs:
        # If the hook procedure processed the message, it may return
        # a nonzero value to prevent the system from passing the
        # message to the rest of the hook chain or the target window
        # procedure.
        # print("DEBUG NOT FORWARDING KEY")
        return 1

    callback_pointer = HOOK_CALLBACK_TYPE(low_level_handler)
    hook_id = t_cast(HHOOK, SetWindowsHookExW(
        WH_KEYBOARD_LL, callback_pointer, GetModuleHandleW(None), 0,
    ))
    if hook_id == 0:
        return WindowsReturnError.stdret('SetWindowsHookExW / keyboard')
    _CALLBACK_POINTERS[hook_id] = callback_pointer

    # Ensure that the hook is *always* uninstalled at exit to prevent OS
    # resource leaks.
    atexit.register(shell__unhook, hook_id)
    return StdRet.pass_ok(hook_id)


def shell__shell_hook(
        callback: Callable[[int, WPARAM, LPARAM], Optional[str]],
) -> StdRet[HHOOK]:
    """
    Adds a global shell hook, called when any key is pressed in any
    context.  The callback is called directly in the thread that invoked
    this method.  It is up to the callback to be as responsive as possible.

    If the callback explicitly returns the value "Cancel"
    (SHELL__CANCEL_CALLBACK_CHAIN), then the next hook in the chain of
    listeners will not be called.  This is made very explicit because
    most circumstances dictate that the next chained handler should be
    called.  Even then, there are circumstances in which the next hook
    will still need to be called.

    The callback takes the parameters (code, wparam, lparam).  It is up
    to the callback to correctly parse the values.  Note that this is
    really windows specific, so it's a good idea to read through the docs.

    This will fail with a ERROR_HOOK_NEEDS_HMOD (1428) error until the crazy
    work-around is implemented.
    The crazy work around is to register a DLL to handle this, and have
    the DLL be loaded into the shell process.  The DLL also needs both a
    x86 and x64 version.  And the DLL pipes the events back to this process.

    https://stackoverflow.com/questions/61413733/setwindowshookex-method-fails-with-code-1428-dll-injection

    :param callback:
    :return: hook handle
    """

    hmod = GetModuleHandleW(None)
    if hmod is None is None:
        return WindowsReturnError.stdret('kernel32.GetModuleHandleW')

    # See https://msdn.microsoft.com/en-us/library/windows/desktop/ms644991(v=vs.85).aspx
    hook_id = None

    def shell_handler(code: int, wparam: WPARAM, lparam: LPARAM) -> LRESULT:
        log.debug(
            "[Shell handler] {code} {wparam} {lparam}",
            code=code, wparam=wparam, lparam=lparam,
        )
        call_next = True
        try:
            # From the docs: If nCode is less than zero, the hook
            # procedure must return the value returned by CallNextHookEx.
            if code >= 0:
                ret = callback(code, wparam, lparam)
                if ret == SHELL__CANCEL_CALLBACK_CHAIN:
                    call_next = False
        except BaseException as err:  # pylint:disable=broad-except
            log.error("[Shell handler] Unexpected error: {err}", err=err)
            # Raising the exception ends up getting swallowed by the finally block.
        if call_next:
            return t_cast(LRESULT, CallNextHookEx(hook_id, code, wparam, lparam))
        # print("Canceling callback chain")
        # From the docs:
        # If the hook procedure processed the message, it may return
        # a nonzero value to prevent the system from passing the
        # message to the rest of the hook chain or the target window
        # procedure.
        return LRESULT(1)

    callback_pointer = HOOK_CALLBACK_TYPE(shell_handler)
    hook_id = t_cast(HHOOK, SetWindowsHookExW(WH_SHELL, callback_pointer, hmod, 0))
    if hook_id == 0:
        return WindowsReturnError.stdret('user32.SetWindowsHookExW / shell')
    log.trace("started shell hook {hook}", hook=repr(hook_id))
    _CALLBACK_POINTERS[hook_id] = callback_pointer

    # Ensure that the hook is *always* uninstalled at exit to prevent OS
    # resource leaks.
    atexit.register(shell__unhook, hook_id)

    return StdRet.pass_ok(hook_id)


def shell__unhook(hook_id: HHOOK) -> None:
    """Remove a windows hook."""
    UnhookWindowsHookEx(hook_id)
    if hook_id in _CALLBACK_POINTERS:
        del _CALLBACK_POINTERS[hook_id]


class MOUSEINPUT(Structure):
    """Part of the INPUT structure.
    see https://msdn.microsoft.com/en-us/library/ms646270(v=vs.85).aspx
    see https://msdn.microsoft.com/en-us/library/ms646271(v=vs.85).aspx"""
    _fields_ = [
        ('dx', c_long),
        ('dy', c_long),
        ('mouseData', c_long),
        ('dwFlags', c_long),
        ('time', c_long),
        ('dwExtraInfo', POINTER(c_ulong))
    ]


class KEYBDINPUT(Structure):
    """Part of the INPUT structure.
    see https://msdn.microsoft.com/en-us/library/ms646270(v=vs.85).aspx
    see https://msdn.microsoft.com/en-us/library/ms646271(v=vs.85).aspx"""
    _fields_ = [
        ('wVk', c_short),
        ('wScan', c_short),
        ('dwFlags', c_long),
        ('time', c_long),
        ('dwExtraInfo', POINTER(c_ulong))
    ]


class HARDWAREINPUT(Structure):
    """Part of the INPUT structure.
    see https://msdn.microsoft.com/en-us/library/ms646270(v=vs.85).aspx
    see https://msdn.microsoft.com/en-us/library/ms646271(v=vs.85).aspx"""
    _fields_ = [
        ('uMsg', c_long),
        ('wParamL', c_short),
        ('wParamH', c_short)
    ]


class INPUTUNION(c_Union):
    """Part of the INPUT structure.
    see https://msdn.microsoft.com/en-us/library/ms646270(v=vs.85).aspx
    see https://msdn.microsoft.com/en-us/library/ms646271(v=vs.85).aspx"""
    _fields_ = [
        ('mi', MOUSEINPUT),
        ('ki', KEYBDINPUT),
        ('hi', HARDWAREINPUT)
    ]


class INPUT(Structure):
    """The INPUT structure.
    see https://msdn.microsoft.com/en-us/library/ms646270(v=vs.85).aspx
    see https://msdn.microsoft.com/en-us/library/ms646271(v=vs.85).aspx"""
    _fields_ = [
        ('type', c_long),
        ('value', INPUTUNION)
    ]


def shell__inject_input_vks(codes: Sequence[Tuple[int, bool]]) -> bool:
    """Inject multiple vk codes into the keyboard buffer."""
    count = len(codes)

    # The inefficient form, but works if the "correct" version goes bonkers.
    # success_count = 0
    # for vk_code, is_key_up in codes:
    #     flag = 0
    #     if is_key_up:
    #         flag = KEYEVENTF_KEYUP
    #     inp = INPUT(type=INPUT_KEYBOARD, value=INPUTUNION(ki=KEYBDINPUT(
    #         wVk=vk_code,
    #         dwFlags=flag,
    #         time=0,
    #         dwExtraInfo=None,
    #     )))
    #     res = t_cast(UINT, windll.user32.SendInput(1, byref(inp), c_sizeof(INPUT)))
    #     success_count += res
    #     print(" - send input {0} / {1} returned {2}".format(vk_code, is_key_up, res))
    #     if res != 1:
    #         print(" - error: {0}".format(GetLastError()))

    inp_list = (INPUT * count)()
    i = 0
    for vk_code, is_key_up in codes:
        # pylint doesn't understand structures
        inp_list[i].type = INPUT_KEYBOARD  # pylint:disable=attribute-defined-outside-init
        # inp.wScan = scancode  # pylint:disable=attribute-defined-outside-init
        # Scan codes also need to know about the 0xe0 extended key sequence.
        # if is_key_up:
        #     inp.dwFlags = KEYEVENTF_SCANCODE | KEYEVENTF_KEYUP
        # else:
        #     inp.dwFlags = KEYEVENTF_SCANCODE
        inp_list[i].value.ki.wVk = vk_code
        if is_key_up:
            inp_list[i].value.ki.dwFlags = KEYEVENTF_KEYUP  # pylint:disable=attribute-defined-outside-init
        else:
            inp_list[i].value.ki.dwFlags = 0  # pylint:disable=attribute-defined-outside-init
        i += 1

    success_count = t_cast(UINT, windll.user32.SendInput(
        count,
        # c_cast(inp_list, POINTER(INPUT_KEYBOARD)),
        inp_list,
        c_sizeof(INPUT)))
    # print(" - send input returned {0}".format(success_count))
    # if success_count != count:
    #     print(" - error: {0}".format(GetLastError()))

    return success_count == count


def shell__lock_workstation() -> bool:
    """Lock the workstation."""
    res = t_cast(BOOL, windll.user32.LockWorkStation())
    return res.value != 0


def shell__register_window_hook(
        hwnd: HWND,
        message_id_callbacks: Optional[Dict[int, MessageCallback]] = None,
        callback: Optional[MessageCallback] = None,
) -> StdRet[int]:
    """
    Registers the "shell hook" window message with the window, and inserts the
    callback into the message_id_callbacks dict for processing, because
    the message ID is dynamically created.

    :param hwnd:
    :param message_id_callbacks:
    :param callback:
    :return: the message ID for the shell hook message.
    """
    if RegisterShellHookWindow(hwnd) == 0:
        return WindowsReturnError.stdret('user32.RegisterShellHookWindow')
    message_id = t_cast(int, RegisterWindowMessageW("SHELLHOOK"))
    if message_id == 0:
        return WindowsReturnError.stdret('user32.RegisterWindowMessageW')
    if message_id_callbacks is not None and callback:
        log.debug("window hook message {mid}", mid=message_id)
        message_id_callbacks[message_id] = callback
    return StdRet.pass_ok(message_id)


def shell__create_global_message_handler(
        message_id_callbacks: Dict[int, MessageCallback],
) -> NativeMessageCallback:
    """
    Create a callback function.  It handles close and destroy messages,
    and forwarding messages.  The called-in dictionary is not cloned, so it
    can be modified after initial call to change which messages are being
    handled; take note to only modify this structure from within the
    message handling thread to avoid thread safety issues.

    :param message_id_callbacks: a dictionary that stores a mapping
        between the message ID (uint) and a callback that handles
        that message.  The callback takes 4 parameters:
        hwnd of the window that received the message,
        the message ID (uint), the wparam, and the lparam
        (which are both message specific interpreted).
    :return: the constructed handler callback.
    """
    def handler(hwnd: HWND, message: int, wparam: WPARAM, lparam: LPARAM) -> int:
        # This handler must be highly optimized.  No fluff where it isn't needed.
        log.trace(
            "gmh: handling hwnd message 0x{m:08x} 0x{w:08x} 0x{l:08x}",
            m=message, w=wparam, l=lparam,
        )
        if message in message_id_callbacks:
            ret = message_id_callbacks[message](hwnd, message, wparam, lparam)
            if ret is not False:
                return 1
            # False return code means run the standard DefWindowProc.
        elif message == WM_CLOSE:
            log.trace('gmh: hwnd close message triggering DestroyWindow call')
            windll.user32.DestroyWindow(hwnd)
            return 0
        elif message == WM_DESTROY:
            log.trace('gmh: hwnd destroy message triggering PostQuitMessage call')
            windll.user32.PostQuitMessage(0)
            return 0
        else:
            log.trace('gmh: did not handle message.')

        # MyPy requirement.
        return t_cast(int, DefWindowProcW(hwnd, message, wparam, lparam))

    return handler


def shell__pump_messages(on_exit_callback: Callable[[], None]) -> None:
    """Process the next window message."""
    message = MSG()
    log.trace("shell__pump_messages start")
    while True:
        log.trace("shell__pump_messages getting messages")
        msg = GetMessageW(byref(message), 0, 0, 0)
        # log.trace(
        #     "shell__pump_messages {msg:04x}: h {h:04x}; m {m:04x}; w {w:04x}; l: {l:04x}",
        #     msg=msg, h=message.hWnd, m=message.message, w=message.wParam, l=message.lParam,
        # )
        if msg <= 0:
            log.trace("quit message in queue ({value})", value=msg)
            # 0 means WM_QUIT, < 0 means error
            on_exit_callback()
            # Is this right?
            break
        TranslateMessage(byref(message))
        DispatchMessageW(byref(message))
    log.trace("shell__pump_messages stopped")


# Maps the key to the (getter, setter, type, is pv_param?)
_SYSTEM_PARAMETER_MAPPING: Dict[
    str, Tuple[int, int, Type[Union[UINT, DWORD, BOOL, ANIMATIONINFO]], bool],
] = {
    "focus-border-height": (SPI_GETFOCUSBORDERHEIGHT, SPI_SETFOCUSBORDERHEIGHT, UINT, True),
    "focus-border-width": (SPI_GETFOCUSBORDERWIDTH, SPI_SETFOCUSBORDERWIDTH, UINT, True),
    "menu-drop-alignment": (SPI_GETMENUDROPALIGNMENT, SPI_SETMENUDROPALIGNMENT, BOOL, False),
    "menu-fade": (SPI_GETMENUFADE, SPI_SETMENUFADE, BOOL, True),
    "menu-show-delay": (SPI_GETMENUSHOWDELAY, SPI_SETMENUSHOWDELAY, DWORD, False),
    "combobox-animation": (SPI_GETCOMBOBOXANIMATION, SPI_SETCOMBOBOXANIMATION, BOOL, True),
    "cursor-shadow": (SPI_GETCURSORSHADOW, SPI_SETCURSORSHADOW, BOOL, True),
    "gradient-titles": (SPI_GETGRADIENTCAPTIONS, SPI_SETGRADIENTCAPTIONS, BOOL, True),
    "hot-tracking": (SPI_GETHOTTRACKING, SPI_SETHOTTRACKING, BOOL, True),
    "listbox-smooth-scrolling": (
        SPI_GETLISTBOXSMOOTHSCROLLING, SPI_SETLISTBOXSMOOTHSCROLLING, BOOL, True,
    ),
    "menu-animation": (SPI_GETMENUANIMATION, SPI_SETMENUANIMATION, BOOL, True),
    "menu-underlines": (SPI_GETMENUUNDERLINES, SPI_SETMENUUNDERLINES, BOOL, True),
    "selection-fade": (SPI_GETSELECTIONFADE, SPI_SETSELECTIONFADE, BOOL, True),
    "tooltip-animation": (SPI_GETTOOLTIPANIMATION, SPI_SETTOOLTIPANIMATION, BOOL, True),
    "tooltip-fade": (SPI_GETTOOLTIPFADE, SPI_SETTOOLTIPFADE, BOOL, True),
    "ui-effects": (SPI_GETUIEFFECTS, SPI_SETUIEFFECTS, BOOL, True),
    "active-window-tracking": (
        SPI_GETACTIVEWINDOWTRACKING, SPI_SETACTIVEWINDOWTRACKING, BOOL, True,
    ),
    "active-window-tracking-zorder": (
        SPI_GETACTIVEWNDTRKZORDER, SPI_SETACTIVEWNDTRKZORDER, BOOL, True,
    ),
    "active-window-tracking-timeout": (
        SPI_GETACTIVEWNDTRKTIMEOUT, SPI_SETACTIVEWNDTRKTIMEOUT, DWORD, True,
    ),
    "animation": (SPI_GETANIMATION, SPI_SETANIMATION, ANIMATIONINFO, True),  # special case
    "border": (SPI_GETBORDER, SPI_SETBORDER, UINT, False),
}


def shell__system_parameters_info(  # pylint:disable=too-many-branches
        values: Dict[str, Union[int, bool, ANIMATIONINFO]],
) -> Dict[str, Union[int, bool, ANIMATIONINFO, WindowsReturnError]]:
    """
    Sets the values (a dictionary of system parameters to their values), and
    for every value set, it is retrieved first and returned in a corresponding
    object (for easy restoring of values).  If the value is None, then the
    value is just collected.

    If collecting the information caused an issue, then the returned value
    for that parameter is an OSError.

    :param values:
    :return: the original values
    """
    ret: Dict[str, Union[int, bool, ANIMATIONINFO, WindowsReturnError]] = {}
    for parameter, value in values.items():
        if parameter in _SYSTEM_PARAMETER_MAPPING:
            # get
            val = _SYSTEM_PARAMETER_MAPPING[parameter][2]()
            ui_param: UINT = UINT(0)
            if _SYSTEM_PARAMETER_MAPPING[parameter][2] == ANIMATIONINFO:
                ui_param = UINT(c_sizeof(ANIMATIONINFO))
                t_cast(ANIMATIONINFO, val).cbSize = c_sizeof(ANIMATIONINFO)
            res = SystemParametersInfoW(
                _SYSTEM_PARAMETER_MAPPING[parameter][0],
                ui_param, byref(val), 0,
            )
            if res == 0:
                # "If the function fails, the return value is zero"
                ret[parameter] = WindowsReturnError('user32.SystemParametersInfoW(sys params)')
                continue
            if _SYSTEM_PARAMETER_MAPPING[parameter][2] == BOOL:
                ret[parameter] = val == 0
            elif _SYSTEM_PARAMETER_MAPPING[parameter][2] == ANIMATIONINFO:
                ret[parameter] = t_cast(ANIMATIONINFO, val)
            else:
                ret[parameter] = val.value

            # set
            pv_param = None
            ui_param = UINT(0)
            # Should convert from py type to c type correctly.
            if _SYSTEM_PARAMETER_MAPPING[parameter][2] == ANIMATIONINFO:
                ui_param = UINT(c_sizeof(ANIMATIONINFO))
                val = ANIMATIONINFO()
                val.cbSize = c_sizeof(ANIMATIONINFO)
                val.iMinAnimate = value
                pv_param = byref(val)
            elif isinstance(value, (int, bool)):
                val = _SYSTEM_PARAMETER_MAPPING[parameter][2](value)
                if _SYSTEM_PARAMETER_MAPPING[parameter][3]:
                    pv_param = byref(val)
                else:
                    ui_param = t_cast(UINT, val)  # Implicit type based on the mapping.
            # else ignore it; it shouldn't have happened.
            res = SystemParametersInfoW(
                _SYSTEM_PARAMETER_MAPPING[parameter][0],
                ui_param, pv_param, WM_SETTINGCHANGE,
            )
            if res != 0:
                log.error("CLIENT ERROR: failed to set system parameter {p}", p=parameter)
        else:
            log.error("CLIENT ERROR: Unknown system parameter {p}", p=parameter)
    return ret


def shell__set_sys_colors() -> None:
    """Set the system colors."""
    raise NotImplementedError


class MONITORINFOEXW(Structure):
    """The MONITORINFOEXW structure.
    see https://docs.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-monitorinfo
    see https://docs.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-monitorinfoexw"""
    _fields_ = (
        ("cbSize", DWORD),
        ("rcMonitor", RECT),
        ("rcWork", RECT),
        ("dwFlags", DWORD),
        # TODO test this out.  It should be at the end, but don't know for sure.
        ("szDevice", WCHAR * CCHDEVICENAME),
    )


def monitor__find_monitors() -> Sequence[WindowsMonitor]:
    """Find the monitors in the system."""
    monitor_handles: List[Tuple[HMONITOR, LONG, LONG, LONG, LONG]] = []

    def callback(
            h_monitor: HMONITOR, _hdc_monitor: HDC, lprc_monitor: LPRECT, _l_param: LPARAM,
    ) -> bool:
        # hMonitor: display monitor handle
        # hdcMonitor: device context handle; color attributes + clipping region; may be null
        # lprcMonitor: RECT structure w/ device-context coordinates.
        monitor_handles.append((
            h_monitor,
            lprc_monitor.contents.left, lprc_monitor.contents.right,
            lprc_monitor.contents.top, lprc_monitor.contents.bottom,
        ))
        return True

    enum_monitor_proc = WINFUNCTYPE(c_bool, HMONITOR, HDC, LPRECT, LPARAM)
    if EnumDisplayMonitors(None, None, enum_monitor_proc(callback), 0) == 0:
        return EMPTY_TUPLE

    ret: List[WindowsMonitor] = []
    index = 0
    for monitor_handle, vd_l, vd_r, vd_t, vd_b in monitor_handles:
        info = MONITORINFOEXW()
        # pylint is confused by some uses of structures.
        info.cbSize = c_sizeof(MONITORINFOEXW)  # pylint:disable=attribute-defined-outside-init
        if GetMonitorInfoW(monitor_handle, byref(info)) != 0:
            ret.append(WindowsMonitor(
                monitor_handle=monitor_handle,
                monitor_index=index,

                monitor_left=info.rcMonitor.left,
                monitor_right=info.rcMonitor.right,
                monitor_top=info.rcMonitor.top,
                monitor_bottom=info.rcMonitor.bottom,

                work_left=info.rcWork.left,
                work_right=info.rcWork.right,
                work_top=info.rcWork.top,
                work_bottom=info.rcWork.bottom,

                vd_left=vd_l.value,
                vd_right=vd_r.value,
                vd_top=vd_t.value,
                vd_bottom=vd_b.value,

                name=info.szDevice,
                is_primary=(info.dwFlags & MONITORINFOF_PRIMARY) == 1,

                # Generic versions of Windows does not support these API queries.
                # Default for an unknown DPI is 96.  It just is.
                scale_factor=100,
                dpi_x=96,
                dpi_y=96,
            ))
        index += 1

    return ret


def process__get_exit_code(thread_pid: DWORD) -> Optional[int]:
    """

    :param thread_pid:
    :return: None if the process hasn't exited, or the int exit code.
    """
    hproc = windll.kernel32.OpenProcess(
        PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, thread_pid,
    )
    try:
        exit_code = DWORD()
        if GetExitCodeProcess(hproc, byref(exit_code)) != 0:
            if exit_code == STILL_ACTIVE:
                return None
            return exit_code.value
        return None
    finally:
        windll.kernel32.CloseHandle(hproc)


def process__get_window_state(thread_pid: DWORD) -> StdRet[WindowsWindowState]:
    """Get the thread PID's window state."""
    gui_info = GUITHREADINFO()
    gui_info.cbSize = c_sizeof(gui_info)
    res = windll.user32.GetGUIThreadInfo(thread_pid, byref(gui_info))
    if res == 0:
        return WindowsReturnError.stdret('user32.GetGUIThreadInfo')
    return StdRet.pass_ok(create_windows_window_state(gui_info))


def process__get_current_pid() -> DWORD:
    """Get the current process' pid."""
    return t_cast(DWORD, windll.kernel32.GetCurrentProcessId())


def _attach_message_queue_to_thread(current_hwnd: HWND) -> StdRet[None]:
    current_thread_id = windll.kernel32.GetCurrentThreadId()
    thread_process_id = windll.user32.GetWindowThreadProcessId(current_hwnd, None)
    if thread_process_id != current_thread_id:
        res = windll.user32.AttachThreadInput(thread_process_id, current_thread_id, True)
        # ERROR_INVALID_PARAMETER means that the two threads are already attached.
        if res == 0:
            err = WindowsReturnError('user32.AttachThreadInput')
            if err.errno != ERROR_INVALID_PARAMETER:
                # print(f"WARN: could not attach thread input to thread
                # f"{thread_process_id} ({GetLastError()})")
                return StdRet.pass_error(err)
    windll.user32.AttachThreadInput(thread_process_id, current_thread_id, False)
    return RET_OK_NONE
