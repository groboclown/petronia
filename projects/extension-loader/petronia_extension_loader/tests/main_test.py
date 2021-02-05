"""Test the module."""

import unittest
from .. import main


class ExtensionLoaderMainTest(unittest.TestCase):
    """Test the main function."""

    def test_bad_fd(self) -> None:
        """Test with a bad write fd"""
        res = main.main(['x'])
        self.assertEqual(1, res)
