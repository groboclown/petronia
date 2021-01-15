"""Always running listener."""

from petronia_common.util import StdRet, RET_OK_NONE
from petronia_extension_runner.defs import EventHandlerContext
from .requests import InternalLoadExtensionRequestHandler


def register_run_extension_handler(context: EventHandlerContext) -> StdRet[None]:
    """Create the event target for loading extension requests."""
    context.add_target(InternalLoadExtensionRequestHandler(context))
    return RET_OK_NONE
