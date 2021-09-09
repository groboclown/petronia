
# mypy: allow-any-expr
# mypy: allow-any-explicit

"""
Serialization errors.
"""

from typing import Any
from .base import PetroniaError

class PetroniaSerializationError(PetroniaError):
    """
    Basic serialization error.
    """

class PetroniaValueNotSerializable(PetroniaSerializationError):
    """
    The value can't be serialized.
    """
    def __init__(self, msg: str, obj: Any) -> None:
        PetroniaSerializationError.__init__(
            self,
            'Could not serialize "{0}": {1}'.format(repr(obj), msg)
        )


class PetroniaSerializationFormatError(PetroniaSerializationError):
    """
    The value was not in the correct serialization format.
    """


class PetroniaSerializedCollectionFormatError(PetroniaSerializationError):
    """
    The container of serialized values had the wrong format.
    """
