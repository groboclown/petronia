"""Keyboard setup handler."""

from petronia_common.util import StdRet
from .handler import Hooks


def setup(hooks: Hooks) -> StdRet[None]:
    """Set up the keyboard."""

    # xcb_key_symbols_alloc
    # xkb init

    pass
