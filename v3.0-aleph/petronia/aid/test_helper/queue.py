
"""Unit tests for event bus stuff"""

import unittest
from typing import Tuple, List, Optional, Sequence
from ...base.bus import (
    EventId,
    QueuePriority,
    EventCallback,
)
from ...base import (
    ParticipantId,
    NOT_PARTICIPANT,
    INFO,
    log,
)
from ...base.util import T


class _BaseBasicQueuer:
    def listener_call_in(
            self, name: str, event_id: EventId, target_id: ParticipantId, event_obj: object
    ) -> None:
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

    def pure_queuer(
            self,
            when: QueuePriority,
            listeners: Sequence[EventCallback[T]],
            args: Tuple[EventId, ParticipantId, T]
    ) -> None:
        log(INFO, BasicQueuer, 'firing {0} listeners for {1}', len(listeners), args)
        for listener in listeners:
            if isinstance(listener, BasicListener):
                self.__call_in = (when, '', EventId(''), NOT_PARTICIPANT, object())
                log(INFO, BasicQueuer, 'firing test listener {0} for {1}', listener.name, args)
                listener(args[0], args[1], args[2])
                assert len(self.__call_in) == 5
                self.call_order.append(self.__call_in)
                self.__call_in = None
            else:
                log(INFO, BasicQueuer, 'firing internal event listener for {}', args)
                listener(args[0], args[1], args[2])
                self.call_order.append((when, str(listener), args[0], args[1], args[2]))

    def listener_call_in(
            self, name: str, event_id: EventId, target_id: ParticipantId, event_obj: object
    ) -> None:
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
