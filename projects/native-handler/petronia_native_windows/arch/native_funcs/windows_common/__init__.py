
"""
Common Windows imports.
"""

# Many places use Windows naming convention for things, not Python.
# pylint:disable=invalid-name

from typing import Callable
import ctypes
from ctypes import (
    c_int, c_ulong, c_int64, c_long, c_void_p, POINTER,
    byref, create_unicode_buffer, Structure, wintypes, CFUNCTYPE,
    # _SimpleCData,
    GetLastError,
)
from ctypes import sizeof as c_sizeof
from .win_error import WindowsReturnError
# import platform

# These are not modules...

windll = ctypes.windll
WinDLL = ctypes.WinDLL
WINFUNCTYPE = ctypes.WINFUNCTYPE
DWORD = wintypes.DWORD
WORD = wintypes.WORD
LONG = wintypes.LONG
UINT = wintypes.UINT
BYTE = wintypes.BYTE
SHORT = wintypes.SHORT
BOOL = wintypes.BOOL
WCHAR = wintypes.WCHAR
CHAR = wintypes.CHAR
HANDLE = wintypes.HANDLE
WINTYPE_SIZE = wintypes.SIZE

HWND = wintypes.HWND
LPARAM = wintypes.LPARAM
WPARAM = wintypes.WPARAM
HMODULE = wintypes.HMODULE
LPCWSTR = wintypes.LPCWSTR
HINSTANCE = wintypes.HINSTANCE
MSG = wintypes.MSG
HMENU = wintypes.HMENU
LPVOID = wintypes.LPVOID
COLORREF = wintypes.COLORREF

HFONT = wintypes.HFONT
HHOOK = wintypes.HHOOK
HMONITOR = wintypes.HMONITOR

HDC = HANDLE  # windll.gdi32.HDC

POINT = wintypes.POINT
RECT = wintypes.RECT
LPRECT = wintypes.LPRECT


class GUITHREADINFO(Structure):
    """The GUITHREADINFO structure.
    See https://docs.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-guithreadinfo"""
    _fields_ = (
        ("cbSize", DWORD),
        ("flags", DWORD),
        ("hwndActive", HWND),
        ("hwndFocus", HWND),
        ("hwndCapture", HWND),
        ("hwndMenuOwner", HWND),
        ("hwndMoveSize", HWND),
        ("hwndCaret", HWND),
        ("rcCaret", RECT),
    )

# Bit-size specific, but used in many different places.
# LRESULT: Type[Union[c_int64, c_long]] =
#       c_int64 if platform.architecture()[0] == "64bit" else c_long
# However, Python does a good job of handling this if we just use "int".
LRESULT = LPARAM

RGB: Callable[[int, int, int], int] = wintypes.RGB

# Return False to not propagate message.
MessageCallback = Callable[[HWND, int, WPARAM, LPARAM], bool]

NativeMessageCallback = Callable[[HWND, int, WPARAM, LPARAM], int]


class ANIMATIONINFO(Structure):
    """The ANIMATIONINFO structure.
    See https://msdn.microsoft.com/en-us/library/windows/desktop/ms644967(v=vs.85).aspx"""
    _fields_ = (
        ("cbSize", UINT),
        ("iMinAnimate", c_int),
        ("flags", DWORD),
        ("time", DWORD),
        ("dwExtraInfo", c_void_p),
    )
