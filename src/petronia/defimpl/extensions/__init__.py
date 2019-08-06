
"""
Default extension implementations.  Several are available for different
requirements.  Due to the nature of extension loaders, they should only be
created and configured once at startup, and thus do not need the normal
extension definitions.  However, the definitions should still be provided
for proper integration into the extension API.
"""

from .defs import (
    ExtensionLoader,
)
from .loaders import (
    CompositeExtensionLoader,
    CoreExtensionLoader,
    PathExtensionLoader,
    ZipExtensionLoader,
)
