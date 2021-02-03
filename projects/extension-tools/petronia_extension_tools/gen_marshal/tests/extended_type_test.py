"""Test the module."""

import unittest
from .. import extended_type


class SourcedTest(unittest.TestCase):
    """Test the Sourced class."""

    def test_suggested_name(self) -> None:
        """Test the suggested_name functionality."""
        src: extended_type.Sourced[str] = extended_type.Sourced()
        self.assertEqual(None, src.suggested_name)
        src.suggested_name = 'a name'
        self.assertEqual('a name', src.suggested_name)
