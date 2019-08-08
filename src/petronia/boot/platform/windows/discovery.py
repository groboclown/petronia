
"""
Implements the required discovery function.
"""

from ....core.platform.preboot import (
    DiscoveryData,
    ExtensionPaths,
)
from .paths import (
    get_user_paths,
)
from ..general import (
    TEMP_DIR_PATH,
)
from ...bootstrap.managed_queue import RootEventQueueModel

def discover_preboot_data() -> DiscoveryData:
    """
    DiscoveryFunction
    """

    # Find the installation directory.  These are ordered by priority.
    # Note that the standard way to set these in Linux is with compile-time
    # setting.

    user_paths = get_user_paths()

    # For the moment, no extension paths are supported.
    extension_paths = ExtensionPaths()

    return DiscoveryData(
        extension_paths,
        [],
        TEMP_DIR_PATH,
        False,
        RootEventQueueModel(8)
    )
