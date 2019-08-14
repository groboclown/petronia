
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
        [['default.configuration.file']],
        TEMP_DIR_PATH,
        False,
        ExtensionLoaderModel('petronia.defimpl.extensions'),
        RootEventQueueModel(8),
        all_paths
    )
