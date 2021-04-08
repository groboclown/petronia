
import unittest
from ..loop import permutations


class PermutationTest(unittest.TestCase):
    def test_one(self):
        vals = permutations(1)
        self.assertEqual(list(vals), [[0]])

    def test_two(self):
        vals = permutations(2)
        self.assertEqual(list(vals), [
            [0, 1],
            [1, 0],
        ])

    def test_three(self):
        vals = permutations(3)
        self.assertEqual(list(vals), [
            [0, 1, 2],
            [0, 2, 1],
            [1, 0, 2],
            [1, 2, 0],
            [2, 0, 1],
            [2, 1, 0],
        ])
