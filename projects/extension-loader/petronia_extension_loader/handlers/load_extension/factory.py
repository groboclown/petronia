"""Process for loading an extension."""

from petronia_common.event_stream import EventForwarderTarget
from ...defs import EventHandlerContext


def register_load_extension_handler(context: EventHandlerContext) -> None:
    """Create the event target for loading extension requests."""
