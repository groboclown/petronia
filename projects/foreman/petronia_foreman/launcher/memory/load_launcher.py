"""
Finds options specific to the in-memory launcher.
"""

from typing import List, Sequence, Dict, Callable, Any
import os
import sys
import types
import threading
from petronia_common.util import StdRet
from petronia_common.util import i18n as _
from petronia_common.event_stream import BinaryReader, BinaryWriter
from .importer import load_module_from_path
from ...constants import TRANSLATION_CATALOG
from ...configuration import RuntimeConfig

ENTRYPOINT_OPTION = 'entrypoint'
DEFAULT_ENTRYPOINT = 'start_extension'
PYTHON_PATH_OPTION = 'extra-path'


def import_module(
        extension_name: str,
        extension_version: Sequence[int],
        locations: Sequence[str],
        options: RuntimeConfig,
) -> StdRet[types.ModuleType]:
    """Load the module defined in the options."""
    res_module_name = get_module_name(extension_name, extension_version, options)
    if res_module_name.has_error:
        return res_module_name.forward()

    path = get_python_path(locations, options)
    return load_module_from_path(res_module_name.result, path)


def connect_launcher(  # pylint:disable=too-many-arguments
        entrypoint_name: str, module: types.ModuleType,
        error_callback: Callable[[str, str, BaseException], None],
        completed_callback: Callable[[str, str], None],
        arguments: Sequence[str],
        reader: BinaryReader,
        writer: BinaryWriter,
        config: Dict[str, Any],
) -> StdRet[threading.Thread]:
    """Call the module's entrypoint function with the reader, writer, config, and arguments.
    This is done in another thread."""
    if not hasattr(module, entrypoint_name):
        return StdRet.pass_errmsg(
            TRANSLATION_CATALOG,
            _('No such entrypoint {entrypoint} in module {module}'),
            entrypoint=entrypoint_name,
            module=module.__name__,
        )
    entrypoint = getattr(module, entrypoint_name)
    if not callable(entrypoint):
        return StdRet.pass_errmsg(
            TRANSLATION_CATALOG,
            _('Entrypoint {entrypoint} in module {module} is not a function'),
            entrypoint=entrypoint_name,
            module=module.__name__,
        )

    def runner() -> None:
        try:
            entrypoint(reader, writer, config, arguments)
        except BaseException as err:  # pylint:disable=broad-except
            error_callback(module.__name__, entrypoint_name, err)
        else:
            completed_callback(module.__name__, entrypoint_name)

    ret = threading.Thread(target=runner, daemon=True, name=_next_thread_id())
    ret.start()
    return StdRet.pass_ok(ret)


def get_module_name(
        extension_name: str,
        _extension_version: Sequence[int],
        _options: RuntimeConfig,
) -> StdRet[str]:
    """Get the Python module name.  See the __init__ file for the standard."""
    return StdRet.pass_ok(extension_name)


def get_entrypoint_name(options: RuntimeConfig) -> str:
    """Get the entrypoint function name within the module.
    The entrypoint function must take a BinaryReader, BinaryWriter
    as arguments, and return None."""
    return options.options.get(ENTRYPOINT_OPTION, DEFAULT_ENTRYPOINT)


def get_python_path(locations: Sequence[str], options: RuntimeConfig) -> List[str]:
    """Get the path for the module's required libraries."""
    current_path = list(sys.path)
    for location in locations:
        if location not in current_path:
            current_path.append(location)
    res_extra_path = options.get_option(PYTHON_PATH_OPTION)
    if res_extra_path.ok:
        for path in res_extra_path.result.split(os.pathsep):
            if path not in current_path:
                current_path.append(path)
    return current_path


THREAD_INDEX = [0]


def _next_thread_id() -> str:
    THREAD_INDEX[0] += 1
    return 'memory-launcher-' + str(THREAD_INDEX[0])
