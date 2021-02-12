"""
Windows 10 functions
"""

# mypy: allow-any-generics
# mypy: allow-any-explicit

import traceback
from ctypes import WinError
from typing import Dict, Optional
# from typing import cast as t_cast
from .windows_common import (
    CFUNCTYPE,
    DWORD,
    LONG,
    UINT,
    BOOL,
    HWND,
    LPARAM,

    POINT,
    RECT,

    Structure,
    WindowsErrorMessage,
    create_unicode_buffer,
    windll,
    byref,
)
from .supported_functions import (
    Functions,
)
from ..windows_constants import (
    WM_LBUTTONDOWN,
    MK_LBUTTON,
)


def load_functions(environ: Dict[str, str], func_map: Functions) -> None:
    """Load the functions, if the current platform is windows 10."""
    if environ['system'].lower() == 'windows' and environ['release'].lower() == '10':
        load_all_functions(func_map)


def load_all_functions(func_map: Functions) -> None:
    """Load all functions into the structure."""
    from .funcs_win8 import load_all_functions as w8_load  # pylint:disable=import-outside-toplevel
    w8_load(func_map)
    func_map.shell.open_start_menu = shell__open_start_menu


class THREADENTRY32(Structure):
    """The THREADENTRY32 structure.
    See https://msdn.microsoft.com/en-us/library/windows/desktop/ms686735(v=vs.85).aspx"""
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
    see https://msdn.microsoft.com/en-us/library/windows/desktop/ms632611(v=vs.85).aspx
    """
    _fields_ = [
        ("length", UINT),
        ("flags", UINT),
        ("showCmd", UINT),
        ("ptMinPosition", POINT),
        ("ptMaxPosition", POINT),
        ("rcNormalPosition", RECT),
    ]


def shell__open_start_menu(_show_taskbar: bool) -> Optional[WindowsErrorMessage]:
    """Try to open the start menu."""
    # Find the task bar window
    taskbar_hwnd = windll.user32.FindWindowW("Shell_TrayWnd", None)
    if taskbar_hwnd is None or taskbar_hwnd == 0:
        return WindowsErrorMessage('user32.FindWindowW')
    taskbar_size = RECT()
    windll.user32.GetWindowRect(taskbar_hwnd, byref(taskbar_size))

    # Find the process ID of the taskbar window.
    taskbar_pid = DWORD()
    windll.user32.GetWindowThreadProcessId(taskbar_hwnd, byref(taskbar_pid))

    triggered_start = [False]

    # Find the "Start" button in the taskbar.
    def child_window_callback(hwnd: HWND, _: LPARAM) -> bool:
        class_buffer = create_unicode_buffer(256)
        length = windll.user32.GetClassNameW(hwnd, class_buffer, 256)
        if length <= 0:
            class_name = None
        else:
            class_name = class_buffer.value[:length]
        length = windll.user32.GetWindowTextLengthW(hwnd)
        if length > 0:
            title_buff = create_unicode_buffer(length + 1)
            windll.user32.GetWindowTextW(hwnd, title_buff, length + 1)
            print("DEBUG - Inspecting {0} | {2} = {1}".format(hwnd, title_buff.value, class_name))
            if title_buff.value == "Start":
                # Found the window
                print("DEBUG sending Click message")

                # Attach our thread input to the start button, so we can send it a message.
                current_thread_id = windll.kernel32.GetCurrentThreadId()
                thread_process_id = windll.user32.GetWindowThreadProcessId(hwnd, None)
                m_res = windll.user32.AttachThreadInput(thread_process_id, current_thread_id, True)
                if not m_res:
                    return False
                m_res = windll.user32.SendMessageW(hwnd, WM_LBUTTONDOWN, MK_LBUTTON, 0)
                if m_res == 0:
                    # Don't look anymore
                    triggered_start[0] = True
                    return False
                try:
                    print("<<ERROR pressing start button>>")
                    raise WinError()
                except OSError:
                    traceback.print_exc()
        return True

    callback_type = CFUNCTYPE(BOOL, HWND, LPARAM)
    callback_ptr = callback_type(child_window_callback)
    print("DEBUG Iterating over windows for taskbar pid {0}".format(taskbar_pid.value))
    windll.user32.EnumChildWindows(taskbar_hwnd, callback_ptr, 0)

    # if not triggered_start[0]:
    #     raise OSError("Could not find start button")

    return None
