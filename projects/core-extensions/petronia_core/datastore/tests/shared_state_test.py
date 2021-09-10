"""Test the module."""

import unittest
import time
from .. import shared_state


class SharedStateTest(unittest.TestCase):
    """Test the functions in the module."""

    def test_get_store_data(self) -> None:
        """Test the store_data function."""
        shared_state.clear_data()
        upd1, when1 = shared_state.store_json_data('d1', 'v1')
        self.assertFalse(upd1)
        upd2, when2 = shared_state.store_json_data('d2', 'v2')
        self.assertFalse(upd2)
        self.assertEqual({'d1', 'd2'}, set(shared_state.stored_data_ids()))
        self.assertIsNone(shared_state.get_json_data('d0'))
        self.assertEqual(('v1', when1), shared_state.get_json_data('d1'))
        self.assertEqual(('v2', when2), shared_state.get_json_data('d2'))

        # Updating data means time stamp must be different.
        upd1a, when1a = shared_state.store_json_data('d1', 'v1a')
        self.assertTrue(upd1a)
        self.assertNotEqual(when1, when1a)
        self.assertEqual({'d1', 'd2'}, set(shared_state.stored_data_ids()))
        self.assertEqual(('v1a', when1a), shared_state.get_json_data('d1'))

        # Updating data means the time must be different, even if the data values are identical.
        upd2a, when2a = shared_state.store_json_data('d2', 'v2')
        self.assertTrue(upd2a)
        self.assertNotEqual(when2, when2a)

        # force the time to advance a bit, and ensure the times are still different.
        time.sleep(0.1)
        upd2b, when2b = shared_state.store_json_data('d2', 'v2')
        self.assertTrue(upd2b)
        self.assertNotEqual(when2a, when2b)
