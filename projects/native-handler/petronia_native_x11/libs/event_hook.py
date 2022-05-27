"""Event loop handler."""

from typing import List, Optional
import threading
from petronia_common.util import StdRet, RET_OK_NONE
from .xcb import xcb_native
from .api import XcbApi, EventCallback
from .hook_manager import Hooks


ROOT_WINDOW_EVENT_MASK = (
    xcb_native.XCB_EVENT_MASK_SUBSTRUCTURE_REDIRECT__i
    | xcb_native.XCB_EVENT_MASK_SUBSTRUCTURE_NOTIFY__i
    | xcb_native.XCB_EVENT_MASK_ENTER_WINDOW__i
    | xcb_native.XCB_EVENT_MASK_LEAVE_WINDOW__i
    | xcb_native.XCB_EVENT_MASK_STRUCTURE_NOTIFY__i
    | xcb_native.XCB_EVENT_MASK_BUTTON_PRESS__i
    | xcb_native.XCB_EVENT_MASK_BUTTON_RELEASE__i
    | xcb_native.XCB_EVENT_MASK_FOCUS_CHANGE__i
    | xcb_native.XCB_EVENT_MASK_PROPERTY_CHANGE__i
)


class EventApi:
    """Connections into the X11 event loop."""
    __slots__ = (
        '__pending_events',
        '__lock',
        '__api',
        '__event_hooks',
    )

    def __init__(self) -> None:
        self.__pending_events: List[xcb_native.XcbGenericEventP] = []
        self.__lock = threading.RLock()
        self.__api: Optional[XcbApi] = None
        self.__event_hooks: List[EventCallback] = []

    def start_loop(self) -> StdRet[None]:
        """Start the X11 event handling."""

        # We're on the startup side.  First, grab any running windows,
        # and reclaim the window order, if it was set from a previous run.

        pass

    def is_running(self) -> bool:
        """Is the event loop still active?"""
        with self.__lock:
            # Right now, we check by seeing if it's disposed.
            return self.__api is not None

    def add_pending_event(self, event: xcb_native.XcbGenericEventP) -> None:
        """Add an event that was read elsewhere that will need to be handled in the loop.
        Each pending event, if not None, will need to be freed within the loop after being
        handled.
        """
        if event:
            with self.__lock:
                self.__pending_events.append(event)

    def add_event_hook(self, event_hook: EventCallback) -> None:
        """Add a new event hook."""
        with self.__lock:
            self.__event_hooks.append(event_hook)

    def on_server_init(self, xcb: XcbApi) -> StdRet[None]:
        with self.__lock:
            if self.__api is not None:
                # Already setup
                return RET_OK_NONE
            self.__api = xcb

            # Setup events to listen to on the root window.
            xcb.change_window_attributes(
                window_id=xcb.screen_root,
                value_mask=xcb_native.XCB_CW_EVENT_MASK,
                value_list=(ROOT_WINDOW_EVENT_MASK,),
            )

    def on_shutdown(self, xcb: XcbApi, _timeout: float) -> StdRet[None]:
        """On-shutdown hook"""
        with self.__lock:
            if self.__api is None:
                # Already shut down
                return RET_OK_NONE

            # TODO send shutdown to event loop.

            self.__api = None

        return RET_OK_NONE


def setup_events(hooks: Hooks) -> StdRet[EventApi]:
    """Set up the events."""
    ret = EventApi()
    hooks.add_shutdown(ret.on_shutdown)
    return StdRet.pass_ok(ret)
