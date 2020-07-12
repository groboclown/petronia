
"""
Common stream test helpers.
"""

from typing import List, Tuple, Optional, Callable, Coroutine, Any, cast
import unittest
import asyncio
from .. import reader
from .. import consts
from ..defs import RawEvent
from ...util import PetroniaReturnError, T
from ...util.test_helpers import verified_not_none


class ConstSizeChanger:
    """Helper for changing the max size constants.  It allows tests to try out
    reaching those limits without needing to make really large test data values."""
    def __init__(self) -> None:
        """Constructor"""
        self.max_id = consts.MAX_ID_SIZE
        self.max_json = consts.MAX_JSON_SIZE
        self.max_blob = consts.MAX_BLOB_SIZE
        consts.MAX_ID_SIZE = 10
        consts.MAX_JSON_SIZE = 60
        consts.MAX_BLOB_SIZE = 10

    def tear_down(self) -> None:
        """Restores the values."""
        consts.MAX_ID_SIZE = self.max_id
        consts.MAX_JSON_SIZE = self.max_json
        consts.MAX_BLOB_SIZE = self.max_blob


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

    async def execute(self, data: bytes) -> None:
        """Runs the reader with the internal callback functions"""
        await reader.read_event_stream(
            create_read_stream(data),
            self.on_event, self.on_end_of_stream, self.on_error,
        )

    async def on_event(self, event: RawEvent) -> bool:
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


def create_read_stream(data: bytes) -> asyncio.StreamReader:
    """Create a stream reader that returns only the given bytes of data."""
    ret = asyncio.StreamReader()
    ret.feed_data(data)
    ret.feed_eof()
    return ret


def async_run_with_stream(
        data: bytes, func: Callable[[asyncio.StreamReader], Coroutine[Any, Any, T]]
) -> Tuple[T, bytes]:
    """Run a function that takes a StreamReader, using the data passed in,
    and returns the result."""
    async def run_it() -> Tuple[T, bytes]:
        stream = create_read_stream(data)
        res = await func(stream)
        rest = b''
        while not stream.at_eof():
            rest += await stream.read()  # pragma no cover
        return res, rest
    return asyncio.run(run_it())
