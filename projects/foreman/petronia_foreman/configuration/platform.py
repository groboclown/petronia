
"""
Detect the current platform.
"""

from typing import List, Sequence, Optional
import os
import sys
import platform
from petronia_common.util import StdRet
from petronia_common.util import i18n as _
from ..constants import TRANSLATION_CATALOG as CATALOG

# Explicit list of platforms that Petronia currently supports.
SUPPORTED_PLATFORMS = (
    'windows-10',
    'linux-x11',
    'linux-wayland',
)

APP_PATHS = ('petronia', '.petronia')

CATEGORY__WINDOWS = 0
CATEGORY__LINUX = 1
CATEGORY__OSX = 2


class PlatformSettings:
    """
    Settings that describes the current platform.

    This also knows information related to the install layout.
    """

    __slots__ = ('name', 'category', 'config_paths', 'data_paths', 'native_launcher_name',)

    def __init__(  # pylint: disable=too-many-arguments
            self,
            name: str,
            category: int,
            config_paths: Sequence[str],
            data_paths: Sequence[str],
            native_launcher_name: str,
    ) -> None:
        self.name = name
        self.category = category
        self.config_paths = tuple(config_paths)
        self.data_paths = tuple(data_paths)
        self.native_launcher_name = native_launcher_name

    def find_data_dir(self, name: str) -> Optional[str]:
        """Find the data path."""
        for path in self.data_paths:
            fqn = os.path.join(path, name)
            if os.path.isdir(fqn):
                return fqn
        return None


def detect_platform(suggestion: Optional[str]) -> StdRet[PlatformSettings]:
    """Determine the current platform, and """
    system_name = (suggestion or platform.system() or 'Unknown').lower()
    if system_name == 'windows-10':
        return load_windows10_settings()
    if system_name == 'linux-x11':
        return load_linux_x11_settings()
    if system_name == 'linux-wayland':
        return load_linux_wayland_settings()
    if system_name == 'windows':
        return detect_windows()
    if system_name == 'linux':
        return detect_linux()
    return StdRet.pass_errmsg(
        CATALOG,
        _('Could not recognize your platform (found {system_name}).'),
        system_name=system_name,
    )


def load_windows10_settings() -> StdRet[PlatformSettings]:
    """Determine the settings for Windows."""
    return StdRet.pass_ok(PlatformSettings(
        'windows-10',
        CATEGORY__WINDOWS,
        get_petronia_paths([
            os.environ.get('LOCALAPPDATA'),
            os.environ.get('APPDATA'),
            os.environ.get('USERPROFILE'),
            os.environ.get('HOMEPATH'),
            os.environ.get('ALLUSERSPROFILE'),
        ]),
        [detect_install_dir()],
        'windows-10',
    ))


def load_linux_x11_settings() -> StdRet[PlatformSettings]:
    """Load the X11 settings."""
    return StdRet.pass_ok(PlatformSettings(
        'linux-x11',
        CATEGORY__LINUX,
        load_linux_config_paths(),
        load_linux_data_paths(),
        'x11',
    ))


def load_linux_wayland_settings() -> StdRet[PlatformSettings]:
    """Load the wayland settings."""
    return StdRet.pass_ok(PlatformSettings(
        'linux-wayland',
        CATEGORY__LINUX,
        load_linux_config_paths(),
        load_linux_data_paths(),
        'wayland',
    ))


def detect_windows() -> StdRet[PlatformSettings]:
    """Detect the Windows platform settings to use."""
    try:
        # Linux builds will fail on getwindowsversion not a member.
        winver = sys.getwindowsversion().major  # type: ignore  # pylint: disable=no-member
    except BaseException:  # pylint: disable=broad-except  # pragma no cover
        return StdRet.pass_errmsg(  # pragma no cover
            CATALOG,
            _(
                "You requested Windows, but the Windows Version could not be discovered."
            ),
        )

    try:
        # Linux builds will fail on this ctype detection...
        import ctypes.wintypes  # type: ignore  # pylint: disable=import-outside-toplevel,unused-import  # pragma no cover
        from ctypes import byref  # type: ignore  # pylint: disable=import-outside-toplevel,unused-import  # pragma no cover
        from ctypes import windll  # type: ignore  # pylint: disable=import-outside-toplevel,unused-import  # pragma no cover
        from ctypes import WinDLL  # type: ignore  # pylint: disable=import-outside-toplevel,unused-import  # pragma no cover
    except BaseException:  # pylint: disable=broad-except  # pragma no cover
        return StdRet.pass_errmsg(  # pragma no cover
            CATALOG,
            _(
                "Your system ({system} {version} {arch}) does not "
                "support the required Windows libraries."
            ),
            system=platform.system(),
            version=winver,
            arch=platform.architecture()[0],
        )

    if winver == 10:  # pragma no cover
        return load_windows10_settings()  # pragma no cover

    return StdRet.pass_errmsg(  # pragma no cover
        CATALOG,
        _(
            "Your system ({system} {version} {arch}) is not one of the "
            "supported Windows versions."
        ),
        system=platform.system(),
        version=winver,
        arch=platform.architecture()[0],
    )


def detect_linux() -> StdRet[PlatformSettings]:
    """Determine which video interaction method to use."""
    try:
        from ctypes import cdll  # pylint: disable=import-outside-toplevel  # pragma no cover
    except BaseException as err:  # pylint: disable=broad-except  # pragma no cover
        return StdRet.pass_errmsg(  # pragma no cover
            CATALOG,
            _(
                'Could not discover your platform; native library loading not'
                'supported with Python (problem: {err}).'
            ),
            err=repr(err),
        )

    # Check wayland first, because it might be running the XWayland,
    # throwing off the X11 probe.  However, there's the rare situation where
    # someone installed wayland but is using X11.  In that rare case, the user will
    # need to explicitly declare the system.

    try:
        cdll.LoadLibrary('libwayland.so')  # pragma no cover
        return load_linux_wayland_settings()  # pragma no cover
    except OSError:  # pragma no cover
        # Ignored, because it means wayland isn't supported.
        pass  # pragma no cover

    try:
        cdll.LoadLibrary('libxcb.so')  # pragma no cover
        # Check to see if x is actually running.
        # The "proper" way is to open the display, but that means we'll mess
        # up the right approach to handling a window manager, which must be
        # the first client to connect...
        # But that will require some testing.  Testing in that it might be
        # still a window manager if the client connects, disconnects, then
        # is first to connect when nothing else is connected.  Ugh.
        return load_linux_x11_settings()  # pragma no cover
    except OSError:  # pragma no cover
        pass  # pragma no cover

    return StdRet.pass_errmsg(  # pragma no cover
        CATALOG,
        _(
            "'Your platform is not supported, because neither libwayland.so"
            "nor libxcb.so are present.  Please install one to enable support."
        ),
    )


def load_linux_config_paths() -> Sequence[str]:
    """Load the linux configuration paths."""
    # Standards for Linux paths.
    # See https://cgit.freedesktop.org/xdg/xdg-specs/tree/basedir/basedir-spec.xml
    user_home = os.environ.get('HOME', os.path.curdir)
    return get_petronia_paths([
        os.environ.get('XDG_CONFIG_HOME', os.path.join(user_home, '.config')),
        user_home,
        *os.environ.get('XDG_CONFIG_DIRS', '/etc/xdg').split(':'),
    ])


def load_linux_data_paths() -> Sequence[str]:
    """Load the linux data paths"""
    # Standards for Linux paths.
    # See https://cgit.freedesktop.org/xdg/xdg-specs/tree/basedir/basedir-spec.xml
    user_home = os.environ.get('HOME', os.path.curdir)
    paths = get_petronia_paths([
        os.environ.get('XDG_DATA_HOME', os.path.join(user_home, '.local/share')),
        *os.environ.get('XDG_DATA_DIRS', '/usr/local/share/:/usr/share/').split(':'),
    ])
    paths.append(detect_install_dir())
    return paths


def detect_install_dir() -> str:
    """Attempt to find the directory where Petronia is installed."""
    # Note that Petronia may be running as an installed bundle.
    # See https://pyinstaller.readthedocs.io/en/stable/runtime-information.html
    # We take advantage of insight into how Petronia is deployed.  Note that this is
    # consistent between the bundle install and the file-based install.

    bundle_dir: str

    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        # we are running in a pyinstaller bundle
        bundle_dir = os.path.abspath(getattr(sys, '_MEIPASS', os.path.curdir))
    else:
        # we are running in a normal Python environment
        module_dir = os.path.dirname(os.path.abspath(__file__))
        # This module file is in the petronia_foreman/configuration directory.
        bundle_dir = os.path.dirname(os.path.dirname(module_dir))
    if not os.path.isdir(bundle_dir):
        return os.path.abspath(os.path.curdir)
    return bundle_dir


def get_petronia_paths(paths: Sequence[Optional[str]]) -> List[str]:
    """Get the list of paths for Petronia."""
    ret: List[str] = []

    # Use APP_PATHS first...
    for path in paths:
        if path is None:
            continue
        for app_path in APP_PATHS:
            fqn = os.path.abspath(os.path.join(path, app_path))
            if os.path.isdir(fqn):
                ret.append(fqn)

    # Then allow the roots.
    for path in paths:
        if path is None:
            continue
        fqn = os.path.abspath(path)
        if os.path.isdir(fqn):
            ret.append(fqn)

    return ret
