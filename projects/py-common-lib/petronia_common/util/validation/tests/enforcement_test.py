
"""Tests the enforcement module."""

from typing import Optional
import unittest
from ..enforcement import enforce_that, enforce_all
from ... import not_none
from ...message import i18n, STANDARD_PETRONIA_CATALOG


class EnforcementTest(unittest.TestCase):
    """Checks the enforcement API"""

    def test_enforce_that__no(self) -> None:
        """Enforcement that's good."""
        condition = MockCondition(True)
        res = enforce_that("x", 'c', i18n("y"), condition)
        self.assertIsNone(res)

    def test_enforce_that__yes(self) -> None:
        """Enforcement that fails."""
        condition_1 = MockCondition(False)
        res = enforce_that("x", 'c', i18n("y"), condition_1)
        self.assertIsNotNone(res)
        self.assertEqual(
            [('x: validation error', STANDARD_PETRONIA_CATALOG), ('y', 'c')],
            [(m.debug(), m.catalog) for m in not_none(res).messages()],
        )
        self.assertEqual(1, condition_1.run_count)

        res = enforce_that("x", 'c', i18n("y"), condition_1)
        self.assertIsNotNone(res)
        self.assertEqual(
            [('x: validation error', STANDARD_PETRONIA_CATALOG), ('y', 'c')],
            [(m.debug(), m.catalog) for m in not_none(res).messages()],
        )
        self.assertEqual(2, condition_1.run_count)

    def test_enforce_that__multiple_1(self) -> None:
        """Three enforcements, middle is bad."""
        condition_1 = MockCondition(True)
        condition_2 = MockCondition(False)
        condition_3 = MockCondition(True)
        res = enforce_that("x", 'c', i18n("y"), condition_1, condition_2, condition_3)
        self.assertIsNotNone(res)
        self.assertEqual(
            [('x: validation error', STANDARD_PETRONIA_CATALOG), ('y', 'c')],
            [(m.debug(), m.catalog) for m in not_none(res).messages()],
        )
        self.assertEqual(1, condition_1.run_count)
        self.assertEqual(1, condition_2.run_count)
        self.assertEqual(0, condition_3.run_count)

    def test_enforce_that__multiple_2(self) -> None:
        """Three enforcements, all good."""
        print("Running test_enforce_that__multiple_2")
        condition_1 = MockCondition(True)
        condition_2 = MockCondition(True)
        condition_3 = MockCondition(True)
        res = enforce_that("x", 'c', i18n("y"), condition_1, condition_2, condition_3)
        self.assertIsNone(res)
        self.assertEqual(1, condition_1.run_count)
        self.assertEqual(1, condition_2.run_count)
        self.assertEqual(1, condition_3.run_count)

    def test_enforce_that__exception_1(self) -> None:
        """Once enforcement, and it raises an exception."""
        ex = IOError('abc')
        condition_1 = MockCondition(ex=ex)
        condition_2 = MockCondition(True)
        res = enforce_that("x", 'c', i18n("y"), condition_1, condition_2)
        self.assertEqual(1, condition_1.run_count)
        self.assertEqual(0, condition_2.run_count)
        self.assertIsNotNone(res)
        self.assertEqual(
            [('x: validation error (abc)', STANDARD_PETRONIA_CATALOG), ('y', 'c')],
            [(m.debug(), m.catalog) for m in not_none(res).messages()],
        )

    def test_enforce_all__1_ok(self) -> None:
        """Once enforcement, and it's good."""
        condition_1 = MockCondition(True)
        res = enforce_all('abc', 'c', (i18n('b'), condition_1,))
        self.assertEqual(1, condition_1.run_count)
        self.assertIsNone(res)

    def test_enforce_all__1_bad(self) -> None:
        """Once enforcement, and it's bad."""
        condition_1 = MockCondition(False)
        res = enforce_all('abc', 'c', (i18n('b'), condition_1,))
        self.assertEqual(1, condition_1.run_count)
        self.assertIsNotNone(res)
        self.assertEqual(
            [('abc: validation error', STANDARD_PETRONIA_CATALOG), ('b', 'c')],
            [(m.debug(), m.catalog) for m in not_none(res).messages()],
        )

    def test_enforce_all__2_ok(self) -> None:
        """Multiple enforcements, all ok."""
        condition_1 = MockCondition(True)
        condition_2 = MockCondition(True)
        res = enforce_all(
            'abc', 'cx',
            (i18n('b'), condition_1,),
            (i18n('c'), condition_2,),
        )
        self.assertEqual(1, condition_1.run_count)
        self.assertEqual(1, condition_2.run_count)
        self.assertIsNone(res)

    def test_enforce_all__2_bad(self) -> None:
        """Multiple enforcements, all bad."""
        condition_1 = MockCondition(False)
        condition_2 = MockCondition(False)
        res = enforce_all(
            'abc', 'cx',
            (i18n('b'), condition_1,),
            (i18n('c'), condition_2,),
        )
        self.assertEqual(1, condition_1.run_count)
        self.assertEqual(1, condition_2.run_count)
        self.assertIsNotNone(res)
        self.assertEqual(
            [('abc: validation error', STANDARD_PETRONIA_CATALOG), ('b', 'cx'), ('c', 'cx')],
            [(m.debug(), m.catalog) for m in not_none(res).messages()],
        )

    def test_enforce_all__1_error(self) -> None:
        """Enforce with 1 raised exception"""
        ex_1 = IOError('x')
        condition_1 = MockCondition(ex=ex_1)
        res = enforce_all('abcd', 'c', (i18n('x'), condition_1,))
        self.assertEqual(1, condition_1.run_count)
        self.assertIsNotNone(res)
        assert res is not None  # mypy required
        messages = res.messages()
        self.assertEqual(2, len(messages))
        self.assertEqual('abcd: validation error', messages[0].debug())
        self.assertEqual('{src}: validation error ({e})', messages[1].message)
        self.assertEqual({"e": ex_1, "src": "abcd"}, messages[1].arguments)

    def test_enforce_all__2_error(self) -> None:
        """Enforce with 2 raised exception."""
        ex_1 = IOError('x')
        ex_2 = IOError('y')
        condition_1 = MockCondition(ex=ex_1)
        condition_2 = MockCondition(ex=ex_2)
        res = enforce_all('abcd', 'c', (i18n('x'), condition_1,), (i18n('y'), condition_2,))
        self.assertEqual(1, condition_1.run_count)
        self.assertEqual(1, condition_2.run_count)
        self.assertIsNotNone(res)
        assert res is not None  # mypy required
        messages = res.messages()
        self.assertEqual(3, len(messages))
        self.assertEqual('abcd: validation error', messages[0].debug())
        self.assertEqual('{src}: validation error ({e})', messages[1].message)
        self.assertEqual({"e": ex_1, "src": "abcd"}, messages[1].arguments)
        self.assertEqual('{src}: validation error ({e})', messages[2].message)
        self.assertEqual({"e": ex_2, "src": "abcd"}, messages[2].arguments)


class MockCondition:
    """A mock condition function."""
    def __init__(self, ret_val: bool = False, ex: Optional[BaseException] = None) -> None:
        self.ret_val = ret_val
        self.ex = ex
        self.run_count = 0

    def __call__(self) -> bool:
        self.run_count += 1
        if self.ex:
            raise self.ex
        return self.ret_val
