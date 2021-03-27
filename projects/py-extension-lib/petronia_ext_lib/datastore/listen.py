"""Listens to datastore update/delete events."""

from typing import Callable, Generic, Optional
from petronia_common.util import StdRet, T, RET_OK_NONE, tznow, join_none_results
from ..events import datastore
from ..runner.registry import (
    EventObjectParser, EventRegistryContext, EventObjectTarget,
)
from ..standard.embedded_json_data import embedded_json_data


def register_datastore_update_parsers(context: EventRegistryContext) -> StdRet[None]:
    """Register the datastore event parsers, for the listening end."""
    return join_none_results(
        context.register_event_parser(
            datastore.DataUpdateEvent.FULL_EVENT_NAME,
            datastore.DataUpdateEvent.parse_data,
        ),
        context.register_event_parser(
            datastore.DeleteDataEvent.FULL_EVENT_NAME,
            datastore.DeleteDataEvent.parse_data,
        ),
    )


class CachedInstance(Generic[T]):
    """Caches the value and a callback for changes.

    Due to potential threading issues, there is no built-in has-value or not-none."""
    __slots__ = ('value', 'callback', 'parser', 'changed')

    def __init__(
            self, parser: EventObjectParser[T],
            callback: Optional[Callable[[Optional[T]], None]],
    ) -> None:
        self.parser = parser
        self.callback = callback
        self.value: Optional[T] = None
        self.changed = tznow()

    def on_delete(self) -> None:
        """Handle a delete event."""
        if self.value is not None:
            self.value = None
            self.changed = tznow()
            if self.callback:
                self.callback(None)

    def update(self, event: datastore.DataUpdateEvent) -> StdRet[None]:
        """Handle an update data event."""
        if event.changed == self.changed:
            # If the event change date is the exact same as the one in this cache,
            # then the API definition says that the value is unchanged.
            return RET_OK_NONE

        ret = RET_OK_NONE
        self.changed = event.changed
        parsed: Optional[T]
        structured_res = embedded_json_data(event.json)
        if structured_res.has_error:
            ret = structured_res.forward()
        value = structured_res.value
        if isinstance(value, dict):
            parsed_res = self.parser.parse(value)
            if parsed_res.has_error:
                ret = parsed_res.forward()
            parsed = parsed_res.value
        else:
            parsed = None

        self.value = parsed
        if self.callback:
            self.callback(parsed)
        return ret


def register_datastore_target_listener(
        context: EventRegistryContext,
        source_id: str,
        cache: CachedInstance[T],
) -> StdRet[None]:
    """Listens to events sent *to* the source_id (which is the datastore ID),
    and updates the cache accordingly.

    This requires the context to be able to listen to events sent to an event id + target."""
    # Ignore errors from this registration step, because we don't care if it's already
    # been registered.
    register_datastore_update_parsers(context)
    return join_none_results(
        context.register_target(
            datastore.DataRemovedEvent.FULL_EVENT_NAME,
            source_id, StoreDeleteEventListener(cache),
        ),
        context.register_target(
            datastore.DataUpdateEvent.FULL_EVENT_NAME,
            source_id, StoreUpdateEventListener(cache),
        ),
    )


class StoreDeleteEventListener(EventObjectTarget[datastore.DataRemovedEvent], Generic[T]):
    """Listens to the delete event."""
    __slots__ = ('__cache',)

    def __init__(self, cache: CachedInstance[T]):
        self.__cache = cache

    def on_event(self, source: str, target: str, event: datastore.DataRemovedEvent) -> bool:
        # Note: throws away the error.
        self.__cache.on_delete()
        return False


class StoreUpdateEventListener(EventObjectTarget[datastore.DataUpdateEvent], Generic[T]):
    """Listens to the delete event."""
    __slots__ = ('__cache',)

    def __init__(self, cache: CachedInstance[T]):
        self.__cache = cache

    def on_event(self, source: str, target: str, event: datastore.DataUpdateEvent) -> bool:
        # Note: throws away the error.
        self.__cache.update(event)
        return False
