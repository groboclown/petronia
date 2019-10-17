"""
Windows Vista functions
"""

import codecs
import subprocess
import re
import atexit
from ctypes import c_int, wintypes, windll, Structure, WinError, byref, create_unicode_buffer, CFUNCTYPE
from ctypes import sizeof as c_sizeof
from .windows_constants import *


def load_functions(environ, func_map):
    # TODO also detect Windows Serve r2008
    if environ['system'].lower() == 'windows' and environ['release'].lower() == 'vista':
        load_all_functions(func_map)


def load_all_functions(func_map):
    from .funcs_winXP import load_psapi_functions, load_taskbar_functions
    load_psapi_functions(func_map)
    load_taskbar_functions(func_map)
    func_map['shell__find_notification_icons'] = shell__find_notification_icons(func_map)
    func_map['process__load_all_process_details'] = process__load_all_process_details
    func_map['shell__get_window_metrics'] = shell__get_window_metrics
    func_map['shell__get_raw_window_metrics'] = shell__get_raw_window_metrics
    func_map['shell__set_window_metrics'] = shell__set_window_metrics
    func_map['shell__set_border_size'] = shell__set_border_size
    func_map['shell__open_start_menu'] = shell__open_start_menu
    func_map['window__create_borderless_window'] = create_window__create_borderless_window(func_map)


def shell__find_notification_icons(func_map):
    find_window_ex = func_map['window__find_handle_for_child_class_title']
    shell__get_task_bar_window_handles = func_map['shell__get_task_bar_window_handles']

    def fw(parent, class_name):
        return find_window_ex(parent, None, class_name, "")

    def f():
        ret = []
        # Only need one handle
        taskbars = shell__get_task_bar_window_handles()
        if len(taskbars) <= 0:
            # TODO proper logging
            print("No taskbars found")
            return []
        parent_area = fw(fw(taskbars[0], "TrayNotifyWnd"), "SysPager")
        for title in ['User Promoted Notification Area', 'Overflow Notification Area']:
            handle = find_window_ex(
                parent_area,
                None,
                "ToolbarWindow32",
                title
            )
            if handle is not None:
                # TODO get icons
                ret.append(handle)
        return ret
    return f


def process__load_all_process_details():
    """Uses the wmic command, which was introduced in Vista"""
    with subprocess.Popen(['wmic.exe', 'process', 'list'], stdout=subprocess.PIPE) as proc:
        data = codecs.decode(proc.stdout.read(), 'utf-8')
    # It looks like most of the lines are split by '\r\r\n', which is weird.
    lines = re.split(r'\r|\n', data)

    def next_line():
        line = None
        while len(lines) > 0 and (line is None or len(line.strip()) <= 0):
            line = lines.pop(0)
        return line

    def find_columns(header):
        # Format: 'Name     Name        Name     '
        r = {}
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

    ret = []
    row = next_line()
    while row is not None:
        data = {}
        for key, cols in columns.items():
            data[key] = row[cols[0]:cols[1]].strip()
        ret.append(data)
        row = next_line()
    return ret


# https://msdn.microsoft.com/en-us/library/windows/desktop/dd145037(v=vs.85).aspx
class LOGFONT(Structure):
    _fields_ = [
        ("lfHeight", wintypes.LONG),
        ("lfWidth", wintypes.LONG),
        ("lfEscapement", wintypes.LONG),
        ("lfOrientation", wintypes.LONG),
        ("lfWeight", wintypes.LONG),
        ("lfItalic", wintypes.BYTE),
        ("lfUnderline", wintypes.BYTE),
        ("lfStrikeOut", wintypes.BYTE),
        ("lfCharSet", wintypes.BYTE),
        ("lfOutPrecision", wintypes.BYTE),
        ("lfClipPrecision", wintypes.BYTE),
        ("lfQuality", wintypes.BYTE),
        ("lfPitchAndFamily", wintypes.BYTE),

        # Even though we use the W version of the call, we
        # still are expected to use CHAR, not WCHAR here.
        ("lfFaceName", wintypes.CHAR * LF_FACESIZE),
    ]


# https://msdn.microsoft.com/en-us/library/windows/desktop/ff729175(v=vs.85).aspx
class NONCLIENTMETRICS(Structure):
    _fields_ = [
        ("cbSize", wintypes.UINT),
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
    ]


def shell__get_window_metrics():
    metrics = shell__get_raw_window_metrics()
    return {
        'border-width': metrics.iBorderWidth,
        'scroll-width': metrics.iScrollWidth,
        'scroll-height': metrics.iScrollHeight,
        'caption-width': metrics.iCaptionWidth,
        'caption-height': metrics.iCaptionHeight,
        'caption-font': _font_to_dict(metrics.lfCaptionFont),
        'sm-caption-width': metrics.iSmCaptionWidth,
        'sm-caption-height': metrics.iSmCaptionHeight,
        'sm-caption-font': _font_to_dict(metrics.lfSmCaptionFont),
        'menu-width': metrics.iMenuWidth,
        'menu-height': metrics.iMenuHeight,
        'menu-font': _font_to_dict(metrics.lfMenuFont),
        'status-font': _font_to_dict(metrics.lfStatusFont),
        'message-font': _font_to_dict(metrics.lfMessageFont),
        'padded-border-width': metrics.iPaddedBorderWidth,
    }


def shell__get_raw_window_metrics():
    # First, gather the border
    SystemParametersInfoW = windll.user32.SystemParametersInfoW
    metrics = NONCLIENTMETRICS()
    metrics.cbSize = c_sizeof(NONCLIENTMETRICS)
    res = SystemParametersInfoW(SPI_GETNONCLIENTMETRICS, metrics.cbSize, byref(metrics), 0)
    if res != 0:
        raise WinError()
    return metrics


_BASE_OS_METRICS = [None]


def shell__set_window_metrics(metrics):
    SystemParametersInfoW = windll.user32.SystemParametersInfoW

    # Always restore the original user metrics at exit time.
    root_metrics = None
    if _BASE_OS_METRICS[0] is None:
        root_metrics = shell__get_raw_window_metrics()
        _BASE_OS_METRICS[0] = root_metrics
        atexit.register(shell__set_window_metrics, root_metrics)

    if isinstance(metrics, dict):
        m = root_metrics or shell__get_raw_window_metrics()
        m.cbSize = c_sizeof(NONCLIENTMETRICS)
        if 'border-width' in metrics:
            m.iBorderWidth = metrics['border-width']
        if 'scroll-width' in metrics:
            m.iScrollWidth = metrics['scroll-width']
        if 'scroll-height' in metrics:
            m.iScrollHeight = metrics['scroll-height']
        if 'caption-width' in metrics:
            m.iCaptionWidth = metrics['caption-width']
        if 'caption-height' in metrics:
            m.iCaptionHeight = metrics['caption-height']
        if 'caption-font' in metrics:
            m.lfCaptionFont = _dict_to_font(metrics['caption-font'], m.lfCaptionFont)
        if 'sm-caption-width' in metrics:
            m.iSmCaptionWidth = metrics['sm-caption-width']
        if 'sm-caption-height' in metrics:
            m.iSmCaptionHeight = metrics['sm-caption-height']
        if 'sm-caption-font' in metrics:
            m.lfSmCaptionFont = _dict_to_font(metrics['sm-caption-font'], m.lfSmCaptionFont)
        if 'menu-width' in metrics:
            m.iMenuWidth = metrics['menu-width']
        if 'menu-height' in metrics:
            m.iMenuHeight = metrics['menu-height']
        if 'menu-font' in metrics:
            m.lfMenuFont = _dict_to_font(metrics[''], m.lfMenuFont)
        if 'status-font' in metrics:
            m.lfStatusFont = _dict_to_font(metrics['status-font'], m.lfStatusFont)
        if 'message-font' in metrics:
            m.lfMessageFont = _dict_to_font(metrics['message-font'], m.lfMessageFont)
        metrics = m

    assert isinstance(metrics, NONCLIENTMETRICS)
    metrics.cbSize = c_sizeof(NONCLIENTMETRICS)
    # TODO change 0 to SPIF_SENDCHANGE
    res = SystemParametersInfoW(SPI_SETNONCLIENTMETRICS, metrics.cbSize, byref(metrics), 0)
    if res != 0:
        raise WinError()


def _dict_to_font(f, ret=None):
    assert isinstance(f, dict)
    if ret is None:
        ret = LOGFONT()
    if 'height' in f:
        ret.lfHeight = f['height']
    if 'width' in f:
        ret.lfWidth = f['width']
    if 'escapement' in f:
        ret.lfEscapement = f['escapement']
    if 'orientation' in f:
        ret.lfOrientation = f['orientation']
    if 'weight' in f:
        ret.lfWeight = f['weight']
    if 'italic' in f:
        ret.lfItalic = f['italic']
    if 'underline' in f:
        ret.lfUnderline = f['underline']
    if 'strike-out' in f:
        ret.lfStrikeOut = f['strike-out']
    if 'char-set' in f:
        ret.lfCharSet = f['char-set']
    if 'out-precision' in f:
        ret.lfOutPrecision = f['out-precision']
    if 'clip-precision' in f:
        ret.lfClipPrecision = f['clip-precision']
    if 'quality' in f:
        ret.lfQuality = f['quality']
    if 'pitch-and-family' in f:
        ret.lfPitchAndFamily = f['pitch-and-family']
    if 'face-name' in f:
        ret.lfFaceName = f['face-name'][:LF_FACESIZE - 1]
    return ret


def _font_to_dict(f):
    assert isinstance(f, LOGFONT)
    return {
        'height': f.lfHeight,
        'width': f.lfWidth,
        'escapement': f.lfEscapement,
        'orientation': f.lfOrientation,
        'weight': f.lfWeight,
        'italic': f.lfItalic,
        'underline': f.lfUnderline,
        'strike-out': f.lfStrikeOut,
        'char-set': f.lfCharSet,
        'out-precision': f.lfOutPrecision,
        'clip-precision': f.lfClipPrecision,
        'quality': f.lfQuality,
        'pitch-and-family': f.lfPitchAndFamily,
        'face-name': f.lfFaceName,
    }


def shell__set_border_size(border_width, border_padding):
    metrics = shell__get_raw_window_metrics()
    metrics.iBorderWidth = border_width
    metrics.iPaddedBorderWidth = border_padding
    shell__set_window_metrics(metrics)


# https://msdn.microsoft.com/en-us/library/windows/desktop/ms686735(v=vs.85).aspx
class THREADENTRY32(Structure):
    _fields_ = [
        ("dwSize", wintypes.DWORD),
        ("cntUsage", wintypes.DWORD),
        ("th32ThreadID", wintypes.DWORD),
        ("th32OwnerProcessID", wintypes.DWORD),
        ("tpBasePri", wintypes.LONG),
        ("tpDeltaPri", wintypes.LONG),
        ("dwFlags", wintypes.DWORD),
    ]


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


def shell__open_start_menu(show_taskbar):
    # Find the task bar window
    taskbar_hwnd = windll.user32.FindWindowW("Shell_TrayWnd", None)
    if taskbar_hwnd is None or 0 == taskbar_hwnd:
        raise WinError()
    taskbar_size = wintypes.RECT()
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
    taskbar_pid = wintypes.DWORD()
    windll.user32.GetWindowThreadProcessId(taskbar_hwnd, byref(taskbar_pid))

    # Find a thread in that process that has a "Start" button
    triggered_start = [False]

    # noinspection PyUnusedLocal
    def thread_window_callback(hwnd, lparam):
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
                taskbar_rect = wintypes.RECT()
                windll.user32.GetClientRect(taskbar_hwnd, byref(taskbar_rect))

                client_rect = wintypes.RECT()
                windll.user32.GetClientRect(hwnd, byref(client_rect))

                overlap_rect = wintypes.RECT()
                if windll.user32.IntersectRect(byref(overlap_rect), byref(taskbar_rect), byref(client_rect)) != 0:
                    # The taskbar and the start window rectangles overlap each other.
                    # Adjust the start window to be outside of this.
                    # Remember: the taskbar can be anywhere on the edge of the screen.
                    new_x = client_rect.left
                    new_y = client_rect.top
                    if overlap_rect.left == client_rect.left and overlap_rect.right == client_rect.right:
                        # Adjust along the y axis
                        if overlap_rect.top <= client_rect.top <= overlap_rect.bottom:
                            # Adjust down
                            new_y = overlap_rect.bottom
                        else:
                            # Adjust up
                            new_y = client_rect.top - (overlap_rect.bottom - overlap_rect.top)
                    else:
                        # Adjust along the x axis
                        if overlap_rect.left <= client_rect.left <= overlap_rect.right:
                            # Adjust to the right
                            new_x = overlap_rect.right
                        else:
                            new_x = client_rect.left - (overlap_rect.right - overlap_rect.left)
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
            raise WinError()
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

    callback_type = CFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)
    callback_ptr = callback_type(thread_window_callback)
    for thread_id in thread_ids:
        # print("DEBUG Iterating over windows for thread {0} in pid {1}".format(thread_id, taskbar_pid))
        windll.user32.EnumThreadWindows(thread_id, callback_ptr, 0)
        if triggered_start[0]:
            return

    raise OSError("Could not find start button")


# https://msdn.microsoft.com/en-us/library/windows/desktop/bb773244(v=vs.85).aspx
class MARGINS(Structure):
    _fields_ = [
        ("cxLeftWidth", c_int),
        ("cxRightWidth", c_int),
        ("cyTopHeight", c_int),
        ("cyBottomHeight", c_int),
    ]


def create_window__create_borderless_window(func_map):
    # Use an inner window, so that we can use the func_map for accessing other functions
    # that are OS specific.

    # Call out to the answer:
    # http://stackoverflow.com/questions/39731497/create-window-without-titlebar-with-resizable-border-and-without-bogus-6px-whit/39735058

    # However, the WM_CREATE just doesn't work right - it causes windows to
    # be automatically closed, even when 0 is explicitly returned.

    def window__create_borderless_window(class_name, title, message_handler, callback_map,
                                         show_on_taskbar=True, always_on_top=False):
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

        def hit_test(hwnd, msg, wparam, lparam):
            # We don't have a border, so don't worry about
            # border cursor checks.
            # pt = wintypes.POINT()

            # x in low word, y in the high word
            # pt.x = wintypes.DWORD(lparam & 0xffff)
            # pt.y = wintypes.DWORD((lparam >> 16) & 0xffff)
            # windll.user32.ScreenToClient(hwnd, byref(pt))

            # rc = wintypes.RECT()
            # windll.user32.GetClientRect(hwnd, byref(rc))
            return HTCLIENT

        callback_map[WM_NCACTIVATE] = lambda hwnd, msg, wparam, lparam: 0
        callback_map[WM_NCCALCSIZE] = lambda hwnd, msg, wparam, lparam: lparam == 0 and 0 or False
        callback_map[WM_NCHITTEST] = hit_test

        hwnd = func_map['window__create_display_window'](class_name, title, message_handler, style_flags)
        # windll.dwmapi.DwmExtendFrameIntoClientArea(hwnd, byref(margins))

        return hwnd

    return window__create_borderless_window
