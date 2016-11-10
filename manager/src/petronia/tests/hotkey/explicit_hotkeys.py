
import sys

import ctypes
from ctypes import wintypes
from ctypes import CFUNCTYPE, POINTER, c_int, c_uint, c_void_p
from ctypes import byref
import atexit

WH_KEYBOARD_LL = 0x00D

GetModuleHandleA = ctypes.windll.kernel32.GetModuleHandleA
GetModuleHandleA.restype = wintypes.HMODULE
GetModuleHandleA.argtypes = [wintypes.LPCWSTR]

SetWindowsHookExA = ctypes.windll.user32.SetWindowsHookExA
SetWindowsHookExA.restype = c_int
SetWindowsHookExA.argtypes = [c_int, CFUNCTYPE(c_int, c_int, wintypes.HINSTANCE, POINTER(c_void_p)), wintypes.HINSTANCE, wintypes.DWORD]

GetMessageW = ctypes.windll.user32.GetMessageW
GetMessageW.argtypes = [POINTER(wintypes.MSG), wintypes.HWND, c_uint, c_uint]

DispatchMessageW = ctypes.windll.user32.DispatchMessageW
DispatchMessageW.argtypes = [POINTER(wintypes.MSG)]

TranslateMessage = ctypes.windll.user32.TranslateMessage
TranslateMessage.argtypes = [POINTER(wintypes.MSG)]

CallNextHookEx = ctypes.windll.user32.CallNextHookEx

UnhookWindowsHookEx = ctypes.windll.user32.UnhookWindowsHookEx


if __name__ == '__main__':
    def handler(key_code, event_code):
        print("{0} {1}".format(hex(key_code), hex(event_code)))
    handle = [None]

    def low_level_callback(code, rparam, lparam):
        try:
            key_code = 0xFFFFFFFF & lparam[0]  # key code
            handler(key_code, rparam)
        finally:
            return CallNextHookEx(handle[0], code, rparam, lparam)

    callback_pointer = CFUNCTYPE(c_int, c_int, wintypes.HINSTANCE, POINTER(c_void_p))(low_level_callback)
    handle[0] = SetWindowsHookExA(WH_KEYBOARD_LL, callback_pointer, GetModuleHandleA(None), 0)
    atexit.register(UnhookWindowsHookEx, handle[0])

    # Message pumper
    message = wintypes.MSG()
    while True:
        msg = GetMessageW(byref(message), 0, 0, 0)
        if msg == -1:
            UnhookWindowsHookEx(handle[0])
            sys.exit(0)

        elif msg == 0:  # GetMessage return 0 only if WM_QUIT
            sys.exit(0)
        else:
            TranslateMessage(byref(message))
            DispatchMessageW(byref(message))
    try:
        sys.stdin.read()
        pass
    finally:
        # whe.close()
        UnhookWindowsHookEx(handle[0])
