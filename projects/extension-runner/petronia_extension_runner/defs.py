"""
Basic definitions
"""
from petronia_common.event_stream import EventForwarder, EventForwarderTarget
from petronia_common.event_stream.thread_writer import ThreadSafeEventWriter


TRANSLATION_CATALOG = 'extension-runner'


class EventHandlerContext:
    """Simple context for an event handler."""
    __slots__ = ('__forwarder', '__writer',)

    def __init__(self, forwarder: EventForwarder, writer: ThreadSafeEventWriter) -> None:
        self.__forwarder = forwarder
        self.__writer = writer

    @property
    def writer(self) -> ThreadSafeEventWriter:
        """Get the writer."""
        return self.__writer

    def add_target(self, target: EventForwarderTarget) -> None:
        """Add a new target to the forwarder.  The target will receive new
        messages once the next event comes in, or if the stream is already
        at an end.  The `on_eof` function can be called immediately."""
        self.__forwarder.add_target(target)
