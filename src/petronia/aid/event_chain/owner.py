
"""
Creates a listener + sender chain for the event bus for easier to manage
action processing.
"""

from typing import List, Optional
from .data import (
    MappedEvents,
    LinkHandlerData,
)
from .link import (
    EventLinkStart,
)
from ..listener_set import ListenerSet
from ...base import (
    EventBus,
    EventId,
    ParticipantId,
    TARGET_WILDCARD,

    as_request_dispose_listener,
    send_dispose_complete_event,
    RequestDisposeEvent,
)
from ...base.util import ValueHolder


class EventChainManager:
    """
    Listener + sender process.

    This does not register itself to listen on dispose events.  Instead,
    the `dispose` method should be called as part of the owner's normal event
    disposal.  Or, if this is for a stand-alone thing, then the
    `make_self_disposed` should be called; note that this will cause the
    disposal to send a dispose complete event.

    The senders cannot have any kind of internal waiting for other
    events in the chain, as the events are handled sequentially inside the
    handler for this manager.  These kinds of actions will require passing
    the execution handle to another thread.
    """
    __slots__ = ('__pid', '__bus', '_chain_starts', '_mapping', '__listeners', '__disposed',)
    _chain_starts: Optional[List[ValueHolder[LinkHandlerData[object]]]]
    _mapping: Optional[MappedEvents]

    def __init__(self, bus: EventBus, pid: ParticipantId) -> None:
        self.__bus = bus
        self.__pid = pid
        self._chain_starts = []
        self._mapping = MappedEvents(bus)
        self.__listeners = ListenerSet(bus)
        self.__disposed = False

    def create(self) -> EventLinkStart:
        """
        Create a new chain of event processing.
        """
        chains = self._chain_starts
        mapping = self._mapping
        if chains is None or mapping is None:
            # TODO better exception
            raise Exception('already setup chain')
        first: ValueHolder[LinkHandlerData[object]] = ValueHolder(None)
        chains.append(first)
        return EventLinkStart(mapping, first)

    def setup(self) -> None:
        """
        Set up the chain listeners and states.
        """
        chains = self._chain_starts
        mapping = self._mapping
        if chains is None or mapping is None:
            raise Exception('already setup chains')
        if not chains:
            return
        # Clean up the state memory.
        self._chain_starts = None
        self._mapping = None

        # Register all declared events with the correct participant.
        # The mapping object handles the event listening code.

        for first in chains:
            assert first.value
            mapping.set_event_chain_start(first.value)

        events_and_targets = mapping.get_matched_events_and_targets() # type: ignore
        for event_reg, participants in events_and_targets: # type: ignore
            if not participants:
                continue
            if None in participants:
                # No ID to listen on.
                self.__listeners.listen(
                    TARGET_WILDCARD,
                    event_reg, # type: ignore
                    mapping.handle_event
                )
            else:
                # listen on specific ids
                for pid in participants:
                    # Shouldn't ever happen, due to the above check.
                    assert pid is not None
                    self.__listeners.listen(
                        pid,
                        event_reg, # type: ignore
                        mapping.handle_event
                    )


    def dispose(self) -> bool:
        """
        Dispose all the listeners controlled by this chain..
        """
        if self.__disposed:
            return False
        self.__disposed = True
        self._mapping = None
        self._chain_starts = None
        self.__listeners.dispose()
        return True

    def make_self_diposed(self) -> None:
        """
        Turn this set of chain handlers into a self-controlled component.
        This means that it will listen for dipose requests, and dispose itself,
        and send a dispose complete event.
        """
        self.__listeners.listen(self.__pid, as_request_dispose_listener, self.__self_dipose)

    def __self_dipose(
            self,
            eid: EventId, # pylint: disable=unused-argument
            tid: ParticipantId,
            eobj: RequestDisposeEvent # pylint: disable=unused-argument
    ) -> None:
        if tid != self.__pid:
            return
        if self.dispose():
            send_dispose_complete_event(self.__bus, self.__pid)
