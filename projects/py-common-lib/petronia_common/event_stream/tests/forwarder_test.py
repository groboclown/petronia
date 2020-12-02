
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
    write_object_event_to_stream,
    RawEvent,
    is_raw_event_binary,
    as_raw_event_binary_data_reader, as_raw_event_object_data,
    raw_event_id, raw_event_source_id, raw_event_target_id,
)
from ..reader import static_reader
from ..tests.reader_test import PACKET_MARKER, as_bin_str
from ...util import PetroniaReturnError, UserMessage, STANDARD_PETRONIA_CATALOG, i18n


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

    def test_pending_targets__eof(self) -> None:
        """Test how the code handles pending targets during EOF."""

        async def run_test() -> None:
            efp = AccessibleEventForwarder(create_read_stream(b''))
            self.assertTrue(efp.alive)
            target_1 = MockTarget(self)
            efp.add_target(target_1)
            efp.access__end_of_stream()
            target_1.assert_next_on_eof()
            target_1.assert_end()

        asyncio.run(run_test())

    def test_error_and_eof(self) -> None:
        """Generates a bad packet in the reader, and check that things are working."""
        target_1 = MockTarget(self)

        async def run_code() -> None:
            # Generate an incomplete packet to trigger an error.
            efp = AccessibleEventForwarder(create_read_stream(
                PACKET_MARKER +
                b'e' + as_bin_str('event-1') +
                b's' + as_bin_str('source-1')
            ))
            self.assertTrue(efp.alive)
            efp.add_target(target_1)
            await efp.handle_source()

            target_1.assert_next_on_error(UserMessage(
                STANDARD_PETRONIA_CATALOG, i18n('Reached end-of-stream during packet read'),
            ))
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

    def test_error_causes_remove(self) -> None:
        """Generates a bad packet in the reader, and check that an error causes a target
        to be removed, and thus causes targets to all be gone, and the stream handling to
        stop before EOF."""

        async def run_code() -> None:
            target_1 = MockTarget(self)
            target_1.on_error_returns.append(True)

            # Generate an incomplete packet to trigger an error.
            efp = AccessibleEventForwarder(create_read_stream(
                PACKET_MARKER +
                b'e' + as_bin_str('event-1') +
                b's' + as_bin_str('source-1') +
                b'x' +  # invalid character
                PACKET_MARKER +
                b'e' + as_bin_str('event-2') +
                b's' + as_bin_str('source-2') +
                b't' + as_bin_str('target-2') +
                b'[\0\0\1x'
            ))
            self.assertTrue(efp.alive)
            efp.add_target(target_1)
            await efp.handle_source()

            # The error should have triggered the target to be removed,
            # and not pick up other events.
            target_1.assert_next_on_error(UserMessage(
                STANDARD_PETRONIA_CATALOG, i18n('Unexpected data in the event stream'),
            ))
            target_1.assert_end()

            # Another packet is still pending, because EOF was not reached,
            # but there are no more targets registered, so the processing completed.
            self.assertTrue(efp.alive)

            # Ensure things are just fine when called again...
            efp.access__end_of_stream()

        asyncio.run(run_code())

    def test_filter_out_events(self) -> None:
        """Uses a global filter to eliminate packets from being consumed."""

        filter_stack: List[Tuple[str, str, str]] = []
        filter_order: List[bool] = [False, True]

        def filter_callback(event_id: str, source_id: str, target_id: str) -> bool:
            filter_stack.append((event_id, source_id, target_id,))
            return filter_order.pop(0)

        async def run_code() -> None:
            target_1 = MockTarget(self)
            inp_stream = SimpleBinaryWriter()
            await write_binary_event_to_stream(
                inp_stream, 'e1', 's1', 't1', 2, b'12',
            )
            await write_binary_event_to_stream(
                inp_stream, 'e2', 's2', 't2', 2, b'21',
            )
            efp = AccessibleEventForwarder(
                create_read_stream(inp_stream.getvalue()),
                filter_callback,
            )
            self.assertTrue(efp.alive)
            efp.add_target(target_1)
            await efp.handle_source()

            target_1.assert_next_can_handle('e1', 's1', 't1')
            target_1.assert_next_handle('e1', 's1', 't1', b'12')
            # The second event should have been filtered out.
            target_1.assert_next_on_eof()
            target_1.assert_end()

            self.assertFalse(efp.alive)

            # Ensure things are just fine when called again...
            efp.access__end_of_stream()

            # Now check the filtering calls.
            self.assertEqual([], filter_order)
            self.assertEqual(
                [
                    ('e1', 's1', 't1'),
                    ('e2', 's2', 't2'),
                ],
                filter_stack,
            )

        asyncio.run(run_code())

    def test_target_cant_handle(self) -> None:
        """Generates a bad packet in the reader, and check that things are working."""

        async def run_code() -> None:
            target_1 = MockTarget(self)
            target_1.can_handle_returns = [False, True]
            inp_stream = SimpleBinaryWriter()
            await write_binary_event_to_stream(
                inp_stream, 'e1', 's1', 't1', 2, b'12',
            )
            await write_binary_event_to_stream(
                inp_stream, 'e2', 's2', 't2', 2, b'21',
            )
            efp = AccessibleEventForwarder(create_read_stream(inp_stream.getvalue()))
            self.assertTrue(efp.alive)
            efp.add_target(target_1)
            await efp.handle_source()

            target_1.assert_next_can_handle('e1', 's1', 't1')
            # The first event was reported as can't handle, so it isn't consumed.
            target_1.assert_next_can_handle('e2', 's2', 't2')
            target_1.assert_next_handle('e2', 's2', 't2', b'21')
            target_1.assert_next_on_eof()
            target_1.assert_end()

            self.assertFalse(efp.alive)

            # Ensure things are just fine when called again...
            efp.access__end_of_stream()

        asyncio.run(run_code())

    def test_target_event_object(self) -> None:
        """Generates an object event with possible removal."""

        async def run_code() -> None:
            target_1 = MockTarget(self)
            target_1.handle_returns = [False, True]
            inp_stream = SimpleBinaryWriter()
            await write_object_event_to_stream(
                inp_stream, 'e1', 's1', 't1', {'x': 'y'},
            )
            await write_object_event_to_stream(
                inp_stream, 'e2', 's2', 't2', {'a': 'b'},
            )
            await write_object_event_to_stream(
                inp_stream, 'e3', 's3', 't3', {'1': '2'},
            )
            efp = AccessibleEventForwarder(create_read_stream(inp_stream.getvalue()))
            self.assertTrue(efp.alive)
            efp.add_target(target_1)
            await efp.handle_source()

            target_1.assert_next_can_handle('e1', 's1', 't1')
            target_1.assert_next_handle('e1', 's1', 't1', {'x': 'y'})
            target_1.assert_next_can_handle('e2', 's2', 't2')
            target_1.assert_next_handle('e2', 's2', 't2', {'a': 'b'})
            # This call should return True, which means that target is removed from the
            # list, which leaves no targets left, so the remaining event is not read
            # from the stream.
            target_1.assert_end()

            # The EOF was not encountered, so the reader is still alive.
            self.assertTrue(efp.alive)

            # Ensure things are just fine when called again...
            efp.access__end_of_stream()

        asyncio.run(run_code())

    def test_drain_events(self) -> None:
        """Ensure a binary event with no targets is appropriately drained."""

        async def run_code() -> None:
            target_1 = MockTarget(self)
            target_1.can_handle_returns = [False, False, True]
            inp_stream = SimpleBinaryWriter()
            await write_binary_event_to_stream(
                inp_stream, 'e1', 's1', 't1', 2, b'12',
            )
            await write_object_event_to_stream(
                inp_stream, 'e2', 's2', 't2', {'a': 'b'},
            )
            await write_object_event_to_stream(
                inp_stream, 'e3', 's3', 't3', {'x': 'y'},
            )
            efp = AccessibleEventForwarder(create_read_stream(inp_stream.getvalue()))
            self.assertTrue(efp.alive)
            efp.add_target(target_1)
            await efp.handle_source()

            target_1.assert_next_can_handle('e1', 's1', 't1')
            # the first event, the binary one, is not handled, so the handle call is not made.
            target_1.assert_next_can_handle('e2', 's2', 't2')
            # the second event is not handled, so the handle call is not made.
            target_1.assert_next_can_handle('e3', 's3', 't3')
            target_1.assert_next_handle('e3', 's3', 't3', {'x': 'y'})
            target_1.assert_next_on_eof()
            target_1.assert_end()

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

    def test_binary_to_remove(self) -> None:
        """Run with 1 binary target"""
        target_1 = MockTarget(self)
        target_1.handle_returns = [True]

        async def do_test() -> None:
            reader = static_reader(b'123')
            res = await forwarder.stream_forwarder(
                'e1', 's1', 't1', 3,
                reader, [target_1], 1,
            )
            self.assertEqual([target_1], res)
            self.assertEqual(b'', await reader(10))
            target_1.assert_next_handle('e1', 's1', 't1', b'123')
            target_1.assert_end()

        asyncio.run(do_test())


class StreamedBinaryReaderTest(unittest.TestCase):
    """Test the StreamedBinaryReader class"""

    def test_read_data__0_bytes(self) -> None:
        """Test the read_data method with a 0 argument."""
        async def run_test() -> None:
            condition = asyncio.Condition()
            reader = forwarder.StreamedBinaryReader(condition)
            reader.feed_data(b'123')
            res = await reader.read_data(0)
            self.assertEqual(b'', res)
            reader.feed_eof()
            res = await reader.read_data(0)
            self.assertEqual(b'', res)

        asyncio.run(run_test())

    def test_read_data__positive_bytes(self) -> None:
        """Test the read_data method with a requested number of bytes."""
        async def run_test() -> None:
            condition = asyncio.Condition()
            reader = forwarder.StreamedBinaryReader(condition)
            reader.feed_data(b'123')
            reader.feed_eof()
            res = await reader.read_data(1)
            self.assertEqual(b'1', res)
            res = await reader.read_data(16)
            self.assertEqual(b'23', res)
            res = await reader.read_data(16)
            self.assertEqual(b'', res)


        asyncio.run(run_test())


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

    # These aren't needed right now.
    # def access__error_listener(self, error: PetroniaReturnError) -> bool:
    #     """Access the method."""
    #     return self._error_listener(error)
    #
    # async def access__event_listener(self, event: RawEvent) -> bool:
    #     """Access the method."""
    #     return await self._event_listener(event)
