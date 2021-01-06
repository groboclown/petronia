"""
Finds options specific to the in-memory launcher.
"""
from typing import List, Callable
import os
import sys
import types
import threading
from petronia_common.util import StdRet
from petronia_common.util import i18n as _
from petronia_common.event_stream import BinaryReader, BinaryWriter
from .importer import load_module_from_path
from ...constants import TRANSLATION_CATALOG
from ...configuration import LauncherConfig

MODULE_NAME_OPTION = 'module'
ENTRYPOINT_OPTION = 'entrypoint'
PYTHON_PATH_OPTION = 'extra-path'


def import_module(options: LauncherConfig) -> StdRet[types.ModuleType]:
    """Load the module defined in the options."""
    res_module_name = get_module_name(options)
    if res_module_name.has_error:
        return res_module_name.forward()

    path = get_python_path(options)
    return load_module_from_path(res_module_name.result, path)


def connect_launcher(
        entrypoint_name: str, module: types.ModuleType,
        error_callback: Callable[[str, str, BaseException], None],
        completed_callback: Callable[[str, str], None],
        reader: BinaryReader,
        writer: BinaryWriter,
) -> StdRet[threading.Thread]:
    """Call the module's entrypoint function with the reader and writer.
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
            entrypoint(reader, writer)
        except BaseException as err:
            error_callback(module.__name__, entrypoint_name, err)
        else:
            completed_callback(module.__name__, entrypoint_name)

    ret = threading.Thread(target=runner, daemon=True)
    ret.start()
    return StdRet.pass_ok(ret)


def get_module_name(options: LauncherConfig) -> StdRet[str]:
    """Get the Python module name."""
    return options.get_option(MODULE_NAME_OPTION)


def get_entrypoint_name(options: LauncherConfig) -> StdRet[str]:
    """Get the entrypoint function name within the module.
    The entrypoint function must take a BinaryReader, BinaryWriter
    as arguments, and return None."""
    return options.get_option(ENTRYPOINT_OPTION)


def get_python_path(options: LauncherConfig) -> List[str]:
    """Get the path for the module's required libraries."""
    current_path = list(sys.path)
    res_extra_path = options.get_option(PYTHON_PATH_OPTION)
    if res_extra_path.ok:
        for path in res_extra_path.result.split(os.pathsep):
            if path not in current_path:
                current_path.append(path)
    return current_path
