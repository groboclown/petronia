"""
Imports modules from paths.

This uses simple Python importing.
"""

from typing import List
import os
import sys
import types
import importlib
from petronia_common.util import StdRet
from petronia_common.util import i18n as _
from .defs import EntryPointFunctionType, TRANSLATION_CATALOG


def get_entrypoint_function(
        module_name: str,
        entrypoint_name: str,
        python_path: List[str],
) -> StdRet[EntryPointFunctionType]:
    """Load the module and find the entrypoint function."""
    module_res = load_module_from_path(module_name, python_path)
    if module_res.has_error:
        return module_res.forward()
    module = module_res.result
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
    return StdRet.pass_ok(entrypoint)


def load_module_from_path(fullname: str, path: List[str]) -> StdRet[types.ModuleType]:
    """Load the module, searching the given path."""
    for path_item in path:
        add_item_to_path(path_item)

    try:
        ret = importlib.import_module(fullname)
        return StdRet.pass_ok(ret)
    except Exception as err:  # pylint:disable=broad-except
        return StdRet.pass_exception(
            _('extension-runner could not load Python module {name} from path {path}'),
            err,
            name=fullname,
            path=repr(path),
        )


def add_item_to_path(item: str) -> None:
    """Add a local path"""
    abs_path = os.path.abspath(item)
    if os.path.exists(abs_path) and abs_path not in sys.path:
        sys.path.append(item)
