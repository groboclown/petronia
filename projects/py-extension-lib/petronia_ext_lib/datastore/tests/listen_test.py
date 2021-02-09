"""Test the module."""

from typing import List, Optional
import unittest
import datetime
import json
from petronia_common.util import tznow, not_none
from .. import listen
from ...events import timer, datastore
from ...runner import EventObjectParser


class CachedInstanceTest(unittest.TestCase):
    """Test the CachedInstance class."""

    def test_init(self) -> None:
        """Test the initial state.  Uses the timer event object for testing."""
        cached: listen.CachedInstance[timer.HeartbeatEvent] = listen.CachedInstance(
            EventObjectParser(timer.HeartbeatEvent.parse_data), None,
        )
        self.assertIsNone(cached.value)
        self.assertIsNone(cached.callback)

    def test_use_case__with_callback(self) -> None:
        """A use case for testing the major behavior."""

        callback_values: List[Optional[timer.HeartbeatEvent]] = []

        def update_callback(val: Optional[timer.HeartbeatEvent]) -> None:
            callback_values.append(val)

        cached = listen.CachedInstance(
            EventObjectParser(timer.HeartbeatEvent.parse_data), update_callback,
        )
        cached.on_delete()
        self.assertEqual([], callback_values)
        self.assertIsNone(cached.value)

        data1 = timer.HeartbeatEvent(tznow() - datetime.timedelta(hours=-3))
        data1_raw = json.dumps(data1.export_data())

        # Ensure the time for sending != time on the cache.
        update1 = datastore.DataUpdateEvent(
            tznow() - datetime.timedelta(days=-5), data1_raw,
        )
        res = cached.update(update1)
        self.assertIsNone(res.error)
        self.assertEqual(1, len(callback_values))
        self.assertEqual(data1.sent_on, not_none(callback_values[0]).sent_on)
        self.assertIs(cached.value, callback_values[0])

        # Try sending the same event again, which replicates the datastore service resending
        # the stored value.
        res = cached.update(update1)
        self.assertIsNone(res.error)
        self.assertEqual(1, len(callback_values))
        self.assertIs(cached.value, callback_values[0])

        # Try sending an updated event.
        data2 = timer.HeartbeatEvent(tznow() - datetime.timedelta(hours=-2))
        data2_raw = json.dumps(data2.export_data())
        update2 = datastore.DataUpdateEvent(
            tznow() - datetime.timedelta(days=-2), data2_raw,
        )
        res = cached.update(update2)
        self.assertIsNone(res.error)
        self.assertEqual(2, len(callback_values))
        self.assertEqual(data2.sent_on, not_none(callback_values[1]).sent_on)
        self.assertIs(cached.value, callback_values[1])

        # Remove the value
        cached.on_delete()
        self.assertEqual(3, len(callback_values))
        self.assertIsNone(callback_values[2])
        self.assertIsNone(cached.value)

        # Re-Send an update event.
        res = cached.update(update1)
        self.assertIsNone(res.error)
        self.assertEqual(4, len(callback_values))
        self.assertEqual(data1.sent_on, not_none(callback_values[3]).sent_on)
        self.assertIs(cached.value, callback_values[3])

    def test_use_case__without_callback(self) -> None:
        """A use case for testing the major behavior."""

        cached = listen.CachedInstance(
            EventObjectParser(timer.HeartbeatEvent.parse_data), None,
        )
        cached.on_delete()
        self.assertIsNone(cached.value)

        data1 = timer.HeartbeatEvent(tznow() - datetime.timedelta(hours=-3))
        data1_raw = json.dumps(data1.export_data())

        # Ensure the time for sending != time on the cache.
        update1 = datastore.DataUpdateEvent(
            tznow() - datetime.timedelta(days=-5), data1_raw,
        )
        res = cached.update(update1)
        self.assertIsNone(res.error)
        self.assertIsNotNone(cached.value)
        self.assertEqual(data1.sent_on, not_none(cached.value).sent_on)

        # Try sending the same event again, which replicates the datastore service resending
        # the stored value.
        pre_data = cached.value
        res = cached.update(update1)
        self.assertIsNone(res.error)
        self.assertIsNotNone(cached.value)
        self.assertIs(pre_data, cached.value)

        # Try sending an updated event.
        data2 = timer.HeartbeatEvent(tznow() - datetime.timedelta(hours=-2))
        data2_raw = json.dumps(data2.export_data())
        update2 = datastore.DataUpdateEvent(
            tznow() - datetime.timedelta(days=-2), data2_raw,
        )
        res = cached.update(update2)
        self.assertIsNone(res.error)
        self.assertEqual(data2.sent_on, not_none(cached.value).sent_on)

        # Remove the value
        cached.on_delete()
        self.assertIsNone(cached.value)

        # Re-Send an update event.
        res = cached.update(update1)
        self.assertIsNone(res.error)
        self.assertEqual(data1.sent_on, not_none(cached.value).sent_on)
