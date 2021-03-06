
"""
Type-safe event bus.

Includes firing events on event listener adding.
"""

from threading import Lock
from .basic_event_bus import (
    BasicEventBus,
)
from .event_registry import EventRegistry
from ....aid.std import (
    EventBus, EventCallback, EventId,
    ListenerId,
    ParticipantId,
    ComponentId,
    PetroniaLockTimeoutError,
    T,
    log, logerr,
    TRACE, ERROR,
)
from ....aid.bootstrap import (
    TARGET_WILDCARD,
    ListenerRegistrar,
)
from ....base.events.bus import (
    EventListenerAddedEvent,
    EVENT_ID_EVENT_LISTENER_ADDED,
)
from ....base.participant.component import (
    create_component_identity_from_unique_id,
)


class TypeSafeEventBus(EventBus):
    """
    A local, type-safe version of the EventBus.
    """
    __slots__ = ('__bus', '__reg', '__next_id', '__id_lock', '__lock_timeout')

    def __init__(self, bus: BasicEventBus, reg: EventRegistry) -> None:
        assert isinstance(bus, BasicEventBus)
        assert isinstance(reg, EventRegistry)
        self.__bus = bus
        self.__reg = reg
        self.__next_id = 1
        self.__id_lock = Lock()
        self.__lock_timeout = 0.1

    def add_listener(
            self,
            target_id: ParticipantId,
            listener_setup: ListenerRegistrar[T],
            listener: EventCallback[T]
    ) -> ListenerId:
        """
        Registers a type-safe event listener.  Cannot work with a wildcard event ID.

        Each event type should have a custom call function to wrap this.
        """
        event_id, listener = listener_setup(listener)
        self.__reg.validate_has(event_id)
        # swapping between typed T and any generic object.
        # Really, the Event* stuff should take a generic that is of type object.
        # But even that isn't right.  Look, it's complicated.  Don't judge me.
        callback: EventCallback[object] = lambda eid, tid, eo: (
            self.__listener_callback(  # type: ignore
                eid, tid,
                eo,  # type: ignore
                listener  # type: ignore
            ))

        ret = self.__bus.add_listener(
            event_id,
            target_id,
            callback
        )

        # Event added trigger is always sent after registration.  This means
        # that event listeners must be aware of the potential for infinite loops if written wrong.
        # This is sent after, and not before, because the threading model may just end up
        # getting this to run after the method completes anyway.
        self.trigger(
            EVENT_ID_EVENT_LISTENER_ADDED,
            TARGET_WILDCARD,
            EventListenerAddedEvent(event_id, target_id)
        )

        return ret

    def remove_listener(self, listener_id: ListenerId) -> bool:
        """De-register the listener."""
        return self.__bus.remove_listener(listener_id)

    def trigger(self, event_id: EventId, target_id: ParticipantId, event_obj: T) -> None:
        """
        Triggers an event to fire.  The event priority is based upon the
        event id registration.
        """
        # Use the "on trigger" version, so that the registry can hook into
        # early listening of register event events.
        self.__reg.validate_event_on_trigger(event_id, target_id, event_obj)
        priority = self.__reg.get_event_id_priority(event_id)
        assert priority
        self.__bus.trigger(priority, event_id, target_id, event_obj)

    def create_component_id(self, component_category: str) -> ComponentId:
        """
        Creates a unique component ID for a new component in the given
        category.

        Due to the coupling between the implementation of the event bus and
        the uniqueness guarantees of the component ID generation, the
        component ID generation is included in the event bus definition.
        """
        assert component_category
        assert isinstance(component_category, str)

        if not self.__id_lock.acquire(timeout=self.__lock_timeout):
            raise PetroniaLockTimeoutError()
        try:
            ret = self.__next_id
            self.__next_id += 1
        finally:
            self.__id_lock.release()
        return create_component_identity_from_unique_id(component_category, ret)

    def __listener_callback(
            self, event_id: EventId,
            target_id: ParticipantId,
            event_obj: T, callback: EventCallback[T]
    ) -> None:
        log(
            TRACE, TypeSafeEventBus.__listener_callback,
            'Calling listener {0}: event_id={1}, target_id={2}, event_obj={3}',
            callback, event_id, target_id, event_obj
        )
        try:
            self.__reg.validate_event(event_id, target_id, event_obj)
            log(TRACE, TypeSafeEventBus.__listener_callback, 'Valided, now calling callback')
            callback(event_id, target_id, event_obj)
            log(TRACE, TypeSafeEventBus.__listener_callback, 'Finished callback')
        except SystemExit:
            # Let everything else handle this.
            raise
        except BaseException as err:
            logerr(ERROR, TypeSafeEventBus.__listener_callback, err, 'Callback generated error')
            raise err
