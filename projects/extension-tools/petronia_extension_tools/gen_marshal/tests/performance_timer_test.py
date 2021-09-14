"""Test the module"""

import unittest
import time
from .. import performance_timer


class PerfTimerTest(unittest.TestCase):
    """Test the class."""

    def test_use_case(self) -> None:
        """Test the common use case for the performance timer."""
        timer = performance_timer.PerfTimer()
        # Use start/stop
        timer.start()
        time.sleep(0.01)
        self.assertGreaterEqual(
            timer.report('1'),
            0.01,
        )
        time.sleep(0.01)
        self.assertGreaterEqual(
            timer.report('2'),
            0.01,
        )

    def test_non_standard_use_case(self) -> None:
        """Test the non-standard use case for the performance timer."""
        timer = performance_timer.PerfTimer()
        # Don't use start
        time.sleep(0.01)
        self.assertGreaterEqual(
            timer.report('3'),
            0.01
        )
