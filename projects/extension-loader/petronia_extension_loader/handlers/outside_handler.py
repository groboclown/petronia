"""
Handles the full process that loads the extension.
"""
from typing import Dict, Any

from petronia_common.event_stream import EventForwarderTarget, RawBinaryReader
from petronia_common.util import PetroniaReturnError
from ..context import EventHandlerContext
from ..events.impl.extension_loader import LoadExtensionRequestEvent


class LoadExtensionHandler(EventForwarderTarget):
    """
    Listens to the external requests to load an extension.  This begins a chain of
    events.
    """

    __slots__ = ('_context',)

    def __init__(self, context: EventHandlerContext) -> None:
        self._context = context

    def can_consume(self, event_id: str, source_id: str, target_id: str) -> bool:
        return event_id == LoadExtensionRequestEvent.FULL_EVENT_NAME

    def on_error(self, error: PetroniaReturnError) -> bool:
        pass

    def on_eof(self) -> None:
        pass

    def consume_object(
            self, event_id: str, source_id: str,
            target_id: str, event_data: Dict[str, Any],
    ) -> bool:
        # FIXME handle the extension loading.
        pass

    def consume_binary(
            self, event_id: str, source_id: str, target_id: str, size: int,
            data_reader: RawBinaryReader,
    ) -> bool:
        return False
