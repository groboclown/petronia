"""Event loop handler."""

from typing import List, Sequence, Optional
import threading
from petronia_common.util import StdRet, RET_OK_NONE, RET_OK_FALSE
from .xcb import xcb_native
from .api import XcbApi, EventCallback, PROPERTY_MODE__REPLACE
from .hook_manager import Hooks


class ManagedWindow:
    """A native window"""
    __slots__ = ('native_id', 'orig_x', 'orig_y')

    def __init__(self, native_id: xcb_native.XcbWindow, orig_x: int, orig_y: int) -> None:
        self.native_id = native_id
        self.orig_x = orig_x
        self.orig_y = orig_y


class WindowApi:
    """Connections into the X11 event loop."""
    __slots__ = (
        '__lock',
        '__managed_windows',
        '__api', '__screen_tree_cookie',
    )

    def __init__(self) -> None:
        self.__lock = threading.RLock()
        self.__managed_windows: List[ManagedWindow] = []
        self.__api: Optional[XcbApi] = None
        self.__screen_tree_cookie: Optional[xcb_native.XcbQueryTreeCookie] = None

    def on_init_1(self, xcb: XcbApi) -> StdRet[None]:
        """Initialization phase 1 - screen is grabbed."""
        with self.__lock:
            if self.__api is not None:
                # Already setup
                return RET_OK_NONE
            self.__api = xcb

            # Get the window tree while the server is grabbed.  This will be used during
            #   initial startup.
            self.__screen_tree_cookie = xcb.query_tree(xcb.screen_root)
        return RET_OK_NONE

    def on_init_2(self, xcb: XcbApi) -> StdRet[None]:
        """Initialization phase 2 - screen is ungrabbed, haven't captured events yet."""
        # TODO scan the queried tree.
        return RET_OK_NONE

    def on_shutdown(self, xcb: XcbApi, timeout: float) -> StdRet[None]:
        """On-shutdown hook"""
        with self.__lock:
            if self.__api is None:
                # Already shut down
                return RET_OK_NONE

            # TODO send shutdown to event loop.

            win_ids: List[xcb_native.XcbWindow] = []
            for window in self.__managed_windows:
                win_ids.append(window.native_id)
                self.__api.reparent_window(
                    window_id=window.native_id,
                    new_parent_id=self.__api.screen_root,
                    new_x=window.orig_x, new_y=window.orig_y,
                )

            self.__managed_windows.clear()

            self.__api = None

        return RET_OK_NONE

    def get_event_handler(self) -> EventCallback:
        return EwmhCallback()


class EwmhCallback(EventCallback):
    def event_map(self) -> Optional[Sequence[int]]:
        return None

    def handle(self) -> StdRet[bool]:
        return RET_OK_FALSE


def setup_windows(hooks: Hooks) -> StdRet[WindowApi]:
    """Set up the events."""
    ret = WindowApi()
    hooks.add_screen_initializer(ret.on_init_1)
    hooks.add_pre_event_initializer(ret.on_init_2)
    hooks.add_shutdown(ret.on_shutdown)

    # TODO add event hooks for window events.

    hooks.add_event_callback(ret.get_event_handler())
    return StdRet.pass_ok(ret)
