
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
    PetroniaInvalidExtension,
    PetroniaCyclicExtensionDependency,
    PetroniaExtensionInitializationError,
    PetroniaNoCompatibleExtensionFound,
)
from .env import (
    PetroniaEnvironmentError,
    PetroniaFileSystemError,
    PetroniaFileError,
    PetroniaPlatformNotSupported,
)
from .serial import (
    PetroniaSerializationError,
    PetroniaValueNotSerializable,
    PetroniaSerializationFormatError,
    PetroniaSerializedCollectionFormatError,
)
