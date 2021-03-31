"""Handles events that come from the native window extension."""

from petronia_common.util import StdRet, join_none_results
from petronia_ext_lib.extension_loader import send_register_listeners
from petronia_ext_lib.runner import EventRegistryContext, ContextEventObjectTarget
from .state import petronia_portal as portal_state
from .events import window as window_event


def setup(context: EventRegistryContext) -> StdRet[None]:
    """Setup the handler."""
    return join_none_results(
        send_register_listeners(
            context,
            portal_state.EXTENSION_NAME,
            (
                (
                    window_event.WindowCreatedEvent.FULL_EVENT_NAME,
                    window_event.WindowCreatedEvent.UNIQUE_TARGET_FQN,
                ),
                (
                    window_event.WindowDestroyedEvent.FULL_EVENT_NAME,
                    window_event.WindowDestroyedEvent.UNIQUE_TARGET_FQN,
                ),
                (
                    window_event.WindowFlashedEvent.FULL_EVENT_NAME,
                    window_event.WindowFlashedEvent.UNIQUE_TARGET_FQN,
                ),
                (
                    window_event.WindowFocusedEvent.FULL_EVENT_NAME,
                    window_event.WindowFocusedEvent.UNIQUE_TARGET_FQN,
                ),
            ),
        ),
        context.register_event_parser(
            window_event.WindowCreatedEvent.FULL_EVENT_NAME,
            window_event.WindowCreatedEvent.parse_data,
        ),
        context.register_target(
            window_event.WindowCreatedEvent.FULL_EVENT_NAME,
            window_event.WindowCreatedEvent.UNIQUE_TARGET_FQN,
            WindowCreatedHandler(context),
        ),
    )


class WindowCreatedHandler(ContextEventObjectTarget[window_event.WindowCreatedEvent]):
    """Handle window created events."""

    def on_context_event(
            self, context: EventRegistryContext,
            source: str, target: str, event: window_event.WindowCreatedEvent,
    ) -> bool:
        pass


class WindowDestroyedHandler(ContextEventObjectTarget[window_event.WindowDestroyedEvent]):
    """Handle window destroyed events."""

    def on_context_event(
            self, context: EventRegistryContext,
            source: str, target: str, event: window_event.WindowDestroyedEvent,
    ) -> bool:
        pass


class WindowFlashedHandler(ContextEventObjectTarget[window_event.WindowFlashedEvent]):
    """Handle window flashed events."""

    def on_context_event(
            self, context: EventRegistryContext,
            source: str, target: str, event: window_event.WindowFlashedEvent,
    ) -> bool:
        pass


class WindowFocusedHandler(ContextEventObjectTarget[window_event.WindowFocusedEvent]):
    """Handle window focus events."""

    def on_context_event(
            self, context: EventRegistryContext,
            source: str, target: str, event: window_event.WindowFocusedEvent,
    ) -> bool:
        pass
