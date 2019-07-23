
"""
Unit tests for event.py
"""

import unittest
from petronia3.system.bus import EventBus, TARGET_WILDCARD, QUEUE_EVENT_NORMAL
from petronia3.util.tests.test_helper import BasicListener, BasicQueuer
from petronia3.errors import PetroniaInvalidState
from ..event_registry import EventRegistry
from ..typesafe import TypeSafeEventBus
from ..bootstrap import register_event_registry_events


class TypeSafeEventBusTest(unittest.TestCase):
    """Tests for the TypeSafeEventBus"""
    def test_simple(self):
        """Simple use case."""
        evtr = EventRegistry()
        register_event_registry_events(evtr)
        evtr.register('simple', QUEUE_EVENT_NORMAL, EventSimple, EventSimple())
        queue = BasicQueuer(self)
        bus = EventBus(queue.pure_queuer)
        typesafe = TypeSafeEventBus(bus, evtr)
        typesafe.add_listener(TARGET_WILDCARD, lambda x: ('simple', x,), BasicListener('1', queue))

    def test_listen_not_registered(self):
        """Attempt to add_listener() on not-registered event id"""
        evtr = EventRegistry()
        queue = BasicQueuer(self)
        bus = EventBus(queue.pure_queuer)
        typesafe = TypeSafeEventBus(bus, evtr)
        try:
            typesafe.add_listener(TARGET_WILDCARD, lambda x: ('not-registered', x,), BasicListener('1', queue))
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
        bus = EventBus(queue.pure_queuer)
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
