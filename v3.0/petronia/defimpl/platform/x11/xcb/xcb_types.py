
from typing import Optional
import ctypes
from .xcb_h import *
from .xproto_h import *

try:
    xcb_lib = ctypes.cdll.LoadLibrary('libxcb.so.1')
except OSError:
    xcb_lib = None


xcb_setup_p = ctypes.POINTER(xcb_setup_t)


# Public Types
class XcbConnection:
    __slots__ = ('_conn', '_setup_ptr')
    _conn: Optional[xcb_connection_t]
    _setup: Optional[xcb_setup_t]

    def __init__(self, conn: xcb_connection_t, setup_ptr: xcb_setup_p) -> None:
        self._conn = conn
        self._setup_ptr = setup_ptr

    def is_connected(self) -> bool:
        return self._conn is None

    def was_disconnected(self) -> None:
        self._conn = None
        self._setup_ptr = None

    @property
    def ptr(self) -> Optional[xcb_connection_t]:
        return self._conn

    @property
    def setup(self) -> Optional[xcb_setup_t]:
        if not self._setup:
            return None
        return self._setup.contents

    @property
    def setup_ptr(self) -> xcb_setup_p:
        return self._setup_ptr
