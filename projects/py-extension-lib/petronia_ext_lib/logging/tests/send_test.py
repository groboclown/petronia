"""Test the module."""

import unittest
import unittest.mock
from petronia_common.event_stream import (
    read_event_stream,
    as_raw_event_object_data, is_raw_event_object, raw_event_id, raw_event_source_id,
)
from petronia_common.event_stream.tests.shared import (
    create_read_stream, SimpleBinaryWriter, CallbackCollector,
)
from petronia_common.util import UserMessage, i18n
from petronia_common.util.error import SimplePetroniaReturnError, RET_OK_NONE
from .. import send
from ...events import logging
from ...runner import EventRegistryContext
from ...runner.main import EventRegistryContextImpl
from ...standard.error import FILE_ERROR_CATEGORY, CONFIGURATION_ERROR_CATEGORY


class SendTest(unittest.TestCase):
    """Test the functions in the module."""

    def test_send_system_error__no_messages(self) -> None:
        """Test the function."""
        writer = SimpleBinaryWriter()
        context = EventRegistryContextImpl(create_read_stream(b''), writer)
        res = send.send_system_error(
            context, 'my-event:source', SimplePetroniaReturnError(),
            'msg-ident', [FILE_ERROR_CATEGORY],
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
            'my-msg', [FILE_ERROR_CATEGORY],
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

    def test_send_user_error(self) -> None:
        """Test sending a user error."""
        context = unittest.mock.Mock(EventRegistryContext())
        context.send_event.return_value = RET_OK_NONE
        send.send_user_error(
            context, 's1', SimplePetroniaReturnError(UserMessage('c1', i18n('m1'))), 'i1',
        )
        calls = context.send_event.call_args_list
        self.assertEqual(1, len(calls))
        self.assertEqual(
            's1',
            calls[0].args[0],
        )
        self.assertEqual(
            logging.UserErrorEvent.UNIQUE_TARGET_FQN,
            calls[0].args[1],
        )
        event_obj = calls[0].args[2]
        assert isinstance(event_obj, logging.UserErrorEvent)  # nosec  # mypy required
        self.assertEqual(
            {'user_error': {
                'categories': [CONFIGURATION_ERROR_CATEGORY],
                'identifier': 'i1',
                'messages': [{
                    'catalog': 'c1',
                    'message': 'm1',
                    'arguments': [],
                }],
            }},
            event_obj.export_data(),
        )

    def test_send_log_message(self) -> None:
        """Test send_log_message"""
        context = unittest.mock.Mock(EventRegistryContext())
        context.send_event.return_value = RET_OK_NONE
        send.send_log_message(
            context, 's1', 'debug',
            [UserMessage('c', i18n('m1'))],
        )
        calls = context.send_event.call_args_list
        self.assertEqual(1, len(calls))
        self.assertEqual(
            's1',
            calls[0].args[0],
        )
        self.assertEqual(
            logging.LogEvent.UNIQUE_TARGET_FQN,
            calls[0].args[1],
        )
        event_obj = calls[0].args[2]
        assert isinstance(event_obj, logging.LogEvent)  # nosec  # mypy required
        self.assertEqual(
            {
                'scope': 'debug',
                'messages': [{
                    'catalog': 'c',
                    'message': 'm1',
                    'arguments': [],
                }],
            },
            event_obj.export_data(),
        )
