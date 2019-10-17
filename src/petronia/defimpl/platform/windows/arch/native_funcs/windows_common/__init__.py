
"""
Common Windows imports.
"""

from typing import Type, Callable, Sequence, Optional, Union
import ctypes
from ctypes import (
    c_int, c_ulong, c_int64, c_long, c_void_p, POINTER,
    byref, create_unicode_buffer, Structure, wintypes, CFUNCTYPE,
    _SimpleCData,
    GetLastError,
)
import platform
from ctypes import sizeof as c_sizeof

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

# See https://docs.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-guithreadinfo
class GUITHREADINFO(Structure):
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
# LRESULT: Type[Union[c_int64, c_long]] = c_int64 if platform.architecture()[0] == "64bit" else c_long
# However, Python does a good job of handling this if we just use "int".
LRESULT = LPARAM

RGB: Callable[[int, int, int], int] = wintypes.RGB

# Return False to not propagate message.
MessageCallback = Callable[[HWND, int, WPARAM, LPARAM], bool]

NativeMessageCallback = Callable[[HWND, int, WPARAM, LPARAM], int]

# see https://msdn.microsoft.com/en-us/library/windows/desktop/ms644967(v=vs.85).aspx
class ANIMATIONINFO(Structure):
    _fields_ = (
        ("cbSize", UINT),
        ("iMinAnimate", c_int),
        ("flags", DWORD),
        ("time", DWORD),
        ("dwExtraInfo", c_void_p),
    )


class WindowsErrorMessage:
    __slots__ = (
        '__called',
        '__errno', '__errmsg',
    )

    def __init__(self, called_function: str):
        self.__called = called_function
        self.__errno = GetLastError()

        # Should use "FormatMessage", but can't find it.

    @property
    def errno(self) -> int:
        return self.__errno

    @property
    def called_function(self) -> str:
        return self.__called

    def __repr__(self) -> str:
        return 'WindowsErrorMessage(called={0}, errno={1})'.format(
            repr(self.__called),
            repr(self.__errno)
        )
