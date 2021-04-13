"""
Very common patterns involving initialization.
"""

from typing import Dict, Callable, Any
import json
from petronia_common.util import StdRet, T, ValueHolder, RET_OK_NONE, join_none_results
from . import send, listen
from ..runner.registry import (
    EventRegistryContext, ContextEventObjectTarget, EventObject, EventObjectTarget,
    EventObjectParser,
)
from ..events import timer as timer_event
from ..events import datastore as datastore_event


def send_initial_state(
        context: EventRegistryContext,
        data_id: str,
        data: send.StateObject,
        on_sent: Callable[[], None],
        result_handler: Callable[[StdRet[None]], None],
) -> StdRet[None]:
    """Send out the initial state.  Due to extension loading order, the datastore extension
    may not be fully alive yet."""
    res = listen.register_listening_to_datastore(context, data_id, data_id)
    if res.has_error:
        return res.forward()

    # Errors here are ignored, so fake out the res to not falsely report ignored...
    res_ignored = listen.register_datastore_update_parsers(context)
    res_ignored.error_messages()

    found_value = ValueHolder(False)
    transmit = TransmitUntilTarget(
        context,
        found_value, data_id, datastore_event.StoreDataEvent.UNIQUE_TARGET_FQN,
        datastore_event.StoreDataEvent(json.dumps(data.export_data())),
        result_handler,
    )

    def ignored_on_sent(_val: StdRet[Any]) -> None:
        on_sent()

    return join_none_results(
        context.register_target(
            datastore_event.DataUpdateEvent.FULL_EVENT_NAME,
            data_id,
            ReceiveUpdateTarget(data_id, found_value, ignored_on_sent, lambda x: RET_OK_NONE),
        ),
        context.register_target(
            timer_event.HeartbeatEvent.FULL_EVENT_NAME,
            timer_event.HeartbeatEvent.UNIQUE_TARGET_FQN,
            transmit,
        ),

        # Send the initial request.
        context.send_event(
            transmit.source_id, transmit.target_id, transmit.event,
        ),
    )


def wait_for_state(
        context: EventRegistryContext,
        source_id: str,
        data_id: str,
        parser: Callable[[Dict[str, Any]], StdRet[T]],
        callback: Callable[[StdRet[T]], None],
) -> StdRet[None]:
    """
    Wait for another extension to start.  This is triggered by the other extension sending out
    a set-state, but that could be sent before the second extension
    is waiting for it.  Additionally, there's a situation where the datastore extension could be
    loaded after both extensions.  Because of that, this sends out at intervals "send state"
    requests.

    The state listener will stop listening when the first state is received.
    """
    res = listen.register_listening_to_datastore(context, data_id, data_id)
    if res.has_error:
        return res.forward()

    # Errors here are ignored, so fake out the res to not falsely report ignored...
    res_ignored = listen.register_datastore_update_parsers(context)
    res_ignored.error_messages()

    def on_failure(result: StdRet[None]) -> None:
        if result.has_error:
            callback(result.forward())

    found_value = ValueHolder(False)
    transmit = TransmitUntilTarget(
        context,
        found_value, source_id, datastore_event.SendStateEvent.UNIQUE_TARGET_FQN,
        datastore_event.SendStateEvent(data_id),
        on_failure,
    )

    return join_none_results(
        context.register_target(
            datastore_event.DataUpdateEvent.FULL_EVENT_NAME,
            data_id,
            ReceiveUpdateTarget(data_id, found_value, callback, parser),
        ),
        context.register_target(
            timer_event.HeartbeatEvent.FULL_EVENT_NAME,
            timer_event.HeartbeatEvent.UNIQUE_TARGET_FQN,
            transmit,
        ),

        # Send the initial request.
        context.send_event(
            transmit.source_id, transmit.target_id, transmit.event,
        ),
    )


class TransmitUntilTarget(ContextEventObjectTarget[timer_event.HeartbeatEvent]):
    """Retransmit an event at every heartbeat until the value is True."""

    __slots__ = ('value', 'source_id', 'target_id', 'event', 'result_handler')

    def __init__(
            self, context: EventRegistryContext, value: ValueHolder[bool],
            source_id: str, target_id: str, event: EventObject,
            result_handler: Callable[[StdRet[None]], None],
    ) -> None:
        ContextEventObjectTarget.__init__(self, context)
        self.value = value
        self.source_id = source_id
        self.target_id = target_id
        self.event = event
        self.result_handler = result_handler

    def on_context_event(
            self, context: EventRegistryContext, source: str, target: str,
            event: timer_event.HeartbeatEvent,
    ) -> bool:
        if self.value.value:
            return True
        self.result_handler(context.send_event(
            self.source_id, self.target_id, self.event,
        ))
        return False


class ReceiveUpdateTarget(EventObjectTarget[datastore_event.DataUpdateEvent]):
    """Listen to updates."""
    __slots__ = ('target_id', 'found_holder', 'on_receive', 'parser')

    def __init__(
            self, target_id: str, found_holder: ValueHolder[bool],
            on_sent: Callable[[StdRet[T]], None],
            parser: Callable[[Dict[str, Any]], StdRet[T]],
    ) -> None:
        self.target_id = target_id
        self.found_holder = found_holder
        self.on_sent = on_sent
        self.parser = EventObjectParser(parser)

    def on_event(self, source: str, target: str, event: datastore_event.DataUpdateEvent) -> bool:
        if target == self.target_id:
            self.found_holder.value = True
            self.on_sent(listen.get_event_data_value(event, self.parser))
            return True
        return self.found_holder.value
