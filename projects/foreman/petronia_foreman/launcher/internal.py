"""Internal launcher, for extensions that must never be loaded from the non-boot process."""

from typing import Sequence, Optional
from configparser import ConfigParser
from petronia_common.util import StdRet, RET_OK_NONE, STRING_EMPTY_TUPLE
from . import RuntimeContext
from .abc import AbcLauncherCategory
from ..configuration import RuntimeConfig
from ..events import foreman


def create_internal_launcher() -> AbcLauncherCategory:
    """Create a command launcher category"""
    config = ConfigParser()
    config.add_section('internal')
    return InternalLauncherCategory(RuntimeConfig('internal', config))


class InternalLauncherCategory(AbcLauncherCategory):
    """Does nothing.  This is used for extensions loaded from extension yaml
    definition files marked as 'internal'."""
    __slots__ = ('_context',)

    def __init__(self, config: RuntimeConfig) -> None:
        AbcLauncherCategory.__init__(self, config)
        self._context: Optional[RuntimeContext] = None

    def is_valid(self) -> StdRet[None]:
        return RET_OK_NONE

    def initialize(self, context: RuntimeContext) -> StdRet[None]:
        self._context = context
        return RET_OK_NONE

    def start_extension(
            self, handler_id: str, start_event: foreman.LauncherStartExtensionRequestEvent,
    ) -> StdRet[None]:
        # Just pretend like we started the extension.
        return RET_OK_NONE

    def get_active_handler_ids(self) -> Sequence[str]:
        return STRING_EMPTY_TUPLE

    def stop_extension(self, handler_id: str) -> StdRet[None]:
        return RET_OK_NONE

    def stop(self) -> StdRet[None]:
        return RET_OK_NONE
