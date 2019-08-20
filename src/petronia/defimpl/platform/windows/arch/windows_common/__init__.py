
"""
Common Windows imports.
"""

import sys
if sys.platform.startswith('win'):
    from typing import Type, Any
    import ctypes
    from ctypes import (
        c_int, byref, create_unicode_buffer, Structure, wintypes, CFUNCTYPE,
        _SimpleCData
    )
    from ctypes import sizeof as c_sizeof

    # These are not modules...
    windll = ctypes.windll
    WinDLL = ctypes.WinDLL
    WinError = ctypes.WinError
    GetLastError = ctypes.GetLastError
    WINFUNCTYPE: Type = ctypes.WINFUNCTYPE
    DWORD: Type[_SimpleCData[int]] = wintypes.DWORD
    LONG: Type[_SimpleCData[int]] = wintypes.LONG
    UINT: Type[_SimpleCData[int]] = wintypes.UINT
    BYTE: Type[_SimpleCData[int]] = wintypes.BYTE
    BOOL: Type[_SimpleCData[bool]] = wintypes.BOOL

    HWND: Type[_SimpleCData[int]] = wintypes.HWND
    LPARAM: Type[_SimpleCData[Any]] = wintypes.LPARAM
    WPARAM: Type[_SimpleCData[Any]] = wintypes.WPARAM
    HMODULE: Type = wintypes.HMODULE
    LPCWSTR: Type = wintypes.LPCWSTR
    HINSTANCE: Type = wintypes.HINSTANCE
    MSG: Type = wintypes.MSG
    HMENU: Type = wintypes.HMENU
    LPVOID: Type = wintypes.LPVOID
    COLORREF: Type = wintypes.COLORREF

    POINT: Type[_SimpleCData] = wintypes.POINT
    RECT: Type[_SimpleCData] = wintypes.RECT
