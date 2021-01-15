"""
Handles the full process that loads the extension.
"""

from petronia_common.event_stream import EventForwarderTarget, RawEvent
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

    def consume(self, event: RawEvent) -> bool:
        # Find the extension location & other information.
        # Kick off a request to the load_chain_handler.
        raise NotImplementedError
