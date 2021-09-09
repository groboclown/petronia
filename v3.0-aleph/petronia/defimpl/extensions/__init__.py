
"""
Default extension implementations.  Several are available for different
requirements.  Due to the nature of extension loaders, they should only be
created and configured once at startup, and thus do not need the normal
extension definitions.  However, the definitions should still be provided
for proper integration into the extension API.
"""

# Uses the extension loader API for the name, not the extension names.
from .bootstrap import bootstrap_extension_loader
from .bootstrap import compatible_start_extension as start_extension
from .bootstrap import EXTENSION_METADATA
