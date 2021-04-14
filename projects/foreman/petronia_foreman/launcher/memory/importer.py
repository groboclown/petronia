"""
Imports modules from paths.

This uses simple Python importing.
"""

from typing import List
import os
import sys
import types
import importlib
from petronia_common.util import StdRet, UserMessage, RET_OK_NONE
from petronia_common.util import i18n as _
from ...constants import TRANSLATION_CATALOG
from ...user_message import display_message, display_exception


def load_module_from_path(fullname: str, path: List[str]) -> StdRet[types.ModuleType]:
    """Load the module, searching the given path."""
    for path_item in path:
        res = add_item_to_path(path_item)
        if res.has_error:
            return res.forward()

    try:
        ret = importlib.import_module(fullname)
        return StdRet.pass_ok(ret)
    except Exception as err:  # pylint:disable=broad-except
        display_exception(f'[FOREMAN] module {fullname} failed on import', err)
        return StdRet.pass_exception(
            TRANSLATION_CATALOG,
            _('memory-importer for {name} path {path}'),
            err,
            name=fullname,
            path=repr(path),
        )


# To prevent duplicate messages, these are maintained.  Hopefully,
# this isn't too big a list, or our memory will be overwhelmed.
_REPORTED_NOT_EXISTING_PATHS: List[str] = []


def add_item_to_path(item: str) -> StdRet[None]:
    """Add a local path"""
    abs_path = os.path.abspath(item)
    if not os.path.exists(abs_path):
        if abs_path not in _REPORTED_NOT_EXISTING_PATHS:
            _REPORTED_NOT_EXISTING_PATHS.append(abs_path)
            display_message(UserMessage(
                TRANSLATION_CATALOG,
                _('Requested to load a module with non-existent search path {value}'),
                value=abs_path,
            ))
    elif abs_path not in sys.path:
        sys.path.append(abs_path)
    return RET_OK_NONE
