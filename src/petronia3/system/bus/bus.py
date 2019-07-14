
"""
The Event Bus implementation.
"""
from typing import Callable, List, Dict, Tuple, Sequence, NewType
from ..participant import ParticipantId, is_valid_participant_identity
from ...validation import assert_format, assert_all, assert_has_signature
from ...util.rwlock import RWLock


EventId = NewType('EventId', str)
QueuePriority = NewType('QueuePriority', str)
EventCallback = Callable[[EventId, ParticipantId, object], None]
QueueFunction = Callable[
    [QueuePriority, Sequence[EventCallback], Tuple[EventId, ParticipantId, object]],
    None
]
ListenerId = NewType('ListenerId', int)

EVENT_WILDCARD = EventId('*')
TARGET_WILDCARD = ParticipantId(-1)

NOT_LISTENER = ListenerId(0)

QUEUE_EVENT_NOW = QueuePriority('now')
QUEUE_EVENT_NORMAL = QueuePriority('normal')
QUEUE_EVENT_IO = QueuePriority('io')

QUEUE_EVENT_TYPES = (
    QUEUE_EVENT_NOW,
    QUEUE_EVENT_NORMAL,
    QUEUE_EVENT_IO,
)

class EventBus:
    """
    Simple event bus implementation, with support for wildcard listeners.

    The bus does not use weak references for the attached listeners.  It is up
    to the owner to correctly deregister listeners.

    Interaction to this bus should be done indirectly through function handlers
    to aid in the proper type checking.

    Event IDs are allowed to be any string without the '>' character.

    The event bus is the most critical component of the system.  Special effort
    must be made to ensure it has well defined usage.

    Care must be taken on writing event listeners to prevent leaking memory.

    All memory is expected to be global.
    """
    __slots__ = ('__queue', '__listener_reg', '__listener_ids', '__next_id', '__lock')

    # registration of listeners to the event id + the target id.
    __listener_reg: Dict[str, List[ListenerId]]

    # registration of the listener id to the callback.  This is a
    # double lookup, but puts the web of memory objects into one
    # simple structure.
    __listener_ids: Dict[ListenerId, EventCallback]

    def __init__(self, queue: QueueFunction) -> None:
        """

        :param queue callable: a function that accepts the parameters
            (QUEUE_EVENT_TYPE, function, vargs)
            and invokes said function at a near-future time.  The QUEUE_EVENT_TYPE
            indicates the expected behavior of the queueing process.  Note that
            only QUEUE_EVENT_NOW has behavior that must be followed.
        """
        assert callable(queue)
        self.__queue = queue
        self.__listener_reg = {}
        self.__listener_ids = {}
        self.__next_id = 1 # 0 is a "null" listener.
        self.__lock = RWLock()

    def add_listener(
            self,
            event_id: EventId, target_id: ParticipantId, callback: EventCallback
    ) -> ListenerId:
        """
        Registers an event listener.  If the event or target is a wildcard,
        then the listener will  be invoked for any event or target.

        This returns an identifier that is passed to the deregister function.
        This allows for minimal memory usage on the part of the bus, and puts
        the oneous for managing the deregistration on the listener caller.

        If an event is triggered with a wildcard event or target, then only
        listeners to the corresponding wildcard value will match.

        :param event_id str: event to listen to.
        :param target_id str: target of the event to listen to.
        :param callback callable: a function that takes as arguments (event_id, target_id, event_object)
            and is called when a matching event is triggered.  If the listener is registered to a wildcard,
            the real event or target ID is passed as argument.
        :return ListenerId: a unique identifier for the listener.
        """
        if event_id != EVENT_WILDCARD:
            EventBus.assert_event_id(event_id)
        if target_id != TARGET_WILDCARD:
            EventBus.assert_target_id(target_id)
        EventBus.assert_event_callback(callback)

        register_id = EventBus._join_ids(event_id, target_id)

        self.__lock.acquire_write()
        try:
            listener_id = ListenerId(self.__next_id)
            self.__next_id += 1
            if register_id not in self.__listener_reg:
                self.__listener_reg[register_id] = []
            self.__listener_reg[register_id].append(listener_id)
            self.__listener_ids[listener_id] = callback
        finally:
            self.__lock.release()

        return listener_id

    def trigger(self, when: QueuePriority, event_id: EventId, target_id: ParticipantId, event_obj: object) -> None:
        """
        Run each of the registered listeners for the event according to the priority of the
        `when` parameter.  The queue function will determine the actual time of the
        listener invocation.
        """
        assert when in QUEUE_EVENT_TYPES
        EventBus.assert_event_id(event_id)
        EventBus.assert_target_id(target_id)
        # Use a set of event names, in case the event_id or target_id are themselves wildcards.
        events = set([
            EventBus._join_ids(event_id, target_id),
            EventBus._join_ids(EVENT_WILDCARD, target_id),
            EventBus._join_ids(event_id, TARGET_WILDCARD),
            EventBus._join_ids(EVENT_WILDCARD, TARGET_WILDCARD),
        ])
        listeners: List[EventCallback] = []
        self.__lock.acquire_read()
        try:
            for evt in events:
                if evt in self.__listener_reg:
                    for lid in self.__listener_reg[evt]:
                        assert_format(
                            lid in self.__listener_ids,
                            'EventBus',
                            'Fire event found invalid internal state',
                            'Registered event {0} referenced ID {1} must be in the listener ID list',
                            lid, evt
                        )
                        listener = self.__listener_ids[lid]
                        listeners.append(listener)
        finally:
            self.__lock.release()
        self.__queue(
            when,
            listeners,
            (event_id, target_id, event_obj)
        )

    def deregister(self, listener_id: ListenerId) -> bool:
        """
        Remove the listener from receiving events, and remove references
        to the listener callback.

        :return bool: True if the listener was registered, False if not.
            If assertions are enabled, this will raise an error rather than
            return False.
        """
        # We'll be lazy with the lock, because de-register is a less frequent
        # operation.  We could perform a read lock, find all the places to
        # deregister the listener, then promote to a write lock and remove it.
        self.__lock.acquire_write()
        try:
            assert_format(
                listener_id in self.__listener_ids,
                'EventBus',
                'deregistration state issue',
                'deregistration of listener {0} must be called at most once',
                listener_id
            )
            if listener_id in self.__listener_ids:
                del self.__listener_ids[listener_id]
                # At most one registration item contains the listener reference.
                for register_id, reg_list in self.__listener_reg.items():
                    if listener_id in reg_list:
                        reg_list.remove(listener_id)
                    # Because target_id can have a short lifespan, we clean up
                    # the list to prevent the dictionary from getting huge over a long
                    # period of time.
                    if not reg_list:
                        del self.__listener_reg[register_id]
                    return True
            # If we reached this point, then there was a problem with our internal
            # state maintenance.
            assert_format(
                False,
                'EventBus',
                'deregistration state issue',
                'deregistration setup expects {0} to exist in the registration list',
                listener_id
            )
            return False
        finally:
            self.__lock.release()

    @staticmethod
    def assert_event_id(event_id: EventId) -> None:
        """Validate the event id correctness.  For debug-mode only."""
        assert_all(
            'EventBus',
            'Invalid event id ' + str(event_id),

            isinstance(event_id, str),
            len(event_id) > 0,
            event_id.find('>') < 0
        )

    @staticmethod
    def assert_target_id(target_id: ParticipantId) -> None:
        """Validate the target id correctness.  For debug-mode only."""
        assert_format(
            is_valid_participant_identity(target_id),

            'EventBus',
            'Invalid target ID',
            '{0}',
            target_id
        )

    @staticmethod
    def assert_event_callback(callback: EventCallback) -> None:
        """A somewhat expensive operation to ensure the callback conforms
        to the expected signature."""
        assert_has_signature(
            'EventBus',
            'event callback signature must be valid',
            callback,
            None,
            EventId,
            ParticipantId,
            object,
        )

    @staticmethod
    def _join_ids(event_id: EventId, target_id: ParticipantId) -> str:
        return str(event_id) + '>' + str(target_id)
