"""Keyboard setup handler."""

from typing import Sequence, Optional
from petronia_common.util import StdRet, RET_OK_FALSE
from .api import EventCallback
from .hook_manager import Hooks


class KeyboardAPI:
    """Interact with the keyboard stuff."""

    def get_event_handler(self) -> EventCallback:
        return EwmhCallback()


class EwmhCallback(EventCallback):
    def event_map(self) -> Optional[Sequence[int]]:
        return None

    def handle(self) -> StdRet[bool]:
        return RET_OK_FALSE


def setup_keyboard(hooks: Hooks) -> StdRet[KeyboardAPI]:
    """Set up the keyboard."""

    ret = KeyboardAPI()

    # xcb_key_symbols_alloc
    # xkb init

    hooks.add_event_callback(ret.get_event_handler())
    return StdRet.pass_ok(ret)
