
import unittest
from ..bootstrap import bootstrap_state_store
from ...bus import EventRegistry, TypeSafeEventBus
from ...bus.event_bus import EventBus
from ...bus.bootstrap import (
    register_event_registry_events,
    add_event_registry_listener,
)
from ...logging import TRACE, log
from ....util.tests.test_helper import BasicQueuer, EnabledLogs

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
