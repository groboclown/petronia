
# mypy: allow-any-expr
# mypy: allow-any-explicit
# mypy: allow-any-generics

"""
Shared data for a link.
"""

from typing import List, Dict, Set, Tuple, Sequence, Callable, Optional, Generic, Union, Any
from threading import Lock
from ...system.bus import (
    EventBus,
    EventId,
    ListenerRegistrator,
    TARGET_WILDCARD,
)
from ...system.participant import ParticipantId
from ...util.memory import T


Marks = Dict[str, object]
EventMatcher = Callable[[ParticipantId, T, Marks], bool]
IdentifierExtractor = Callable[[ParticipantId, T], object]
LinkRunner = Callable[[EventBus, Marks], None]
TargetGenerator = Callable[[Marks], ParticipantId]
EventObjectGenerator = Callable[[ParticipantId, Marks], T]


def send_runner(
        event_id: EventId,
        target_id: Union[ParticipantId, TargetGenerator], # pylint: disable=invalid-name
        obj: EventObjectGenerator[T]
) -> LinkRunner:
    """Create a LinkRunner function that sends an event."""
    def r(bus: EventBus, marks: Marks) -> None:
        if callable(target_id):
            to_id = target_id(marks)
        else:
            to_id = target_id
        bus.trigger(
            event_id,
            to_id,
            obj(to_id, marks)
        )
    return r



class LinkEventDetails(Generic[T]):
    """Stand-alone definition that identifies a matching event."""
    __slots__ = ('reg', 'matchers', 'track', 'target')

    def __init__(
            self,
            registrator: ListenerRegistrator[T],
            target: Optional[ParticipantId],
            matchers: List[EventMatcher[T]],
            track: Dict[str, IdentifierExtractor[T]]
    ) -> None:
        self.reg = registrator
        self.target = target
        self.matchers = matchers
        self.track = track


class LinkHandlerData(Generic[T]):
    """Stores data for a single event listener link."""
    __slots__ = (
        'timeout', 'link_id', 'next_link_id',
        'event_registrator', 'event_target_id', 'event_matchers',
        'event_extractors', 'generated_ints', 'generated_ids',
        'handlers', 'event_id', 'timeout',
    )
    event_target_id: Optional[ParticipantId]
    event_matchers: Sequence[EventMatcher[T]]
    event_extractors: Dict[str, IdentifierExtractor[T]]
    generated_ints: Set[str] # may be too much memory... a list instead?
    generated_ids: List[Tuple[str, str]]
    handlers: List[LinkRunner]

    def __init__(self, link_id: int, details: LinkEventDetails) -> None:
        self.link_id = link_id
        self.next_link_id = -1
        self.generated_ints = set()
        self.generated_ids = []
        self.handlers = []
        self.timeout_seconds = -1.0

        if details.target is None or details.target == TARGET_WILDCARD:
            self.event_target_id = None
        else:
            self.event_target_id = details.target
        self.event_registrator = details.reg
        self.event_matchers = tuple(details.matchers)
        self.event_extractors = details.track

        # hack to work-around the type safe nature...
        setup = self.event_registrator(None) # type: ignore
        self.event_id = setup[0]

    @property
    def is_valid(self) -> bool:
        """Is this a valid handler?"""
        return (
            # If there is no next link, then there has to be at least one
            # handler.
            self.next_link_id >= 0 or
            len(self.handlers) > 0
        )

    def is_matched_event(
            self,
            target_id: ParticipantId,
            event_obj: T,
            marks: Marks
    ) -> bool:
        """Assumes the event ID has already been matched."""
        if self.event_target_id and self.event_target_id != target_id:
            return False
        for matcher in self.event_matchers:
            if not matcher(target_id, event_obj, marks):
                return False
        return True


class MappedEvents:
    """A memory-safe mapping of events to chains, both active and
    templates.  This data structure is carefully constructed to
    work with the rest of the API in the event_chain module, so don't
    expect to work this this as an end-user.

    One aspect of this data structure is that it helps prevent inter-object
    references, so it can clean itself up just by removing references to the
    instance.

    The timeouts are not implemented yet.
    """
    __slots__ = (
        '__lock', '__bus',
        '_event_chain_start', '_handlers',
        '_active_event_links',
        '_active_chain_data', '__next_active_chain_id'
    )

    # The chain definitions.  Events will trigger creation of active
    # chains based on these.  They have internal links to each other based
    # on the next_link_id pointing to the key in this dictionary.
    _handlers: List[LinkHandlerData[Any]]

    # This is a list of each event name pointing to the first link in a
    # chain.  Each int is a pointer into the _handlers.  These are the
    # "templates" for creating a new chain.
    _event_chain_start: Dict[EventId, Set[int]]

    # Active chains are listening for a next event, which are added into
    # this list.
    _active_event_links: Dict[EventId, Set[int]]

    # The active chain ID (index in the list), pointing to the current handler
    # in the chain, and all the current marks for that chain.
    _active_chain_data: Dict[int, Tuple[int, Marks]]

    def __init__(self, bus: EventBus) -> None:
        self.__lock = Lock()
        self.__bus = bus
        self._handlers = []
        self._event_chain_start = {}
        self._active_event_links = {}
        self._active_chain_data = {}
        self.__next_active_chain_id = 0

    def create_next_handler_data(self, for_event: LinkEventDetails[T]) -> LinkHandlerData[T]:
        """Create a new LinkHandlerData instance."""
        ret: LinkHandlerData[T]
        with self.__lock:
            next_id = len(self._handlers)
            ret = LinkHandlerData(next_id, for_event)
            self._handlers.append(ret)
            assert self._handlers[next_id] is ret
        return ret

    def set_event_chain_start(self, handler: LinkHandlerData[T]) -> None:
        """Mark a previously created and constructed handler as the start of
        a chain."""
        with self.__lock:
            assert self._handlers[handler.link_id] is handler
            assert handler.is_valid
            if not self._event_chain_start[handler.event_id]:
                self._event_chain_start[handler.event_id] = set()
            self._event_chain_start[handler.event_id].add(handler.link_id)

    def check_timeouts(self) -> None:
        """Check the active waiting events to see if any of them have timed
        out."""

        # TODO needs implementation.

    def get_matched_events_and_targets(
            self
    ) -> Sequence[Tuple[ListenerRegistrator[Any], Set[Optional[ParticipantId]]]]:
        """Find all the events listend to in the handlers, and all of the
        explicitly specified participants for that event.  If a handler does
        not call out a participant, then a None is added."""
        registrators: Dict[EventId, ListenerRegistrator[Any]] = {}
        particpants: Dict[EventId, Set[Optional[ParticipantId]]] = {}
        for handler in self._handlers:
            if not handler.is_valid:
                # TODO better exception
                raise Exception(
                    'chain for event {0} is not valid'.format(handler.event_id)
                )
            if handler.event_id not in registrators:
                registrators[handler.event_id] = handler.event_registrator
            if handler.event_id not in particpants:
                particpants[handler.event_id] = set()
            particpants[handler.event_id].add(handler.event_target_id)

        ret: List[Tuple[ListenerRegistrator, Set[Optional[ParticipantId]]]] = []
        for event_id, participant_ids in particpants.items():
            ret.append((
                registrators[event_id],
                participant_ids,
            ))
        return ret


    def handle_event(
            self,
            event_id: EventId, target_id: ParticipantId,
            event_obj: T
    ) -> None:
        """
        Performs all the logic necessary to match the event against the
        chains, and advances the state based on the actions.
        """
        marks: Marks
        hid: int
        handler: LinkHandlerData[T]
        with self.__lock:
            if event_id in self._event_chain_start:
                # Create new active chains.
                marks = {}
                for hid in self._event_chain_start[event_id]:
                    handler = self._handlers[hid]
                    if handler.is_matched_event(target_id, event_obj, marks):
                        # The start of a new active chain.
                        active_chain_id = self.__next_active_chain_id
                        self.__next_active_chain_id += 1
                        self.__handle_link(
                            active_chain_id, handler,
                            target_id, event_obj,
                            marks
                        )
                        marks = {}
            if event_id in self._active_event_links:
                # Handling the links can change the list.  So make a copy of
                # it to prevent weird errors.
                active_ids = tuple(self._active_event_links[event_id])
                for active_chain_id in active_ids:
                    # This if condition should always be true, but just in case
                    # some weird edge case happens, it's here.
                    if active_chain_id in self._active_chain_data:
                        hid, marks = self._active_chain_data[active_chain_id]
                        handler = self._handlers[hid]
                        self.__handle_link(active_chain_id, handler, target_id, event_obj, marks)

    def __handle_link(
            self,
            active_chain_id: int,
            handler: LinkHandlerData[T],
            target_id: ParticipantId,
            event_obj: T,
            marks: Marks
    ) -> None:
        # Extract the event object parts.
        for key, extractor in handler.event_extractors.items():
            val_e = extractor(target_id, event_obj)
            marks[key] = val_e

        # Create the unique numbers.
        for key in handler.generated_ints:
            # Sure.  Let's reuse this counter.
            val_i = self.__next_active_chain_id
            self.__next_active_chain_id += 1
            marks[key] = val_i

        # Create the component ids.
        for key, category in handler.generated_ids:
            val_c = self.__bus.create_component_id(category)
            marks[key] = val_c

        # run the handlers.
        for runner in handler.handlers:
            runner(self.__bus, marks)

        # advance the handler.
        link_set = self._active_event_links[handler.event_id]
        link_set.discard(active_chain_id)
        if not link_set:
            del self._active_event_links[handler.event_id]

        next_handler_id = handler.next_link_id
        if next_handler_id >= 0:
            next_handler = self._handlers[next_handler_id]
            assert next_handler.event_id
            if next_handler.event_id not in self._active_event_links:
                self._active_event_links[next_handler.event_id] = set()
            self._active_event_links[next_handler.event_id].add(active_chain_id)
            self._active_chain_data[active_chain_id] = (next_handler_id, marks,)
        elif active_chain_id in self._active_chain_data:
            # End of the chain.  Need the if clause in the rare case of an
            # event chain with only the starting listener.
            del self._active_chain_data[active_chain_id]
