"""Test the module."""

from typing import Sequence, List, Tuple
import unittest
from petronia_common.extension.config.extension_schema import ExtensionVersion
from .. import extension_info


class ExtensionInfoHelperTest(unittest.TestCase):
    """Test the functions in the module."""

    def test_list_as_extension_version(self) -> None:
        """Test the function list_as_extension_version"""
        test_data: Sequence[Tuple[List[int], ExtensionVersion]] = [
            ([3, 4, 5, 6], (3, 4, 5)),
            ([3, 4, 5], (3, 4, 5)),
            ([6, 7], (6, 7, 0)),
            ([1], (1, 0, 0)),
            ([], (0, 0, 0)),
        ]
        for val, expected in test_data:
            with self.subTest(str(val)):
                self.assertEqual(expected, extension_info.list_as_extension_version(val))
