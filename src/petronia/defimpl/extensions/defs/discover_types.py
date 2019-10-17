
# mypy: allow-any-expr
# mypy: allow-any-explicit
# mypy: allow-any-generics

"""
Type definitions for loaders.
"""

from typing import Tuple, List, Sequence, Dict, Any, Callable, Optional, Union, Iterable
from ....errors import PetroniaInvalidExtension
from ....base import EventBus
from ....base.util import (
    optional_key,
    optional_list_key,

    EMPTY_TUPLE,
)
from ....core.extensions.api import (
    ExtensionVersion,
    ANY_VERSION,
)

# is secure?, version
SecureExtensionVersion = Tuple[bool, ExtensionVersion]
NO_VERSIONS: Tuple[SecureExtensionVersion] = EMPTY_TUPLE # type: ignore
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

    def __repr__(self) -> str:
        return "ExtensionCompatibility({0}, {1}, {2})".format(
            repr(self.__name), repr(self._min), repr(self._below)
        )

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
        '__loader', '_defaults',
    )
    _depends: Sequence[ExtensionCompatibility]
    _implements: Sequence[ExtensionCompatibility]
    _defaults: Sequence[ExtensionCompatibility]
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
        self.__license = optional_key(json_def, 'license', str)
        self.__homepage = optional_key(json_def, 'homepage', str)
        self._authors = optional_list_key(json_def, 'authors', str) or EMPTY_TUPLE
        self.__description = optional_key(json_def, 'description', str)
        depends: List[ExtensionCompatibility] = []
        raw_depends = optional_key(json_def, 'depends')
        if not isinstance(raw_depends, Iterable):
            raise PetroniaInvalidExtension(
                name,
                EMPTY_TUPLE,
                '"depends" not defined as an array in extension definition; found {0}'.format(
                    type(raw_depends)
                )
            )
        for dep in raw_depends:
            if isinstance(dep, dict):
                depends.append(_parse_extension_compatibility(name, dep))
        self._depends = tuple(depends)

        ext_type = optional_key(json_def, 'type')
        if ext_type == 'api':
            self.__is_impl = False
            self.__is_api = True
            self._implements = ()
            raw_defaults = optional_key(json_def, 'defaults')
            if not isinstance(raw_defaults, Iterable):
                raise PetroniaInvalidExtension(
                    name,
                    EMPTY_TUPLE,
                    '"defaults" must be defined as a list of dictionaries in extension definition'
                )
            defaults: List[ExtensionCompatibility] = []
            for dep in raw_defaults:
                if not isinstance(dep, dict):
                    raise PetroniaInvalidExtension(
                        name,
                        EMPTY_TUPLE,
                        '"defaults" must be defined as a list of dictionaries in extension definition'
                    )
                defaults.append(_parse_extension_compatibility(name, dep))
            self._defaults = tuple(defaults)
        elif ext_type == 'impl':
            self.__is_impl = True
            self.__is_api = False
            self._defaults = ()
            impl = optional_key(json_def, 'implements')
            if not isinstance(impl, Iterable):
                raise PetroniaInvalidExtension(
                    name,
                    EMPTY_TUPLE,
                    '"implements" must be defined as a list of dictionaries in extension definition'
                )
            implements: List[ExtensionCompatibility] = []
            for dep in impl:
                if not isinstance(dep, dict):
                    raise PetroniaInvalidExtension(
                        name,
                        EMPTY_TUPLE,
                        '"implements" must be defined as a list of dictionaries in extension definition'
                    )
                implements.append(_parse_extension_compatibility(name, dep))
            self._implements = tuple(implements)
        elif ext_type == 'standalone':
            self.__is_api = False
            self.__is_impl = False
            self._defaults = ()
            self._implements = ()
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
        """
        The version with security option.
        """
        return self.__version

    @property
    def is_secure(self) -> bool:
        """
        Can this extension be loaded into a reduced security context?
        Non-secure extensions must be loaded into tighter security sandboxes.
        """
        return self.__version[0]

    @property
    def is_implementation(self) -> bool:
        """
        Is this an implementation of one or more API extensions?
        """
        return self.__is_impl

    @property
    def is_api(self) -> bool:
        """
        Is this an API extension?
        """
        return self.__is_api

    @property
    def is_standalone(self) -> bool:
        """
        Is this an extension that is neither an API nor an implementation of an API?
        """
        return not self.__is_api and not self.__is_impl

    @property
    def depends_on(self) -> Sequence[ExtensionCompatibility]:
        """
        List of extensions that must be loaded before this one.
        """
        return self._depends

    @property
    def implements(self) -> Sequence[ExtensionCompatibility]:
        """
        List of APIs that this implements.
        """
        return self._implements

    @property
    def description(self) -> Optional[str]:
        return self.__description

    @property
    def authors(self) -> Sequence[str]:
        return self._authors

    @property
    def defaults(self) -> Sequence[ExtensionCompatibility]:
        """
        List of default implementations of the API, if this is an API type.
        Returns an empty list for implementation types.
        """
        return self._defaults

    @property
    def homepage(self) -> Optional[str]:
        return self.__homepage

    @property
    def license(self) -> Optional[str]:
        return self.__license

    def __repr__(self) -> str:
        return "DiscoveredExtension(name={0}, version={1})".format(
            self.name, self.secure_version
        )


def _parse_extension_compatibility(ext_name: str, raw: Dict[str, Any]) -> ExtensionCompatibility:
    name = optional_key(raw, 'extension', str)
    if not name:
        raise PetroniaInvalidExtension(
            ext_name, [],
            'invalid "extension" value in compatibility expression'
        )
    min1: Optional[Sequence[Union[int, float]]] = optional_list_key(raw, 'minimum', (int, float,))
    below1: Optional[Sequence[Union[int, float]]] = optional_list_key(raw, 'below', (int, float,))
    if not min1 or len(min1) != 3:
        raise PetroniaInvalidExtension(
            ext_name, [],
            'invalid "minimum" value in compatibility expression: {0}'.format(min1)
        )
    minimum = (int(1 * min1[0]), int(1 * min1[1]), int(1 * min1[2]),)
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
