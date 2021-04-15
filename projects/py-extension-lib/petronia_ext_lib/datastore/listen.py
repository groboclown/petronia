"""Listens to datastore update/delete events."""

from typing import Callable, Generic, Optional
from petronia_common.util import StdRet, T, RET_OK_NONE, tznow, join_none_results
from petronia_common.util import i18n as _
from ..events import datastore
from ..runner.registry import (
    EventObjectParser, EventRegistryContext, EventObjectTarget,
)
from ..standard.embedded_json_data import embedded_json_data
from ..extension_loader.registration import send_register_listeners
from ..defs import TRANSLATION_CATALOG


def register_listening_to_datastore(
        context: EventRegistryContext, extension_name: str, source_id: Optional[str],
) -> StdRet[None]:
    """Register an extension to listen to datastore update/delete events."""
    return send_register_listeners(
        context,
        extension_name,
        (
            (
                datastore.DataUpdateEvent.FULL_EVENT_NAME,
                source_id,
            ),
            (
                datastore.DataRemovedEvent.FULL_EVENT_NAME,
                source_id,
            ),
        ),
    )


def register_datastore_update_parsers(context: EventRegistryContext) -> StdRet[None]:
    """Register the datastore event parsers, for the listening end."""
    return join_none_results(
        context.register_event_parser(
            datastore.DataUpdateEvent.FULL_EVENT_NAME,
            datastore.DataUpdateEvent.parse_data,
        ),
        context.register_event_parser(
            datastore.DataRemovedEvent.FULL_EVENT_NAME,
            datastore.DataRemovedEvent.parse_data,
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

        self.changed = event.changed
        parsed = get_event_data_value(event, self.parser)
        self.value = parsed.value

        if self.callback:
            self.callback(self.value)

        if parsed.has_error:
            return parsed.forward()
        return RET_OK_NONE


def get_event_data_value(
        event: datastore.DataUpdateEvent,
        parser: EventObjectParser[T],
) -> StdRet[T]:
    """Convert the data stored in the event's json value using the parser."""
    structured_res = embedded_json_data(event.json)
    if structured_res.has_error:
        return structured_res.forward()
    value = structured_res.value
    if isinstance(value, dict):
        parsed_res = parser.parse(value)
        if parsed_res.has_error:
            return parsed_res.forward()
        return parsed_res
    return StdRet.pass_errmsg(
        TRANSLATION_CATALOG,
        _('Embedded json data for DataUpdateEvent is not a json dictionary'),
    )


def register_datastore_target_listener(
        context: EventRegistryContext,
        source_id: str,
        cache: CachedInstance[T],
) -> StdRet[None]:
    """Listens to events sent *to* the source_id (which is the datastore ID),
    and updates the cache accordingly.

    This requires the context to be able to listen to events sent to an event id + target."""

    return join_none_results(
        register_datastore_update_parsers(context),
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
