"""Test the module."""

import unittest
from .. import permutations


class PermutationsTest(unittest.TestCase):
    """Test the module functions"""

    def test_one(self) -> None:
        """A single value permutations."""
        vals = permutations.permutations(1)
        self.assertEqual(list(vals), [[0]])

    def test_two(self) -> None:
        """Two values permutations."""
        vals = permutations.permutations(2)
        self.assertEqual(list(vals), [
            [0, 1],
            [1, 0],
        ])

    def test_three(self) -> None:
        """Three values permutations."""
        vals = permutations.permutations(3)
        self.assertEqual(list(vals), [
            [0, 1, 2],
            [0, 2, 1],
            [1, 0, 2],
            [1, 2, 0],
            [2, 0, 1],
            [2, 1, 0],
        ])
