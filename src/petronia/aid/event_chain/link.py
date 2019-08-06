
"""
The chain construction API.
"""

from typing import Generic, Dict, List, Union, Optional
from .data import (
    EventMatcher,
    MappedEvents,
    IdentifierExtractor,
    LinkRunner,
    LinkHandlerData,
    LinkEventDetails,
    TargetGenerator,
    EventObjectGenerator,
    send_runner,
)
from ...base.bus import (
    ListenerRegistrator,
    EventId,
)
from ...base import ParticipantId
from ...base.util import T, V, ValueHolder


class EventHas(Generic[T]):
    """Stand-alone definition that identifies a matching event."""
    __slots__ = ('_reg', '_matchers', '_track', '_target')
    _target: Optional[ParticipantId]
    _matchers: List[EventMatcher[T]]
    _track: Dict[str, IdentifierExtractor[T]]

    def __init__(self, registrator: ListenerRegistrator[T]) -> None:
        self._reg = registrator
        self._matchers = []
        self._track = {}
        self._target = None

    def to(self, target_id: ParticipantId) -> 'EventHas[T]': # pylint: disable=invalid-name
        """Set the matching target for the event.  This can only be done for
        hard-coded target IDs; for marked target IDs, use the matching
        function instead."""
        self._target = target_id
        return self

    def matching(
            self,
            matcher: EventMatcher[T]
    ) -> 'EventHas[T]':
        """Checks the event object to see if it should be handled."""
        self._matchers.append(matcher)
        return self

    def track(
            self,
            key: str,
            extractor: IdentifierExtractor[T]
    ) -> 'EventHas[T]':
        """Extract part of the event into a "mark" value that can be used in
        later event processing routines."""
        self._track[key] = extractor
        return self

    @property
    def and_has(self) -> 'EventHas[T]':
        """Connective tissue for making nice reading sentances."""
        return self

    def finish(self) -> LinkEventDetails[T]:
        """Internal use only."""
        return LinkEventDetails(self._reg, self._target, self._matchers, self._track)



class EventLinkRunner(Generic[T]):
    """
    Adds in the ordered handlers for the event.
    """
    __slots__ = ('_chains', '_data',)

    def __init__(self, chains: MappedEvents, data: LinkHandlerData[T]) -> None:
        """Internal use only.  Do not call directly."""
        self._chains = chains
        self._data = data

    def run(
            self,
            runner: LinkRunner
    ) -> 'EventLinkRunner[T]':
        """Run the handler."""
        self._data.handlers.append(runner)
        return self

    def send(
            self,
            event_id: EventId,
            to_target: Union[ParticipantId, TargetGenerator],
            event_obj: EventObjectGenerator[T]
    ) -> 'EventLinkRunner[T]':
        """Send an event."""
        self._data.handlers.append(send_runner(event_id, to_target, event_obj))
        return self

    @property
    def and_also(self) -> 'EventLinkRunner[T]':
        """syntactic sugar."""
        return self

    def then(self) -> 'EventLinkWait':
        """Wait for another event after this one."""
        return EventLinkWait(self._chains, self._data)



class EventLinkPrep(Generic[T]):
    """
    Preperations to handling the event.
    """
    __slots__ = ('_chains', '_data',)

    def __init__(self, chains: MappedEvents, data: LinkHandlerData[T]) -> None:
        """Internal use only.  Do not call directly."""
        self._chains = chains
        self._data = data

    def create_unique_int_as(
            self,
            mark_id: str
    ) -> 'EventLinkPrep[T]':
        """Add a unique integer (for this chain) into the set of marks for
        later use in this event handling chain."""
        self._data.generated_ints.add(mark_id)
        return self

    def create_component_id(
            self,
            mark_id: str,
            component_category: str
    ) -> 'EventLinkPrep[T]':
        """Create a new component ID in this event handling chain."""
        self._data.generated_ids.append((mark_id, component_category,))
        return self

    def then_wait_for(self) -> 'EventLinkWait':
        """Don't perform any actions, and instead start waiting for another
        event to occur."""
        return EventLinkWait(self._chains, self._data)

    def then_handle_with(self) -> EventLinkRunner[T]:
        """Start handling the event."""
        return EventLinkRunner(self._chains, self._data)


class EventLinkWait:
    """
    Start of a new chain, or waiting for more events.
    """
    __slots__ = ('_chains', '__prev_data', '__timeout', '_next')

    def __init__(self, chains: MappedEvents, prev_data: Optional[LinkHandlerData[V]]) -> None:
        """Internal use only.  Do not call directly."""
        self._chains = chains
        self.__prev_data = prev_data
        self.__timeout = -1.0

    def with_timeout(self, timeout_seconds: float) -> 'EventLinkWait':
        """
        Time to allow waiting on these events before the wait is considered timed out.
        This uses the timer events to wake up and cancel the events.  If the event is
        received after the chain timed out, but before the timer event triggers, then
        the event chain isn't considered timed out, and it processes like usual.
        """
        self.__timeout = timeout_seconds
        return self

    def when(
            self,
            event_like: Union[EventHas[T], LinkEventDetails[T]]
    ) -> EventLinkPrep[T]:
        """
        When an event that matches the given identification is encountered, start the
        next part of the link.
        """
        next_link = self._setup_next(event_like)
        return EventLinkPrep(self._chains, next_link)

    def _setup_next(
            self,
            event_like: Union[EventHas[T], LinkEventDetails[T]]
    ) -> LinkHandlerData[T]:
        assert not self.__prev_data or self.__prev_data.next_link_id < 0

        if isinstance(event_like, EventHas):
            details = event_like.finish()
        else:
            details = event_like

        next_link = self._chains.create_next_handler_data(details)
        if self.__prev_data:
            self.__prev_data.next_link_id = next_link.link_id
        return next_link


class EventLinkStart(EventLinkWait):
    """
    Start of a new chain.
    """
    __slots__ = ('__total_timeout', '__first')

    def __init__(self, chains: MappedEvents, first: ValueHolder[LinkHandlerData[V]]) -> None:
        """Internal use only.  Do not call directly."""
        EventLinkWait.__init__(self, chains, None)
        self.__total_timeout = -1.0
        self.__first = first

    def with_total_timeout(self, timeout_seconds: float) -> EventLinkWait:
        """
        The entire chain has this long to wait before the link is considered timed out.
        This uses the timer events to wake up and cancel the events.  If it timed out
        before the timer event, then the events will keep processing.

        A value < 0 will result in no timeout.
        """
        self.__total_timeout = timeout_seconds
        return self

    def when(
            self,
            event_like: Union[EventHas[T], LinkEventDetails[T]]
    ) -> EventLinkPrep[T]:
        """
        When an event that matches the given identification is encountered, start the
        next part of the link.
        """
        assert not self.__first.value
        next_link = self._setup_next(event_like)
        self.__first.value = next_link
        return EventLinkPrep(self._chains, next_link)
