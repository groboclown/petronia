"""
Windows Vista functions
"""

from typing import Sequence, Tuple, List, Callable, Union, Optional
import codecs
import subprocess
import re
import atexit
from .windows_common import (
    c_int,
    LONG, DWORD, BYTE, CHAR, BOOL, UINT, LRESULT,
    POINT, RECT, WPARAM, LPARAM, HWND,
    windll, Structure,
    byref, create_unicode_buffer,
    MessageCallback, NativeMessageCallback,
    WindowsErrorMessage,
)
from ctypes import CFUNCTYPE, WinError
from ctypes import sizeof as c_sizeof
from ..windows_constants import *
from .supported_functions import (
    Functions,
)
from .window_metrics import WindowMetrics, FontMetrics


def load_functions(environ: Dict[str, str], func_map: Functions) -> None:
    # TODO also detect Windows Serve r2008
    if environ['system'].lower() == 'windows' and environ['release'].lower() == 'vista':
        load_all_functions(func_map)


def load_all_functions(func_map: Functions) -> None:
    from .funcs_winXP import load_psapi_functions, load_taskbar_functions
    load_psapi_functions(func_map)
    load_taskbar_functions(func_map)
    func_map.shell.find_notification_icons = create_shell__find_notification_icons(func_map)
    func_map.process.load_all_process_details = process__load_all_process_details
    func_map.shell.get_window_metrics = shell__get_window_metrics
    func_map.shell.set_window_metrics = shell__set_window_metrics
    func_map.shell.set_border_size = shell__set_border_size
    func_map.shell.open_start_menu = shell__open_start_menu
    func_map.window.create_borderless_window = create_window__create_borderless_window(func_map)


def create_shell__find_notification_icons(func_map: Functions) -> Optional[Callable[[], Sequence[HWND]]]:
    if not func_map.window.find_handle_for_child_class_title:
        return None
    find_window_ex = func_map.window.find_handle_for_child_class_title
    if not func_map.shell.get_task_bar_window_handles:
        return None
    shell__get_task_bar_window_handles = func_map.shell.get_task_bar_window_handles

    def fw(parent: Optional[HWND], class_name: str) -> Optional[HWND]:
        if not parent:
            return None
        return find_window_ex(parent, None, class_name, "")

    def f() -> Sequence[HWND]:
        ret: List[HWND] = []
        # Only need one handle
        taskbars = shell__get_task_bar_window_handles()
        if len(taskbars) <= 0:
            # TODO proper logging
            print("No taskbars found")
            return ()
        parent_area = fw(fw(taskbars[0], "TrayNotifyWnd"), "SysPager")
        if not parent_area:
            return ()
        for title in ['User Promoted Notification Area', 'Overflow Notification Area']:
            handle = find_window_ex(
                parent_area,
                None,
                "ToolbarWindow32",
                title
            )
            if handle is not None and handle.value is not None and handle not in ret:
                # TODO get icons
                ret.append(handle)
        return ret
    return f


def process__load_all_process_details() -> Sequence[Dict[str, str]]:
    """Uses the wmic command, which was introduced in Vista"""
    with subprocess.Popen(['wmic.exe', 'process', 'list'], stdout=subprocess.PIPE) as proc:
        pdata = codecs.decode(proc.stdout.read(), 'utf-8')
    # It looks like most of the lines are split by '\r\r\n', which is weird.
    lines = re.split(r'[\r\n]', pdata)

    def next_line() -> Optional[str]:
        line = None
        while len(lines) > 0 and (line is None or len(line.strip()) <= 0):
            line = lines.pop(0)
        return line

    def find_columns(header: Optional[str]) -> Dict[str, Tuple[int, int]]:
        if not header:
            return {}
        # Format: 'Name     Name        Name     '
        r: Dict[str, Tuple[int, int]] = {}
        state = 0
        col_start = 0
        for i in range(len(header)):
            c = header[i]
            if state == 0:
                # Text of name
                if c.isspace():
                    state = 1
            elif state == 1:
                if not c.isspace():
                    name = header[col_start:i].strip()
                    r[name] = (col_start, i)
                    col_start = i
                    state = 0
        name = header[col_start:-1].strip()
        r[name] = (col_start, -1)
        return r

    # Find the column positions, based on the header
    columns = find_columns(next_line())

    ret: List[Dict[str, str]] = []
    row = next_line()
    while row is not None:
        data: Dict[str, str] = {}
        for key, cols in columns.items():
            data[key] = row[cols[0]:cols[1]].strip()
        ret.append(data)
        row = next_line()
    return ret


# https://msdn.microsoft.com/en-us/library/windows/desktop/dd145037(v=vs.85).aspx
class LOGFONT(Structure):
    _fields_ = (
        ("lfHeight", LONG),
        ("lfWidth", LONG),
        ("lfEscapement", LONG),
        ("lfOrientation", LONG),
        ("lfWeight", LONG),
        ("lfItalic", BYTE),
        ("lfUnderline", BYTE),
        ("lfStrikeOut", BYTE),
        ("lfCharSet", BYTE),
        ("lfOutPrecision", BYTE),
        ("lfClipPrecision", BYTE),
        ("lfQuality", BYTE),
        ("lfPitchAndFamily", BYTE),

        # Even though we use the W version of the call, we
        # still are expected to use CHAR, not WCHAR here.
        ("lfFaceName", CHAR * LF_FACESIZE),
    )


# https://msdn.microsoft.com/en-us/library/windows/desktop/ff729175(v=vs.85).aspx
class NONCLIENTMETRICS(Structure):
    _fields_ = (
        ("cbSize", UINT),
        ("iBorderWidth", c_int),
        ("iScrollWidth", c_int),
        ("iScrollHeight", c_int),
        ("iCaptionWidth", c_int),
        ("iCaptionHeight", c_int),
        ("lfCaptionFont", LOGFONT),
        ("iSmCaptionWidth", c_int),
        ("iSmCaptionHeight", c_int),
        ("lfSmCaptionFont", LOGFONT),
        ("iMenuWidth", c_int),
        ("iMenuHeight", c_int),
        ("lfMenuFont", LOGFONT),
        ("lfStatusFont", LOGFONT),
        ("lfMessageFont", LOGFONT),

        # Windows Vista has this extra parameter
        ("iPaddedBorderWidth", c_int)
    )


def shell__get_window_metrics() -> Union[WindowMetrics, WindowsErrorMessage]:
    metrics = shell__get_raw_window_metrics()
    if isinstance(metrics, WindowsErrorMessage):
        return metrics
    return WindowMetrics(
        border_width=metrics.iBorderWidth,
        scroll_width=metrics.iScrollWidth,
        scroll_height=metrics.iScrollHeight,
        caption_width=metrics.iCaptionWidth,
        caption_height=metrics.iCaptionHeight,
        caption_font=_font_to_dict(metrics.lfCaptionFont),
        sm_caption_width=metrics.iSmCaptionWidth,
        sm_caption_height=metrics.iSmCaptionHeight,
        sm_caption_font=_font_to_dict(metrics.lfSmCaptionFont),
        menu_width=metrics.iMenuWidth,
        menu_height=metrics.iMenuHeight,
        menu_font=_font_to_dict(metrics.lfMenuFont),
        status_font=_font_to_dict(metrics.lfStatusFont),
        message_font=_font_to_dict(metrics.lfMessageFont),
        padded_border_width=metrics.iPaddedBorderWidth
    )


def shell__get_raw_window_metrics() -> Union[NONCLIENTMETRICS, WindowsErrorMessage]:
    # First, gather the border
    SystemParametersInfoW = windll.user32.SystemParametersInfoW
    metrics = NONCLIENTMETRICS()
    metrics.cbSize = c_sizeof(NONCLIENTMETRICS)
    res = SystemParametersInfoW(SPI_GETNONCLIENTMETRICS, metrics.cbSize, byref(metrics), 0)
    if res != 0:
        return WindowsErrorMessage('user32.SystemParametersInfoW')
    return metrics


_BASE_OS_METRICS: List[Optional[NONCLIENTMETRICS]] = [None]


def shell__set_window_metrics(metrics: WindowMetrics) -> Optional[WindowsErrorMessage]:
    return inner__set_window_metrics(metrics)


def inner__set_window_metrics(metrics: Union[NONCLIENTMETRICS, WindowMetrics]) -> Optional[WindowsErrorMessage]:
    SystemParametersInfoW = windll.user32.SystemParametersInfoW

    # Always restore the original user metrics at exit time.
    root_metrics = None
    if _BASE_OS_METRICS[0] is None:
        root_metrics = shell__get_raw_window_metrics()
        if isinstance(root_metrics, WindowsErrorMessage):
            return root_metrics
        _BASE_OS_METRICS[0] = root_metrics
        atexit.register(shell__set_window_metrics, root_metrics)

    m: NONCLIENTMETRICS
    if isinstance(metrics, WindowMetrics):
        mx = root_metrics or shell__get_raw_window_metrics()
        if isinstance(mx, WindowsErrorMessage):
            return mx
        m = mx
        m.cbSize = c_sizeof(NONCLIENTMETRICS)
        m.iBorderWidth = metrics.border_width
        m.iScrollWidth = metrics.scroll_width
        m.iScrollHeight = metrics.scroll_height
        m.iCaptionWidth = metrics.caption_width
        m.iCaptionHeight = metrics.caption_height
        _dict_to_font(metrics.caption_font, m.lfCaptionFont)
        m.iSmCaptionWidth = metrics.sm_caption_width
        m.iSmCaptionHeight = metrics.sm_caption_height
        _dict_to_font(metrics.sm_caption_font, m.lfSmCaptionFont)
        m.iMenuWidth = metrics.menu_width
        m.iMenuHeight = metrics.menu_height
        _dict_to_font(metrics.menu_font, m.lfMenuFont)
        _dict_to_font(metrics.status_font, m.lfStatusFont)
        _dict_to_font(metrics.message_font, m.lfMessageFont)
    else:
        m = metrics

    m.cbSize = c_sizeof(NONCLIENTMETRICS)
    # TODO change 0 to SPIF_SENDCHANGE
    res = SystemParametersInfoW(SPI_SETNONCLIENTMETRICS, m.cbSize, byref(m), 0)
    if res != 0:
        return WindowsErrorMessage('user32.SystemParametersInfoW')
    return None


def _dict_to_font(f: FontMetrics, ret: Optional[LOGFONT] = None) -> LOGFONT:
    if ret is None:
        ret = LOGFONT()
    ret.lfHeight = f.height
    ret.lfWidth = f.width
    ret.lfEscapement = f.escapement
    ret.lfOrientation = f.orientation
    ret.lfWeight = f.weight
    ret.lfItalic = f.italic
    ret.lfUnderline = f.underline
    ret.lfStrikeOut = f.strikeout
    ret.lfCharSet = f.charset
    ret.lfOutPrecision = f.out_precision
    ret.lfClipPrecision = f.clip_precision
    ret.lfQuality = f.quality
    ret.lfPitchAndFamily = f.pitch_and_family
    if f.face_name:
        ret.lfFaceName = f.face_name[:LF_FACESIZE - 1]
    return ret


def _font_to_dict(f: LOGFONT) -> FontMetrics:
    assert isinstance(f, LOGFONT)
    return FontMetrics(
        height=f.lfHeight,
        width=f.lfWidth,
        escapement=f.lfEscapement,
        orientation=f.lfOrientation,
        weight=f.lfWeight,
        italic=f.lfItalic,
        underline=f.lfUnderline,
        strikeout=f.lfStrikeOut,
        charset=f.lfCharSet,
        out_precision=f.lfOutPrecision,
        clip_precision=f.lfClipPrecision,
        quality=f.lfQuality,
        pitch_and_family=f.lfPitchAndFamily,
        face_name=f.lfFaceName,
    )


def shell__set_border_size(border_width: int, border_padding: int) -> Optional[WindowsErrorMessage]:
    metrics = shell__get_raw_window_metrics()
    if isinstance(metrics, WindowsErrorMessage):
        return metrics
    metrics.iBorderWidth = border_width
    metrics.iPaddedBorderWidth = border_padding
    return inner__set_window_metrics(metrics)


# https://msdn.microsoft.com/en-us/library/windows/desktop/ms686735(v=vs.85).aspx
class THREADENTRY32(Structure):
    _fields_ = [
        ("dwSize", DWORD),
        ("cntUsage", DWORD),
        ("th32ThreadID", DWORD),
        ("th32OwnerProcessID", DWORD),
        ("tpBasePri", LONG),
        ("tpDeltaPri", LONG),
        ("dwFlags", DWORD),
    ]


# see https://msdn.microsoft.com/en-us/library/windows/desktop/ms632611(v=vs.85).aspx
class WINDOWPLACEMENT(Structure):
    _fields_ = [
        ("length", UINT),
        ("flags", UINT),
        ("showCmd", UINT),
        ("ptMinPosition", POINT),
        ("ptMaxPosition", POINT),
        ("rcNormalPosition", RECT),
    ]


def shell__open_start_menu(show_taskbar: bool) -> Optional[WindowsErrorMessage]:
    # Find the task bar window
    taskbar_hwnd = windll.user32.FindWindowW("Shell_TrayWnd", None)
    if taskbar_hwnd is None or 0 == taskbar_hwnd:
        return WindowsErrorMessage('user32.FindWindowW')
    taskbar_size = RECT()
    windll.user32.GetWindowRect(taskbar_hwnd, byref(taskbar_size))

    # if show_taskbar:
    #     if windll.user32.IsWindowVisible(taskbar_hwnd):
    #         placement = WINDOWPLACEMENT()
    #         placement.length = c_sizeof(WINDOWPLACEMENT)
    #         val = windll.user32.GetWindowPlacement(taskbar_hwnd, byref(placement))
    #         if val is not None:
    #             show_cmd = placement.showCmd
    #             if (show_cmd == SW_SHOWNORMAL or show_cmd == SW_MAXIMIZE or show_cmd == SW_SHOWMAXIMIZED
    #                     or show_cmd == SW_SHOWNOACTIVATE or show_cmd == SW_SHOW or show_cmd == SW_SHOWNA
    #                     or show_cmd == SW_RESTORE):
    #                 show_taskbar = False
    if show_taskbar:
        # The task bar is auto-hide.  It's always present, but not on screen.
        # The trick Windows uses is pushing it off-screen, so it's just barely
        # visible.

        windll.user32.GetWindowRect(taskbar_hwnd, byref(taskbar_size))
        # Figure out which corner it's in.  It's either top, left, right, or bottom.
        # We do this by finding a "0", which indicates where on the screen it's
        # located.  However, with strange, multi-monitor setups, this isn't always
        # correct.  But it's a good guess.
        # windll.user32.SetWindowPos(taskbar_hwnd, HWND_TOPMOST, 0, 0, 0, 0, SWP_NOSIZE | SWP_SHOWWINDOW)

        # TODO show the task bar.
        # print("<<Don't know how to show the task bar>>")

    # Find the process ID of the taskbar window.
    taskbar_pid = DWORD()
    windll.user32.GetWindowThreadProcessId(taskbar_hwnd, byref(taskbar_pid))

    # Find a thread in that process that has a "Start" button
    triggered_start = [False]

    # noinspection PyUnusedLocal
    def thread_window_callback(hwnd: HWND, lparam: LPARAM) -> bool:
        length = windll.user32.GetWindowTextLengthW(hwnd)
        if length > 0:
            buff = create_unicode_buffer(length + 1)
            windll.user32.GetWindowTextW(hwnd, buff, length + 1)
            # print("DEBUG - Inspecting {0} = {1}".format(hwnd, buff.value))
            if buff.value == "Start":
                # Found the window
                # print("DEBUG sending Click message")
                m_res = windll.user32.SendMessageW(hwnd, BM_CLICK, 0, 0)
                if m_res != 0:
                    # Don't look anymore
                    triggered_start[0] = True
                    return False
                else:
                    try:
                        print("<<ERROR pressing start button>>")
                        raise WinError()
                    except OSError:
                        import traceback
                        traceback.print_exc()
            if buff.value == "Start menu":
                triggered_start[0] = True
                if windll.user32.IsWindowVisible(hwnd):
                    p = WINDOWPLACEMENT()
                    p.length = c_sizeof(WINDOWPLACEMENT)
                    val = windll.user32.GetWindowPlacement(hwnd, byref(p))
                    if val is not None:
                        show_cmd = p.showCmd
                        if (show_cmd == SW_SHOWNORMAL or show_cmd == SW_MAXIMIZE or show_cmd == SW_SHOWMAXIMIZED
                                or show_cmd == SW_SHOWNOACTIVATE or show_cmd == SW_SHOW or show_cmd == SW_SHOWNA
                                or show_cmd == SW_RESTORE):
                            # Hide the window
                            # print("DEBUG hiding the start menu {0}".format(show_cmd))
                            windll.user32.ShowWindow(hwnd, SW_HIDE)
                            return False
                # print("DEBUG showing the start menu ({0})".format(placement.showCmd))
                windll.user32.ShowWindow(hwnd, SW_SHOW)

                # If the task bar is hidden, then part of the start window is not shown fully.
                # SW_MAXIMIZE will show it fully, but the rendering becomes messed up.
                taskbar_rect = RECT()
                windll.user32.GetClientRect(taskbar_hwnd, byref(taskbar_rect))

                client_rect = RECT()
                windll.user32.GetClientRect(hwnd, byref(client_rect))

                overlap_rect = RECT()
                if windll.user32.IntersectRect(byref(overlap_rect), byref(taskbar_rect), byref(client_rect)) != 0:
                    # The taskbar and the start window rectangles overlap each other.
                    # Adjust the start window to be outside of this.
                    # Remember: the taskbar can be anywhere on the edge of the screen.
                    new_x = client_rect.left.value
                    new_y = client_rect.top.value
                    if (
                            overlap_rect.left.value == client_rect.left.value and
                            overlap_rect.right.value == client_rect.right.value
                    ):
                        # Adjust along the y axis
                        if overlap_rect.top.value <= client_rect.top.value <= overlap_rect.bottom.value:
                            # Adjust down
                            new_y = overlap_rect.bottom.value
                        else:
                            # Adjust up
                            new_y = client_rect.top.value - (overlap_rect.bottom.value - overlap_rect.top.value)
                    else:
                        # Adjust along the x axis
                        if overlap_rect.left.value <= client_rect.left.value <= overlap_rect.right.value:
                            # Adjust to the right
                            new_x = overlap_rect.right.value
                        else:
                            new_x = client_rect.left.value - (overlap_rect.right.value - overlap_rect.left.value)
                    windll.user32.SetWindowPos(
                        hwnd, None, new_x, new_y,
                        0, 0, SWP_NOSIZE)

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

                return False
        # else:
        #     print("DEBUG - Inspecting {0} => no title, ignoring".format(hwnd))
        return True

    # Find the threads for the process ID
    thread_ids = []
    hsnapshot = windll.kernel32.CreateToolhelp32Snapshot(TH32CS_SNAPTHREAD, taskbar_pid)
    if hsnapshot == INVALID_HANDLE_VALUE:
        raise WinError()
    try:
        thread_entry = THREADENTRY32()
        thread_entry.dwSize = c_sizeof(THREADENTRY32)

        # print("DEBUG Getting threads for pid {0}".format(taskbar_pid))
        res = windll.kernel32.Thread32First(hsnapshot, byref(thread_entry))
        # print("DEBUG :: first: {0}".format(res))
        if res == 0:
            return WindowsErrorMessage('kernel32.Thread32First')
        while res != 0:
            if thread_entry.dwSize > THREADENTRY32.th32OwnerProcessID.offset:
                thread_ids.append(thread_entry.th32ThreadID)
            # else:
            #     print("DEBUG - returned too small size {0}".format(thread_entry.dwSize))
            thread_entry.dwSize = c_sizeof(THREADENTRY32)
            res = windll.kernel32.Thread32Next(hsnapshot, byref(thread_entry))
            # print("DEBUG :: next: {0}".format(res))
    finally:
        windll.kernel32.CloseHandle(hsnapshot)

    callback_type = CFUNCTYPE(BOOL, HWND, LPARAM)
    callback_ptr = callback_type(thread_window_callback)
    for thread_id in thread_ids:
        # print("DEBUG Iterating over windows for thread {0} in pid {1}".format(thread_id, taskbar_pid))
        windll.user32.EnumThreadWindows(thread_id, callback_ptr, 0)
        if triggered_start[0]:
            return None

    return WindowsErrorMessage("Could not find start button")


# https://msdn.microsoft.com/en-us/library/windows/desktop/bb773244(v=vs.85).aspx
class MARGINS(Structure):
    _fields_ = [
        ("cxLeftWidth", c_int),
        ("cxRightWidth", c_int),
        ("cyTopHeight", c_int),
        ("cyBottomHeight", c_int),
    ]


def create_window__create_borderless_window(
        func_map: Functions
) -> Callable[
        [str, str, MessageCallback, Dict[int, MessageCallback], Optional[bool], Optional[bool]],
        Union[HWND, WindowsErrorMessage]
]:
    # Use an inner window, so that we can use the func_map for accessing other functions
    # that are OS specific.

    # Call out to the answer:
    # http://stackoverflow.com/questions/39731497/create-window-without-titlebar-with-resizable-border-and-without-bogus-6px-whit/39735058

    # However, the WM_CREATE just doesn't work right - it causes windows to
    # be automatically closed, even when 0 is explicitly returned.

    def window__create_borderless_window(
            class_name: str, title: str,
            message_handler: MessageCallback,
            callback_map: Dict[int, MessageCallback],
            show_on_taskbar: Optional[bool] = True,
            always_on_top: Optional[bool] = False
    ) -> Union[HWND, WindowsErrorMessage]:
        margins = MARGINS()
        margins.cxLeftWidth = 0
        margins.cxRightWidth = 0
        margins.cyTopHeight = 0
        margins.cyBottomHeight = 0

        style_flags = {
            'popup', 'visible',
            # 'layered',   This causes the windows to not show up.
            'transparent'
        }
        if always_on_top:
            style_flags.add('topmost')
        if not show_on_taskbar:
            style_flags.add('tool-window')

        def hit_test(_hwnd: HWND, _msg: int, _wparam: WPARAM, _lparam: LPARAM) -> bool:
            # We don't have a border, so don't worry about
            # border cursor checks.
            # pt = wintypes.POINT()

            # x in low word, y in the high word
            # pt.x = wintypes.DWORD(lparam & 0xffff)
            # pt.y = wintypes.DWORD((lparam >> 16) & 0xffff)
            # windll.user32.ScreenToClient(hwnd, byref(pt))

            # rc = wintypes.RECT()
            # windll.user32.GetClientRect(hwnd, byref(rc))
            # return HTCLIENT
            return True

        def zero(_hwnd: HWND, _msg: int, _wparam: WPARAM, _lparam: LPARAM) -> bool:
            # return 0
            return False

        callback_map[WM_NCACTIVATE] = zero
        callback_map[WM_NCCALCSIZE] = zero
        callback_map[WM_NCHITTEST] = hit_test

        if func_map.window.create_display_window:
            hwnd = func_map.window.create_display_window(class_name, title, message_handler, style_flags)
            # windll.dwmapi.DwmExtendFrameIntoClientArea(hwnd, byref(margins))
            return hwnd
        return WindowsErrorMessage('not supported')

    return window__create_borderless_window
