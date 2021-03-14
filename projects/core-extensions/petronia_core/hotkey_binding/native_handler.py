"""Handle native hotkey pressed events."""

from typing import Callable, Sequence, List, Iterable, Optional
from petronia_common.util import (
    StdRet, UserMessage, ValueHolder,
    RET_OK_NONE, EMPTY_LIST, join_none_results, i18n,
)
from petronia_ext_lib.runner import EventRegistryContext, EventObjectTarget, DecisionHandlerProxy
from petronia_ext_lib.extension_loader import send_register_listeners
from .events.ext import hotkey as native_hotkey
from .events.impl import hotkey_binding as ext_hotkey
from ..user_messages import TRANSLATION_CATALOG

# Rather than reimport...
_ = i18n


def register_native_handlers(
        context: EventRegistryContext,
        hotkey_pressed_callback: Callable[[List[str]], None],
) -> StdRet[None]:
    """Register the handlers for the native responses and events."""
    return join_none_results(
        context.register_event_parser(
            native_hotkey.HotkeyPressedEvent.FULL_EVENT_NAME,
            native_hotkey.HotkeyPressedEvent.parse_data,
        ),
        context.register_event_parser(
            native_hotkey.SetHotkeyBindingsSuccessEvent.FULL_EVENT_NAME,
            native_hotkey.SetHotkeyBindingsSuccessEvent.parse_data,
        ),
        context.register_event_parser(
            native_hotkey.SetHotkeyBindingsFailedEvent.FULL_EVENT_NAME,
            native_hotkey.SetHotkeyBindingsFailedEvent.parse_data,
        ),
        context.register_target(
            native_hotkey.HotkeyPressedEvent.FULL_EVENT_NAME,
            None,
            HotkeyPressedTarget(hotkey_pressed_callback),
        ),
        send_register_listeners(
            context,
            ext_hotkey.EXTENSION_NAME,
            (
                (
                    native_hotkey.HotkeyPressedEvent.FULL_EVENT_NAME,
                    None,
                ),
                (
                    native_hotkey.SetHotkeyBindingsSuccessEvent.FULL_EVENT_NAME,
                    SET_BINDING_TARGET_ID,
                ),
                (
                    native_hotkey.SetHotkeyBindingsFailedEvent.FULL_EVENT_NAME,
                    SET_BINDING_TARGET_ID,
                ),
            ),
        ),
    )


REQUEST_SUCCEEDED = 0
REQUEST_FAILED = 1
REQUEST_TIMED_OUT = 2

REQUEST_TIMEOUT_SECONDS = 10.0

_MIN_REQUEST = -999999
_MAX_REQUEST = 9999999
_SET_HOTKEY_BINDINGS_REQUEST = [_MIN_REQUEST]

SET_BINDING_TARGET_ID = ext_hotkey.EXTENSION_NAME + ':native-hotkey-binding'


class HotkeyPressedTarget(EventObjectTarget[native_hotkey.HotkeyPressedEvent]):
    """Handler for the pressed hotkey event."""
    __slots__ = ('_callback',)

    def __init__(self, callback: Callable[[List[str]], None]) -> None:
        self._callback = callback

    def on_event(
            self, _source: str, _target: str, event: native_hotkey.HotkeyPressedEvent,
    ) -> bool:
        self._callback(event.hotkey.keys)
        return False


def send_set_hotkey_bindings(
        context: EventRegistryContext,
        sequence_type: str,
        master_sequence: Sequence[str],
        bound_keys: Iterable[Sequence[str]],
        on_complete: Callable[[int, Sequence[UserMessage]], None],
) -> StdRet[None]:
    """Send a request to bind hotkeys.  This will listen for binding success
    or failure, and perform the proper notifications back."""

    source_request = _SET_HOTKEY_BINDINGS_REQUEST[0]
    _SET_HOTKEY_BINDINGS_REQUEST[0] += 1
    if _SET_HOTKEY_BINDINGS_REQUEST[0] > _MAX_REQUEST:
        _SET_HOTKEY_BINDINGS_REQUEST[0] = _MIN_REQUEST

    def on_success(
            _source: str, _target: str, event: native_hotkey.SetHotkeyBindingsSuccessEvent,
    ) -> bool:
        if event.request == source_request:
            # Handle the request.
            on_complete(REQUEST_SUCCEEDED, [])
            # Not active anymore.
            return True
        return False

    def on_failure(
            _source: str, _target: str, event: native_hotkey.SetHotkeyBindingsFailedEvent,
    ) -> bool:
        if event.request == source_request:
            # Handle the request.
            on_complete(REQUEST_FAILED, [
                *master_problems(event.master_problem),
                *bound_problems(event.bound_problems),
            ])
            # Not active anymore.
            return True
        return False

    def cancelled() -> None:
        on_complete(REQUEST_TIMED_OUT, [UserMessage(
            TRANSLATION_CATALOG,
            _('request to native extension to bind new keys timed out after {timeout} seconds'),
            timeout=REQUEST_TIMEOUT_SECONDS,
        )])

    # Register the targets then send the event.

    active_state = ValueHolder(True)
    context.register_target(
        native_hotkey.SetHotkeyBindingsSuccessEvent.FULL_EVENT_NAME,
        SET_BINDING_TARGET_ID,
        DecisionHandlerProxy(on_success, active_state, cancelled),
        timeout=REQUEST_TIMEOUT_SECONDS,
    )
    context.register_target(
        native_hotkey.SetHotkeyBindingsFailedEvent.FULL_EVENT_NAME,
        SET_BINDING_TARGET_ID,
        DecisionHandlerProxy(on_failure, active_state, cancelled),
        timeout=REQUEST_TIMEOUT_SECONDS,
    )

    context.send_event(
        SET_BINDING_TARGET_ID,
        native_hotkey.SetHotkeyBindingsEvent.UNIQUE_TARGET_FQN,
        native_hotkey.SetHotkeyBindingsEvent(
            source_request,
            native_hotkey.MasterHotkeySequence(sequence_type, list(master_sequence)),
            [
                native_hotkey.BoundHotkey(list(seq))
                for seq in bound_keys
            ],
        ),
    )

    return RET_OK_NONE


def bound_problems(problems: Optional[List[native_hotkey.BoundHotkeyProblem]]) -> List[UserMessage]:
    """Convert bound hotkey problems into user messages."""
    if not problems:
        return EMPTY_LIST
    ret: List[UserMessage] = []
    for problem in problems:
        ret.extend(error_to_user_message(problem.error))
    return ret


def master_problems(
        problem: Optional[native_hotkey.MasterHotkeySequenceProblem],
) -> List[UserMessage]:
    """Convert a master hotkey sequence problem into a list of messages."""
    if not problem:
        return EMPTY_LIST
    return error_to_user_message(problem.error)


def error_to_user_message(err: native_hotkey.Error) -> List[UserMessage]:
    """Convert a native hotkey error structure into a user message."""
    return [
        UserMessage(
            msg.catalog,
            i18n(msg.message),
            **{
                arg.name: arg.value.value
                for arg in (msg.arguments or EMPTY_LIST)
            },
        )
        for msg in err.messages
    ]
