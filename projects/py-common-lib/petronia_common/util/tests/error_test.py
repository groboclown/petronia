
from typing import Optional
import unittest
from .. import error
from ..message import UserMessage, UserMessageData, i18n


class StdRetTest(unittest.TestCase):
    def test_pass_error_0(self) -> None:
        """No error messages"""
        ret: error.StdRet[str] = error.StdRet.pass_error()
        self.assertIsNotNone(ret)
        self.assertEqual(
            tuple(),
            ret.error_messages(),
        )
        self.assertTrue(ret.has_error)
        self.assertFalse(ret.ok)
        self.assertIsNotNone(ret.error)
        self.assertIsNotNone(ret.valid_error)
        self.assertIsNone(ret.value)
        self.assertFalse(ret.not_none)

        forwarded: error.StdRet[float] = ret.forward()
        # Ensure the same memory is used.
        self.assertIs(ret, forwarded)

    def test_pass_error_1(self) -> None:
        """One error message"""
        ret: error.StdRet[str] = error.StdRet.pass_error(error.join_errors(_m('1')))
        self.assertIsNotNone(ret)
        self.assertEqual(
            (_m('1'),),
            ret.error_messages(),
        )
        self.assertTrue(ret.has_error)
        self.assertFalse(ret.ok)
        self.assertIsNotNone(ret.error)
        self.assertIsNotNone(ret.valid_error)
        self.assertIsNone(ret.value)
        self.assertFalse(ret.not_none)

    def test_pass_error_2(self) -> None:
        """One error message"""
        ret: error.StdRet[str] = error.StdRet.pass_error(
            error.join_errors(_m('1')), error.join_errors(_m('2')),
        )
        self.assertIsNotNone(ret)
        self.assertEqual(
            (_m('1'), _m('2'),),
            ret.error_messages(),
        )
        self.assertTrue(ret.has_error)
        self.assertFalse(ret.ok)
        self.assertIsNotNone(ret.error)
        self.assertIsNotNone(ret.valid_error)
        self.assertIsNone(ret.value)
        self.assertFalse(ret.not_none)

    def test_pass_errmsg_0(self) -> None:
        """Error message with no arguments"""
        ret: error.StdRet[str] = error.StdRet.pass_errmsg(i18n('xyz'))
        self.assertIsNotNone(ret)
        self.assertEqual(
            (_m('xyz'),),
            ret.error_messages(),
        )
        self.assertTrue(ret.has_error)
        self.assertFalse(ret.ok)
        self.assertIsNotNone(ret.error)
        self.assertIsNotNone(ret.valid_error)
        self.assertIsNone(ret.value)
        self.assertFalse(ret.not_none)

    def test_pass_errmsg_1(self) -> None:
        """Error message with an argument"""
        ret: error.StdRet[str] = error.StdRet.pass_errmsg(i18n('xy{x}z'), x=2)
        self.assertIsNotNone(ret)
        self.assertEqual(
            (_m('xy{x}z', x=2),),
            ret.error_messages(),
        )
        self.assertTrue(ret.has_error)
        self.assertFalse(ret.ok)
        self.assertIsNotNone(ret.error)
        self.assertIsNotNone(ret.valid_error)
        self.assertIsNone(ret.value)
        self.assertFalse(ret.not_none)

    def test_pass_ok_0(self) -> None:
        """No error message, None value."""
        ret: error.StdRet[Optional[str]] = error.StdRet.pass_ok(None)
        self.assertIsNotNone(ret)
        self.assertEqual(tuple(), ret.error_messages())
        self.assertFalse(ret.has_error)
        self.assertTrue(ret.ok)
        self.assertIsNone(ret.error)
        self.assertIsNone(ret.value)
        self.assertFalse(ret.not_none)

    def test_pass_ok_1(self) -> None:
        """No error message, None value."""
        ret = error.StdRet.pass_ok('x')
        self.assertIsNotNone(ret)
        self.assertEqual(tuple(), ret.error_messages())
        self.assertFalse(ret.has_error)
        self.assertTrue(ret.ok)
        self.assertIsNone(ret.error)
        self.assertTrue(ret.not_none)
        self.assertEqual('x', ret.value)
        self.assertEqual('x', ret.result)

    def test_pass_exception_1(self) -> None:
        ex = IOError('1')
        ret: error.StdRet[int] = error.StdRet.pass_exception(i18n('a'), ex, a=1, b='a')
        self.assertIsNotNone(ret)
        self.assertTrue(ret.has_error)
        self.assertFalse(ret.ok)
        self.assertIsNotNone(ret.error)
        self.assertFalse(ret.not_none)
        self.assertIsNone(ret.value)
        err = ret.error
        assert err is not None  # mypy required
        self.assertEqual(1, len(err.messages()))
        self.assertIsInstance(err, error.ExceptionPetroniaReturnError)
        assert isinstance(err, error.ExceptionPetroniaReturnError)  # mypy required
        self.assertEqual(ex, err.exception())
        self.assertEqual(
            "ExceptionPetroniaReturnError(UserMessage('a', a=1, b='a', exception=OSError('1')), OSError('1'))",
            repr(err),
        )


class FunctionTest(unittest.TestCase):
    def test_possible_error_0_0_a(self) -> None:
        res = error.possible_error()
        self.assertIsNone(res)

    def test_possible_error_0_0_b(self) -> None:
        res = error.possible_error(messages=[], errors=[])
        self.assertIsNone(res)

    def test_possible_error_0_1(self) -> None:
        res = error.possible_error(
            messages=[], errors=[error.SimplePetroniaReturnError()],
        )
        self.assertIsNotNone(res)
        assert res is not None  # mypy required
        self.assertEqual(tuple(), res.messages())

    def test_possible_error_0_2(self) -> None:
        res = error.possible_error(
            messages=[], errors=[
                error.SimplePetroniaReturnError(),
                error.SimplePetroniaReturnError(_m('1')),
            ],
        )
        self.assertIsNotNone(res)
        assert res is not None  # mypy required
        self.assertEqual((_m('1'),), res.messages())

    def test_possible_error_1_0(self) -> None:
        res = error.possible_error(
            messages=[_m('x')], errors=[],
        )
        self.assertIsNotNone(res)
        assert res is not None  # mypy required
        self.assertEqual((_m('x'),), res.messages())

    def test_possible_error_2_0(self) -> None:
        res = error.possible_error(
            messages=[_m('x'), _m('y')], errors=[],
        )
        self.assertIsNotNone(res)
        assert res is not None  # mypy required
        self.assertEqual((_m('x'), _m('y')), res.messages())

    def test_possible_error_2_3(self) -> None:
        res = error.possible_error(
            messages=[_m('x'), _m('y')], errors=[
                error.SimplePetroniaReturnError(),
                error.SimplePetroniaReturnError(_m('1')),
                error.SimplePetroniaReturnError(_m('2')),
            ],
        )
        self.assertIsNotNone(res)
        assert res is not None  # mypy required
        self.assertEqual((_m('x'), _m('y'), _m('1'), _m('2'),), res.messages())


def _m(message: str, **args: UserMessageData) -> UserMessage:
    return UserMessage(i18n(message), **args)
