
"""
Type definitions for loaders.
"""

from typing import Sequence, Optional
from .discover_types import (
    DiscoveredExtension,
    ExtensionVersion,
    SecureExtensionVersion,
)


class ExtensionLoader:
    """
    Abstract definition for all loaders.
    """
    def find_extension(
            self,
            only_secure: bool,
            name: str,
            version: ExtensionVersion
    ) -> Optional[DiscoveredExtension]:
        """
        Finds the extension with the given name and version.  If not found,
        then returns None.
        """
        raise NotImplementedError()

    def find_versions(self, name: str) -> Sequence[SecureExtensionVersion]:
        """
        Discovers the versions of the extension name available for loading.
        If a version agnostic module exists (such as a built-in version), then
        the ANY_VERSION is returned.
        """
        raise NotImplementedError()
