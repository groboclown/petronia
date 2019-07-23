
"""
Error types when trying to load extensions.
"""

from typing import Sequence
from .base import PetroniaError


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
    def __init__(self, extension_name: str, dependencies_loaded: Sequence[str], msg: str) -> None:
        PetroniaExtensionError.__init__(self, extension_name, msg)
        self.dependencies_loaded = tuple(dependencies_loaded)

class PetroniaExtensionNotFound(PetroniaExtensionLoadError):
    """
    No extension with the given name was found.
    """
    def __init__(self, extension_name: str, dependencies_loaded: Sequence[str]) -> None:
        PetroniaExtensionLoadError.__init__(
            self, extension_name, dependencies_loaded,
            'could not find module'
        )

class PetroniaCyclicExtensionDependency(PetroniaExtensionLoadError):
    """
    The extension defines a dependency which in turn depends on this extension.
    """
    __slots__ = ('cycle_in',)
    def __init__(self, extension_name: str, cycle_in: Sequence[str], dependencies_loaded: Sequence[str]) -> None:
        PetroniaExtensionLoadError.__init__(
            self, extension_name, dependencies_loaded,
            'multiple extensions depend upon each other: {0}'.format(cycle_in)
        )
        self.cycle_in = tuple(cycle_in)

class PetroniaInvalidExtension(PetroniaExtensionLoadError):
    """
    The extension was not defined correctly.
    """
    def __init__(self, extension_name: str, dependencies_loaded: Sequence[str], msg: str) -> None:
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
            self, extension_name: str, dependencies_loaded: Sequence[str], source: BaseException
    ) -> None:
        PetroniaExtensionLoadError.__init__(
            self, extension_name, dependencies_loaded,
            str(source)
        )
        self.source_error = source
