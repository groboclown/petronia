"""Hotkey listener handlers."""

from typing import Sequence, List, Dict, Optional
from petronia_common.util import StdRet, RET_OK_NONE, not_none
from petronia_ext_lib import runner
from petronia_ext_lib import datastore
from petronia_ext_lib.standard.error import create_error_data, INVALID_USER_ACTION_ERROR_CATEGORY
from ..events.impl import hotkey
from ..user_messages import report_send_receive_problems


class BoundKeyProblems:
    """A problem binding hotkeys.

    The master_problem reflects errors with the master sequence.  The sequence_problems
    is a collection of each sequence and its problem.  Only sequences with problems need
    to be included in the dictionary.
    """
    __slots__ = ('master_problem', 'sequence_problems')

    def __init__(self) -> None:
        self.master_problem = RET_OK_NONE
        self.sequence_problems: Dict[Sequence[str], StdRet] = {}


class HotkeyHandler:
    """UI-specific handler for the low-level hotkey code."""

    def set_hotkey_bindings(
            self,
            master_sequence: str,
            key_sequences: Sequence[Sequence[str]],
    ) -> BoundKeyProblems:
        """Takes the master sequence (which is a specially formatted string, left up to
        the OS implementation, but should be standardized where possible), and a collection
        of key sequences to be bound as hotkeys.
        """
        raise NotImplementedError  # pragma no cover


def send_hotkey_pressed(
        context: runner.EventRegistryContext, sequence: Sequence[str],
) -> StdRet[None]:
    """Send a hotkey pressed event."""
    return context.send_event(
        hotkey.HotkeyPressedEvent.UNIQUE_TARGET_FQN,
        hotkey.HotkeyPressedEvent.UNIQUE_TARGET_FQN,
        hotkey.HotkeyPressedEvent(hotkey.BoundHotkey(list(sequence))),
    )


def register_hotkey_listeners(
        context: runner.EventRegistryContext,
        handler: HotkeyHandler,
) -> StdRet[None]:
    """Register the event listeners and parsers into the context."""
    res = context.register_event_parser(
        hotkey.SetHotkeyBindingsEvent.FULL_EVENT_NAME,
        hotkey.SetHotkeyBindingsEvent.parse_data,
    )
    if res.has_error:
        return res
    return context.register_target(
        hotkey.SetHotkeyBindingsEvent.FULL_EVENT_NAME,
        hotkey.SetHotkeyBindingsEvent.UNIQUE_TARGET_FQN,
        HotkeyBindingsTarget(context, handler),
    )


class HotkeyBindingsTarget(runner.EventObjectTarget[hotkey.SetHotkeyBindingsEvent]):
    """Handler for hotkey binding set events."""
    __slots__ = ('_context', '_handler')

    def __init__(self, context: runner.EventRegistryContext, handler: HotkeyHandler) -> None:
        self._context: Optional[runner.EventRegistryContext] = context
        self._handler: Optional[HotkeyHandler] = handler

    def on_close(self) -> None:
        self._context = None
        self._handler = None

    def on_event(
            self, source: str, target: str, event: hotkey.SetHotkeyBindingsEvent,
    ) -> bool:
        if not self._context or not self._handler:
            return True
        res = self._handler.set_hotkey_bindings(
            event.master, [b.keys for b in event.bound],
        )
        bound_errors: List[hotkey.BoundHotkeyProblem] = []
        master_error: Optional[hotkey.MasterHotkeySequenceProblem] = None
        for keys, error_res in res.sequence_problems.items():
            if error_res.has_error:
                bound_errors.append(hotkey.BoundHotkeyProblem(
                    hotkey.BoundHotkey(list(keys)),
                    not_none(create_error_data(
                        hotkey.Error,
                        hotkey.LocalizableMessage,
                        hotkey.MessageArgument,
                        hotkey.MessageArgumentValue,
                        error_res.valid_error,
                        [INVALID_USER_ACTION_ERROR_CATEGORY],
                        'bound-key', 'native-hotkey',
                    )),
                ))
        if res.master_problem.has_error:
            master_error = hotkey.MasterHotkeySequenceProblem(
                event.master,
                not_none(create_error_data(
                    hotkey.Error,
                    hotkey.LocalizableMessage,
                    hotkey.MessageArgument,
                    hotkey.MessageArgumentValue,
                    res.master_problem.valid_error,
                    [INVALID_USER_ACTION_ERROR_CATEGORY],
                    'master-sequence', 'native-hotkey',
                )),
            )

        # Note: sending messages has the errors reported simply.
        if bound_errors or master_error:
            # State did not change.
            report_send_receive_problems(
                internal__send_bind_hotkey_failed(
                    self._context, source, master_error, bound_errors,
                )
            )
        else:
            report_send_receive_problems(
                internal__send_bind_hotkey_success(self._context, source)
            )
            report_send_receive_problems(
                internal__send_hotkey_state(self._context, event.master, event.bound)
            )
        return False


def internal__send_bind_hotkey_failed(
        context: runner.EventRegistryContext,
        target_id: str,
        master_error: Optional[hotkey.MasterHotkeySequenceProblem],
        bound_errors: List[hotkey.BoundHotkeyProblem],
) -> StdRet[None]:
    """Send the bind hotkey failed event."""
    return context.send_event(
        hotkey.SetHotkeyBindingsEvent.UNIQUE_TARGET_FQN,
        target_id,
        hotkey.SetHotkeyBindingsFailedEvent(master_error, bound_errors),
    )


def internal__send_bind_hotkey_success(
        context: runner.EventRegistryContext, target_id: str,
) -> StdRet[None]:
    """Send a bind hotkey success event."""
    return context.send_event(
        hotkey.SetHotkeyBindingsEvent.UNIQUE_TARGET_FQN,
        target_id,
        hotkey.SetHotkeyBindingsSuccessEvent(),
    )


def internal__send_hotkey_state(
        context: runner.EventRegistryContext, master: str, bound: List[hotkey.BoundHotkey],
) -> StdRet[None]:
    """Send the store hotkey state event."""
    return datastore.send_store_data(
        context,
        hotkey.HotkeyBindingsState.UNIQUE_TARGET_FQN,
        hotkey.HotkeyBindingsState(master, bound),
    )