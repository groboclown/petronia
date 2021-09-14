
"""
Top-level native windows functions and types.
"""


from typing import Sequence
import importlib
import sys

# Top-level global def
from .funcs_any_win import SHELL__CANCEL_CALLBACK_CHAIN
from .supported_functions import (
    Functions,
    PaintFunctions,
    ShellFunctions,
    MonitorFunctions,
    ProcessFunctions,

    PaintCallback,
    WindowsWindowState,
)
from .windows_common import (
    HWND, DWORD, c_int, RECT, LONG,
    UINT, WPARAM, LPARAM, LRESULT,
    HDC, HFONT, HHOOK, ANIMATIONINFO,
    MessageCallback, NativeMessageCallback,
)


def internal_load_functions(modules: Sequence[str]) -> Functions:
    """Load the functions from the list of modules."""
    import platform  # pylint:disable=import-outside-toplevel
    import struct  # pylint:disable=import-outside-toplevel

    # Ensure we're on Windows
    if 'windows' not in platform.system().lower():  # pragma no cover
        return Functions()  # pragma no cover

    # Set up environment settings to make inspection of the current
    # platform easy for function modules to check.
    void_ptr_bits = struct.calcsize('P') * 8
    winver = sys.getwindowsversion()
    environ = {
        '32-bit': void_ptr_bits == 32,
        '64-bit': void_ptr_bits == 64,

        # Release name is in Lib/platform.py
        'release': platform.release(),
        'version': platform.version(),
        'system': platform.system(),
        'version-major': winver.major,
        'version-minor': winver.minor,
        'version-build': winver.build,
        'version-platform': winver.platform,
        'version-service_pack': winver.service_pack,
    }

    ret = Functions()
    for name in modules:
        # This can cause all kinds of errors.  However, those errors should be picked
        # up in unit tests (it's all based on hard-coded strings, not user-configurable
        # stuff).  So error checking doesn't exist here.
        mod = importlib.import_module(name, __name__)
        getattr(mod, 'load_functions')(environ, ret)
    return ret


# Defines the list of modules that contains platform specific functions.
# They are loaded in a specific order to overwrite previous, less-specific
# versions of the functions.
WINDOWS_FUNCTIONS = internal_load_functions([
    __name__ + ".funcs_x86_win",
    __name__ + ".funcs_x64_win",

    # any_win must ALWAYS be after the bit ones, because of dependencies.
    __name__ + ".funcs_any_win",

    # OS-specific come after the architecture ones
    __name__ + ".funcs_win_xp",
    __name__ + ".funcs_win_vista",
    __name__ + ".funcs_win7",
    __name__ + ".funcs_win8",
    __name__ + ".funcs_win10",
])
