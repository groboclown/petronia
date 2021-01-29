
"""
Test the forwarder module.
"""

from typing import List, Tuple
import unittest
import threading
from concurrent.futures import ThreadPoolExecutor
from .. import thread_stream
from .shared import (
    SimpleBinaryWriter, MockTarget,
    create_read_stream, create_raw_reader, as_bin_str,
    PACKET_MARKER,
)
from ..reader import static_reader
from ..writer import (
    write_binary_event_to_stream,
    write_object_event_to_stream,
)
from ..forwarder import EventForwarder, BaseEventForwarderTarget
from .. import RawEvent
from ...util import UserMessage, STANDARD_PETRONIA_CATALOG, i18n
from ...util.error import SimplePetroniaReturnError


class EventForwarderTest(unittest.TestCase):
    """
    Test the EventForwarder class.
    """

    def test_no_events_and_eof(self) -> None:
        """No events in the reader, and check that things are working."""
        target_1 = MockTarget(self)

        inp_stream = SimpleBinaryWriter()
        write_binary_event_to_stream(
            inp_stream, 'e1', 's1', 't1', 2, b'12',
        )
        efp = AccessibleEventForwarder(
            create_read_stream(inp_stream.getvalue()),
            thread_stream.ThreadedStreamForwarder(),
        )
        self.assertTrue(efp.alive)
        efp.add_target(target_1)
        efp.handle_source()

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

    def test_pending_targets__eof(self) -> None:
        """Test how the code handles pending targets during EOF."""

        efp = AccessibleEventForwarder(
            create_read_stream(b''),
            thread_stream.ThreadedStreamForwarder(),
        )
        self.assertTrue(efp.alive)
        target_1 = MockTarget(self)
        efp.add_target(target_1)
        efp.access__end_of_stream()
        target_1.assert_next_on_eof()
        target_1.assert_end()

    def test_error_and_eof(self) -> None:
        """Generates a bad packet in the reader, and check that things are working."""
        target_1 = MockTarget(self)

        # Generate an incomplete packet to trigger an error.
        efp = AccessibleEventForwarder(create_read_stream(
            PACKET_MARKER +
            b'e' + as_bin_str('event-1') +
            b's' + as_bin_str('source-1')
        ), thread_stream.ThreadedStreamForwarder())
        self.assertTrue(efp.alive)
        efp.add_target(target_1)
        efp.handle_source()

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

    def test_error_causes_remove(self) -> None:
        """Generates a bad packet in the reader, and check that an error causes a target
        to be removed, and thus causes targets to all be gone, and the stream handling to
        stop before EOF."""

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
        ), thread_stream.ThreadedStreamForwarder())
        self.assertTrue(efp.alive)
        efp.add_target(target_1)
        efp.handle_source()

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

    def test_filter_out_events(self) -> None:
        """Uses a global filter to eliminate packets from being consumed."""

        filter_stack: List[Tuple[str, str, str]] = []
        filter_order: List[bool] = [False, True]

        def filter_callback(event_id: str, source_id: str, target_id: str, _vt: RawEvent) -> bool:
            filter_stack.append((event_id, source_id, target_id))
            return filter_order.pop(0)

        target_1 = MockTarget(self)
        inp_stream = SimpleBinaryWriter()
        write_binary_event_to_stream(
            inp_stream, 'e1', 's1', 't1', 2, b'12',
        )
        write_binary_event_to_stream(
            inp_stream, 'e2', 's2', 't2', 2, b'21',
        )
        efp = AccessibleEventForwarder(
            create_read_stream(inp_stream.getvalue()),
            thread_stream.ThreadedStreamForwarder(),
            filter_callback,
        )
        self.assertTrue(efp.alive)
        efp.add_target(target_1)
        efp.handle_source()

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

    def test_multiple_callbacks_filtered(self) -> None:
        """Register multiple targets but only one is called."""

        target_1 = MockTarget(self)
        target_1.can_handle_returns.extend([True, True])
        target_1.handle_returns.extend([False, False])
        target_2 = MockTarget(self)
        target_2.can_handle_returns.extend([False, False])

        inp_stream = SimpleBinaryWriter()
        # Write event as binary
        write_binary_event_to_stream(
            inp_stream, 'e1', 's1', 't1', 2, b'12',
        )
        write_object_event_to_stream(
            inp_stream, 'e2', 's2', 't2', {'x': 'y'},
        )
        efp = AccessibleEventForwarder(
            create_read_stream(inp_stream.getvalue()),
            thread_stream.ThreadedStreamForwarder(),
        )
        self.assertTrue(efp.alive)
        efp.add_target(target_1)
        efp.add_target(target_2)
        efp.handle_source()

        target_1.assert_next_can_handle('e1', 's1', 't1')
        target_2.assert_next_can_handle('e1', 's1', 't1')
        target_1.assert_next_handle('e1', 's1', 't1', b'12')
        # The first event should have not been handled by the second target.
        target_1.assert_next_can_handle('e2', 's2', 't2')
        target_2.assert_next_can_handle('e2', 's2', 't2')
        target_1.assert_next_handle('e2', 's2', 't2', {'x': 'y'})
        # The second event should have not been handled by the second target.
        target_1.assert_next_on_eof()
        target_2.assert_next_on_eof()
        target_1.assert_end()
        target_2.assert_end()

        self.assertFalse(efp.alive)

        # Ensure things are just fine when called again...
        efp.access__end_of_stream()

    def test_target_cant_handle(self) -> None:
        """Generates a bad packet in the reader, and check that things are working."""

        target_1 = MockTarget(self)
        target_1.can_handle_returns = [False, True]
        inp_stream = SimpleBinaryWriter()
        write_binary_event_to_stream(
            inp_stream, 'e1', 's1', 't1', 2, b'12',
        )
        write_binary_event_to_stream(
            inp_stream, 'e2', 's2', 't2', 2, b'21',
        )
        efp = AccessibleEventForwarder(
            create_read_stream(inp_stream.getvalue()),
            thread_stream.ThreadedStreamForwarder(),
        )
        self.assertTrue(efp.alive)
        efp.add_target(target_1)
        efp.handle_source()

        target_1.assert_next_can_handle('e1', 's1', 't1')
        # The first event was reported as can't handle, so it isn't consumed.
        target_1.assert_next_can_handle('e2', 's2', 't2')
        target_1.assert_next_handle('e2', 's2', 't2', b'21')
        target_1.assert_next_on_eof()
        target_1.assert_end()

        self.assertFalse(efp.alive)

        # Ensure things are just fine when called again...
        efp.access__end_of_stream()

    def test_target_event_object(self) -> None:
        """Generates an object event with possible removal."""

        target_1 = MockTarget(self)
        target_1.handle_returns = [False, True]
        inp_stream = SimpleBinaryWriter()
        write_object_event_to_stream(
            inp_stream, 'e1', 's1', 't1', {'x': 'y'},
        )
        write_object_event_to_stream(
            inp_stream, 'e2', 's2', 't2', {'a': 'b'},
        )
        write_object_event_to_stream(
            inp_stream, 'e3', 's3', 't3', {'1': '2'},
        )
        efp = AccessibleEventForwarder(
            create_read_stream(inp_stream.getvalue()),
            thread_stream.ThreadedStreamForwarder(),
        )
        self.assertTrue(efp.alive)
        efp.add_target(target_1)
        efp.handle_source()

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

    def test_drain_events(self) -> None:
        """Ensure a binary event with no targets is appropriately drained."""

        target_1 = MockTarget(self)
        target_1.can_handle_returns = [False, False, True]
        inp_stream = SimpleBinaryWriter()
        write_binary_event_to_stream(
            inp_stream, 'e1', 's1', 't1', 2, b'12',
        )
        write_object_event_to_stream(
            inp_stream, 'e2', 's2', 't2', {'a': 'b'},
        )
        write_object_event_to_stream(
            inp_stream, 'e3', 's3', 't3', {'x': 'y'},
        )
        efp = AccessibleEventForwarder(
            create_read_stream(inp_stream.getvalue()),
            thread_stream.ThreadedStreamForwarder(ThreadPoolExecutor(12)),
        )
        self.assertTrue(efp.alive)
        efp.add_target(target_1)
        efp.handle_source()

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


class StreamForwarderTest(unittest.TestCase):
    """
    Test the permutations on the stream_forwarder function
    and its dependent StreamedBinaryReader class.
    """

    def test_no_targets(self) -> None:
        """Invoke with no targets."""
        reader = static_reader(b'123')
        res = thread_stream.ThreadedStreamForwarder()(
            'e1', 's1', 't1', 3,
            reader, [], 10,
        )
        self.assertEqual([], res)
        self.assertEqual(b'', reader(10))

    def test_one_binary_target(self) -> None:
        """Run with 1 binary target"""
        target_1 = MockTarget(self)

        reader = static_reader(b'123')
        res = thread_stream.ThreadedStreamForwarder()(
            'e1', 's1', 't1', 3,
            reader, [target_1], 1,
        )
        self.assertEqual([], res)
        self.assertEqual(b'', reader(10))
        target_1.assert_next_handle('e1', 's1', 't1', b'123')
        target_1.assert_end()

    def test_two_binary_targets(self) -> None:
        """Run with 2 binary targets"""
        target_1 = MockTarget(self)
        target_2 = MockTarget(self)

        reader = static_reader(b'123')
        res = thread_stream.ThreadedStreamForwarder()(
            'e1', 's1', 't1', 3,
            reader, [target_1, target_2], 1,
        )
        self.assertEqual([], res)
        self.assertEqual(b'', reader(10))
        target_1.assert_next_handle('e1', 's1', 't1', b'123')
        target_1.assert_end()
        target_2.assert_next_handle('e1', 's1', 't1', b'123')
        target_2.assert_end()

    def test_binary_to_remove(self) -> None:
        """Run with 1 binary target"""
        target_1 = MockTarget(self)
        target_1.handle_returns = [True]

        reader = static_reader(b'123')
        res = thread_stream.ThreadedStreamForwarder()(
            'e1', 's1', 't1', 3,
            reader, [target_1], 1,
        )
        self.assertEqual([target_1], res)
        self.assertEqual(b'', reader(10))
        target_1.assert_next_handle('e1', 's1', 't1', b'123')
        target_1.assert_end()


class StreamedBinaryReaderTest(unittest.TestCase):
    """Test the StreamedBinaryReader class"""

    def test_read_data__0_bytes(self) -> None:
        """Test the read_data method with a 0 argument."""
        condition = threading.Condition()
        reader = thread_stream.StreamedBinaryReader(condition)
        reader.feed_data(b'123')
        res = reader.read_data(0)
        self.assertEqual(b'', res)
        reader.feed_eof()
        res = reader.read_data(0)
        self.assertEqual(b'', res)

    def test_read_data__positive_bytes(self) -> None:
        """Test the read_data method with a requested number of bytes."""
        condition = threading.Condition()
        reader = thread_stream.StreamedBinaryReader(condition)
        reader.feed_data(b'123')
        reader.feed_eof()
        res = reader.read_data(1)
        self.assertEqual(b'1', res)
        res = reader.read_data(16)
        self.assertEqual(b'23', res)
        res = reader.read_data(16)
        self.assertEqual(b'', res)


class BaseEventForwarderTargetTest(unittest.TestCase):
    """Test the BaseEventForwarderTarget class."""

    def test_on_error__on_eof(self) -> None:
        """Test the on_error and on_eof methods."""
        target = BaseEventForwarderTarget()
        self.assertFalse(target.on_error(SimplePetroniaReturnError()))
        # Nothing really to do here but ensure this call doesn't fail.
        target.on_eof()

    def test_consume_object(self) -> None:
        """Test the consume_object method"""
        target = BaseEventForwarderTarget()
        self.assertFalse(target.consume_object('x', 'y', 'z', {}))

    def test_consume_binary(self) -> None:
        """Test the consume_binary method"""
        reader = create_raw_reader(b'123456')
        target = BaseEventForwarderTarget()
        self.assertFalse(target.consume_binary('x', 'y', 'z', 4, reader))
        self.assertEqual(b'56', reader())


class AccessibleEventForwarder(EventForwarder):
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
