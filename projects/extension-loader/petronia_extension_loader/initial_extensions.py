"""
Load the initial extensions.
"""

from typing import Sequence, Dict, List

from petronia_ext_lib.runner import EventRegistryContext
from petronia_common.util import StdRet, UserMessage, join_errors, RET_OK_NONE
from petronia_common.util import i18n as _
from .defs import ExtensionInfo
from .setup import get_boot_extensions, get_extension_dirs
from .finder import (
    find_installed_extensions,
    parse_extension_name_version,
)
from .order import add_pending_extensions
from .search import find_best_extension
from .defs import TRANSLATION_CATALOG
from .handlers.boot_extension_handler import add_boot_time_extensions
from .shared_state import ExtLoaderSharedState
from .messages import display_messages


def boot_extensions(
        shared_state: ExtLoaderSharedState,
        context: EventRegistryContext,
        warn_on_definition_errors: bool = True,
) -> StdRet[None]:
    """Find the extensions to load, and request them to be loaded."""
    # Note: each time extensions are requested after boot, the installed extensions
    # are reloaded.  This allows for runtime adding extensions.

    installed, errors = find_installed_extensions(get_extension_dirs())
    if warn_on_definition_errors and errors:
        for name, message in errors.items():
            display_messages(name, *message)

    # Find everything that we want to load first.
    # Load the boot extensions, then find dependencies and implementations.
    boot_extensions_res = find_boot_extensions(installed)
    if boot_extensions_res.has_error:
        return boot_extensions_res.forward()
    add_boot_time_extensions(boot_extensions_res.result.values())
    pending_res = add_pending_extensions(
        shared_state.load_list(),
        boot_extensions_res.result.values(),
        installed,
    )
    if pending_res.has_error:
        return pending_res.forward()
    start_res = shared_state.start_ready_extensions(context)
    if start_res.has_error:
        return start_res.forward()
    return RET_OK_NONE


def find_boot_extensions(installed: Sequence[ExtensionInfo]) -> StdRet[Dict[str, ExtensionInfo]]:
    """Find the boot extensions mapped to the list of installed extensions."""
    errors: List[UserMessage] = []
    ret: Dict[str, ExtensionInfo] = {}
    for name_ver in get_boot_extensions():
        name, major, minor, patch = parse_extension_name_version(name_ver)
        if name in ret:
            continue
        best = find_best_extension(
            name, (major or 0, minor or 0, patch or 0), None, installed,
        )
        if not best:
            errors.append(UserMessage(
                TRANSLATION_CATALOG,
                _('Extension listed in boot list, but is not installed: {req}'),
                req=name_ver,
            ))
        else:
            ret[name] = best
    if errors:
        return StdRet.pass_error(join_errors(*errors))
    return StdRet.pass_ok(ret)
