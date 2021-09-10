"""Test the module."""

import unittest
import json
from petronia_common.event_stream import (
    read_event_stream,
    as_raw_event_object_data, is_raw_event_object, raw_event_id, raw_event_source_id,
)
from petronia_common.event_stream.tests.shared import (
    create_read_stream, SimpleBinaryWriter, CallbackCollector,
)
from petronia_common.util import tznow
from .. import send
from ...events import timer, datastore
from ...runner.main import EventRegistryContextImpl


class SendTest(unittest.TestCase):
    """Test the functions in the module."""

    def test_send_store_data(self) -> None:
        """Test the function."""
        writer = SimpleBinaryWriter()
        context = EventRegistryContextImpl('x', create_read_stream(b''), writer)
        store_data = timer.HeartbeatEvent(tznow())
        send.send_store_data(context, 'my-event:data', store_data)
        reader = create_read_stream(writer.getvalue())
        collector = CallbackCollector()
        read_event_stream(
            reader, collector.on_event, collector.on_end_of_stream, collector.on_error,
        )

        event = collector.next_as_raw_event(self)
        self.assertTrue(is_raw_event_object(event))
        self.assertEqual(datastore.StoreDataRequestEvent.FULL_EVENT_NAME, raw_event_id(event))
        self.assertEqual('my-event:data', raw_event_source_id(event))
        res1 = datastore.StoreDataRequestEvent.parse_data(as_raw_event_object_data(event))
        self.assertIsNone(res1.error)
        res2 = timer.HeartbeatEvent.parse_data(json.loads(res1.result.json))
        self.assertIsNone(res2.error)
        self.assertEqual(store_data.sent_on, res2.result.sent_on)
        collector.next_as_eof(self)
