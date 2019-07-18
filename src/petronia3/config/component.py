
"""
Definition for components that use a configuration part.
"""

from typing import Tuple, Callable, Dict, Union, Sequence
from ..system.participant import ParticipantId

# Supported persistent types...
PersistPrimitiveType = Union[str, float, bool, None]
PersistPrimitiveListType = Union[
    Sequence[str],
    Sequence[float],
    Sequence[bool]
]
PersistType = Dict[str, Union[
    PersistPrimitiveType,
    PersistPrimitiveListType
]]

class PersistableState:
    """Persistable state, used for configuration state objects that can be
    persisted."""
    def persist(self) -> PersistType:
        """Persists this state to a simple Json object."""
        raise NotImplementedError()

ConfigStateLoader = Callable[
    [PersistType],
    Tuple[ParticipantId, PersistableState]
]
