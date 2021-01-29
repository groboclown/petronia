"""Extensions to the standard types."""

from typing import Optional, Generic
from petronia_common.util import T
from petronia_common.extension.config.event_schema import StructureEventDataType


class Sourced(Generic[T]):
    """Wrapper that gives a hint to the type name."""
    __slots__ = ('suggested_name',)

    def __init__(self) -> None:
        self.suggested_name: Optional[str] = None
