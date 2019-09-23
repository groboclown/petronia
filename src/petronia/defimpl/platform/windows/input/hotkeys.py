
from typing import Tuple, Sequence, List, Callable
from .keymap import (
    vk_to_names,
    is_specially_handled_vk_key,
)
from ...general.hotkey import (
    ACTION_CANCELLED,
    ACTION_PENDING,
    ACTION_COMPLETE,
    HotKeyChain,
)
from .....aid.simp import (
    EventBus,
    ValueHolder,
)
from .....core.platform.api.user_input.hotkey import (
    send_hotkey_pressed_event,
    send_hotkey_progress_event,
    send_hotkey_progress_cancelled_event,
)


def create_hotkey_handler(
        bus: EventBus, parsed_hotkeys: HotKeyChain,
        resend_invalid_hotkey: ValueHolder[bool],
        pass_through_win_key: ValueHolder[bool]
) -> Callable[[int, int, bool, bool], Tuple[bool, Sequence[Tuple[int, bool]]]]:
    """
    Creates a handler for the `set_key_handler` method of `WindowsHookEvent`.
    This doesn't need special clean-up actions; this function should only be sent
    to that set_key_handler function, and that will handle the memory.

    :param bus:
    :param parsed_hotkeys:
    :param resend_invalid_hotkey: True if pressing an invalid hotkey combo causes injecting those keys.
    :param pass_through_win_key: True if the `win` key press & release should be passed-through, regardless
        of the hotkey matching state.
    :return: the handler.
    """

    pending_keys: List[str] = []
    pending_scancodes: List[Tuple[int, bool]] = []

    def handler(
            vk_code: int, scan_code: int, is_key_up: bool, is_injected: bool
    ) -> Tuple[bool, Sequence[Tuple[int, bool]]]:
        if is_injected:
            # Forward on injected keys...
            # print(" - Ignoring injected keys")
            return False, ()
        # return True to cancel the key handling...
        cancel_key_forward = True
        if pass_through_win_key.value and is_specially_handled_vk_key(vk_code):
            cancel_key_forward = False

        res, actions = parsed_hotkeys.key_action(vk_code, not is_key_up)
        if res == ACTION_PENDING:
            pending_keys.append(vk_to_names(vk_code)[0] or '(unknown)')
            pending_scancodes.append((scan_code, is_key_up,))
            print(" - Pending hotkeys: " + repr(actions))
            send_hotkey_progress_event(bus, pending_keys, actions or ())
            return cancel_key_forward, ()
        if res == ACTION_CANCELLED:
            pending_scancodes.append((scan_code, is_key_up,))
            ret_codes = tuple(pending_scancodes)
            pending_keys.clear()
            pending_scancodes.clear()
            send_hotkey_progress_cancelled_event(bus)

            if resend_invalid_hotkey.value:
                # Block this key from propagating, so that we can inject all the
                # keys in order that were captured.
                print(" - Cancelled hotkey combo; forwarding " + repr(ret_codes))
                return cancel_key_forward, ret_codes
            print(" - Cancelled hotkey combo")
            return False, ()
        if res == ACTION_COMPLETE:
            pending_keys.clear()
            pending_scancodes.clear()
            print(" - Sending hotkey pressed event: " + repr(actions))
            send_hotkey_pressed_event(bus, (actions or ('',))[0])
            return cancel_key_forward, ()
        # Ignore the keypress, and let everything process the key as usual.
        # print(" - Ignoring key")
        return False, ()

    return handler
