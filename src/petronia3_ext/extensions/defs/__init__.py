
"""
Internal stuff for the loaders.
"""

from petronia3.extensions.extensions.api import (
    ExtensionVersion,
    LoadedExtension,
)
from .discover_types import (
    DiscoveredExtension,
    SecureExtensionVersion,
    ExtensionCompatibility,
    ModuleLoader,
    compare_version,
    ANY_VERSION,
    SECURE_ANY_VERSION,
    INSECURE_ANY_VERSION,
    ANY_VERSION_SEQ,
    SECURE_ANY_VERSION_SEQ,
    INSECURE_ANY_VERSION_SEQ,
    NO_VERSIONS,
)
from .loader_types import (
    ExtensionLoader,
)
from .cache import (
    ExtensionStorageCache,
)
