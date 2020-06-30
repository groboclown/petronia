
from typing import Optional
import unittest
from ..global_state import set_global_assertion_state, are_assertions_enabled
from ..assertions import PetroniaAssertionError, enforce_that, assert_that
from ...message import i18n


class AssertionsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__assertion_state = are_assertions_enabled()

    def tearDown(self) -> None:
        set_global_assertion_state(self.__assertion_state)

    def test_assert_that__disabled(self) -> None:
        set_global_assertion_state(False)
        condition = MockCondition(False)
        assert_that("x", "y", condition)
        self.assertEqual(0, condition.run_count)

    def test_assert_that__yes(self) -> None:
        set_global_assertion_state(True)
        condition = MockCondition(True)
        assert_that("x", "y", condition)
        self.assertEqual(1, condition.run_count)

    def test_assert_that__no(self) -> None:
        set_global_assertion_state(True)
        condition = MockCondition(False)
        try:
            assert_that("x", "y", condition)
            self.fail('did not raise exception')
        except PetroniaAssertionError as e:
            self.assertEqual(1, condition.run_count)
            self.assertEqual("PetroniaAssertionError('x: y', None)", repr(e))

    def test_assert_that__exception(self) -> None:
        set_global_assertion_state(True)
        condition = MockCondition(ex=IOError('abc'))
        try:
            assert_that("x", "y", condition)
            self.fail('did not raise exception')
        except PetroniaAssertionError as e:
            self.assertEqual(1, condition.run_count)
            self.assertEqual("PetroniaAssertionError('x: y', OSError('abc'))", repr(e))

    def test_assert_that__multi_1(self) -> None:
        set_global_assertion_state(True)
        condition_1 = MockCondition(True)
        condition_2 = MockCondition(False)
        condition_3 = MockCondition(True)
        try:
            assert_that("x", "y", condition_1, condition_2, condition_3)
            self.fail('did not raise exception')
        except PetroniaAssertionError as e:
            self.assertEqual(1, condition_1.run_count)
            self.assertEqual(1, condition_2.run_count)
            self.assertEqual(0, condition_3.run_count)
            self.assertEqual("PetroniaAssertionError('x: y', None)", repr(e))

    def test_assert_that__multi_2(self) -> None:
        set_global_assertion_state(True)
        condition_1 = MockCondition(True)
        condition_2 = MockCondition(True)
        condition_3 = MockCondition(True)
        assert_that("x", "y", condition_1, condition_2, condition_3)
        self.assertEqual(1, condition_1.run_count)
        self.assertEqual(1, condition_2.run_count)
        self.assertEqual(1, condition_3.run_count)

    def test_enforce_that__no(self) -> None:
        condition = MockCondition(True)
        res = enforce_that("x", i18n("y"), condition)
        self.assertIsNone(res)

    def test_enforce_that__yes(self) -> None:
        # Make sure the global assertion state doesn't affect the enforcement,
        # and that it doesn't cause exceptions.

        set_global_assertion_state(False)
        condition_1 = MockCondition(False)
        res = enforce_that("x", i18n("y"), condition_1)
        self.assertIsNotNone(res)
        self.assertEqual(
            "SimplePetroniaReturnError(UserMessage('{src}: validation error for {problem}', src='x', problem='y'))",
            repr(res),
        )
        self.assertEqual(1, condition_1.run_count)

        set_global_assertion_state(False)
        res = enforce_that("x", i18n("y"), condition_1)
        self.assertIsNotNone(res)
        self.assertEqual(
            "SimplePetroniaReturnError(UserMessage('{src}: validation error for {problem}', src='x', problem='y'))",
            repr(res),
        )
        self.assertEqual(2, condition_1.run_count)

    def test_enforce_that__multiple_1(self) -> None:
        condition_1 = MockCondition(True)
        condition_2 = MockCondition(False)
        condition_3 = MockCondition(True)
        res = enforce_that("x", i18n("y"), condition_1, condition_2, condition_3)
        self.assertIsNotNone(res)
        self.assertEqual(
            "SimplePetroniaReturnError(UserMessage('{src}: validation error for {problem}', src='x', problem='y'))",
            repr(res),
        )
        self.assertEqual(1, condition_1.run_count)
        self.assertEqual(1, condition_2.run_count)
        self.assertEqual(0, condition_3.run_count)

    def test_enforce_that__multiple_2(self) -> None:
        condition_1 = MockCondition(True)
        condition_2 = MockCondition(True)
        condition_3 = MockCondition(True)
        res = enforce_that("x", i18n("y"), condition_1, condition_2, condition_3)
        self.assertIsNone(res)
        self.assertEqual(1, condition_1.run_count)
        self.assertEqual(1, condition_2.run_count)
        self.assertEqual(1, condition_3.run_count)


class MockCondition:
    def __init__(self, ret_val: bool = False, ex: Optional[BaseException] = None) -> None:
        self.ret_val = ret_val
        self.ex = ex
        self.run_count = 0

    def __call__(self, *args, **kwargs) -> bool:
        self.run_count += 1
        if self.ex:
            raise self.ex
        return self.ret_val
