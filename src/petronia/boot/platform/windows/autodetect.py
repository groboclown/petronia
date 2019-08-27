
# Ignore types, because if this is run on Linux, it will cause problems.
# types: ignore

"""
Auto-detect the right extension to provide the Platform API.
"""

import sys
from ....aid.simp import PetroniaPlatformNotSupported


def discover_platform_ext() -> str:
    # Set up environment settings to make inspection of the current
    # platform easy for function modules to check.
    import platform

    if not hasattr(sys, 'getwindowsversion'):
        raise PetroniaPlatformNotSupported(
            '{0} {1}'.format(sys.platform, platform.architecture()[0])
        )

    try:
        winver = sys.getwindowsversion().major
        import ctypes.wintypes
        from ctypes import byref
        from ctypes import windll
        from ctypes import WinDLL
    except:
        raise PetroniaPlatformNotSupported(
            '{0} {1}'.format(sys.platform, platform.architecture()[0])
        )

    if winver == 10:
        return 'default.platform.windows'

    raise PetroniaPlatformNotSupported(
        'Windows v{0} {1}'.format(winver, platform.architecture()[0])
    )
