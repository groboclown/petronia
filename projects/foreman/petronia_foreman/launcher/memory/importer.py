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
from ...user_message import display_message


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
        return StdRet.pass_exception(
            _('memory-importer for {name} path {path}'),
            err,
            name=fullname,
            path=repr(path),
        )


def add_item_to_path(item: str) -> StdRet[None]:
    """Add a local path"""
    abs_path = os.path.abspath(item)
    if not os.path.exists(abs_path):
        # return StdRet.pass_errmsg(
        #     TRANSLATION_CATALOG,
        #     _('Requested to load a module with non-existent search path {value}'),
        #     value=abs_path,
        # )
        display_message(UserMessage(
            TRANSLATION_CATALOG,
            _('Requested to load a module with non-existent search path {value}'),
            value=abs_path,
        ))
    if item not in sys.path:
        sys.path.append(item)
    return RET_OK_NONE
