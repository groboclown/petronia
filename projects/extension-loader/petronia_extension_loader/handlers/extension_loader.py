"""Primary functionality to load an extension."""

from typing import Sequence, Optional
from petronia_common.extension.config import ExtensionVersion
from petronia_common.extension.runner import EventRegistryContext
from petronia_common.util import StdRet, RET_OK_NONE
from petronia_common.util import i18n as _
from ..defs import ExtensionInfo, TRANSLATION_CATALOG
from ..shared_state import ExtLoaderSharedState
from ..finder import find_installed_extensions
from ..setup import get_extension_dirs
from ..search import find_best_extension
from ..order import add_pending_extensions


def initiate_load_extension(
        shared_state: ExtLoaderSharedState,
        context: EventRegistryContext,
        source_id: Optional[str],
        extension_name: str,
        min_version: Optional[Sequence[int]],
        max_version: Optional[Sequence[int]],
        installed_extensions: Optional[Sequence[ExtensionInfo]],
) -> StdRet[Optional[Sequence[int]]]:
    """Begins the processing for loading an extension.  If the
    extension is already loaded, then the loaded version is
    returned, otherwise None is returned.  This does not send out
    error events."""

    as_loaded_ext = shared_state.load_list().get_loaded_info(extension_name)
    if as_loaded_ext is not None:
        return StdRet.pass_ok(as_loaded_ext.version)

    installed: Sequence[ExtensionInfo]
    if not installed_extensions:
        # Note: we report errors at startup time.  After that, they
        # are silently ignored.
        installed, _errors = find_installed_extensions(get_extension_dirs())
    else:
        installed = installed_extensions

    min_version_formal: Optional[ExtensionVersion]
    max_version_formal: Optional[ExtensionVersion]
    if min_version is None:
        min_version_formal = None
    else:
        min_version_formal = (min_version[0], min_version[1], min_version[2])
    if max_version is None:
        max_version_formal = None
    else:
        max_version_formal = (max_version[0], max_version[1], max_version[2])

    ext_info = find_best_extension(
        extension_name, min_version_formal, max_version_formal, installed,
    )
    if not ext_info:
        return StdRet.pass_errmsg(
            TRANSLATION_CATALOG,
            _('no extension installed matches {name} [>={min_version}, <{max_version}]'),
            name=extension_name,
            min_version=min_version,
            max_version=max_version,
        )
    res = load_extension(shared_state, context, source_id, ext_info, installed)
    if not res:
        return res.forward()
    return RET_OK_NONE


def load_extension(
        shared_state: ExtLoaderSharedState,
        context: EventRegistryContext,
        source_id: Optional[str],
        extension: ExtensionInfo,
        installed_extensions: Sequence[ExtensionInfo],
) -> StdRet[None]:
    """Attempt to load the extension and all of its unloaded dependencies."""
    if source_id:
        extension.add_request_source_id(source_id)
    res = add_pending_extensions(
        shared_state.load_list(),
        [extension],
        installed_extensions,
    )
    if res.has_error:
        return res.forward()
    shared_state.start_ready_extensions(context)
    return RET_OK_NONE
