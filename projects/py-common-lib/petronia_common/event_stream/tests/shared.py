"""
Shared test constants, functions, and other definitions.
"""

from typing import List, Tuple, Optional, cast
import unittest
import io
from .. import reader
from ..defs import RawEvent
from ...util import PetroniaReturnError
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
