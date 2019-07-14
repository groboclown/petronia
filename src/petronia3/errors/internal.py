
"""
Internal errors, which indicate coding problems.
"""

from typing import Optional, Any
from .base import PetroniaError

class PetroniaInternalError(PetroniaError):
    """
    Base internal error
    """


class PetroniaInvalidState(AssertionError):
    """
    Encountered an invalid state.

    These are debug validations, so cannot be relied to fire in a production
    environment.
    """
    def __init__(self, src: str, validation_problem: str, details: Optional[str] = None) -> None:
        if details is None:
            msg = "{0}: {1}".format(src, validation_problem)
        else:
            msg = "{0}: {1}: {2}".format(src, validation_problem, details)
        AssertionError.__init__(
            self,
            msg
        )
