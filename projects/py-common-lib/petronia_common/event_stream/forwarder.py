
"""
A streaming reader that forks the read to many streams.

This is very similar behavior to the tio version, but due to the nature of
asyncio, it has nuances that must be distinct.
"""

from typing import List, Callable, Protocol, Optional

from .reader import BinaryReader, read_event_stream
from .defs import (
    RawEvent, RawBinaryReader,
    raw_event_id, raw_event_source_id, raw_event_target_id,
    raw_event_binary_size,
    is_raw_event_object, is_raw_event_binary,
    as_raw_event_binary_data_reader,
)
from ..util import PetroniaReturnError, EMPTY_LIST


READ_SIZE_LIMIT = 4 * 1024


class EventForwarderTarget:
    """Interface for targets of events."""
    __slots__ = ()

    def can_consume(self, event_id: str, source_id: str, target_id: str) -> bool:
        """Can this target handle the given event?"""
        raise NotImplementedError()  # pragma no cover

    def on_error(self, error: PetroniaReturnError) -> bool:
        """Handler for stream errors.  If this returns True, then
        the target is de-registered."""
        raise NotImplementedError()  # pragma no cover

    def on_eof(self) -> None:
        """Called when the stream is closed.  The target will no longer be
        used by the forwarder."""
        raise NotImplementedError()  # pragma no cover

    def consume(self, event: RawEvent) -> bool:
        """Called if the `can_consume` method returns True.
        If this returns True, then the target will be de-registered."""
        raise NotImplementedError()  # pragma no cover


class BinaryEventStreamForwarder(Protocol):
    """Forwards a binary event to 1 or more targets.
    It needs to read in a bit of data (up to the read_size),
    pass that on to each of the targets' readers, wait for those
    targets to finish consuming that data, then repeat until the
    data is fully processed."""
    def __call__(  # pylint: disable=too-many-arguments
        self,
        event_id: str,
        source_id: str,
        target_id: str,
        blob_size: int,
        reader: RawBinaryReader,
        targets: List[EventForwarderTarget],
        read_size: int,
    ) -> List[EventForwarderTarget]: ...


class EventForwarder:
    """
    Reads in packets from the source, and passes them to the targets.

    It's designed to not pass partial data to the targets.
    """
    # The read() methods are indirectly wrapped into an async wait to the StreamReader source,
    # so there is no reason to explicitly call an await on the read functions.
    __slots__ = (
        '__source', '__targets', '__pending_targets', '__filter', '__alive', '__forwarder',
    )

    def __init__(
            self, source: BinaryReader,
            stream_forwarder: BinaryEventStreamForwarder,
            event_filter: Optional[Callable[[str, str, str], bool]] = None,
    ) -> None:
        self.__source = source
        self.__filter = event_filter
        self.__targets: List[EventForwarderTarget] = []
        self.__pending_targets: List[EventForwarderTarget] = []
        self.__alive = True
        self.__forwarder = stream_forwarder

    @property
    def alive(self) -> bool:
        """Is this forwarder still running?"""
        return self.__alive

    def add_target(self, target: EventForwarderTarget) -> None:
        """Add a new target to the forwarder.  The target will receive new
        messages once the next event comes in, or if the stream is already
        at an end.  The `on_eof` function can be called immediately."""
        if not self.__alive:
            target.on_eof()
        else:
            self.__pending_targets.append(target)

    def handle_source(self) -> None:
        """Background pipe reader and forwarder to all the targets."""
        self._manage_targets(EMPTY_LIST)
        read_event_stream(
            self.__source,
            self._event_listener,
            self._end_of_stream,
            self._error_listener,
        )

    def _end_of_stream(self) -> None:
        if self.__alive:
            self.__alive = False
            for target in self.__targets:
                target.on_eof()
            for target in self.__pending_targets:
                target.on_eof()
            self.__targets.clear()
            self.__pending_targets.clear()

    def _error_listener(self, error: PetroniaReturnError) -> bool:
        assert self.__alive
        to_remove: List[EventForwarderTarget] = []
        for target in self.__targets:
            if target.on_error(error):
                to_remove.append(target)
        return self._manage_targets(to_remove)

    def _event_listener(self, event: RawEvent) -> bool:
        assert self.__alive
        event_id = raw_event_id(event)
        source_id = raw_event_source_id(event)
        target_id = raw_event_target_id(event)
        to_remove: List[EventForwarderTarget] = []
        to_call: List[EventForwarderTarget] = []

        if self.__filter and self.__filter(event_id, source_id, target_id):
            return self._manage_targets([])

        for target in self.__targets:
            if target.can_consume(event_id, source_id, target_id):
                to_call.append(target)
        if to_call:
            to_remove = self._send_event(event, to_call)
        else:
            # No targets for this event.  So the event reader needs to
            # be drained.
            EventForwarder._drain_event(event)
        return self._manage_targets(to_remove)

    def _send_event(
            self, event: RawEvent, targets: List[EventForwarderTarget],
    ) -> List[EventForwarderTarget]:
        assert self.__alive
        to_remove: List[EventForwarderTarget] = []
        event_id = raw_event_id(event)
        event_source_id = raw_event_source_id(event)
        event_target_id = raw_event_target_id(event)

        if is_raw_event_object(event):
            # Simple handling, because the data is already fully read.
            for target in self.__targets:
                if target.consume(event):
                    to_remove.append(target)
        else:
            # Binary object.  This is more complicated.  We must forward the
            # event to each target, but in a memory safe way.
            to_remove = self.__forwarder(
                event_id,
                event_source_id,
                event_target_id,
                raw_event_binary_size(event),
                as_raw_event_binary_data_reader(event),
                targets,
                READ_SIZE_LIMIT,
            )
        return to_remove

    @staticmethod
    def _drain_event(event: RawEvent) -> None:
        if is_raw_event_binary(event):
            reader = as_raw_event_binary_data_reader(event)
            # Loop until we receive 0 bytes from the reader.
            # We do not pass in a size limit, because that should already
            # be set optimally by the reader.
            while len(reader()) > 0:
                pass
        # The other type is already fully read.

    def _manage_targets(self, removed: List[EventForwarderTarget]) -> bool:
        # Don't need to be alive to call this...
        new_targets: List[EventForwarderTarget] = []
        for target in self.__targets:
            if target not in removed:
                new_targets.append(target)
        new_targets.extend(self.__pending_targets)
        self.__pending_targets.clear()
        self.__targets = new_targets
        # Return True if there are no more targets to process the stream.
        return not self.__targets
