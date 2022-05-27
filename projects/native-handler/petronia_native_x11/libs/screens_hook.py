"""Graphics context setup handler."""

from typing import Optional, Sequence
from petronia_common.util import StdRet, RET_OK_FALSE
from .api import EventCallback
from .hook_manager import Hooks


class ScreenApi:
    """The API for accessing the monitors and virtual screen."""

    def get_event_handler(self) -> EventCallback:
        return ScreenEventCallback()


class ScreenEventCallback(EventCallback):
    def event_map(self) -> Optional[Sequence[int]]:
        return None

    def handle(self) -> StdRet[bool]:
        return RET_OK_FALSE


def setup_screens(hooks: Hooks) -> StdRet[ScreenApi]:
    """Set up the graphics context."""

    # scan the screens

    # add event hooks for when the screen size changes.

    return StdRet.pass_ok(ScreenApi())
