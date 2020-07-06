
from typing import Optional
from ...util import PetroniaReturnError


class AbcConfigType:
    """
    A structured value, parsed from a configuration, that has its internal
    format verified after construction.
    """

    # pragma no cover
    def validate_type(self) -> Optional[PetroniaReturnError]:
        raise NotImplementedError()  # pragma no cover

    # pragma no cover
    def __repr__(self) -> str:
        raise NotImplementedError()  # pragma no cover
