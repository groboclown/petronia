
"""
Definition for an "event handler", meaning can generate events or consume events.
The router associates targets with processes.
"""

from typing import Dict, Iterable, Sequence, List, Set, Tuple, Optional

from petronia_common.util import StdRet, RET_OK_NONE
from petronia_common.util import i18n as _
from ..constants import TRANSLATION_CATALOG as CATALOG

# EventId, TargetId
EventTargetHandle = Tuple[Optional[str], Optional[str]]
_NONE_NONE: EventTargetHandle = (None, None)


class EventHandlerSet:
    """A collection of event handlers."""
    __slots__ = (
        '__handler_produces', '__handler_consumes', '__handler_source_prefixes',
        '__produces', '__sources', '__consumes',
    )

    def __init__(self) -> None:
        self.__handler_produces: Dict[str, Sequence[str]] = {}
        self.__handler_consumes: Dict[str, List[EventTargetHandle]] = {}
        self.__handler_source_prefixes: Dict[str, Sequence[str]] = {}
        self.__produces: Set[str] = set()
        self.__sources: Set[str] = set()
        self.__consumes: Set[EventTargetHandle] = set()

    def can_produce(self, event_id: str, source_id: str) -> bool:
        """Can this set of handlers produce the given event id with the soruce id?"""
        if event_id not in self.__produces:
            return False
        for source_prefix in self.__sources:
            if source_id.startswith(source_prefix):
                return True
        return False

    def can_consume(self, event_id: str, target_id: str) -> bool:
        """Can this set of handlers consume the given event_id + target_id?"""
        to_check: Set[Tuple[Optional[str], Optional[str]]] = {
            _NONE_NONE,
            (event_id, None),
            (None, target_id),
            (event_id, target_id),
        }
        # print(f"Handler: can consume {to_check} in {self.__consumes}")
        return not self.__consumes.isdisjoint(to_check)

    def contains_handler_id(self, handler_id: str) -> bool:
        """Does this handler set contain the given handler?"""
        return handler_id in self.__handler_consumes

    def add_handler(
            self,
            handler_id: str,
            produces: Iterable[str],
            initial_consumes: Iterable[EventTargetHandle],
            source_id_prefixes: Iterable[str],
    ) -> StdRet[None]:
        """Add a new handler to the set.  The list of consumes can include duplicate
        values, and that list of duplicates will be maintained over time.

        If the same handler_id is already registered, an error is returned."""
        if handler_id in self.__handler_consumes:
            return StdRet.pass_errmsg(
                CATALOG,
                _('event handler {handler_id} already registered'),
                handler_id=handler_id,
            )
        self.__handler_produces[handler_id] = tuple(produces)
        self.__handler_consumes[handler_id] = list(initial_consumes)
        self.__handler_source_prefixes[handler_id] = tuple(source_id_prefixes)
        self.__produces.update(produces)
        self.__sources.update(source_id_prefixes)
        self.__consumes.update(initial_consumes)
        return RET_OK_NONE

    def add_listener(
            self, handler_id: str, event_id: Optional[str], target_id: Optional[str],
    ) -> StdRet[None]:
        """Add an event / target listener registration to the handler id."""
        if handler_id not in self.__handler_consumes:
            return StdRet.pass_errmsg(
                CATALOG,
                _('event handler {handler_id} not registered'),
                handler_id=handler_id,
            )
        event_handle = (event_id, target_id)
        self.__handler_consumes[handler_id].append(event_handle)
        self.__consumes.add(event_handle)
        return RET_OK_NONE

    def remove_listener(
            self, handler_id: str, event_id: Optional[str], target_id: Optional[str],
    ) -> StdRet[None]:
        """Remove the event / target listener registration for this handler."""
        if handler_id not in self.__handler_consumes:
            return StdRet.pass_errmsg(
                CATALOG,
                _('event handler {handler_id} not registered'),
                handler_id=handler_id,
            )
        event_handle = (event_id, target_id)
        try:
            self.__handler_consumes[handler_id].remove(event_handle)
        except ValueError:
            return StdRet.pass_errmsg(
                CATALOG,
                _('handler {handler_id} is not registered to listen to {event_id} / {target_id}'),
                handler_id=handler_id,
                event_id=event_id,
                target_id=target_id,
            )
        return RET_OK_NONE

    def remove_handler(self, handler_id: str) -> StdRet[None]:
        """Remove the handler from this set."""
        if handler_id not in self.__handler_consumes:
            return StdRet.pass_errmsg(
                CATALOG,
                _('event handler {handler_id} not registered'),
                handler_id=handler_id,
            )
        del self.__handler_consumes[handler_id]
        del self.__handler_produces[handler_id]
        self._reprocess_structures()
        return RET_OK_NONE

    def _reprocess_structures(self) -> None:
        self.__produces.clear()
        self.__sources.clear()
        self.__consumes.clear()
        for produces in self.__handler_produces.values():
            self.__produces.update(produces)
        for consumes in self.__handler_consumes.values():
            self.__consumes.update(consumes)
        for sources in self.__handler_source_prefixes.values():
            self.__sources.update(sources)
