
import unittest
import io
from .util import CallbackCollector
from .. import reader, writer, defs


class ReadWriteTest(unittest.TestCase):
    def test_1_packet(self) -> None:
        inp_stream = io.BytesIO()
        collector = CallbackCollector()
        data_1 = {"this": ["is", "Sparta"]}
        writer.write_object_event_to_stream(inp_stream, 'e1', 's1', 't1', data_1)
        outp_stream = io.BytesIO(inp_stream.getvalue())
        reader.read_event_stream(
            outp_stream, collector.on_event, collector.on_end_of_stream, collector.on_error,
        )
        event_1 = collector.next_as_raw_event(self)
        collector.next_as_eof(self)
        self.assertTrue(defs.is_raw_event_object(event_1))
        self.assertFalse(defs.is_raw_event_binary(event_1))
        self.assertEqual('e1', defs.raw_event_id(event_1))
        self.assertEqual('s1', defs.raw_event_source_id(event_1))
        self.assertEqual('t1', defs.raw_event_target_id(event_1))
        self.assertEqual(data_1, defs.as_raw_event_object_data(event_1))

    def test_4_packets(self) -> None:
        inp_stream = io.BytesIO()
        collector = CallbackCollector()
        data_1 = {"this": ["is", "Sparta"]}
        data_2 = b'that is Japan'
        data_3 = {"is": "this", "wonderful?": False}
        data_4 = b'Simulating a \0 stream of \x01 \x80\x81 data'
        writer.write_object_event_to_stream(inp_stream, 'e1', 's1', 't1', data_1)
        writer.write_binary_event_to_stream(inp_stream, 'event-2', 'source-2', 'target-2', len(data_2), data_2)
        writer.write_object_event_to_stream(inp_stream, 'e1', 's2', 't3', data_3)
        writer.write_binary_event_to_stream(inp_stream, 'event-4', 'source-1', 'target-2', len(data_4), data_4)
        outp_stream = io.BytesIO(inp_stream.getvalue())
        reader.read_event_stream(
            outp_stream, collector.on_event, collector.on_end_of_stream, collector.on_error,
        )
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
        self.assertEqual(data_2, defs.as_raw_event_binary_data_reader(event_2)())

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
        self.assertEqual(data_4, defs.as_raw_event_binary_data_reader(event_4)())
