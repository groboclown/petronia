
"""
Top-level native windows functions and types.
"""


from typing import Sequence
import sys
import importlib

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
    HWND, DWORD, c_int, RECT,
    UINT, WPARAM, LPARAM, LRESULT,
    HDC, HFONT, HHOOK, ANIMATIONINFO,
    MessageCallback, NativeMessageCallback,
)


def _load_functions(modules: Sequence[str]) -> Functions:
    import platform  # pylint:disable=import-outside-toplevel
    import struct  # pylint:disable=import-outside-toplevel

    # Ensure we're on Windows
    assert 'windows' in platform.system().lower()

    # Set up environment settings to make inspection of the current
    # platform easy for function modules to check.
    void_ptr_bits = struct.calcsize('P') * 8
    winver = sys.getwindowsversion()
    environ = {
        '32-bit': void_ptr_bits == 32,
        '64-bit': void_ptr_bits == 64,
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
        if isinstance(name, str):
            try:
                mod = importlib.import_module(name, __name__)
            except:
                print("Problem loading module " + name)
                raise
        else:
            mod = name
        if hasattr(mod, 'load_functions'):
            mod.load_functions(environ, ret)  # type: ignore
    return ret


# Defines the list of modules that contains platform specific functions.
# They are loaded in a specific order to overwrite previous, less-specific
# versions of the functions.
WINDOWS_FUNCTIONS = _load_functions([
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
