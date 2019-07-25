
"""
Exception declaration module.
"""

from .base import PetroniaError
from .thread import PetroniaThreadError, PetroniaLockTimeoutError
from .internal import (
    PetroniaInternalError,
    PetroniaInvalidState,
)
from .extensions import (
    PetroniaExtensionError,
    PetroniaExtensionNotFound,
    PetroniaExtensionNotFound,
    PetroniaInvalidExtension,
    PetroniaCyclicExtensionDependency,
    PetroniaExtensionInitializationError,
)
from .env import (
    PetroniaEnvironmentError,
    PetroniaFileSystemError,
    PetroniaFileError,
)