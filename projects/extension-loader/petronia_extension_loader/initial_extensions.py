"""
Load the initial extensions.
"""

from typing import Sequence, Dict, List

from petronia_common.extension.runner import EventRegistryContext
from petronia_common.util import StdRet, UserMessage, join_errors
from petronia_common.util import i18n as _
from .defs import ExtensionInfo
from .setup import get_boot_extensions, get_extension_dirs
from .finder import (
    find_installed_extensions,
    parse_extension_name_version,
)
from .handlers.factory import request_bootup
from .search import find_best_extension
from .defs import TRANSLATION_CATALOG


def boot_extensions(context: EventRegistryContext) -> StdRet[None]:
    """Find the extensions to load, and request them to be loaded."""
    # Note: each time extensions are requested after boot, the installed extensions
    # are reloaded.  This allows for runtime adding extensions.
    installed_res = find_installed_extensions(get_extension_dirs())
    if installed_res.has_error:
        return installed_res.forward()

    # Find everything that we want to load first.
    # Load the boot extensions, then find dependencies and implementations.
    boot_extensions_res = find_boot_extensions(installed_res.result)
    if boot_extensions_res.has_error:
        return boot_extensions_res.forward()
    bootup_res = request_bootup(
        context, boot_extensions_res.result.values(),
        installed_res.result,
    )
    return bootup_res.forward()


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
