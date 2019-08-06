
"""
Implements the required discovery function.
"""

import tempfile
from .....core.platform.preboot import (
    DiscoveryData,
    ExtensionPaths,
)
from .paths import (
    get_distribution_paths,
    get_user_paths,
)
from ....bootstrap.managed_queue import RootEventQueueModel

TEMP_DIR = tempfile.TemporaryDirectory(prefix='petronia3-')

def discover_preboot_data() -> DiscoveryData:
    """
    DiscoveryFunction
    """

    # Find the installation directory.  These are ordered by priority.
    # Note that the standard way to set these in Linux is with compile-time
    # setting.

    distro_paths = get_distribution_paths()
    user_paths = get_user_paths()

    # For the moment, no extension paths are supported.
    extension_paths = ExtensionPaths()

    return DiscoveryData(
        extension_paths, [], TEMP_DIR.name, False,
        RootEventQueueModel(8)
    )
