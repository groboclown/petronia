"""Test the module."""

import unittest
from .. import router_loop
from ...events import foreman


class RouterLoopLogicTest(unittest.TestCase):
    """Test the class and functions in the module."""

    def test_get_handler_id(self) -> None:
        """Test the create_handler_id function."""
        self.assertEqual(
            foreman.EXTENSION_NAME + ':ext1',
            router_loop.get_handler_id('ext1'),
        )
