"""
Windows functions for any architecture.
"""


from ctypes import wintypes, byref, windll, WinDLL
from ctypes import CFUNCTYPE, POINTER, c_int, c_uint, c_void_p, c_long, c_ulong, c_ulonglong, c_bool, c_char
from ctypes import WINFUNCTYPE, create_unicode_buffer, Structure, WinError, GetLastError
from ctypes import sizeof as c_sizeof
from ctypes import cast as c_cast
from .windows_constants import *
import atexit
import sys
import traceback


# noinspection PyUnusedLocal
def load_functions(environ, func_map):
    func_map['window__find_handles'] = window__find_handles
    func_map['window__enum_window_handles'] = window__enum_window_handles
    func_map['window__find_handle_for_class_title'] = window__find_handle_for_class_title
    func_map['window__find_handle_for_child_class_title'] = window__find_handle_for_child_class_title
    func_map['window__get_title'] = window__get_title
    func_map['window__is_visible'] = window__is_visible
    func_map['window__get_process_id'] = window__get_process_id
    func_map['window__get_class_name'] = window__get_class_name
    func_map['window__get_module_filename'] = window__get_module_filename
    func_map['window__get_thread_window_handles'] = window__get_thread_window_handles
    func_map['window__get_child_window_handles'] = window__get_child_window_handles
    func_map['window__border_rectangle'] = window__border_rectangle
    func_map['window__client_rectangle'] = window__client_rectangle
    func_map['window__move_resize'] = window__move_resize
    func_map['window__redraw'] = window__redraw
    func_map['window__repaint'] = window__repaint
    func_map['window__wait_gui_thread_idle'] = window__wait_gui_thread_idle
    func_map['window__send_message'] = window__send_message
    func_map['window__post_message'] = window__post_message
    func_map['window__close'] = window__close
    func_map['window__maximize'] = window__maximize
    func_map['window__minimize'] = window__minimize
    func_map['window__restore'] = window__restore
    func_map['window__get_visibility_states'] = window__get_visibility_states
    func_map['window__set_position'] = window__set_position
    func_map['window__set_layered_attributes'] = window__set_layered_attributes
    func_map['window__get_active_window'] = window__get_active_window
    func_map['window__activate'] = window__activate
    func_map['window__create_message_window'] = window__create_message_window
    func_map['window__create_display_window'] = window__create_display_window
    func_map['window__get_font_for_description'] = window__get_font_for_description
    func_map['window__draw_border_outline'] = window__draw_border_outline
    func_map['window__get_text_size'] = window__get_text_size
    func_map['window__do_paint'] = window__do_paint
    func_map['window__do_draw'] = window__do_draw
    func_map['paint__draw_text'] = paint__draw_text
    func_map['paint__draw_outline_text'] = paint__draw_outline_text
    func_map['shell__get_task_bar_window_handles'] = shell__get_task_bar_window_handles
    func_map['shell__keyboard_hook'] = shell__keyboard_hook
    func_map['shell__shell_hook'] = shell__shell_hook
    func_map['shell__register_window_hook'] = shell__register_window_hook
    func_map['shell__create_global_message_handler'] = shell__create_global_message_handler
    func_map['shell__unhook'] = shell__unhook
    func_map['shell__inject_scancode'] = shell__inject_scancode
    func_map['shell__lock_workstation'] = shell__lock_workstation
    func_map['shell__pump_messages'] = shell__pump_messages
    func_map['shell__system_parameters_info'] = shell__system_parameters_info
    func_map['monitor__find_monitors'] = monitor__find_monitors
    func_map['process__get_exit_code'] = process__get_exit_code
    func_map['process__get_window_state'] = process__get_window_state
    func_map['process__get_current_pid'] = process__get_current_pid
    func_map['process__get_current_username_domain'] = process__get_current_username_domain


GetModuleHandleW = windll.kernel32.GetModuleHandleW
GetModuleHandleW.restype = wintypes.HMODULE
GetModuleHandleW.argtypes = [wintypes.LPCWSTR]

HOOK_CALLBACK_TYPE = CFUNCTYPE(c_int, c_int, wintypes.HINSTANCE, POINTER(c_void_p))
SetWindowsHookExW = windll.user32.SetWindowsHookExW
SetWindowsHookExW.restype = c_int
SetWindowsHookExW.argtypes = [c_int, HOOK_CALLBACK_TYPE, wintypes.HINSTANCE, wintypes.DWORD]

GetMessageW = windll.user32.GetMessageW
GetMessageW.argtypes = [POINTER(wintypes.MSG), wintypes.HWND, c_uint, c_uint]

DispatchMessageW = windll.user32.DispatchMessageW
DispatchMessageW.argtypes = [POINTER(wintypes.MSG)]

TranslateMessage = windll.user32.TranslateMessage
TranslateMessage.argtypes = [POINTER(wintypes.MSG)]

CallNextHookEx = windll.user32.CallNextHookEx

UnhookWindowsHookEx = windll.user32.UnhookWindowsHookEx

GetExitCodeProcess = windll.kernel32.GetExitCodeProcess
GetExitCodeProcess.restype = wintypes.BOOL

EnumDisplayMonitors = windll.user32.EnumDisplayMonitors
EnumDisplayMonitors.restype = wintypes.BOOL

RegisterShellHookWindow = windll.user32.RegisterShellHookWindow
RegisterShellHookWindow.argtypes = [wintypes.HWND]
RegisterShellHookWindow.restype = wintypes.BOOL

RegisterWindowMessageW = windll.user32.RegisterWindowMessageW
RegisterWindowMessageW.argtypes = [wintypes.LPCWSTR]
RegisterWindowMessageW.restype = c_uint

RegisterClassExW = windll.user32.RegisterClassExW

CreateWindowExW = windll.user32.CreateWindowExW

DefWindowProcW = windll.user32.DefWindowProcW
DefWindowProcW.argtypes = [wintypes.HWND, c_uint, wintypes.WPARAM, wintypes.LPARAM]

SystemParametersInfoW = windll.user32.SystemParametersInfoW

SetWindowPos = windll.user32.SetWindowPos

SetActiveWindow = windll.user32.SetActiveWindow

SetForegroundWindow = windll.user32.SetForegroundWindow

SetLayeredWindowAttributes = windll.user32.SetLayeredWindowAttributes
SetLayeredWindowAttributes.argtypes = [wintypes.HWND, wintypes.COLORREF, wintypes.BYTE, wintypes.DWORD]

WNDPROCTYPE = WINFUNCTYPE(c_int, wintypes.HWND, c_uint, wintypes.WPARAM, wintypes.LPARAM)


def window__find_handles():
    """
    Find all the top-level window handles (type HWND)

    :return: list of window handles.
    """
    ret = []

    def callback(hwnd):
        ret.append(hwnd)
        # return True to continue the enumeration
        return True

    window__enum_window_handles(callback)

    return ret


def window__enum_window_handles(callback):

    # noinspection PyUnusedLocal
    def callback_wrapper(hwnd, lparam):
        return callback(hwnd)

    enum_win_proc = WINFUNCTYPE(c_bool, c_int, POINTER(c_int))
    windll.user32.EnumWindows(enum_win_proc(callback_wrapper), None)


def window__find_handle_for_class_title(class_name, title):
    return windll.user32.FindWindowW(class_name, title)


def window__find_handle_for_child_class_title(hwnd_parent, hwnd_child_after, class_name, title):
    return windll.user32.FindWindowExW(hwnd_parent, hwnd_child_after, class_name, title)


def window__get_title(hwnd_handle):
    length = windll.user32.GetWindowTextLengthW(hwnd_handle)
    if length > 0:
        buff = create_unicode_buffer(length + 1)
        windll.user32.GetWindowTextW(hwnd_handle, buff, length + 1)
        return buff.value
    return ""


def window__is_visible(hwnd_handle):
    return windll.user32.IsWindowVisible(hwnd_handle) != 0


def window__get_process_id(hwnd_handle):
    pid = wintypes.DWORD()
    thread_pid = windll.user32.GetWindowThreadProcessId(hwnd_handle, byref(pid))
    return pid


def window__get_class_name(hwnd_handle):
    buff = create_unicode_buffer(MAX_CLASS_NAME_LENGTH + 1)
    windll.user32.GetClassNameW(hwnd_handle, buff, MAX_CLASS_NAME_LENGTH + 1)
    return buff.value


def window__get_module_filename(hwnd_handle):
    buff = create_unicode_buffer(MAX_FILENAME_LENGTH + 1)
    size = windll.user32.GetWindowModuleFileNameW(hwnd_handle, buff, MAX_FILENAME_LENGTH + 1)
    if size <= 0:
        # raise WinError()
        return None
    return buff.value[:size]


def window__get_thread_window_handles(thread_process_id):
    """

    :param thread_process_id: thread process ID, as from window__get_thread_process_id
    :return: hwnd for all top-level windows with this thread process id.
    """
    ret = []

    def callback(hwnd, lparam):
        ret.append(hwnd)
        return True

    enum_win_proc = WINFUNCTYPE(c_bool, POINTER(c_int), POINTER(c_int))
    windll.user32.EnumThreadWindows(wintypes.DWORD(thread_process_id), enum_win_proc(callback), None)

    return ret


def window__get_child_window_handles(hwnd_parent):
    ret = []

    def callback(hwnd, lparam):
        ret.append(hwnd)
        return True

    enum_win_proc = WINFUNCTYPE(c_bool, POINTER(c_int), POINTER(c_int))
    windll.user32.EnumChildWindows(hwnd_parent, enum_win_proc(callback), None)

    return ret


def _rect_to_dict(rect):
    return {
        'x': rect.left,
        'y': rect.top,
        'width': rect.right - rect.left,
        'height': rect.bottom - rect.top,
        'left': rect.left,
        'right': rect.right,
        'top': rect.top,
        'bottom': rect.bottom,
    }


def window__border_rectangle(hwnd):
    """
    The outer border size and position of the window

    :param hwnd:
    :return: a dict with the keys 'x', 'y', 'width', 'height',
        'left', 'right', 'top', 'bottom'
    """
    rect = wintypes.RECT()
    res = windll.user32.GetWindowRect(hwnd, byref(rect))
    if res == 0:
        raise WinError()
    return _rect_to_dict(rect)


def window__client_rectangle(hwnd):
    """
    The client-usable space within the border rectangle.  Top and Left
    are always 0.

    :param hwnd:
    :return: the rectangle structure.
    """
    client_rect = wintypes.RECT()
    res = windll.user32.GetClientRect(hwnd, byref(client_rect))
    if res == 0:
        raise WinError()
    return _rect_to_dict(client_rect)


def window__move_resize(hwnd, x, y, width, height, repaint=True):
    """
    Move and resize the window.
    """

    ret = windll.user32.MoveWindow(hwnd, x, y, width, height, repaint)

    # check that it worked correctly
    if not ret:
        raise WinError()


def window__redraw(hwnd):
    # window__wait_gui_thread_idle(hwnd)
    # res = windll.user32.ChangeWindowMessageFilterEx(hwnd, WM_PAINT, 1, None)
    # res = windll.user32.UpdateWindow(hwnd)
    res = windll.user32.RedrawWindow(
        hwnd, None, None,
        RDW_INTERNALPAINT | RDW_ERASE | RDW_ALLCHILDREN | RDW_FRAME)
    if res == 0:
        # Successful!
        return

    # None of the above worked, probably because the process isolation doesn't allow
    # our process to send a message to another process.

    # So, try minimize then restore (if maximized, it will restore itself again)
    # This really messes up the z-ordering, though.
    if window__is_visible(hwnd):
        windll.user32.ShowWindow(hwnd, SW_MINIMIZE)
        windll.user32.ShowWindow(hwnd, SW_RESTORE)


def window__repaint(hwnd):
    # res = windll.user32.InvalidateRect(hwnd, None, False)
    res = windll.user32.RedrawWindow(hwnd, None, None, RDW_INVALIDATE)
    if res == 0:
        raise WinError()


def window__wait_gui_thread_idle(hwnd):
    thread_pid = window__get_process_id(hwnd)
    if thread_pid:
        hproc = windll.kernel32.OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, thread_pid)
        try:
            res = windll.user32.WaitForInputIdle(hproc, 1000)
            if res != 0:
                raise WinError()
        finally:
            windll.kernel32.CloseHandle(hproc)
    windll.user32.WaitGuiThreadIdle(hwnd)


def window__send_message(hwnd, key, arg1, arg2):
    return windll.user32.SendMessageW(hwnd, key, arg1, arg2)


def window__post_message(hwnd, key, arg1, arg2):
    res = windll.user32.PostMessageW(hwnd, key, arg1, arg2)
    return res != 0


def window__close(hwnd):
    # For a full implementation, see
    # Code modified from http://msdn.microsoft.com/msdnmag/issues/02/08/CQA/

    # Give the "must close" message to the window
    res = window__post_message(hwnd, WM_CLOSE, 0, 0)
    return res != 0


def window__maximize(hwnd):
    res = windll.user32.ShowWindow(hwnd, SW_MAXIMIZE)
    return res != 0


def window__minimize(hwnd):
    res = windll.user32.ShowWindow(hwnd, SW_MINIMIZE)
    if res == 0:
        raise WinError()


def window__restore(hwnd):
    # This needs to be called twice, because of the situation
    # where a window was maximized then minimized.  The first
    # restore will bring it back to visible, but maximized,
    # and the second will bring it to restored.
    windll.user32.ShowWindow(hwnd, SW_RESTORE)
    windll.user32.ShowWindow(hwnd, SW_RESTORE)


# see https://msdn.microsoft.com/en-us/library/windows/desktop/ms632611(v=vs.85).aspx
class WINDOWPLACEMENT(Structure):
    _fields_ = [
        ("length", wintypes.UINT),
        ("flags", wintypes.UINT),
        ("showCmd", wintypes.UINT),
        ("ptMinPosition", wintypes.POINT),
        ("ptMaxPosition", wintypes.POINT),
        ("rcNormalPosition", wintypes.RECT),
    ]


def window__get_visibility_states(hwnd):
    """
    Returns a list of the current visibility state of the window.


    :param hwnd:
    :return: a list of zero or more of:
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
        return []
    show_cmd = placement.showCmd
    if show_cmd == SW_HIDE:
        return ['hidden']
    if show_cmd == SW_SHOWNORMAL:
        return ['shown', 'restored', 'active']
    if show_cmd == SW_SHOWMINIMIZED:
        return ['shown', 'minimized', 'active']
    if show_cmd == SW_MAXIMIZE:
        return ['shown', 'maximized', 'active']
    if show_cmd == SW_SHOWMAXIMIZED:
        return ['shown', 'maximized', 'active']
    if show_cmd == SW_SHOWNOACTIVATE:
        return ['shown', 'restored']
    if show_cmd == SW_SHOW:
        return ['shown', 'restored', 'active']
    if show_cmd == SW_MINIMIZE:
        return ['shown', 'minimized', 'active']
    if show_cmd == SW_SHOWMINNOACTIVE:
        return ['shown', 'minimized']
    if show_cmd == SW_SHOWNA:
        return ['shown', 'restored']
    if show_cmd == SW_RESTORE:
        return ['shown', 'restored', 'active']
    return []


class LOGBRUSH(Structure):
    _fields_ = [
        # C:/PROGRA~1/MIAF9D~1/VC98/Include/wingdi.h 1025
        ('lbStyle', c_uint),
        ('lbColor', wintypes.DWORD),  # COLORREF
        ('lbHatch', c_long),
    ]


def window__draw_border_outline(rect, color, width, line_style=PS_SOLID, fill_style=BS_NULL, parent_hwnd=None):
    """
    Draws a border on the screen.  Does not need a window context.

    :param fill_style:
    :param line_style:
    :param rect: border to draw
    :param color: RBG integer (0xRRGGBB)
    :param width:
    :param line_style:
    :param parent_hwnd: handle of the parent window, if any.
    :return:
    """
    color &= 0xffffff

    pen_handle = None
    brush_handle = None
    dc_handle = None

    try:
        # Pen == outside drawing definition
        pen_handle = windll.gdi32.CreatePen(line_style, width, color)

        # Brush == inside
        brush_def = LOGBRUSH()
        # BS_NULL so that the fill is empty
        brush_def.lbStyle = fill_style
        brush_def.lbHatch = HS_DIAGCROSS
        brush_def.lbColor = color
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

        windll.gdi32.Rectangle(dc_handle, rect['left'], rect['top'], rect['right'], rect['bottom'])
    finally:
        if brush_handle is not None:
            windll.gdi32.DeleteObject(brush_handle)
        if pen_handle is not None:
            windll.gdi32.DeleteObject(pen_handle)
        if dc_handle is not None:
            windll.gdi32.DeleteDC(dc_handle)


def window__set_position(hwnd, hwnd_after_zorder, x, y, width, height, flags):
    zorder = hwnd_after_zorder
    if zorder in HWND_ZORDER_MAP:
        zorder = HWND_ZORDER_MAP[zorder]
    uflags = 0
    for flag in flags:
        if flag in SWP_FLAG_MAP:
            uflags |= SWP_FLAG_MAP[flag]
        else:
            # TODO better error
            print("Unknown SWP set position flag {0}".format(flag))
    res = SetWindowPos(hwnd, zorder, x, y, width, height, uflags)
    return res != 0


def window__set_layered_attributes(hwnd, r, g, b, a):
    res = SetLayeredWindowAttributes(
        hwnd, wintypes.RGB(r, g, b), a, LWA_ALPHA)
    if res == 0:
        raise WinError()


def window__get_active_window():
    # GetActiveWindow is only for the current thread.
    # It usually just returns None.
    hwnd = windll.user32.GetForegroundWindow()
    if hwnd == 0:
        return None
    return hwnd


def window__activate(hwnd):
    # Give the window the focus.  This is the Microsoft Magic Focus Dance.
    current_hwnd = windll.user32.GetForegroundWindow()
    current_thread_id = windll.kernel32.GetCurrentThreadId()
    thread_process_id = windll.user32.GetWindowThreadProcessId(current_hwnd, None)
    res = windll.user32.AttachThreadInput(thread_process_id, current_thread_id, True)
    if res == 0:
        # TODO better logging
        print("WARN: could not attach thread input to thread {0}".format(thread_process_id))
        return True
    res = windll.user32.SetWindowPos(hwnd, HWND_TOPMOST, 0, 0, 0, 0, SWP_NOSIZE | SWP_NOMOVE)
    if res == 0:
        return False
    # At this point, the window hwnd is valid, so we don't need to fail out
    # if the results are non-zero.  Some of these will not succeed due to
    # attributes of the window, rather than the window not existing.
    windll.user32.SetWindowPos(hwnd, HWND_NOTOPMOST, 0, 0, 0, 0, SWP_NOSIZE | SWP_NOMOVE)
    windll.user32.SetForegroundWindow(hwnd)
    windll.user32.AttachThreadInput(thread_process_id, current_thread_id, False)
    windll.user32.SetFocus(hwnd)
    windll.user32.SetActiveWindow(hwnd)
    return True


class WNDCLASSEX(Structure):
    _fields_ = [("cbSize", c_uint),
                ("style", c_uint),
                ("lpfnWndProc", WNDPROCTYPE),
                ("cbClsExtra", c_int),
                ("cbWndExtra", c_int),
                ("hInstance", wintypes.HANDLE),
                ("hIcon", wintypes.HANDLE),
                ("hCursor", wintypes.HANDLE),
                ("hBrush", wintypes.HANDLE),
                ("lpszMenuName", wintypes.LPCWSTR),
                ("lpszClassName", wintypes.LPCWSTR),
                ("hIconSm", wintypes.HANDLE)]


def window__create_message_window(
        class_name,
        message_handler):
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
        # TODO real error
        raise WinError()
    # Top level, never viewed, window.  Note that we set title to
    # "null" to further emphasize that this is a non-viewable window.
    # We don't use a message-only window, so that the window can
    # receive global event hooks.
    hwnd = CreateWindowExW(
        0, class_name, None,
        WS_OVERLAPPEDWINDOW, 0, 0, 0, 0, HWND_DESKTOP, None, hinst, None
    )
    if hwnd is None or hwnd == 0:
        raise WinError()

    _CALLBACK_POINTERS[hwnd] = window_proc
    return hwnd


def window__create_display_window(
        class_name,
        title,
        message_handler,
        style_flags):
    """
    Create a viewable window, to do stuff to it.

    :param class_name:
    :param message_handler: the handler procedure created by shell__create_global_message_handler
    :param title: defaults to the class name
    :param style_flags: list of strings within WS_STYLE_BIT_MAP
    :return: hwnd
    """

    if not class_name.startswith(PETRONIA_CREATED_WINDOW__CLASS_PREFIX):
        class_name = PETRONIA_CREATED_WINDOW__CLASS_PREFIX + class_name

    # A persistent pointer to a handler.  Must be persisted so it isn't
    # removed when we exit this method.
    window_proc = WNDPROCTYPE(message_handler)
    hinst = GetModuleHandleW(None)

    window_class = WNDCLASSEX()
    window_class.cbSize = c_sizeof(WNDCLASSEX)
    window_class.style = CS_DBLCLKS
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
        raise WinError()

    style = 0
    for flag in style_flags:
        if flag in WS_STYLE_BIT_MAP:
            style |= WS_STYLE_BIT_MAP[flag]

    hwnd = CreateWindowExW(
        0, class_name, title,
        style, 0, 0, 10, 10,
        None,  # HWND_DESKTOP,
        None, hinst, None
    )
    if hwnd is None or hwnd == 0:
        raise WinError()

    _CALLBACK_POINTERS[hwnd] = window_proc
    return hwnd


_FONT_HANDLES = {}


def window__get_font_for_description(font, hwnd=None, base_hdc=None):
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
        hfont = windll.gdi32.CreateFontW(
            -height, 0, 0, 0,
            weight, italic, underline, strikeout,
            DEFAULT_CHARSET, OUT_TT_PRECIS, CLIP_DEFAULT_PRECIS, PROOF_QUALITY, FF_DONTCARE,
            create_unicode_buffer(font_name))
        if hfont == 0 or hfont is None:
            raise WinError()
        _FONT_HANDLES[font] = hfont

        atexit.register(_delete_gdi_object, hfont)

        return hfont
    finally:
        if base_hdc is None and created_hdc is None:
            windll.user32.ReleaseDC(hdc)
        if base_hdc is None and created_hdc is not None:
            windll.gdi32.DeleteDC(hdc)


def _delete_gdi_object(obj_handle):
    windll.gdi32.DeleteObject(obj_handle)


def window__get_text_size(hfont, text, hwnd=None, base_hdc=None):
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
    size = wintypes.SIZE()
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
                raise WinError()
            height += size.cy
            width = max(width, size.cx)
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
    _fields_ = [
        ("hdc", wintypes.HANDLE),
        ("fErase", c_bool),
        ("rcPaint", wintypes.RECT),
        ("fRestore", c_bool),
        ("fIncUpdate", c_bool),
        ("rgbReserved", wintypes.BYTE * 32),
    ]


def window__do_paint(hwnd, paint_callback):
    """
    Start the paint callback message.

    :param hwnd:
    :param paint_callback: function, takes 2 argument: the hwnd, and the hdc of the paint.
    :return: paint_callback return value
    """
    ps = PAINTSTRUCT()
    hdc = windll.user32.BeginPaint(hwnd, byref(ps))
    if hdc == 0 or hdc is None:
        raise WinError()
    try:
        return paint_callback(hwnd, hdc)
    finally:
        windll.user32.EndPaint(hwnd, byref(ps))


def window__do_draw(hwnd, paint_callback):
    hdc = windll.user32.GetDC(hwnd)
    try:
        paint_callback(hwnd, hdc)
    finally:
        windll.user32.ReleaseDC(hdc)


def paint__draw_text(hdc, hfont, text, pos_x, pos_y, width, height, fg_color, bg_color):
    old_hfont = None
    try:
        old_hfont = windll.gdi32.SelectObject(hdc, hfont)
        if fg_color:
            fg = wintypes.RGB((fg_color >> 16) & 0xff, (fg_color >> 8) & 0xff, fg_color & 0xff)
            windll.gdi32.SetTextColor(hdc, fg)
        if bg_color:
            bg = wintypes.RGB((bg_color >> 16) & 0xff, (bg_color >> 8) & 0xff, bg_color & 0xff)
            windll.gdi32.SetBkColor(hdc, bg)
            windll.gdi32.SetBkMode(hdc, OPAQUE)
        else:
            bg = wintypes.RGB(0, 0, 0)
            windll.gdi32.SetBkColor(hdc, bg)
            windll.gdi32.SetBkMode(hdc, TRANSPARENT)

        rect = wintypes.RECT()
        rect.left = pos_x
        rect.top = pos_y
        rect.right = pos_x + width
        rect.bottom = pos_y + height

        ret = windll.user32.DrawTextW(
            hdc, create_unicode_buffer(text), len(text), byref(rect),
            DT_LEFT | DT_TOP | DT_NOPREFIX)
        if ret == 0:
            raise WinError()
    finally:
        # To prevent a memory leak
        if old_hfont is not None:
            windll.gdi32.SelectObject(hdc, old_hfont)


def paint__draw_outline_text(hdc, hfont, text, pos_x, pos_y, outline_width, outline_color, fill_color, bg_color):
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
    outline_rgb = wintypes.RGB((outline_color >> 16) & 0xff, (outline_color >> 8) & 0xff, outline_color & 0xff)
    fill_rgb = wintypes.RGB((fill_color >> 16) & 0xff, (fill_color >> 8) & 0xff, fill_color & 0xff)
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
            bg = wintypes.RGB((bg_color >> 16) & 0xff, (bg_color >> 8) & 0xff, bg_color & 0xff)
            windll.gdi32.SetBkColor(hdc, bg)
            windll.gdi32.SetBkMode(hdc, OPAQUE)
        else:
            bg = wintypes.RGB(0, 0, 0)
            windll.gdi32.SetBkColor(hdc, bg)
            windll.gdi32.SetBkMode(hdc, TRANSPARENT)

        windll.gdi32.BeginPath(hdc)
        windll.gdi32.TextOutW(hdc, pos_x, pos_y, create_unicode_buffer(text), len(text))
        windll.gdi32.EndPath(hdc)
        windll.gdi32.StrokeAndFillPath(hdc)
    finally:
        if fill_brush is not None:
            _delete_gdi_object(fill_brush)
        if outline_pen is not None:
            _delete_gdi_object(outline_pen)
        # To prevent a memory leak
        if old_hfont is not None:
            windll.gdi32.SelectObject(hdc, old_hfont)


def shell__get_task_bar_window_handles():
    ret = []

    for hwnd in window__find_handles():
        cname = window__get_class_name(hwnd)
        if cname == "Shell_TrayWnd":
            ret.append(hwnd)

    return ret

SHELL__CANCEL_CALLBACK_CHAIN = "Cancel"


# see https://msdn.microsoft.com/en-us/library/windows/desktop/ms644967(v=vs.85).aspx
class KBDLLHOOKSTRUCT(Structure):
    _fields_ = [
        ("vkCode", wintypes.DWORD),
        ("scanCode", wintypes.DWORD),
        ("flags", wintypes.DWORD),
        ("time", wintypes.DWORD),
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


def shell__keyboard_hook(callback):
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
    registry key `HKEY_CURRENT_USER\Control Panel\Desktop`.  In Windows 7
    and later, if the hook goes beyond this time, the hook is silently
    removed, and the application won't know about it.

    :param callback:
    :return: hook handle
    """
    hook_id = None

    def low_level_handler(code, wparam, lparam):
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
                return CallNextHookEx(hook_id, code, wparam, lparam)
            else:
                # From the docs:
                # If the hook procedure processed the message, it may return
                # a nonzero value to prevent the system from passing the
                # message to the rest of the hook chain or the target window
                # procedure.
                # print("DEBUG NOT FORWARDING KEY")
                return 1

    callback_pointer = HOOK_CALLBACK_TYPE(low_level_handler)
    hook_id = SetWindowsHookExW(WH_KEYBOARD_LL, callback_pointer, GetModuleHandleW(None), 0)
    _CALLBACK_POINTERS[hook_id] = callback_pointer

    # Ensure that the hook is *always* uninstalled at exit to prevent OS
    # resource leaks.
    atexit.register(shell__unhook, hook_id)
    return hook_id


def shell__shell_hook(callback):
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
    # See https://msdn.microsoft.com/en-us/library/windows/desktop/ms644991(v=vs.85).aspx
    hook_id = None

    def shell_handler(code, wparam, lparam):
        call_next = True
        try:
            if code >= 0:
                ret = callback(code, wparam, lparam)
                if ret == SHELL__CANCEL_CALLBACK_CHAIN:
                    call_next = False
        except:
            print("Unexpected error: {0}".format(sys.exc_info()[0]))
            raise
        finally:
            # From the docs: If nCode is less than zero, the hook
            # procedure must return the value returned by CallNextHookEx.
            if call_next or code < 0:
                return CallNextHookEx(hook_id, code, wparam, lparam)
            else:
                # print("Canceling callback chain")
                # From the docs:
                # If the hook procedure processed the message, it may return
                # a nonzero value to prevent the system from passing the
                # message to the rest of the hook chain or the target window
                # procedure.
                return 1

    callback_pointer = HOOK_CALLBACK_TYPE(shell_handler)
    hook_id = SetWindowsHookExW(WH_SHELL, callback_pointer, GetModuleHandleW(None), 0)
    _CALLBACK_POINTERS[hook_id] = callback_pointer

    # Ensure that the hook is *always* uninstalled at exit to prevent OS
    # resource leaks.
    atexit.register(shell__unhook, hook_id)

    return hook_id


def shell__unhook(hook_id):
    UnhookWindowsHookEx(hook_id)
    if hook_id in _CALLBACK_POINTERS:
        del _CALLBACK_POINTERS[hook_id]


# see https://msdn.microsoft.com/en-us/library/ms646270(v=vs.85).aspx
# see https://msdn.microsoft.com/en-us/library/ms646271(v=vs.85).aspx
class INPUT_KEYBOARD(Structure):
    _fields_ = [
        ("type", wintypes.DWORD),
        ("wVk", wintypes.WORD),
        ("wScan", wintypes.WORD),
        ("dwFlags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", c_void_p),
    ]


def shell__inject_scancode(scancode, is_key_up):
    inp = INPUT_KEYBOARD()
    inp.type = INPUT_KEYBOARD
    inp.wScan = scancode
    if is_key_up:
        inp.dwFlags = KEYEVENTF_SCANCODE | KEYEVENTF_KEYUP
    else:
        inp.dwFlags = KEYEVENTF_SCANCODE
    res = windll.user32.SendInput(1, byref(inp), c_sizeof(INPUT_KEYBOARD))
    if res != 1:  # 1 == number of events sent
        raise WinError()


def shell__lock_workstation():
    res = windll.user32.LockWorkStation()
    if res == 0:
        raise WinError()


def shell__register_window_hook(hwnd, message_id_callbacks=None, callback=None):
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
        raise WinError()
    message_id = RegisterWindowMessageW("SHELLHOOK")
    if message_id_callbacks:
        message_id_callbacks[message_id] = callback
    return message_id


def shell__create_global_message_handler(message_id_callbacks):
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

    def handler(hwnd, message, wparam, lparam):
        if message in message_id_callbacks:
            ret = message_id_callbacks[message](hwnd, message, wparam, lparam)
            return ret or 0
        else:
            return DefWindowProcW(hwnd, message, wparam, lparam)

    message_id_callbacks[WM_DESTROY] = lambda m: windll.user32.PostQuitMessage(0)
    return handler


def shell__pump_messages(on_exit_callback=None):
    assert on_exit_callback is None or callable(on_exit_callback)
    message = wintypes.MSG()
    while True:
        msg = GetMessageW(byref(message), 0, 0, 0)
        if msg <= 0:
            # print("DEBUG quit message in queue")
            # 0 means WM_QUIT, < 0 means error
            if on_exit_callback is not None and callable(on_exit_callback):
                on_exit_callback()
            else:
                sys.exit(0)
        else:
            TranslateMessage(byref(message))
            DispatchMessageW(byref(message))


# see https://msdn.microsoft.com/en-us/library/windows/desktop/ms644967(v=vs.85).aspx
class ANIMATIONINFO(Structure):
    _fields_ = [
        ("cbSize", wintypes.UINT),
        ("iMinAnimate", c_int),
        ("flags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", c_void_p),
    ]

# Maps the key to the (getter, setter, type, is pv_param?)
_SYSTEM_PARAMETER_MAPPING = {
    "focus-border-height": (SPI_GETFOCUSBORDERHEIGHT, SPI_SETFOCUSBORDERHEIGHT, wintypes.UINT, True),
    "focus-border-width": (SPI_GETFOCUSBORDERWIDTH, SPI_SETFOCUSBORDERWIDTH, wintypes.UINT, True),
    "menu-drop-alignment": (SPI_GETMENUDROPALIGNMENT, SPI_SETMENUDROPALIGNMENT, wintypes.BOOL, False),
    "menu-fade": (SPI_GETMENUFADE, SPI_SETMENUFADE, wintypes.BOOL, True),
    "menu-show-delay": (SPI_GETMENUSHOWDELAY, SPI_SETMENUSHOWDELAY, wintypes.DWORD, False),
    "combobox-animation": (SPI_GETCOMBOBOXANIMATION, SPI_SETCOMBOBOXANIMATION, wintypes.BOOL, True),
    "cursor-shadow": (SPI_GETCURSORSHADOW, SPI_SETCURSORSHADOW, wintypes.BOOL, True),
    "gradient-titles": (SPI_GETGRADIENTCAPTIONS, SPI_SETGRADIENTCAPTIONS, wintypes.BOOL, True),
    "hot-tracking": (SPI_GETHOTTRACKING, SPI_SETHOTTRACKING, wintypes.BOOL, True),
    "listbox-smooth-scrolling": (SPI_GETLISTBOXSMOOTHSCROLLING, SPI_SETLISTBOXSMOOTHSCROLLING, wintypes.BOOL, True),
    "menu-animation": (SPI_GETMENUANIMATION, SPI_SETMENUANIMATION, wintypes.BOOL, True),
    "menu-underlines": (SPI_GETMENUUNDERLINES, SPI_SETMENUUNDERLINES, wintypes.BOOL, True),
    "selection-fade": (SPI_GETSELECTIONFADE, SPI_SETSELECTIONFADE, wintypes.BOOL, True),
    "tooltip-animation": (SPI_GETTOOLTIPANIMATION, SPI_SETTOOLTIPANIMATION, wintypes.BOOL, True),
    "tooltip-fade": (SPI_GETTOOLTIPFADE, SPI_SETTOOLTIPFADE, wintypes.BOOL, True),
    "ui-effects": (SPI_GETUIEFFECTS, SPI_SETUIEFFECTS, wintypes.BOOL, True),
    "active-window-tracking": (SPI_GETACTIVEWINDOWTRACKING, SPI_SETACTIVEWINDOWTRACKING, wintypes.BOOL, True),
    "active-window-tracking-zorder": (SPI_GETACTIVEWNDTRKZORDER, SPI_SETACTIVEWNDTRKZORDER, wintypes.BOOL, True),
    "active-window-tracking-timeout": (SPI_GETACTIVEWNDTRKTIMEOUT, SPI_SETACTIVEWNDTRKTIMEOUT, wintypes.DWORD, True),
    "animation": (SPI_GETANIMATION, SPI_SETANIMATION, ANIMATIONINFO, None),  # special case
    "border": (SPI_GETBORDER, SPI_SETBORDER, wintypes.UINT, False),
}


def shell__system_parameters_info(values):
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
    ret = {}
    for parameter, value in values.items():
        if parameter in _SYSTEM_PARAMETER_MAPPING:
            # get
            val = _SYSTEM_PARAMETER_MAPPING[parameter][2]()
            ui_param = 0
            if _SYSTEM_PARAMETER_MAPPING[parameter][2] == ANIMATIONINFO:
                ui_param = c_sizeof(ANIMATIONINFO)
                val.cbSize = c_sizeof(ANIMATIONINFO)
            res = SystemParametersInfoW(
                _SYSTEM_PARAMETER_MAPPING[parameter][0],
                ui_param, byref(val), 0
            )
            if res != 0:
                # Nope!  This can lose critical information
                # raise WinError()
                ret[parameter] = WinError()
                continue
            if _SYSTEM_PARAMETER_MAPPING[parameter][2] == wintypes.BOOL:
                ret[parameter] = val == 0
            else:
                ret[parameter] = int(val)

            # set
            pv_param = None
            ui_param = 0
            # Should convert from py type to c type correctly.
            if _SYSTEM_PARAMETER_MAPPING[parameter][2] == ANIMATIONINFO:
                ui_param = c_sizeof(ANIMATIONINFO)
                val = ANIMATIONINFO()
                val.cbSize = c_sizeof(ANIMATIONINFO)
                val.iMinAnimate = value
                pv_param = byref(val)
            else:
                val = _SYSTEM_PARAMETER_MAPPING[parameter][2](value)
                if _SYSTEM_PARAMETER_MAPPING[parameter][3]:
                    pv_param = byref(val)
                else:
                    ui_param = val
            res = SystemParametersInfoW(
                _SYSTEM_PARAMETER_MAPPING[parameter][0],
                ui_param, pv_param, WM_SETTINGCHANGE
            )
            if res != 0:
                # Nope!
                # raise WinError()
                try:
                    raise WinError()
                except OSError:
                    # TODO better error reporting
                    traceback.print_exc()
        else:
            # TODO better errors
            print("CLIENT ERROR: Unknown system parameter {0}".format(parameter))


# TODO
def shell__set_sys_colors():
    pass


def monitor__find_monitors():
    ret = []

    def callback(h_monitor, hdc_monitor, lprc_monitor, lParam):
        # hMonitor: display monitor handle
        # hdcMonitor: device context handle; color attributes + clipping region
        # lprcMonitor: RECT structure w/ device-context coordinates.
        ret.append({
            'monitor_handle': h_monitor,
            'device_context_handle': hdc_monitor,
            'left': lprc_monitor.contents.left,
            'right': lprc_monitor.contents.right,
            'top': lprc_monitor.contents.top,
            'bottom': lprc_monitor.contents.bottom,
            'width': lprc_monitor.contents.right - lprc_monitor.contents.left,
            'height': lprc_monitor.contents.bottom - lprc_monitor.contents.top,
            'primary': len(ret) == 0,
            'index': len(ret),
        })
        return True

    enum_monitor_proc = WINFUNCTYPE(c_bool, POINTER(c_int), POINTER(c_int), POINTER(wintypes.RECT), POINTER(c_int))
    if EnumDisplayMonitors(None, None, enum_monitor_proc(callback), None) == 0:
        raise Exception("Could not find monitors")

    # for i in ret:
    #     info = POINTER(wintypes.MONITORINFOEX())
    #     if GetMonitorInfo(i['monitor_handle'], info) != 0:
    #         i['primary'] = info.contents.dwFlags == MONITORINFOF_PRIMARY
    #         i['name'] = str(info.contents.szDevice)

    return ret


def process__get_exit_code(thread_pid):
    """

    :param thread_pid:
    :return: None if the process hasn't exited, or the int exit code.
    """
    hproc = windll.kernel32.OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, thread_pid)
    try:
        exit_code = wintypes.DWORD()
        if GetExitCodeProcess(hproc, byref(exit_code)) != 0:
            if exit_code == STILL_ACTIVE:
                return None
            return int(exit_code)
        raise WinError()
    finally:
        windll.kernel32.CloseHandle(hproc)


def process__get_window_state(thread_pid):
    gui_info = wintypes.GUITHREADINFO()
    gui_info.cbSize = c_sizeof(gui_info)
    res = windll.user32.GetGUIThreadInfo(thread_pid, byref(gui_info))
    if not res:
        # TODO real error
        raise WinError()

    ret = {
        'active_hwnd': gui_info.hwndActive,
        'focus_hwnd': gui_info.hwndFocus,
        'capture_hwnd': gui_info.hwndCapture,
        'menu_hwnd': gui_info.hwndMenuOwner,
        'movesize_hwnd': gui_info.hwndMoveSize,
        'caret_hwnd': gui_info.hwndCaret,
        'caret_rect': _rect_to_dict(gui_info.rcCaret),
        'flags': []
    }
    if res.flags & GUI_CARETBLINKING == GUI_CARETBLINKING:
        ret['flags'].append('caret-blinking')
    if res.flags & GUI_INMENUMODE == GUI_INMENUMODE:
        ret['flags'].append('in-menu-mode')
    if res.flags & GUI_INMOVESIZE == GUI_INMOVESIZE:
        ret['flags'].append('in-move-size')
    if res.flags & GUI_POPUPMENUMODE == GUI_POPUPMENUMODE:
        ret['flags'].append('popup-menu-mode')
    if res.flags & GUI_SYSTEMMENUMODE == GUI_SYSTEMMENUMODE:
        ret['flags'].append('in-system-menu-mode')

    return ret


def process__get_current_pid():
    return windll.kernel32.GetCurrentProcessId()


def process__get_current_username_domain():
    # Just the username is easy (GetUserName), but the domain takes more work.
    return process__get_username_domain_for_pid(process__get_current_pid())
