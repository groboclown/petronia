
"""
Detect the current platform.

os_category: current OS platform.
"""

from typing import List, Sequence, Optional
import os
import sys
import platform
from petronia_common.util import StdRet, RET_OK_NONE
from petronia_common.util import i18n as _
from ..constants import TRANSLATION_CATALOG as CATALOG

# Explicit list of platforms that Petronia currently supports.
SUPPORTED_PLATFORMS = (
    'windows-10',
    'linux-x11',
    'linux-wayland',
)

APP_PATHS = ('petronia', '.petronia')

CATEGORY__UNDEFINED = -1
CATEGORY__WINDOWS = 0
CATEGORY__LINUX = 1
CATEGORY__OSX = 2

platform_name = 'unknown'  # pylint:disable=invalid-name
os_category: int = CATEGORY__UNDEFINED  # pylint:disable=invalid-name
configuration_paths: List[str] = []  # pylint:disable=invalid-name
data_paths: List[str] = []  # pylint:disable=invalid-name


def initial_setup(suggestion: Optional[str]) -> StdRet[None]:
    """Initial platform setup or discovery.  This will reset all configuration.
    """
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


def find_data_dir(name: str) -> Optional[str]:
    """Find the named directory from the data paths."""
    for path in data_paths:
        fqn = os.path.join(path, name)
        if os.path.isdir(fqn):
            return fqn
    return None


def find_data_file(name: str, *possible_sub_dirs: str) -> Optional[str]:
    """Find the named directory from the data paths."""
    for path in data_paths:
        for sub_dir in possible_sub_dirs:
            fqn = os.path.join(path, sub_dir, name)
            if os.path.isfile(fqn):
                return fqn
    return None


def load_windows10_settings() -> StdRet[None]:
    """Determine the settings for Windows."""
    global platform_name, os_category  # pylint:disable=invalid-name,global-statement
    platform_name = 'windows-10'
    os_category = CATEGORY__WINDOWS
    configuration_paths.clear()
    configuration_paths.extend(find_petronia_paths([
        os.environ.get('LOCALAPPDATA'),
        os.environ.get('APPDATA'),
        os.environ.get('USERPROFILE'),
        os.environ.get('HOMEPATH'),
        os.environ.get('ALLUSERSPROFILE'),
    ]))
    data_paths.clear()
    data_paths.extend([detect_install_dir()])
    return RET_OK_NONE


def load_linux_x11_settings() -> StdRet[None]:
    """Load the X11 settings."""
    global platform_name, os_category  # pylint:disable=invalid-name,global-statement
    platform_name = 'linux-x11'
    os_category = CATEGORY__LINUX
    configuration_paths.extend(find_linux_config_paths())
    data_paths.extend(find_linux_data_paths())
    return RET_OK_NONE


def load_linux_wayland_settings() -> StdRet[None]:
    """Load the wayland settings."""
    global platform_name, os_category  # pylint:disable=invalid-name,global-statement
    platform_name = 'linux-wayland'
    os_category = CATEGORY__LINUX
    configuration_paths.extend(find_linux_config_paths())
    data_paths.extend(find_linux_data_paths())
    return RET_OK_NONE


def detect_windows() -> StdRet[None]:
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

    try:  # pragma no cover
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


def detect_linux() -> StdRet[None]:
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


def find_linux_config_paths() -> Sequence[str]:
    """Load the linux configuration paths."""
    # Standards for Linux paths.
    # See https://cgit.freedesktop.org/xdg/xdg-specs/tree/basedir/basedir-spec.xml
    user_home = os.environ.get('HOME', os.path.curdir)
    return find_petronia_paths([
        os.environ.get('XDG_CONFIG_HOME', os.path.join(user_home, '.config')),
        user_home,
        *os.environ.get('XDG_CONFIG_DIRS', '/etc/xdg').split(':'),
    ])


def find_linux_data_paths() -> Sequence[str]:
    """Load the linux data paths"""
    # Standards for Linux paths.
    # See https://cgit.freedesktop.org/xdg/xdg-specs/tree/basedir/basedir-spec.xml
    user_home = os.environ.get('HOME', os.path.curdir)
    paths = find_petronia_paths([
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


def find_petronia_paths(paths: Sequence[Optional[str]]) -> List[str]:
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
