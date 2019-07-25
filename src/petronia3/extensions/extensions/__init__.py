
"""
Handlers for loading and unloading extensions.

Like all extensions, this must strictly adhere to the normal extension
convensions.  However, due to its nature, it isn't loaded like a normal
extension, because it does the loading.
"""

from .api import *

EXTENSION_METADATA = {
    "name": "core.extensions.api",
    "version": (1, 0, 0,),
    "type": "api",
    "depends": [
        {
            "extension": "core.state.api",
            "minimum": (1, 0, 0,),
        },
    ],
    "description": "required capabilities for all extensions loaders",
    "authors": ("petronia",),
    "homepage": "https://github.com/groboclown/petronia"
}
