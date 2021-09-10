
"""Test the module"""

import unittest
import io
from .. import defs


class DefsModuleTest(unittest.TestCase):
    """Test functions in the module."""

    def test_convert_reader_to_raw(self) -> None:
        """Test convert_reader_to_raw"""
        reader = io.BytesIO(b'my-bits')
        raw = defs.convert_reader_to_raw(reader)
        res = raw(3) + raw()
        self.assertEqual(res, b'my-bits')
