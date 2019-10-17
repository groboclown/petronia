
# mypy: allow-any-generics
# mypy: allow-any-explicit

"""
Windows 10 functions
"""
from ctypes import WinError
from typing import Dict, Optional
from typing import cast as t_cast
from .windows_common import (
    CFUNCTYPE,
    DWORD,
    LONG,
    UINT,
    BOOL,
    HWND,
    LPARAM,
    c_long,

    POINT,
    RECT,

    Structure,
    WindowsErrorMessage,
    create_unicode_buffer,
    windll,
    byref,
    c_sizeof,
)
from .supported_functions import (
    Functions,
)
from ..windows_constants import (
    WM_LBUTTONDOWN,
    MK_LBUTTON,
    BM_CLICK,
    SW_SHOWNORMAL,
    SW_MAXIMIZE,
    SW_SHOWMAXIMIZED,
    SW_SHOWNOACTIVATE,
    SW_SHOW,
    SW_SHOWNA,
    SW_RESTORE,
    SW_HIDE,
    SWP_NOSIZE,
    SWP_NOMOVE,
    HWND_TOPMOST,
    HWND_NOTOPMOST,
    TH32CS_SNAPTHREAD,
    INVALID_HANDLE_VALUE,
)


def load_functions(environ: Dict[str, str], func_map: Functions) -> None:
    if environ['system'].lower() == 'windows' and environ['release'].lower() == '10':
        load_all_functions(func_map)


def load_all_functions(func_map: Functions) -> None:
    from .funcs_win8 import load_all_functions as w8_load
    w8_load(func_map)
    func_map.shell.open_start_menu = shell__open_start_menu


# https://msdn.microsoft.com/en-us/library/windows/desktop/ms686735(v=vs.85).aspx
class THREADENTRY32(Structure):
    _fields_ = [
        ("dwSize", DWORD),
        ("cntUsage", DWORD),
        ("th32ThreadID", DWORD),
        ("th32OwnerProcessID", DWORD),
        ("tpBasePri", LONG),
        ("tpDeltaPri", LONG),
        ("dwFlags", DWORD),
    ]


# see https://msdn.microsoft.com/en-us/library/windows/desktop/ms632611(v=vs.85).aspx
class WINDOWPLACEMENT(Structure):
    _fields_ = [
        ("length", UINT),
        ("flags", UINT),
        ("showCmd", UINT),
        ("ptMinPosition", POINT),
        ("ptMaxPosition", POINT),
        ("rcNormalPosition", RECT),
    ]


def shell__open_start_menu(show_taskbar: bool) -> Optional[WindowsErrorMessage]:
    # Find the task bar window
    taskbar_hwnd = windll.user32.FindWindowW("Shell_TrayWnd", None)
    if taskbar_hwnd is None or 0 == taskbar_hwnd:
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
                else:
                    try:
                        print("<<ERROR pressing start button>>")
                        raise WinError()
                    except OSError:
                        import traceback
                        traceback.print_exc()
        return True

    callback_type = CFUNCTYPE(BOOL, HWND, LPARAM)
    callback_ptr = callback_type(child_window_callback)
    print("DEBUG Iterating over windows for taskbar pid {0}".format(taskbar_pid.value))
    windll.user32.EnumChildWindows(taskbar_hwnd, callback_ptr, 0)

    # if not triggered_start[0]:
    #     raise OSError("Could not find start button")

    return None


def shell__open_start_menu_bad(show_taskbar: bool) -> None:
    # Find the task bar window
    taskbar_hwnd = windll.user32.FindWindowW("Shell_TrayWnd", None)
    if taskbar_hwnd is None or 0 == taskbar_hwnd:
        raise WinError()
    taskbar_size = RECT()
    windll.user32.GetWindowRect(taskbar_hwnd, byref(taskbar_size))

    # Find the process ID of the taskbar window.
    taskbar_pid = DWORD()
    windll.user32.GetWindowThreadProcessId(taskbar_hwnd, byref(taskbar_pid))

    # Find the child window that has a "Start" class name.

    # TODO this is all wrong below here for Windows 10.

    # Find a thread in that process that has a "Start" button
    triggered_start = [False]

    # noinspection PyUnusedLocal
    def thread_window_callback(hwnd: HWND, lparam: LPARAM) -> bool:
        class_buffer = create_unicode_buffer(256)
        length = windll.user32.GetClassNameW(hwnd, class_buffer, 256)
        if length <= 0:
            class_name = None
        else:
            class_name = str(class_buffer.value)[:length]
        length = windll.user32.GetWindowTextLengthW(hwnd)
        if length > 0:
            title_buff = create_unicode_buffer(length + 1)
            windll.user32.GetWindowTextW(hwnd, title_buff, length + 1)
            print("DEBUG - Inspecting {0} | {2} = {1}".format(hwnd, title_buff.value, class_name))
            if title_buff.value == "Start":
                # Found the window
                print("DEBUG sending Click message")
                m_res = windll.user32.SendMessageW(hwnd, BM_CLICK, 0, 0)
                if m_res != 0:
                    # Don't look anymore
                    triggered_start[0] = True
                    return False
                else:
                    try:
                        # Note: WinError only used here for error debugging.
                        print("<<ERROR pressing start button>>")
                        raise WinError()
                    except OSError:
                        import traceback
                        traceback.print_exc()
            if title_buff.value == "Start menu":
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
                            print("DEBUG hiding the start menu {0}".format(show_cmd))
                            windll.user32.ShowWindow(hwnd, SW_HIDE)
                            return False
                # print("DEBUG showing the start menu ({0})".format(placement.showCmd))
                windll.user32.ShowWindow(hwnd, SW_SHOW)

                # If the task bar is hidden, then part of the start window is not shown fully.
                # SW_MAXIMIZE will show it fully, but the rendering becomes messed up.
                taskbar_rect = RECT()
                windll.user32.GetClientRect(taskbar_hwnd, byref(taskbar_rect))

                client_rect = RECT()
                windll.user32.GetClientRect(hwnd, byref(client_rect))

                overlap_rect = RECT()
                if windll.user32.IntersectRect(byref(overlap_rect), byref(taskbar_rect), byref(client_rect)) != 0:
                    # The taskbar and the start window rectangles overlap each other.
                    # Adjust the start window to be outside of this.
                    # Remember: the taskbar can be anywhere on the edge of the screen.
                    client_left = client_rect.left.value
                    client_right = client_rect.right.value
                    client_top = client_rect.top.value
                    overlap_left = overlap_rect.left.value
                    overlap_right = overlap_rect.right.value
                    overlap_top = overlap_rect.top.value
                    overlap_bottom = overlap_rect.bottom.value
                    new_x = client_left
                    new_y = client_top
                    if overlap_left == client_left and overlap_right == client_right:
                        # Adjust along the y axis
                        if overlap_top <= client_top <= overlap_bottom:
                            # Adjust down
                            new_y = overlap_bottom
                        else:
                            # Adjust up
                            new_y = client_top - (overlap_bottom - overlap_top)
                    else:
                        # Adjust along the x axis
                        if overlap_left <= client_left <= overlap_right:
                            # Adjust to the right
                            new_x = overlap_right
                        else:
                            new_x = client_left - (overlap_right - overlap_left)
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
        else:
            print("DEBUG - Inspecting {0} | {1} => no title, ignoring".format(hwnd, class_name))
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

    callback_type = CFUNCTYPE(BOOL, HWND, LPARAM)
    callback_ptr = callback_type(thread_window_callback)
    for thread_id in thread_ids:
        print("DEBUG Iterating over windows for thread {0} in pid {1}".format(thread_id, taskbar_pid.value))
        windll.user32.EnumThreadWindows(thread_id, callback_ptr, 0)
        if triggered_start[0]:
            return

    raise OSError("Could not find start button")
