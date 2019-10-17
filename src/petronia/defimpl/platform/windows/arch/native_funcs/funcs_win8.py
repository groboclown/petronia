"""
Windows 8 & 8.1 functions
"""

from typing import Tuple, Union
from ctypes import cast as c_cast
from .windows_common import (
    DWORD, BOOL, HANDLE, LPVOID, LPCWSTR, BYTE,
    POINTER, byref,
    windll,
    WindowsErrorMessage,
    create_unicode_buffer,
)
from ..windows_constants import *
from .supported_functions import (
    Functions,
)


def load_functions(environ: Dict[str, str], func_map: Functions) -> None:
    if environ['system'].lower() == 'windows' and (environ['release'].lower() == '8' or environ['release'].lower() == '8.1'):
        load_all_functions(func_map)


def load_all_functions(func_map: Functions) -> None:
    from .funcs_win7 import load_all_functions as w7_load
    w7_load(func_map)
    func_map.process.get_username_domain_for_pid = process__get_username_domain_for_pid
    func_map.process.get_current_username_domain = process__get_current_username_domain


def process__get_username_domain_for_pid(thread_pid: DWORD) -> Union[Tuple[str, str], WindowsErrorMessage]:
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
        POINTER(DWORD)
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

            if GetTokenInformation(access_token, TOKEN_INFORMATION__TOKEN_USER, None, 0, byref(length)) == 0:
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
            if GetTokenInformation(access_token, TOKEN_INFORMATION__TOKEN_USER, sid_info, length, byref(length)) == 0:
                return WindowsErrorMessage('advapi32.GetTokenInformation')

            # The "sid_info" is a pointer to a structure, but the only thing we care about
            # is the first value in the structure (index 0), which is itself a pointer to a SID structure.
            sid_ptr = sid_info[0]

            username = create_unicode_buffer(MAX_USERNAME_LENGTH + 1)
            username_size = DWORD(MAX_USERNAME_LENGTH)
            domain = create_unicode_buffer(MAX_USERNAME_LENGTH + 1)
            domain_size = DWORD(MAX_USERNAME_LENGTH)
            sid_name_type = DWORD()

            res = LookupAccountSidW(
                None, sid_ptr, username, byref(username_size),
                domain, byref(domain_size), byref(sid_name_type))
            if res == 0:
                return WindowsErrorMessage('advapi32.LookupAccountSidW')

            # return username.value[0:username_size], domain.value[0:domain_size]
            return username.value, domain.value
        finally:
            windll.kernel32.CloseHandle(access_token)
    finally:
        windll.kernel32.CloseHandle(hproc)


def process__get_current_username_domain() -> Union[Tuple[str, str], WindowsErrorMessage]:
    # Just the username is easy (GetUserName), but the domain takes more work.
    return process__get_username_domain_for_pid(windll.kernel32.GetCurrentProcessId())
