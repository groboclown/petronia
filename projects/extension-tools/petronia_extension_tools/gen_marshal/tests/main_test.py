"""Test the module."""

import unittest
from .. import main


class MainTest(unittest.TestCase):
    """Test the functions."""

    def test_normalize_name__simple(self) -> None:
        """Test normalize_name function with a simple string."""
        res = main.normalize_name('abc')
        self.assertEqual(res, 'abc')

    def test_normalize_name__replaced(self) -> None:
        """Test normalize_name function with a value that needs replacement."""
        res = main.normalize_name('abc-^.2^3')
        self.assertEqual(res, '2_3')
