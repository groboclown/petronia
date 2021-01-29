"""Test the module."""

from typing import List, Tuple
import unittest
import threading
import concurrent.futures
from .shared import SimpleBinaryWriter, create_raw_reader
from .. import thread_writer
from ..defs import (
    RawEventObject, to_raw_event_object,
    RawEventBinary, to_raw_event_binary,
    raw_event_id, raw_event_source_id, raw_event_target_id,
    as_raw_event_object_data,
    raw_event_binary_size, as_raw_event_binary_data_reader, RawBinaryReader,
)
from ..writer import write_object_event_to_stream, write_binary_event_to_stream


class ThreadWriterTest(unittest.TestCase):
    """Test the ThreadSafeEventWriter and AsyncThreadSafeEventWriter classes."""

    def setUp(self) -> None:
        self.threads: List[threading.Thread] = []
        self.executor = concurrent.futures.ThreadPoolExecutor(1)

    def tearDown(self) -> None:
        for thread in self.threads:  # pragma no cover
            thread.join(10.0)  # pragma no cover
        self.executor.shutdown(wait=True)

    def test_basic_write_object(self) -> None:
        """Test a simple write to a stream."""

        writer = SimpleBinaryWriter()
        t_writer = thread_writer.ThreadSafeEventWriter(writer)

        t_writer.write_object_event('e1', 's1', 't1', {'x': 'y'})
        self._assert_object_events_equal(
            [to_raw_event_object('e1', 's1', 't1', {'x': 'y'})],
            writer,
        )

    def test_basic_write_binary(self) -> None:
        """Test a simple write to a stream."""

        writer = SimpleBinaryWriter()
        t_writer = thread_writer.ThreadSafeEventWriter(writer)

        t_writer.write_binary_event('e1', 's1', 't1', 2, b'12')
        self._assert_binary_events_equal(
            [to_raw_event_binary('e1', 's1', 't1', 2, create_raw_reader(b'12'))],
            writer,
        )

    def test_async_write_object_event(self) -> None:
        """Test async_write_object_event with a simple object."""

        writer = SimpleBinaryWriter()
        lock = threading.RLock()
        t_writer = thread_writer.AsyncThreadSafeEventWriter(
            writer, executor=self.executor, lock=lock,
        )
        # Write out of order using the async parts.
        with lock:
            f_res1 = t_writer.async_write_object_event('e1', 's1', 't1', {'x': 'y'})
            res2 = t_writer.write_object_event('e2', 's2', 't2', {'a': 'b'})
        res1 = f_res1.result(2.0)
        self.assertIsNone(res1.error)
        self.assertIsNone(res2.error)
        self._assert_object_events_equal(
            [
                to_raw_event_object('e2', 's2', 't2', {'a': 'b'}),
                to_raw_event_object('e1', 's1', 't1', {'x': 'y'}),
            ],
            writer,
        )

    def test_async_write_simple_binary_event(self) -> None:
        """Test async_write_simple_binary_event with a simple binary bytes."""

        writer = SimpleBinaryWriter()
        lock = threading.RLock()
        t_writer = thread_writer.AsyncThreadSafeEventWriter(
            writer, executor=self.executor, lock=lock,
        )
        # Write out of order using the async parts.
        with lock:
            f_res1 = t_writer.async_write_simple_binary_event('e1', 's1', 't1', b'1')
            res2 = t_writer.write_binary_event('e2', 's2', 't2', 2, b'12')
        res1 = f_res1.result(2.0)
        self.assertIsNone(res1.error)
        self.assertIsNone(res2.error)
        self._assert_binary_events_equal(
            [
                to_raw_event_binary('e2', 's2', 't2', 2, create_raw_reader(b'12')),
                to_raw_event_binary('e1', 's1', 't1', 1, create_raw_reader(b'1')),
            ],
            writer,
        )

    def test_async_write_reader_binary_event(self) -> None:
        """Test async_write_binary_event."""

        created_reader = [0]

        def mk_reader() -> Tuple[int, RawBinaryReader]:
            created_reader[0] += 1
            return 3, create_raw_reader(b'123')

        writer = SimpleBinaryWriter()
        lock = threading.RLock()
        t_writer = thread_writer.AsyncThreadSafeEventWriter(
            writer, executor=self.executor, lock=lock,
        )
        # Write out of order using the async parts.
        with lock:
            f_res1 = t_writer.async_write_binary_event('e1', 's1', 't1', mk_reader)
            res2 = t_writer.write_binary_event('e2', 's2', 't2', 2, b'12')
            self.assertEqual([0], created_reader)
        res1 = f_res1.result(2.0)
        self.assertIsNone(res1.error)
        self.assertIsNone(res2.error)
        self.assertEqual([1], created_reader)
        self._assert_binary_events_equal(
            [
                to_raw_event_binary('e2', 's2', 't2', 2, create_raw_reader(b'12')),
                to_raw_event_binary('e1', 's1', 't1', 3, create_raw_reader(b'123')),
            ],
            writer,
        )

    def _assert_object_events_equal(
            self, expected: List[RawEventObject], writer: SimpleBinaryWriter,
    ) -> None:
        expected_writer = SimpleBinaryWriter()
        for event in expected:
            write_object_event_to_stream(
                expected_writer,
                raw_event_id(event),
                raw_event_source_id(event),
                raw_event_target_id(event),
                as_raw_event_object_data(event),
            )
        self.assertEqual(expected_writer.getvalue(), writer.getvalue())

    def _assert_binary_events_equal(
            self, expected: List[RawEventBinary], writer: SimpleBinaryWriter,
    ) -> None:
        expected_writer = SimpleBinaryWriter()
        for event in expected:
            write_binary_event_to_stream(
                expected_writer,
                raw_event_id(event),
                raw_event_source_id(event),
                raw_event_target_id(event),
                raw_event_binary_size(event),
                as_raw_event_binary_data_reader(event),
            )
        self.assertEqual(expected_writer.getvalue(), writer.getvalue())
