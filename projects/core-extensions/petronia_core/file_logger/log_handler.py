"""Handle event requests."""

from petronia_common.util import StdRet, join_none_results
from petronia_ext_lib.runner import EventRegistryContext, EventObjectTarget
from petronia_ext_lib.events import logging
from petronia_ext_lib.extension_loader import send_register_listeners
from . import shared_state
from .state import file_logger


def register_log_listener(
        context: EventRegistryContext,
) -> StdRet[None]:
    """Register the listeners for the logging events."""
    return join_none_results(
        send_register_listeners(
            context, file_logger.EXTENSION_NAME,
            (
                (
                    logging.UserErrorEvent.FULL_EVENT_NAME,
                    logging.UserErrorEvent.UNIQUE_TARGET_FQN,
                ),
                (
                    logging.SystemErrorEvent.FULL_EVENT_NAME,
                    logging.SystemErrorEvent.UNIQUE_TARGET_FQN,
                ),
                (
                    logging.LogEvent.FULL_EVENT_NAME,
                    logging.LogEvent.UNIQUE_TARGET_FQN,
                ),
            ),
        ),

        context.register_event_parser(
            logging.UserErrorEvent.FULL_EVENT_NAME,
            logging.UserErrorEvent.parse_data,
        ),
        context.register_target(
            logging.UserErrorEvent.FULL_EVENT_NAME,
            # using the simple context, so no exact target ID used.
            None,
            # logging.UserErrorEvent.UNIQUE_TARGET_FQN,
            UserMessageTarget(),
        ),

        context.register_event_parser(
            logging.SystemErrorEvent.FULL_EVENT_NAME,
            logging.SystemErrorEvent.parse_data,
        ),
        context.register_target(
            logging.SystemErrorEvent.FULL_EVENT_NAME,
            # using the simple context, so no exact target ID used.
            None,
            # logging.SystemErrorEvent.UNIQUE_TARGET_FQN,
            SystemMessageTarget(),
        ),

        context.register_event_parser(
            logging.LogEvent.FULL_EVENT_NAME,
            logging.LogEvent.parse_data,
        ),
        context.register_target(
            logging.LogEvent.FULL_EVENT_NAME,
            # using the simple context, so no exact target ID used.
            None,
            # logging.LogEvent.UNIQUE_TARGET_FQN,
            LogTarget(),
        ),
    )


class UserMessageTarget(EventObjectTarget[logging.UserErrorEvent]):
    """Handles the User error events."""
    def on_event(self, source: str, target: str, event: logging.UserErrorEvent) -> bool:
        shared_state.write_error(
            source,
            shared_state.MESSAGE_TYPE_USER,
            event.user_error,
        )
        return False


class SystemMessageTarget(EventObjectTarget[logging.SystemErrorEvent]):
    """Handles the system error events."""
    def on_event(self, source: str, target: str, event: logging.SystemErrorEvent) -> bool:
        shared_state.write_error(
            source,
            shared_state.MESSAGE_TYPE_SYSTEM,
            event.error,
        )
        return False


class LogTarget(EventObjectTarget[logging.LogEvent]):
    """Handles the log events."""
    def on_event(self, source: str, target: str, event: logging.LogEvent) -> bool:
        shared_state.write_messages(
            source,
            event.scope,
            event.messages,
        )
        return False
