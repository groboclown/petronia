"""Handle hotkey-binding events."""

from typing import List, Sequence, Callable
from petronia_common.util import StdRet, join_none_results, join_errors, UserMessage
from petronia_ext_lib.runner import EventRegistryContext, ContextEventObjectTarget
from petronia_ext_lib.logging import send_system_error
from petronia_ext_lib.standard import error
from petronia_ext_lib.extension_loader import send_register_listeners
from . import shared_state, store_handler, native_handler
from .events.impl import hotkey_binding as hotkey_events
from .state import hotkey_binding as hotkey_state
from ..user_messages import report_send_receive_problems


def register_bind_handlers(
        context: EventRegistryContext,
) -> StdRet[None]:
    """Register the handlers for the key binding requests."""

    # Improvement:
    # Until the native hotkey config is posted to the datastore, we can't assume that
    # the extension is ready to handle requests.  We need a global registration handler;
    # right now, that's done by the

    return join_none_results(
        send_register_listeners(
            context,
            hotkey_state.EXTENSION_NAME,
            [
                (
                    hotkey_events.ExtensionEventRegisterEvent.FULL_EVENT_NAME,
                    hotkey_events.ExtensionEventRegisterEvent.UNIQUE_TARGET_FQN,
                ),
                (
                    hotkey_events.SetMasterSequenceRequestEvent.FULL_EVENT_NAME,
                    hotkey_events.SetMasterSequenceRequestEvent.UNIQUE_TARGET_FQN,
                ),
                (
                    hotkey_events.BoundKeyRegisterEvent.FULL_EVENT_NAME,
                    hotkey_events.BoundKeyRegisterEvent.UNIQUE_TARGET_FQN,
                ),
                (
                    hotkey_events.BoundKeyRemoveEvent.FULL_EVENT_NAME,
                    hotkey_events.BoundKeyRemoveEvent.UNIQUE_TARGET_FQN,
                ),
            ],
        ),
        context.register_event_parser(
            hotkey_events.ExtensionEventRegisterEvent.FULL_EVENT_NAME,
            hotkey_events.ExtensionEventRegisterEvent.parse_data,
        ),
        context.register_event_parser(
            hotkey_events.SetMasterSequenceRequestEvent.FULL_EVENT_NAME,
            hotkey_events.SetMasterSequenceRequestEvent.parse_data,
        ),
        context.register_event_parser(
            hotkey_events.BoundKeyRegisterEvent.FULL_EVENT_NAME,
            hotkey_events.BoundKeyRegisterEvent.parse_data,
        ),
        context.register_event_parser(
            hotkey_events.BoundKeyRemoveEvent.FULL_EVENT_NAME,
            hotkey_events.BoundKeyRemoveEvent.parse_data,
        ),

        context.register_target(
            hotkey_events.ExtensionEventRegisterEvent.FULL_EVENT_NAME,
            hotkey_events.ExtensionEventRegisterEvent.UNIQUE_TARGET_FQN,
            ExtensionEventRegisterEventTarget(context),
        ),
        context.register_target(
            hotkey_events.SetMasterSequenceRequestEvent.FULL_EVENT_NAME,
            hotkey_events.SetMasterSequenceRequestEvent.UNIQUE_TARGET_FQN,
            SetMasterSequenceRequestEventTarget(context),
        ),
        context.register_target(
            hotkey_events.BoundKeyRegisterEvent.FULL_EVENT_NAME,
            hotkey_events.BoundKeyRegisterEvent.UNIQUE_TARGET_FQN,
            BoundKeyRegisterEventTarget(context),
        ),
        context.register_target(
            hotkey_events.BoundKeyRemoveEvent.FULL_EVENT_NAME,
            hotkey_events.BoundKeyRemoveEvent.UNIQUE_TARGET_FQN,
            BoundKeyRemoveEventTarget(context),
        ),
    )


def create_on_hotkey_pressed_callback(
        context: EventRegistryContext,
) -> Callable[[List[str]], None]:
    """Callback when native layer announces a hotkey binding pressed."""

    def on_hotkey_pressed(bound_key_sequence: List[str]) -> None:
        event = shared_state.get_bound_event(bound_key_sequence)
        if event:
            report_send_receive_problems(
                'hotkey-binding',
                send_hotkey_fired_event(context, event),
            )

    return on_hotkey_pressed


def send_hotkey_fired_event(
        context: EventRegistryContext,
        event: hotkey_events.BoundEvent,
) -> StdRet[None]:
    """Send a hotkey fired event."""
    print(f'[HOTKEY] translated hotkey to {repr(event.export_data())}')
    return context.send_event(
        hotkey_events.HotkeyFiredEvent.UNIQUE_TARGET_FQN,
        event.target_id,
        hotkey_events.HotkeyFiredEvent(event),
    )


class ExtensionEventRegisterEventTarget(
    ContextEventObjectTarget[hotkey_events.ExtensionEventRegisterEvent]
):
    """Handle ExtensionEventRegisterEvent events."""

    def on_context_event(
            self, context: EventRegistryContext, source: str, target: str,
            event: hotkey_events.ExtensionEventRegisterEvent,
    ) -> bool:
        shared_state.set_extension_event(hotkey_events.Events(
            event.name,
            event.description,
            event.target_id,

            # May want to copy each parameter...
            list(event.parameters),
        ))
        report_send_receive_problems(
            'hotkey-binding',
            store_handler.send_extension_events_state(context),
        )
        return False


class SetMasterSequenceRequestEventTarget(
    ContextEventObjectTarget[hotkey_events.SetMasterSequenceRequestEvent]
):
    """Handle SetMasterSequenceRequestEvent events.

    This needs to send the request to update the native bindings, and if that's successful,
    update the local state."""
    __slots__ = ()

    def on_context_event(
            self, context: EventRegistryContext, source: str, target: str,
            event: hotkey_events.SetMasterSequenceRequestEvent,
    ) -> bool:

        def on_complete(status: int, errors: Sequence[UserMessage]) -> None:
            if status == native_handler.REQUEST_SUCCEEDED:
                shared_state.set_master_sequence(event.sequence_type, event.keys)
                report_send_receive_problems(
                    'hotkey-binding', store_handler.send_bound_keys_state(context),
                )
                report_send_receive_problems(
                    'hotkey-binding', store_handler.send_configuration_state(context),
                )
            else:
                report_send_receive_problems('hotkey-binding', send_system_error(
                    context, hotkey_state.EXTENSION_NAME,
                    join_errors(*errors), 'hotkey-bind-timeout',
                    [error.INTERNAL_ERROR_CATEGORY],
                ))

        report_send_receive_problems('hotkey-binding', native_handler.send_set_hotkey_bindings(
            context, event.sequence_type, event.keys, shared_state.list_bound_keys(),
            on_complete,
        ))
        return False


class BoundKeyRegisterEventTarget(
    ContextEventObjectTarget[hotkey_events.BoundKeyRegisterEvent]
):
    """Handle BoundKeyRegisterEvent events

    This needs to send the request to update the native bindings, and if that's successful,
    update the local state."""
    __slots__ = ()

    def on_context_event(
            self, context: EventRegistryContext, source: str, target: str,
            event: hotkey_events.BoundKeyRegisterEvent,
    ) -> bool:

        def on_complete(status: int, errors: Sequence[UserMessage]) -> None:
            if status == native_handler.REQUEST_SUCCEEDED:
                shared_state.set_bound_key(event.keys, event.comment, event.event)
                report_send_receive_problems(
                    'hotkey-binding', store_handler.send_bound_keys_state(context),
                )
                report_send_receive_problems(
                    'hotkey-binding', store_handler.send_configuration_state(context),
                )
            else:
                # This may not be a timeout, but could be a valid error.
                report_send_receive_problems('hotkey-binding', send_system_error(
                    context, hotkey_state.EXTENSION_NAME,
                    join_errors(*errors), 'hotkey-bind-timeout',
                    [error.INTERNAL_ERROR_CATEGORY],
                ))

        master = shared_state.get_master_sequence()
        new_bound_keys = set(shared_state.list_bound_keys())
        new_bound_keys.add(tuple(event.keys))

        report_send_receive_problems('hotkey-binding', native_handler.send_set_hotkey_bindings(
            context, master.sequence_type, master.sequence, new_bound_keys,
            on_complete,
        ))
        return False


class BoundKeyRemoveEventTarget(
    ContextEventObjectTarget[hotkey_events.BoundKeyRemoveEvent],
):
    """Handle BoundKeyRemoveEvent events

    This needs to send the request to update the native bindings, and if that's successful,
    update the local state."""

    __slots__ = ()

    def on_context_event(
            self, context: EventRegistryContext, source: str, target: str,
            event: hotkey_events.BoundKeyRemoveEvent,
    ) -> bool:
        if shared_state.get_bound_event(event.keys) is None:
            # No such registered key.  No need to go through all the event processing.
            return False

        def on_complete(status: int, errors: Sequence[UserMessage]) -> None:
            if status == native_handler.REQUEST_SUCCEEDED:
                # Double check, in case another of these events came in before this completed.
                if shared_state.remove_bound_key(event.keys):
                    report_send_receive_problems(
                        'hotkey-binding', store_handler.send_bound_keys_state(context),
                    )
                    report_send_receive_problems(
                        'hotkey-binding', store_handler.send_configuration_state(context),
                    )
            else:
                report_send_receive_problems('hotkey-binding', send_system_error(
                    context, hotkey_state.EXTENSION_NAME,
                    join_errors(*errors), 'hotkey-bind-timeout',
                    [error.INTERNAL_ERROR_CATEGORY],
                ))

        master = shared_state.get_master_sequence()
        new_bound_keys = set(shared_state.list_bound_keys())
        new_bound_keys.remove(tuple(event.keys))

        report_send_receive_problems('hotkey-binding', native_handler.send_set_hotkey_bindings(
            context, master.sequence_type, master.sequence, new_bound_keys,
            on_complete,
        ))
        return False
