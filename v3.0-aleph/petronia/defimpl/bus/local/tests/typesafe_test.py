
"""
Unit tests for event.py
"""

import unittest
from .....aid.test_helper import BasicListener, BasicQueuer
from .....aid.std import (
    PetroniaInvalidState,
    EventId,
    SingletonId,
)
from .....aid.bootstrap import (
    TARGET_WILDCARD, QUEUE_EVENT_NORMAL, GLOBAL_EVENT_PROTECTION,
)
from ..event_registry import EventRegistry
from ..basic_event_bus import BasicEventBus
from ..typesafe import TypeSafeEventBus
from ..bootstrap import register_core_events


class TypeSafeEventBusTest(unittest.TestCase):
    """Tests for the TypeSafeEventBus"""
    def test_simple(self):
        """Simple use case."""
        evtr = EventRegistry()
        register_core_events(evtr)
        evtr.register(EventId('simple'), QUEUE_EVENT_NORMAL, GLOBAL_EVENT_PROTECTION, EventSimple, EventSimple())
        queue = BasicQueuer(self)
        bus = BasicEventBus(queue.pure_queuer)
        typesafe = TypeSafeEventBus(bus, evtr)
        typesafe.add_listener(TARGET_WILDCARD, lambda x: ('simple', x,), BasicListener('1', queue))

    def test_listen_not_registered(self):
        """Attempt to add_listener() on not-registered event id"""
        evtr = EventRegistry()
        register_core_events(evtr)
        queue = BasicQueuer(self)
        bus = BasicEventBus(queue.pure_queuer)
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
        register_core_events(evtr)
        queue = BasicQueuer(self)
        bus = BasicEventBus(queue.pure_queuer)
        typesafe = TypeSafeEventBus(bus, evtr)
        try:
            typesafe.trigger(EventId('not-registered'), SingletonId('tgt'), EventSimple())
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
