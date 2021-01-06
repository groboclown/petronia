"""Intercepts events from a reader, to support events that the launcher handles
directly with the launched program."""

from typing import List, Callable, Optional
from petronia_common.event_stream import (
    BinaryReader, RawEvent,
    is_raw_event_binary,
)
from petronia_common.event_stream.reader import MarkedStreamReader, parse_raw_event


DO_NOT_BUBBLE_EVENT__KEEP_HANDLER = 1
BUBBLE_EVENT__KEEP_HANDLER = 2
DO_NOT_BUBBLE_EVENT__REMOVE_HANDLER = 3
BUBBLE_EVENT__REMOVE_HANDLER = 4
_REMOVE_HANDLER_RESPONSE = (
    DO_NOT_BUBBLE_EVENT__REMOVE_HANDLER,
    BUBBLE_EVENT__REMOVE_HANDLER,
)
_DO_NOT_BUBBLE_EVENT = (
    DO_NOT_BUBBLE_EVENT__REMOVE_HANDLER,
    DO_NOT_BUBBLE_EVENT__KEEP_HANDLER,
)

EventHandler = Callable[[Optional[RawEvent]], int]


class ReadStreamIntercept(BinaryReader):
    """A proxy on top of the underlying reader, to pull in events
    that are handled by the launcher and not routed outside of the
    launcher.

    FIXME the right way to handle this is through the router, to include a filter handler.
    """
    __slots__ = ('_buf', '_handlers', '_marked_stream', '_clone')

    def __init__(self, proxy: BinaryReader) -> None:
        self._clone = ClonedReader(proxy)
        self._marked_stream = MarkedStreamReader(self._clone)
        self._handlers: List[EventHandler] = []
        self._buf = bytearray()

    def read(self, max_read_size: int = -1) -> bytes:
        ret_data = b''
        remaining_size = max_read_size
        while max_read_size < 0 or remaining_size > 0:
            if len(self._buf) <= 0:
                raw_event, _error, eof = parse_raw_event(self._marked_stream)
                # Error is implicitly handled by the cloned stream.
                bubble = self.handle_event(raw_event)
                if bubble:
                    self._buf.extend(self._clone.fetch())
                # If not bubble, then don't allow the event's data to be passed on
                # to the caller.
                if eof and max_read_size < 0:
                    ret_data += self._buf
                    self._buf.clear()
                    return ret_data
            if max_read_size < 0:
                ret_data += bytes(self._buf)
                self._buf.clear()
            else:
                to_read = min(remaining_size, len(self._buf))
                ret_data += self._buf[:to_read]
                del self._buf[:to_read]
                remaining_size -= to_read
        return ret_data

    def add_handler(self, handler: EventHandler) -> None:
        """Add a new event handler."""
        self._handlers.append(handler)

    def handle_event(self, raw_event: Optional[RawEvent]) -> bool:
        """When a raw event is parsed, pass it to the handlers."""
        if raw_event and is_raw_event_binary(raw_event):
            # TODO This requires performing the full read across the handlers, and
            #   if there are no handlers, then to read all that data anyway.
            # Additionally, with the cloning, this becomes even more complex to
            # prevent a memory explosion.
            raise RuntimeError('Intercepting binary events is not yet supported.')
        removed_handlers: List[EventHandler] = []
        bubble = True
        for handler in self._handlers:
            resp = handler(raw_event)
            if bubble and resp in _DO_NOT_BUBBLE_EVENT:
                bubble = False
            if resp in _REMOVE_HANDLER_RESPONSE:
                removed_handlers.append(handler)
        for to_remove in removed_handlers:
            self._handlers.remove(to_remove)
        return bubble


class ClonedReader(BinaryReader):
    """Keeps a copy of what's read."""
    __slots__ = ('_proxy', 'value',)

    def __init__(self, stream: BinaryReader) -> None:
        self.value = bytearray()
        self._proxy = stream

    def read(self, max_read_size: int = -1) -> bytes:
        res = self._proxy.read(max_read_size)
        self.value.extend(res)
        return res

    def fetch(self) -> bytes:
        """Get the bytes that have been read, and clear out the buffer."""
        res = bytes(self.value)
        self.value.clear()
        return res
