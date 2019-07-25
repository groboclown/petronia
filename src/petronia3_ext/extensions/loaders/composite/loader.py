
"""
The composite loader.

It doesn't use the cache.
"""

from typing import Optional, Sequence, Set
from ...defs import (
    DiscoveredExtension,
    ExtensionLoader,
    ExtensionVersion,
    SecureExtensionVersion,
)


class CompositeExtensionLoader(ExtensionLoader):
    """
    Delegates extension loading to sub-loaders.
    """
    __slots__ = ('_proxies',)
    _proxies: Sequence[ExtensionLoader]

    def __init__(self, proxies: Sequence[ExtensionLoader]) -> None:
        self._proxies = proxies

    def find_versions(self, name: str) -> Sequence[SecureExtensionVersion]:
        ret: Set[ExtensionVersion] = set()
        for proxy in self._proxies:
            ret = ret.union(proxy.find_versions(name))
        return tuple(ret)

    def find_extension(
            self,
            only_secure: bool,
            name: str,
            version: ExtensionVersion
    ) -> Optional[DiscoveredExtension]:
        for proxy in self._proxies:
            ret = proxy.find_extension(name, only_secure, version)
            if ret:
                return ret
        return None
