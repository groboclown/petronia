"""Handle event requests."""

from typing import Optional
from petronia_common.event_stream import RawBinaryReader
from petronia_common.util import StdRet, join_none_results, UserMessage
from petronia_common.util import i18n as _
from petronia_ext_lib.extension_loader import send_register_listeners
from petronia_ext_lib.runner import (
    EventRegistryContext, ContextEventObjectTarget, EventBinaryTarget,
)
from petronia_ext_lib.standard.localizable_message import create_localizable_message
from . import shared_state
from .events.impl import binarystore as binarystore_event
from .state import binarystore as binarystore_state
from ..user_messages import report_send_receive_problems, TRANSLATION_CATALOG


def register_bin_store_data_listener(context: EventRegistryContext) -> StdRet[None]:
    """Register the store data listener."""
    return join_none_results(
        send_register_listeners(
            context,
            binarystore_state.EXTENSION_NAME,
            (
                (binarystore_event.StoreDataRequestEvent.FULL_EVENT_NAME, None),
                (binarystore_event.StoreDataDataEvent.FULL_EVENT_NAME, None),
            ),
        ),

        context.register_event_parser(
            binarystore_event.StoreDataRequestEvent.FULL_EVENT_NAME,
            binarystore_event.StoreDataRequestEvent.parse_data,
        ),
        context.register_target(
            binarystore_event.StoreDataRequestEvent.FULL_EVENT_NAME,
            binarystore_event.StoreDataRequestEvent.UNIQUE_TARGET_FQN,
            StoreDataRequestHandler(context),
        ),

        # No parser for binary events.
        context.register_binary_target(
            binarystore_event.StoreDataDataEvent.FULL_EVENT_NAME,
            binarystore_event.StoreDataDataEvent.UNIQUE_TARGET_FQN,
            StoreDataHandler(context),
        ),
    )


class StoreDataRequestHandler(ContextEventObjectTarget[binarystore_event.StoreDataRequestEvent]):
    """Handles the prepare for store data requests."""

    def on_context_event(
            self, context: EventRegistryContext, source: str, target: str,
            event: binarystore_event.StoreDataRequestEvent,
    ) -> bool:
        if event.mime_type not in shared_state.VALID_MIME_TYPES:
            report_send_receive_problems(
                'binarystore',
                context.send_event(
                    binarystore_event.StoreDataRequestEvent.UNIQUE_TARGET_FQN,
                    source,
                    binarystore_event.StoreDataRefusedEvent(
                        reason=create_localizable_message(
                            binarystore_event.LocalizableMessage,
                            binarystore_event.MessageArgument,
                            binarystore_event.MessageArgumentValue,
                            UserMessage(
                                TRANSLATION_CATALOG,
                                _('unsupported mime type "{mime_type}" for data_id {data_id}'),
                                mime_type=event.mime_type,
                                data_id=source,
                            ),
                        ),
                    ),
                ),
            )
        pending = shared_state.PendingStoreData(mime_type=event.mime_type)
        res = shared_state.add_pending(source, pending)
        if res is not None:
            report_send_receive_problems(
                'binarystore',
                context.send_event(
                    binarystore_event.StoreDataRequestEvent.UNIQUE_TARGET_FQN,
                    source,
                    binarystore_event.StoreDataRefusedEvent(
                        reason=create_localizable_message(
                            binarystore_event.LocalizableMessage,
                            binarystore_event.MessageArgument,
                            binarystore_event.MessageArgumentValue,
                            UserMessage(
                                TRANSLATION_CATALOG,
                                _('cannot store data_id {data_id}, it is already in state {state}'),
                                state=res,
                                data_id=source,
                            ),
                        ),
                    ),
                ),
            )
            return False
        # print(f"[DATASTORE] stored data for {source}")
        report_send_receive_problems('datastore', context.send_event(
            binarystore_event.StoreDataRequestEvent.UNIQUE_TARGET_FQN,
            source,
            binarystore_event.StoreDataAllowedEvent(),
        ))
        return False


class StoreDataHandler(EventBinaryTarget):
    """Handle the data storage request."""
    __slots__ = ('context',)

    def __init__(self, context: EventRegistryContext) -> None:
        self.context: Optional[EventRegistryContext] = context

    def on_close(self) -> None:
        self.context = None

    def on_event(self, source: str, target: str, size: int, reader: RawBinaryReader) -> bool:
        if self.context is None:
            # Stop parsing
            return True

        res = shared_state.store_binary_data(source, size, reader)
        if res.has_error:
            # ... not the right kind of reporting mechanism.
            report_send_receive_problems('binarystore', res)
            report_send_receive_problems('binarystore', self.context.send_event(
                binarystore_event.StoreDataRequestEvent.UNIQUE_TARGET_FQN,
                source,
                binarystore_event.DataDescriptionEvent(
                    state=shared_state.is_deleted(source) and 'deleted' or 'unset',
                    mime_type=None, sha256=None, size=None,
                ),
            ))
        elif res.value is None:
            report_send_receive_problems(
                'binarystore',
                StdRet.pass_errmsg(
                    TRANSLATION_CATALOG,
                    _('bad api usage: no valid pending storage request for data_id {data_id}'),
                    data_id=source,
                )
            )
            report_send_receive_problems('binarystore', self.context.send_event(
                binarystore_event.StoreDataRequestEvent.UNIQUE_TARGET_FQN,
                source,
                binarystore_event.DataDescriptionEvent(
                    state=shared_state.is_deleted(source) and 'deleted' or 'unset',
                    mime_type=None, sha256=None, size=None,
                ),
            ))
        else:
            assert res.result is not None
            report_send_receive_problems('binarystore', self.context.send_event(
                binarystore_event.StoreDataRequestEvent.UNIQUE_TARGET_FQN,
                source,
                binarystore_event.DataDescriptionEvent(
                    state='active',
                    mime_type=res.result.mime_type,
                    sha256=res.result.sha256,
                    size=res.result.size,
                ),
            ))
        # Continue listening
        return False
