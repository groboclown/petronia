
"""
General definition for the caching mechanism.
"""

from typing import Optional, Sequence

class ExtensionStorageCache:
    """
    Keeps track of what extensions exist.  Implementations can define where
    or how the cache is persisted.
    """
    def has_cache_for(self, extension: str) -> bool:
        """
        "extension" is a loader-specific name of an extension, which can
        include the version.
        """
        raise NotImplementedError()

    def get_sub_cache(self, sub_name: str) -> self:
        """
        Creates a sub-cache, in case the loader delegates to another
        loader.
        """
        raise NotImplementedError()

    def get_cached_data(self, extension: str) -> Optional[Sequence[str]]:
        """
        Returns the loader's implementation specific data on the extension,
        which was stored earlier.
        """
        raise NotImplementedError()

    def clear_cache(self) -> None:
        """
        cleans out this cache's information.  It can clean out sub-cache
        data, too.
        """
        raise NotImplementedError()

    def set_cached_data(self, extension: str, data: Sequence[str]) -> None:
        """
        Sets the data for the extension name.  The name of the extension can
        include version data, but is loader specific.  Same for the data.
        """
        raise NotImplementedError()
