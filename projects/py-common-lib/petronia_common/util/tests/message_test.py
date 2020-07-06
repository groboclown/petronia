
"""Test the message module."""

import unittest
from .. import message


class MessageTest(unittest.TestCase):
    """Runs tests on the message class."""
    def test_message(self) -> None:
        """Simple constructor / accessor."""
        str1 = message.i18n('m1')
        msg = message.UserMessage(str1)
        self.assertIs(str1, msg.message)

    def test_arguments_empty(self) -> None:
        """No-argument value."""
        msg = message.UserMessage(message.i18n('m2m'))
        self.assertEqual({}, msg.arguments)

    def test_arguments_several(self) -> None:
        """Different typed arguments."""
        msg = message.UserMessage(message.i18n('m3x'), a="1", b=["x"], c=True)
        self.assertEqual({"a": "1", "b": ["x"], "c": True}, msg.arguments)

    def test_debug(self) -> None:
        """Debug output generation."""
        msg = message.UserMessage(message.i18n('4: {a} {b} {c}'), a="1", b=["x"], c=True)
        self.assertEqual("4: 1 ['x'] True", msg.debug())

    def test_equal(self) -> None:
        """Equality check."""
        msg1 = message.UserMessage(message.i18n('5: {a} {b} {c}'), a="1", b=["x"], c=True)
        msg2 = message.UserMessage(message.i18n('5: {a} {b} {c}'), b=["x"], c=True, a="1")
        self.assertTrue(msg1 == msg2)
        self.assertTrue(msg2 == msg1)

    def test_not_equal(self) -> None:
        """Not equal check."""
        msg1 = message.UserMessage(message.i18n('6: {a} {b} {c}'), a="1", b=["x"], c=True)
        msg2 = message.UserMessage(message.i18n('6: {a} {b} {c}'), b=["x"], c=False, a="1")
        msg3 = message.UserMessage(message.i18n('6: {a} {b} {c}'), b=["y"], c=True, a="1")
        msg4 = message.UserMessage(message.i18n('6: {a} {b} {c}'), a="1")
        msg5 = message.UserMessage(message.i18n('6: oh yeah'))
        msg1_b = message.UserMessage(message.i18n('6: {a} {b} {c}'), a="1", b=["x"], c=True)

        self.assertTrue(msg1 != msg2)

        # This is explicit != to ensure type on the function invocation.
        # noinspection PyComparisonWithNone
        self.assertTrue(msg1 != None)  # pylint: disable=C0121

        self.assertTrue(msg1 != 16)
        self.assertFalse(msg1 != msg1_b)
        self.assertTrue(msg1 != msg3)
        self.assertTrue(msg1 != msg4)
        self.assertTrue(msg1 != msg5)

    def test_hash(self) -> None:
        """hash check"""
        msg1 = message.UserMessage(message.i18n('5: {a} {b} {c}'), a="1", b=["x"], c=True)
        msg2 = message.UserMessage(message.i18n('5: {a} {b} {c}'), b=["x"], c=True, a="1")
        msg3 = message.UserMessage(message.i18n('6: {a} {b} {c}'), b=["y"], c=True, a="1")

        self.assertEqual(hash(msg1), hash(msg2))
        self.assertEqual(hash(msg1), hash(msg1))
        self.assertNotEqual(hash(msg1), hash(msg3))
