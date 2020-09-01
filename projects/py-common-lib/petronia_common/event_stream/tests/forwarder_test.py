
"""
Test the forwarder module.
"""

from typing import List, Tuple, Any
import unittest
import asyncio
from .util import create_read_stream, SimpleBinaryWriter
from .. import (
    forwarder,
    write_binary_event_to_stream,
    RawEvent,
    is_raw_event_binary,
    as_raw_event_binary_data_reader, as_raw_event_object_data,
    raw_event_id, raw_event_source_id, raw_event_target_id,
)
from ..reader import static_reader
from ...util import PetroniaReturnError, UserMessage


class EventForwarderTest(unittest.TestCase):
    """
    Test the EventForwarder class.
    """

    def test_no_events_and_eof(self) -> None:
        """No events in the reader, and check that things are working."""
        target_1 = MockTarget(self)

        async def run_code() -> None:
            inp_stream = SimpleBinaryWriter()
            await write_binary_event_to_stream(
                inp_stream, 'e1', 's1', 't1', 2, b'12',
            )
            efp = AccessibleEventForwarder(create_read_stream(inp_stream.getvalue()))
            self.assertTrue(efp.alive)
            efp.add_target(target_1)
            await efp.handle_source()

            target_1.assert_next_can_handle('e1', 's1', 't1')
            target_1.assert_next_handle('e1', 's1', 't1', b'12')
            target_1.assert_next_on_eof()
            target_1.assert_end()

            target_2 = MockTarget(self)
            efp.add_target(target_2)
            target_2.assert_next_on_eof()
            target_2.assert_end()

            self.assertFalse(efp.alive)

            # Ensure things are just fine when called again...
            efp.access__end_of_stream()


        asyncio.run(run_code())


class StreamForwarderTest(unittest.TestCase):
    """
    Test the permutations on the stream_forwarder function
    and its dependent StreamedBinaryReader class.
    """

    def test_no_targets(self) -> None:
        """Invoke with no targets."""
        async def do_test() -> None:
            reader = static_reader(b'123')
            res = await forwarder.stream_forwarder(
                'e1', 's1', 't1', 3,
                reader, [], 10,
            )
            self.assertEqual([], res)
            self.assertEqual(b'', await reader(10))

        asyncio.run(do_test())

    def test_one_binary_target(self) -> None:
        """Run with 1 binary target"""
        target_1 = MockTarget(self)

        async def do_test() -> None:
            reader = static_reader(b'123')
            res = await forwarder.stream_forwarder(
                'e1', 's1', 't1', 3,
                reader, [target_1], 1,
            )
            self.assertEqual([], res)
            self.assertEqual(b'', await reader(10))
            target_1.assert_next_handle('e1', 's1', 't1', b'123')
            target_1.assert_end()

        asyncio.run(do_test())

    def test_two_binary_targets(self) -> None:
        """Run with 2 binary targets"""
        target_1 = MockTarget(self)
        target_2 = MockTarget(self)

        async def do_test() -> None:
            reader = static_reader(b'123')
            res = await forwarder.stream_forwarder(
                'e1', 's1', 't1', 3,
                reader, [target_1, target_2], 1,
            )
            self.assertEqual([], res)
            self.assertEqual(b'', await reader(10))
            target_1.assert_next_handle('e1', 's1', 't1', b'123')
            target_1.assert_end()
            target_2.assert_next_handle('e1', 's1', 't1', b'123')
            target_2.assert_end()

        asyncio.run(do_test())


class MockTarget(forwarder.EventForwarderTarget):
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

    async def consume(self, event: RawEvent) -> bool:
        """Callback"""
        print("== called handle")
        if is_raw_event_binary(event):
            stream_reader = as_raw_event_binary_data_reader(event)
            print("== == reading data")
            data = b''
            last_read = b'x'
            while last_read != b'':
                last_read = await stream_reader(-1)
                data += last_read
            self.call_stack.append(('handle', [
                raw_event_id(event),
                raw_event_source_id(event),
                raw_event_target_id(event),
                data,
            ]))
        else:
            self.call_stack.append(('handle', [
                raw_event_id(event),
                raw_event_source_id(event),
                raw_event_target_id(event),
                as_raw_event_object_data(event),
            ]))

        if self.handle_returns:
            return self.handle_returns.pop(0)
        return False

    def assert_end(self) -> None:
        """Assertion"""
        self.__test.assertEqual([], self.call_stack)


class AccessibleEventForwarder(forwarder.EventForwarder):
    """Accessible method version of the event forwarder."""
    def access__end_of_stream(self) -> None:
        """Access the method."""
        self._end_of_stream()

    def access__error_listener(self, error: PetroniaReturnError) -> bool:
        """Access the method."""
        return self._error_listener(error)

    async def access__event_listener(self, event: RawEvent) -> bool:
        """Access the method."""
        return await self._event_listener(event)
