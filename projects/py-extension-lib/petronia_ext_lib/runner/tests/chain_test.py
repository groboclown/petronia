"""Test the module."""

from typing import List, Tuple
import unittest
from petronia_common.util import ValueHolder
from .. import chain


class DecisionHandlerProxyTest(unittest.TestCase):
    """Test the DecisionHandlerProxy class."""

    def test_on_event__active_false(self) -> None:
        """Test on_event when the active flag is True and the callback returns False."""
        trace: List[Tuple[str, str, object]] = []
        static_obj = object()
        active = ValueHolder(True)

        def callback(source: str, target: str, event: object) -> bool:
            trace.append((source, target, event))
            return False

        proxy = chain.DecisionHandlerProxy(callback, active)
        res = proxy.on_event('s-1', 't-1', static_obj)
        self.assertFalse(res)
        self.assertTrue(active.value)
        self.assertEqual(
            [('s-1', 't-1', static_obj)],
            trace,
        )

    def test_on_event__active_true(self) -> None:
        """Test on_event when the active flag is True and the callback returns True."""
        trace: List[Tuple[str, str, object]] = []
        static_obj = object()
        active = ValueHolder(True)

        def callback(source: str, target: str, event: object) -> bool:
            trace.append((source, target, event))
            return True

        proxy = chain.DecisionHandlerProxy(callback, active)
        res = proxy.on_event('s-1', 't-1', static_obj)
        self.assertTrue(res)
        self.assertFalse(active.value)
        self.assertEqual(
            [('s-1', 't-1', static_obj)],
            trace,
        )

    def test_on_event__inactive(self) -> None:
        """Test on_event when the active flag is True and the callback returns True."""
        active = ValueHolder(False)

        def callback(_source: str, _target: str, _event: object) -> bool:
            raise NotImplementedError  # pragma no cover

        proxy = chain.DecisionHandlerProxy(callback, active)
        res = proxy.on_event('s-1', 't-1', object())
        self.assertTrue(res)
        self.assertFalse(active.value)
