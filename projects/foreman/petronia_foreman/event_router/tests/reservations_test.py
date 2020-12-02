"""Test the module"""

from typing import Optional
import unittest
import re
from petronia_common.event_stream import EventForwarderTarget
from petronia_common.util import StdRet, i18n, RET_OK_NONE
from .. import reservations


class ChannelReservationsTest(unittest.TestCase):
    """Test the ChannelReservations class."""

    def test_reserve_channel__empty_set(self) -> None:
        """Call reserve_channel with no callbacks stored."""
        channel_res = reservations.ChannelReservations()
        res = channel_res.reserve_channel('some name')
        self.assertTrue(res.ok)

    def test_add_channel_reservation_callback__str__empty_set(self) -> None:
        """Call add_channel_reservation_callback with no channel patterns reserved yet."""
        channel_res = reservations.ChannelReservations()
        res = channel_res.add_channel_reservation_callback(
            'channel name',
            lambda x: StdRet.pass_errmsg('x', i18n('expected error')),
        )
        self.assertTrue(res.ok)

        # Ensure it's registered correctly.
        resp = channel_res.reserve_channel('channel name')
        self.assertTrue(resp.has_error)
        err = resp.valid_error
        self.assertEqual(
            'expected error',
            err.messages()[0].message,
        )

    def test_add_channel_reservation_callback__str__duplicate(self) -> None:
        """Call add_channel_reservation_callback with no channel patterns reserved yet."""
        channel_res = reservations.ChannelReservations()
        res = channel_res.add_channel_reservation_callback('channel name', lambda x: RET_OK_NONE)
        self.assertTrue(res.ok)
        res = channel_res.add_channel_reservation_callback('channel name', lambda x: RET_OK_NONE)
        self.assertFalse(res.ok)

    def test_add_channel_reservation_callback__str__escape(self) -> None:
        """Call add_channel_reservation_callback with proper string escaping."""
        channel_res = reservations.ChannelReservations()
        res = channel_res.add_channel_reservation_callback(
            'channel\\d',
            lambda x: StdRet.pass_errmsg('x', i18n('expected error')),
        )
        self.assertTrue(res.ok)

        # Ensure it's registered correctly with escaping.
        self.assertTrue(channel_res.reserve_channel('channel1').ok)
        self.assertTrue(channel_res.reserve_channel('x-channel\\d').ok)
        self.assertTrue(channel_res.reserve_channel('channel\\d-y').ok)
        resp = channel_res.reserve_channel('channel\\d')
        self.assertTrue(resp.has_error)
        err = resp.valid_error
        self.assertEqual(
            'expected error',
            err.messages()[0].message,
        )

    def test_add_channel_reservation_callback__re__empty_set(self) -> None:
        """Call add_channel_reservation_callback with no channel patterns reserved yet."""
        channel_res = reservations.ChannelReservations()
        res = channel_res.add_channel_reservation_callback(
            re.compile(r'channel\d+'),
            lambda x: StdRet.pass_errmsg('x', i18n('expected error')),
        )
        self.assertTrue(res.ok)

        # Ensure it's registered correctly for different matches.
        resp = channel_res.reserve_channel('channel2')
        self.assertTrue(resp.has_error)
        err = resp.valid_error
        self.assertEqual(
            'expected error',
            err.messages()[0].message,
        )

        # Ensure it's registered correctly for different matches.
        resp = channel_res.reserve_channel('channel33')
        self.assertTrue(resp.has_error)
        err = resp.valid_error
        self.assertEqual(
            'expected error',
            err.messages()[0].message,
        )

    def test_add_channel_reservation_callback__re__duplicate(self) -> None:
        """Call add_channel_reservation_callback with no channel patterns reserved yet."""
        channel_res = reservations.ChannelReservations()
        res = channel_res.add_channel_reservation_callback(
            re.compile(r'channel\d+'),
            lambda x: RET_OK_NONE,
        )
        self.assertTrue(res.ok)
        res = channel_res.add_channel_reservation_callback(
            re.compile(r'channel\d+'),
            lambda x: RET_OK_NONE,
        )
        self.assertFalse(res.ok)

    def test_add_channel_reservation_callback__re_str_duplicate(self) -> None:
        """Call add_channel_reservation_callback with no channel patterns reserved yet."""
        channel_res = reservations.ChannelReservations()
        res = channel_res.add_channel_reservation_callback(
            re.compile(r'^channel$'),
            lambda x: RET_OK_NONE,
        )
        self.assertTrue(res.ok)
        res = channel_res.add_channel_reservation_callback(
            'channel',
            lambda x: RET_OK_NONE,
        )
        self.assertFalse(res.ok)

    def test_reserve_channel__duplicate(self) -> None:
        """Run the channel registration twice."""
        channel_res = reservations.ChannelReservations()
        self.assertTrue(channel_res.reserve_channel('abc'))
        res = channel_res.reserve_channel('abc')
        self.assertTrue(res.has_error)
        self.assertEqual(
            'channel name already reserved ({name})',
            res.valid_error.messages()[0].message,
        )

    def test_reserve_channel__first_fails(self) -> None:
        """Run the channel registration once with a failure, which should not mark the
        channel as reserved, then a second time to reserve it, then a third to trigger a
        duplicate."""
        count = [0]

        def callback(_: str) -> StdRet[Optional[EventForwarderTarget]]:
            count[0] += 1
            if count[0] <= 1:
                return StdRet.pass_errmsg(
                    'c', i18n('expected error'),
                )
            return RET_OK_NONE

        channel_res = reservations.ChannelReservations()
        channel_res.add_channel_reservation_callback('abc', callback)
        self.assertEqual(0, count[0])
        res = channel_res.reserve_channel('abc')
        self.assertEqual(1, count[0])
        self.assertFalse(res.ok)
        self.assertEqual(
            'expected error',
            res.valid_error.messages()[0].message,
        )
        self.assertTrue(channel_res.reserve_channel('abc').ok)
        self.assertEqual(2, count[0])
        res = channel_res.reserve_channel('abc')
        self.assertEqual(2, count[0])  # duplicate reached before callback called
        self.assertTrue(res.has_error)
        self.assertEqual(
            'channel name already reserved ({name})',
            res.valid_error.messages()[0].message,
        )

    def test_reserve_release_reserve(self) -> None:
        """Attempt to reserve, release, reserve."""
        channel_res = reservations.ChannelReservations()
        self.assertFalse(channel_res.release_channel('abc'))
        self.assertTrue(channel_res.reserve_channel('abc').ok)
        self.assertFalse(channel_res.reserve_channel('abc').ok)
        self.assertTrue(channel_res.release_channel('abc'))
        self.assertTrue(channel_res.reserve_channel('abc').ok)
        self.assertFalse(channel_res.reserve_channel('abc').ok)
        self.assertTrue(channel_res.release_channel('abc'))
        self.assertFalse(channel_res.release_channel('abc'))
