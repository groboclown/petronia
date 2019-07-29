
"""
The common API that platform implementations must provide before the
extensions are loaded.  This does not define a real extension, but rather the
necessities that the platform preboot must provide, and some helpful types
to support accessing those platform provided items.

This involves just data discovery used by the bootstrap implementation.
"""

from .directories import (
    SandboxPath,
    ExtensionPaths,
)

from .discovery import (
    DiscoveryData,
    DiscoveryFunction,
    DISCOVERY_FUNCTION_NAME,
    RunSystemFunction,
    RUN_SYSTEM_FUNCTION_NAME,
    PREBOOT_MODULE_NAME,
)
