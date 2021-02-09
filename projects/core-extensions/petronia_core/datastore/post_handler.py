"""Handle event requests."""

from petronia_common.util import StdRet, join_errors, RET_OK_NONE
from petronia_ext_lib.runner import EventRegistryContext, EventObjectTarget
from . import shared_state
from .events.impl import datastore


def register_post_data_listener(context: EventRegistryContext) -> StdRet[None]:
    """Register the store data listener."""
    res1 = context.register_event_parser(
        datastore.SendStateEvent.FULL_EVENT_NAME,
        datastore.SendStateEvent.parse_data,
    )
    res2 = context.register_target(
        datastore.SendStateEvent.FULL_EVENT_NAME,
        None,
        SendStateHandler(context),
    )
    if res1.has_error or res2.has_error:
        return StdRet.pass_error(join_errors(*res1.error_messages(), *res2.error_messages()))
    return RET_OK_NONE


class SendStateHandler(EventObjectTarget[datastore.SendStateEvent]):
    """Handles the store data requests."""
    __slots__ = ('__context',)

    def __init__(self, context: EventRegistryContext) -> None:
        self.__context = context

    def on_event(self, source: str, target: str, event: datastore.SendStateEvent) -> bool:
        res = shared_state.get_data(event.store_id)
        if not res:
            # does not exist, so send removed event.
            self.__context.send_event(
                datastore.DeleteDataEvent.UNIQUE_TARGET_FQN,
                source,
                datastore.DataRemovedEvent(),
            )
            return False
        data, updated = res
        self.__context.send_event(
            datastore.StoreDataEvent.UNIQUE_TARGET_FQN,
            event.store_id,
            datastore.DataUpdateEvent(updated, data),
        )
        return False
