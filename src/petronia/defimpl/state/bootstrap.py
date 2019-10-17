
"""
EventBus interaction for the global state.
"""

from ...core.state.api.events import (
    EVENT_ID_UPDATE_STATE_REQUEST,
    StateStoreUpdateRequestEvent,

    EVENT_ID_UPDATED_STATE,
    StateStoreUpdatedEvent,
)
from ...aid.std import (
    EventId,
    EventBus, EventCallback,
    ParticipantId,
    T,
    log,
    TRACE, VERBOSE,
)
from ...aid.bootstrap import (
    create_singleton_identity,
    ListenerSetup,
    ANY_VERSION,
)
from ...base.bus import (
    EventListenerAddedEvent,
    as_listener_added_listener,
    TARGET_WILDCARD,
)
from ...base.internal_.internal_extension import petronia_extension
from ...aid.lifecycle import create_module_listener_helper
from .store import StateStore


MODULE_ID = create_singleton_identity('default.state')

EXTENSION_METADATA = petronia_extension({
    'type': 'impl',
    'implements': ({
        'extension': 'core.state.api',
        'minimum': ANY_VERSION,
    },),
    'depends': (),
    'name': 'default.state',
    'version': (1, 0, 0,),
})


def bootstrap_state_store(bus: EventBus) -> None:
    """Register all state store events."""
    helper = create_module_listener_helper(bus, MODULE_ID)
    store = _BusAwareStateStore(bus)
    # ListenerIds are not persisted, because this is a singleton
    # that is never disposed.
    helper.listen(  # type: ignore
        TARGET_WILDCARD,
        _as_update_state_request_listener,
        store.on_update_request
    )
    helper.listen(
        TARGET_WILDCARD,
        as_listener_added_listener,
        store.on_listener_added
    )


class _BusAwareStateStore:
    """
    A StateStore that correctly interacts with the EventBus.
    """
    __slots__ = ('__bus', '__store',)

    def __init__(self, bus: EventBus) -> None:
        self.__bus = bus
        self.__store = StateStore()

    def on_update_request(
            self,
            _eid: EventId, _tid: ParticipantId,  # pylint: disable=unused-argument
            event: StateStoreUpdateRequestEvent[T]
    ) -> None:
        """When a state is requested to be updated."""
        old_state = self.__store.set_state(
            event.state_id, event.state_type,
            event.state
        )
        log(VERBOSE, _BusAwareStateStore, 'Updated state for {0}', _tid)
        log(TRACE, _BusAwareStateStore, 'Set {0} state to {1}', _tid, event.state)
        self.__bus.trigger(EVENT_ID_UPDATED_STATE, event.state_id, StateStoreUpdatedEvent(
            event.state_id, event.state_type, event.state, old_state
        ))

    def on_listener_added(
            self,
            eid: EventId, tid: ParticipantId,  # pylint: disable=unused-argument
            event: EventListenerAddedEvent
    ) -> None:
        """
        Whenever a new listener is added to the event bus.
        This allows new listeners to a specific state to receive the state when they
        start.
        """
        if event.event_id == EVENT_ID_UPDATED_STATE and tid in self.__store:
            log(
                TRACE, _BusAwareStateStore.on_listener_added,
                'Handling request to listen for an update state {0} event',
                tid
            )
            # Rebroadcast the state.
            state = self.__store.get_state(tid)
            state_type = self.__store.get_state_type(tid)
            if state and state_type:
                log(
                    TRACE, _BusAwareStateStore.on_listener_added,
                    'Sending out the current state for {0} {1}', tid, state
                )
                print("DEBUG Sending out the current state for {0} {1}".format(tid, state))
                self.__bus.trigger(EVENT_ID_UPDATED_STATE, tid, StateStoreUpdatedEvent(
                    tid, state_type, state, state
                ))


def _as_update_state_request_listener(
        callback: EventCallback[StateStoreUpdateRequestEvent[T]]
) -> ListenerSetup[StateStoreUpdateRequestEvent[T]]:
    return (EVENT_ID_UPDATE_STATE_REQUEST, callback,)
