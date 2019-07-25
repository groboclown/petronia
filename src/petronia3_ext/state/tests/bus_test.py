
import unittest
from petronia3.system.logging import TRACE, log
from petronia3.util.tests.test_helper import BasicQueuer, EnabledLogs
from petronia3_root.bootstrap import (
    register_event_registry_events,
    add_event_registry_listener,
)
from ..bootstrap import bootstrap_state_store

class BusTest(unittest.TestCase):
    def test_register_events(self):
        with EnabledLogs(TRACE):
            log(TRACE, BusTest, "Starting test_register_events")

            # Setup
            evtr = EventRegistry()
            register_event_registry_events(evtr)
            queue = BasicQueuer(self)
            bus = EventBus(queue.pure_queuer)
            typesafe = TypeSafeEventBus(bus, evtr)
            add_event_registry_listener(typesafe, evtr)

            bootstrap_state_store(typesafe)
