
from typing import Tuple, Sequence, List, Set, Iterable, Callable
from .keymap import (
    vk_to_names,
    is_specially_handled_vk_key,
    get_modifier_vk_keys,
)
from ...general.hotkey import (
    ACTION_CANCELLED,
    ACTION_PENDING,
    ACTION_COMPLETE,
    HotKeyChain,
)
from .....aid.std import (
    EventBus,
    ValueHolder,
)
from .....core.platform.api.user_input.hotkey import (
    send_hotkey_pressed_event,
    send_hotkey_progress_event,
    send_hotkey_progress_cancelled_event,
)


def create_pass_through_win_key_set(pass_through_win_key: bool) -> Iterable[int]:
    """
    Create the list that's input into create_hotkey_handler.

    All modifier keys are pass-through, with the exception of the win-key.
    This can be explicitly blocked to prevent the native Windows win-key
    handling from running.  Note that win+L can never be blocked.
    """
    return get_modifier_vk_keys(pass_through_win_key)


def create_hotkey_handler(
        bus: EventBus, parsed_hotkeys: HotKeyChain,
        resend_invalid_hotkey: ValueHolder[bool],
        pass_through_keys: ValueHolder[Iterable[int]]
) -> Callable[[int, int, bool, bool], Tuple[bool, Sequence[Tuple[int, bool]]]]:
    """
    Creates a handler for the `set_key_handler` method of `WindowsHookEvent`.
    This doesn't need special clean-up actions; this function should only be sent
    to that set_key_handler function, and that will handle the memory.

    :param bus:
    :param parsed_hotkeys:
    :param resend_invalid_hotkey: True if pressing an invalid hotkey combo causes injecting those keys.
    :param pass_through_keys: list of vk codes to pass-through.  If a hotkey is captured and it's not
            in this list, then it's not forwarded on.
    :return: the handler.
    """

    pending_keys: List[str] = []
    pending_scancodes: List[Tuple[int, bool]] = []
    current_action_down: Set[int] = set()

    def handler(
            vk_code: int, scan_code: int, is_key_up: bool, is_injected: bool
    ) -> Tuple[bool, Sequence[Tuple[int, bool]]]:
        if is_injected:
            # Forward on injected keys...
            # print(" - Ignoring injected keys")
            return False, ()
        # return True to cancel the key handling...
        cancel_key_forward = True
        if pass_through_keys.value and vk_code in pass_through_keys.value:
            cancel_key_forward = False

        res, actions = parsed_hotkeys.key_action(vk_code, not is_key_up)
        if res == ACTION_PENDING:
            pending_keys.append(vk_to_names(vk_code)[0] or '(unknown)')
            pending_scancodes.append((scan_code, is_key_up,))
            if is_key_up:
                current_action_down.remove(vk_code)
            else:
                current_action_down.add(vk_code)
            # print(" - Handled keys " + repr(pending_keys) + " (" + repr(pending_scancodes) + ")")
            # print("   Remaining possible combinations: " + repr(actions))
            send_hotkey_progress_event(bus, pending_keys, tuple(actions or ()))
            return cancel_key_forward, ()
        if res == ACTION_CANCELLED:
            if not is_key_up and vk_code in current_action_down:
                # Do not cancel the action.  Take this to mean a key repeat down,
                # with no state change.
                return cancel_key_forward, ()
            pending_scancodes.append((scan_code, is_key_up,))
            ret_codes = tuple(pending_scancodes)
            pending_keys.clear()
            pending_scancodes.clear()
            current_action_down.clear()
            send_hotkey_progress_cancelled_event(bus)

            if resend_invalid_hotkey.value:
                # Block this key from propagating, so that we can inject all the
                # keys in order that were captured.
                # print(" - Cancelled hotkey combo; forwarding {0:02x} {1:02x}".format(*ret_codes))
                return cancel_key_forward, ret_codes
            # print(" - Cancelled hotkey combo")
            return False, ()
        if res == ACTION_COMPLETE:
            pending_keys.clear()
            pending_scancodes.clear()
            current_action_down.clear()
            t_actions = tuple(actions or ('',))
            print(" - Sending hotkey pressed event: " + repr(t_actions))
            send_hotkey_pressed_event(bus, t_actions[0])
            return cancel_key_forward, ()
        # Ignore the key press, and let everything process the key as usual.
        # print(" - Ignoring key")
        return False, ()

    return handler
