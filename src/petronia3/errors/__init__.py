
"""
Exception declaration module.
"""

from .base import PetroniaError
from .thread import PetroniaThreadError, PetroniaLockTimeoutError
from .internal import (
    PetroniaInternalError,
    PetroniaInvalidState,
)
