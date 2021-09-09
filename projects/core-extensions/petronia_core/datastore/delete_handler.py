"""Handle event requests."""

from petronia_common.util import StdRet, join_none_results
from petronia_ext_lib.runner import EventRegistryContext, ContextEventObjectTarget
from petronia_ext_lib.extension_loader import send_register_listeners
from . import shared_state
from .events.impl import datastore as datastore_event
from .state import datastore as datastore_state
from ..user_messages import report_send_receive_problems


def register_delete_data_listener(context: EventRegistryContext) -> StdRet[None]:
    """Register the store data listener."""
    return join_none_results(
        send_register_listeners(
            context,
            datastore_state.EXTENSION_NAME,
            (
                (datastore_event.DeleteDataRequestEvent.FULL_EVENT_NAME, None),
            ),
        ),
        context.register_event_parser(
            datastore_event.DeleteDataRequestEvent.FULL_EVENT_NAME,
            datastore_event.DeleteDataRequestEvent.parse_data,
        ),
        context.register_target(
            datastore_event.DeleteDataRequestEvent.FULL_EVENT_NAME,
            None,
            DeleteDataHandler(context),
        ),
    )


class DeleteDataHandler(ContextEventObjectTarget[datastore_event.DeleteDataRequestEvent]):
    """Handles the store data requests."""

    def on_context_event(
            self, context: EventRegistryContext, source: str, target: str,
            event: datastore_event.DeleteDataRequestEvent,
    ) -> bool:
        if shared_state.delete_data(source):
            # Deleted.
            print(f"[DATASTORE] deleted data for {source}")
            report_send_receive_problems('datastore', context.send_event(
                datastore_event.DeleteDataRequestEvent.UNIQUE_TARGET_FQN,
                source,
                datastore_event.DataRemovedEvent(),
            ))
        return False
