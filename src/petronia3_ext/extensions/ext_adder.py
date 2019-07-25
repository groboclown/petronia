
"""
All the code necessary to load an extension and get it active in the system.
"""

from typing import Optional
from .defs import (
    ExtensionVersion,
    ExtensionLoader,
    ExtensionCompatibility,
    compare_version,
)

def load_extension(
        extension_name: str,
        loader: ExtensionLoader
) -> bool:
    # Find the most recent version of the extension.
    versions = loader.find_versions(extension_name)
    found: Optional[ExtensionVersion] = None
    for version in versions:
        if not found or compare_version(found, version) < 0:
            found = version
    if not found:
        return False

    

    # TODO LOAD IT

    return True

def load_compatible_extension(
        compat: ExtensionCompatibility,
        loader: ExtensionLoader
) -> None:
    versions = loader.find_versions(compat.name)
    for version in versions:
        pass
    pass
