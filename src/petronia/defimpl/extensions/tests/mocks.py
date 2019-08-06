
from typing import Sequence, Iterable, Optional, Dict, Any
from ....base import EventBus
from ..defs import (
    ExtensionLoader,
    ExtensionVersion,
    ExtensionCompatibility,
    DiscoveredExtension,
    SecureExtensionVersion,
)

def never_called_module_loader(bus: EventBus) -> None:
    raise Exception('should not be called')

def mk_disc(
        name: str, version: SecureExtensionVersion,
        depends: Iterable[ExtensionCompatibility],
        implements: Optional[ExtensionCompatibility] = None
) -> DiscoveredExtension:
    etype = "api"
    if implements:
        etype = "impl"
    json_data = {
        "type": etype,
        "depends": map(compat_to_dict, depends),
        "implements": (),
        "defaults": (),
    }
    if implements:
        json_data["implements"] = compat_to_dict(implements)
    return DiscoveredExtension(
        name, version, json_data, never_called_module_loader
    )

def compat_to_dict(compat: ExtensionCompatibility) -> Dict[str, Any]:
    ret = {
        "extension": compat.name,
        "minimum": (compat.minimum[0], compat.minimum[1], compat.minimum[2])
    }
    if compat.below:
        ret["below"] = (compat.below[0], compat.below[1], compat.below[2])
    return ret


class MockLoader(ExtensionLoader):
    _exts: Dict[str, Dict[SecureExtensionVersion, DiscoveredExtension]]

    def __init__(self, *exts: DiscoveredExtension) -> None:
        self._exts = {}
        for disc in exts:
            if disc.name not in self._exts:
                self._exts[disc.name] = {}
            self._exts[disc.name][disc.secure_version] = disc

    def find_extension(
            self,
            only_secure: bool,
            name: str,
            version: ExtensionVersion
    ) -> Optional[DiscoveredExtension]:
        sver = (only_secure, version)
        if name in self._exts and sver in self._exts[name]:
            return self._exts[name][sver]
        if not only_secure:
            nsver = (True, version)
            if name in self._exts and nsver in self._exts[name]:
                return self._exts[name][nsver]
        return None

    def find_versions(self, name: str) -> Sequence[SecureExtensionVersion]:
        """
        Discovers the versions of the extension name available for loading.
        If a version agnostic module exists (such as a built-in version), then
        the ANY_VERSION is returned.
        """
        if name in self._exts:
            return tuple(self._exts[name].keys())
        return []
