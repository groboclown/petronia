
import unittest
from petronia3.system.logging import TRACE, log
from petronia3.extensions.state.api.bootstrap import bootstrap_state_store_api
from petronia3_root.util.test_helper import (
    BasicQueuer, EnabledLogs,
    create_core_system,
)
from ..bootstrap import bootstrap_state_store

class BusTest(unittest.TestCase):
    def test_register_events(self):
        with EnabledLogs(TRACE):
            log(TRACE, BusTest, "Starting test_register_events")

            # Setup
            queue = BasicQueuer(self)
            bus = create_core_system(queue.pure_queuer)
            bootstrap_state_store_api(bus)
            bootstrap_state_store(bus)
