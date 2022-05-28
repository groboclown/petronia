"""extension setup handler."""

from typing import Sequence, Optional
from petronia_common.util import StdRet, RET_OK_FALSE
from .api import EventCallback
from .hook_manager import Hooks


class XExtensionApi:
    """API for working with X extensions."""

    def get_event_handler(self) -> EventCallback:
        return EwmhCallback()


class EwmhCallback(EventCallback):
    def event_map(self) -> Optional[Sequence[int]]:
        return None

    def handle(self) -> StdRet[bool]:
        return RET_OK_FALSE


def setup_x_ext(hooks: Hooks) -> StdRet[XExtensionApi]:
    """Set up the extensions."""
    ret = XExtensionApi()

    # check for each needed extension
    #  - xtest
    #  - shape
    #  - xfixes

    hooks.add_event_callback(ret.get_event_handler())
    return StdRet.pass_ok(ret)
