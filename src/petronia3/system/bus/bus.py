
"""
The Event Bus implementation.
"""

from ...errors import assert_get, assert_contains
from ...util.rwlock import RWLock


EVENT_WILDCARD = '*'
TARGET_WILDCARD = '*'

QUEUE_EVENT_NOW = 'now'
QUEUE_EVENT_NORMAL = 'normal'
QUEUE_EVENT_IO = 'io'

QUEUE_EVENT_TYPES = (
    QUEUE_EVENT_NOW,
    QUEUE_EVENT_NORMAL,
    QUEUE_EVENT_IO,
)

class EventBus:
    """
    Simple event bus implementation, with support for wildcard listeners.

    Interaction to this bus should be done indirectly through function handlers
    to aid in the proper type checking.

    Event IDs are allowed to be any string without the '>' character.
    """

    def __init__(self, queue):
        """

        :param queue callable: a function that accepts the parameters (QUEUE_EVENT_TYPE, function, vargs, kargs)
            and invokes said function at a near-future time.  The QUEUE_EVENT_TYPE indicates the expected behavior
            of the queueing process.  Note that only QUEUE_EVENT_NOW has behavior that must be followed.
        """
        assert callable(queue)
        self.__queue = queue
        self.__listener_reg = {}
        self.__listener_ids = {}
        self.__next_id = 0
        self.__lock = RWLock()

    def add_listener(self, event_id: str, target_id: str, callback: callable):
        """
        Registers an event listener.  If the event or target is a wildcard, then the listener will
        be invoked for any event or target.

        This returns the function that will de-register the listener.  This allows for the same listener
        function to be registered on multiple events, each with its own lifecycle.

        :param event_id str: event to listen to.
        :param target_id str: target of the event to listen to.
        :param callback callable: a function that takes as arguments (event_id, target_id, event_object)
            and is called when a matching event is triggered.  If the listener is registered to a wildcard,
            the real event or target ID is passed as argument.
        :return callable: a simple function that, when called, will de-register the listener
            for the event / target.
        """
        EventBus.validate_event_id(event_id)
        EventBus.validate_target_id(target_id)
        register_id = EventBus._join_ids(event_id, target_id)
        listener = EventListener(callback)

        self.__lock.acquire_write()
        try:
            listener_id = self.__next_id
            self.__next_id += 1
            if register_id not in self.__listener_reg:
                self.__listener_reg[register_id] = []
            self.__listener_reg[register_id].append(listener_id)
            self.__listener_ids[listener_id] = listener
        finally:
            self.__lock.release()

        return lambda: self._deregister(listener_id, register_id)

    def trigger(self, event_id: str, target_id: str, event_obj):
        """
        The bus will send the event to the listeners at an appropriate time.

        :param event_id str: event ID to trigger.
        """
        self.__fire_event(QUEUE_EVENT_NORMAL, event_id, target_id, event_obj)

    def trigger_io(self, event_id: str, target_id: str, event_obj):
        """
        The bus will send the event to the listeners at an appropriate time.

        :param event_id str: event ID to trigger.
        """
        self.__fire_event(QUEUE_EVENT_IO, event_id, target_id, event_obj)

    def trigger_now(self, event_id, target_id, event_obj):
        """
        The bus will execute all event listeners at the time of execution.
        The current thread will wait until all listeners complete execution.
        """
        self.__fire_event(QUEUE_EVENT_NOW, event_id, target_id, event_obj)

    def __fire_event(self, when: str, event_id, target_id, event_obj):
        assert when in QUEUE_EVENT_TYPES
        EventBus.validate_event_id(event_id)
        EventBus.validate_target_id(target_id)
        # Use a set of event names, in case the event_id or target_id are themselves wildcards.
        events = set([
            EventBus._join_ids(event_id, target_id),
            EventBus._join_ids(EVENT_WILDCARD, target_id),
            EventBus._join_ids(event_id, TARGET_WILDCARD),
            EventBus._join_ids(EVENT_WILDCARD, TARGET_WILDCARD),
        ])
        listeners = []
        self.__lock.acquire_read()
        try:
            for evt in events:
                if evt in self.__listener_reg:
                    for lid in self.__listener_reg[evt]:
                        listener = assert_get(
                            self.__listener_ids, lid,
                            'EventBus',
                            'Registered event {0} referenced ID {1} must be in the listener ID list'.format(lid, evt)
                        )
                        assert isinstance(listener, EventListener)
                        listeners.append(listener)
        finally:
            self.__lock.release()
        for listener in listeners:
            # listener is of type EventListener, which is callable.
            self.__queue(
                when,
                listener,
                [event_id, target_id, event_obj]
            )

    def _deregister(self, listener_id, register_id):
        self.__lock.acquire_write()
        try:
            listener = assert_get(
                self.__listener_ids, listener_id,
                'EventBus',
                'deregistration of listener {0} must be called at most once'
            )
            listener.disable()
            del self.__listener_ids[listener_id]

            reg_list = assert_get(
                self.__listener_reg, register_id,
                'EventBus',
                'deregistration setup expects {0} to exist in the event registration dictionary'
            )
            assert_contains(
                reg_list, listener_id,
                'EventBus',
                'deregistration setup expects {0} to exist in the registration list'
            )
            reg_list.remove(listener_id)
            # Because target_id can have a short lifespan, we clean up
            # the list to prevent the dictionary from getting huge over a long
            # period of time.
            if not self.__listener_reg[register_id]:
                del self.__listener_reg[register_id]
        finally:
            self.__lock.release()

    @staticmethod
    def validate_event_id(event_id):
        """Validate the event id correctness."""
        assert isinstance(event_id, str)
        assert event_id # includes checking for length > 0
        assert event_id.find('>') < 0

    @staticmethod
    def validate_target_id(target_id):
        """Validate the target id correctness."""
        assert isinstance(target_id, str)
        assert target_id # includes checking for length > 0

    @staticmethod
    def _join_ids(event_id, target_id):
        return event_id + '>' + target_id


class EventListener:
    """
    Internal class that handles invoking an event listener, and includes special
    management for deregistering protection.
    """
    def __init__(self, callback: callable):
        self.__callback = callback
        self.__enabled = True

    def disable(self):
        """Disables the event listener"""
        self.__enabled = False

    def __call__(self, *vargs, **kvargs):
        if self.__enabled:
            self.__callback(*vargs, **kvargs)
