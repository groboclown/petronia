
"""
Definition for an "event handler", meaning can generate events or consume events.
The router associates targets with processes.
"""

from typing import Iterable, Mapping, Optional


class EventHandler:
    """Consumer and producer of events.  This is just the
    rough definition, enough for the router to understand what are
    valid sources and targets, and whether the events can be sent to them."""
    __slots__ = ('__handler_id', '__consumes', '__produces',)

    def __init__(
            self,
            handler_id: str,
            consumes_anonymous: Mapping[str, bool],
            produced_event_ids: Iterable[str],
    ) -> None:
        """

        :param handler_id:
        :param consumes_anonymous: mapping between the
            listened-to event ID and whether it listens to any event,
            regardless of its target.
        :param produced_event_ids: list of all event IDs that this handler
            can produce.
        """
        self.__handler_id = handler_id
        self.__consumes = dict(consumes_anonymous)
        self.__produces = set(produced_event_ids)

    def __repr__(self) -> str:
        return f"EventHandler({self.__handler_id})"

    @property
    def handler_id(self) -> str:
        """The event handler ID, for use with source and target IDs."""
        return self.__handler_id

    def can_produce(self, event_id: str) -> bool:
        """Returns True if the event id is valid for this handler."""
        return event_id in self.__produces

    def can_consume(self, event_id: str, target_id: Optional[str]) -> bool:
        """Returns True if the event id is valid for this handler.
        If the target ID is None, then it is a broadcast ID, meaning that
        any listener of the event will receive it.
        """
        is_anonymous = self.__consumes.get(event_id)
        return (
            is_anonymous is not None and
            (
                is_anonymous is True or
                target_id is None or
                target_id == self.__handler_id
            )
        )
