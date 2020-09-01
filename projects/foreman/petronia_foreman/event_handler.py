
"""
Parse and handle events directed to foreman.
"""

from petronia_common.event_stream import (
    RawEvent,
    EventForwarderTarget,
    is_raw_event_object,
    raw_event_id,
    raw_event_source_id,
    raw_event_target_id,
)
from petronia_common.util import PetroniaReturnError


class ForemanEventTarget(EventForwarderTarget):
    """Processes events directed to the Foreman process."""

    def can_consume(self, event_id: str, source_id: str, target_id: str) -> bool:
        pass

    async def consume(self, event: RawEvent) -> bool:
        pass

    def on_error(self, error: PetroniaReturnError) -> bool:
        pass

    def on_eof(self) -> None:
        pass
