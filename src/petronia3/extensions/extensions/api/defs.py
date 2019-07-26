
"""
Common type information
"""

from typing import Tuple, Any, no_type_check

# major, minor, micro
ExtensionVersion = Tuple[int, int, int]

class LoadedExtension:
    """
    Simple data type for the loaded extension.
    """
    __slots__ = ('__name', '__secure', '__version')
    def __init__(self, name: str, secure: bool, version: ExtensionVersion) -> None:
        self.__name = name
        self.__secure = secure
        self.__version = version

    @property
    def name(self) -> str:
        return self.__name

    @property
    def is_secure(self) -> bool:
        return self.__secure

    @property
    def version(self) -> ExtensionVersion:
        return self.__version

    @no_type_check
    def __eq__(self, other: Any) -> bool:
        if hasattr(other, '__class__') and other.__class__ == self.__class__:
            return (
                other.name == self.__name and
                other.is_secure == self.__secure and
                other.version == self.__version
            )
        return False
