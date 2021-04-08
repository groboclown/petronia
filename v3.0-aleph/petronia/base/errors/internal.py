
"""
Internal errors, which indicate coding problems.
"""

from typing import Optional, Union
from .base import PetroniaError

class PetroniaInternalError(PetroniaError):
    """
    Base internal error
    """


class PetroniaInternalStateError(PetroniaInternalError):
    """
    The internal state of the system did not match an expectation, which
    indidates a bug in the code.

    These are not skippable and will always be fired in production.
    """
    def __init__(self, src: Union[str, object], message: str) -> None:
        PetroniaInternalError.__init__(self, '{0}: {1}'.format(repr(src), message))


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
