
"""Tests the read and write stream functions together."""

import unittest
import asyncio
from .util import (
    CallbackCollector, SimpleBinaryWriter,
    async_run_with_stream, create_read_stream,
)
from .. import reader, writer, defs


class ReadWriteTest(unittest.TestCase):
    """Combines the read and write stream handlers, to ensure they work together correctly."""
    def test_1_packet(self) -> None:
        """Writes then reads 1 event packet."""
        inp_stream = SimpleBinaryWriter()
        collector = CallbackCollector()
        data_1 = {"this": ["is", "Sparta"]}
        res1 = asyncio.run(
            writer.write_object_event_to_stream(inp_stream, 'e1', 's1', 't1', data_1),
        )
        self.assertTrue(res1.ok)
        _, remaining = async_run_with_stream(
            inp_stream.getvalue(),
            lambda outp_stream: reader.read_event_stream(
                outp_stream, collector.on_event, collector.on_end_of_stream, collector.on_error,
            )
        )
        self.assertEqual(b'', remaining)
        event_1 = collector.next_as_raw_event(self)
        collector.next_as_eof(self)
        self.assertTrue(defs.is_raw_event_object(event_1))
        self.assertFalse(defs.is_raw_event_binary(event_1))
        self.assertEqual('e1', defs.raw_event_id(event_1))
        self.assertEqual('s1', defs.raw_event_source_id(event_1))
        self.assertEqual('t1', defs.raw_event_target_id(event_1))
        self.assertEqual(data_1, defs.as_raw_event_object_data(event_1))

    def test_4_packets(self) -> None:
        """Writes then reads 4 event packets."""
        async def do_test() -> None:
            inp_stream = SimpleBinaryWriter()
            collector = CallbackCollector()
            data_1 = {"this": ["is", "Sparta"]}
            data_2 = b'that is Japan'
            data_3 = {"is": "this", "wonderful?": False}
            data_4 = b'Simulating a \0 stream of \x01 \x80\x81 data'
            res1 = await writer.write_object_event_to_stream(
                inp_stream, 'e1', 's1', 't1', data_1,
            )
            self.assertTrue(res1.ok)
            res1 = await writer.write_binary_event_to_stream(
                inp_stream, 'event-2', 'source-2', 'target-2', len(data_2), data_2,
            )
            self.assertTrue(res1.ok)
            res1 = await writer.write_object_event_to_stream(
                inp_stream, 'e1', 's2', 't3', data_3,
            )
            self.assertTrue(res1.ok)
            res1 = await writer.write_binary_event_to_stream(
                inp_stream, 'event-4', 'source-1', 'target-2', len(data_4), data_4,
            )
            self.assertTrue(res1.ok)
            outp_stream = create_read_stream(inp_stream.getvalue())
            res2 = await reader.read_event_stream(
                outp_stream, collector.on_event, collector.on_end_of_stream, collector.on_error,
            )
            remaining = await outp_stream.read()
            self.assertIsNone(res2)
            self.assertEqual(b'', remaining)
            event_1 = collector.next_as_raw_event(self)
            event_2 = collector.next_as_raw_event(self)
            event_3 = collector.next_as_raw_event(self)
            event_4 = collector.next_as_raw_event(self)
            collector.next_as_eof(self)

            self.assertTrue(defs.is_raw_event_object(event_1))
            self.assertFalse(defs.is_raw_event_binary(event_1))
            self.assertEqual('e1', defs.raw_event_id(event_1))
            self.assertEqual('s1', defs.raw_event_source_id(event_1))
            self.assertEqual('t1', defs.raw_event_target_id(event_1))
            self.assertEqual(data_1, defs.as_raw_event_object_data(event_1))

            self.assertFalse(defs.is_raw_event_object(event_2))
            self.assertTrue(defs.is_raw_event_binary(event_2))
            self.assertEqual('event-2', defs.raw_event_id(event_2))
            self.assertEqual('source-2', defs.raw_event_source_id(event_2))
            self.assertEqual('target-2', defs.raw_event_target_id(event_2))
            self.assertEqual(data_2, await defs.as_raw_event_binary_data_reader(event_2)())

            self.assertTrue(defs.is_raw_event_object(event_3))
            self.assertFalse(defs.is_raw_event_binary(event_3))
            self.assertEqual('e1', defs.raw_event_id(event_3))
            self.assertEqual('s2', defs.raw_event_source_id(event_3))
            self.assertEqual('t3', defs.raw_event_target_id(event_3))
            self.assertEqual(data_3, defs.as_raw_event_object_data(event_3))

            self.assertFalse(defs.is_raw_event_object(event_4))
            self.assertTrue(defs.is_raw_event_binary(event_4))
            self.assertEqual('event-4', defs.raw_event_id(event_4))
            self.assertEqual('source-1', defs.raw_event_source_id(event_4))
            self.assertEqual('target-2', defs.raw_event_target_id(event_4))
            self.assertEqual(data_4, await defs.as_raw_event_binary_data_reader(event_4)())

        asyncio.run(do_test())
