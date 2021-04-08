
"""
Tests for the timer impl extension
"""

import unittest
import threading
from typing import List, Callable
from ....base import EventBus
from ....boot.bootstrap.bus import bootstrap_event_bus
from ....core.timer.api.bootstrap import bootstrap_timer_api
from ....core.state.api.events import EVENT_ID_UPDATED_STATE, StateStoreUpdatedEvent
from ....core.state.api.bootstrap import bootstrap_state_store_api
from ....aid.test_helper import BasicQueuer
from ..config import TimerConfig, TARGET_TIMER_CONFIG
from ..bootstrap import BusTimer


class TimerTest(unittest.TestCase):
    """Unit tests for the timer."""
    def test_timer_runner(self) -> None:
        """
        Test out the function that runs in the thread.
        """
        queuer = BasicQueuer(self)
        bus = bootstrap_event_bus(queuer.pure_queuer)
        bootstrap_state_store_api(bus)
        bootstrap_timer_api(bus)
        timer = BusTimer(bus, TimerConfig(1.0, True))
        timer.mk_thread = mk_thread
        sleeper = SleepFunc(2, timer)
        timer.sleeper = sleeper.sleep

        # This has the chance of running forever if the sleeper isn't written
        # right.
        while timer.is_config_active():
            timer.run_in_loop()

        self.assertFalse(timer.is_running)
        self.assertEqual(
            len(sleeper.sleep_times),
            2
        )
        # This can return anywhere between 0 and 1, depending upon the speed
        # of the thread execution.
        self.assertLessEqual(sleeper.sleep_times[0], 1.0)
        self.assertLessEqual(sleeper.sleep_times[1], 1.0)


def mk_thread(
        bus: EventBus, is_alive: Callable[[], bool], callback: Callable[[], None]
) -> threading.Thread:
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
        if self.call_count >= self.max_sleep_calls:
            self.timer.on_config_change(
                EVENT_ID_UPDATED_STATE,
                TARGET_TIMER_CONFIG,
                StateStoreUpdatedEvent(
                    TARGET_TIMER_CONFIG, TimerConfig, TimerConfig(1, False), None
                )
            )
