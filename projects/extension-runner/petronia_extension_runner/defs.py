"""
Basic definitions
"""
from typing import Sequence, Dict, Callable, Any
from petronia_common.event_stream import (
    EventForwarder, EventForwarderTarget, BinaryReader, BinaryWriter,
)
from petronia_common.event_stream.thread_writer import ThreadSafeEventWriter
from petronia_common.util import StdRet

TRANSLATION_CATALOG = 'extension-runner'


EntryPointFunctionType = Callable[
    [BinaryReader, BinaryWriter, Dict[str, Any], Sequence[str]],
    StdRet[None],
]


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
