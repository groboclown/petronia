"""Shared library xcb-cursor"""

import ctypes


class XcbCursorContext(ctypes.Structure):
    """xcb-cursor xcb_cursor_context_t opaque type"""
    _fields_ = []


XcbCursorContextP = ctypes.POINTER(XcbCursorContext)
XcbCursorContextPP = ctypes.POINTER(XcbCursorContextP)
