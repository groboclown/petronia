
# Usage: python3 -m unittest petronia.tests.layout_navigation

import unittest

from ..system.bus import SingleThreadedBus
from ..system.component import Component
from ..system import event_ids, target_ids


class BusCallbackTests(unittest.TestCase):
    def test_multiple_events_one_callback(self):
        bus = SingleThreadedBus()

        found_events = []

        def single_callback(event_id, target_id, event_obj):
            found_events.append((event_id, target_id, event_obj))

        bus.add_listener(event_ids.CONFIG__UPDATE, target_ids.ANY, single_callback)
        bus.add_listener(event_ids.CONFIG__REQUEST_LOAD, target_ids.ANY, single_callback)

        bus.fire(event_ids.CONFIG__UPDATE, target_ids.BROADCAST, {})
        self.assertEqual(len(found_events), 1,
                         "first event: {0}".format(found_events))
        bus.fire(event_ids.CONFIG__REQUEST_LOAD, target_ids.BROADCAST, {})
        self.assertEqual(len(found_events), 2,
                         "second event: {0}".format(found_events))

    def test_component_multiple_listen(self):
        bus = SingleThreadedBus()
        cp = MultipleListen(bus)

        bus.fire(event_ids.CONFIG__UPDATE, target_ids.BROADCAST, {})
        self.assertEqual(len(cp.found_events), 1,
                         "first event: {0}".format(cp.found_events))
        bus.fire(event_ids.CONFIG__REQUEST_LOAD, target_ids.BROADCAST, {})
        self.assertEqual(len(cp.found_events), 2,
                         "second event: {0}".format(cp.found_events))


class MultipleListen(Component):
    def __init__(self, bus):
        Component.__init__(self, bus)
        self.found_events = []

        self._listen(event_ids.CONFIG__UPDATE, target_ids.ANY, self.single_callback)
        self._listen(event_ids.CONFIG__REQUEST_LOAD, target_ids.ANY, self.single_callback)

    def single_callback(self, event_id, target_id, event_obj):
        self.found_events.append((event_id, target_id, event_obj))


if __name__ == '__main__':
    unittest.main()
