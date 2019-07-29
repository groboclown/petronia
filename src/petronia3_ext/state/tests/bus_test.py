
import unittest
from petronia3.system.logging import TRACE, log
from petronia3_root.util.test_helper import (
    BasicQueuer, EnabledLogs,
    bootstrap_event_bus,
    load_core_extensions,
)
from ..bootstrap import bootstrap_state_store

class BusTest(unittest.TestCase):
    def test_register_events(self):
        with EnabledLogs(TRACE):
            log(TRACE, BusTest, "Starting test_register_events")

            # Setup
            queue = BasicQueuer(self)
            bus = bootstrap_event_bus(queue.pure_queuer)
            load_core_extensions(bus)
            bootstrap_state_store(bus)
