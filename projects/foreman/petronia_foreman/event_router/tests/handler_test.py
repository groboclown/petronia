"""Test the module."""

import unittest
from .. import handler


class EventHandlerSetTest(unittest.TestCase):
    """Test the EventHandlerSet class."""

    def test_can_produce(self) -> None:
        """Test can_produce in its variations."""
        ehs = handler.EventHandlerSet()
        self.assertFalse(ehs.can_produce('e'))
        res = ehs.add_handler('h1', ['e'], [])
        self.assertIsNone(res.error)
        self.assertTrue(ehs.can_produce('e'))
        res = ehs.remove_handler('h1')
        self.assertIsNone(res.error)
        self.assertFalse(ehs.can_produce('e'))

    def test_can_consume(self) -> None:
        """Test can_consume in its variations."""
        ehs = handler.EventHandlerSet()
        self.assertFalse(ehs.can_consume('e', 't'))

        # None-None handler (catch-all)
        res = ehs.add_handler('h1', [], [(None, None)])
        self.assertIsNone(res.error)
        self.assertTrue(ehs.can_consume('e', 't'))
        res = ehs.remove_handler('h1')
        self.assertIsNone(res.error)
        self.assertFalse(ehs.can_consume('e', 't'))

        # e-None handler (catch-all for target)
        res = ehs.add_handler('h1', [], [('e', None)])
        self.assertIsNone(res.error)
        self.assertTrue(ehs.can_consume('e', 't'))
        self.assertTrue(ehs.can_consume('e', 't1'))
        self.assertFalse(ehs.can_consume('e1', 't'))
        res = ehs.remove_handler('h1')
        self.assertIsNone(res.error)
        self.assertFalse(ehs.can_consume('e', 't'))

        # None-t handler (catch-all for event)
        res = ehs.add_handler('h1', [], [(None, 't')])
        self.assertIsNone(res.error)
        self.assertTrue(ehs.can_consume('e', 't'))
        self.assertTrue(ehs.can_consume('e1', 't'))
        self.assertFalse(ehs.can_consume('e', 't1'))
        res = ehs.remove_handler('h1')
        self.assertIsNone(res.error)
        self.assertFalse(ehs.can_consume('e', 't'))

        # e-t handler
        res = ehs.add_handler('h1', [], [('e', 't')])
        self.assertIsNone(res.error)
        self.assertTrue(ehs.can_consume('e', 't'))
        self.assertFalse(ehs.can_consume('e1', 't'))
        self.assertFalse(ehs.can_consume('e', 't1'))
        res = ehs.remove_handler('h1')
        self.assertIsNone(res.error)
        self.assertFalse(ehs.can_consume('e', 't'))

    def test_contains_handler(self) -> None:
        """Test the contains_handler method."""
        ehs = handler.EventHandlerSet()
        self.assertFalse(ehs.contains_handler_id('h2'))
        res = ehs.add_handler('h2', [], [])
        self.assertIsNone(res.error)
        self.assertTrue(ehs.contains_handler_id('h2'))
        res = ehs.remove_handler('h2')
        self.assertIsNone(res.error)
        self.assertFalse(ehs.contains_handler_id('h2'))

    def test_add_handler__duplicate(self) -> None:
        """Test add_handler with a duplicate ID."""
        ehs = handler.EventHandlerSet()
        res = ehs.add_handler('hd', [], [])
        self.assertIsNone(res.error)
        res = ehs.add_handler('hd', ['e'], [])
        self.assertIsNotNone(res.error)

    def test_remove_handler__not_registered(self) -> None:
        """Test add_handler with a duplicate ID."""
        ehs = handler.EventHandlerSet()
        res = ehs.remove_handler('h2')
        self.assertIsNotNone(res.error)

    def test_add_listener__no_handler(self) -> None:
        """Test add_listener with no such handler."""
        ehs = handler.EventHandlerSet()
        res = ehs.add_listener('h1', None, None)
        self.assertIsNotNone(res.error)

    def test_remove_listener__no_handler(self) -> None:
        """Test remove_listener with no such handler registered."""
        ehs = handler.EventHandlerSet()
        res = ehs.remove_listener('h1', None, None)
        self.assertIsNotNone(res.error)

    def test_remove_listener__no_listener(self) -> None:
        """Test remove_listener with no such listener on the handler."""
        ehs = handler.EventHandlerSet()
        res = ehs.add_handler('h1', ['e1'], [])
        self.assertIsNone(res.error)
        res = ehs.add_handler('h2', ['e2'], [])
        self.assertIsNone(res.error)
        res = ehs.add_listener('h1', 'e2', 't2')
        self.assertIsNone(res.error)
        res = ehs.remove_listener('h2', 'e1', None)
        self.assertIsNotNone(res.error)
