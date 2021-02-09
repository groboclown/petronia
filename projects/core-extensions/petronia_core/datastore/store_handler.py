"""Handle event requests."""

from petronia_common.util import StdRet, join_errors, RET_OK_NONE
from petronia_ext_lib.logging import send_system_error
from petronia_ext_lib.runner import EventRegistryContext, EventObjectTarget
from petronia_ext_lib.standard.embedded_json_data import embedded_json_data
from petronia_ext_lib.standard.error import INTERNAL_ERROR_CATEGORY
from . import shared_state
from .events.impl import datastore


def register_store_data_listener(context: EventRegistryContext) -> StdRet[None]:
    """Register the store data listener."""
    res1 = context.register_event_parser(
        datastore.StoreDataEvent.FULL_EVENT_NAME,
        datastore.StoreDataEvent.parse_data,
    )
    res2 = context.register_target(
        datastore.StoreDataEvent.FULL_EVENT_NAME,
        None,
        StoreDataHandler(context),
    )
    if res1.has_error or res2.has_error:
        return StdRet.pass_error(join_errors(*res1.error_messages(), *res2.error_messages()))
    return RET_OK_NONE


class StoreDataHandler(EventObjectTarget[datastore.StoreDataEvent]):
    """Handles the store data requests."""
    __slots__ = ('__context',)

    def __init__(self, context: EventRegistryContext) -> None:
        self.__context = context

    def on_event(self, source: str, target: str, event: datastore.StoreDataEvent) -> bool:
        data = event.json
        valid_data = embedded_json_data(data)
        if valid_data.has_error:
            # Ignore error if it can't send.
            send_system_error(
                self.__context,
                datastore.StoreDataEvent.UNIQUE_TARGET_FQN,
                valid_data.valid_error,
                [INTERNAL_ERROR_CATEGORY],
                'invalid-json-data',
            )
            return False
        _updated, new_date = shared_state.store_data(source, data)
        # Ignore error if can't send.
        self.__context.send_event(
            datastore.StoreDataEvent.UNIQUE_TARGET_FQN,
            source,
            datastore.DataUpdateEvent(new_date, data),
        )
        return False
