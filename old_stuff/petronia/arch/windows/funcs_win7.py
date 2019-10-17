"""
Windows 7 functions
"""

import ctypes
from ctypes import windll, wintypes, byref, POINTER, WinError, create_unicode_buffer, GetLastError
from ctypes import sizeof as c_sizeof
from .windows_constants import *


def load_functions(environ, func_map):
    # TODO include Windows Server 2008 R2 detection
    if environ['system'].lower() == 'windows' and environ['release'].lower() == '7':
        load_all_functions(func_map)


def load_all_functions(func_map):
    from .funcs_winVista import load_all_functions as wv_load
    wv_load(func_map)
    load_kernel_functions(func_map)
    # func_map['shell__open_start_menu'] = shell__open_start_menu


def load_kernel_functions(func_map):
    func_map['process__get_executable_filename'] = process__get_executable_filename
    func_map['process__get_all_pids'] = process__get_all_pids


def process__get_executable_filename(thread_pid):
    # This only finds processes, not services.

    GetProcessImageFileName = windll.kernel32.K32GetProcessImageFileNameW
    GetProcessImageFileName.restype = wintypes.DWORD
    OpenProcess = windll.kernel32.OpenProcess
    # OpenProcess.restype = wintypes.HANDLE

    hproc = OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, thread_pid)
    if hproc is None:
        raise WinError()
    try:
        filename = create_unicode_buffer(MAX_FILENAME_LENGTH + 1)

        # For some reason, this isn't found in Windows 10.
        res = GetProcessImageFileName(hproc, byref(filename), MAX_FILENAME_LENGTH + 1)
        if res <= 0:
            # raise ctypes.WinError()
            return None
        return str(filename.value[:res])
    finally:
        windll.kernel32.CloseHandle(hproc)


# def shell__open_start_menu():
#     # In Windows 7, the start button is part of the desktop?
#     desktop_hwnd = windll.user32.GetDesktopWindow()
#
#     # FIXME DEBUG
#     print("DEBUG desktop_hwnd: {0}".format(desktop_hwnd))
#
#     # Find the "start" button on the tray window
#     start_hwnd = windll.user32.FindWindowExW(desktop_hwnd, None, 'Button', 'Start')
#     if (start_hwnd is None or start_hwnd == 0) and GetLastError() != 0:
#         start_hwnd = windll.user32.FindWindowExW(desktop_hwnd, None, None, 'Start')
#         if (start_hwnd is None or start_hwnd == 0) and GetLastError() != 0:
#             # start_hwnd = windll.user32.FindWindowExW(desktop_hwnd, None, 'Button', None)
#             if start_hwnd is None or start_hwnd == 0:
#                 raise WinError()
#     print("Start button: {0}".format(start_hwnd))
#
#     # Send a click message to the button
#     res = windll.user32.SendMessageW(start_hwnd, BM_CLICK, 0, 0)
#     if res == 0:
#         raise WinError()


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
