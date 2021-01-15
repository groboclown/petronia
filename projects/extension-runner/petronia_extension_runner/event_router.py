"""Routes events based on event IDs to handlers."""

from petronia_common.event_stream import EventForwarder, BinaryReader, BinaryWriter
from petronia_common.event_stream.thread_stream import ThreadedStreamForwarder
from petronia_common.event_stream.thread_writer import ThreadSafeEventWriter
from petronia_common.util import StdRet
from .defs import EventHandlerContext
from .handlers import register_run_extension_handler


def create_router(reader: BinaryReader, outp: BinaryWriter) -> StdRet[EventForwarder]:
    """Create the event forwarder with the default event handlers registered."""
    writer = ThreadSafeEventWriter(outp)
    ret = EventForwarder(
        reader,
        ThreadedStreamForwarder(),
        None,
    )

    context = EventHandlerContext(ret, writer)
    res = register_run_extension_handler(context)
    if res.has_error:
        return res.forward()

    return StdRet.pass_ok(ret)
