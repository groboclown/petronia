"""Handle event requests."""

from petronia_common.util import StdRet, join_errors, RET_OK_NONE
from petronia_ext_lib.runner import EventRegistryContext, EventObjectTarget
from . import shared_state
from .events.impl import datastore


def register_delete_data_listener(context: EventRegistryContext) -> StdRet[None]:
    """Register the store data listener."""
    res1 = context.register_event_parser(
        datastore.DeleteDataEvent.FULL_EVENT_NAME,
        datastore.DeleteDataEvent.parse_data,
    )
    res2 = context.register_target(
        datastore.DeleteDataEvent.FULL_EVENT_NAME,
        None,
        DeleteDataHandler(context),
    )
    if res1.has_error or res2.has_error:
        return StdRet.pass_error(join_errors(*res1.error_messages(), *res2.error_messages()))
    return RET_OK_NONE


class DeleteDataHandler(EventObjectTarget[datastore.DeleteDataEvent]):
    """Handles the store data requests."""
    __slots__ = ('__context',)

    def __init__(self, context: EventRegistryContext) -> None:
        self.__context = context

    def on_event(self, source: str, target: str, event: datastore.DeleteDataEvent) -> bool:
        if shared_state.delete_data(source):
            # Deleted.
            # Do not report problem on send event error
            self.__context.send_event(
                datastore.DeleteDataEvent.UNIQUE_TARGET_FQN,
                source,
                datastore.DataRemovedEvent(),
            )
        return False
