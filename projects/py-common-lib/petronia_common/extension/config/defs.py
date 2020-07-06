
"""
Basic definitions for configuration objects.
"""

from typing import Optional
from ...util import PetroniaReturnError


class AbcConfigType:
    """
    A structured value, parsed from a configuration, that has its internal
    format verified after construction.
    """

    # pragma no cover
    def validate_type(self) -> Optional[PetroniaReturnError]:
        """Validate whether this type was created in a way consistent with
        the expected constraints."""
        raise NotImplementedError()  # pragma no cover

    # pragma no cover
    def __repr__(self) -> str:
        """Generate a representation of the config type object."""
        raise NotImplementedError()  # pragma no cover
