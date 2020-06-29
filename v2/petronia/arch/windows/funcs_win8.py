"""
Windows 8 & 8.1 functions
"""

from ctypes import (windll, wintypes, byref, WinError,
                    create_unicode_buffer, GetLastError, POINTER)
from ctypes import cast as c_cast
from .windows_constants import *


def load_functions(environ, func_map):
    if environ['system'].lower() == 'windows' and (environ['release'].lower() == '8' or environ['release'].lower() == '8.1'):
        load_all_functions(func_map)


def load_all_functions(func_map):
    from .funcs_win7 import load_all_functions as w7_load
    w7_load(func_map)
    func_map['process__get_username_domain_for_pid'] = process__get_username_domain_for_pid
    func_map['process__get_current_username_domain'] = process__get_current_username_domain


def shell__open_start_menu():
    pass


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
    hproc = windll.kernel32.OpenProcess(PROCESS_QUERY_LIMITED_INFORMATION, False, thread_pid)
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
