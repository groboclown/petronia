"""
Standard Windows functions required for the system.

The required APIs are:
    * running processes
        *
    * GUI windows
        * mapping a window to a process ID
"""

import sys
import importlib

# Top-level global def
from .funcs_any_win import SHELL__CANCEL_CALLBACK_CHAIN


def __load_functions(modules):
    import platform
    import struct

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

    ret = {}
    for name in modules:
        if isinstance(name, str):
            try:
                mod = importlib.import_module(name, __name__)
            except:
                print("Problem loading module " + name)
                raise
        else:
            mod = name
        mod.load_functions(environ, ret)
    return ret


# Defines the list of modules that contains platform specific functions.
# They are loaded in a specific order to overwrite previous, less-specific
# versions of the functions.
__FUNCTIONS = __load_functions([
    "petronia.arch.windows.funcs_x86_win",
    "petronia.arch.windows.funcs_x64_win",

    # any_win must ALWAYS be after the bit ones, because of dependencies.
    "petronia.arch.windows.funcs_any_win",

    # OS-specific come after the architecture ones
    "petronia.arch.windows.funcs_winXP",
    "petronia.arch.windows.funcs_winVista",
    "petronia.arch.windows.funcs_win7",
    "petronia.arch.windows.funcs_win8",
    "petronia.arch.windows.funcs_win10",

])

# Special code that loads those final, platform-specific functions into
# the current module namespace.
__current_module = importlib.import_module(__name__)
for __k, __v in __FUNCTIONS.items():
    setattr(__current_module, __k, __v)
