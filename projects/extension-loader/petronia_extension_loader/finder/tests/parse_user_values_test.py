"""Test the module"""

from typing import List, Tuple, Optional
import unittest
from .. import parse_user_values


class ParseUserValuesTest(unittest.TestCase):
    """Test the functions in the module."""

    DATA: List[Tuple[str, str, str, Optional[int], Optional[int], Optional[int]]] = [
        ('no version', 'my.ext', 'my.ext', None, None, None),
        ('no major', 'my.ext:', 'my.ext', None, None, None),
        ('bad major', 'my.ext:x', 'my.ext', None, None, None),
        ('good major', 'my.ext:134', 'my.ext', 134, None, None),
        ('bad major, good minor', 'my.ext:xx.134', 'my.ext', None, None, None),
        ('bad major, good minor, good patch', 'my.ext:xx.134.6', 'my.ext', None, None, None),
        ('good major, bad minor', 'my.ext:3.x', 'my.ext', 3, None, None),
        ('good major, good minor', 'my.ext:3.990', 'my.ext', 3, 990, None),
        ('good major, bad minor, good patch', 'my.ext:3.x.6', 'my.ext', 3, None, None),
        ('good major, good minor, bad patch', 'my.ext:3.6.x', 'my.ext', 3, 6, None),
        ('good major, good minor, good patch', 'my.ext:3.6.0', 'my.ext', 3, 6, 0),
    ]

    def test_parse_extension_name_version(self) -> None:
        """Test parse_extension_name_version with no version information"""
        for (
                test, key, expected_name, expected_major, expected_minor, expected_patch,
        ) in ParseUserValuesTest.DATA:
            with self.subTest(test):
                name, major, minor, patch = parse_user_values.parse_extension_name_version(key)
                self.assertEqual(expected_name, name)
                self.assertEqual(expected_major, major)
                self.assertEqual(expected_minor, minor)
                self.assertEqual(expected_patch, patch)
