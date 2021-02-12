"""
Windows 7 functions
"""

# Many places use Windows naming convention for things, not Python.
# pylint:disable=invalid-name

from typing import List, Sequence, Dict, Union
from ctypes import sizeof as c_sizeof
from .windows_common import (
    DWORD,
    create_unicode_buffer, byref, windll,
    WindowsErrorMessage,
)
from ..windows_constants import (
    PROCESS_QUERY_INFORMATION, PROCESS_VM_READ,
    MAX_FILENAME_LENGTH,
)
from .supported_functions import (
    Functions,
)


def load_functions(environ: Dict[str, str], func_map: Functions) -> None:
    """Load the windows 7 functions, if the current platform is windows 7."""
    # TODO include Windows Server 2008 R2 detection
    if environ['system'].lower() == 'windows' and environ['release'].lower() == '7':
        load_all_functions(func_map)


def load_all_functions(func_map: Functions) -> None:
    """Load all the functions into the function map."""
    from .funcs_win_vista import load_all_functions as wv_load  # pylint:disable=import-outside-toplevel
    wv_load(func_map)
    load_kernel_functions(func_map)
    # func_map['shell__open_start_menu'] = shell__open_start_menu


def load_kernel_functions(func_map: Functions) -> None:
    """Load in the kernel functions."""
    func_map.process.get_executable_filename = process__get_executable_filename
    func_map.process.get_all_pids = process__get_all_pids


def process__get_executable_filename(thread_pid: DWORD) -> Union[WindowsErrorMessage, str]:
    """Get executable filename for the thread PIDs; processes not services."""

    GetProcessImageFileName = windll.kernel32.K32GetProcessImageFileNameW
    GetProcessImageFileName.restype = DWORD
    OpenProcess = windll.kernel32.OpenProcess
    # OpenProcess.restype = wintypes.HANDLE

    hproc = OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, thread_pid)
    if hproc is None or hproc == 0:
        # err = WindowsErrorMessage('kernel32.OpenProcess')
        # print(f"WARNING *** Failed to open process handle for pid {thread_pid}: {err}")
        # return err
        return WindowsErrorMessage('kernel32.OpenProcess')
    try:
        filename = create_unicode_buffer(MAX_FILENAME_LENGTH + 1)

        # For some reason, this isn't found in Windows 10.
        res = GetProcessImageFileName(hproc, byref(filename), MAX_FILENAME_LENGTH + 1)
        if res <= 0:
            # print(f"DEBUG failed to read filename for handle {hproc} pid {thread_pid}")
            return WindowsErrorMessage('kernel32.K32GetProcessImageFileNameW')
        # print(f"DEBUG found filename for pid {thread_pid}: {filename.value}")
        return str(filename.value[:res])
    finally:
        windll.kernel32.CloseHandle(hproc)


# def shell__open_start_menu():
#     # In Windows 7, the start button is part of the desktop?
#     desktop_hwnd = windll.user32.GetDesktopWindow()
#
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


def process__get_all_pids() -> Union[WindowsErrorMessage, Sequence[DWORD]]:
    """Get all PIDs for running processes."""
    process_buff = (DWORD * 2048)()
    process_size = DWORD()
    res = windll.psapi.EnumProcesses(process_buff, c_sizeof(process_buff), byref(process_size))
    if res != 0:
        return WindowsErrorMessage('psapi.EnumProcesses')
    count = process_size.value // c_sizeof(DWORD)
    ret: List[DWORD] = []
    for i in range(count):
        ret.append(DWORD(process_buff[i]))
    return tuple(ret)
