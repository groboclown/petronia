"""Global data store.  Data is assembled based on steps."""

from typing import Optional
import threading
from petronia_common.util import T
from petronia_ext_lib.runner import LookupEventRegistryContext
from .common_data.wm_data import WindowManagerData
from .configuration import ConfigurationStore
from .event_handler import EventHandlerLoop
from .libs import (
    libxcb, libcairo, libc, libxcb_icccm,
    libxcb_util, libxcb_types,
    libxcb_consts,
)


PROPERTY_MODE__REPLACE = libxcb_consts.XCB_PROP_MODE_REPLACE
PROPERTY_MODE__PREPEND = libxcb_consts.XCB_PROP_MODE_PREPEND
PROPERTY_MODE__APPEND = libxcb_consts.XCB_PROP_MODE_APPEND
PropertyModeEnum = (PROPERTY_MODE__REPLACE, PROPERTY_MODE__PREPEND, PROPERTY_MODE__APPEND)


class RunningData:
    """Fully running system's data."""
    __slots__ = (
        '__wm', '__loop',
    )

    def __init__(
            self,
            wm_data: WindowManagerData,
            event_loop: EventHandlerLoop,
    ) -> None:
        self.__wm = wm_data
        self.__loop = event_loop

    @property
    def window_manager_data(self) -> WindowManagerData:
        """The previous set of data."""
        return self.__wm

    @property
    def event_loop(self) -> EventHandlerLoop:
        """The event loop."""
        return self.__loop

    @property
    def context(self) -> LookupEventRegistryContext:
        return self.__wm.libs.context

    @property
    def config(self) -> ConfigurationStore:
        return self.__wm.libs.config

    @property
    def xcb(self) -> libxcb.LibXcb:
        """libxcb library"""
        return self.__wm.libs.xcb

    @property
    def cairo(self) -> libcairo.LibCairo:
        return self.__wm.libs.cairo

    @property
    def clib(self) -> libc.LibC:
        return self.__wm.libs.clib

    def has_xcb_util(self) -> bool:
        """libxcb-util library"""
        return self.__wm.libs.has_xcb_util()

    @property
    def xcb_util(self) -> libxcb_util.LibXcbUtil:
        """libxcb-util library"""
        return self.__wm.libs.xcb_util

    def has_xcb_icccm(self) -> bool:
        return self.__wm.libs.has_xcb_icccm()

    @property
    def xcb_icccm(self) -> libxcb_icccm.LibXcbIcccm:
        return self.__wm.libs.xcb_icccm

    def freeable(
            self,
            value,  # types: ctypes.pointer[T]
            lock: Optional[threading.Lock] = None,
    ) -> libc.Pointer[T]:
        """Make the value free-able"""
        return self.__wm.libs.clib.freeable(value, lock)

    @property
    def connection(self) -> libxcb_types.XcbConnectionP:
        return self.__wm.connection
