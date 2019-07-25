
"""
Loads the core extensions.
"""

import importlib.util
from importlib.machinery import ModuleSpec
from typing import Sequence, Optional
from ...defs import (
    DiscoveredExtension,
    ExtensionLoader,
    ExtensionVersion,
    SecureExtensionVersion,
    SECURE_ANY_VERSION_SEQ,
)
from ...util.spec import get_extension_from_module_spec


class CoreExtensionLoader(ExtensionLoader):
    """
    Loads default Petronia extensions through the normal Python paths.
    """

    def find_versions(self, name: str) -> Sequence[SecureExtensionVersion]:
        mod_spec = self._load_spec(name)
        if mod_spec:
            # Core extensions are always marked as secure.
            return SECURE_ANY_VERSION_SEQ
        return tuple()

    def find_extension(
            self,
            only_secure: bool,
            name: str,
            version: ExtensionVersion
    ) -> Optional[DiscoveredExtension]:
        # Ignore the "only_secure", because core extensions are always
        # marked as secure.
        mod_spec = self._load_spec(name)
        if mod_spec is not None:
            # If this returns "None", then there's something wrong
            # with Petronia.
            return get_extension_from_module_spec(name, version, mod_spec, None)
        return None

    def _load_spec(self, name) -> Optional[ModuleSpec]:
        if name.startswith('core.'):
            formal_name = 'petronia3.extensions.' + name[5:]
        elif name.startswith('default.'):
            formal_name = 'petronia3_ext.' + name[8:]
        elif name.startswith('petornia3.extensions.') or name.startswith('petronia3_ext.'):
            formal_name = name
        else:
            return None
        return importlib.util.find_spec(formal_name)
