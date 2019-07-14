
import unittest
from ...bus import EventRegistry
from ..bus import register_events

class BusTest(unittest.TestCase):
    def test_register_events(self):
        reg = EventRegistry()
        register_events(reg)
