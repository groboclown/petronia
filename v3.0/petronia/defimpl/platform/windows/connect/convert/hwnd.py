
"""
HWND as an external reference.
"""

from typing import Optional
from ...arch.native_funcs.windows_common import HWND


def hwnd_to_id(hwnd: HWND) -> Optional[int]:
    return hwnd.value


def id_to_hwnd(identity: Optional[int]) -> HWND:
    hwnd = HWND(identity)
    return hwnd
