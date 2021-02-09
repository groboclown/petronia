"""Test the module."""

import unittest
import datetime
from .. import tzdate


class TzDateTest(unittest.TestCase):
    """Test the functions."""

    def test_now__has_timezone(self) -> None:
        """Test that now has the timezone, and that it is the current time but in UTC."""
        dt_now = datetime.datetime.now()
        tz_now = tzdate.tznow()

        self.assertEqual(tz_now.tzinfo, datetime.timezone.utc)

        as_local = tz_now.astimezone()
        self.assertAlmostEqual(
            as_local.timestamp(),
            dt_now.timestamp(),
            delta=2.0,
        )
