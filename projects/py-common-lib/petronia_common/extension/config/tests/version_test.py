
"""version module test"""

import unittest
from .. import version


class VersionTest(unittest.TestCase):
    """Test version functions"""
    def test_cmp_versions__equal(self) -> None:
        """version cmp_extension"""
        self.assertEqual(
            0,
            version.cmp_extension((1, 1, 0), (1, 1, 0)),
        )

    def test_cmd_versions__lt_0(self) -> None:
        """version cmp_extension"""
        self.assertEqual(
            -3,
            version.cmp_extension((1, 2, 3), (4, 4, 0))
        )

    def test_cmd_versions__lt_1(self) -> None:
        """version cmp_extension"""
        self.assertEqual(
            -2,
            version.cmp_extension((1, 2, 3), (1, 4, 0))
        )

    def test_cmd_versions__lt_2(self) -> None:
        """version cmp_extension"""
        self.assertEqual(
            -6,
            version.cmp_extension((1, 2, 3), (1, 2, 9))
        )

    def test_cmd_versions__gt_0(self) -> None:
        """version cmp_extension"""
        self.assertEqual(
            3,
            version.cmp_extension((4, 4, 0), (1, 2, 3))
        )

    def test_cmd_versions__gt_1(self) -> None:
        """version cmp_extension"""
        self.assertEqual(
            2,
            version.cmp_extension((1, 4, 0), (1, 2, 3))
        )

    def test_cmd_versions__gt_2(self) -> None:
        """version cmp_extension"""
        self.assertEqual(
            6,
            version.cmp_extension((1, 2, 9), (1, 2, 3))
        )
