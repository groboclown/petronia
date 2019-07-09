
"""
Internal errors, which indicate coding problems.
"""

from .base import PetroniaError

class PetroniaInternalError(PetroniaError):
    """
    Base internal error
    """


class PetroniaInvalidState(PetroniaInternalError):
    """
    Encountered an invalid state.
    """
    def __init__(self, src: str, validation_problem: str, details=None):
        if details is None:
            msg = "{0}: {1}".format(src, validation_problem)
        else:
            msg = "{0}: expected {1}: {2}".format(src, validation_problem, details)
        PetroniaInternalError.__init__(
            self,
            msg
        )


def assert_state(condition: bool, src: str, validation_problem: str, details=None):
    """
    Perform a state validation check.
    """
    if not condition:
        raise PetroniaInvalidState(src, validation_problem, details)

def assert_contains(container: dict or list or tuple, key: str or int, src: str, validation_format: str):
    """
    Ensure the container has the given key
    """
    assert_state(key in container, src, validation_format.format(key))

def assert_get(container: dict or list or tuple, key: str or int, src: str, validation_format: str):
    """
    Ensure the container has the given key, and returns the key's contents.
    """
    assert_state(key in container, src, validation_format.format(key))
    return container[key]
