"""Handle event requests."""

from petronia_common.event_stream import convert_reader_to_raw
from petronia_common.util import StdRet, join_none_results
from petronia_common.util import i18n as _
from petronia_ext_lib.runner import EventRegistryContext, ContextEventObjectTarget
from petronia_ext_lib.extension_loader import send_register_listeners
from . import shared_state
from .events.impl import binarystore as binarystore_event
from .state import binarystore as binarystore_state
from ..user_messages import report_send_receive_problems, TRANSLATION_CATALOG


def register_bin_fetch_data_listener(context: EventRegistryContext) -> StdRet[None]:
    """Register the store data listener."""
    return join_none_results(
        send_register_listeners(
            context,
            binarystore_state.EXTENSION_NAME,
            (
                (
                    binarystore_event.DescribeDataRequestEvent.FULL_EVENT_NAME,
                    binarystore_event.DescribeDataRequestEvent.UNIQUE_TARGET_FQN,
                ),
                (
                    binarystore_event.SendDataRequestEvent.FULL_EVENT_NAME,
                    binarystore_event.SendDataRequestEvent.UNIQUE_TARGET_FQN,
                ),
            ),
        ),
        context.register_event_parser(
            binarystore_event.DescribeDataRequestEvent.FULL_EVENT_NAME,
            binarystore_event.DescribeDataRequestEvent.parse_data,
        ),
        context.register_event_parser(
            binarystore_event.SendDataRequestEvent.FULL_EVENT_NAME,
            binarystore_event.SendDataRequestEvent.parse_data,
        ),

        context.register_target(
            binarystore_event.DescribeDataRequestEvent.FULL_EVENT_NAME,
            binarystore_event.DescribeDataRequestEvent.UNIQUE_TARGET_FQN,
            DescribeDataHandler(context),
        ),
        context.register_target(
            binarystore_event.SendDataRequestEvent.FULL_EVENT_NAME,
            binarystore_event.SendDataRequestEvent.UNIQUE_TARGET_FQN,
            SendDataHandler(context),
        ),
    )


class DescribeDataHandler(ContextEventObjectTarget[binarystore_event.DescribeDataRequestEvent]):
    """Handles the describe-data request."""

    def on_context_event(
            self, context: EventRegistryContext, source: str, target: str,
            event: binarystore_event.DescribeDataRequestEvent,
    ) -> bool:
        data = shared_state.get_data(event.store_id)
        if data:
            report_send_receive_problems('binarydata', context.send_event(
                binarystore_event.DescribeDataRequestEvent.UNIQUE_TARGET_FQN,
                event.store_id,
                binarystore_event.DataDescriptionEvent(
                    state='active',
                    mime_type=data.mime_type, sha256=data.sha256, size=data.size,
                ),
            ))
        elif shared_state.is_deleted(event.store_id):
            report_send_receive_problems('binarydata', context.send_event(
                binarystore_event.DescribeDataRequestEvent.UNIQUE_TARGET_FQN,
                event.store_id,
                binarystore_event.DataDescriptionEvent(
                    state='deleted',
                    mime_type=None, sha256=None, size=None,
                ),
            ))
        else:
            report_send_receive_problems('binarydata', context.send_event(
                binarystore_event.DescribeDataRequestEvent.UNIQUE_TARGET_FQN,
                event.store_id,
                binarystore_event.DataDescriptionEvent(
                    state='unset',
                    mime_type=None, sha256=None, size=None,
                ),
            ))

        # Continue parsing
        return False


class SendDataHandler(ContextEventObjectTarget[binarystore_event.SendDataRequestEvent]):
    """Handles the fetch data requests."""

    def on_context_event(
            self, context: EventRegistryContext, source: str, target: str,
            event: binarystore_event.SendDataRequestEvent,
    ) -> bool:
        data = shared_state.get_data(event.store_id)
        if data:
            try:
                with open(data.filename, 'rb') as f:
                    report_send_receive_problems('binarystore', context.send_binary_event_stream(
                        # Yes, the source target comes from a different event...
                        binarystore_event.SendDataRequestEvent.UNIQUE_TARGET_FQN,
                        event.store_id,
                        binarystore_event.BinaryDataEvent.FULL_EVENT_NAME,
                        data.size, convert_reader_to_raw(f),
                    ))
            except OSError as err:
                report_send_receive_problems('binarystore', StdRet.pass_exception(
                    TRANSLATION_CATALOG,
                    _('problem loading data from cache for data_id {data_id}'),
                    err,
                    data_id=event.store_id,
                ))
        # else ignore
        return False
