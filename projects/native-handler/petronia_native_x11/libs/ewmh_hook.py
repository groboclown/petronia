"""Extended Window Manager Hints setup handler."""

from typing import Sequence, Optional
from petronia_common.util import StdRet, RET_OK_FALSE
from .api import EventCallback
from .hook_manager import Hooks


class EwmhApi:
    """Api for interacting with extended window manager hints."""
    __slots__ = ()

    def get_event_handler(self) -> EventCallback:
        return EwmhCallback()


class EwmhCallback(EventCallback):
    def event_map(self) -> Optional[Sequence[int]]:
        return None

    def handle(self) -> StdRet[bool]:
        return RET_OK_FALSE


def setup_ewmh(hooks: Hooks) -> StdRet[EwmhApi]:
    """Set up ewmh."""

    # ewmh init

    return StdRet.pass_ok(EwmhApi())
