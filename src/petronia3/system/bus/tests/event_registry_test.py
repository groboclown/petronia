
"""
Unit tests for event.py
"""

import unittest
from ..event_registry import (
    EventRegistry
)
from ..event_bus import QUEUE_EVENT_NORMAL
from ....errors import PetroniaInvalidState


class EventRegistryTest(unittest.TestCase):
    """
    Tests for the EventRegistry.
    """
    def test_register_normal(self):
        """register() with correct event type.  Also checks has_event_id and event_ids, a bit."""
        evtr = EventRegistry()
        evtr.register('simple', QUEUE_EVENT_NORMAL, EventSimple, EventSimple())
        self.assertTrue(
            evtr.has_event_id('simple')
        )
        self.assertEqual(
            list(evtr.event_ids),
            ['simple']
        )
        evtr.validate_event('simple', 'tgt', EventSimple())
        evtr.validate_has('simple')

    def test_register_no_slots(self):
        """register() an object with no defiend slots"""
        evtr = EventRegistry()
        try:
            evtr.register('no_slots', QUEUE_EVENT_NORMAL, EventNoSlot, EventNoSlot())
            self.fail('Did not raise error')
        except PetroniaInvalidState as err:
            self.assertEqual(
                str(err),
                'EventRegistry: event object must be valid: event classes must provide the __slots__ member for itself and all parent classes'
            )
        try:
            evtr.validate_has('no_slots')
            self.fail('Did not raise error')
        except PetroniaInvalidState as err2:
            self.assertEqual(
                str(err2),
                'EventRegistry: event validation: event ID no_slots must be registered as a valid event'
            )

    def test_register_not_inherit(self):
        """register() an object which is a dictionary."""
        evtr = EventRegistry()
        try:
            evtr.register('no_event', QUEUE_EVENT_NORMAL, dict, {})
            self.fail('Did not raise error')
        except PetroniaInvalidState as err:
            self.assertEqual(
                str(err),
                'EventRegistry: event object must be valid: event must be an object'
            )

    def test_nothing_registered(self):
        """has_event_id and event_ids with an empty registry."""
        evtr = EventRegistry()
        self.assertFalse(evtr.has_event_id('e'))
        self.assertFalse(evtr.event_ids)
        self.assertIsNotNone(evtr.event_ids)


class EventSimple:
    """No additional stuff in event."""

    # Even with no members, it must define the __slots__ value.
    __slots__ = ('x',)

class EventNoSlot:
    """No __slots__ capability."""
    def __init__(self):
        self.xyz = 1
