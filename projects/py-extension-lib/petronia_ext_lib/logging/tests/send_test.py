"""Test the module."""

import unittest
from petronia_common.event_stream import (
    read_event_stream,
    as_raw_event_object_data, is_raw_event_object, raw_event_id, raw_event_source_id,
)
from petronia_common.event_stream.tests.shared import (
    create_read_stream, SimpleBinaryWriter, CallbackCollector,
)
from petronia_common.util import UserMessage, i18n
from petronia_common.util.error import SimplePetroniaReturnError
from .. import send
from ...events import logging
from ...runner.main import EventRegistryContextImpl
from ...standard.error import FILE_ERROR_CATEGORY


class SendTest(unittest.TestCase):
    """Test the functions in the module."""

    def test_send_system_error__no_messages(self) -> None:
        """Test the function."""
        writer = SimpleBinaryWriter()
        context = EventRegistryContextImpl(create_read_stream(b''), writer)
        res = send.send_system_error(
            context, 'my-event:source', SimplePetroniaReturnError(),
            [FILE_ERROR_CATEGORY], 'msg-ident',
        )
        self.assertIsNone(res.error)
        reader = create_read_stream(writer.getvalue())
        collector = CallbackCollector()
        read_event_stream(
            reader, collector.on_event, collector.on_end_of_stream, collector.on_error,
        )

        # Should not have sent an event.
        collector.next_as_eof(self)

    def test_send_system_error(self) -> None:
        """Test the function."""
        writer = SimpleBinaryWriter()
        context = EventRegistryContextImpl(create_read_stream(b''), writer)
        send.send_system_error(
            context, 'my-event:source',
            SimplePetroniaReturnError(UserMessage('c1', i18n('m1'))),
            [FILE_ERROR_CATEGORY], 'my-msg',
        )
        reader = create_read_stream(writer.getvalue())
        collector = CallbackCollector()
        read_event_stream(
            reader, collector.on_event, collector.on_end_of_stream, collector.on_error,
        )

        event = collector.next_as_raw_event(self)
        self.assertTrue(is_raw_event_object(event))
        self.assertEqual(logging.SystemErrorEvent.FULL_EVENT_NAME, raw_event_id(event))
        self.assertEqual('my-event:source', raw_event_source_id(event))
        res = logging.SystemErrorEvent.parse_data(as_raw_event_object_data(event))
        self.assertIsNone(res.error)
        self.assertEqual(1, len(res.result.error.messages))
        self.assertEqual(
            'c1',
            res.result.error.messages[0].catalog,
        )
        self.assertEqual(
            'm1',
            res.result.error.messages[0].message,
        )
        collector.next_as_eof(self)
