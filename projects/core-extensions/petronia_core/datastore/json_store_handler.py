"""Handle event requests."""
from petronia_common.util import StdRet, join_none_results
from petronia_ext_lib.logging import send_system_error
from petronia_ext_lib.runner import (
    EventRegistryContext, ContextEventObjectTarget,
)
from petronia_ext_lib.extension_loader import send_register_listeners
from petronia_ext_lib.standard.embedded_json_data import embedded_json_data
from petronia_ext_lib.standard.error import INTERNAL_ERROR_CATEGORY
from . import shared_state
from .events.impl import datastore as datastore_event
from .state import datastore as datastore_state
from ..user_messages import report_send_receive_problems


def register_json_store_data_listener(context: EventRegistryContext) -> StdRet[None]:
    """Register the store data listener."""
    return join_none_results(
        send_register_listeners(
            context,
            datastore_state.EXTENSION_NAME,
            (
                (datastore_event.StoreDataRequestEvent.FULL_EVENT_NAME, None),
            ),
        ),
        context.register_event_parser(
            datastore_event.StoreDataRequestEvent.FULL_EVENT_NAME,
            datastore_event.StoreDataRequestEvent.parse_data,
        ),
        context.register_target(
            datastore_event.StoreDataRequestEvent.FULL_EVENT_NAME,
            None,
            StoreDataHandler(context),
        ),
    )


class StoreDataHandler(ContextEventObjectTarget[datastore_event.StoreDataRequestEvent]):
    """Handles the store data requests."""

    def on_context_event(
            self, context: EventRegistryContext, source: str, target: str,
            event: datastore_event.StoreDataRequestEvent,
    ) -> bool:
        data = event.json
        valid_data = embedded_json_data(data)
        if valid_data.has_error:
            report_send_receive_problems('datastore', send_system_error(
                context,
                datastore_event.StoreDataRequestEvent.UNIQUE_TARGET_FQN,
                valid_data.valid_error,
                'invalid-json-data',
                [INTERNAL_ERROR_CATEGORY],
            ))
            return False
        _updated, new_date = shared_state.store_json_data(source, data)
        # print(f"[DATASTORE] stored data for {source}")
        report_send_receive_problems('datastore', context.send_event(
            datastore_event.SendStateRequestEvent.UNIQUE_TARGET_FQN,
            source,
            datastore_event.DataUpdatedEvent(new_date, data),
        ))
        return False