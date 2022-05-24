"""Loads the library."""

from typing import Dict, List, Optional
from .impl import Xcb
from ..funcs import LibFunctions


_GLOBAL_XCB_CONNECTION: Optional[Xcb] = None


def load_functions(_env: Dict[str, str], func_map: LibFunctions) -> None:
    global _GLOBAL_XCB_CONNECTION
    if _GLOBAL_XCB_CONNECTION is None:
        _GLOBAL_XCB_CONNECTION = Xcb()
    func_map.ui.connect = _GLOBAL_XCB_CONNECTION.connect
