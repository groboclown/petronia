
"""
Extensions have a common schema definition.

The constructors are allowed to have "too many arguments" (according to pylint),
because they are expected to only be invoked from within these local modules.
"""

from typing import Sequence, Iterable, List, Set, Literal, Optional
from abc import ABC
import re
from .defs import AbcConfigType
from .event_schema import EventType
from .version import ExtensionVersion, cmp_extension
from ...util import PetroniaReturnError, UserMessage, possible_error
from ...util import i18n as _

ExtensionType = Literal["impl", "api", "standalone"]


class ExtensionDependency:
    """Defines another extension on which this extension requires to be loaded."""
    __slots__ = ('__name', '__minimum', '__below',)

    def __init__(
            self,
            name: str,
            minimum_version: ExtensionVersion,
            below_version: Optional[ExtensionVersion],
    ) -> None:
        self.__name = name
        self.__minimum = minimum_version
        self.__below = below_version

    def __repr__(self) -> str:
        return (
            f'ExtensionDependency({self.name}, '
            f'min={self.minimum_version}, below={self.below_version})'
        )

    @property
    def name(self) -> str:
        """Name of the required dependency."""
        return self.__name

    @property
    def minimum_version(self) -> ExtensionVersion:
        """Minimum allowed version for the loaded dependency."""
        return self.__minimum

    @property
    def below_version(self) -> Optional[ExtensionVersion]:
        """Optional upper-bound for the dependency version that no longer conforms to what's
        required."""
        return self.__below

    def is_within(self, version: ExtensionVersion) -> bool:
        """Is the given version within this dependency bounds?"""
        if cmp_extension(self.minimum_version, version) > 0:
            return False
        if self.__below and cmp_extension(self.__below, version) <= 0:
            return False
        return True


class AbcExtensionMetadata(AbcConfigType, ABC):
    """Base class for extension types."""
    __slots__ = (
        '__name', '__about', '__description', '__version', '__extension_type',
        '__depends', '__licenses', '__authors',
    )

    def __init__(  # pylint: disable=R0913
            self,
            name: str,
            version: ExtensionVersion,
            about: str,
            description: str,
            extension_type: ExtensionType,
            depends: Iterable[ExtensionDependency],
            licenses: Iterable[str],
            authors: Iterable[str],
    ) -> None:
        """Constructor."""
        self.__name = name
        self.__version = version
        self.__about = about
        self.__description = description
        self.__extension_type = extension_type
        self.__depends = tuple(depends)
        self.__licenses = tuple(set(licenses))
        self.__authors = tuple(set(authors))

    @property
    def name(self) -> str:
        """Extension name."""
        return self.__name

    @property
    def version(self) -> ExtensionVersion:
        """Version of this extension."""
        return self.__version

    @property
    def about(self) -> str:
        """Short description about this extension."""
        return self.__about

    @property
    def description(self) -> str:
        """Detailed description about this extension."""
        return self.__description

    @property
    def extension_type(self) -> ExtensionType:
        """The kind of extension, which implies the supported data."""
        return self.__extension_type

    @property
    def depends_on(self) -> Sequence[ExtensionDependency]:
        """The other extensions that must be loaded before this one."""
        return self.__depends

    @property
    def authors(self) -> Sequence[str]:
        """List of people credited with creating this extension."""
        return self.__authors

    @property
    def licenses(self) -> Sequence[str]:
        """License(s) for this extension."""
        return self.__licenses

    def _sub_repr(self) -> str:
        return (
            f'name={repr(self.name)}, version={self.version}, '
            f'about={repr(self.about)}, description={repr(self.description)}, '
            f'depends={repr(self.depends_on)}, licenses={repr(self.licenses)}, '
            f'authors={repr(self.authors)}'
        )


class ApiExtensionMetadata(AbcExtensionMetadata):
    """An API style extension.  These do not implement any logic.
    Indeed, this metadata is the full contents of the extension."""
    __slots__ = ('__events', '__default_implementation')

    def __init__(  # pylint: disable=R0913
            self,
            name: str,
            version: ExtensionVersion,
            about: str,
            description: str,
            depends: Iterable[ExtensionDependency],
            licenses: Iterable[str],
            authors: Iterable[str],
            events: Iterable[EventType],
            default_implementation: Optional[ExtensionDependency],
    ) -> None:
        """All the data needed to create this extension."""
        AbcExtensionMetadata.__init__(
            self, name, version, about, description, "api", depends, licenses, authors,
        )
        self.__events = tuple(events)
        self.__default_implementation = default_implementation

    def __repr__(self) -> str:
        return (
            f'ApiExtensionMetadata({self._sub_repr()}, events={repr(self.events)})'
        )

    @property
    def events(self) -> Sequence[EventType]:
        """Events defined by this API."""
        return self.__events

    @property
    def default_implementation(self) -> Optional[ExtensionDependency]:
        """The optional default implementation, if the end-user does not define one."""
        return self.__default_implementation

    def validate_type(self) -> Optional[PetroniaReturnError]:
        messages: List[UserMessage] = []
        validate_name(self.name, messages)
        validate_dependencies(self.depends_on, messages)
        event_names: Set[str] = set()
        for event in self.events:
            if event.name in event_names:
                messages.append(UserMessage(
                    _('duplicate event name: {name}'),
                    name=event.name,
                ))
            else:
                event_names.add(event.name)
            validation = event.validate_type()
            if validation:
                messages.extend(validation.messages())
        return possible_error(messages)


class ImplExtensionMetadata(AbcExtensionMetadata):
    """Implementation of an API."""
    __slots__ = ('__implements',)

    def __init__(  # pylint: disable=R0913
            self,
            name: str,
            version: ExtensionVersion,
            about: str,
            description: str,
            depends: Iterable[ExtensionDependency],
            licenses: Iterable[str],
            authors: Iterable[str],
            implements: Iterable[ExtensionDependency],
    ) -> None:
        """Constructor."""
        AbcExtensionMetadata.__init__(
            self, name, version, about, description, "api", depends, licenses, authors,
        )
        self.__implements = tuple(implements)

    def __repr__(self) -> str:
        return f'ImplExtensionMetadata({self._sub_repr()}, implements={repr(self.implements)})'

    @property
    def implements(self) -> Sequence[ExtensionDependency]:
        """Lists of APIs this extension implements."""
        return self.__implements

    def validate_type(self) -> Optional[PetroniaReturnError]:
        messages: List[UserMessage] = []
        validate_name(self.name, messages)
        validate_dependencies(self.depends_on, messages)
        validate_dependencies(self.implements, messages)
        return possible_error(messages)


class StandAloneExtensionMetadata(AbcExtensionMetadata):
    """A stand-alone extension, which may use APIs, but doesn't implement them."""
    __slots__ = ()

    def __init__(  # pylint: disable=R0913
            self,
            name: str,
            version: ExtensionVersion,
            about: str,
            description: str,
            depends: Iterable[ExtensionDependency],
            licenses: Iterable[str],
            authors: Iterable[str],
    ) -> None:
        """Standalone extension constructor."""
        AbcExtensionMetadata.__init__(
            self, name, version, about, description, "standalone", depends, licenses, authors,
        )

    def __repr__(self) -> str:
        return f'StandAloneExtensionMetadata({self._sub_repr()})'

    def validate_type(self) -> Optional[PetroniaReturnError]:
        messages: List[UserMessage] = []
        validate_name(self.name, messages)
        validate_dependencies(self.depends_on, messages)
        return possible_error(messages)


MIN_EXTENSION_NAME_LENGTH = 2
MAX_EXTENSION_NAME_LENGTH = 255
EXTENSION_NAME_FORMAT = re.compile(r'^[a-z0-9][a-z0-9_]*(?:\.[a-z0-9][a-z0-9_]*)*$')


def validate_name(name: str, messages: List[UserMessage]) -> None:
    """Validate that the extension name matches the expected format."""
    if EXTENSION_NAME_FORMAT.match(name) is None:
        messages.append(UserMessage(
            _('extension name ({name}) must conform to the pattern [a-z0-9][a-z0-9._]'),
            name=name
        ))
    if not MIN_EXTENSION_NAME_LENGTH <= len(name) <= MAX_EXTENSION_NAME_LENGTH:
        messages.append(UserMessage(
            _(
                # TODO ensure po generated localization file uses this whole string.
                'extension name ({name}) must be {MIN_EXTENSION_NAME_LENGTH} '
                'to {MAX_EXTENSION_NAME_LENGTH} long'),
            name=name,
            MIN_EXTENSION_NAME_LENGTH=MIN_EXTENSION_NAME_LENGTH,
            MAX_EXTENSION_NAME_LENGTH=MAX_EXTENSION_NAME_LENGTH,
        ))


def validate_dependencies(
        dependencies: Sequence[ExtensionDependency], messages: List[UserMessage],
) -> None:
    """Validate that the dependency names conform to the standards."""
    dependency_names: Set[str] = set()
    for dep in dependencies:
        if dep.name in dependency_names:
            messages.append(UserMessage(
                _('duplicate dependency: {name}'),
                name=dep.name,
            ))
        else:
            dependency_names.add(dep.name)
