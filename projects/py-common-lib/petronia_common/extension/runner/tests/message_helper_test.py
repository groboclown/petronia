"""Test the module"""

from typing import cast
import unittest
import datetime
from .. import message_helper
from ....util.message import UserMessage, i18n


class MessageHelperTest(unittest.TestCase):
    """Test the message helper functions."""

    def test_get_message_arguments__empty(self) -> None:
        """Test get_message_arguments with no arguments."""
        res = message_helper.get_message_arguments(UserMessage('c', i18n('y')))
        self.assertEqual(
            [],
            res,
        )

    def test_get_message_arguments__all_types(self) -> None:
        """Test get_message_arguments with all argument types."""
        now = datetime.datetime.now()
        res = message_helper.get_message_arguments(UserMessage(
            'c', i18n('y'),
            sv='string-value',
            bv=True,
            nv=None,
            iv=12,
            fv=9.5,
            dtv=now,
            dv=now.date(),
            tv=now.time(),
            ev=[],
            slv=['sv1', 'sv2'],
            blv=[False, True],
            ilv=[1, 2],
            flv=[4.4, 5.5],
            dtlv=[now, now],
            dlv=[now.date(), now.date()],
            tlv=[now.time(), now.time()],
            dcv={'s': 1, 'x': 2},

            # Force bad typing code paths.
            # This can happen if the called-out methods are incorrectly masked as something else.
            ov=cast(int, TestReprObj()),
            olv=[cast(int, TestReprObj())],
        ))
        today = datetime.datetime(year=now.year, month=now.month, day=now.day)
        time_now = now
        self.assertEqual(
            [
                ('blv', 'bool_list', [False, True]),
                ('bv', 'bool', True),
                ('dcv', 'string_list', ['s=1', 'x=2']),
                ('dlv', 'datetime_list', [today, today]),
                ('dtlv', 'datetime_list', [now, now]),
                ('dtv', 'datetime', now),
                ('dv', 'datetime', today),
                ('ev', 'string_list', []),
                ('flv', 'float_list', [4.4, 5.5]),
                ('fv', 'float', 9.5),
                ('ilv', 'int_list', [1, 2]),
                ('iv', 'int', 12),
                ('nv', 'string', '<null>'),
                ('olv', 'string_list', [TEST_REPR_OBJ_STR]),
                ('ov', 'string', TEST_REPR_OBJ_STR),
                ('slv', 'string_list', ['sv1', 'sv2']),
                ('sv', 'string', 'string-value'),
                ('tlv', 'datetime_list', [time_now, time_now]),
                ('tv', 'datetime', time_now),
            ],
            sorted(res, key=lambda x: str(x[0])),
        )


TEST_REPR_OBJ_STR = '-An invalid type-'


class TestReprObj:
    """A class used for testing invalid types."""

    def __str__(self) -> str:
        return TEST_REPR_OBJ_STR

    def __repr__(self) -> str:
        raise NotImplementedError  # pragma no cover
