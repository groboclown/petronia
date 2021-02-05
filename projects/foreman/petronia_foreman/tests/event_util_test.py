"""Test the module"""

import unittest
from petronia_common.util import UserMessage, i18n, not_none
from petronia_common.util.error import SimplePetroniaReturnError
from petronia_common.extension.runner import message_helper
from .. import event_util
from ..events import foreman


class EventUtilTest(unittest.TestCase):
    """Tests the functions of the module."""

    def test_create_std_ret_errors__no_messages(self) -> None:
        """Test the create_std_ret_errors function"""
        event = event_util.create_std_ret_errors(
            SimplePetroniaReturnError(),
            [message_helper.FILE_ERROR_CATEGORY],
        )
        self.assertEqual([], event)

    def test_create_std_ret_errors__messages(self) -> None:
        """Test the create_std_ret_errors function"""
        event = event_util.create_std_ret_errors(
            SimplePetroniaReturnError(
                UserMessage('c', i18n('x')),
                UserMessage('c', i18n('a {b} c'), b='1'),
            ),
            [message_helper.FILE_ERROR_CATEGORY],
        )
        self.assertEqual(2, len(event))
        ev0 = event[0]
        ev1 = event[1]
        self.assertEqual(foreman.EXTENSION_NAME, ev0.source)
        self.assertEqual('x', ev0.error_message.message)
        self.assertEqual([], ev0.error_message.arguments)

        self.assertEqual(foreman.EXTENSION_NAME, ev1.source)
        self.assertEqual('a {b} c', ev1.error_message.message)
        self.assertIsNotNone(ev1.error_message.arguments)
        arguments = not_none(ev1.error_message.arguments)
        self.assertEqual(1, len(arguments))
        self.assertEqual('b', arguments[0].name)
        self.assertEqual('string', arguments[0].value.name)
        self.assertEqual('1', arguments[0].value.value)

    def test_create_top_std_ret_errors__no_messages(self) -> None:
        """Test the create_top_std_ret_error function"""
        event = event_util.create_top_std_ret_error(
            SimplePetroniaReturnError(),
            [message_helper.FILE_ERROR_CATEGORY],
        )
        self.assertEqual('unknown-error', event.identifier)

    def test_create_top_std_ret_errors__messages(self) -> None:
        """Test the create_top_std_ret_error function"""
        event = event_util.create_top_std_ret_error(
            SimplePetroniaReturnError(
                UserMessage('c', i18n('x')),
                UserMessage('c', i18n('a {b} c'), b='1'),
            ),
            [message_helper.FILE_ERROR_CATEGORY],
        )
        self.assertEqual(foreman.EXTENSION_NAME, event.source)
        self.assertEqual('x', event.error_message.message)
        self.assertEqual([], event.error_message.arguments)
