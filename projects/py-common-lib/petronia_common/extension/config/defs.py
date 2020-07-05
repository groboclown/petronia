
from typing import Optional
from ...util import PetroniaReturnError


class AbcConfigType:
    """
    A structured value, parsed from a configuration, that has its internal
    format verified after construction.
    """
    def validate_type(self) -> Optional[PetroniaReturnError]:
        raise NotImplementedError()

    def __repr__(self) -> str:
        raise NotImplementedError()
