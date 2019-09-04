
"""
Common type information
"""

from typing import Tuple, Any, no_type_check

# major, minor, micro
ExtensionVersion = Tuple[int, int, int]

MAX_DEWEY_VERSION = 999999999
ANY_VERSION: ExtensionVersion = (-1, -1, -1,)


def is_version_valid(version: ExtensionVersion) -> bool:
    """Is the version number valid?"""
    if not isinstance(version, tuple) or len(version) != 3:
        return False
    if version == ANY_VERSION:
        return True
    return (
        0 <= version[0] <= MAX_DEWEY_VERSION and
        0 <= version[1] <= MAX_DEWEY_VERSION and
        0 <= version[2] <= MAX_DEWEY_VERSION
    )


class LoadedExtension:
    """
    Simple data type for the loaded extension.
    """
    __slots__ = ('__name', '__secure', '__version', '__hash')

    def __init__(self, name: str, secure: bool, version: ExtensionVersion) -> None:
        self.__name = name
        self.__secure = secure
        self.__version = version
        # secure is not common enough to put in the hash.
        self.__hash = hash(name) ^ hash(version)

    @property
    def name(self) -> str:
        return self.__name

    @property
    def is_secure(self) -> bool:
        return self.__secure

    @property
    def version(self) -> ExtensionVersion:
        return self.__version

    def __repr__(self) -> str:
        return "LoadedExtension(name={0}, secure={1}, version={2})".format(
            self.name, self.is_secure, self.version
        )

    @no_type_check
    def __eq__(self, other: Any) -> bool:
        if hasattr(other, '__class__') and other.__class__ == self.__class__:
            # print("checking {0} against {1}".format(self, other))
            return (
                other.name == self.__name and
                other.is_secure == self.__secure and
                other.version == self.__version
            )
        print("not equal - not same class")
        return False

    def __hash__(self) -> int:
        return self.__hash
