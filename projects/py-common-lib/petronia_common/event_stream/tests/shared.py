"""
Shared test constants, functions, and other definitions.
"""

from typing import List, Tuple, Dict, Optional, Any, cast
import unittest
import io
import threading
from .. import reader
from ..forwarder import EventForwarderTarget
from ..writer import write_binary_event_to_stream, write_object_event_to_stream
from ..defs import (
    RawEvent, RawBinaryReader, BinaryReader,
    is_raw_event_binary, raw_event_id, raw_event_source_id,
    raw_event_target_id, raw_event_binary_size, as_raw_event_binary_data_reader,
    as_raw_event_object_data,
)
from ...util import PetroniaReturnError, UserMessage
from ...util.test_helpers import verified_not_none

PACKET_MARKER = b'\0\0['


def as_bin_str(data: str) -> bytes:
    """Helper to convert a data string to a binary encoded length + bytes data"""
    ret = b''
    raw_data = data.encode('utf-8')
    count = len(raw_data)
    ret += bytes(bytearray(((count >> 8) & 0xff,)))
    ret += bytes(bytearray((count & 0xff,)))
    ret += raw_data
    return ret


class CallbackCollector:
    """Collects data and sends mocked responses for the standard
    callbacks to the read packet function."""
    actual: List[Tuple[Optional[RawEvent], Optional[PetroniaReturnError], bool]]
    event_responses: List[bool]
    error_responses: List[bool]

    def __init__(
            self,
            event_responses: Optional[List[bool]] = None,
            error_responses: Optional[List[bool]] = None,
    ) -> None:
        """Constructor"""
        self.actual = []
        self.event_responses = event_responses or []
        self.error_responses = error_responses or []

    def execute(self, data: bytes) -> None:
        """Runs the reader with the internal callback functions"""
        reader.read_event_stream(
            create_read_stream(data),
            self.on_event, self.on_end_of_stream, self.on_error,
        )

    def on_event(self, event: RawEvent) -> bool:
        """`event packet received` callback function"""
        self.actual.append((event, None, False,))
        ret = False
        if self.event_responses:
            ret = self.event_responses.pop(0)
        return ret

    def on_end_of_stream(self) -> None:
        """`end-of-stream` callback function"""
        self.actual.append((None, None, True,))

    def on_error(self, error: PetroniaReturnError) -> bool:
        """`error` callback function"""
        self.actual.append((None, error, False,))
        ret = False
        if self.error_responses:
            ret = self.error_responses.pop(0)
        return ret

    def next_as_raw_event(self, parent: unittest.TestCase) -> RawEvent:
        """Ensures the next callback was a raw event packet, and returns it."""
        parent.assertTrue(len(self.actual) > 0)
        next_actual = self.actual.pop(0)
        return cast(RawEvent, verified_not_none(next_actual[0], parent))

    def next_as_error(self, parent: unittest.TestCase) -> PetroniaReturnError:
        """Ensures the next callback was an error, and returns it."""
        parent.assertTrue(len(self.actual) > 0)
        next_actual = self.actual.pop(0)
        return verified_not_none(next_actual[1], parent)

    def next_as_eof(self, parent: unittest.TestCase) -> None:
        """Ensures the next callback was an EOF signal"""
        parent.assertEqual(len(self.actual), 1)
        next_actual = self.actual.pop(0)
        parent.assertTrue(next_actual[2])

    def is_empty(self) -> bool:
        """Are there any events left?"""
        return len(self.actual) <= 0


class SimpleBinaryWriter:
    """Simplest implementation of a binary writer."""
    def __init__(self) -> None:
        self.__value = b''

    def write(self, data: bytes) -> None:
        """Implement the binary writer protocol."""
        self.__value += data

    def getvalue(self) -> bytes:
        """Fetch the data written to this writer."""
        return self.__value


def create_read_stream(data: bytes) -> reader.BinaryReader:
    """Create a stream reader that returns only the given bytes of data."""
    return io.BytesIO(data)


def create_raw_reader(data: bytes) -> reader.RawBinaryReader:
    """Create a raw binary reader."""

    stream = io.BytesIO(data)

    def read(max_read_count: int = -1) -> bytes:
        return stream.read(max_read_count)

    return read


class MockTarget(EventForwarderTarget):
    """Mock up a target."""

    def __init__(self, test: unittest.TestCase) -> None:
        self.__test = test
        self.can_handle_returns: List[bool] = []
        self.on_error_returns: List[bool] = []
        self.handle_returns: List[bool] = []
        self.call_stack: List[Tuple[str, List[Any]]] = []

    def assert_next_can_handle(
            self,
            event_id: str, source_id: str, target_id: str,
    ) -> None:
        """Assertion"""
        self.__test.assertTrue(len(self.call_stack) > 0)
        name, args = self.call_stack.pop(0)
        self.__test.assertEqual('can_handle', name)
        self.__test.assertEqual(event_id, args[0])
        self.__test.assertEqual(source_id, args[1])
        self.__test.assertEqual(target_id, args[2])

    def can_consume(self, event_id: str, source_id: str, target_id: str) -> bool:
        """Callback"""
        print("== called can_handle")
        self.call_stack.append(('can_handle', [event_id, source_id, target_id]))
        if self.can_handle_returns:
            return self.can_handle_returns.pop(0)
        return True

    def assert_next_on_error(self, *messages: UserMessage) -> None:
        """Assertion"""
        self.__test.assertTrue(len(self.call_stack) > 0)
        name, args = self.call_stack.pop(0)
        self.__test.assertEqual('on_error', name)
        err = args[0]
        assert isinstance(err, PetroniaReturnError)
        self.__test.assertEqual(messages, err.messages())

    def on_error(self, error: PetroniaReturnError) -> bool:
        """Callback"""
        print("== called on_error")
        self.call_stack.append(('on_error', [error]))
        if self.on_error_returns:
            return self.on_error_returns.pop(0)
        return False

    def assert_next_on_eof(self) -> None:
        """Assertion"""
        self.__test.assertTrue(len(self.call_stack) > 0)
        name, _ = self.call_stack.pop(0)
        self.__test.assertEqual('on_eof', name)

    def on_eof(self) -> None:
        """Callback"""
        print("== called on_eof")
        self.call_stack.append(('on_eof', []))

    def assert_next_handle(
            self,
            event_id: str,
            source_id: str,
            target_id: str,
            data: Any,
    ) -> None:
        """Assertion"""
        self.__test.assertTrue(len(self.call_stack) > 0)
        name, args = self.call_stack.pop(0)
        self.__test.assertEqual('handle', name)
        self.__test.assertEqual(event_id, args[0])
        self.__test.assertEqual(source_id, args[1])
        self.__test.assertEqual(target_id, args[2])
        self.__test.assertEqual(data, args[3])

    def consume_object(
            self, event_id: str, source_id: str, target_id: str, event_data: Dict[str, Any],
    ) -> bool:
        self.call_stack.append(('handle', [event_id, source_id, target_id, event_data]))
        if self.handle_returns:
            return self.handle_returns.pop(0)
        return False

    def consume_binary(
            self, event_id: str, source_id: str, target_id: str, size: int,
            data_reader: RawBinaryReader,
    ) -> bool:
        data = b''
        last_read = b'x'
        while last_read != b'':
            last_read = data_reader(-1)
            data += last_read
        self.call_stack.append(('handle', [
            event_id,
            source_id,
            target_id,
            data,
        ]))
        if self.handle_returns:
            return self.handle_returns.pop(0)
        return False

    def assert_end(self) -> None:
        """Assertion"""
        self.__test.assertEqual([], self.call_stack)


def events_as_reader(*events: RawEvent) -> BinaryReader:
    """Create a reader that sends the argument events."""
    writer = SimpleBinaryWriter()
    for event in events:
        if is_raw_event_binary(event):
            write_binary_event_to_stream(
                writer,
                raw_event_id(event),
                raw_event_source_id(event),
                raw_event_target_id(event),
                raw_event_binary_size(event),
                as_raw_event_binary_data_reader(event),
            )
        else:
            write_object_event_to_stream(
                writer,
                raw_event_id(event),
                raw_event_source_id(event),
                raw_event_target_id(event),
                as_raw_event_object_data(event),
            )
    return create_read_stream(writer.getvalue())


class DelayedEofConditionBinaryReader:
    """A proxy binary reader that sends a condition when the data is fully read."""
    __slots__ = ('_proxy', '_broadcast', '_read_wait', 'timeout', 'bytes_read')

    def __init__(self, condition: threading.Condition, timeout: float = 200.0) -> None:
        self._proxy: Optional[BinaryReader] = None
        self._broadcast = condition
        self._read_wait = threading.Condition()
        self.bytes_read = 0
        self.timeout = timeout

    def send_events(self, *events: RawEvent) -> None:
        """Send events to the reader.  Can only be called once."""
        with self._read_wait:
            assert self._proxy is None
            self._proxy = events_as_reader(*events)
            self._read_wait.notify_all()

    def read(self, max_read_size: int = -1) -> bytes:
        """Implementation of the BinaryReader read."""
        with self._read_wait:
            if not self._proxy:
                self._read_wait.wait(timeout=self.timeout)
        assert self._proxy is not None
        with self._broadcast:
            ret = self._proxy.read(max_read_size)
            self.bytes_read += len(ret)
            # print(f"reader: read {self.bytes_read} bytes so far")
            if not ret:
                self._broadcast.notify_all()
        return ret
