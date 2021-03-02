"""
Windows Vista functions
"""

# Many places use Windows naming convention for things, not Python.
# pylint:disable=invalid-name

from typing import Sequence, Dict, Tuple, List, Callable, Union, Optional
import codecs

# Need to be aware of the issues with calling out to a subprocess...
import subprocess  # nosec

import re
import atexit
import traceback
from ctypes import CFUNCTYPE, WinError, windll
from ctypes import sizeof as c_sizeof
from petronia_common.util import StdRet, not_none, RET_OK_NONE
from petronia_common.util import i18n as _
from petronia_native.common import log, user_messages
from .windows_common import (
    c_int,
    LONG, DWORD, BYTE, CHAR, BOOL, UINT,
    POINT, RECT, WPARAM, LPARAM, HWND,
    windll, Structure,
    byref, create_unicode_buffer,
    MessageCallback,
    WindowsReturnError,
)
from .supported_functions import (
    Functions,
)
from .window_metrics import WindowMetrics, FontMetrics
from ..windows_constants import (
    LF_FACESIZE,
    SPI_GETNONCLIENTMETRICS, SPI_SETNONCLIENTMETRICS,
    BM_CLICK,
    SW_SHOWNORMAL, SW_MAXIMIZE, SW_SHOWMAXIMIZED, SW_SHOWNOACTIVATE, SW_SHOW, SW_SHOWNA,
    SW_RESTORE, SW_HIDE, SWP_NOSIZE, SWP_NOMOVE,
    HWND_TOPMOST, HWND_NOTOPMOST,
    TH32CS_SNAPTHREAD,
    INVALID_HANDLE_VALUE,
    WM_NCACTIVATE, WM_NCCALCSIZE, WM_NCHITTEST,
    NOTIFY_FOR_ALL_SESSIONS, NOTIFY_FOR_THIS_SESSION,
)


def load_functions(environ: Dict[str, str], func_map: Functions) -> None:
    """Load all the functions, if this is running on Windows Vista."""
    if (
            environ['system'].lower() == 'windows'
            and environ['release'].lower() in ('6', 'vista', '2008server')
    ):
        load_all_functions(func_map)


def load_all_functions(func_map: Functions) -> None:
    """Load all the functions."""
    from .funcs_win_xp import load_psapi_functions, load_taskbar_functions  # pylint:disable=import-outside-toplevel
    load_psapi_functions(func_map)
    load_taskbar_functions(func_map)
    func_map.shell.find_notification_icons = create_shell__find_notification_icons(func_map)
    func_map.process.load_all_process_details = process__load_all_process_details
    func_map.monitor.set_native_dpi_awareness = monitor__set_native_dpi_awareness
    func_map.shell.register_session_notification = shell__register_session_notification
    func_map.shell.unregister_session_notification = shell__unregister_session_notification
    func_map.shell.get_window_metrics = shell__get_window_metrics
    func_map.shell.set_window_metrics = shell__set_window_metrics
    func_map.shell.set_border_size = shell__set_border_size
    func_map.shell.open_start_menu = shell__open_start_menu
    func_map.window.create_borderless_window = create_window__create_borderless_window(func_map)


def create_shell__find_notification_icons(
        func_map: Functions,
) -> Optional[Callable[[], Sequence[HWND]]]:
    """Find the notifications icons area on the task bar."""
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
            log.info("No taskbars found")
            return ()
        parent_area = fw(fw(taskbars[0], "TrayNotifyWnd"), "SysPager")
        if not parent_area:
            return ()
        for title in ['User Promoted Notification Area', 'Overflow Notification Area']:
            handle = find_window_ex(
                parent_area,
                None,
                "ToolbarWindow32",
                title,
            )
            if handle is not None and handle.value is not None and handle not in ret:
                # TODO get icons
                ret.append(handle)
        return ret
    return f


def process__load_all_process_details() -> Sequence[Dict[str, str]]:
    """Uses the wmic command, which was introduced in Vista"""

    # This calls out to an external process, but there is no user input to the arguments
    # which would cause a security issue.
    try:
        with subprocess.Popen(  # nosec
                ['wmic.exe', 'process', 'list'], stdout=subprocess.PIPE,
        ) as proc:
            pdata = codecs.decode(not_none(proc.stdout).read(), 'utf-8')
    except Exception as err:  # pylint:disable=broad-except
        # This can be a decoding issue, an execution issue, or any number of other problems.
        log.error('Failed to run wmic process: {err}', err=err)
        return []

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
        for i in range(len(header)):  # pylint:disable=consider-using-enumerate
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


def monitor__set_native_dpi_awareness() -> StdRet[None]:
    """Set the native DPI awareness for this process."""
    # In Windows Vista and Windows 7, this is the equivalent of turning on
    # system DPI aware mode:
    # This app does not scale for DPI changes.
    # It will query for the DPI once and use that value for the
    # lifetime of the app. If the DPI changes, the app will not
    # adjust to the new DPI value. It will be automatically scaled
    # up or down by the system when the DPI changes from the system
    # value.
    res = windll.user32.SetProcessDPIAware()
    return WindowsReturnError.checked_stdret('user32.SetProcessDPIAware', res)


def shell__register_session_notification(
        receiving_window: HWND, for_all_sessions: bool,
) -> StdRet[None]:
    """Register the receiving window with notifications about the session."""
    res = windll.wtsapi32.WTSRegisterSessionNotification(
        receiving_window,
        NOTIFY_FOR_ALL_SESSIONS if for_all_sessions else NOTIFY_FOR_THIS_SESSION,
    )
    return WindowsReturnError.checked_stdret('wtsapi32.WTSRegisterSessionNotification', res)


def shell__unregister_session_notification(receiving_window: HWND) -> StdRet[None]:
    """Unregister from the shell__register_session_notification call.  Must be done."""
    res = windll.wtsapi32.WTSUnRegisterSessionNotification(receiving_window)
    return WindowsReturnError.checked_stdret('wtsapi32.WTSUnRegisterSessionNotification', res)


class LOGFONT(Structure):  # pylint:disable=too-many-instance-attributes
    """The LOGFONT structure
    see https://msdn.microsoft.com/en-us/library/windows/desktop/dd145037(v=vs.85).aspx"""
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


class NONCLIENTMETRICS(Structure):
    """The NONCLIENTMETRICS structure
    see https://msdn.microsoft.com/en-us/library/windows/desktop/ff729175(v=vs.85).aspx"""
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
        ("iPaddedBorderWidth", c_int),
    )


def shell__get_window_metrics() -> StdRet[WindowMetrics]:
    """Get the global window metrics."""
    metrics_res = shell__get_raw_window_metrics()
    if metrics_res.has_error:
        return metrics_res.forward()
    metrics = metrics_res.result
    return StdRet.pass_ok(WindowMetrics(
        # pylint is confused about what type metrics is.
        # pylint also thinks that metrics is a WindowsErrorMessage, even though it's
        # explicitly checked for and returned above.
        border_width=metrics.iBorderWidth,  # pylint:disable=attribute-defined-outside-init,no-member
        scroll_width=metrics.iScrollWidth,  # pylint:disable=attribute-defined-outside-init,no-member
        scroll_height=metrics.iScrollHeight,  # pylint:disable=attribute-defined-outside-init,no-member
        caption_width=metrics.iCaptionWidth,  # pylint:disable=attribute-defined-outside-init,no-member
        caption_height=metrics.iCaptionHeight,  # pylint:disable=attribute-defined-outside-init,no-member
        caption_font=_font_to_dict(metrics.lfCaptionFont),  # pylint:disable=attribute-defined-outside-init,no-member
        sm_caption_width=metrics.iSmCaptionWidth,  # pylint:disable=attribute-defined-outside-init,no-member
        sm_caption_height=metrics.iSmCaptionHeight,  # pylint:disable=attribute-defined-outside-init,no-member
        sm_caption_font=_font_to_dict(metrics.lfSmCaptionFont),  # pylint:disable=attribute-defined-outside-init,no-member
        menu_width=metrics.iMenuWidth,  # pylint:disable=attribute-defined-outside-init,no-member
        menu_height=metrics.iMenuHeight,  # pylint:disable=attribute-defined-outside-init,no-member
        menu_font=_font_to_dict(metrics.lfMenuFont),  # pylint:disable=attribute-defined-outside-init,no-member
        status_font=_font_to_dict(metrics.lfStatusFont),  # pylint:disable=attribute-defined-outside-init,no-member
        message_font=_font_to_dict(metrics.lfMessageFont),  # pylint:disable=attribute-defined-outside-init,no-member
        padded_border_width=metrics.iPaddedBorderWidth,  # pylint:disable=attribute-defined-outside-init,no-member
    ))


def shell__get_raw_window_metrics() -> StdRet[NONCLIENTMETRICS]:
    """Get the raw window metrics."""
    # First, gather the border
    SystemParametersInfoW = windll.user32.SystemParametersInfoW
    metrics = NONCLIENTMETRICS()
    # pylint is confused by structures.
    metrics.cbSize = c_sizeof(NONCLIENTMETRICS)  # pylint:disable=attribute-defined-outside-init
    res = SystemParametersInfoW(SPI_GETNONCLIENTMETRICS, metrics.cbSize, byref(metrics), 0)
    if res == 0:
        return WindowsReturnError.stdret('user32.SystemParametersInfoW')
    return StdRet.pass_ok(metrics)


_BASE_OS_METRICS: List[Optional[NONCLIENTMETRICS]] = [None]


def shell__set_window_metrics(metrics: WindowMetrics) -> StdRet[None]:
    """Set the window metrics"""
    return inner__set_window_metrics(metrics)


def inner__set_window_metrics(
        metrics: Union[NONCLIENTMETRICS, WindowMetrics],
) -> StdRet[None]:
    """Set the windows metrics."""
    SystemParametersInfoW = windll.user32.SystemParametersInfoW

    # Always actions the original user metrics at exit time.
    root_metrics = None
    if _BASE_OS_METRICS[0] is None:
        root_metrics = shell__get_raw_window_metrics()
        if root_metrics.has_error:
            return root_metrics.forward()
        _BASE_OS_METRICS[0] = root_metrics.result
        atexit.register(shell__set_window_metrics, root_metrics.result)

    m: NONCLIENTMETRICS
    if isinstance(metrics, WindowMetrics):
        mx = root_metrics or shell__get_raw_window_metrics()
        if mx.has_error:
            return mx.forward()
        m = mx.result
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
    return WindowsReturnError.checked_stdret('user32.SystemParametersInfoW', res)


def _dict_to_font(f: FontMetrics, ret: Optional[LOGFONT] = None) -> LOGFONT:
    if ret is None:
        ret = LOGFONT()
    # pylint doesn't understand what LOGFONT is.
    ret.lfHeight = f.height  # pylint:disable=attribute-defined-outside-init
    ret.lfWidth = f.width  # pylint:disable=attribute-defined-outside-init
    ret.lfEscapement = f.escapement  # pylint:disable=attribute-defined-outside-init
    ret.lfOrientation = f.orientation  # pylint:disable=attribute-defined-outside-init
    ret.lfWeight = f.weight  # pylint:disable=attribute-defined-outside-init
    ret.lfItalic = f.italic  # pylint:disable=attribute-defined-outside-init
    ret.lfUnderline = f.underline  # pylint:disable=attribute-defined-outside-init
    ret.lfStrikeOut = f.strikeout  # pylint:disable=attribute-defined-outside-init
    ret.lfCharSet = f.charset  # pylint:disable=attribute-defined-outside-init
    ret.lfOutPrecision = f.out_precision  # pylint:disable=attribute-defined-outside-init
    ret.lfClipPrecision = f.clip_precision  # pylint:disable=attribute-defined-outside-init
    ret.lfQuality = f.quality  # pylint:disable=attribute-defined-outside-init
    ret.lfPitchAndFamily = f.pitch_and_family  # pylint:disable=attribute-defined-outside-init
    if f.face_name:  # pylint:disable=attribute-defined-outside-init
        ret.lfFaceName = f.face_name[:LF_FACESIZE - 1]  # pylint:disable=attribute-defined-outside-init
    return ret


def _font_to_dict(f: LOGFONT) -> FontMetrics:
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


def shell__set_border_size(border_width: int, border_padding: int) -> StdRet[None]:
    """Set the global border size for the standard Windows shell."""
    metrics_res = shell__get_raw_window_metrics()
    if metrics_res.has_error:
        return metrics_res.forward()
    # pylint is confused by this structure.
    metrics = metrics_res.result
    metrics.iBorderWidth = border_width  # pylint:disable=attribute-defined-outside-init
    metrics.iPaddedBorderWidth = border_padding  # pylint:disable=attribute-defined-outside-init
    return inner__set_window_metrics(metrics)


class THREADENTRY32(Structure):
    """The THREADENTRY32 structure
    see https://msdn.microsoft.com/en-us/library/windows/desktop/ms686735(v=vs.85).aspx"""
    _fields_ = [
        ("dwSize", DWORD),
        ("cntUsage", DWORD),
        ("th32ThreadID", DWORD),
        ("th32OwnerProcessID", DWORD),
        ("tpBasePri", LONG),
        ("tpDeltaPri", LONG),
        ("dwFlags", DWORD),
    ]


class WINDOWPLACEMENT(Structure):
    """The WINDOWPLACEMENT structure.
    see see https://msdn.microsoft.com/en-us/library/windows/desktop/ms632611(v=vs.85).aspx"""
    _fields_ = [
        ("length", UINT),
        ("flags", UINT),
        ("showCmd", UINT),
        ("ptMinPosition", POINT),
        ("ptMaxPosition", POINT),
        ("rcNormalPosition", RECT),
    ]


def shell__open_start_menu(show_taskbar: bool) -> StdRet[None]:  # pylint:disable=too-many-statements
    """Try to open the start menu."""
    # Find the task bar window
    taskbar_hwnd = windll.user32.FindWindowW("Shell_TrayWnd", None)
    if taskbar_hwnd is None or taskbar_hwnd == 0:
        return WindowsReturnError.stdret('user32.FindWindowW')
    taskbar_size = RECT()
    windll.user32.GetWindowRect(taskbar_hwnd, byref(taskbar_size))

    # if show_taskbar:
    #     if windll.user32.IsWindowVisible(taskbar_hwnd):
    #         placement = WINDOWPLACEMENT()
    #         placement.length = c_sizeof(WINDOWPLACEMENT)
    #         val = windll.user32.GetWindowPlacement(taskbar_hwnd, byref(placement))
    #         if val is not None:
    #             show_cmd = placement.showCmd
    #             if show_cmd in (
    #                     SW_SHOWNORMAL, SW_MAXIMIZE, SW_SHOWMAXIMIZED, SW_SHOWNOACTIVATE,
    #                     SW_SHOW, SW_SHOWNA, SW_RESTORE,
    #             ):
    #                 show_taskbar = False
    if show_taskbar:
        # The task bar is auto-hide.  It's always present, but not on screen.
        # The trick Windows uses is pushing it off-screen, so it's just barely
        # visible.

        # TODO error checking
        windll.user32.GetWindowRect(taskbar_hwnd, byref(taskbar_size))
        # Figure out which corner it's in.  It's either top, left, right, or bottom.
        # We do this by finding a "0", which indicates where on the screen it's
        # located.  However, with strange, multi-monitor setups, this isn't always
        # correct.  But it's a good guess.
        # windll.user32.SetWindowPos(
        #   taskbar_hwnd, HWND_TOPMOST, 0, 0, 0, 0, SWP_NOSIZE | SWP_SHOWWINDOW)

        # TODO show the task bar.
        # log.info("<<Don't know how to show the task bar>>")

    # Find the process ID of the taskbar window.
    taskbar_pid = DWORD()
    windll.user32.GetWindowThreadProcessId(taskbar_hwnd, byref(taskbar_pid))

    # Find a thread in that process that has a "Start" button
    triggered_start = [False]

    # noinspection PyUnusedLocal
    def thread_window_callback(hwnd: HWND, _lparam: LPARAM) -> bool:  # pylint:disable=too-many-locals,too-many-branches,too-many-statements
        length = windll.user32.GetWindowTextLengthW(hwnd)
        if length > 0:
            buff = create_unicode_buffer(length + 1)
            windll.user32.GetWindowTextW(hwnd, buff, length + 1)
            # log.debug("Inspecting {hwnd} = {buff}", hwnd=hwnd, buff=buff.value)
            if buff.value == "Start":
                # Found the window
                # print("DEBUG sending Click message")
                m_res = windll.user32.SendMessageW(hwnd, BM_CLICK, 0, 0)
                if m_res != 0:
                    # Don't look anymore
                    triggered_start[0] = True
                    return False
                try:
                    log.error("<<ERROR pressing start button>>")
                    raise WinError()
                except OSError:
                    traceback.print_exc()
            if buff.value == "Start menu":
                triggered_start[0] = True
                if windll.user32.IsWindowVisible(hwnd):
                    p = WINDOWPLACEMENT()
                    # pylint is confused by structures
                    p.length = c_sizeof(WINDOWPLACEMENT)  # pylint:disable=attribute-defined-outside-init
                    val = windll.user32.GetWindowPlacement(hwnd, byref(p))
                    if val is not None:
                        show_cmd = p.showCmd
                        if show_cmd in (
                                SW_SHOWNORMAL, SW_MAXIMIZE, SW_SHOWMAXIMIZED, SW_SHOWNOACTIVATE,
                                SW_SHOW, SW_SHOWNA, SW_RESTORE,
                        ):
                            # Hide the window
                            # log.debug("hiding the start menu {cmd}", cmd=show_cmd)
                            windll.user32.ShowWindow(hwnd, SW_HIDE)
                            return False
                # log.debug("showing the start menu ({cmd})", cmd=placement.showCmd)
                windll.user32.ShowWindow(hwnd, SW_SHOW)

                # If the task bar is hidden, then part of the start window is not shown fully.
                # SW_MAXIMIZE will show it fully, but the rendering becomes messed up.
                taskbar_rect = RECT()
                windll.user32.GetClientRect(taskbar_hwnd, byref(taskbar_rect))

                client_rect = RECT()
                windll.user32.GetClientRect(hwnd, byref(client_rect))

                overlap_rect = RECT()
                if (
                        windll.user32.IntersectRect(
                            byref(overlap_rect), byref(taskbar_rect), byref(client_rect),
                        ) != 0
                ):
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
                        if (
                                overlap_rect.top.value
                                <= client_rect.top.value <= overlap_rect.bottom.value
                        ):
                            # Adjust down
                            new_y = overlap_rect.bottom.value
                        else:
                            # Adjust up
                            new_y = (
                                    client_rect.top.value
                                    - (overlap_rect.bottom.value - overlap_rect.top.value)
                            )
                    else:
                        # Adjust along the x axis
                        if (
                                overlap_rect.left.value
                                <= client_rect.left.value <= overlap_rect.right.value
                        ):
                            # Adjust to the right
                            new_x = overlap_rect.right.value
                        else:
                            new_x = (
                                    client_rect.left.value
                                    - (overlap_rect.right.value - overlap_rect.left.value)
                            )
                    windll.user32.SetWindowPos(
                        hwnd, None, new_x, new_y,
                        0, 0, SWP_NOSIZE,
                    )

                # Give the window the focus.  This is the Microsoft Magic Focus Dance.
                current_hwnd = windll.user32.GetForegroundWindow()
                current_thread_id = windll.kernel32.GetCurrentThreadId()
                thread_process_id = windll.user32.GetWindowThreadProcessId(current_hwnd, None)
                windll.user32.AttachThreadInput(thread_process_id, current_thread_id, True)
                windll.user32.SetWindowPos(hwnd, HWND_TOPMOST, 0, 0, 0, 0, SWP_NOSIZE | SWP_NOMOVE)
                windll.user32.SetWindowPos(
                    hwnd, HWND_NOTOPMOST, 0, 0, 0, 0, SWP_NOSIZE | SWP_NOMOVE,
                )
                windll.user32.SetForegroundWindow(hwnd)
                windll.user32.AttachThreadInput(thread_process_id, current_thread_id, False)
                windll.user32.SetFocus(hwnd)
                windll.user32.SetActiveWindow(hwnd)

                return False
        # else:
        #     log.debug("Inspecting {hwnd} => no title, ignoring", hwnd=hwnd)
        return True

    # Find the threads for the process ID
    thread_ids = []
    hsnapshot = windll.kernel32.CreateToolhelp32Snapshot(TH32CS_SNAPTHREAD, taskbar_pid)
    if hsnapshot == INVALID_HANDLE_VALUE:
        raise WinError()
    try:
        # pylint is confused by structures.
        thread_entry = THREADENTRY32()
        thread_entry.dwSize = c_sizeof(THREADENTRY32)  # pylint:disable=attribute-defined-outside-init

        # log.debug("Getting threads for pid {pid}", pid=taskbar_pid)
        res = windll.kernel32.Thread32First(hsnapshot, byref(thread_entry))
        # log.debug(" :: first: {res}", res=res)
        if res == 0:
            return WindowsReturnError.stdret('kernel32.Thread32First')
        while res != 0:
            # pylint is confused by structures.
            if thread_entry.dwSize > THREADENTRY32.th32OwnerProcessID.offset:  # pylint:disable=attribute-defined-outside-init
                thread_ids.append(thread_entry.th32ThreadID)  # pylint:disable=attribute-defined-outside-init
            # else:
            #     log.debug("returned too small size {size}", size=thread_entry.dwSize)
            thread_entry.dwSize = c_sizeof(THREADENTRY32)  # pylint:disable=attribute-defined-outside-init
            res = windll.kernel32.Thread32Next(hsnapshot, byref(thread_entry))
            # log.debug(" :: next: {res}", res=res)
    finally:
        windll.kernel32.CloseHandle(hsnapshot)

    callback_type = CFUNCTYPE(BOOL, HWND, LPARAM)
    callback_ptr = callback_type(thread_window_callback)
    for thread_id in thread_ids:
        # log.debug(f"Iterating over windows for thread {thread_id} in pid {taskbar_pid}")
        windll.user32.EnumThreadWindows(thread_id, callback_ptr, 0)
        if triggered_start[0]:
            return RET_OK_NONE

    return StdRet.pass_errmsg(
        user_messages.TRANSLATION_CATALOG,
        _('could not find start button'),
    )


class MARGINS(Structure):
    """The MARGINS structure.
    See https://msdn.microsoft.com/en-us/library/windows/desktop/bb773244(v=vs.85).aspx."""
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
        StdRet[HWND],
]:
    """Create a borderless window."""
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
            always_on_top: Optional[bool] = False,
    ) -> StdRet[HWND]:
        margins = MARGINS()
        # pylint doesn't understand structures.
        margins.cxLeftWidth = 0  # pylint:disable=attribute-defined-outside-init
        margins.cxRightWidth = 0  # pylint:disable=attribute-defined-outside-init
        margins.cyTopHeight = 0  # pylint:disable=attribute-defined-outside-init
        margins.cyBottomHeight = 0  # pylint:disable=attribute-defined-outside-init

        style_flags = {
            'popup', 'visible',
            # 'layered',   This causes the windows to not show up.
            'transparent',
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
            hwnd_res = func_map.window.create_display_window(
                class_name, title, message_handler, style_flags,
            )
            # windll.dwmapi.DwmExtendFrameIntoClientArea(hwnd, byref(margins))
            return hwnd_res
        return StdRet.pass_errmsg(
            user_messages.TRANSLATION_CATALOG,
            _('not supported'),
        )

    return window__create_borderless_window
