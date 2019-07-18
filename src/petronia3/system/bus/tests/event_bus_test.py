
"""Unit tests for event bus stuff"""

import unittest

from ....util.tests.test_helper import BasicListener, BasicQueuer
from ..event_bus import (
    EventBus,
    EventId,

    EVENT_WILDCARD, TARGET_WILDCARD,
    QUEUE_EVENT_NOW, QUEUE_EVENT_NORMAL, QUEUE_EVENT_IO,
)
from ...participant import (
    create_singleton_identity,
)


class EventBusTest(unittest.TestCase):
    """Unit tests for the EventBus"""

    def test_event_trigger_listeners(self) -> None:
        """
        Test that, for different event and target ID registration, the
        trigger calls only the required listeners the exact number of
        required times.
        """
        queue = BasicQueuer(self)
        bus = EventBus(queue.pure_queuer)

        bus.add_listener(
            EventId('e1'), create_singleton_identity('1'), BasicListener('1', queue)
        )
        bus.add_listener(
            EventId('e1'), create_singleton_identity('2'), BasicListener('2', queue)
        )
        bus.add_listener(
            EventId('e2'), create_singleton_identity('1'), BasicListener('3', queue)
        )
        bus.add_listener(
            EventId('e1'), TARGET_WILDCARD, BasicListener('4', queue)
        )
        bus.add_listener(
            EVENT_WILDCARD, create_singleton_identity('1'), BasicListener('5', queue)
        )
        bus.add_listener(
            EVENT_WILDCARD, TARGET_WILDCARD, BasicListener('6', queue)
        )

        evt = object()
        bus.trigger(QUEUE_EVENT_NORMAL, EventId('e1'), create_singleton_identity('1'), evt)
        queue.assert_called_only(
            QUEUE_EVENT_NORMAL,
            ['1', '4', '5', '6'],
            'e1', '1', evt
        )

        bus.trigger(QUEUE_EVENT_IO, EventId('e1'), create_singleton_identity('2'), evt)
        queue.assert_called_only(
            QUEUE_EVENT_IO,
            ['2', '4' ,'6'],
            'e1', '2', evt
        )

        bus.trigger(QUEUE_EVENT_NOW, EventId('e2'), create_singleton_identity('1'), evt)
        queue.assert_called_only(
            QUEUE_EVENT_NOW,
            ['3', '5', '6'],
            'e2', '1', evt
        )

        bus.trigger(QUEUE_EVENT_NORMAL, EventId('e2'), create_singleton_identity('2'), evt)
        queue.assert_called_only(
            QUEUE_EVENT_NORMAL,
            ['6'],
            'e2', '2', evt
        )

        bus.trigger(QUEUE_EVENT_NORMAL, EventId('e1'), TARGET_WILDCARD, evt)
        queue.assert_called_only(
            QUEUE_EVENT_NORMAL,
            ['4', '6'],
            'e1', TARGET_WILDCARD, evt
        )

        bus.trigger(QUEUE_EVENT_NORMAL, EVENT_WILDCARD, create_singleton_identity('1'), evt)
        queue.assert_called_only(
            QUEUE_EVENT_NORMAL,
            ['5', '6'],
            EVENT_WILDCARD, '1', evt
        )
        bus.trigger(QUEUE_EVENT_NORMAL, EVENT_WILDCARD, TARGET_WILDCARD, evt)
        queue.assert_called_only(
            QUEUE_EVENT_NORMAL,
            ['6'],
            EVENT_WILDCARD, TARGET_WILDCARD, evt
        )

    def test_no_listeners(self) -> None:
        """Test correct behavior when no listeners are registered on the bus."""
        queue = BasicQueuer(self)
        bus = EventBus(queue.pure_queuer)
        bus.trigger(QUEUE_EVENT_NORMAL, EventId('e1'), create_singleton_identity('1'), object())
        queue.assert_length(0)
