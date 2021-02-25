"""
Windows 8 & 8.1 functions
"""

# Many places use Windows naming convention for things, not Python.
# pylint:disable=invalid-name

from typing import List, Tuple, Dict, Sequence, Union, Optional
from ctypes import c_bool
from ctypes import cast as c_cast
from .windows_common import (
    DWORD, BOOL, HANDLE, LPVOID, LPCWSTR, BYTE, UINT, LONG, c_int, HDC, LPRECT, LPARAM,
    HMONITOR, WINFUNCTYPE,
    POINTER, byref, c_sizeof,
    windll,
    WindowsErrorMessage,
    create_unicode_buffer,
)
from .funcs_any_win import (
    EnumDisplayMonitors, MONITORINFOEXW, GetMonitorInfoW,
)
from .monitor import WindowsMonitor
from .supported_functions import (
    Functions,
)
from ..windows_constants import (
    PROCESS_QUERY_LIMITED_INFORMATION, ERROR_ACCESS_DENIED, TOKEN_QUERY,
    TOKEN_INFORMATION__TOKEN_USER, ERROR_INSUFFICIENT_BUFFER,
    MAX_USERNAME_LENGTH, PROCESS_PER_MONITOR_DPI_AWARE,
    MDT_RAW_DPI, S_OK, SCALE_100_PERCENT, MONITORINFOF_PRIMARY,
)


def load_functions(environ: Dict[str, str], func_map: Functions) -> None:
    """Load all the functions in this module, if the platform is windows 8"""
    if (
            environ['system'].lower() == 'windows'
            and environ['release'].lower() in (
                '8', '8.1', '2012server', '2012serverr2', 'post8.1',
                'post2012serverr2',
            )
    ):
        load_all_functions(func_map)


def load_all_functions(func_map: Functions) -> None:
    """Load in all the functions for this platform."""
    from .funcs_win7 import load_all_functions as w7_load  # pylint:disable=import-outside-toplevel
    w7_load(func_map)
    func_map.process.get_username_domain_for_pid = process__get_username_domain_for_pid
    func_map.process.get_current_username_domain = process__get_current_username_domain
    func_map.monitor.find_monitors = monitor__find_monitors
    func_map.monitor.set_native_dpi_awareness = monitor__set_native_dpi_awareness


def process__get_username_domain_for_pid(  # pylint:disable=too-many-branches,too-many-return-statements,too-many-locals
        thread_pid: DWORD,
) -> Union[Tuple[str, str], WindowsErrorMessage]:
    """

    :param thread_pid:
    :return: the tuple (username, domain) for the user that owns the pid.
    """
    OpenProcessToken = windll.advapi32.OpenProcessToken
    OpenProcessToken.argtypes = (HANDLE, DWORD, POINTER(HANDLE))
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
    hproc = windll.kernel32.OpenProcess(PROCESS_QUERY_LIMITED_INFORMATION, False, thread_pid)
    if hproc == 0:
        err = WindowsErrorMessage('kernel32.OpenProcess')
        if err.errno == ERROR_ACCESS_DENIED:
            # Don't raise a problem in this situation.  Instead, return unique information.
            return "[denied]", "[denied]"
        return err
    try:
        access_token = HANDLE()
        res = OpenProcessToken(hproc, DWORD(TOKEN_QUERY), byref(access_token))
        if res == 0 or access_token is None:
            return WindowsErrorMessage('advapi32.OpenProcessToken')
        try:
            length = DWORD(0)

            if GetTokenInformation(
                    access_token, TOKEN_INFORMATION__TOKEN_USER, None, 0, byref(length),
            ) == 0:
                err = WindowsErrorMessage('advapi32.GetTokenInformation')
                if err.errno != ERROR_INSUFFICIENT_BUFFER:
                    return err
                base_sid_info = (BYTE * length.value)()
                if base_sid_info is None:
                    # Could not allocate space.
                    # May be wrong error...
                    return WindowsErrorMessage('malloc')
                sid_info = c_cast(base_sid_info, POINTER(LPVOID))
            else:
                sid_info = POINTER(LPVOID)()
            if GetTokenInformation(
                    access_token, TOKEN_INFORMATION__TOKEN_USER, sid_info, length, byref(length),
            ) == 0:
                return WindowsErrorMessage('advapi32.GetTokenInformation')

            # The "sid_info" is a pointer to a structure, but the only thing we care about
            # is the first value in the structure (index 0), which is itself a pointer to a
            # SID structure.
            sid_ptr = sid_info[0]

            username = create_unicode_buffer(MAX_USERNAME_LENGTH + 1)
            username_size = DWORD(MAX_USERNAME_LENGTH)
            domain = create_unicode_buffer(MAX_USERNAME_LENGTH + 1)
            domain_size = DWORD(MAX_USERNAME_LENGTH)
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


def monitor__set_native_dpi_awareness() -> Optional[WindowsErrorMessage]:
    """Set the DPI awareness for this process.  This affects how the API calls act on
    screen pixel units."""
    awareness = c_int()
    error_code = windll.shcore.GetProcessDpiAwareness(0, byref(awareness))
    if error_code != 0:  # S_OK
        return WindowsErrorMessage('shcore.GetProcessDpiAwareness', error_code)

    if awareness != PROCESS_PER_MONITOR_DPI_AWARE:
        error_code = windll.shcore.SetProcessDpiAwareness(2)
        if error_code != 0:  # S_OK
            return WindowsErrorMessage('shcore.SetProcessDpiAwareness', error_code)

    return None


def monitor__find_monitors() -> Sequence[WindowsMonitor]:
    """Get the list of monitors."""
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
        return ()

    ret: List[WindowsMonitor] = []
    index = 0
    dpi_x = UINT()
    dpi_y = UINT()
    scale_factor = c_int()
    for monitor_handle, vd_l, vd_r, vd_t, vd_b in monitor_handles:
        info = MONITORINFOEXW()
        info.cbSize = c_sizeof(MONITORINFOEXW)
        if GetMonitorInfoW(monitor_handle, byref(info)) != 0:
            res = windll.shcore.GetDpiForMonitor(
                monitor_handle, MDT_RAW_DPI, byref(dpi_x), byref(dpi_y),
            )
            if res != S_OK:
                # could not get the DPI; use the default.
                dpi_x = UINT(96)
                dpi_y = UINT(96)
                print(f"DEBUG ** Monitor {index}/{monitor_handle} could not find DPI: {res}")
            else:
                print(
                    f"DEBUG ** Monitor {index}/{monitor_handle} "
                    f"has dpi ({dpi_x}, {dpi_y})/{type(dpi_x)}"
                )

            res = windll.shcore.GetScaleFactorForMonitor(
                monitor_handle, byref(scale_factor)
            )
            if res != S_OK:
                # could not get the scale factor.
                scale_factor = c_int(SCALE_100_PERCENT)
                print(
                    f"DEBUG ** Monitor {index}/{monitor_handle} could not find scale factor: {res}"
                )
            else:
                print(
                    f"DEBUG ** Monitor {index}/{monitor_handle} has scale factor "
                    f"{repr(scale_factor)}/{type(scale_factor)}"
                )

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
                scale_factor=scale_factor.value,
                dpi_x=dpi_x.value,
                dpi_y=dpi_y.value,
            ))
        index += 1

    return ret
