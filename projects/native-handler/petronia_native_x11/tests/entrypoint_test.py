"""Test the module."""

import unittest
from .. import entrypoint


class EntrypointTest(unittest.TestCase):
    """Test the functions in the module."""

    def test_parse_config(self) -> None:
        """Test parse_config with data."""
        config = {'connection': {'replace_existing_wm': True}}
        res = entrypoint.parse_config(config)
        self.assertEqual([], [m.debug() for m in res.error_messages()])
        self.assertIsNotNone(res.value)
