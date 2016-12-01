"""
Windows XP functions
"""

from ctypes import (windll, wintypes, byref, Structure, c_int, c_uint, WinError, WinDLL,
                    create_unicode_buffer, c_wchar_p, GetLastError, Structure,
                    POINTER, WINFUNCTYPE)
from ctypes import sizeof as c_sizeof
from ctypes import cast as c_cast
from .windows_constants import *
import atexit



def load_functions(environ, func_map):
    # TODO include Windows Server 2003 detection
    if environ['system'].lower() == 'windows' and environ['release'].lower() == 'xp':
        func_map['shell__find_notification_icons'] = shell__find_notification_icons(func_map)
        func_map['process__load_all_process_details'] = process__load_all_process_details
        load_psapi_functions(func_map)
        load_info_functions(func_map)
        load_taskbar_functions(func_map)
        load_window_functions(func_map)


def load_psapi_functions(func_map):
    func_map['process__get_executable_filename'] = process__get_executable_filename
    func_map['process__get_all_service_information'] = process__get_all_service_information
    func_map['process__get_username_domain_for_pid'] = process__get_username_domain_for_pid
    func_map['process__get_current_username_domain'] = process__get_current_username_domain
    func_map['process__get_all_pids'] = process__get_all_pids


def load_info_functions(func_map):
    func_map['shell__get_window_metrics'] = shell__get_window_metrics
    func_map['shell__get_raw_window_metrics'] = shell__get_raw_window_metrics
    func_map['shell__set_window_metrics'] = shell__set_window_metrics
    func_map['shell__set_border_size'] = shell__set_border_size


def load_taskbar_functions(func_map):
    func_map['shell__open_start_menu'] = shell__open_start_menu


def load_window_functions(func_map):
    func_map['window__create_borderless_window'] = create_window__create_borderless_window(func_map)


def shell__find_notification_icons(func_map):
    find_window_ex = func_map['window__find_handle_for_child_class_title']
    shell__get_task_bar_window_handles = func_map['shell__get_task_bar_window_handles']

    def fw(parent, class_name):
        return find_window_ex(parent, None, class_name, "")

    def f():
        ret = []
        parent_area = fw(fw(shell__get_task_bar_window_handles(), "TrayNotifyWnd"), "SysPager")
        for title in ['Notification Area', 'Overflow Notification Area']:
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


def process__get_executable_filename(thread_pid):
    psapi = WinDLL('psapi.dll')
    EnumProcesses = psapi.EnumProcesses
    EnumProcessModules = psapi.EnumProcessModules
    GetModuleBaseName = psapi.GetModuleBaseNameW
    # Alternate: GetModuleFileNameEx
    GetProcessImageFileName = psapi.GetProcessImageFileNameW

    hproc = windll.kernel32.OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, thread_pid)
    try:
        filename = create_unicode_buffer(MAX_FILENAME_LENGTH + 1)

        res = GetProcessImageFileName(hproc, None, byref(filename), MAX_FILENAME_LENGTH + 1)
        if res > 0:
            return filename.value[:res]
    finally:
        windll.kernel32.CloseHandle(hproc)

    # So, GetProcessImageFileName failed, as it's apt to do.
    # So, do this the hard way.

    process_list = (wintypes.DWORD * MAX_PROCESS_COUNT)()
    bytes_returned = wintypes.DWORD()
    res = EnumProcesses(process_list, c_sizeof(process_list), byref(bytes_returned))
    if res != 0:
        return None
        # raise ctypes.WinError()
    for i in range(bytes_returned / c_sizeof(wintypes.DWORD)):
        pid = process_list[i]
        if pid == thread_pid:
            hproc = windll.kernel32.OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, None, pid)
            if hproc is None or 0 == hproc:
                continue
            try:
                buffer_index_count = 1024
                count_allocated_space = wintypes.DWORD()
                hmod_list = (wintypes.HMODULE * buffer_index_count)()
                res = EnumProcessModules(
                    hproc.value, hmod_list, wintypes.DWORD(c_sizeof(hmod_list)), byref(count_allocated_space)
                )
                if res == 0:
                    # Error; ignore
                    continue
                for j in range(count_allocated_space / c_sizeof(wintypes.HMODULE)):
                    mod_name = create_unicode_buffer(MAX_FILENAME_LENGTH + 1)
                    res = GetModuleBaseName(hproc, hmod_list[j], mod_name, MAX_FILENAME_LENGTH + 1)
                    if res != 0:
                        return str(mod_name.value[:res])
            finally:
                windll.kernel32.CloseHandle(hproc)
    return None


def process__get_username_domain_for_pid(thread_pid):
    """

    :param thread_pid:
    :return: the tuple (username, domain) for the user that owns the pid.
    """
    OpenProcessToken = windll.advapi32.OpenProcessToken
    OpenProcessToken.argtypes = [wintypes.HANDLE, wintypes.DWORD, POINTER(wintypes.HANDLE)]
    OpenProcessToken.restype = wintypes.BOOL
    GetTokenInformation = windll.advapi32.GetTokenInformation
    LookupAccountSidW = windll.advapi32.LookupAccountSidW
    LookupAccountSidW.argtypes = [
        wintypes.LPCWSTR, wintypes.LPVOID,
        wintypes.LPCWSTR, POINTER(wintypes.DWORD),
        wintypes.LPCWSTR, POINTER(wintypes.DWORD),
        POINTER(wintypes.DWORD)
    ]
    LookupAccountSidW.restype = wintypes.BOOL

    # WinXP does not support PROCESS_QUERY_LIMITED_INFORMATION
    # This needs to have a special Windows 8 vs. other implementation.
    # Win 8 uses the more limited query.
    hproc = windll.kernel32.OpenProcess(PROCESS_QUERY_INFORMATION, False, thread_pid)
    if hproc == 0:
        if GetLastError() == ERROR_ACCESS_DENIED:
            # Don't raise a problem in this situation.  Instead, return unique information.
            return "[denied]", "[denied]"
        raise WinError()
    try:
        access_token = wintypes.HANDLE()
        res = OpenProcessToken(hproc, wintypes.DWORD(TOKEN_QUERY), byref(access_token))
        if res == 0 or access_token is None:
            raise WinError()
        try:
            length = wintypes.DWORD(0)

            if GetTokenInformation(access_token, TOKEN_INFORMATION__TOKEN_USER, None, 0, byref(length)) == 0:
                if GetLastError() != ERROR_INSUFFICIENT_BUFFER:
                    raise WinError()
                sid_info = (wintypes.BYTE * length.value)()
                if sid_info is None:
                    raise WinError()
                sid_info = c_cast(sid_info, POINTER(wintypes.LPVOID))
            else:
                sid_info = POINTER(wintypes.LPVOID)()
            if GetTokenInformation(access_token, TOKEN_INFORMATION__TOKEN_USER, sid_info, length, byref(length)) == 0:
                raise WinError()

            # The "sid_info" is a pointer to a structure, but the only thing we care about
            # is the first value in the structure (index 0), which is itself a pointer to a SID structure.
            sid_ptr = sid_info[0]

            username = create_unicode_buffer(MAX_USERNAME_LENGTH + 1)
            username_size = wintypes.DWORD(MAX_USERNAME_LENGTH)
            domain = create_unicode_buffer(MAX_USERNAME_LENGTH + 1)
            domain_size = wintypes.DWORD(MAX_USERNAME_LENGTH)
            sid_name_type = wintypes.DWORD()

            res = LookupAccountSidW(
                None, sid_ptr, username, byref(username_size),
                domain, byref(domain_size), byref(sid_name_type))
            if res == 0:
                raise WinError()

            # return username.value[0:username_size], domain.value[0:domain_size]
            return username.value, domain.value
        finally:
            windll.kernel32.CloseHandle(access_token)
    finally:
        windll.kernel32.CloseHandle(hproc)


def process__get_current_username_domain():
    # Just the username is easy (GetUserName), but the domain takes more work.
    return process__get_username_domain_for_pid(windll.kernel32.GetCurrentProcessId())


def process__load_all_process_details():
    raise OSError("Undefined")


# https://msdn.microsoft.com/en-us/library/windows/desktop/ms682648(v=vs.85).aspx
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms685992(v=vs.85).aspx
class ENUM_SERVICE_STATUS_PROCESS(Structure):
    _fields_ = [
        ("lpServiceName", c_wchar_p),  # string pointer
        ("lpDisplayName", c_wchar_p),  # string pointer
        # ServiceStatusProcess
        ("dwServiceType", wintypes.DWORD),
        ("dwCurrentState", wintypes.DWORD),
        ("dwControlsAccepted", wintypes.DWORD),
        ("dwWin32ExitCode", wintypes.DWORD),
        ("dwServiceSpecificExitCode", wintypes.DWORD),
        ("dwCheckPoint", wintypes.DWORD),
        ("dwWaitHint", wintypes.DWORD),
        ("dwProcessId", wintypes.DWORD),
        ("dwServiceFlags", wintypes.DWORD),
    ]

_SERVICE_TYPES = {
    1: 'SERVICE_KERNEL_DRIVER',
    2: 'SERVICE_FILE_SYSTEM_DRIVER',
    0x10: 'SERVICE_WIN32_OWN_PROCESS',
    0x20: 'SERVICE_WIN32_SHARE_PROCESS',
}
_SERVICE_CURRENT_STATES = {
    0x5: 'SERVICE_CONTINUE_PENDING',
    0x6: 'SERVICE_PAUSE_PENDING',
    0x7: 'SERVICE_PAUSED',
    0x4: 'SERVICE_RUNNING',
    0x2: 'SERVICE_START_PENDING',
    0x3: 'SERVICE_STOP_PENDING',
    0x1: 'SERVICE_STOPPED',
}


def process__get_all_service_information():
    advapi32 = WinDLL('advapi32.dll')
    OpenSCManager = advapi32.OpenSCManagerW
    OpenSCManager.restype = wintypes.DWORD
    EnumServicesStatusEx = advapi32.EnumServicesStatusExW
    # EnumServicesStatusExW(SC_HANDLE,SC_ENUM_TYPE,DWORD,DWORD,LPBYTE,DWORD,LPDWORD,LPDWORD,LPDWORD,LPCWSTR);
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
    CloseServiceHandle.argtypes = [wintypes.HANDLE]

    sc = OpenSCManager(None, None, SC_MANAGER_ENUMERATE_SERVICE)
    if sc == 0:
        raise WinError()
    try:
        bytes_needed = wintypes.DWORD(0)
        service_byte_count = wintypes.DWORD(0)
        service_count = wintypes.DWORD(0)
        resume_handle = wintypes.DWORD(0)
        status_array = None

        # Start off with 0 bytes allocated, and increase from there.
        while True:
            res = EnumServicesStatusEx(
                sc, SC_ENUM_PROCESS_INFO,
                # SERVICE_DRIVER | SERVICE_FILE_SYSTEM_DRIVER | SERVICE_KERNEL_DRIVER | SERVICE_WIN32,
                SERVICE_WIN32,
                SERVICE_STATE_ALL, status_array,
                service_byte_count, byref(bytes_needed), byref(service_count),
                byref(resume_handle), None
            )
            if res != 0:
                break
            if GetLastError() != ERROR_MORE_DATA:
                # raise ctypes.WinError()
                return []
            print("need {0} bytes".format(bytes_needed))
            service_byte_count = bytes_needed
            count = bytes_needed.value // c_sizeof(ENUM_SERVICE_STATUS_PROCESS)
            status_array = (ENUM_SERVICE_STATUS_PROCESS * count)()
        ret = []
        for i in range(service_count.value):
            status = status_array[i]
            controls_accepted = []
            if status.dwControlsAccepted & SERVICE_ACCEPT_NETBINDCHANGE == SERVICE_ACCEPT_NETBINDCHANGE:
                controls_accepted.append('SERVICE_ACCEPT_NETBINDCHANGE')
            if status.dwControlsAccepted & SERVICE_ACCEPT_PARAMCHANGE == SERVICE_ACCEPT_PARAMCHANGE:
                controls_accepted.append('SERVICE_ACCEPT_PARAMCHANGE')
            if status.dwControlsAccepted & SERVICE_ACCEPT_PAUSE_CONTINUE == SERVICE_ACCEPT_PAUSE_CONTINUE:
                controls_accepted.append('SERVICE_ACCEPT_PAUSE_CONTINUE')
            if status.dwControlsAccepted & SERVICE_ACCEPT_PRESHUTDOWN == SERVICE_ACCEPT_PRESHUTDOWN:
                controls_accepted.append('SERVICE_ACCEPT_PRESHUTDOWN')
            if status.dwControlsAccepted & SERVICE_ACCEPT_SHUTDOWN == SERVICE_ACCEPT_SHUTDOWN:
                controls_accepted.append('SERVICE_ACCEPT_SHUTDOWN')
            if status.dwControlsAccepted & SERVICE_ACCEPT_STOP == SERVICE_ACCEPT_STOP:
                controls_accepted.append('SERVICE_ACCEPT_STOP')

            ret.append({
                'display_name': status.lpServiceName.value,
                'service_name': status.lpDisplayName.value,
                'service_type': (
                    status.dwServiceType in _SERVICE_TYPES and
                    _SERVICE_TYPES[status.dwServiceType] or None
                ),
                'current_state': (
                    status.dwCurrentState in _SERVICE_CURRENT_STATES and
                    _SERVICE_CURRENT_STATES[status.dwCurrentState] or None
                ),
                'controls_accepted': controls_accepted,
                'exit_code': status.dwWin32ExitCode,
                'service_exit_code': status.dwServiceSpecificExitCode,
                'check_point': status.dwCheckPoint,
                'wait_time_millis_hint': status.dwWaitHint,
                'process_id': status.dwProcessId,
                'flags': status.dwServiceFlags == 1 and ['SERVICE_RUNS_IN_SYSTEM_PROCESS'] or [],
            })
        return ret
    finally:
        CloseServiceHandle(sc)


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
    ]


def shell__get_window_metrics():
    metrics = shell__get_raw_window_metrics()
    return {
        'border-width': metrics.iBorderWidth,
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

        # Vista support
        'padded-border-width': 0,
    }


def shell__get_raw_window_metrics():
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


# noinspection PyUnusedLocal
def shell__set_border_size(border_width, border_padding):
    metrics = shell__get_raw_window_metrics()
    metrics.iBorderWidth = border_width
    shell__set_window_metrics(metrics)


def shell__open_start_menu():
    # Find the task bar window
    taskbar_hwnd = windll.user32.FindWindowW("Shell_TrayWnd", None)
    if taskbar_hwnd is None or 0 == taskbar_hwnd:
        raise WinError()

    # Find the "start" button on the tray window
    start_hwnd = windll.user32.FindWindowExW(taskbar_hwnd, None, 'Button', 'Start')
    if start_hwnd is None:
        start_hwnd = windll.user32.FindWindowExW(taskbar_hwnd, None, None, 'Start')
        if start_hwnd is None:
            start_hwnd = windll.user32.FindWindowExW(taskbar_hwnd, None, 'Button', None)
            if start_hwnd is None:
                raise WinError()

    # Send a click message to the button
    windll.user32.SendMessageW(start_hwnd, BM_CLICK, 0, 0)


def process__get_all_pids():
    process_buff = (wintypes.DWORD * 2048)()
    process_size = wintypes.DWORD()
    res = windll.psapi.EnumProcesses(process_buff, c_sizeof(process_buff), byref(process_size))
    if res != 0:
        raise WinError()
    count = process_size / c_sizeof(wintypes.DWORD)
    ret = []
    for i in range(count):
        ret.append(process_buff[i])
    return ret


def create_window__create_borderless_window(func_map):
    style_flags = ['popup', 'visible']

    # Note that WM_CREATE just doesn't work.  Any attempt to use it,
    # even when explicitly returning 0, just causes the windows to be
    # destroyed.

    def window__create_borderless_window(class_name, title, message_handler, callback_map,
                                         show_on_taskbar=True, always_on_top=False):
        ex_style_flags = {
            'layered': True,
            'transparent': True,
            'window-edge': False,
            'client-edge': False,
            'topmost': always_on_top,
            'tool-window': not show_on_taskbar,
        }

        hwnd = func_map['window__create_display_window'](class_name, title, message_handler, style_flags)
        func_map['window__set_style'](hwnd, ex_style_flags)
        return hwnd

    return window__create_borderless_window
