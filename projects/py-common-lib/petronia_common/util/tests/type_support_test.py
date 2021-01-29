
"""Test the type_support module."""

import unittest
from .. import type_support


class TypeSupportTest(unittest.TestCase):
    """Test the type_support functions."""

    def test_without_none__empty(self) -> None:
        """Test without_none with no values."""
        self.assertEqual(
            [],
            type_support.without_none([]),
        )

    def test_without_none__no_none(self) -> None:
        """Test without_none with no values."""
        self.assertEqual(
            [1, 2],
            type_support.without_none([1, 2]),
        )

    def test_without_none__nones(self) -> None:
        """Test without_none with no values."""
        self.assertEqual(
            [1, 2, 3],
            type_support.without_none([1, 2, None, None, 3]),
        )

    def test_without_none__mixed_type(self) -> None:
        """Test without_none with no values."""
        self.assertEqual(
            [1, "x", 3],
            type_support.without_none([1, "x", None, None, 3]),
        )

    def test_not_none__none(self) -> None:
        """Test not_none with a none value"""
        try:
            type_support.not_none(None)
            self.fail('Did not raise assertion failure.')  # pragma no cover
        except ValueError as err:
            self.assertEqual('value assumed not None but is None', str(err))

    def test_not_none__not_none(self) -> None:
        """Test not_none with non-none values"""
        self.assertEqual('s', type_support.not_none('s'))
        self.assertEqual(0, type_support.not_none(0))
        self.assertEqual(0.0, type_support.not_none(0.0))
