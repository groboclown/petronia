"""Listens to datastore update/delete events."""

from typing import Callable, Generic, Optional
from petronia_common.util import StdRet, T, tznow, RET_OK_NONE
from ..events import datastore
from ..runner.registry import (
    EventObjectParser,
)
from ..standard.embedded_json_data import embedded_json_data


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
