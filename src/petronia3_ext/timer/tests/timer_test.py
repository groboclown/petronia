
"""
Tests for the timer impl extension
"""

import unittest
import threading
from typing import List, Callable
from petronia3_root.bootstrap.core import create_core_system
from petronia3.extensions.state.api.events import EVENT_ID_UPDATED_STATE, StateStoreUpdatedEvent
from petronia3_root.util.test_helper import BasicQueuer, BasicListener
from ..config import TimerConfig, TARGET_TIMER_CONFIG
from ..bootstrap import BusTimer

class TimerTest(unittest.TestCase):
    """Unit tests for the timer."""
    def test_timer_runner(self) -> None:
        """
        Test out the function that runs in the thread.
        """
        queuer = BasicQueuer(self)
        bus = create_core_system(queuer.pure_queuer)
        timer = BusTimer(bus, TimerConfig(1.0, True))
        timer.mk_thread = mk_thread
        sleeper = SleepFunc(2, timer)
        timer.sleeper = sleeper.sleep

        # This has the chance of running forever if the sleeper isn't written
        # right.
        timer.run()

        self.assertFalse(timer.is_running)
        self.assertEqual(
            sleeper.sleep_times,
            [1.0, 1.0]
        )


def mk_thread(callback: Callable[[], None]) -> threading.Thread:
    """Mock for creating the thread."""
    raise Exception('should not be called')


class SleepFunc:
    """State and sleep function."""
    sleep_times: List[float]

    def __init__(self, max_sleep_calls: int, timer: BusTimer) -> None:
        self.sleep_times = []
        self.max_sleep_calls = max_sleep_calls
        self.timer = timer
        self.call_count = 0


    def sleep(self, secs: float) -> None:
        """Mock for the thread to sleep a while."""
        self.sleep_times.append(secs)
        self.call_count += 1
        if self.call_count > self.max_sleep_calls:
            self.timer.on_config_change(
                EVENT_ID_UPDATED_STATE,
                TARGET_TIMER_CONFIG,
                StateStoreUpdatedEvent(
                    TARGET_TIMER_CONFIG, TimerConfig, TimerConfig(1, False), None
                )
            )
