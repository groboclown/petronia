"""Test the module"""

from typing import Sequence, Tuple, List, cast
import unittest
import datetime

from petronia_common.util import not_none
from petronia_common.util.message import UserMessage, UserMessageData, i18n
from .. import localizable_message
from ...events import logging


class LocalizableMessageTest(unittest.TestCase):
    """Test the message helper functions."""

    def test_create_localizable_message(self) -> None:
        """Test create_localizable_message, using the logging error message
        to test against."""

        res = localizable_message.create_localizable_message(
            logging.LocalizableMessage, logging.MessageArgument, logging.MessageArgumentValue,
            UserMessage('c1', i18n('m1'), a1='v1'),
        )
        self.assertEqual('m1', res.message)
        self.assertEqual('c1', res.catalog)
        self.assertIsNotNone(res.arguments)
        args = not_none(res.arguments)
        self.assertEqual(1, len(args))
        self.assertEqual('a1', args[0].name)
        self.assertEqual(
            localizable_message.STRING_LOCALE_ARGUMENT_TYPE,
            args[0].value.name,
        )
        self.assertEqual('v1', args[0].value.value)

    def test_create_message_argument_value(self) -> None:
        """Test create_message_argument_value."""
        now = datetime.datetime.now()
        today = datetime.datetime(year=now.year, month=now.month, day=now.day)
        time_now = now

        test_data: Sequence[Tuple[
            UserMessageData,
            localizable_message.LocaleMessageArgumentTypeName,
            localizable_message.LocaleMessageArgumentType,
        ]] = [
            ('string-value', localizable_message.STRING_LOCALE_ARGUMENT_TYPE, 'string-value'),
            (None, localizable_message.STRING_LOCALE_ARGUMENT_TYPE, '<null>'),
            (12, localizable_message.INT_LOCALE_ARGUMENT_TYPE, 12),
            (9.5, localizable_message.FLOAT_LOCALE_ARGUMENT_TYPE, 9.5),
            (False, localizable_message.BOOL_LOCALE_ARGUMENT_TYPE, False),
            (now, localizable_message.DATETIME_LOCALE_ARGUMENT_TYPE, now),
            (now.date(), localizable_message.DATETIME_LOCALE_ARGUMENT_TYPE, today),
            (now.time(), localizable_message.DATETIME_LOCALE_ARGUMENT_TYPE, time_now),
            (  # mypy issues
                cast(List[int], []),
                localizable_message.STRING_LIST_LOCALE_ARGUMENT_TYPE,
                cast(List[str], []),
            ),
            (['s1', 's2'], localizable_message.STRING_LIST_LOCALE_ARGUMENT_TYPE, ['s1', 's2']),
            ([1, 2], localizable_message.INT_LIST_LOCALE_ARGUMENT_TYPE, [1, 2]),
            ([4.4, 5.5], localizable_message.FLOAT_LIST_LOCALE_ARGUMENT_TYPE, [4.4, 5.5]),
            ([True, False], localizable_message.BOOL_LIST_LOCALE_ARGUMENT_TYPE, [True, False]),
            ([now, now], localizable_message.DATETIME_LIST_LOCALE_ARGUMENT_TYPE, [now, now]),
            (
                [now.date(), now.date()],
                localizable_message.DATETIME_LIST_LOCALE_ARGUMENT_TYPE,
                [today, today],
            ),
            (
                [now.time(), now.time()],
                localizable_message.DATETIME_LIST_LOCALE_ARGUMENT_TYPE,
                [time_now, time_now],
            ),
            (
                {'s2': 1, 's1': 'x2'},
                localizable_message.STRING_LIST_LOCALE_ARGUMENT_TYPE,
                # Note the alphabetizing
                ["s1='x2'", 's2=1'],
            ),

            # Force bad values that shouldn't be possible in normal Python typed programming.
            (
                cast(int, TestReprObj()),
                localizable_message.STRING_LOCALE_ARGUMENT_TYPE,
                TEST_REPR_OBJ_STR,
            ),
            (
                [cast(int, TestReprObj()), cast(int, TestReprObj())],
                localizable_message.STRING_LIST_LOCALE_ARGUMENT_TYPE,
                [TEST_REPR_OBJ_STR, TEST_REPR_OBJ_STR],
            ),
        ]
        for src_data, expected_name, expected_val in test_data:
            with self.subTest(str(src_data)):
                actual_name, actual_val = localizable_message.create_message_argument_value(
                    src_data,
                )
                self.assertEqual((expected_name, expected_val), (actual_name, actual_val))


TEST_REPR_OBJ_STR = '-An invalid type-'


class TestReprObj:
    """A class used for testing invalid types."""

    def __str__(self) -> str:
        return TEST_REPR_OBJ_STR

    def __repr__(self) -> str:
        return repr(TEST_REPR_OBJ_STR)
