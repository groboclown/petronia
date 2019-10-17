
"""
Error types when trying to load extensions.
"""

from typing import Iterable
from .base import PetroniaError
from ..util.memory import EMPTY_TUPLE


class PetroniaExtensionError(PetroniaError):
    """
    Base class for errors related to extensions.
    """
    __slots__ = ('extension_name',)

    def __init__(self, extension_name: str, msg: str) -> None:
        PetroniaError.__init__(self, 'Extension {0}: {1}'.format(extension_name, msg))
        self.extension_name = extension_name


class PetroniaExtensionLoadError(PetroniaExtensionError):
    """
    The extension could not be loaded.  However, during load, other dependencies
    may have been loaded, and thus may need to be removed.
    """
    __slots__ = ('dependencies_loaded',)

    def __init__(self, extension_name: str, dependencies_loaded: Iterable[str], msg: str) -> None:
        PetroniaExtensionError.__init__(self, extension_name, msg)
        self.dependencies_loaded = tuple(dependencies_loaded)


class PetroniaExtensionNotFound(PetroniaExtensionLoadError):
    """
    No extension with the given name was found.
    """
    def __init__(self, extension_name: str, dependencies_loaded: Iterable[str]) -> None:
        PetroniaExtensionLoadError.__init__(
            self, extension_name, dependencies_loaded,
            'could not find module'
        )


class PetroniaCyclicExtensionDependency(PetroniaExtensionLoadError):
    """
    The extension defines a dependency which in turn depends on this extension.
    """
    __slots__ = ('cycle_in',)

    def __init__(self, extension_name: str, cycle_in: Iterable[str], dependencies_loaded: Iterable[str]) -> None:
        PetroniaExtensionLoadError.__init__(
            self, extension_name, dependencies_loaded,
            'multiple extensions depend upon each other: {0}'.format(cycle_in)
        )
        self.cycle_in = tuple(cycle_in)


class PetroniaInvalidExtension(PetroniaExtensionLoadError):
    """
    The extension was not defined correctly.
    """
    def __init__(self, extension_name: str, dependencies_loaded: Iterable[str], msg: str) -> None:
        PetroniaExtensionLoadError.__init__(
            self, extension_name, dependencies_loaded,
            msg
        )


class PetroniaExtensionInitializationError(PetroniaExtensionLoadError):
    """
    The extension raised an error during the load.
    """
    __slots__ = ('source_error',)

    def __init__(
            self, extension_name: str, dependencies_loaded: Iterable[str], source: BaseException
    ) -> None:
        PetroniaExtensionLoadError.__init__(
            self, extension_name, dependencies_loaded,
            str(source)
        )
        self.source_error = source


class PetroniaNoCompatibleExtensionFound(PetroniaExtensionLoadError):
    """
    A dependency for an extension was found, but no compatible version was
    available.  It could be that multiple extensions had dependencies on it,
    but they had conflicting version requirements.
    """
    def __init__(
            self, extension_name: str, dependent: Iterable[str]
    ) -> None:
        PetroniaExtensionLoadError.__init__(
            self, extension_name,
            EMPTY_TUPLE, # type: ignore
            'no compatible version found; possible conflict as dependency of {0}'.format(
                ', '.join(dependent)
            )
        )
        self.dependent = dependent


class PetroniaExtensionImplementationNotFound(PetroniaExtensionLoadError):
    """
    No extension found that extends the given extension.
    """
    def __init__(self, extension_name: str, dependencies_loaded: Iterable[str]) -> None:
        PetroniaExtensionLoadError.__init__(
            self, extension_name, dependencies_loaded,
            'No implementation of the extension'
        )
