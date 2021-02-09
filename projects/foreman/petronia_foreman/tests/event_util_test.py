"""Test the module"""

import unittest
from petronia_common.util import UserMessage, i18n, not_none
from petronia_common.util.error import SimplePetroniaReturnError
from petronia_ext_lib.standard import error
from .. import event_util
from ..events import foreman


class EventUtilTest(unittest.TestCase):
    """Tests the functions of the module."""

    def test_create_std_ret_errors__no_messages(self) -> None:
        """Test the create_std_ret_errors function"""
        event = event_util.create_std_ret_errors(
            SimplePetroniaReturnError(),
            'id1',
            [error.FILE_ERROR_CATEGORY],
        )
        self.assertIsNone(event)

    def test_create_std_ret_errors__messages(self) -> None:
        """Test the create_std_ret_errors function"""
        event_res = event_util.create_std_ret_errors(
            SimplePetroniaReturnError(
                UserMessage('c', i18n('x')),
                UserMessage('c', i18n('a {b} c'), b='1'),
            ),
            'id1',
            [error.FILE_ERROR_CATEGORY],
        )
        self.assertIsNotNone(event_res)
        event = not_none(event_res)
        self.assertEqual(foreman.EXTENSION_NAME, event.source)
        self.assertEqual(2, len(event.messages))
        ev0 = event.messages[0]
        ev1 = event.messages[1]
        self.assertEqual('x', ev0.message)
        self.assertEqual([], ev0.arguments)

        self.assertEqual('a {b} c', ev1.message)
        self.assertIsNotNone(ev1.arguments)
        arguments = not_none(ev1.arguments)
        self.assertEqual(1, len(arguments))
        self.assertEqual('b', arguments[0].name)
        self.assertEqual('string', arguments[0].value.name)
        self.assertEqual('1', arguments[0].value.value)
