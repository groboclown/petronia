"""
Windows functions for any architecture.
"""


from ctypes import wintypes, byref, windll, WinDLL
from ctypes import CFUNCTYPE, POINTER, c_int, c_uint, c_void_p, c_long, c_ulong, c_ulonglong, c_bool, c_char
from ctypes import WINFUNCTYPE, create_unicode_buffer, Structure, WinError
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
    func_map['window__wait_gui_thread_idle'] = window__wait_gui_thread_idle
    func_map['window__send_message'] = window__send_message
    func_map['window__post_message'] = window__post_message
    func_map['window__close'] = window__close
    func_map['window__maximize'] = window__maximize
    func_map['window__minimize'] = window__minimize
    func_map['window__restore'] = window__restore
    func_map['window__get_visibility_states'] = window__get_visibility_states
    func_map['window__draw_border_outline'] = window__draw_border_outline
    func_map['window__set_transparency'] = window__set_transparency
    func_map['window__set_position'] = window__set_position
    func_map['window__get_active_window'] = window__get_active_window
    func_map['window__activate'] = window__activate
    func_map['window__create_message_window'] = window__create_message_window
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
    func_map['process__get_username_domain_for_pid'] = process__get_username_domain_for_pid
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

SetWindowLongPtrW = windll.user32.SetWindowLongPtrW

SetWindowPos = windll.user32.SetWindowPos

SetActiveWindow = windll.user32.SetActiveWindow

SetForegroundWindow = windll.user32.SetForegroundWindow

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
    windll.user32.GetWindowRect(hwnd, byref(rect))
    return _rect_to_dict(rect)


def window__client_rectangle(hwnd):
    """
    The client-usable space within the border rectangle.  Top and Left
    are always 0.

    :param hwnd:
    :return: the rectangle structure.
    """
    client_rect = wintypes.RECT()
    windll.user32.GetClientRect(hwnd, byref(client_rect))
    return _rect_to_dict(client_rect)


def window__move_resize(hwnd, x, y, width, height, repaint=True):
    """
    Move and resize the window.
    """

    ret = windll.user32.MoveWindow(hwnd, x, y, width, height, repaint)

    # check that it worked correctly
    if not ret:
        # TODO real exception
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
    windll.user32.PostMessageW(hwnd, key, arg1, arg2)


def window__close(hwnd):
    # For a full implementation, see
    # Code modified from http://msdn.microsoft.com/msdnmag/issues/02/08/CQA/

    # Give the "must close" message to the window
    window__post_message(hwnd, WM_CLOSE, 0, 0)


def window__maximize(hwnd):
    windll.user32.ShowWindow(hwnd, SW_MAXIMIZE)


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


def window__draw_border_outline(rect, color, width, line_style=PS_SOLID, fill_style=BS_NULL):
    """

    :param fill_style:
    :param line_style:
    :param rect: border to draw
    :param color: RBG integer (0xRRGGBB)
    :param width:
    :param line_style:
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
        brush_handle = windll.gdi32.CreateBrushIndirect(byref(brush_def))

        # Create a device context to draw on
        dc_handle = windll.gdi32.CreateDCW("DISPLAY", None, None, None)
        windll.gdi32.SelectObject(dc_handle, brush_handle)
        windll.gdi32.SelectObject(dc_handle, pen_handle)

        windll.gdi32.Rectangle(dc_handle, rect['left'], rect['top'], rect['right'], rect['bottom'])
    finally:
        if brush_handle is not None:
            windll.gdi32.DeleteObject(brush_handle)
        if pen_handle is not None:
            windll.gdi32.DeleteObject(pen_handle)
        if dc_handle is not None:
            windll.gdi32.DeleteDC(dc_handle)


def window__set_transparency(hwnd, alpha_value=128):
    raise NotImplemented()
    # TODO this needs to depend upon the SetWindowLong or SetWindowLongPtr
    # defined in x86 and x64.
    # if alpha_value < 0 or alpha_value > 255:
    #     raise ValueError("Alpha must be within the range 0 to 255")
    # ret = windll.user32.SetWindowLong(hwnd, GWL_EXSTYLE, window__get_exstyle(hwnd) | WS_EX_LAYERED)
    # if ret == 0:
    #     # TODO real error
    #     raise WinError()
    # ret = windll.user32.SetLayeredWindowAttributes(hwnd, wintypes.RGB(0, 0, 0), alpha_value, LWA_ALPHA)
    # if not ret:
    #     # TODO real error
    #     raise WinError()


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
    SetWindowPos(hwnd, zorder, x, y, width, height, uflags)


def window__get_active_window():
    hwnd = windll.user32.GetActiveWindow()
    if hwnd == 0:
        return None
    return hwnd


def window__activate(hwnd):
    # Give the window the focus.  This is the Microsoft Magic Focus Dance.
    current_hwnd = windll.user32.GetForegroundWindow()
    current_thread_id = windll.kernel32.GetCurrentThreadId()
    thread_process_id = windll.user32.GetWindowThreadProcessId(current_hwnd, None)
    windll.user32.AttachThreadInput(thread_process_id, current_thread_id, True)
    windll.user32.SetWindowPos(hwnd, HWND_TOPMOST, 0, 0, 0, 0, SWP_NOSIZE | SWP_NOMOVE)
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
        message_handler,
        title=None):
    """
    Create a "message" window - a window that's only for posting messages
    to, and for handling other OS messages.

    However, some broadcast messages we need, like WM_DISPLAYCHANGE.
    Therefore, it needs to be a real window that is just never shown.

    :param message_handler: the handler procedure created by shell__create_global_message_handler
    :param class_name: unique class name for the window
    :param title: defaults to the class name
    :return:
    """
    title = title or class_name

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
    # Message window only
    # hwnd = CreateWindowExW(
    #     0, class_name, title,
    #     0, 0, 0, 0, 0, HWND_MESSAGE, None, None, None
    # )
    # Top level, never viewed, window.  Note that we set title to
    # "null" to further emphasize that this is a non-viewable window.
    hwnd = CreateWindowExW(
        0, class_name, None,
        WS_OVERLAPPEDWINDOW, 0, 0, 0, 0, HWND_DESKTOP, None, hinst, None
    )

    _CALLBACK_POINTERS[hwnd] = window_proc
    return hwnd


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
        print("Shell handler")
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
                print("Canceling callback chain")
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
                exit(0)
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


def process__get_username_domain_for_pid(thread_pid):
    """

    :param thread_pid:
    :return: the tuple (username, domain) for the user that owns the pid.
    """
    OpenProcessToken = windll.advapi32.OpenProcessToken
    OpenProcessToken.argyptes = [wintypes.HANDLE, wintypes.DWORD, POINTER(wintypes.HANDLE)]
    OpenProcessToken.restype = wintypes.BOOL

    hproc = windll.kernel32.OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, thread_pid)
    if hproc == 0:
        raise WinError()
    try:
        access_token = wintypes.HANDLE()
        res = OpenProcessToken(hproc, wintypes.DWORD(TOKEN_QUERY), byref(access_token))
        if res == 0:
            raise WinError()
        try:
            actual_size = wintypes.DWORD(0)
            # Get the data size
            res = windll.advapi32.GetTokenInformation(
                access_token, TOKEN_INFORMATION__TOKEN_USER,
                None, 0, byref(actual_size))
            # TODO check if res is not error and not allocation size problem
            # if res == 0 and GetLastError() != ERROR_INSUFFICIENT_BUFFER:
            #     raise WinError()
            actual_size = wintypes.DWORD(actual_size.value - 4)
            sid_info = (wintypes.BYTE * actual_size.value)()

            # FIXME It looks like the sid_info isn't being
            # correctly populated.  It's causing the user/domain
            # to come back empty.
            res = windll.advapi32.GetTokenInformation(
                access_token, TOKEN_INFORMATION__TOKEN_USER,
                sid_info, actual_size, byref(actual_size))
            if res != 0:
                print("Allocated {0} bytes".format(actual_size))
                raise WinError()

            username = create_unicode_buffer(MAX_USERNAME_LENGTH + 1)
            username_size = wintypes.DWORD(MAX_USERNAME_LENGTH)
            domain = create_unicode_buffer(MAX_USERNAME_LENGTH + 1)
            domain_size = wintypes.DWORD(MAX_USERNAME_LENGTH)
            sid_name_type = wintypes.DWORD()

            res = windll.advapi32.LookupAccountSidW(
                None, sid_info[0], username, byref(username_size),
                domain, byref(domain_size), byref(sid_name_type))
            if res != 0:
                raise WinError()
            # print("DEBUG [{0}] [{1}] {2}".format(username.value, domain.value, sid_name_type))
            return username.value, domain.value
        finally:
            windll.kernel32.CloseHandle(access_token)
    finally:
        windll.kernel32.CloseHandle(hproc)


def process__get_current_username_domain():
    # Just the username is easy (GetUserName), but the domain takes more work.
    return process__get_username_domain_for_pid(process__get_current_pid())
