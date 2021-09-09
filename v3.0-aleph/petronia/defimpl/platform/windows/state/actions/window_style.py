
from typing import Dict, Mapping, Union, Optional
from ...arch.native_funcs import (
    HWND,
    WINDOWS_FUNCTIONS,
)
from ......aid.std import (
    log, WARN,
    # DEBUG, TRACE, VERBOSE, INFO,
)
from ...connect import (
    WindowsErrorMessage,
)


def set_window_style(
        hwnd: HWND,
        style: Mapping[str, Union[str, float, bool]]
) -> Optional[WindowsErrorMessage]:
    if not WINDOWS_FUNCTIONS.window.set_style:
        return None
    flags: Dict[str, bool] = {}
    for f, val in style.items():
        if val is True:
            flags[f] = True
    res = WINDOWS_FUNCTIONS.window.set_style(hwnd, flags)
    if isinstance(res, WindowsErrorMessage):
        log(
            WARN, set_window_style,
            "Could not set the style state of {0}: {1}",
            hwnd, res
        )
        return res
    return None
