"""Handle hotkey-binding events."""

from typing import List, Callable
from petronia_common.util import StdRet, join_none_results
from petronia_ext_lib.runner import EventRegistryContext
from petronia_ext_lib.extension_loader import send_register_listeners
from .events.impl import hotkey_binding as hotkey_events
from .state import hotkey_binding as hotkey_state
from .shared_state import get_bound_event
from ..user_messages import report_send_receive_problems


def register_bind_handlers(
        context: EventRegistryContext,
) -> StdRet[None]:
    """Register the handlers for the key binding requests."""
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

        # TODO add in listeners.
    )


def create_on_hotkey_pressed_callback(
        context: EventRegistryContext,
) -> Callable[[List[str]], None]:
    """Callback when native layer announces a hotkey binding pressed."""

    def on_hotkey_pressed(bound_key_sequence: List[str]) -> None:
        event = get_bound_event(bound_key_sequence)
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
    return context.send_event(
        hotkey_events.HotkeyFiredEvent.UNIQUE_TARGET_FQN,
        event.target_id,
        hotkey_events.HotkeyFiredEvent(event),
    )
