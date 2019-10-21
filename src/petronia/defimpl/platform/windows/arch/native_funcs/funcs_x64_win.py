"""
64-bit windows functions
"""

from typing import Union
from .windows_common import (
    HWND,
    windll,
    WindowsErrorMessage,
)
from ..windows_constants import *
from .supported_functions import (
    Functions,
)


def load_functions(environ: Dict[str, str], func_map: Functions) -> None:
    if environ['64-bit']:
        func_map.window.set_style = window__set_style
        func_map.window.has_style = window__has_style
        func_map.window.get_style = window__get_style


def window__set_style(hwnd: HWND, style_update: Dict[str, bool]) -> Union[WindowsErrorMessage, Dict[str, bool]]:
    """
    Update a window's style.  "style_update" is a dictionary of style
    keys that map to either True or False, depending on how the style
    should be modified.  Style values not specified in the update
    will not be changed.

    :param hwnd:
    :param style_update:
    :return: the original style values (usable as input to this function).
    """
    assert isinstance(style_update, dict)

    SetWindowLongPtrW = windll.user32.SetWindowLongPtrW
    SetLastError = windll.kernel32.SetLastError

    original_style = window__get_style(hwnd)
    expected_style = dict(original_style)
    std_style_update = False
    std_bits = 0
    for k, mask in WS_STYLE_BIT_MAP.items():
        if k in style_update and original_style[k] != style_update[k]:
            std_style_update = True
            expected_style[k] = style_update[k]
            if style_update[k]:
                std_bits |= mask
        elif original_style[k]:
            std_bits |= mask
    if std_style_update:
        SetLastError(0)
        res = SetWindowLongPtrW(hwnd, GWL_STYLE, std_bits)
        if res == 0:
            return WindowsErrorMessage('user32.SetWindowLongPtrW(GWL_STYLE)')

    ex_style_update = False
    ex_bits = 0
    for k, mask in WS_EX_STYLE_BIT_MAP.items():
        if k in style_update and original_style[k] != style_update[k]:
            ex_style_update = True
            expected_style[k] = style_update[k]
            if style_update[k]:
                ex_bits |= mask
        elif original_style[k]:
            ex_bits |= mask
    if ex_style_update:
        SetLastError(0)
        # print("DEBUG Setting Window Ex Style to {0}".format(hex(ex_bits)))
        res = SetWindowLongPtrW(hwnd, GWL_EXSTYLE, ex_bits)
        if res == 0:
            return WindowsErrorMessage('user32.SetWindowLongPtrW(GWL_EXSTYLE)')

    # Sometimes, it only changed some of the values.
    # Double check.
    final_style = window__get_style(hwnd)
    if expected_style != final_style:
        # raise OSError("Did not fully set style to {0}; found {1}".format(
        #     expected_style, final_style))
        # print("DEBUG Did not fully set style to {0}; found {1}".format(
        #     expected_style, final_style))
        pass

    return original_style


def window__has_style(hwnd_handle: HWND, style: str) -> bool:
    full_style = window__get_style(hwnd_handle)
    return style in full_style


def window__get_style(hwnd_handle: HWND) -> Dict[str, bool]:
    ret = {}
    GetWindowLongPtrW = windll.user32.GetWindowLongPtrW
    bits = GetWindowLongPtrW(hwnd_handle, GWL_STYLE)
    for k, mask in WS_STYLE_BIT_MAP.items():
        ret[k] = (bits & mask == mask)
    bits = GetWindowLongPtrW(hwnd_handle, GWL_EXSTYLE)
    for k, mask in WS_EX_STYLE_BIT_MAP.items():
        ret[k] = (bits & mask == mask)
    return ret
