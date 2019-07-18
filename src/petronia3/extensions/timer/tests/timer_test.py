
import unittest
import threading
from typing import List, Callable
from ..config import TimerConfig
from ..bootstrap import BusTimer
from ..events import TARGET_TIMER
from ....bootstrap.core import create_core_system
from ....system.state.events import EVENT_ID_UPDATED_STATE
from ....util.tests.test_helper import BasicQueuer, BasicListener

class TimerTest(unittest.TestCase):
    def test_timer(self) -> None:
        queuer = BasicQueuer(self)
        bus = create_core_system(queuer.pure_queuer)
        timer = BusTimer(bus, TimerConfig(1.0, False))
        timer.mk_thread = mk_thread
        sleeper = SleepFunc(2, timer)
        timer.sleeper = sleeper.sleep

        # This has the chance of running forever if the sleeper isn't written
        # right.
        timer.run()

        self.assertEqual(
            sleeper.sleep_times,
            [1.0, 1.0]
        )
        self.assertFalse(timer.is_running)


def mk_thread(callback: Callable[[], None]) -> threading.Thread:
    raise Exception('should not be called')


class SleepFunc:
    sleep_times: List[float]

    def __init__(self, max_sleep_calls: int, timer: BusTimer) -> None:
        self.sleep_times = []
        self.max_sleep_calls = max_sleep_calls
        self.timer = timer
        self.call_count = 0


    def sleep(self, secs: float) -> None:
        self.sleep_times.append(secs)
        self.call_count += 1
        if self.call_count > self.max_sleep_calls:
            self.timer.on_config_change(EVENT_ID_UPDATED_STATE, TARGET_TIMER, TimerConfig(1, False))
