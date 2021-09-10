"""Handle event requests."""

from petronia_common.util import StdRet, join_none_results
from petronia_ext_lib.runner import EventRegistryContext, ContextEventObjectTarget
from petronia_ext_lib.extension_loader import send_register_listeners
from . import shared_state
from .events.impl import binarystore as binarystore_event
from .state import binarystore as binarystore_state
from ..user_messages import report_send_receive_problems


def register_bin_delete_data_listener(context: EventRegistryContext) -> StdRet[None]:
    """Register the store data listener."""
    return join_none_results(
        send_register_listeners(
            context,
            binarystore_state.EXTENSION_NAME,
            (
                (binarystore_event.DeleteDataRequestEvent.FULL_EVENT_NAME, None),
            ),
        ),
        context.register_event_parser(
            binarystore_event.DeleteDataRequestEvent.FULL_EVENT_NAME,
            binarystore_event.DeleteDataRequestEvent.parse_data,
        ),
        context.register_target(
            binarystore_event.DeleteDataRequestEvent.FULL_EVENT_NAME,
            binarystore_event.DeleteDataRequestEvent.UNIQUE_TARGET_FQN,
            DeleteDataHandler(context),
        ),
    )


class DeleteDataHandler(ContextEventObjectTarget[binarystore_event.DeleteDataRequestEvent]):
    """Handles the store data requests."""

    def on_context_event(
            self, context: EventRegistryContext, source: str, target: str,
            event: binarystore_event.DeleteDataRequestEvent,
    ) -> bool:
        if shared_state.delete_binary_data(source):
            # Deleted.
            print(f"[DATASTORE] deleted data for {source}")
            report_send_receive_problems('binarystore', context.send_event(
                binarystore_event.DeleteDataRequestEvent.UNIQUE_TARGET_FQN,
                source,
                binarystore_event.DataDescriptionEvent(
                    state='deleted', mime_type=None, sha256=None, size=None,
                ),
            ))
        return False
