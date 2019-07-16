
"""Unit tests for event bus stuff"""

import unittest
from typing import Tuple, List, Optional, Sequence

from ..bus import (
    EventBus,
    EventId,
    QueuePriority,

    EVENT_WILDCARD, TARGET_WILDCARD,
    QUEUE_EVENT_NOW, QUEUE_EVENT_NORMAL, QUEUE_EVENT_IO,
)
from ...participant import (
    create_singleton_identity,
    ParticipantId,
    NOT_PARTICIPANT,
)


class _BaseBasicQueuer:
    def listener_call_in(self, name: str, event_id: EventId, target_id: ParticipantId, event_obj: object) -> None:
        raise NotImplementedError()


class BasicListener:
    """Listener that integrates with the BasicQueuer"""
    def __init__(self, name: str, queuer: _BaseBasicQueuer) -> None:
        self.name = name
        self.queuer = queuer

    def __call__(self, event_id: EventId, target_id: ParticipantId, event_obj: object) -> None:
        self.queuer.listener_call_in(self.name, event_id, target_id, event_obj)


class BasicQueuer(_BaseBasicQueuer):
    """Basic testable queuer"""

    call_order: List[Tuple[QueuePriority, str, EventId, ParticipantId, object]]
    __call_in: Optional[Tuple[QueuePriority, str, EventId, ParticipantId, object]]

    def __init__(self, utc: unittest.TestCase) -> None:
        self.utc = utc
        self.call_order = []
        self.__call_in = None

    def __call__(
            self,
            when: QueuePriority,
            listeners: Sequence[BasicListener],
            args: Tuple[EventId, ParticipantId, object]
    ) -> None:
        for listener in listeners:
            self.__call_in = (when, '', EventId(''), NOT_PARTICIPANT, object())
            listener(args[0], args[1], args[2])
            assert len(self.__call_in) == 5
            self.call_order.append(self.__call_in)
            self.__call_in = None

    def listener_call_in(self, name: str, event_id: EventId, target_id: ParticipantId, event_obj: object) -> None:
        """
        Called by the BasicListener.
        """
        assert self.__call_in
        self.__call_in = (self.__call_in[0], name, event_id, target_id, event_obj)

    def assert_length(self, length: int) -> None:
        """Assertion number of calls"""
        self.utc.assertEqual(
            len(self.call_order),
            length,
            'call state: {0}'.format(repr(self.call_order))
        )

    def assert_called_only(
            self,
            when: str,
            listener_id_list: List[str],
            event_id: str, target_id: str, event_obj: object
    ) -> None:
        """Check that only the given event on the given listeners is called."""
        self.assert_length(len(listener_id_list))
        for cod in self.call_order:
            self.utc.assertEqual(len(cod), 5, 'call state: {0}'.format(repr(self.call_order)))
            self.utc.assertEqual(cod[0], when, 'call state: {0}'.format(repr(self.call_order)))
            self.utc.assertIn(
                cod[1],
                listener_id_list, 'call state: {0}'.format(repr(self.call_order))
            )
            self.utc.assertEqual(cod[2], event_id, 'call state: {0}'.format(repr(self.call_order)))
            self.utc.assertEqual(cod[3], target_id, 'call state: {0}'.format(repr(self.call_order)))
            self.utc.assertEqual(cod[4], event_obj, 'call state: {0}'.format(repr(self.call_order)))
        self.clear()

    def clear(self) -> None:
        """Reset the call order list"""
        self.call_order = []


class EventBusTest(unittest.TestCase):
    """Unit tests for the EventBus"""

    def test_event_trigger_listeners(self) -> None:
        """
        Test that, for different event and target ID registration, the
        trigger calls only the required listeners the exact number of
        required times.
        """
        queue = BasicQueuer(self)
        bus = EventBus(queue) # type: ignore

        bus.add_listener(EventId('e1'), create_singleton_identity('1'), BasicListener('1', queue))
        bus.add_listener(EventId('e1'), create_singleton_identity('2'), BasicListener('2', queue))
        bus.add_listener(EventId('e2'), create_singleton_identity('1'), BasicListener('3', queue))
        bus.add_listener(EventId('e1'), TARGET_WILDCARD, BasicListener('4', queue))
        bus.add_listener(EVENT_WILDCARD, create_singleton_identity('1'), BasicListener('5', queue))
        bus.add_listener(EVENT_WILDCARD, TARGET_WILDCARD, BasicListener('6', queue))

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
        bus = EventBus(queue) # type: ignore
        bus.trigger(QUEUE_EVENT_NORMAL, EventId('e1'), create_singleton_identity('1'), object())
        queue.assert_length(0)
