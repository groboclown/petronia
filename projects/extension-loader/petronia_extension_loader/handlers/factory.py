"""Process for loading an extension."""

from typing import Iterable
from petronia_common.util import StdRet, RET_OK_NONE
from .outside_handler import LoadExtensionHandler
from ..context import EventHandlerContext
from ..defs import ExtensionInfo


def register_load_extension_handler(context: EventHandlerContext) -> StdRet[None]:
    """Create the event target for loading extension requests."""
    context.add_target(LoadExtensionHandler(context))
    return RET_OK_NONE


def request_bootup(
        context: EventHandlerContext,
        boot_time_extensions: Iterable[ExtensionInfo],
        installed_extensions: Iterable[ExtensionInfo],
) -> StdRet[None]:
    """Start the process to load all the boot-time extensions.
    When the last one has finished loading, a startup event is sent."""
    return context.add_pending_extensions(boot_time_extensions, installed_extensions)
