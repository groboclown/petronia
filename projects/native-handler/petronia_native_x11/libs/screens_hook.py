"""Graphics context setup handler."""

from typing import Optional, Sequence
from petronia_common.util import StdRet, RET_OK_NONE, RET_OK_FALSE
from .api import EventCallback, XcbApi
from .hook_manager import Hooks


class ScreenApi:
    """The API for accessing the monitors and virtual screen."""

    def get_event_handler(self) -> EventCallback:
        return ScreenEventCallback()

    def on_init_2(self, xcb: XcbApi) -> StdRet[None]:
        return RET_OK_NONE


class ScreenEventCallback(EventCallback):
    def event_map(self) -> Optional[Sequence[int]]:
        return None

    def handle(self) -> StdRet[bool]:
        return RET_OK_FALSE


def setup_screens(hooks: Hooks) -> StdRet[ScreenApi]:
    """Set up the graphics context."""
    ret = ScreenApi()
    hooks.add_pre_event_initializer(ret.on_init_2)

    # add event hooks for when the screen size changes.
    hooks.add_event_callback(ret.get_event_handler())
    return StdRet.pass_ok(ret)
