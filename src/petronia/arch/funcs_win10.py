"""
Windows 10 functions
"""


from ctypes import c_int, wintypes, windll, Structure, WinError, byref, create_unicode_buffer, CFUNCTYPE
from ctypes import sizeof as c_sizeof
from .windows_constants import *


def load_functions(environ, func_map):
    if environ['system'].lower() == 'windows' and environ['release'].lower() == '10':
        load_all_functions(func_map)


def load_all_functions(func_map):
    from .funcs_win8 import load_all_functions as w8_load
    w8_load(func_map)
    func_map['shell__open_start_menu'] = shell__open_start_menu


# https://msdn.microsoft.com/en-us/library/windows/desktop/ms686735(v=vs.85).aspx
class THREADENTRY32(Structure):
    _fields_ = [
        ("dwSize", wintypes.DWORD),
        ("cntUsage", wintypes.DWORD),
        ("th32ThreadID", wintypes.DWORD),
        ("th32OwnerProcessID", wintypes.DWORD),
        ("tpBasePri", wintypes.LONG),
        ("tpDeltaPri", wintypes.LONG),
        ("dwFlags", wintypes.DWORD),
    ]


# see https://msdn.microsoft.com/en-us/library/windows/desktop/ms632611(v=vs.85).aspx
class WINDOWPLACEMENT(Structure):
    _fields_ = [
        ("length", wintypes.UINT),
        ("flags", wintypes.UINT),
        ("showCmd", wintypes.UINT),
        ("ptMinPosition", wintypes.POINT),
        ("ptMaxPosition", wintypes.POINT),
        ("rcNormalPosition", wintypes.RECT),
    ]


def shell__open_start_menu(show_taskbar):
    # Find the task bar window
    taskbar_hwnd = windll.user32.FindWindowW("Shell_TrayWnd", None)
    if taskbar_hwnd is None or 0 == taskbar_hwnd:
        raise WinError()
    taskbar_size = wintypes.RECT()
    windll.user32.GetWindowRect(taskbar_hwnd, byref(taskbar_size))

    # Find the process ID of the taskbar window.
    taskbar_pid = wintypes.DWORD()
    windll.user32.GetWindowThreadProcessId(taskbar_hwnd, byref(taskbar_pid))
    
    triggered_start = [False]
    
    # Find the "Start" button in the taskbar.
    def child_window_callback(hwnd, lparam):
        class_buff = create_unicode_buffer(256)
        length = windll.user32.GetClassNameW(hwnd, class_buff, 256)
        if length <= 0:
            class_buff = None
        else:
            class_buff = class_buff.value[:length]
        length = windll.user32.GetWindowTextLengthW(hwnd)
        if length > 0:
            title_buff = create_unicode_buffer(length + 1)
            windll.user32.GetWindowTextW(hwnd, title_buff, length + 1)
            print("DEBUG - Inspecting {0} | {2} = {1}".format(hwnd, title_buff.value, class_buff))
            if title_buff.value == "Start":
                # Found the window
                print("DEBUG sending Click message")
                
                # Attach our thread input to the start button, so we can send it a message.
                current_thread_id = windll.kernel32.GetCurrentThreadId()
                thread_process_id = windll.user32.GetWindowThreadProcessId(hwnd, None)
                m_res = windll.user32.AttachThreadInput(thread_process_id, current_thread_id, True)
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
        
    callback_type = CFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)
    callback_ptr = callback_type(child_window_callback)
    print("DEBUG Iterating over windows for taskbar pid {0}".format(taskbar_pid.value))
    windll.user32.EnumChildWindows(taskbar_hwnd, callback_ptr, 0)

    # if not triggered_start[0]:
    #     raise OSError("Could not find start button")


def shell__open_start_menu_bad(show_taskbar):
    # Find the task bar window
    taskbar_hwnd = windll.user32.FindWindowW("Shell_TrayWnd", None)
    if taskbar_hwnd is None or 0 == taskbar_hwnd:
        raise WinError()
    taskbar_size = wintypes.RECT()
    windll.user32.GetWindowRect(taskbar_hwnd, byref(taskbar_size))

    # Find the process ID of the taskbar window.
    taskbar_pid = wintypes.DWORD()
    windll.user32.GetWindowThreadProcessId(taskbar_hwnd, byref(taskbar_pid))
    
    # Find the child window that has a "Start" class name.
    
    # TODO this is all wrong below here for Windows 10.

    # Find a thread in that process that has a "Start" button
    triggered_start = [False]

    # noinspection PyUnusedLocal
    def thread_window_callback(hwnd, lparam):
        class_buff = create_unicode_buffer(256)
        length = windll.user32.GetClassNameW(hwnd, class_buff, 256)
        if length <= 0:
            class_buff = None
        else:
            class_buff = class_buff.value[:length]
        length = windll.user32.GetWindowTextLengthW(hwnd)
        if length > 0:
            title_buff = create_unicode_buffer(length + 1)
            windll.user32.GetWindowTextW(hwnd, title_buff, length + 1)
            print("DEBUG - Inspecting {0} | {2} = {1}".format(hwnd, title_buff.value, class_buff))
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
                print("DEBUG showing the start menu ({0})".format(placement.showCmd))
                windll.user32.ShowWindow(hwnd, SW_SHOW)

                # If the task bar is hidden, then part of the start window is not shown fully.
                # SW_MAXIMIZE will show it fully, but the rendering becomes messed up.
                taskbar_rect = wintypes.RECT()
                windll.user32.GetClientRect(taskbar_hwnd, byref(taskbar_rect))

                client_rect = wintypes.RECT()
                windll.user32.GetClientRect(hwnd, byref(client_rect))

                overlap_rect = wintypes.RECT()
                if windll.user32.IntersectRect(byref(overlap_rect), byref(taskbar_rect), byref(client_rect)) != 0:
                    # The taskbar and the start window rectangles overlap each other.
                    # Adjust the start window to be outside of this.
                    # Remember: the taskbar can be anywhere on the edge of the screen.
                    new_x = client_rect.left
                    new_y = client_rect.top
                    if overlap_rect.left == client_rect.left and overlap_rect.right == client_rect.right:
                        # Adjust along the y axis
                        if overlap_rect.top <= client_rect.top <= overlap_rect.bottom:
                            # Adjust down
                            new_y = overlap_rect.bottom
                        else:
                            # Adjust up
                            new_y = client_rect.top - (overlap_rect.bottom - overlap_rect.top)
                    else:
                        # Adjust along the x axis
                        if overlap_rect.left <= client_rect.left <= overlap_rect.right:
                            # Adjust to the right
                            new_x = overlap_rect.right
                        else:
                            new_x = client_rect.left - (overlap_rect.right - overlap_rect.left)
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
            print("DEBUG - Inspecting {0} | {1} => no title, ignoring".format(hwnd, class_buff))
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

    callback_type = CFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)
    callback_ptr = callback_type(thread_window_callback)
    for thread_id in thread_ids:
        print("DEBUG Iterating over windows for thread {0} in pid {1}".format(thread_id, taskbar_pid.value))
        windll.user32.EnumThreadWindows(thread_id, callback_ptr, 0)
        if triggered_start[0]:
            return

    raise OSError("Could not find start button")
