
"""
Threading error classes.
"""

from .base import PetroniaError

class PetroniaThreadError(PetroniaError):
    """
    Base class for thread-based errors.
    """

class PetroniaLockTimeoutError(PetroniaThreadError):
    """
    Waited too long on a lock to release.  Most probably due to
    a deadlock somewhere.
    """
    