"""Handle event requests."""

from petronia_common.util import StdRet, join_none_results
from petronia_ext_lib.runner import EventRegistryContext, EventObjectTarget
from petronia_ext_lib.extension_loader import send_register_listeners
from . import shared_state
from .events.impl import datastore


def register_delete_data_listener(context: EventRegistryContext) -> StdRet[None]:
    """Register the store data listener."""
    return join_none_results(
        send_register_listeners(
            context,
            datastore.EXTENSION_NAME,
            (
                (datastore.DeleteDataEvent.FULL_EVENT_NAME, None),
            ),
        ),
        context.register_event_parser(
            datastore.DeleteDataEvent.FULL_EVENT_NAME,
            datastore.DeleteDataEvent.parse_data,
        ),
        context.register_target(
            datastore.DeleteDataEvent.FULL_EVENT_NAME,
            None,
            DeleteDataHandler(context),
        ),
    )


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
