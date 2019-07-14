
"""
Unit tests for event.py
"""

import unittest
from ..event import (
    EventRegistry
)
from ..typesafe import TypeSafeEventBus, register_events
from ..bus import EventBus, TARGET_WILDCARD, QUEUE_EVENT_NORMAL
from .bus_test import BasicQueuer, BasicListener
from ....errors import PetroniaInvalidState


class TypeSafeEventBusTest(unittest.TestCase):
    """Tests for the TypeSafeEventBus"""
    def test_simple(self):
        """Simple use case."""
        evtr = EventRegistry()
        register_events(evtr)
        evtr.register('simple', QUEUE_EVENT_NORMAL, EventSimple, EventSimple())
        queue = BasicQueuer(self)
        bus = EventBus(queue)
        typesafe = TypeSafeEventBus(bus, evtr)
        typesafe.add_listener('simple', TARGET_WILDCARD, BasicListener('1', queue))

    def test_listen_not_registered(self):
        """Attempt to add_listener() on not-registered event id"""
        evtr = EventRegistry()
        queue = BasicQueuer(self)
        bus = EventBus(queue)
        typesafe = TypeSafeEventBus(bus, evtr)
        try:
            typesafe.add_listener('not-registered', TARGET_WILDCARD, BasicListener('1', queue))
            self.fail('Did not raise error')
        except PetroniaInvalidState as err:
            self.assertEqual(
                str(err),
                'EventRegistry: event validation: event ID not-registered must be registered as a valid event'
            )

    def test_trigger_not_registered(self):
        """Trigger an event that isn't registered."""
        evtr = EventRegistry()
        queue = BasicQueuer(self)
        bus = EventBus(queue)
        typesafe = TypeSafeEventBus(bus, evtr)
        try:
            typesafe.trigger('not-registered', 'tgt', EventSimple())
            self.fail('Did not raise error')
        except PetroniaInvalidState as err:
            self.assertEqual(
                str(err),
                'EventRegistry: event ID invalid: event ID not-registered must be registered as a valid event'
            )


class EventSimple:
    """No additional stuff in event."""

    # Even with no members, it must define the __slots__ value.
    __slots__ = ('x',)
