
"""
Windows XP functions
"""

# Many places use Windows naming convention for things, not Python.
# pylint:disable=invalid-name

from typing import Sequence, List, Tuple, Dict, Callable, Union, Optional
from ctypes import c_wchar_p, c_int
from ctypes import sizeof as c_sizeof
from ctypes import cast as c_cast
import atexit
from .windows_common import (
    byref, create_unicode_buffer,
    DWORD, UINT, LONG, CHAR, BOOL, BYTE, LPCWSTR, LPVOID, HMODULE, HANDLE, HWND,
    WPARAM, LPARAM,
    POINTER, Structure,
    WindowsErrorMessage,
    WinDLL, windll,
    MessageCallback,
)
from .supported_functions import (
    Functions,
)
from .process_metrics import ProcessMetrics
from .window_metrics import WindowMetrics, FontMetrics
from .. import windows_constants


def load_functions(environ: Dict[str, str], func_map: Functions) -> None:
    """Load all the functions, if this is running on windows xp"""
    # TODO include Windows Server 2003 detection
    if environ['system'].lower() == 'windows' and environ['release'].lower() == 'xp':
        func_map.shell.find_notification_icons = create_shell__find_notification_icons(func_map)
        func_map.process.load_all_process_details = process__load_all_process_details
        load_psapi_functions(func_map)
        load_info_functions(func_map)
        load_taskbar_functions(func_map)
        load_window_functions(func_map)


def load_psapi_functions(func_map: Functions) -> None:
    """Load the psapi functions."""
    func_map.process.get_executable_filename = process__get_executable_filename
    func_map.process.get_all_service_information = process__get_all_service_information
    func_map.process.get_username_domain_for_pid = process__get_username_domain_for_pid
    func_map.process.get_current_username_domain = process__get_current_username_domain
    func_map.process.get_all_pids = process__get_all_pids


def load_info_functions(func_map: Functions) -> None:
    """Load the info gathering functions"""
    func_map.shell.get_window_metrics = shell__get_window_metrics
    func_map.shell.set_window_metrics = shell__set_window_metrics
    func_map.shell.set_border_size = shell__set_border_size


def load_taskbar_functions(func_map: Functions) -> None:
    """Load the taskbar-specific functions"""
    func_map.shell.open_start_menu = shell__open_start_menu


def load_window_functions(func_map: Functions) -> None:
    """Load the window functions"""
    func_map.window.create_borderless_window = create_window__create_borderless_window(func_map)


def create_shell__find_notification_icons(
        func_map: Functions,
) -> Optional[Callable[[], Sequence[HWND]]]:
    """Find the notifications icons section on the task bar."""
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
        for tbw_handle in shell__get_task_bar_window_handles():
            parent_area = fw(fw(tbw_handle, "TrayNotifyWnd"), "SysPager")
            if not parent_area:
                continue
            for title in ['Notification Area', 'Overflow Notification Area']:
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


def process__get_executable_filename(  # pylint:disable=too-many-locals,too-many-branches
        thread_pid: DWORD,
) -> Union[str, WindowsErrorMessage, None]:
    """Get the executable filename for the thread PID."""
    psapi = WinDLL('psapi.dll')
    EnumProcesses = psapi.EnumProcesses
    EnumProcessModules = psapi.EnumProcessModules
    GetModuleBaseName = psapi.GetModuleBaseNameW
    # Alternate: GetModuleFileNameEx
    GetProcessImageFileName = psapi.GetProcessImageFileNameW

    hproc = windll.kernel32.OpenProcess(
        windows_constants.PROCESS_QUERY_INFORMATION | windows_constants.PROCESS_VM_READ,
        False, thread_pid,
    )
    if hproc != 0 and hproc is not None:
        try:
            filename = create_unicode_buffer(windows_constants.MAX_FILENAME_LENGTH + 1)

            res = GetProcessImageFileName(
                hproc, None, byref(filename), windows_constants.MAX_FILENAME_LENGTH + 1,
            )
            if res > 0:
                print(f"DEBUG found filename ({thread_pid}) for pid {filename}")
                return filename.value[:res]
            print(
                f"DEBUG failed to get filename for pid {thread_pid}: "
                f"{WindowsErrorMessage('GetProcessImageFileName')}"
            )
        finally:
            windll.kernel32.CloseHandle(hproc)
    else:
        print(f"DEBUG failed to open the process handle for pid {thread_pid}")

    # So, GetProcessImageFileName failed, as it's apt to do.
    # So, do this the hard way.

    process_list = (DWORD * windows_constants.MAX_PROCESS_COUNT)()
    bytes_returned = DWORD()
    res = EnumProcesses(process_list, c_sizeof(process_list), byref(bytes_returned))
    if res != 0:
        return WindowsErrorMessage('psapi.EnumProcesses')
        # raise ctypes.WinError()
    for i in range(bytes_returned.value // c_sizeof(DWORD)):
        pid = process_list[i]
        if pid == thread_pid:
            hproc = windll.kernel32.OpenProcess(
                windows_constants.PROCESS_QUERY_INFORMATION | windows_constants.PROCESS_VM_READ,
                None, pid,
            )
            if hproc is None or hproc == 0:
                continue
            try:
                buffer_index_count = 1024
                count_allocated_space = DWORD()
                hmod_list = (HMODULE * buffer_index_count)()
                res = EnumProcessModules(
                    hproc.value, hmod_list, DWORD(c_sizeof(hmod_list)),
                    byref(count_allocated_space),
                )
                if res == 0:
                    # Error; ignore
                    continue
                for j in range(count_allocated_space.value // c_sizeof(HMODULE)):
                    mod_name = create_unicode_buffer(windows_constants.MAX_FILENAME_LENGTH + 1)
                    res = GetModuleBaseName(
                        hproc, hmod_list[j], mod_name,
                        windows_constants.MAX_FILENAME_LENGTH + 1,
                    )
                    if res != 0:
                        return str(mod_name.value[:res])
            finally:
                windll.kernel32.CloseHandle(hproc)
    return None


def process__get_username_domain_for_pid(  # pylint:disable=too-many-locals,too-many-return-statements,too-many-branches
        thread_pid: DWORD,
) -> Union[Tuple[str, str], WindowsErrorMessage]:
    """

    :param thread_pid:
    :return: the tuple (username, domain) for the user that owns the pid.
    """
    OpenProcessToken = windll.advapi32.OpenProcessToken
    OpenProcessToken.argtypes = [HANDLE, DWORD, POINTER(HANDLE)]
    OpenProcessToken.restype = BOOL
    GetTokenInformation = windll.advapi32.GetTokenInformation
    LookupAccountSidW = windll.advapi32.LookupAccountSidW
    LookupAccountSidW.argtypes = [
        LPCWSTR, LPVOID,
        LPCWSTR, POINTER(DWORD),
        LPCWSTR, POINTER(DWORD),
        POINTER(DWORD),
    ]
    LookupAccountSidW.restype = BOOL

    # WinXP does not support PROCESS_QUERY_LIMITED_INFORMATION
    # This needs to have a special Windows 8 vs. other implementation.
    # Win 8 uses the more limited query.
    hproc = windll.kernel32.OpenProcess(
        windows_constants.PROCESS_QUERY_INFORMATION, False, thread_pid,
    )
    if hproc == 0:
        err = WindowsErrorMessage('kernel32.OpenProcess')
        if err.errno == windows_constants.ERROR_ACCESS_DENIED:
            # Don't raise a problem in this situation.  Instead, return unique information.
            return "[denied]", "[denied]"
        return err
    try:
        access_token = HANDLE()
        res = OpenProcessToken(hproc, DWORD(windows_constants.TOKEN_QUERY), byref(access_token))
        if res == 0 or access_token is None:
            return WindowsErrorMessage('advapi32.OpenProcessToken')
        try:
            length = DWORD(0)
            res = GetTokenInformation(
                access_token, windows_constants.TOKEN_INFORMATION__TOKEN_USER,
                None, 0, byref(length),
            )
            if res == 0:
                err = WindowsErrorMessage('advapi32.GetTokenInformation')
                if err.errno != windows_constants.ERROR_INSUFFICIENT_BUFFER:
                    return err
                raw_sid_info = (BYTE * length.value)()
                if raw_sid_info is None:
                    return WindowsErrorMessage('memory allocation failed')
                sid_info = c_cast(raw_sid_info, POINTER(LPVOID))
            else:
                sid_info = POINTER(LPVOID)()
            res = GetTokenInformation(
                access_token, windows_constants.TOKEN_INFORMATION__TOKEN_USER, sid_info,
                length, byref(length),
            )
            if res == 0:
                return WindowsErrorMessage('advapi32.GetTokenInformation')

            # The "sid_info" is a pointer to a structure, but the only thing we care about
            # is the first value in the structure (index 0), which is itself a pointer to a
            # SID structure.
            sid_ptr = sid_info[0]

            username = create_unicode_buffer(windows_constants.MAX_USERNAME_LENGTH + 1)
            username_size = DWORD(windows_constants.MAX_USERNAME_LENGTH)
            domain = create_unicode_buffer(windows_constants.MAX_USERNAME_LENGTH + 1)
            domain_size = DWORD(windows_constants.MAX_USERNAME_LENGTH)
            sid_name_type = DWORD()

            res = LookupAccountSidW(
                None, sid_ptr, username, byref(username_size),
                domain, byref(domain_size), byref(sid_name_type),
            )
            if res == 0:
                return WindowsErrorMessage('advapi32.LookupAccountSidW')

            # return username.value[0:username_size], domain.value[0:domain_size]
            return username.value, domain.value
        finally:
            windll.kernel32.CloseHandle(access_token)
    finally:
        windll.kernel32.CloseHandle(hproc)


def process__get_current_username_domain() -> Union[Tuple[str, str], WindowsErrorMessage]:
    """Get the current username / domain"""
    # Just the username is easy (GetUserName), but the domain takes more work.
    return process__get_username_domain_for_pid(windll.kernel32.GetCurrentProcessId())


def process__load_all_process_details() -> Sequence[Dict[str, str]]:
    """Load all the process details, for all the processes."""
    raise OSError("Undefined")


class ENUM_SERVICE_STATUS_PROCESS(Structure):
    """The ENUM_SERVICE_STATUS_PROCESS structure.
    see https://msdn.microsoft.com/en-us/library/windows/desktop/ms682648(v=vs.85).aspx
    see https://msdn.microsoft.com/en-us/library/windows/desktop/ms685992(v=vs.85).aspx"""
    _fields_ = (
        ("lpServiceName", c_wchar_p),  # string pointer
        ("lpDisplayName", c_wchar_p),  # string pointer
        # ServiceStatusProcess
        ("dwServiceType", DWORD),
        ("dwCurrentState", DWORD),
        ("dwControlsAccepted", DWORD),
        ("dwWin32ExitCode", DWORD),
        ("dwServiceSpecificExitCode", DWORD),
        ("dwCheckPoint", DWORD),
        ("dwWaitHint", DWORD),
        ("dwProcessId", DWORD),
        ("dwServiceFlags", DWORD),
    )


_SERVICE_TYPES: Dict[int, str] = {
    1: 'SERVICE_KERNEL_DRIVER',
    2: 'SERVICE_FILE_SYSTEM_DRIVER',
    0x10: 'SERVICE_WIN32_OWN_PROCESS',
    0x20: 'SERVICE_WIN32_SHARE_PROCESS',
}

_SERVICE_CURRENT_STATES: Dict[int, str] = {
    0x5: 'SERVICE_CONTINUE_PENDING',
    0x6: 'SERVICE_PAUSE_PENDING',
    0x7: 'SERVICE_PAUSED',
    0x4: 'SERVICE_RUNNING',
    0x2: 'SERVICE_START_PENDING',
    0x3: 'SERVICE_STOP_PENDING',
    0x1: 'SERVICE_STOPPED',
}


def process__get_all_service_information() -> Union[  # pylint:disable=too-many-locals,too-many-branches
    WindowsErrorMessage, Sequence[ProcessMetrics],
]:
    """Get information for all the services."""
    advapi32 = WinDLL('advapi32.dll')
    OpenSCManager = advapi32.OpenSCManagerW
    OpenSCManager.restype = DWORD
    EnumServicesStatusEx = advapi32.EnumServicesStatusExW
    # EnumServicesStatusExW(SC_HANDLE,
    #   SC_ENUM_TYPE,DWORD,DWORD,LPBYTE,DWORD,LPDWORD,LPDWORD,LPDWORD,LPCWSTR);
    # EnumServicesStatusEx.argtypes = [
    #     c_int,             # hSCManager (SC_HANDLE)
    #     c_int,             # InfoLevel (SC_ENUM_TYPE)
    #     wintypes.DWORD,    # dwServiceType
    #     wintypes.DWORD,    # dwServiceState
    #     wintypes.LPBYTE,   # lpServices
    #     wintypes.DWORD,    # cbBufSize
    #     wintypes.LPDWORD,  # pcbBytesNeeded
    #     wintypes.LPDWORD,  # lpServicesReturned
    #     wintypes.LPDWORD,  # lpResumeHandle
    #     wintypes.LPCWSTR   # pszGroupname
    # ]
    CloseServiceHandle = advapi32.CloseServiceHandle
    CloseServiceHandle.argtypes = [HANDLE]

    sc = OpenSCManager(None, None, windows_constants.SC_MANAGER_ENUMERATE_SERVICE)
    if sc == 0:
        return WindowsErrorMessage('advapi32.OpenSCManagerW')
    try:
        bytes_needed = DWORD(0)
        service_byte_count = DWORD(0)
        service_count = DWORD(0)
        resume_handle = DWORD(0)
        status_array = None

        # Start off with 0 bytes allocated, and increase from there.
        while True:
            res = EnumServicesStatusEx(
                sc, windows_constants.SC_ENUM_PROCESS_INFO,

                # was: SERVICE_DRIVER | SERVICE_FILE_SYSTEM_DRIVER |
                # SERVICE_KERNEL_DRIVER | SERVICE_WIN32,
                windows_constants.SERVICE_WIN32,

                windows_constants.SERVICE_STATE_ALL, status_array,
                service_byte_count, byref(bytes_needed), byref(service_count),
                byref(resume_handle), None,
            )
            if res != 0:
                break
            err = WindowsErrorMessage('advapi32.EnumServicesStatusExW')
            if err.errno != windows_constants.ERROR_MORE_DATA:
                # return err
                return ()
            print("need {0} bytes".format(bytes_needed))
            service_byte_count = bytes_needed
            count = bytes_needed.value // c_sizeof(ENUM_SERVICE_STATUS_PROCESS)
            status_array = (ENUM_SERVICE_STATUS_PROCESS * count)()
        if not status_array:
            # Nothing found on first pass.
            return ()
        ret: List[ProcessMetrics] = []
        for i in range(service_count.value):
            status = status_array[i]
            controls_accepted = []
            if _has_bit_set(
                    status.dwControlsAccepted, windows_constants.SERVICE_ACCEPT_NETBINDCHANGE,
            ):
                controls_accepted.append('SERVICE_ACCEPT_NETBINDCHANGE')
            if _has_bit_set(
                    status.dwControlsAccepted, windows_constants.SERVICE_ACCEPT_PARAMCHANGE,
            ):
                controls_accepted.append('SERVICE_ACCEPT_PARAMCHANGE')
            if _has_bit_set(
                    status.dwControlsAccepted, windows_constants.SERVICE_ACCEPT_PAUSE_CONTINUE,
            ):
                controls_accepted.append('SERVICE_ACCEPT_PAUSE_CONTINUE')
            if _has_bit_set(
                    status.dwControlsAccepted, windows_constants.SERVICE_ACCEPT_PRESHUTDOWN,
            ):
                controls_accepted.append('SERVICE_ACCEPT_PRESHUTDOWN')
            if _has_bit_set(status.dwControlsAccepted, windows_constants.SERVICE_ACCEPT_SHUTDOWN):
                controls_accepted.append('SERVICE_ACCEPT_SHUTDOWN')
            if _has_bit_set(status.dwControlsAccepted, windows_constants.SERVICE_ACCEPT_STOP):
                controls_accepted.append('SERVICE_ACCEPT_STOP')

            ret.append(ProcessMetrics(
                display_name=status.lpServiceName.value,
                service_name=status.lpDisplayName.value,
                service_type=(
                    status.dwServiceType in _SERVICE_TYPES and
                    _SERVICE_TYPES[status.dwServiceType] or None
                ),
                current_state=(
                    status.dwCurrentState in _SERVICE_CURRENT_STATES and
                    _SERVICE_CURRENT_STATES[status.dwCurrentState] or None
                ),
                controls_accepted=controls_accepted,
                exit_code=status.dwWin32ExitCode,
                service_exit_code=status.dwServiceSpecificExitCode,
                check_point=status.dwCheckPoint,
                wait_time_millis_hint=status.dwWaitHint,
                process_id=status.dwProcessId,
                flags=status.dwServiceFlags == 1 and ['SERVICE_RUNS_IN_SYSTEM_PROCESS'] or [],
            ))
        return ret
    finally:
        CloseServiceHandle(sc)


def _has_bit_set(dw: DWORD, bit_mask: int) -> bool:
    return (dw.value & bit_mask) == bit_mask


class LOGFONT(Structure):  # pylint:disable=too-many-instance-attributes
    """The LOGFONT structure
    see https://msdn.microsoft.com/en-us/library/windows/desktop/dd145037(v=vs.85).aspx"""
    _fields_ = [
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
        ("lfFaceName", CHAR * windows_constants.LF_FACESIZE),
    ]


class NONCLIENTMETRICS(Structure):  # pylint:disable=too-many-instance-attributes
    """The NONCLIENTMETRICS structure
    see https://msdn.microsoft.com/en-us/library/windows/desktop/ff729175(v=vs.85).aspx"""
    _fields_ = [
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
    ]


def shell__get_window_metrics() -> Union[WindowMetrics, WindowsErrorMessage]:
    """Get the global windows metrics."""
    metrics = shell__get_raw_window_metrics()
    if isinstance(metrics, WindowsErrorMessage):
        return metrics
    return WindowMetrics(
        # for some unknown reason, pylint doesn't like the lOGFONT typed member functions;
        # it complains that the "metrics" object is a WindowsErrorMessage.

        border_width=metrics.iBorderWidth.value,
        scroll_width=0,
        scroll_height=metrics.iScrollHeight.value,
        caption_width=metrics.iCaptionWidth.value,
        caption_height=metrics.iCaptionHeight.value,
        caption_font=_font_to_dict(metrics.lfCaptionFont),  # pylint:disable=no-member
        sm_caption_width=metrics.iSmCaptionWidth.value,
        sm_caption_height=metrics.iSmCaptionHeight.value,
        sm_caption_font=_font_to_dict(metrics.lfSmCaptionFont),  # pylint:disable=no-member
        menu_width=metrics.iMenuWidth.value,
        menu_height=metrics.iMenuHeight.value,
        menu_font=_font_to_dict(metrics.lfMenuFont),  # pylint:disable=no-member
        status_font=_font_to_dict(metrics.lfStatusFont),  # pylint:disable=no-member
        message_font=_font_to_dict(metrics.lfMessageFont),  # pylint:disable=no-member

        # XP does not support this value.
        padded_border_width=0,
    )


def shell__get_raw_window_metrics() -> Union[NONCLIENTMETRICS, WindowsErrorMessage]:
    """Get the raw window metrics."""
    SystemParametersInfoW = windll.user32.SystemParametersInfoW
    metrics = NONCLIENTMETRICS()
    metrics.cbSize = c_sizeof(NONCLIENTMETRICS)  # pylint:disable=attribute-defined-outside-init
    res = SystemParametersInfoW(
        windows_constants.SPI_GETNONCLIENTMETRICS, metrics.cbSize, byref(metrics), 0,
    )
    if res != 0:
        return WindowsErrorMessage('user32.SystemParametersInfoW')
    return metrics


_BASE_OS_METRICS: List[Optional[NONCLIENTMETRICS]] = [None]


def shell__set_window_metrics(metrics: WindowMetrics) -> Optional[WindowsErrorMessage]:
    """Set the global window metrics."""
    return inner__set_window_metrics(metrics)


def inner__set_window_metrics(
        metrics: Union[NONCLIENTMETRICS, WindowMetrics],
) -> Optional[WindowsErrorMessage]:
    """Set the global window metrics."""
    SystemParametersInfoW = windll.user32.SystemParametersInfoW

    # Always actions the original user metrics at exit time.
    root_metrics = None
    if _BASE_OS_METRICS[0] is None:
        root_metrics = shell__get_raw_window_metrics()
        if isinstance(root_metrics, WindowsErrorMessage):
            return root_metrics
        _BASE_OS_METRICS[0] = root_metrics
        atexit.register(shell__set_window_metrics, root_metrics)

    m: NONCLIENTMETRICS
    if isinstance(metrics, WindowMetrics):
        if root_metrics:
            if isinstance(root_metrics, WindowsErrorMessage):
                return root_metrics
            m = root_metrics
        else:
            raw_m = shell__get_raw_window_metrics()
            if isinstance(raw_m, WindowsErrorMessage):
                return raw_m
            m = raw_m
        m.cbSize = c_sizeof(NONCLIENTMETRICS)  # pylint:disable=attribute-defined-outside-init
        m.iBorderWidth = DWORD(metrics.border_width)  # pylint:disable=attribute-defined-outside-init
        m.iScrollWidth = DWORD(metrics.scroll_width)  # pylint:disable=attribute-defined-outside-init
        m.iScrollHeight = DWORD(metrics.scroll_height)  # pylint:disable=attribute-defined-outside-init
        m.iCaptionWidth = DWORD(metrics.caption_width)  # pylint:disable=attribute-defined-outside-init
        m.iCaptionHeight = DWORD(metrics.caption_height)  # pylint:disable=attribute-defined-outside-init
        _dict_to_font(metrics.caption_font, m.lfCaptionFont)
        m.iSmCaptionWidth = DWORD(metrics.sm_caption_width)  # pylint:disable=attribute-defined-outside-init
        m.iSmCaptionHeight = DWORD(metrics.sm_caption_height)  # pylint:disable=attribute-defined-outside-init
        _dict_to_font(metrics.sm_caption_font, m.lfSmCaptionFont)
        m.iMenuWidth = DWORD(metrics.menu_width)  # pylint:disable=attribute-defined-outside-init
        m.iMenuHeight = DWORD(metrics.menu_height)  # pylint:disable=attribute-defined-outside-init
        _dict_to_font(metrics.menu_font, m.lfMenuFont)
        _dict_to_font(metrics.status_font, m.lfStatusFont)
        _dict_to_font(metrics.message_font, m.lfMessageFont)
    else:
        m = metrics

    m.cbSize = c_sizeof(NONCLIENTMETRICS)  # pylint:disable=attribute-defined-outside-init
    res = SystemParametersInfoW(
        windows_constants.SPI_SETNONCLIENTMETRICS, m.cbSize, byref(m),
        windows_constants.SPIF_SENDCHANGE,
    )
    if res != 0:
        return WindowsErrorMessage('user32.SystemParametersInfoW')
    return None


def _dict_to_font(f: FontMetrics, ret: Optional[LOGFONT] = None) -> LOGFONT:
    if ret is None:
        ret = LOGFONT()
    ret.lfHeight = LONG(f.height)  # pylint:disable=attribute-defined-outside-init
    ret.lfWidth = LONG(f.width)  # pylint:disable=attribute-defined-outside-init
    ret.lfEscapement = LONG(f.escapement)  # pylint:disable=attribute-defined-outside-init
    ret.lfOrientation = LONG(f.orientation)  # pylint:disable=attribute-defined-outside-init
    ret.lfWeight = LONG(f.weight)  # pylint:disable=attribute-defined-outside-init
    ret.lfItalic = BYTE(f.italic)  # pylint:disable=attribute-defined-outside-init
    ret.lfUnderline = BYTE(f.underline)  # pylint:disable=attribute-defined-outside-init
    ret.lfStrikeOut = BYTE(f.strikeout)  # pylint:disable=attribute-defined-outside-init
    ret.lfCharSet = BYTE(f.charset)  # pylint:disable=attribute-defined-outside-init
    ret.lfOutPrecision = BYTE(f.out_precision)  # pylint:disable=attribute-defined-outside-init
    ret.lfClipPrecision = BYTE(f.clip_precision)  # pylint:disable=attribute-defined-outside-init
    ret.lfQuality = BYTE(f.quality)  # pylint:disable=attribute-defined-outside-init
    ret.lfPitchAndFamily = BYTE(f.pitch_and_family)  # pylint:disable=attribute-defined-outside-init
    if f.face_name:
        ret.lfFaceName = f.face_name[:windows_constants.LF_FACESIZE - 1]  # pylint:disable=attribute-defined-outside-init
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


def shell__set_border_size(
        border_width: int, border_padding: int,
) -> Optional[WindowsErrorMessage]:
    """Set the global border size."""
    metrics = shell__get_raw_window_metrics()
    if isinstance(metrics, WindowsErrorMessage):
        return metrics
    metrics.iBorderWidth = DWORD(border_width + border_padding)  # pylint:disable=attribute-defined-outside-init
    return inner__set_window_metrics(metrics)


def shell__open_start_menu(_dunno: bool) -> Optional[WindowsErrorMessage]:
    """Try to open the start menu."""
    # Find the task bar window
    taskbar_hwnd = windll.user32.FindWindowW("Shell_TrayWnd", None)
    if taskbar_hwnd is None or taskbar_hwnd == 0:
        return WindowsErrorMessage('user32.FindWindowW')

    # Find the "start" button on the tray window
    start_hwnd = windll.user32.FindWindowExW(taskbar_hwnd, None, 'Button', 'Start')
    if start_hwnd is None:
        start_hwnd = windll.user32.FindWindowExW(taskbar_hwnd, None, None, 'Start')
        if start_hwnd is None:
            start_hwnd = windll.user32.FindWindowExW(taskbar_hwnd, None, 'Button', None)
            if start_hwnd is None:
                return WindowsErrorMessage('user32.FindWindowExW')

    # Send a click message to the button
    windll.user32.SendMessageW(start_hwnd, windows_constants.BM_CLICK, 0, 0)
    # TODO error checking???
    return None


def process__get_all_pids() -> Union[WindowsErrorMessage, Sequence[DWORD]]:
    """Get all the process PIDs"""
    process_buff = (DWORD * 2048)()
    process_size = DWORD()
    res = windll.psapi.EnumProcesses(process_buff, c_sizeof(process_buff), byref(process_size))
    if res != 0:
        return WindowsErrorMessage('psapi.EnumProcesses')
    count = process_size.value // c_sizeof(DWORD)
    ret = []
    for i in range(count):
        ret.append(DWORD(process_buff[i]))
    return ret


def create_window__create_borderless_window(
        func_map: Functions
) -> Optional[Callable[
    [str, str, MessageCallback, Dict[int, MessageCallback], Optional[bool], Optional[bool]],
    Union[HWND, WindowsErrorMessage],
]]:
    """Create a window without borders."""
    # Note that WM_CREATE just doesn't work.  Any attempt to use it,
    # even when explicitly returning 0, just causes the windows to be
    # destroyed.

    def window__create_borderless_window(
            class_name: str, title: str,
            message_handler: MessageCallback,
            callback_map: Dict[int, MessageCallback],
            show_on_taskbar: Optional[bool] = True,
            always_on_top: Optional[bool] = False,
    ) -> Union[HWND, WindowsErrorMessage]:
        create_display_window = func_map.window.create_display_window
        if not create_display_window:
            return WindowsErrorMessage('not implemented')
        style_flags = {
            'popup', 'visible', 'layered', 'transparent',
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

            # return windows_constants.HTCLIENT
            return True

        def zero(_hwnd: HWND, _msg: int, _wparam: WPARAM, _lparam: LPARAM) -> bool:
            return False

        callback_map[windows_constants.WM_NCACTIVATE] = zero
        callback_map[windows_constants.WM_NCCALCSIZE] = zero
        callback_map[windows_constants.WM_NCHITTEST] = hit_test

        hwnd = create_display_window(class_name, title, message_handler, style_flags)
        return hwnd

    return window__create_borderless_window
