"""Test the module."""

from typing import List
import unittest
import threading
from .shared import SimpleBinaryWriter, create_raw_reader
from .. import thread_writer
from ..defs import (
    RawEventObject, to_raw_event_object,
    RawEventBinary, to_raw_event_binary,
    raw_event_id, raw_event_source_id, raw_event_target_id,
    as_raw_event_object_data,
    raw_event_binary_size, as_raw_event_binary_data_reader,
)
from ..writer import write_object_event_to_stream, write_binary_event_to_stream


class ThreadWriterTest(unittest.TestCase):
    """Test the class."""

    def setUp(self) -> None:
        self.threads: List[threading.Thread] = []

    def tearDown(self) -> None:
        for thread in self.threads:  # pragma no cover
            thread.join(10.0)  # pragma no cover

    def test_basic_write_object(self) -> None:
        """Test a simple write to a stream."""

        writer = SimpleBinaryWriter()
        t_writer = thread_writer.ThreadSafeEventWriter(writer)

        t_writer.write_object_event('e1', 's1', 't1', {'x': 'y'})
        self._assert_object_events_equal(
            to_raw_event_object('e1', 's1', 't1', {'x': 'y'}),
            writer,
        )

    def test_basic_write_binary(self) -> None:
        """Test a simple write to a stream."""

        writer = SimpleBinaryWriter()
        t_writer = thread_writer.ThreadSafeEventWriter(writer)

        t_writer.write_binary_event('e1', 's1', 't1', 2, b'12')
        self._assert_binary_events_equal(
            to_raw_event_binary('e1', 's1', 't1', 2, create_raw_reader(b'12')),
            writer,
        )

    def _assert_object_events_equal(
            self, expected: RawEventObject, writer: SimpleBinaryWriter,
    ) -> None:
        expected_writer = SimpleBinaryWriter()
        write_object_event_to_stream(
            expected_writer,
            raw_event_id(expected),
            raw_event_source_id(expected),
            raw_event_target_id(expected),
            as_raw_event_object_data(expected),
        )
        self.assertEqual(expected_writer.getvalue(), writer.getvalue())

    def _assert_binary_events_equal(
            self, expected: RawEventBinary, writer: SimpleBinaryWriter,
    ) -> None:
        expected_writer = SimpleBinaryWriter()
        write_binary_event_to_stream(
            expected_writer,
            raw_event_id(expected),
            raw_event_source_id(expected),
            raw_event_target_id(expected),
            raw_event_binary_size(expected),
            as_raw_event_binary_data_reader(expected),
        )
        self.assertEqual(expected_writer.getvalue(), writer.getvalue())
