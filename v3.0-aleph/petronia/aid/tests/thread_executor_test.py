
from typing import Optional
import unittest
from threading import Barrier
from ..test_helper import (
    BasicQueuer,
    load_core_extensions,
    bootstrap_event_bus,
)
from ..thread.executor import ThreadedExecutor


class ThreadedExecutorTest(unittest.TestCase):
    executor: Optional[ThreadedExecutor]

    def setUp(self) -> None:
        self.queue = BasicQueuer(self)
        self.bus = bootstrap_event_bus(self.queue.pure_queuer)
        load_core_extensions(self.bus)
        self.executor = None

    def tearDown(self) -> None:
        if self.executor:
            self.executor.stop(10)
            self.assertFalse(self.executor.is_alive())

    def test_queue_after_stop(self) -> None:
        self.executor = ThreadedExecutor[str](self.bus, 'test_queue_after_stop', True, lambda x: None, lambda x: False)
        self.executor.stop(-1)
        try:
            self.executor.add_execution('')
            self.fail('Did not raise error after add_execution')
        except RuntimeError:
            pass

    def test_queue_after_drain(self) -> None:
        self.executor = ThreadedExecutor[str](self.bus, 'test_queue_after_stop', True, lambda x: None, lambda x: False)
        self.executor.begin_drain()
        try:
            self.executor.add_execution('')
            self.fail('Did not raise error after add_execution')
        except RuntimeError:
            pass

    def test_queue_two(self) -> None:
        pass
