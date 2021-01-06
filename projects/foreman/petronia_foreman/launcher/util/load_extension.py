"""Handles events to a loader for starting an extension."""

from typing import Tuple, Sequence, Callable, Optional
import time
from petronia_common.util import StdRet, UserMessage, i18n
from petronia_common.event_stream import (
    write_object_event_to_stream,
    raw_event_id, is_raw_event_object, as_raw_event_object_data, RawEvent,
)
from .launched_channel import LaunchedInstance
from .cmd_events import extension_commands
from .stream_intercept import (
    BUBBLE_EVENT__REMOVE_HANDLER,
    BUBBLE_EVENT__KEEP_HANDLER,
    DO_NOT_BUBBLE_EVENT__KEEP_HANDLER,
    DO_NOT_BUBBLE_EVENT__REMOVE_HANDLER,
)
from ...constants import TRANSLATION_CATALOG

# So we don't need a double import
_ = i18n


def request_extension_load(
        launcher: LaunchedInstance,
        handler_id: str,
        extension_name: str, extension_version: Tuple[int, int, int],
) -> StdRet[None]:
    """Send an event to the launcher to request an extension to load."""
    return write_object_event_to_stream(
        launcher.writer,
        extension_commands.InternalLoadExtensionRequestEvent.FULL_EVENT_NAME,
        'category', handler_id,
        extension_commands.InternalLoadExtensionRequestEvent(
            name=extension_name,
            version=list(extension_version),
        ).export_data(),
    )


def parse_extension_load_event(
        raw_event: RawEvent,
) -> StdRet[Optional[extension_commands.InternalLoadExtensionSuccessEvent]]:
    """Check a raw event.  If it's a load extension failure, then an error is returned.
    If it's a success event, it's returned.  If it's some other event, None is returned."""
    event_id = raw_event_id(raw_event)
    if (
        not is_raw_event_object(raw_event)
        or event_id not in (
            extension_commands.InternalLoadExtensionFailedEvent.FULL_EVENT_NAME,
            extension_commands.InternalLoadExtensionSuccessEvent.FULL_EVENT_NAME,
        )
    ):
        # Invalid event type
        return StdRet.pass_ok(None)

    if event_id == extension_commands.InternalLoadExtensionFailedEvent.FULL_EVENT_NAME:
        # failed to load extension event.
        error_event = extension_commands.InternalLoadExtensionFailedEvent.parse_data(
            as_raw_event_object_data(raw_event),
        )
        if error_event.has_error:
            return error_event.forward()
        return StdRet.pass_errmsg(
            TRANSLATION_CATALOG,
            i18n(error_event.result.error.message),
            **{
                arg.name: arg.value
                for arg in error_event.result.error.arguments
            },
        )

    # With the "if" above, this should always be true.
    assert event_id == extension_commands.InternalLoadExtensionSuccessEvent.FULL_EVENT_NAME

    success_event = extension_commands.InternalLoadExtensionSuccessEvent.parse_data(
        as_raw_event_object_data(raw_event),
    )
    if success_event.has_error:
        return success_event.forward()
    return StdRet.pass_ok(success_event.result)


def create_intercept_extension_loaded_event_handler(
        extension_name: str,
        extension_version: Tuple[int, int, int],
        on_extension_loaded: Callable[[], None],
        on_extension_load_failed: Callable[[Sequence[UserMessage]], None],
        timeout: float,
) -> Callable[[Optional[RawEvent]], int]:
    """Part of the event parsing chain to wait for the extension to be loaded.
    When the handler finds the response or times out, then the callable returns True."""
    assert timeout > 0.0
    end_time = time.time() + timeout
    version_list = list(extension_version)

    def ret(raw_event: Optional[RawEvent]) -> int:
        # We received the event, so go ahead and process it rather than checking for the
        # timeout.
        if raw_event:
            res = parse_extension_load_event(raw_event)
            if res.has_error:
                on_extension_load_failed(res.valid_error.messages())
                return DO_NOT_BUBBLE_EVENT__REMOVE_HANDLER
            if res.value is not None:
                if (
                        res.value.name == extension_name
                        and list(res.value.version) == version_list
                ):
                    on_extension_loaded()
                    return DO_NOT_BUBBLE_EVENT__REMOVE_HANDLER
                else:
                    if end_time > time.time():
                        on_extension_load_failed([UserMessage(
                            TRANSLATION_CATALOG,
                            _('Timed out waiting for extension {name} {version} to load'),
                            name=extension_name,
                            version=extension_version,
                        )])
                        return BUBBLE_EVENT__REMOVE_HANDLER
                    return DO_NOT_BUBBLE_EVENT__KEEP_HANDLER

        if end_time > time.time():
            on_extension_load_failed([UserMessage(
                TRANSLATION_CATALOG,
                _('Timed out waiting for extension {name} {version} to load'),
                name=extension_name,
                version=extension_version,
            )])
            return BUBBLE_EVENT__REMOVE_HANDLER

        return BUBBLE_EVENT__KEEP_HANDLER

    return ret
