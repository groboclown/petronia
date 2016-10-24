
"""
The task bar across all the windows.
"""

# General method for replacing the built-in task bar:
#   1. Find the existing task bar:
#           FindWindowW("Shell_TrayWnd", None)
#      If it already exists, then don't replace it, just add our custom thingy.
#   2. Setup and register WNDCLASS wc:
#          wc.lpfnWndProc = callback(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
#          wc.hInstance = some module handle
#          wc.lpszClassName = "Shell_TrayWnd"
#          wc.style = CS_DBLCLKS
#          RegisterClass(byref(wc))
#   3. Create the window
#          CreateWindowEx(
#               WS_EX_TOOLWINDOW,
#               wc.lpszClassName,
#               wc.lpszClassName,
#               WS_POPUP | WS_CLIPSIBLINGS | WS_CLIPCHILDREN | WS_OVERLAPPED,
#               0,0,0,0, None, None, module handle, POINTER(this window))
#   4. Post a broadcast message that the taskbar was created.
#          PostMessage(HWND_BROADCAST, RegisterWindowMessage("TaskbarCreated"), 0,0)
#   ... lots of other things.
