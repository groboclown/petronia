"""Setup Petronia event handlers."""

from typing import Sequence, Callable
from petronia_common.util import StdRet, RET_OK_NONE
from petronia_ext_lib.runner import EventRegistryContext
from ..libs.setup import X11Access
from .. import configuration


class PetroniaEventHandlers:
    """API for working with the event handlers post setup."""

    def connect_to_x11(self, x11: X11Access) -> StdRet[None]:
        return RET_OK_NONE

    def post_start_handlers(self) -> Sequence[Callable[[], StdRet[None]]]:
        return []


def setup_petronia_events(
        context: EventRegistryContext,
        config_store: configuration.ConfigurationStore,
) -> StdRet[PetroniaEventHandlers]:
    return StdRet.pass_ok(PetroniaEventHandlers())
