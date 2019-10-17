
import sys

import ctypes
from ctypes import wintypes
from ctypes import CFUNCTYPE, POINTER, c_int, c_uint, c_void_p
from ctypes import byref
import atexit
import threading
from petronia.arch import funcs

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

__CALLBACK_POINTERS = []


def hook_keyboard(callback):
    handle = None

    def low_level_callback(code, rparam, lparam):
        try:
            key_code = 0xFFFFFFFF & lparam[0]  # key code
            callback(key_code, rparam & 0xFFFFFFFF)
        finally:
            return CallNextHookEx(handle, code, rparam, lparam)
    # The really big problem is the callback_pointer.
    # Once it goes out of scope, it is destroyed
    callback_pointer = CFUNCTYPE(c_int, c_int, wintypes.HINSTANCE, POINTER(c_void_p))(low_level_callback)
    __CALLBACK_POINTERS.append(callback_pointer)
    handle = SetWindowsHookExA(WH_KEYBOARD_LL, callback_pointer, GetModuleHandleA(None), 0)
    atexit.register(UnhookWindowsHookEx, handle)
    return handle


def run():
    def handler(key_code, event_code):
        print("{0} {1}".format(hex(key_code), hex(event_code)))

    handle = hook_keyboard(handler)

    def on_exit():
        pass

    funcs.shell__pump_messages(on_exit)


if __name__ == '__main__':

    pump_thread = threading.Thread(
        target=run,
        daemon=False
    )
    pump_thread.start()
