
"""
Extended assertions for typing.
"""

from typing import Optional
import unittest
from ..memory import T


def verified_not_none(value: Optional[T], test_case: unittest.TestCase) -> T:
    """Verifies that the value is not none, and returns the not-none value.
    This is a common enough pattern in unit tests to avoid the mypy required
    assertion after the unit test assertion."""
    test_case.assertIsNotNone(value)
    assert value is not None  # mypy required
    return value
