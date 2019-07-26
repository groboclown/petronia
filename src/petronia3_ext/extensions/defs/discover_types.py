
# mypy: allow-any-expr
# mypy: allow-any-explicit
# mypy: allow-any-generics

"""
Type definitions for loaders.
"""

from typing import Tuple, Sequence, Dict, Any, Callable, Optional, Union
from petronia3.errors import PetroniaInvalidExtension
from petronia3.system.bus import EventBus
from petronia3.util.op import (
    optional_key,
    optional_list_key,
    optional_typed_key,
)
from petronia3.extensions.extensions.api import (
    ExtensionVersion,
)
from petronia3.util.memory import EMPTY_TUPLE

# is secure?, version
SecureExtensionVersion = Tuple[bool, ExtensionVersion]
NO_VERSIONS: Tuple[SecureExtensionVersion] = EMPTY_TUPLE # type: ignore

MAX_DEWEY_VERSION = 999999999
ANY_VERSION: ExtensionVersion = (-1, -1, -1,)
SECURE_ANY_VERSION: SecureExtensionVersion = (True, ANY_VERSION,)
INSECURE_ANY_VERSION: SecureExtensionVersion = (False, ANY_VERSION,)
ANY_VERSION_SEQ: Tuple[ExtensionVersion] = (ANY_VERSION,)
SECURE_ANY_VERSION_SEQ: Tuple[SecureExtensionVersion] = (SECURE_ANY_VERSION,)
INSECURE_ANY_VERSION_SEQ: Tuple[SecureExtensionVersion] = (INSECURE_ANY_VERSION,)


def compare_version(first: ExtensionVersion, second: ExtensionVersion) -> int:
    """
    Returns < 0 if the first version is lower than the second, 0 if they are equal,
    and > 0 if the first version is higher than the second.
    """
    if first[0] == second[0]:
        if first[1] == second[1]:
            return first[2] - second[2]
        return first[1] - second[1]
    return first[0] - second[0]

class ExtensionCompatibility:
    """
    Describes the compatibility request for an extension.
    """
    __slots__ = ('__name', '_min', '_below',)
    _min: ExtensionVersion
    _below: Optional[ExtensionVersion]

    def __init__(
            self, name: str, minimum: ExtensionVersion, below: Optional[ExtensionVersion]
    ) -> None:
        self.__name = name
        self._min = minimum
        self._below = below

    @property
    def name(self) -> str:
        """Name of the extension"""
        return self.__name

    @property
    def minimum(self) -> ExtensionVersion:
        """Minimum compatible version"""
        return self._min

    @property
    def below(self) -> Optional[ExtensionVersion]:
        """optional maximum version at which this is no longer compatible"""
        return self._below

    def is_compatible_with(self, version: ExtensionVersion) -> bool:
        """
        Does this compatibility description allow for the input
        version to be a match?
        """
        if version == ANY_VERSION or self._min == ANY_VERSION:
            return True

        if compare_version(self._min, version) > 0:
            # Minimum version is > checked version
            return False
        # else it's a match on min.

        if self._below and self._below != ANY_VERSION:
            if compare_version(self._below, version) >= 0:
                # the "must be below" version is equal or higher than
                # the checked version.
                return False
            # else it's a match on below

        return True


ModuleLoader = Callable[[EventBus], None]


class DiscoveredExtension:
    """
    All attributes that must be defined for an extension.

    Raises PetroniaInvalidExtension if the json_def is invalid.
    """
    __slots__ = (
        '__name', '__version',
        '__is_impl', '__is_api',
        '_depends', '_implements',
        '__description', '_authors',
        '__homepage', '__license',
        '__loader',
    )
    _depends: Sequence[ExtensionCompatibility]
    _implements: Optional[ExtensionCompatibility]
    _authors: Sequence[str]

    def __init__(
            self,
            name: str, version: SecureExtensionVersion,
            json_def: Dict[str, Any],
            loader: ModuleLoader
    ) -> None:
        self.__name = name
        self.__version = version
        self.__loader = loader
        self.__license = optional_typed_key(json_def, 'license', str)
        self.__homepage = optional_typed_key(json_def, 'homepage', str)
        self._authors = optional_list_key(json_def, 'authors', str) or EMPTY_TUPLE
        self.__description = optional_typed_key(json_def, 'description', str)
        depends = []
        raw_depends = optional_key(json_def, 'depends')
        if not isinstance(raw_depends, (list, tuple)):
            raise PetroniaInvalidExtension(
                name,
                EMPTY_TUPLE,
                '"depends" not defined as an array in extension definition'
            )
        for dep in raw_depends:
            if isinstance(dep, dict):
                depends.append(_parse_extension_compatibility(name, dep))
        self._depends = tuple(depends)

        ext_type = optional_key(json_def, 'type')
        if ext_type == 'api':
            self.__is_impl = False
            self.__is_api = True
            self._implements = None
        elif ext_type == 'impl':
            self.__is_impl = True
            self.__is_api = False
            impl = optional_key(json_def, 'implements')
            if not isinstance(impl, dict):
                raise PetroniaInvalidExtension(
                    name,
                    EMPTY_TUPLE,
                    '"implements" must be defined as a dictionary in extension definition'
                )
            self._implements = _parse_extension_compatibility(name, impl)
        else:
            raise PetroniaInvalidExtension(
                name,
                EMPTY_TUPLE,
                'no valid "type" value in extension definition'
            )

    @property
    def module_loader(self) -> ModuleLoader:
        return self.__loader

    @property
    def name(self) -> str:
        return self.__name

    @property
    def version(self) -> ExtensionVersion:
        return self.__version[1]

    @property
    def secure_version(self) -> SecureExtensionVersion:
        return self.__version

    @property
    def is_secure(self) -> bool:
        return self.__version[0]

    @property
    def is_implementation(self) -> bool:
        return self.__is_impl

    @property
    def is_api(self) -> bool:
        return self.__is_api

    @property
    def depends_on(self) -> Sequence[ExtensionCompatibility]:
        return self._depends

    @property
    def implements(self) -> Optional[ExtensionCompatibility]:
        return self._implements

    @property
    def description(self) -> Optional[str]:
        return self.__description

    @property
    def authors(self) -> Sequence[str]:
        return self._authors

    @property
    def homepage(self) -> Optional[str]:
        return self.__homepage

    @property
    def license(self) -> Optional[str]:
        return self.__license


def _parse_extension_compatibility(ext_name: str, raw: Dict[str, Any]) -> ExtensionCompatibility:
    name = optional_typed_key(raw, 'extension', str)
    if not name:
        raise PetroniaInvalidExtension(
            ext_name, [],
            'invalid "extension" value in compatibility expression'
        )
    minimum1: Optional[Sequence[Union[int, float]]] = optional_list_key(raw, 'minimum', Union[int, float])
    below1: Optional[Sequence[Union[int, float]]] = optional_list_key(raw, 'below', Union[int, float])
    if minimum1 and len(minimum1) == 3:
        minimum = (int(1 * minimum1[0]), int(1 * minimum1[1]), int(1 * minimum1[2]),)
    else:
        raise PetroniaInvalidExtension(
            ext_name, [],
            'invalid "minimum" value in compatibility expression'
        )
    below: Optional[ExtensionVersion] = None
    if below1:
        if len(below1) == 3:
            below = (int(below1[0]), int(below1[1]), int(below1[2]),)
        else:
            raise PetroniaInvalidExtension(
                ext_name, [],
                'invalid "below" value in compatibility expression'
            )
    return ExtensionCompatibility(name, minimum, below)
