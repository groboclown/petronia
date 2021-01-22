"""Test the module."""

import unittest
from .. import main


class ForemanMainTest(unittest.TestCase):
    """Test the main function."""

    def test_bad_platform(self) -> None:
        """Test running main with a forced platform name that isn't known."""
        res = main.main(['foreman', '-p', 'unknown'])
        self.assertEqual(1, res)
