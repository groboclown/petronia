
"""
Auto-detect the right extension to provide the Platform API.
"""

from ....aid.std import PetroniaPlatformNotSupported


def discover_platform_ext() -> str:
    import sys
    import platform

    try:
        from ctypes import cdll
    except:
        raise PetroniaPlatformNotSupported(
            '{0} {1}'.format(sys.platform, platform.architecture()[0])
        )

    # Check wayland first, because it might be running the XWayland,
    # throwing off the X11 probe.
    try:
        cdll.LoadLibrary('libwayland.so')
        return 'default.platform.wayland'
    except OSError:
        pass

    try:
        xcb = cdll.LoadLibrary('libxcb.so')
        # Check to see if x is actually running.
        # The "proper" way is to open the display, but that means we'll mess
        # up the right approach to handling a window manager, which must be
        # the first client to connect.
        return 'default.platform.x11'
    except OSError:
        pass

    raise PetroniaPlatformNotSupported(
        '{0} {1}'.format(sys.platform, platform.architecture()[0])
    )
