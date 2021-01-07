"""Routes events based on event IDs to handlers."""

from petronia_common.event_stream import EventForwarder, BinaryReader, BinaryWriter
from petronia_common.event_stream.thread_stream import ThreadedStreamForwarder
from petronia_common.event_stream.thread_writer import ThreadSafeEventWriter
from .defs import EventHandlerContext
from .handlers.load_extension.factory import register_load_extension_handler


def create_router(reader: BinaryReader, outp: BinaryWriter) -> EventForwarder:
    """Create the event forwarder with the default event handlers registered."""
    writer = ThreadSafeEventWriter(outp)
    ret = EventForwarder(
        reader,
        ThreadedStreamForwarder(),
        None,
    )

    context = EventHandlerContext(ret, writer)
    register_load_extension_handler(context)

    return ret
