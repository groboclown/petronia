"""
Very common patterns involving initialization.
"""

from typing import Dict, Callable, Optional, Any
from petronia_common.util import StdRet, T, ValueHolder, join_none_results
from . import listen
from ..runner.registry import (
    EventRegistryContext, ContextEventObjectTarget, EventObject,
    EventObjectParser,
)
from ..extension_loader import send_register_listeners
from ..events import timer as timer_event
from ..events import datastore as datastore_event


def initialize_cached_state(
        context: EventRegistryContext,
        source_id: str,
        data_id: str,
        cache: listen.CachedInstance[T],
) -> StdRet[None]:
    """Listen for changes to the data object.  It will send out a 'send update' message every
    heartbeat until it is initially loaded."""

    def on_failure(_result: StdRet[None]) -> None:
        # WRONG
        pass

    found_value = ValueHolder(False)
    transmit = TransmitUntilTarget(
        context,
        found_value, source_id, datastore_event.SendStateEvent.UNIQUE_TARGET_FQN,
        datastore_event.SendStateEvent(data_id),
        on_failure,
    )

    original_callback = cache.callback

    def first_callback(value: Optional[T]) -> None:
        print(f'[] Received {data_id} in {source_id}')
        found_value.value = True
        cache.callback = original_callback
        if original_callback:
            original_callback(value)

    cache.callback = first_callback

    return join_none_results(
        context.register_event_parser(
            timer_event.HeartbeatEvent.FULL_EVENT_NAME,
            timer_event.HeartbeatEvent.parse_data,
        ),
        listen.register_datastore_target_listener(context, data_id, cache),
        send_register_listeners(
            context, source_id[:source_id.index(':')],
            (
                (
                    timer_event.HeartbeatEvent.FULL_EVENT_NAME,
                    timer_event.HeartbeatEvent.UNIQUE_TARGET_FQN,
                ),
            ),
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
        callback: Callable[[EventRegistryContext, StdRet[T]], None],
) -> StdRet[None]:
    """
    Wait for a state to load.  This will transmit a "send state" message every
    heartbeat until the state is loaded.  This is necessary in case the send message
    is handled before the register listener completes.

    If the data is deleted, this will keep listening.
    """
    res = listen.register_listening_to_datastore(context, data_id, data_id)
    if res.has_error:
        return res.forward()
    res = send_register_listeners(
        context, source_id,
        (
            (
                timer_event.HeartbeatEvent.FULL_EVENT_NAME,
                timer_event.HeartbeatEvent.UNIQUE_TARGET_FQN,
            ),
        ),
    )
    if res.has_error:
        return res.forward()

    def on_failure(result: StdRet[None]) -> None:
        if result.has_error:
            callback(context, result.forward())

    found_value = ValueHolder(False)
    transmit = TransmitUntilTarget(
        context,
        found_value, source_id, datastore_event.SendStateEvent.UNIQUE_TARGET_FQN,
        datastore_event.SendStateEvent(data_id),
        on_failure,
    )

    return join_none_results(
        listen.register_datastore_update_parsers(context),
        context.register_event_parser(
            timer_event.HeartbeatEvent.FULL_EVENT_NAME,
            timer_event.HeartbeatEvent.parse_data,
        ),
        context.register_target(
            datastore_event.DataUpdateEvent.FULL_EVENT_NAME,
            data_id,
            ReceiveUpdateTarget(context, data_id, found_value, callback, parser),
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
            print(f'-- heartbeat complete for {self.target_id} <- {self.source_id}')
            return True
        print(f'-- heartbeat with no resolution.  Sending {self.event.fully_qualified_event_name}')
        self.result_handler(context.send_event(
            self.source_id, self.target_id, self.event,
        ))
        return False


class ReceiveUpdateTarget(ContextEventObjectTarget[datastore_event.DataUpdateEvent]):
    """Listen to updates."""
    __slots__ = ('target_id', 'found_holder', 'on_receive', 'parser')

    def __init__(
            self, context: EventRegistryContext, target_id: str, found_holder: ValueHolder[bool],
            on_receive: Callable[[EventRegistryContext, StdRet[T]], None],
            parser: Callable[[Dict[str, Any]], StdRet[T]],
    ) -> None:
        ContextEventObjectTarget.__init__(self, context)
        self.target_id = target_id
        self.found_holder = found_holder
        self.on_receive = on_receive
        self.parser = EventObjectParser(parser)

    def on_context_event(
            self, context: EventRegistryContext, source: str, target: str,
            event: datastore_event.DataUpdateEvent,
    ) -> bool:
        if target == self.target_id:
            self.found_holder.value = True
            self.on_receive(context, listen.get_event_data_value(event, self.parser))
            return True
        return self.found_holder.value
