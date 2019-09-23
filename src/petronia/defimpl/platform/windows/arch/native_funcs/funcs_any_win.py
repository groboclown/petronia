
"""
Windows functions for any architecture or supported version.
"""

from typing import Dict, Sequence, List, Iterable, Callable, Optional, Tuple, Type, Union, Any
from typing import cast as t_cast
import sys
from ctypes import sizeof as c_sizeof
from ctypes import cast as c_cast
import atexit
from ctypes import (
    CFUNCTYPE,
    POINTER,
    byref,
    c_int,
    c_uint,
    c_void_p,
    c_long,
    c_bool,
    create_unicode_buffer,
    Structure,
)
from .windows_common import (
    WINFUNCTYPE, ANIMATIONINFO,
    windll, WindowsErrorMessage, GetLastError,
    LPCWSTR, LPVOID, LPRECT,
    DWORD, WORD, BOOL, BYTE, UINT, WCHAR, SHORT, LRESULT, WINTYPE_SIZE,
    COLORREF, RECT, POINT, RGB, HFONT, HDC,
    HWND, HMENU, HMODULE, HINSTANCE, HANDLE, HMONITOR,
    MSG, WPARAM, LPARAM, HHOOK, GUITHREADINFO,
    MessageCallback, NativeMessageCallback,
)
from ..windows_constants import (
    PETRONIA_CREATED_WINDOW__CLASS_PREFIX,
    MAX_CLASS_NAME_LENGTH,
    MAX_FILENAME_LENGTH,
    RDW_INTERNALPAINT, RDW_ERASE, RDW_ALLCHILDREN, RDW_FRAME, RDW_INVALIDATE,
    SW_MINIMIZE, SW_RESTORE, SW_SHOW, SW_HIDE, SW_MAXIMIZE, SW_SHOWNA,
    SW_SHOWNORMAL, SW_SHOWMINIMIZED, SW_SHOWMAXIMIZED, SW_SHOWNOACTIVATE, SW_SHOWMINNOACTIVE,
    HWND_TOPMOST, HWND_NOTOPMOST, HWND_DESKTOP,
    SWP_NOSIZE, SWP_NOMOVE,
    PROCESS_QUERY_INFORMATION, PROCESS_VM_READ,
    WM_CLOSE, WM_DESTROY, WH_SHELL, WM_SETTINGCHANGE,
    PS_SOLID, PS_GEOMETRIC, BS_NULL, HS_DIAGCROSS, OPAQUE, TRANSPARENT,
    DT_LEFT, DT_TOP, DT_NOPREFIX,
    LWA_ALPHA, COLOR_WINDOW,
    KEYEVENTF_SCANCODE, KEYEVENTF_KEYUP,
    FW_NORMAL, FW_BOLD, DEFAULT_CHARSET, OUT_TT_PRECIS, CLIP_DEFAULT_PRECIS, PROOF_QUALITY, FF_DONTCARE,
    LOGPIXELSY, MONITORINFOF_PRIMARY,
    IDI_APPLICATION, IDC_ARROW, CW_USEDEFAULT,
    WS_OVERLAPPEDWINDOW, STILL_ACTIVE,
    LLHKF_UP, LLHKF_UP, LLKHF_INJECTED, LLKHF_INJECTED, WH_KEYBOARD_LL,
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
from .supported_functions import (
    Functions,
    PaintCallback,
)
from .color import to_rgb
from .window_state import (
    WindowsWindowState,
    create_windows_window_state,
    convert_rect,
)
from ......core.platform.api import (
    ScreenRect,
    ScreenSize,
    Color,
    NativeScreenInfo,
)
from ......base.util import T


def load_functions(_: Dict[str, str], func_map: Functions) -> None:
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
    func_map.shell.inject_scancode = shell__inject_scancode
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


def window__enum_window_handles(callback: Callable[[HWND], bool]) -> None:

    # noinspection PyUnusedLocal
    def callback_wrapper(hwnd: HWND, lparam: Any) -> bool:
        return callback(hwnd)

    enum_win_proc = WINFUNCTYPE(c_bool, c_int, POINTER(c_int))
    windll.user32.EnumWindows(enum_win_proc(callback_wrapper), None)


def window__find_handle_for_class_title(class_name: str, title: str) -> Optional[HWND]:
    return t_cast(HWND, windll.user32.FindWindowW(class_name, title))


def window__find_handle_for_child_class_title(
        hwnd_parent: HWND, hwnd_child_after: Optional[HWND], class_name: str, title: str
) -> Optional[HWND]:
    return t_cast(HWND, windll.user32.FindWindowExW(hwnd_parent, hwnd_child_after, class_name, title))


def window__get_title(hwnd_handle: HWND) -> str:
    length = windll.user32.GetWindowTextLengthW(hwnd_handle)
    if length > 0:
        buff = create_unicode_buffer(length + 1)
        windll.user32.GetWindowTextW(hwnd_handle, buff, length + 1)
        return buff.value
    return ""


def window__is_visible(hwnd_handle: HWND) -> bool:
    val = t_cast(int, windll.user32.IsWindowVisible(hwnd_handle))
    return val != 0


def window__get_process_id(hwnd_handle: HWND) -> DWORD:
    pid = DWORD()
    # thread_pid =
    windll.user32.GetWindowThreadProcessId(hwnd_handle, byref(pid))
    return pid


def window__get_class_name(hwnd_handle: HWND) -> Union[WindowsErrorMessage, str]:
    buff = create_unicode_buffer(MAX_CLASS_NAME_LENGTH + 1)
    size = windll.user32.GetClassNameW(hwnd_handle, buff, MAX_CLASS_NAME_LENGTH + 1)
    if size <= 0:
        return WindowsErrorMessage('user32.GetClassNameW')
    return buff.value[:size]


def window__get_module_filename(hwnd_handle: HWND) -> Union[WindowsErrorMessage, str]:
    buff = create_unicode_buffer(MAX_FILENAME_LENGTH + 1)
    size = windll.user32.GetWindowModuleFileNameW(hwnd_handle, buff, MAX_FILENAME_LENGTH + 1)
    if size <= 0:
        return WindowsErrorMessage('user32.GetWindowModuleFileNameW')
    return buff.value[:size]


def window__get_thread_window_handles(thread_process_id: DWORD) -> Sequence[HWND]:
    """

    :param thread_process_id: thread process ID, as from window__get_thread_process_id
    :return: hwnd for all top-level windows with this thread process id.
    """
    ret: List[HWND] = []

    def callback(hwnd: HWND, _: LPARAM) -> bool:
        ret.append(hwnd)
        return True

    enum_win_proc = WINFUNCTYPE(c_bool, POINTER(c_int), POINTER(c_int))
    windll.user32.EnumThreadWindows(thread_process_id, enum_win_proc(callback), None)

    return ret


def window__get_child_window_handles(hwnd_parent: HWND) -> Sequence[HWND]:
    ret: List[HWND] = []

    def callback(hwnd: HWND, _: LPARAM) -> bool:
        ret.append(hwnd)
        return True

    enum_win_proc = WINFUNCTYPE(c_bool, POINTER(c_int), POINTER(c_int))
    windll.user32.EnumChildWindows(hwnd_parent, enum_win_proc(callback), None)

    return ret


def window__border_rectangle(hwnd: HWND) -> Union[WindowsErrorMessage, ScreenRect]:
    """
    The outer border size and position of the window

    :param hwnd:
    :return: a ScreenRect, or None if not found.
    """
    rect = RECT()
    res = windll.user32.GetWindowRect(hwnd, byref(rect))
    if res == 0:
        return WindowsErrorMessage('user32.GetWindowRect')
    return convert_rect(rect)


def window__client_rectangle(hwnd: HWND) -> Union[WindowsErrorMessage, ScreenRect]:
    """
    The client-usable space within the border rectangle.  Top and Left
    are always 0.

    :param hwnd:
    :return: the rectangle structure, or None
    """
    client_rect = RECT()
    res = windll.user32.GetClientRect(hwnd, byref(client_rect))
    if res == 0:
        return WindowsErrorMessage('user32.GetClientRect')
    return convert_rect(client_rect)


def window__move_resize(
        hwnd: HWND, x: int, y: int, width: int, height: int,
        repaint: Optional[bool] = True
) -> bool:
    """
    Move and resize the window.
    """

    ret = t_cast(BOOL, windll.user32.MoveWindow(hwnd, x, y, width, height, repaint))

    # check that it worked correctly?

    return ret != 0


def window__redraw(hwnd: HWND, force: Optional[bool] = False) -> bool:
    # window__wait_gui_thread_idle(hwnd)
    # res = windll.user32.ChangeWindowMessageFilterEx(hwnd, WM_PAINT, 1, None)
    # res = windll.user32.UpdateWindow(hwnd)
    res = windll.user32.RedrawWindow(
        hwnd, None, None,
        RDW_INTERNALPAINT | RDW_ERASE | RDW_ALLCHILDREN | RDW_FRAME)
    if res != 0:
        # Successful!
        return True

    # None of the above worked, probably because the process isolation doesn't allow
    # our process to send a message to another process.

    # So, try minimize then restore (if maximized, it will restore itself again)
    # This really messes up the z-ordering, though.
    if force and window__is_visible(hwnd):
        windll.user32.ShowWindow(hwnd, SW_MINIMIZE)
        windll.user32.ShowWindow(hwnd, SW_RESTORE)
        return True

    return False


def window__repaint(hwnd: HWND) -> Optional[WindowsErrorMessage]:
    # res = windll.user32.InvalidateRect(hwnd, None, False)
    res = windll.user32.RedrawWindow(hwnd, None, None, RDW_INVALIDATE)
    if res == 0:
        return WindowsErrorMessage('user32.RedrawWindow')
    return None


def window__wait_gui_thread_idle(hwnd: HWND, timeout: Optional[int] = 1000) -> Optional[WindowsErrorMessage]:
    thread_pid = window__get_process_id(hwnd)
    if thread_pid:
        hproc = windll.kernel32.OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, thread_pid)
        try:
            res = windll.user32.WaitForInputIdle(hproc, timeout)
            # == 0: wait okay.
            # == WAIT_TIMEOUT: wait timed out
            # == WAIT_FAILED: error occurred
            if res != 0:
                return WindowsErrorMessage('user32.WaitForInputIdle')
        finally:
            windll.kernel32.CloseHandle(hproc)
    windll.user32.WaitGuiThreadIdle(hwnd)
    return None


def window__send_message(hwnd: HWND, key: UINT, arg1: WPARAM, arg2: LPARAM) -> Union[WindowsErrorMessage, LRESULT]:
    err = _attach_message_queue_to_thread(hwnd)
    if err:
        return err
    return t_cast(LRESULT, windll.user32.SendMessageW(hwnd, key, arg1, arg2))


def window__post_message(hwnd: HWND, key: UINT, arg1: WPARAM, arg2: LPARAM) -> Optional[WindowsErrorMessage]:
    err = _attach_message_queue_to_thread(hwnd)
    if err:
        return err
    res = windll.user32.PostMessageW(hwnd, key, arg1, arg2)
    if res == 0:
        return WindowsErrorMessage('user32.PostMessageW')
    return None


def window__close(hwnd: HWND) -> Optional[WindowsErrorMessage]:
    # For a full implementation, see
    # Code modified from http://msdn.microsoft.com/msdnmag/issues/02/08/CQA/

    # Give the "must close" message to the window
    return window__post_message(
        hwnd, UINT(WM_CLOSE), WPARAM(0), LPARAM(0)
    )


def window__maximize(hwnd: HWND) -> Optional[WindowsErrorMessage]:
    res = windll.user32.ShowWindow(hwnd, SW_MAXIMIZE)
    if res == 0:
        return WindowsErrorMessage('user32.ShowWindow')
    return None


def window__minimize(hwnd: HWND) -> Optional[WindowsErrorMessage]:
    res = windll.user32.ShowWindow(hwnd, SW_MINIMIZE)
    if res == 0:
        return WindowsErrorMessage('user32.ShowWindow')
    return None


def window__restore(hwnd: HWND) -> Optional[WindowsErrorMessage]:
    # This needs to be called twice, because of the situation
    # where a window was maximized then minimized.  The first
    # restore will bring it back to visible, but maximized,
    # and the second will bring it to restored.
    # But... the first call will return:
    # "If the window was previously hidden, the return value is zero."
    # So, only call it twice if it was minimized.
    if windll.user32.ShowWindow(hwnd, SW_RESTORE) == 0:
        windll.user32.ShowWindow(hwnd, SW_RESTORE)
    return None


# see https://msdn.microsoft.com/en-us/library/windows/desktop/ms632611(v=vs.85).aspx
class WINDOWPLACEMENT(Structure):
    _fields_ = (
        ("length", UINT),
        ("flags", UINT),
        ("showCmd", UINT),
        ("ptMinPosition", POINT),
        ("ptMaxPosition", POINT),
        ("rcNormalPosition", RECT),
    )


def window__get_visibility_states(hwnd: HWND) -> Sequence[str]:
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
    placement.length = c_sizeof(placement)
    val = windll.user32.GetWindowPlacement(hwnd, byref(placement))
    if val is None:
        return ()
    show_cmd = placement.showCmd
    if show_cmd == SW_HIDE:
        return ('hidden',)
    if show_cmd == SW_SHOWNORMAL:
        return ('shown', 'restored', 'active',)
    if show_cmd == SW_SHOWMINIMIZED:
        return ('shown', 'minimized', 'active',)
    if show_cmd == SW_MAXIMIZE:
        return ('shown', 'maximized', 'active',)
    if show_cmd == SW_SHOWMAXIMIZED:
        return ('shown', 'maximized', 'active',)
    if show_cmd == SW_SHOWNOACTIVATE:
        return ('shown', 'restored',)
    if show_cmd == SW_SHOW:
        return ('shown', 'restored', 'active',)
    if show_cmd == SW_MINIMIZE:
        return ('shown', 'minimized', 'active',)
    if show_cmd == SW_SHOWMINNOACTIVE:
        return ('shown', 'minimized',)
    if show_cmd == SW_SHOWNA:
        return ('shown', 'restored',)
    if show_cmd == SW_RESTORE:
        return ('shown', 'restored', 'active',)
    return ()


class LOGBRUSH(Structure):
    _fields_ = (
        # VC98/Include/wingdi.h 1025
        ('lbStyle', c_uint),
        ('lbColor', DWORD),  # COLORREF
        ('lbHatch', c_long),
    )


def window__draw_border_outline(
        rect: ScreenRect,
        color: Color,
        width: int,
        line_style: Optional[int] = PS_SOLID,
        fill_style: Optional[int] = BS_NULL,
        parent_hwnd: Optional[HWND] = None
) -> None:
    """
    Draws a border on the screen.  Does not need a window context.

    :param fill_style:
    :param line_style:
    :param rect: border to draw
    :param color: Petronia color
    :param width:
    :param line_style:
    :param parent_hwnd: handle of the parent window, if any.
    :return:
    """
    pen_handle = None
    brush_handle = None
    dc_handle = None
    color_ref = to_rgb(color)

    try:
        # Pen == outside drawing definition
        pen_handle = windll.gdi32.CreatePen(line_style, width, color_ref)

        # Brush == inside
        brush_def = LOGBRUSH()
        # BS_NULL so that the fill is empty
        brush_def.lbStyle = fill_style
        brush_def.lbHatch = HS_DIAGCROSS
        brush_def.lbColor = color_ref
        brush_handle = windll.gdi32.CreateBrushIndirect(byref(brush_def))

        # Create a device context to draw on
        dc_handle = windll.gdi32.CreateDCW("DISPLAY", None, None, None)
        windll.gdi32.SelectObject(dc_handle, brush_handle)
        windll.gdi32.SelectObject(dc_handle, pen_handle)

        # FIXME EXPERIMENTAL CODE
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
        # FIXME EXPERIMENTAL CODE

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
        x: int, y: int,
        width: int, height: int,
        flags: Iterable[str]
) -> Optional[WindowsErrorMessage]:
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
            # TODO better error
            print("Unknown SWP set position flag {0}".format(flag))
    res = SetWindowPos(hwnd, zorder, x, y, width, height, uflags)
    if res == 0:
        return WindowsErrorMessage('user32.SetWindowPos')
    return None


# TODO use the Color object.
def window__set_layered_attributes(hwnd: HWND, r: int, g: int, b: int, a: int) -> Optional[WindowsErrorMessage]:
    res = SetLayeredWindowAttributes(hwnd, RGB(r, g, b), a, LWA_ALPHA)
    if res == 0:
        return WindowsErrorMessage('user32.SetLayeredWindowAttributes')
    return None


def window__get_active_window() -> Optional[HWND]:
    # GetActiveWindow is only for the current thread.
    # It usually just returns None.
    hwnd = t_cast(HWND, windll.user32.GetForegroundWindow())
    if hwnd == 0:
        return None
    return hwnd


def window__activate(hwnd: HWND) -> Optional[WindowsErrorMessage]:
    # Give the window the focus.  This is the Microsoft Magic Focus Dance.
    current_hwnd = windll.user32.GetForegroundWindow()
    current_thread_id = windll.kernel32.GetCurrentThreadId()
    thread_process_id = windll.user32.GetWindowThreadProcessId(current_hwnd, None)
    if thread_process_id != current_thread_id:
        res = windll.user32.AttachThreadInput(thread_process_id, current_thread_id, True)
        # ERROR_INVALID_PARAMETER means that the two threads are already attached.
        if res == 0:
            err = WindowsErrorMessage('user32.AttachThreadInput')
            if err.errno != ERROR_INVALID_PARAMETER:
                # "WARN: could not attach thread input to thread {0} ({1})".format(thread_process_id, GetLastError())
                return err
    res = windll.user32.SetWindowPos(hwnd, HWND_TOPMOST, 0, 0, 0, 0, SWP_NOSIZE | SWP_NOMOVE)
    if res == 0:
        return WindowsErrorMessage('user32.SetWindowPos')
    # At this point, the window hwnd is valid, so we don't need to fail out
    # if the results are non-zero.  Some of these will not succeed due to
    # attributes of the window, rather than the window not existing.
    windll.user32.SetWindowPos(hwnd, HWND_NOTOPMOST, 0, 0, 0, 0, SWP_NOSIZE | SWP_NOMOVE)
    windll.user32.AttachThreadInput(thread_process_id, current_thread_id, False)
    windll.user32.SetForegroundWindow(hwnd)
    windll.user32.SetFocus(hwnd)
    windll.user32.SetActiveWindow(hwnd)
    return None


class WNDCLASSEX(Structure):
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
        ("hIconSm", HANDLE)
    ]


def window__create_message_window(
        class_name: str, message_handler: NativeMessageCallback
) -> Union[HWND, WindowsErrorMessage]:
    """
    Create a "message" window - a window that's only for posting messages
    to, and for handling other OS messages.

    However, some broadcast messages we need, like WM_DISPLAYCHANGE.
    Therefore, it needs to be a real window that is just never shown.

    :param message_handler: the handler procedure created by shell__create_global_message_handler
    :param class_name: unique class name for the window
    :return: hwnd
    """

    if not class_name.startswith(PETRONIA_CREATED_WINDOW__CLASS_PREFIX):
        class_name = PETRONIA_CREATED_WINDOW__CLASS_PREFIX + class_name

    # A persistent pointer to a handler.  Must be persisted so it isn't
    # removed when we exit this method.
    # print("creating a windows procedure for " + repr(message_handler))
    window_proc = WNDPROCTYPE(message_handler)
    hinst = GetModuleHandleW(None)
    window_class = WNDCLASSEX()
    window_class.cbSize = c_sizeof(WNDCLASSEX)
    window_class.style = 0
    window_class.lpfnWndProc = window_proc
    window_class.cbClsExtra = 0
    window_class.cbWndExtra = 0
    window_class.hInstance = hinst
    window_class.hIcon = 0
    window_class.hCursor = 0
    window_class.hBrush = 0
    window_class.lpszMenuName = 0
    window_class.lpszClassName = class_name
    window_class.hIconSm = 0

    if not RegisterClassExW(byref(window_class)):
        return WindowsErrorMessage('user32.RegisterClassExW')
    # Top level, never viewed, window.  Note that we set title to
    # "null" to further emphasize that this is a non-viewable window.
    # We don't use a message-only window, so that the window can
    # receive global event hooks.
    hwnd: HWND = CreateWindowExW(
        0, class_name, None,
        WS_OVERLAPPEDWINDOW, 0, 0, 0, 0, HWND_DESKTOP, None, hinst, None
    )
    if hwnd is None or hwnd == 0:
        return WindowsErrorMessage('user32.CreateWindowExW')

    _CALLBACK_POINTERS[hwnd] = window_proc
    return hwnd


def window__create_display_window(
        class_name: str,
        title: str,
        message_handler: MessageCallback,
        style_flags: Iterable[str]
) -> Union[HWND, WindowsErrorMessage]:
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
    window_class.cbSize = c_sizeof(WNDCLASSEX)
    window_class.style = 0
    window_class.lpfnWndProc = window_proc
    window_class.cbClsExtra = 0
    window_class.cbWndExtra = 0
    window_class.hInstance = hinst
    window_class.hIcon = app_icon
    window_class.hCursor = cursor_icon
    window_class.hBrush = COLOR_WINDOW + 1
    window_class.lpszMenuName = 0
    window_class.lpszClassName = class_name
    window_class.hIconSm = small_icon

    if not RegisterClassExW(byref(window_class)):
        return WindowsErrorMessage('user32.RegisterClassExW')

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
        None,  # HWND_DESKTOP,
        None, hinst, None
    ))
    if hwnd is None or hwnd == 0:
        return WindowsErrorMessage('user32.CreateWindowExW')
    windll.user32.ShowWindow(hwnd, SW_SHOWNORMAL)
    windll.user32.UpdateWindow(hwnd)

    _CALLBACK_POINTERS[hwnd] = window_proc
    return hwnd


_FONT_HANDLES: Dict[str, Optional[HFONT]] = {}


def window__get_font_for_description(
        font: str,
        hwnd: Optional[HWND] = None, base_hdc: Optional[HDC] = None
) -> Optional[HFONT]:
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
            elif 'bold' == param or 'b' == param:
                weight = FW_BOLD
            elif 'italic' == param or 'italics' == param or 'i' == param:
                italic = 1
            elif 'underline' == param or 'under' == param or 'u' == param:
                underline = 1
            elif 'strikethrough' == param or 'strikeout' == param or 'strike' == param or 's' == param:
                strikeout = 1

        pixels_per_point_y = windll.gdi32.GetDeviceCaps(hdc, LOGPIXELSY)
        if pixels_per_point_y <= 0:
            pixels_per_point_y = 72
        height = (point * pixels_per_point_y) // 72
        hfont: HANDLE = windll.gdi32.CreateFontW(
            -height, 0, 0, 0,
            weight, italic, underline, strikeout,
            DEFAULT_CHARSET, OUT_TT_PRECIS, CLIP_DEFAULT_PRECIS, PROOF_QUALITY, FF_DONTCARE,
            create_unicode_buffer(font_name))
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
        hwnd: Optional[HWND] = None, base_hdc: Optional[HDC] = None
) -> Union[ScreenSize, WindowsErrorMessage]:
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
                byref(size)
            )
            if res == 0:
                return WindowsErrorMessage('gdi32.GetTextExtentPoint32W')
            height += size.cy.value
            width = max(width, size.cx.value)
        return width, height
    finally:
        # To prevent a memory leak
        if hdc is not None and old_hfont is not None:
            windll.gdi32.SelectObject(hdc, old_hfont)
        if base_hdc is None and created_hdc is None:
            windll.user32.ReleaseDC(hdc)
        if base_hdc is None and created_hdc is not None:
            windll.gdi32.DeleteDC(hdc)


class PAINTSTRUCT(Structure):
    _fields_ = (
        ("hdc", HANDLE),
        ("fErase", c_bool),
        ("rcPaint", RECT),
        ("fRestore", c_bool),
        ("fIncUpdate", c_bool),
        ("rgbReserved", BYTE * 32),
    )


def window__do_paint(hwnd: HWND, paint_callback: PaintCallback[T]) -> Union[T, WindowsErrorMessage]:
    """
    Start the paint callback message.

    :param hwnd:
    :param paint_callback: function, takes 2 argument: the hwnd, and the hdc of the paint.
    :return: paint_callback return value
    """
    ps = PAINTSTRUCT()
    hdc = windll.user32.BeginPaint(hwnd, byref(ps))
    if hdc == 0 or hdc is None:
        return WindowsErrorMessage('user32.BeginPaint')
    try:
        return paint_callback(hwnd, hdc)
    finally:
        windll.user32.EndPaint(hwnd, byref(ps))


def window__do_draw(hwnd: HWND, paint_callback: PaintCallback[T]) -> Union[T, WindowsErrorMessage]:
    hdc: HDC = windll.user32.GetDC(hwnd)
    if hdc == 0 or hdc is None:
        return WindowsErrorMessage('user32.GetDC')
    try:
        return paint_callback(hwnd, hdc)
    finally:
        windll.user32.ReleaseDC(hdc)


def paint__draw_rect(
        hdc: HDC, pos_x: int, pos_y: int, width: int, height: int, color: Color
) -> Optional[WindowsErrorMessage]:
    # Note: this uses separated out x,y,w,h rather than SceenArea.  That's because
    # the higher level function must convert from virtual screen units to pixels.
    rect = RECT()
    rect.left = c_long(pos_x)
    rect.top = c_long(pos_y)
    rect.right = c_long(pos_x + width)
    rect.bottom = c_long(pos_y + height)
    fill_rgb = to_rgb(color)
    fill_brush = None
    try:
        fill_brush = windll.gdi32.CreateSolidBrush(fill_rgb)
        res = windll.user32.FillRect(hdc, byref(rect), fill_brush)
        if res == 0:
            return WindowsErrorMessage('user32.FillRect')
        return None
    finally:
        if fill_brush is not None:
            _delete_gdi_object(fill_brush)


def paint__draw_text(
        hdc: HDC, hfont: HFONT,
        text: str,
        pos_x: int, pos_y: int, width: int, height: int,
        fg_color: Optional[Color], bg_color: Optional[Color]
) -> Optional[WindowsErrorMessage]:
    old_hfont = None
    try:
        old_hfont = windll.gdi32.SelectObject(hdc, hfont)
        if fg_color:
            fg = to_rgb(fg_color)
            windll.gdi32.SetTextColor(hdc, fg)
        if bg_color:
            bg = to_rgb(bg_color)
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

        ret = windll.user32.DrawTextW(
            hdc, create_unicode_buffer(text), len(text), byref(rect),
            DT_LEFT | DT_TOP | DT_NOPREFIX)
        if ret == 0:
            return WindowsErrorMessage('user32.DrawTextW')
        return None
    finally:
        # To prevent a memory leak
        if old_hfont is not None:
            windll.gdi32.SelectObject(hdc, old_hfont)


def paint__draw_outline_text(
        hdc: HDC, hfont: HFONT,
        text: str,
        pos_x: int, pos_y: int,
        outline_width: int, outline_color: Color, fill_color: Color, bg_color: Optional[Color]
) -> Optional[WindowsErrorMessage]:
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
    outline_rgb = to_rgb(outline_color)
    fill_rgb = to_rgb(fill_color)
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
            bg = to_rgb(bg_color)
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
        if res == 0:
            return WindowsErrorMessage('gdi32.StrokeAndFillPath')
        return None
    finally:
        if fill_brush is not None:
            _delete_gdi_object(fill_brush)
        if outline_pen is not None:
            _delete_gdi_object(outline_pen)
        # To prevent a memory leak
        if old_hfont is not None:
            windll.gdi32.SelectObject(hdc, old_hfont)


def shell__get_task_bar_window_handles() -> Sequence[HWND]:
    ret = []

    for hwnd in window__find_handles():
        cname = window__get_class_name(hwnd)
        if cname == "Shell_TrayWnd":
            ret.append(hwnd)

    return ret


def shell__is_key_pressed(v_key: c_int) -> bool:
    state = t_cast(SHORT, windll.user32.GetAsyncKeyState(v_key))
    return state != 0


SHELL__CANCEL_CALLBACK_CHAIN = "Cancel"


# see https://msdn.microsoft.com/en-us/library/windows/desktop/ms644967(v=vs.85).aspx
class KBDLLHOOKSTRUCT(Structure):
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
        callback: Callable[[int, int, bool, bool], Optional[str]]
) -> Union[HHOOK, WindowsErrorMessage]:
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
                #     flag_bits & LLKHF_LOWER_IL_INJECTED == LLKHF_LOWER_IL_INJECTED and 'lower-injected' or None,
                #     flag_bits & LLKHF_INJECTED == LLKHF_INJECTED and 'injected' or None,
                #     flag_bits & LLHKF_ALTDOWN == LLHKF_ALTDOWN and 'alt' or None,
                #     flag_bits & LLHKF_UP == LLHKF_UP and 'up' or 'down',
                # ]
                ret = callback(
                    kbd_ptr.vkCode,
                    kbd_ptr.scanCode,
                    flag_bits & LLHKF_UP == LLHKF_UP,
                    flag_bits & LLKHF_INJECTED == LLKHF_INJECTED
                )
                if ret == SHELL__CANCEL_CALLBACK_CHAIN:
                    call_next = False
        finally:
            if call_next:
                # print(" - forwarding key event")
                return t_cast(int, CallNextHookEx(hook_id, code, wparam, lparam))
            else:
                # From the docs:
                # If the hook procedure processed the message, it may return
                # a nonzero value to prevent the system from passing the
                # message to the rest of the hook chain or the target window
                # procedure.
                print("DEBUG NOT FORWARDING KEY")
                return 1

    callback_pointer = HOOK_CALLBACK_TYPE(low_level_handler)
    hook_id = t_cast(HHOOK, SetWindowsHookExW(WH_KEYBOARD_LL, callback_pointer, GetModuleHandleW(None), 0))
    if hook_id == 0:
        return WindowsErrorMessage('SetWindowsHookExW / keyboard')
    _CALLBACK_POINTERS[hook_id] = callback_pointer

    # Ensure that the hook is *always* uninstalled at exit to prevent OS
    # resource leaks.
    atexit.register(shell__unhook, hook_id)
    return hook_id


def shell__shell_hook(callback: Callable[[int, WPARAM, LPARAM], Optional[str]]) -> Union[HHOOK, WindowsErrorMessage]:
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

    :param callback:
    :return: hook handle
    """

    # Without some tricky logic, the shell hook will always fail.
    # Specifically, it must use a DLL to perform the hook.  One for 64-bit
    # applications, and one for 32-bit applications.
    # See https://www.codeproject.com/Articles/18638/Using-Window-Messages-to-Implement-Global-System-H
    # Otherwise, this error is encountered.
    #   ERROR_HOOK_NEEDS_HMOD (1428):
    #   Cannot set nonlocal hook without a module handle.
    #
    hmod = GetModuleHandleW(None)
    if hmod is None is None:
        return WindowsErrorMessage('GetModuleHandleW')

    # See https://msdn.microsoft.com/en-us/library/windows/desktop/ms644991(v=vs.85).aspx
    hook_id = None

    def shell_handler(code: int, wparam: WPARAM, lparam: LPARAM) -> LRESULT:
        print("[Shell handler] {0} {1} {2}".format(code, wparam, lparam))
        call_next = True
        try:
            # From the docs: If nCode is less than zero, the hook
            # procedure must return the value returned by CallNextHookEx.
            if code >= 0:
                ret = callback(code, wparam, lparam)
                if ret == SHELL__CANCEL_CALLBACK_CHAIN:
                    call_next = False
        except:  # pylint: broad-except
            print("Unexpected error: {0}".format(sys.exc_info()[0]))
            raise
        finally:
            if call_next:
                return t_cast(LRESULT, CallNextHookEx(hook_id, code, wparam, lparam))
            else:
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
        return WindowsErrorMessage('SetWindowsHookExW / shell')
    print("started shell hook " + repr(hook_id))
    _CALLBACK_POINTERS[hook_id] = callback_pointer

    # Ensure that the hook is *always* uninstalled at exit to prevent OS
    # resource leaks.
    atexit.register(shell__unhook, hook_id)

    return hook_id


def shell__unhook(hook_id: HHOOK) -> None:
    UnhookWindowsHookEx(hook_id)
    if hook_id in _CALLBACK_POINTERS:
        del _CALLBACK_POINTERS[hook_id]


# see https://msdn.microsoft.com/en-us/library/ms646270(v=vs.85).aspx
# see https://msdn.microsoft.com/en-us/library/ms646271(v=vs.85).aspx
class INPUT_KEYBOARD(Structure):
    _fields_ = [
        ("type", DWORD),
        ("wVk", WORD),
        ("wScan", WORD),
        ("dwFlags", DWORD),
        ("time", DWORD),
        ("dwExtraInfo", c_void_p),
    ]


def shell__inject_scancode(scancode: int, is_key_up: bool) -> bool:
    inp = INPUT_KEYBOARD()
    inp.type = INPUT_KEYBOARD
    inp.wScan = scancode
    if is_key_up:
        inp.dwFlags = KEYEVENTF_SCANCODE | KEYEVENTF_KEYUP
    else:
        inp.dwFlags = KEYEVENTF_SCANCODE
    res = t_cast(UINT, windll.user32.SendInput(1, byref(inp), c_sizeof(INPUT_KEYBOARD)))
    return res.value == 1  # 1 == number of events sent


def shell__lock_workstation() -> bool:
    res = t_cast(BOOL, windll.user32.LockWorkStation())
    return res.value != 0


def shell__register_window_hook(
        hwnd: HWND,
        message_id_callbacks: Optional[Dict[int, MessageCallback]] = None,
        callback: Optional[MessageCallback] = None
) -> Union[int, WindowsErrorMessage]:
    """
    Registers the "shell hook" window message with the window, and inserts the
    callback into the message_id_callbacks dict for processing, because
    the message ID is dynamically created.

    :param hwnd:
    :param message_id_callbacks:
    :param callback:
    :return: the message ID for the shell hook message.
    """
    assert message_id_callbacks is None or isinstance(message_id_callbacks, dict)

    if not RegisterShellHookWindow(hwnd):
        return WindowsErrorMessage('RegisterShellHookWindow')
    message_id = t_cast(int, RegisterWindowMessageW("SHELLHOOK"))
    if message_id == 0:
        return WindowsErrorMessage('RegisterWindowMessageW')
    if message_id_callbacks is not None and callback:
        print("DEBUG window hook message {0}".format(message_id))
        message_id_callbacks[message_id] = callback
    return message_id


def shell__create_global_message_handler(message_id_callbacks: Dict[int, MessageCallback]) -> NativeMessageCallback:
    """

    :param message_id_callbacks: a dictionary that stores a mapping
        between the message ID (uint) and a callback that handles
        that message.  The callback takes 4 parameters:
        hwnd of the window that received the message,
        the message ID (uint), the wparam, and the lparam
        (which are both message specific interpreted).
    :return: the constructed handler callback.
    """
    assert isinstance(message_id_callbacks, dict)

    def handler(hwnd: HWND, message: int, wparam: WPARAM, lparam: LPARAM) -> int:
        print("DEBUG handling hwnd message {0} {1} {2}".format(message, wparam, lparam))
        if message in message_id_callbacks:
            ret = message_id_callbacks[message](hwnd, message, wparam, lparam)
            if ret is not False:
                return 1
            # False return code means run the standard DefWindowProc.
        elif message == WM_CLOSE:
            windll.user32.DestroyWindow(hwnd)
            return 0
        elif message == WM_DESTROY:
            windll.user32.PostQuitMessage(0)
            return 0
        return t_cast(int, DefWindowProcW(hwnd, message, wparam, lparam))

    return handler


def shell__pump_messages(on_exit_callback: Callable[[], None]) -> None:
    assert callable(on_exit_callback)
    message = MSG()
    while True:
        msg = GetMessageW(byref(message), 0, 0, 0)
        if msg <= 0:
            # print("DEBUG quit message in queue")
            # 0 means WM_QUIT, < 0 means error
            on_exit_callback()
            # Is this right?
            break
        else:
            TranslateMessage(byref(message))
            DispatchMessageW(byref(message))


# Maps the key to the (getter, setter, type, is pv_param?)
_SYSTEM_PARAMETER_MAPPING: Dict[str, Tuple[int, int, Type[Union[UINT, DWORD, BOOL, ANIMATIONINFO]], bool]] = {
    "focus-border-height": (SPI_GETFOCUSBORDERHEIGHT, SPI_SETFOCUSBORDERHEIGHT, UINT, True),
    "focus-border-width": (SPI_GETFOCUSBORDERWIDTH, SPI_SETFOCUSBORDERWIDTH, UINT, True),
    "menu-drop-alignment": (SPI_GETMENUDROPALIGNMENT, SPI_SETMENUDROPALIGNMENT, BOOL, False),
    "menu-fade": (SPI_GETMENUFADE, SPI_SETMENUFADE, BOOL, True),
    "menu-show-delay": (SPI_GETMENUSHOWDELAY, SPI_SETMENUSHOWDELAY, DWORD, False),
    "combobox-animation": (SPI_GETCOMBOBOXANIMATION, SPI_SETCOMBOBOXANIMATION, BOOL, True),
    "cursor-shadow": (SPI_GETCURSORSHADOW, SPI_SETCURSORSHADOW, BOOL, True),
    "gradient-titles": (SPI_GETGRADIENTCAPTIONS, SPI_SETGRADIENTCAPTIONS, BOOL, True),
    "hot-tracking": (SPI_GETHOTTRACKING, SPI_SETHOTTRACKING, BOOL, True),
    "listbox-smooth-scrolling": (SPI_GETLISTBOXSMOOTHSCROLLING, SPI_SETLISTBOXSMOOTHSCROLLING, BOOL, True),
    "menu-animation": (SPI_GETMENUANIMATION, SPI_SETMENUANIMATION, BOOL, True),
    "menu-underlines": (SPI_GETMENUUNDERLINES, SPI_SETMENUUNDERLINES, BOOL, True),
    "selection-fade": (SPI_GETSELECTIONFADE, SPI_SETSELECTIONFADE, BOOL, True),
    "tooltip-animation": (SPI_GETTOOLTIPANIMATION, SPI_SETTOOLTIPANIMATION, BOOL, True),
    "tooltip-fade": (SPI_GETTOOLTIPFADE, SPI_SETTOOLTIPFADE, BOOL, True),
    "ui-effects": (SPI_GETUIEFFECTS, SPI_SETUIEFFECTS, BOOL, True),
    "active-window-tracking": (SPI_GETACTIVEWINDOWTRACKING, SPI_SETACTIVEWINDOWTRACKING, BOOL, True),
    "active-window-tracking-zorder": (SPI_GETACTIVEWNDTRKZORDER, SPI_SETACTIVEWNDTRKZORDER, BOOL, True),
    "active-window-tracking-timeout": (SPI_GETACTIVEWNDTRKTIMEOUT, SPI_SETACTIVEWNDTRKTIMEOUT, DWORD, True),
    "animation": (SPI_GETANIMATION, SPI_SETANIMATION, ANIMATIONINFO, True),  # special case
    "border": (SPI_GETBORDER, SPI_SETBORDER, UINT, False),
}


def shell__system_parameters_info(
        values: Dict[str, Union[int, bool, ANIMATIONINFO]]
) -> Dict[str, Union[int, bool, ANIMATIONINFO, WindowsErrorMessage]]:
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
    assert isinstance(values, dict)
    ret: Dict[str, Union[int, bool, ANIMATIONINFO, WindowsErrorMessage]] = {}
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
                ui_param, byref(val), 0
            )
            if res != 0:
                # Nope!  This can lose critical information
                # raise WinError()
                ret[parameter] = WindowsErrorMessage('SystemParametersInfoW')
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
            else:
                assert isinstance(value, bool) or isinstance(value, int)
                val = _SYSTEM_PARAMETER_MAPPING[parameter][2](value)
                if _SYSTEM_PARAMETER_MAPPING[parameter][3]:
                    pv_param = byref(val)
                else:
                    ui_param = t_cast(UINT, val)  # Implicit type based on the mapping.
            res = SystemParametersInfoW(
                _SYSTEM_PARAMETER_MAPPING[parameter][0],
                ui_param, pv_param, WM_SETTINGCHANGE
            )
            if res != 0:
                # TODO report the error better
                print("CLIENT ERROR: failed to set system parameter {0}".format(parameter))
        else:
            # TODO better errors
            print("CLIENT ERROR: Unknown system parameter {0}".format(parameter))
    return ret


# TODO
def shell__set_sys_colors() -> None:
    pass


# https://docs.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-monitorinfo
# https://docs.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-monitorinfoexw
class MONITORINFOEXW(Structure):
    _fields_ = (
        ("cbSize", DWORD),
        ("rcMonitor", RECT),
        ("rcWork", RECT),
        ("dwFlags", DWORD),
        # TODO test this out.  It should be at the end, but don't know for sure.
        ("szDevice", WCHAR * CCHDEVICENAME),
    )


def monitor__find_monitors() -> Sequence[NativeScreenInfo]:
    monitor_handles: List[HMONITOR] = []

    def callback(h_monitor: HMONITOR, hdc_monitor: HDC, lprc_monitor: LPRECT, l_param: LPARAM) -> bool:
        # hMonitor: display monitor handle
        # hdcMonitor: device context handle; color attributes + clipping region; may be null
        # lprcMonitor: RECT structure w/ device-context coordinates.
        monitor_handles.append(h_monitor)
        return True

    enum_monitor_proc = WINFUNCTYPE(c_bool, HMONITOR, HDC, LPRECT, LPARAM)
    if EnumDisplayMonitors(None, None, enum_monitor_proc(callback), 0) == 0:
        return ()

    ret: List[NativeScreenInfo] = []
    index = 0
    for monitor_handle in monitor_handles:
        info = MONITORINFOEXW()
        info.cbSize = c_sizeof(MONITORINFOEXW)
        if GetMonitorInfoW(monitor_handle, byref(info)) != 0:
            ret.append(NativeScreenInfo(
                # Disguise the handle as something else
                handle=str(monitor_handle),
                screen_index=index,
                screen_size=(
                    info.rcWork.left, info.rcWork.top,
                    info.rcWork.right - info.rcWork.left + 1,
                    info.rcWork.bottom - info.rcWork.top + 1
                ),
                work_area=(
                    info.rcMonitor.left, info.rcMonitor.top,
                    info.rcMonitor.right - info.rcMonitor.left + 1,
                    info.rcMonitor.bottom - info.rcMonitor.top + 1
                ),
                name=info.szDevice,
                is_primary=(info.dwFlags & MONITORINFOF_PRIMARY) == 1
            ))
        index += 1

    return ret


def process__get_exit_code(thread_pid: DWORD) -> Optional[int]:
    """

    :param thread_pid:
    :return: None if the process hasn't exited, or the int exit code.
    """
    hproc = windll.kernel32.OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, thread_pid)
    try:
        exit_code = DWORD()
        if GetExitCodeProcess(hproc, byref(exit_code)) != 0:
            if exit_code == STILL_ACTIVE:
                return None
            return exit_code.value
        return None
    finally:
        windll.kernel32.CloseHandle(hproc)


def process__get_window_state(thread_pid: DWORD) -> Union[WindowsWindowState, WindowsErrorMessage]:
    gui_info = GUITHREADINFO()
    gui_info.cbSize = c_sizeof(gui_info)
    res = windll.user32.GetGUIThreadInfo(thread_pid, byref(gui_info))
    if not res:
        return WindowsErrorMessage('user32.GetGUIThreadInfo')
    return create_windows_window_state(gui_info)


def process__get_current_pid() -> DWORD:
    return t_cast(DWORD, windll.kernel32.GetCurrentProcessId())


def _attach_message_queue_to_thread(current_hwnd: HWND) -> Optional[WindowsErrorMessage]:
    current_thread_id = windll.kernel32.GetCurrentThreadId()
    thread_process_id = windll.user32.GetWindowThreadProcessId(current_hwnd, None)
    if thread_process_id != current_thread_id:
        res = windll.user32.AttachThreadInput(thread_process_id, current_thread_id, True)
        # ERROR_INVALID_PARAMETER means that the two threads are already attached.
        if res == 0:
            err = WindowsErrorMessage('user32.AttachThreadInput')
            if err.errno != ERROR_INVALID_PARAMETER:
                # "WARN: could not attach thread input to thread {0} ({1})".format(thread_process_id, GetLastError())
                return err
    windll.user32.AttachThreadInput(thread_process_id, current_thread_id, False)
    return None
