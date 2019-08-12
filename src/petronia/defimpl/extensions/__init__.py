
"""
Default extension implementations.  Several are available for different
requirements.  Due to the nature of extension loaders, they should only be
created and configured once at startup, and thus do not need the normal
extension definitions.  However, the definitions should still be provided
for proper integration into the extension API.
"""

# Not renamed, because the extension loader doesn't load itself.
from .bootstrap import bootstrap_extension_loader
