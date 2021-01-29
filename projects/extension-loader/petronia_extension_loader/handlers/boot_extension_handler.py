"""Handles requests and event sending for managing the boot-time extensions."""

from typing import Set, Tuple, Iterable

from petronia_common.extension.config import ExtensionVersion
from petronia_common.util import StdRet, RET_OK_NONE
from petronia_common.util import i18n as _
from ..events.impl.extension_loader import SystemStartedEvent
from ..defs import ExtensionInfo, TRANSLATION_CATALOG
from ..shared_state import ExtLoaderSharedState

_BOOT_TIME_EXTENSIONS: Set[Tuple[str, ExtensionVersion]] = set()
_REMAINING_BOOT_TIME_EXTENSIONS: Set[str] = set()
_STARTUP_COMPLETE_SENT = [False]


def add_boot_time_extensions(extensions: Iterable[ExtensionInfo]) -> StdRet[None]:
    """Add extensions to the list of booted extensions.  When all of
    these are loaded, the startup complete event is sent.

    If the booting requires dynamically adding these after dependent
    extensions finish loading, then make sure this is called before
    the on_extension_load_complete is called.
    """
    if _STARTUP_COMPLETE_SENT[0]:
        return StdRet.pass_errmsg(
            TRANSLATION_CATALOG,
            _('Cannot add more boot time extensions because startup complete event already sent.'),
        )
    for extension in extensions:
        _BOOT_TIME_EXTENSIONS.add((extension.name, extension.version))
        _REMAINING_BOOT_TIME_EXTENSIONS.add(extension.name)
    return RET_OK_NONE


def clear_boot_time_extensions() -> None:
    """Used for unit testing."""
    _BOOT_TIME_EXTENSIONS.clear()
    _REMAINING_BOOT_TIME_EXTENSIONS.clear()
    _STARTUP_COMPLETE_SENT[0] = False


def on_extension_load_complete(context: EventHandlerContext, extension_name: str) -> StdRet[None]:
    """If this extension is the last of the known boot-time extensions, then the
    setup complete event is sent."""
    if _STARTUP_COMPLETE_SENT[0]:
        return RET_OK_NONE
    try:
        _REMAINING_BOOT_TIME_EXTENSIONS.remove(extension_name)
    except KeyError:
        return RET_OK_NONE
    if _REMAINING_BOOT_TIME_EXTENSIONS:
        # There are still some pending boot-time extensions waiting to be loaded.
        return RET_OK_NONE
    res = context.writer.write_object_event(
        SystemStartedEvent.FULL_EVENT_NAME,
        SystemStartedEvent.UNIQUE_TARGET_FQN,
        SystemStartedEvent.UNIQUE_TARGET_FQN,
        SystemStartedEvent().export_data(),
    )
    _REMAINING_BOOT_TIME_EXTENSIONS.clear()
    _STARTUP_COMPLETE_SENT[0] = True
    return res
