"""Handle the request to load an extension."""
from typing import Dict, Any

from petronia_common.event_stream import EventForwarderTarget, RawBinaryReader
from petronia_common.util import PetroniaReturnError
from ..defs import EventHandlerContext


class InternalLoadExtensionRequestHandler(EventForwarderTarget):
    """Starts the extension loading chain."""

    __slots__ = ('_context',)

    def __init__(self, context: EventHandlerContext) -> None:
        self._context = context

    def can_consume(self, event_id: str, source_id: str, target_id: str) -> bool:
        pass

    def on_error(self, error: PetroniaReturnError) -> bool:
        pass

    def on_eof(self) -> None:
        pass

    def consume_object(
            self, event_id: str, source_id: str, target_id: str, event_data: Dict[str, Any],
    ) -> bool:
        pass

    def consume_binary(
            self, event_id: str, source_id: str, target_id: str, size: int,
            data_reader: RawBinaryReader,
    ) -> bool:
        pass
