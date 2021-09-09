
"""
Implements the required discovery function.
"""

from ....core.platform.preboot import (
    DiscoveryData,
    ExtensionPaths,
    ExtensionLoaderModel,
)
from .paths import (
    get_user_paths,
)
from ..general import (
    TEMP_DIR_PATH,
    get_preboot_extension_sets,
)
from ...bootstrap.managed_queue import RootEventQueueModel
from .autodetect import discover_platform_ext


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
        get_preboot_extension_sets(),
        [
            ['default.configuration.file'],
            [discover_platform_ext()],
        ],
        TEMP_DIR_PATH,
        False,
        ExtensionLoaderModel('petronia.defimpl.extensions'),
        RootEventQueueModel(8),
        user_paths,
        '''
Windows Specific Setup:

The configuration for Windows will add default configuration search path
of the directories %LOCALAPPDATA%\petronia and %HOME%\.petronia.
'''
    )
