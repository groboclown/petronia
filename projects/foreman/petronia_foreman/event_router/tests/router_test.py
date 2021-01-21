"""Test the router module."""

from typing import Tuple
import unittest
import threading
from concurrent.futures import ThreadPoolExecutor
from petronia_common.event_stream import (
    BinaryWriter, BinaryReader, RawEvent,
    to_raw_event_object, to_raw_event_binary, read_event_stream,
)
from petronia_common.event_stream.tests.shared import (
    create_read_stream, create_raw_reader,
    SimpleBinaryWriter, MockTarget, DelayedEofConditionBinaryReader, CallbackCollector,
)
from petronia_common.util import (
    StdRet, PetroniaReturnError, UserMessage,
    i18n, join_errors,
)
from petronia_common.util.message import USER_MESSAGE_CATALOG_EXCEPTION
from .. import router
from ..channel import EventFilterResult


class OnCloseTargetTest(unittest.TestCase):
    """Tests the OnCloseTarget class"""
    def setUp(self) -> None:
        self.count = [0]

    def _callback(self) -> None:
        self.count[0] += 1

    def test_on_eof(self) -> None:
        """Run the on_eof method."""
        target = router.OnCloseTarget(self._callback)
        target.on_eof()
        self.assertEqual(1, self.count[0])

    def test_can_consume(self) -> None:
        """Run the can_consume method."""
        target = router.OnCloseTarget(self._callback)
        self.assertFalse(target.can_consume('x', 'y', 'z'))
        self.assertEqual(0, self.count[0])

    def test_on_error(self) -> None:
        """Run the on_error method."""
        target = router.OnCloseTarget(self._callback)
        self.assertFalse(target.on_error(PetroniaReturnError()))
        self.assertEqual(0, self.count[0])

    def test_consume(self) -> None:
        """Run the consume method."""
        target = router.OnCloseTarget(self._callback)

        res = target.consume_object('x', 'y', 'z', {})
        self.assertFalse(res)
        self.assertEqual(0, self.count[0])


class EventRouterTest(unittest.TestCase):
    """Tests the router basic functionality."""

    def test_register_channel__blocked(self) -> None:
        """Test register_channel when the registration callback blocks it."""

        def create_reader_writer() -> StdRet[Tuple[BinaryReader, BinaryWriter]]:
            raise Exception('Should not be called')  # pragma no cover

        executor = ThreadPoolExecutor()
        lock = threading.Semaphore()
        event_router = router.EventRouter(lock, executor=executor)
        event_router.add_reservation_callback('ch', lambda _: StdRet.pass_errmsg(
            'x', i18n('expected error'),
        ))
        res = event_router.register_channel('ch', create_reader_writer)
        self.assertTrue(res.has_error)
        self.assertEqual(
            'expected error',
            res.valid_error.messages()[0].message,
        )

    def test_register_channel__error(self) -> None:
        """Test register_channel when the registration callback fails."""
        expected_messages = (UserMessage('x', i18n('y')),)

        def create_reader_writer_error() -> StdRet[Tuple[BinaryReader, BinaryWriter]]:
            return StdRet.pass_error(join_errors(*expected_messages))

        lock = threading.Semaphore()
        event_router = router.EventRouter(lock)
        res = event_router.register_channel('ch', create_reader_writer_error)
        self.assertIsNotNone(res.error)
        self.assertEqual(
            expected_messages,
            res.valid_error.messages(),
        )
        self.assertEqual(
            (),
            tuple(event_router.get_registered_channel_names()),
        )

        # Ensure it can still be registered again if it doesn't fail.
        res = event_router.register_channel('ch', _create_reader_writer_ok)
        self.assertIsNone(res.error)
        self.assertEqual(
            ('ch',),
            tuple(event_router.get_registered_channel_names()),
        )

    def test_register_channel__with_target(self) -> None:
        """Test register_channel when the registration callback fails."""
        condition = threading.Condition()
        reader = DelayedEofConditionBinaryReader(condition)

        def create_reader_writer() -> StdRet[Tuple[BinaryReader, BinaryWriter]]:
            return StdRet.pass_ok((
                # The channel will receive data...
                reader,
                SimpleBinaryWriter(),
            ))

        executor = ThreadPoolExecutor()
        lock = threading.Semaphore()
        target = MockTarget(self)
        target.can_handle_returns.append(True)
        target.handle_returns.append(False)
        event_router = router.EventRouter(lock, executor=executor, target=target)
        res = event_router.register_channel('ch', create_reader_writer)
        self.assertIsNone(res.error)
        self.assertEqual(
            ('ch',),
            tuple(event_router.get_registered_channel_names()),
        )
        res = event_router.add_handler('ch', 'h1', ['e1'], [])
        self.assertIsNone(res.error)
        reader.send_events(
            to_raw_event_object('e1', 's1', 't1', {'x': 'y'}),
            to_raw_event_binary('e1', 's2', 't2', 2, create_raw_reader(b'ab')),
        )
        # wait for the thread reader to stop
        with condition:
            condition.wait(2.0)
        executor.shutdown(wait=True)
        target.assert_next_can_handle('e1', 's1', 't1')
        target.assert_next_handle('e1', 's1', 't1', {'x': 'y'})
        target.assert_next_can_handle('e1', 's2', 't2')
        target.assert_next_handle('e1', 's2', 't2', b'ab')
        target.assert_next_on_eof()
        target.assert_end()

    def test_close_channel__unregistered(self) -> None:
        """Test close_channel when the channel name is not registered."""
        lock = threading.Semaphore()
        event_router = router.EventRouter(lock)
        ret = event_router.close_channel('ch')
        self.assertFalse(ret)

    def test_close_channel__registered(self) -> None:
        """Test register_channel when the registration callback blocks it."""
        lock = threading.Semaphore()
        event_router = router.EventRouter(lock)
        res = event_router.register_channel('ch', _create_reader_writer_ok)
        self.assertIsNone(res.error)
        ret = event_router.close_channel('ch')
        self.assertTrue(ret)
        self.assertEqual((), tuple(event_router.get_registered_channel_names()))

    def test_get_channel_for_handler__exists(self) -> None:
        """Test get_channel_for_handler where the handler is registered."""
        lock = threading.Semaphore()
        event_router = router.EventRouter(lock)
        self.assertEqual((), tuple(event_router.get_registered_channel_names()))
        res = event_router.register_channel('ch', _create_reader_writer_ok)
        self.assertIsNone(res.error)
        self.assertEqual(('ch',), tuple(event_router.get_registered_channel_names()))
        res = event_router.add_handler('ch', 'hd', [], [])
        self.assertIsNone(res.error)
        ch_name = event_router.get_channel_for_handler('hd')
        self.assertEqual('ch', ch_name)

    def test_get_channel_for_handler__not_exists(self) -> None:
        """Test get_channel_for_handler where the handler is not registered, but others are."""
        lock = threading.Semaphore()
        event_router = router.EventRouter(lock)
        res = event_router.register_channel('ch', _create_reader_writer_ok)
        self.assertIsNone(res.error)
        res = event_router.add_handler('ch', 'hd', [], [])
        self.assertIsNone(res.error)
        ch_name = event_router.get_channel_for_handler('hd1')
        self.assertIsNone(ch_name)

    def test_get_channel_for_handler__empty(self) -> None:
        """Test get_channel_for_handler where no channels are registered."""

        lock = threading.Semaphore()
        event_router = router.EventRouter(lock)
        ch_name = event_router.get_channel_for_handler('hd1')
        self.assertIsNone(ch_name)

    def test_add_handler__duplicate(self) -> None:
        """Test add_handler with a duplicate ID."""
        lock = threading.Semaphore()
        event_router = router.EventRouter(lock)
        res = event_router.register_channel('ch1', _create_reader_writer_ok)
        self.assertIsNone(res.error)
        res = event_router.add_handler('ch1', 'h1', [], [])
        self.assertIsNone(res.error)
        res = event_router.add_handler('ch1', 'h1', [], [])
        self.assertIsNotNone(res.error)
        res = event_router.register_channel('ch2', _create_reader_writer_ok)
        self.assertIsNone(res.error)
        # the handler ID should be unique across channels.
        res = event_router.add_handler('ch1', 'h1', [], [])
        self.assertIsNotNone(res.error)

        # Removing the handler, though, allows for the other channel to add it.
        self.assertTrue(event_router.remove_handler('h1'))
        res = event_router.add_handler('ch1', 'h1', [], [])
        self.assertIsNone(res.error)

    def test_add_handler__no_channel(self) -> None:
        """Test add_handler with a not-registered channel."""
        lock = threading.Semaphore()
        event_router = router.EventRouter(lock)
        res = event_router.add_handler('ch1', 'h1', [], [])
        self.assertIsNotNone(res.error)

    def test_remove_handler__not_registered(self) -> None:
        """Test add_handler with a not-registered channel."""
        lock = threading.Semaphore()
        event_router = router.EventRouter(lock)
        self.assertFalse(event_router.remove_handler('h1'))
        res = event_router.register_channel('ch1', _create_reader_writer_ok)
        self.assertIsNone(res.error)
        self.assertFalse(event_router.remove_handler('h1'))

    def test_add_remove_handler_listener__not_registered(self) -> None:
        """Test add_handler_listener and remove_handler_listener with a not-registered handle."""
        lock = threading.Semaphore()
        event_router = router.EventRouter(lock)
        self.assertFalse(event_router.add_handler_listener('h1', None, None))
        res = event_router.register_channel('ch1', _create_reader_writer_ok)
        self.assertIsNone(res.error)
        # ... and if a handle is registered, but not the one we're looking for ...
        res = event_router.add_handler('ch1', 'h1', [], [])
        self.assertIsNone(res.error)
        self.assertFalse(event_router.add_handler_listener('h2', None, None))
        self.assertFalse(event_router.remove_handler_listener('h1', 'x', 'y'))

    def test_add_remove_handler_listener__registered(self) -> None:
        """Test add_handler_listener and remove_handler_listener with a registered handle."""
        lock = threading.Semaphore()
        event_router = router.EventRouter(lock)
        res = event_router.register_channel('ch1', _create_reader_writer_ok)
        self.assertIsNone(res.error)
        res = event_router.add_handler('ch1', 'h1', [], [])
        self.assertIsNone(res.error)
        self.assertTrue(event_router.add_handler_listener('h1', None, None))
        self.assertFalse(event_router.remove_handler_listener('h1', 'x', 'y'))
        self.assertTrue(event_router.remove_handler_listener('h1', None, None))
        self.assertFalse(event_router.remove_handler_listener('h1', None, None))

    def test_add_internal_event_handler__not_registered(self) -> None:
        """Test add_internal_event_handler with no registered channel."""
        lock = threading.Semaphore()
        event_router = router.EventRouter(lock)
        res = event_router.add_internal_event_handler('ch', _never_called_handler)
        self.assertIsNotNone(res.error)

    def test_add_internal_event_handler__registered(self) -> None:
        """Test add_internal_event_handler with no registered channel."""
        lock = threading.Semaphore()
        event_router = router.EventRouter(lock)
        res = event_router.register_channel('ch1', _create_reader_writer_ok)
        self.assertIsNone(res.error)
        res = event_router.add_internal_event_handler('ch1', _never_called_handler)
        self.assertIsNone(res.error)

    def test_inject_event__multiple_channels(self) -> None:
        """Test inject_event with multiple listening channels."""
        reader1 = DelayedEofConditionBinaryReader(threading.Condition())
        writer1 = SimpleBinaryWriter()
        reader2 = DelayedEofConditionBinaryReader(threading.Condition())
        writer2 = SimpleBinaryWriter()

        def create_reader_writer_1() -> StdRet[Tuple[BinaryReader, BinaryWriter]]:
            return StdRet.pass_ok((reader1, writer1))

        def create_reader_writer_2() -> StdRet[Tuple[BinaryReader, BinaryWriter]]:
            return StdRet.pass_ok((reader2, writer2))

        executor = ThreadPoolExecutor()
        lock = threading.Semaphore()
        event_router = router.EventRouter(lock, executor=executor)
        res = event_router.register_channel('ch1', create_reader_writer_1)
        self.assertIsNone(res.error)
        res = event_router.register_channel('ch2', create_reader_writer_2)
        self.assertIsNone(res.error)
        res = event_router.add_handler('ch1', 'h1', [], [(None, None)])
        self.assertIsNone(res.error)
        res = event_router.add_handler('ch2', 'h2', [], [('e1', 't1')])
        self.assertIsNone(res.error)

        # Inject two events...
        event_h1 = to_raw_event_object('e1', 's1', 't2', {})
        event_h1_2 = to_raw_event_object('e1', 's1', 't1', {})

        event_router.inject_event(event_h1)
        event_router.inject_event(event_h1_2)

        # Wait to have an EOF until after the injection, otherwise the channels
        # could be removed before the test has completed.
        reader1.send_events()
        reader2.send_events()

        executor.shutdown(wait=True)

        h1_collector = CallbackCollector()
        read_event_stream(
            create_read_stream(writer1.getvalue()),
            h1_collector.on_event, h1_collector.on_end_of_stream, h1_collector.on_error,
        )
        self.assertEqual(
            event_h1,
            h1_collector.next_as_raw_event(self),
        )
        self.assertEqual(
            event_h1_2,
            h1_collector.next_as_raw_event(self),
        )
        h1_collector.next_as_eof(self)
        self.assertTrue(h1_collector.is_empty())

        h2_collector = CallbackCollector()
        read_event_stream(
            create_read_stream(writer2.getvalue()),
            h2_collector.on_event, h2_collector.on_end_of_stream, h2_collector.on_error,
        )
        self.assertEqual(
            event_h1_2,
            h2_collector.next_as_raw_event(self),
        )
        h2_collector.next_as_eof(self)
        self.assertTrue(h2_collector.is_empty())

    def test_inject_event__write_error(self) -> None:
        """Test register_channel when the registration callback fails."""
        condition1 = threading.Condition()
        reader1 = DelayedEofConditionBinaryReader(condition1)
        writer1 = ErrorBinaryWriter()

        # The target determines whether the on-error for a channel
        # causes a close-the-channel.
        target = MockTarget(self)
        target.on_error_returns.append(True)

        def create_reader_writer_1() -> StdRet[Tuple[BinaryReader, BinaryWriter]]:
            return StdRet.pass_ok((reader1, writer1))

        executor = ThreadPoolExecutor()
        lock = threading.Semaphore()
        event_router = router.EventRouter(lock, executor=executor, target=target)
        res = event_router.register_channel('ch1', create_reader_writer_1)
        self.assertIsNone(res.error)
        res = event_router.add_handler('ch1', 'h1', [], [(None, None)])
        self.assertIsNone(res.error)

        # Inject the event
        event_router.inject_event(to_raw_event_object('e1', 's1', 't2', {}))

        # Wait to have an EOF until after the injection, otherwise the channels
        # could be removed before the test has completed.
        reader1.send_events()
        with condition1:
            condition1.wait(2.0)

        executor.shutdown(wait=True)

        # Because the target returns True on error, the channel is de-registered.
        self.assertEqual(1, writer1.call_count)
        self.assertEqual((), tuple(event_router.get_registered_channel_names()))

        target.assert_next_on_error(UserMessage(
            USER_MESSAGE_CATALOG_EXCEPTION,
            i18n('writing event to stream'), exception=ErrorBinaryWriter.ERROR,
        ))
        target.assert_next_on_eof()
        target.assert_end()

    def test_inject_event_to_channel(self) -> None:
        """Test inject_event_to_channel."""
        reader1 = DelayedEofConditionBinaryReader(threading.Condition())
        writer1 = SimpleBinaryWriter()
        reader2 = DelayedEofConditionBinaryReader(threading.Condition())
        writer2 = SimpleBinaryWriter()

        def create_reader_writer_1() -> StdRet[Tuple[BinaryReader, BinaryWriter]]:
            return StdRet.pass_ok((reader1, writer1))

        def create_reader_writer_2() -> StdRet[Tuple[BinaryReader, BinaryWriter]]:
            return StdRet.pass_ok((reader2, writer2))

        executor = ThreadPoolExecutor()
        lock = threading.Semaphore()
        event_router = router.EventRouter(lock, executor=executor)
        res = event_router.register_channel('ch1', create_reader_writer_1)
        self.assertIsNone(res.error)
        res = event_router.register_channel('ch2', create_reader_writer_2)
        self.assertIsNone(res.error)
        res = event_router.add_handler('ch1', 'h1', [], [(None, None)])
        self.assertIsNone(res.error)
        res = event_router.add_handler('ch2', 'h2', [], [(None, None)])
        self.assertIsNone(res.error)

        # Inject an event...
        event_h1 = to_raw_event_object('e1', 's1', 't2', {})

        event_router.inject_event_to_channel('ch1', event_h1)

        # Wait to have an EOF until after the injection, otherwise the channels
        # could be removed before the test has completed.
        reader1.send_events()
        reader2.send_events()

        executor.shutdown(wait=True)

        h1_collector = CallbackCollector()
        read_event_stream(
            create_read_stream(writer1.getvalue()),
            h1_collector.on_event, h1_collector.on_end_of_stream, h1_collector.on_error,
        )
        self.assertEqual(
            event_h1,
            h1_collector.next_as_raw_event(self),
        )
        h1_collector.next_as_eof(self)
        self.assertTrue(h1_collector.is_empty())

        h2_collector = CallbackCollector()
        read_event_stream(
            create_read_stream(writer2.getvalue()),
            h2_collector.on_event, h2_collector.on_end_of_stream, h2_collector.on_error,
        )
        h2_collector.next_as_eof(self)
        self.assertTrue(h2_collector.is_empty())


def _create_reader_writer_ok() -> StdRet[Tuple[BinaryReader, BinaryWriter]]:
    return StdRet.pass_ok((create_read_stream(b''), SimpleBinaryWriter()))


def _never_called_handler(_eid: str, _sid: str, _tid: str, _evt: RawEvent) -> EventFilterResult:
    raise Exception('should never be called')  # pragma no cover


class ErrorBinaryWriter:
    """Binary Writer that generates an error"""
    __slots__ = ('call_count', 'data_count')

    ERROR = OSError('writer closed')

    def __init__(self) -> None:
        self.call_count = 0
        self.data_count = 0

    def write(self, data: bytes) -> None:
        """Implement the binary writer protocol."""
        self.call_count += 1
        self.data_count += len(data)
        raise ErrorBinaryWriter.ERROR
