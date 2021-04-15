"""Handle event requests."""

from petronia_common.util import StdRet, join_none_results
from petronia_ext_lib.runner import EventRegistryContext, ContextEventObjectTarget
from petronia_ext_lib.extension_loader import send_register_listeners
from . import shared_state
from .events.impl import datastore as datastore_event
from .state import datastore as datastore_state
from ..user_messages import report_send_receive_problems


def register_post_data_listener(context: EventRegistryContext) -> StdRet[None]:
    """Register the store data listener."""
    return join_none_results(
        send_register_listeners(
            context,
            datastore_state.EXTENSION_NAME,
            (
                (datastore_event.SendStateEvent.FULL_EVENT_NAME, None),
            ),
        ),
        context.register_event_parser(
            datastore_event.SendStateEvent.FULL_EVENT_NAME,
            datastore_event.SendStateEvent.parse_data,
        ),
        context.register_target(
            datastore_event.SendStateEvent.FULL_EVENT_NAME,
            None,
            SendStateHandler(context),
        ),
    )


class SendStateHandler(ContextEventObjectTarget[datastore_event.SendStateEvent]):
    """Handles the store data requests."""

    def on_context_event(
            self, context: EventRegistryContext, source: str, target: str,
            event: datastore_event.SendStateEvent,
    ) -> bool:
        res = shared_state.get_data(event.store_id)
        if not res:
            # does not exist, so send removed event.
            print(f"[DATASTORE] sending delete update for {event.store_id}")
            report_send_receive_problems('datastore', context.send_event(
                # Yes, the source target comes from a different event...
                datastore_event.DeleteDataEvent.UNIQUE_TARGET_FQN,
                event.store_id,
                datastore_event.DataRemovedEvent(),
            ))
            return False
        print(f"[DATASTORE] sending data update for {event.store_id}")
        data, updated = res
        report_send_receive_problems('datastore', context.send_event(
            # Yes, the source target comes from a different event...
            datastore_event.StoreDataEvent.UNIQUE_TARGET_FQN,
            event.store_id,
            datastore_event.DataUpdateEvent(updated, data),
        ))
        return False
