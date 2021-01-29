"""Process for loading an extension."""

from typing import Iterable
from petronia_common.extension.runner import EventRegistryContext
from petronia_common.util import StdRet, RET_OK_NONE
from .outside_handler import LoadExtensionHandler
from ..defs import ExtensionInfo
from ..shared_state import ExtLoaderSharedState


def register_load_extension_handler(
        shared_state: ExtLoaderSharedState,
        registry: EventRegistryContext,
) -> StdRet[None]:
    """Create the event target for loading extension requests."""
    registry.add_target(LoadExtensionHandler(registry))
    return RET_OK_NONE


def request_bootup(
        shared_state: ExtLoaderSharedState,
        registry: EventRegistryContext,
        boot_time_extensions: Iterable[ExtensionInfo],
        installed_extensions: Iterable[ExtensionInfo],
) -> StdRet[None]:
    """Start the process to load all the boot-time extensions.
    When the last one has finished loading, a startup event is sent."""
    return shared_state.add_pending_extensions(
        boot_time_extensions, installed_extensions,
        registry,
    )
