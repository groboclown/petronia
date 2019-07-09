
import unittest

from .bus import (
    EventBus,

    EVENT_WILDCARD, TARGET_WILDCARD,
    QUEUE_EVENT_NOW, QUEUE_EVENT_NORMAL, QUEUE_EVENT_IO,
)

class EventBusTest(unittest.TestCase):
    """Unit tests for the EventBus"""

    def test_event_trigger_listeners(self):
        """
        Test that, for different event and target ID registration, the
        trigger calls only the required listeners the exact number of
        required times.
        """
        queue = BasicQueuer(self)
        bus = EventBus(queue)

        bus.add_listener('e1', 't1', BasicListener('1', queue))
        bus.add_listener('e1', 't2', BasicListener('2', queue))
        bus.add_listener('e2', 't1', BasicListener('3', queue))
        bus.add_listener('e1', TARGET_WILDCARD, BasicListener('4', queue))
        bus.add_listener(EVENT_WILDCARD, 't1', BasicListener('5', queue))
        bus.add_listener(EVENT_WILDCARD, TARGET_WILDCARD, BasicListener('6', queue))

        evt = {}
        bus.trigger('e1', 't1', evt)
        queue.assert_called_only(
            QUEUE_EVENT_NORMAL,
            ['1', '4', '5', '6'],
            'e1', 't1', evt
        )

        bus.trigger('e1', 't2', evt)
        queue.assert_called_only(
            QUEUE_EVENT_NORMAL,
            ['2', '4' ,'6'],
            'e1', 't2', evt
        )

        bus.trigger('e2', 't1', evt)
        queue.assert_called_only(
            QUEUE_EVENT_NORMAL,
            ['3', '5', '6'],
            'e2', 't1', evt
        )
        bus.trigger('e2', 't2', evt)
        queue.assert_called_only(
            QUEUE_EVENT_NORMAL,
            ['6'],
            'e2', 't2', evt
        )

    def test_no_listeners(self):
        """Test correct behavior when no listeners are registered on the bus."""
        queue = BasicQueuer(self)
        bus = EventBus(queue)
        bus.trigger('e1', 't1', {})
        queue.assert_length(0)

    def test_now(self):
        """Test that, when trigger_now called, the queuer gets the right thread category."""
        queue = BasicQueuer(self)
        bus = EventBus(queue)
        evt = {}
        bus.add_listener('e1', 't1', BasicListener('1', queue))
        bus.trigger_now('e1', 't1', evt)
        queue.assert_called_only(
            QUEUE_EVENT_NOW,
            ['1'],
            'e1', 't1', evt
        )

    def test_io(self):
        """Test that, when trigger_now called, the queuer gets the right thread category."""
        queue = BasicQueuer(self)
        bus = EventBus(queue)
        evt = {}
        bus.add_listener('e1', 't1', BasicListener('1', queue))
        bus.trigger_io('e1', 't1', evt)
        queue.assert_called_only(
            QUEUE_EVENT_IO,
            ['1'],
            'e1', 't1', evt
        )



class BasicQueuer:
    """blah"""
    def __init__(self, utc: unittest.TestCase):
        self.utc = utc
        self.call_order = []
        self.__call_in = None

    def __call__(self, when, listener, args):
        self.__call_in = [when]
        listener(args[0], args[1], args[2])
        assert len(self.__call_in) == 5
        self.call_order.append(self.__call_in)
        self.__call_in = None

    def listener_call_in(self, name, eid, tid, eobj):
        self.__call_in.extend([name, eid, tid, eobj])

    def assert_length(self, length: int):
        """blah"""
        self.utc.assertEquals(len(self.call_order), length, 'call state: {0}'.format(repr(self.call_order)))

    def assert_called_only(
            self,
            when, listener_id_list, event_id, target_id, event_obj
    ):
        """blah"""
        self.assert_length(len(listener_id_list))
        for cod in self.call_order:
            self.utc.assertEquals(len(cod), 5, 'call state: {0}'.format(repr(self.call_order)))
            self.utc.assertEquals(cod[0], when, 'call state: {0}'.format(repr(self.call_order)))
            self.utc.assertIn(cod[1], listener_id_list, 'call state: {0}'.format(repr(self.call_order)))
            self.utc.assertEquals(cod[2], event_id, 'call state: {0}'.format(repr(self.call_order)))
            self.utc.assertEquals(cod[3], target_id, 'call state: {0}'.format(repr(self.call_order)))
            self.utc.assertEquals(cod[4], event_obj, 'call state: {0}'.format(repr(self.call_order)))
        self.clear()

    def clear(self):
        """blah"""
        self.call_order = []


class BasicListener:
    """blah"""
    def __init__(self, name, queuer: BasicQueuer):
        self.name = name
        self.queuer = queuer

    def __call__(self, *vargs, **kvargs):
        assert not kvargs
        assert len(vargs) == 3
        self.queuer.listener_call_in(self.name, vargs[0], vargs[1], vargs[2])