"""Handle event requests."""

import os
from petronia_common.util import StdRet, join_none_results
from petronia_common.util import i18n as _
from petronia_ext_lib.runner import EventRegistryContext, ContextEventObjectTarget
from petronia_ext_lib.extension_loader import send_register_listeners
from . import shared_state
from .events.impl import datastore as datastore_event
from .state import datastore as datastore_state
from ..user_messages import report_send_receive_problems, TRANSLATION_CATALOG


def register_post_data_listener(context: EventRegistryContext) -> StdRet[None]:
    """Register the store data listener."""
    return join_none_results(
        send_register_listeners(
            context,
            datastore_state.EXTENSION_NAME,
            (
                (datastore_event.SendStateRequestEvent.FULL_EVENT_NAME, None),
            ),
        ),
        context.register_event_parser(
            datastore_event.SendStateRequestEvent.FULL_EVENT_NAME,
            datastore_event.SendStateRequestEvent.parse_data,
        ),
        context.register_target(
            datastore_event.SendStateRequestEvent.FULL_EVENT_NAME,
            None,
            SendStateHandler(context),
        ),
    )


class SendStateHandler(ContextEventObjectTarget[datastore_event.SendStateRequestEvent]):
    """Handles the store data requests."""

    def on_context_event(
            self, context: EventRegistryContext, source: str, target: str,
            event: datastore_event.SendStateRequestEvent,
    ) -> bool:
        res = shared_state.get_data(event.store_id)
        if res:
            print(f"[DATASTORE] sending data update for {event.store_id}")
            data, updated = res
            report_send_receive_problems('datastore', context.send_event(
                # Yes, the source target comes from a different event...
                datastore_event.StoreDataRequestEvent.UNIQUE_TARGET_FQN,
                event.store_id,
                datastore_event.DataUpdatedEvent(updated, data),
            ))
            return False
        res_bin = shared_state.get_binary_file(event.store_id)
        if res_bin:
            if not os.path.isfile(res_bin):
                report_send_receive_problems('datastore', StdRet.pass_errmsg(
                    TRANSLATION_CATALOG,
                    _('Could not find cache file {filename}'),
                    filename=res_bin,
                ))
                return False
            file_size = os.path.getsize(res_bin)
            with open(res_bin, 'rb') as f:
                report_send_receive_problems('datastore', context.send_binary_event_stream(
                    datastore_event.StoreBinaryRequestEvent.UNIQUE_TARGET_FQN,
                    event.store_id,
                    datastore_event.BinaryUpdatedEvent.FULL_EVENT_NAME,
                    file_size, f.read,
                ))
            return False
        # does not exist, so send removed event.
        print(f"[DATASTORE] sending delete update for {event.store_id}")
        report_send_receive_problems('datastore', context.send_event(
            # Yes, the source target comes from a different event...
            datastore_event.DeleteDataRequestEvent.UNIQUE_TARGET_FQN,
            event.store_id,
            datastore_event.DataRemovedEvent(),
        ))
        return False
