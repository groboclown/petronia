
import unittest
from ..global_state import are_assertions_enabled, set_global_assertion_state


class GlobalStateTest(unittest.TestCase):
    def test_enable(self) -> None:
        set_global_assertion_state(True)
        self.assertTrue(are_assertions_enabled())

    def test_disable(self) -> None:
        set_global_assertion_state(False)
        self.assertFalse(are_assertions_enabled())
