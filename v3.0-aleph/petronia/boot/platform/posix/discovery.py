
"""
Implements the required discovery function.
"""

from typing import List
from ....core.platform.preboot import (
    DiscoveryData,
    ExtensionPaths,
    ExtensionLoaderModel,
)
from .paths import (
    get_distribution_paths,
    get_user_paths,
)
from ..general import (
    TEMP_DIR_PATH,
    get_preboot_extension_sets,
)
from ...bootstrap.managed_queue import RootEventQueueModel
from .autodetect import discover_platform_ext

# From https://www.freedesktop.org/wiki/Specifications/basedir-spec/
# * There is a single base directory relative to which user-specific data
#   files should be written. This directory is defined by the environment
#   variable $XDG_DATA_HOME.
#   ...
#   $XDG_DATA_HOME defines the base directory relative to which user specific
#   data files should be stored. If $XDG_DATA_HOME is either not set or empty,
#   a default equal to $HOME/.local/share should be used.
#
# * There is a single base directory relative to which user-specific
#   configuration files should be written. This directory is defined by the
#   environment variable $XDG_CONFIG_HOME.
#   ...
#   $XDG_CONFIG_HOME defines the base directory relative to which user
#   specific configuration files should be stored. If $XDG_CONFIG_HOME is
#   either not set or empty, a default equal to $HOME/.config should be used.
#
# * There is a set of preference ordered base directories relative to which
#   data files should be searched. This set of directories is defined by the
#   environment variable $XDG_DATA_DIRS.
#   ...
#   $XDG_DATA_DIRS defines the preference-ordered set of base directories to
#   search for data files in addition to the $XDG_DATA_HOME base directory.
#   The directories in $XDG_DATA_DIRS should be seperated with a colon ':'.
#   If $XDG_DATA_DIRS is either not set or empty, a value equal to
#   /usr/local/share/:/usr/share/ should be used.
#
# * There is a set of preference ordered base directories relative to which
#   configuration files should be searched. This set of directories is defined
#   by the environment variable $XDG_CONFIG_DIRS.
#   ...
#   $XDG_CONFIG_DIRS defines the preference-ordered set of base directories to
#   search for configuration files in addition to the $XDG_CONFIG_HOME base
#   directory. The directories in $XDG_CONFIG_DIRS should be seperated with
#   a colon ':'.
#   If $XDG_CONFIG_DIRS is either not set or empty, a value equal to /etc/xdg
#   should be used.
#
# * There is a single base directory relative to which user-specific
#   non-essential (cached) data should be written. This directory is defined
#   by the environment variable $XDG_CACHE_HOME.
#
# * $XDG_CACHE_HOME defines the base directory relative to which user specific
#   non-essential data files should be stored. If $XDG_CACHE_HOME is either
#   not set or empty, a default equal to $HOME/.cache should be used.
#
# * The order of base directories denotes their importance; the first
#   directory listed is the most important. When the same information is
#   defined in multiple places the information defined relative to the more
#   important base directory takes precedent. The base directory defined by
#   $XDG_DATA_HOME is considered more important than any of the base
#   directories defined by $XDG_DATA_DIRS. The base directory defined by
#   $XDG_CONFIG_HOME is considered more important than any of the base
#   directories defined by $XDG_CONFIG_DIRS.


def discover_preboot_data() -> DiscoveryData:
    """
    DiscoveryFunction
    """

    # Find the installation directory.  These are ordered by priority.
    # Note that the standard way to set these in Linux is with compile-time
    # setting.

    distro_paths = get_distribution_paths()
    user_paths = get_user_paths()
    all_paths: List[str] = []
    all_paths.extend(distro_paths)
    all_paths.extend(user_paths)

    # For the moment, no extension paths are supported.
    extension_paths = ExtensionPaths()

    return DiscoveryData(
        extension_paths,
        get_preboot_extension_sets(),
        [
            ['default.configuration.file',],
            [discover_platform_ext()],
        ],
        TEMP_DIR_PATH,
        False,
        ExtensionLoaderModel('petronia.defimpl.extensions'),
        RootEventQueueModel(8),
        all_paths,
        '''
POSIX Specific Setup:

(TODO)
'''
    )
