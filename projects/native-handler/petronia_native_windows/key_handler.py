"""A key press handler + hotkey integration."""

from typing import List, Sequence, Iterable, Set, Tuple, Optional, Dict
import threading
from concurrent.futures import ThreadPoolExecutor
from petronia_common.util import EMPTY_TUPLE, StdRet, UserMessage, join_errors
from petronia_common.util import i18n as _
from petronia_ext_lib.runner import EventRegistryContext
from petronia_native.common import handlers, hotkey_chain, user_messages
from .arch.native_funcs.windows_common import WPARAM, LPARAM
from .arch import windows_constants
from .datastore.petronia_native_windows import Hotkeys as HotkeyConfig
from . import configuration
from . import message_loop
from . import hook_messages
from . import keymap


class WindowsKeyHandler(handlers.hotkey.HotkeyHandler):
    """Windows integration between the message loop and the
    Petronia events.

    This uses a lock to protect memory access, but all operations in the lock outside
    the message loop must be extremely short, in order to prevent the message loop from
    hanging.
    """
    __slots__ = (
        '__bindings', '__chain', '__config', '__lock', '__active_keys', '__super_in_active',
        '__down_modifiers', '__context', '__executor', '__sequence_names',
    )

    def __init__(
            self, context: EventRegistryContext, config: configuration.ConfigurationStore,
            executor: Optional[ThreadPoolExecutor] = None,
    ) -> None:
        self.__lock = threading.Lock()
        self.__chain = hotkey_chain.HotKeyChain()
        self.__config = config
        self.__context = context
        self.__executor = executor or ThreadPoolExecutor(1)
        self.__sequence_names: Dict[str, Sequence[str]] = {}

        # This will be returned by the key_handler if the current chain is cancelled.
        self.__active_keys: List[Tuple[int, bool]] = []
        self.__super_in_active = False
        self.__down_modifiers: Set[int] = set()

    def register_with_loop(self, loop: message_loop.WindowsMessageLoop) -> None:
        """Register this handler with the loop."""
        loop.set_key_handler(self.key_handler)
        loop.add_message_handler(hook_messages.session_changed_message(
            self.on_session_changed_message,
        ))

    def get_config(self) -> HotkeyConfig:
        """Get the hotkey configuration."""
        config = self.__config.get_config()
        if config:
            return config.hotkeys
        return HotkeyConfig(False)

    def set_hotkey_bindings(
            self, master_sequence: str, key_sequences: Sequence[Sequence[str]],
    ) -> handlers.hotkey.BoundKeyProblems:
        is_ok, ret, names, chains = parse_bindings(master_sequence, key_sequences)
        if is_ok:
            with self.__lock:
                self.__sequence_names = names
                self.__chain.set_key_chains(chains)

                # This may need to be sent back to the Windows session, but for now
                # we're just ignoring it all.  Changing hotkey bindings should be
                # rare enough that this isn't an issue.
                self.__active_keys.clear()

                # Not clearing out active modifiers, though.
                # Should these be passed in?

        return ret

    def on_session_changed_message(self, action: WPARAM, _session_id: LPARAM) -> None:
        """Handle session changed messages; passed as the callback for hook_messages
        session_changed_message."""
        if action == windows_constants.WTS_SESSION_UNLOCK:
            # At unlock, all bets are off about the current key state.
            with self.__lock:
                self.__chain.reset()
                self.__active_keys.clear()
                self.__down_modifiers.clear()

    def key_handler(
            self,
            vk_code: int, _scan_code: int, is_key_up: bool, _is_key_injected: bool,
    ) -> Tuple[bool, Sequence[Tuple[int, bool]]]:
        """Handle the low-level key events.  This function is passed to the message_loop's
        set_key_handler.

        This MUST be done all in-process, because if the key sequence is not a bound hotkey,
        then it must be re-injected into the Windows system (if the config says so).

        Also, because this is done in-process, it can't grab a lock.

        Returns a tuple of
        (bool - true if cancel propagation of key, false if let it go through,
        list of (scancode, is_key_up) injected keys).
        """

        # Cache values before we go into the lock.
        own_super_key = self.get_config().own_super_key
        is_modifier = keymap.is_vk_modifier(vk_code)
        is_super = keymap.is_specially_handled_vk_key(vk_code)
        cancel_propagation_on_ignore = own_super_key and is_super

        with self.__lock:
            if is_modifier:
                if is_key_up:
                    self.__down_modifiers.remove(vk_code)
                else:
                    self.__down_modifiers.add(vk_code)

            state, next_parts = self.__chain.key_action(
                hotkey_chain.StandardKeyCode(vk_code),
                not is_key_up,
            )

            if state == hotkey_chain.IGNORED:
                # Not in a hot key chain.
                return cancel_propagation_on_ignore, EMPTY_TUPLE

            if state == hotkey_chain.ACTION_CANCELLED:
                # Started off as maybe in a chain, but ended up not being in one.
                # This means all the keys up to this point need to be sent back.
                res: Sequence[Tuple[int, bool]]
                if own_super_key and (is_super or self.__super_in_active):
                    res = EMPTY_TUPLE
                else:
                    res = self.__active_keys
                self.__active_keys.clear()
                self.__super_in_active = False
                return cancel_propagation_on_ignore, res

            if state == hotkey_chain.ACTION_PENDING:
                # This key is part of a chain.
                self.__super_in_active = self.__super_in_active or is_super
                self.__active_keys.append((vk_code, is_key_up))
                return True, EMPTY_TUPLE

            # Final state: ACTION_COMPLETE
            # Clear out our key chain state
            self.__super_in_active = False
            self.__active_keys.clear()

            # Send the hotkey action.  This needs to be done in a worker thread, so that
            # it doesn't block the message loop.
            self.__executor.submit(self.send_hotkey, next_parts)

    def send_hotkey(self, next_parts: Iterable[str]) -> None:
        """Send the hotkey associated with this sequence name."""
        sequence_name = tuple(next_parts)[0]
        sequence = self.__sequence_names.get(sequence_name)
        if sequence:
            user_messages.report_send_receive_problems(
                handlers.hotkey.send_hotkey_pressed(self.__context, sequence)
            )


def parse_bindings(
        master_sequence: str, key_sequences: Sequence[Sequence[str]],
) -> Tuple[
    bool,
    handlers.hotkey.BoundKeyProblems,
    Dict[str, Sequence[str]],
    List[Tuple[Sequence[hotkey_chain.KeyCombo], str]],
]:
    """Parse the complete hotkey chain bindings into input for the hotkey chain.
    Returns was ok?, BoundKeyProblems return value, sequence names, and the chain.

    For this implementation, the master sequence can only be a meta-key, like
    shift or super.  The master key sequence is the name of the key separated
    by a plus.
    """

    valid = True
    problems = handlers.hotkey.BoundKeyProblems()
    sequence_names: Dict[str, Sequence[str]] = {}
    sequences: List[Tuple[Sequence[hotkey_chain.KeyCombo], str]] = []

    master_keys_res = parse_primary_master_sequence(master_sequence)
    if master_keys_res.has_error:
        problems.master_problem = master_keys_res.forward()
        valid = False

    # Parse sequences
    for key_sequence in key_sequences:
        sequence_res = parse_sequence(key_sequence)
        if sequence_res.has_error:
            problems.sequence_problems[tuple(key_sequence)] = sequence_res.forward()
            valid = False
        elif master_keys_res.ok:
            codes, name = sequence_res.result
            combo = hotkey_chain.create_primary_chain(master_keys_res.result, codes)
            if combo.has_error:
                problems.sequence_problems[tuple(key_sequence)] = sequence_res.forward()
                valid = False
            else:
                sequence_names[name] = key_sequence
                sequences.append(
                    (combo.result, name)
                )

    return valid, problems, sequence_names, sequences


def parse_primary_master_sequence(
        master_sequence: str,
) -> StdRet[Sequence[hotkey_chain.ModifierKeyCode]]:
    """Parse a primary chain master key as a sequence of meta-keys.

    This returns a list of the keys to press.  If a key has multiple choices
    (say, lshift or rshift), then that is one of the internal lists."""
    master_key_names = master_sequence.split('+')
    errors: List[UserMessage] = []
    ret: List[hotkey_chain.ModifierKeyCode] = []

    for name in master_key_names:
        codes = keymap.get_vk_keys_for_alias(name, True)
        code_len = len(codes)
        if code_len <= 0:
            errors.append(UserMessage(
                user_messages.TRANSLATION_CATALOG,
                _('unknown modifier key: {name}'),
                name=name.strip(),
            ))
        elif code_len == 1:
            ret.append(hotkey_chain.StandardKeyCode(codes[0]))
        else:
            ret.append([
                hotkey_chain.StandardKeyCode(code)
                for code in codes
            ])

    if errors:
        return StdRet.pass_error(join_errors(*errors))
    return StdRet.pass_ok(ret)


def parse_sequence(sequence: Sequence[str]) -> StdRet[
    Tuple[Sequence[hotkey_chain.StandardKeyCode], str]
]:
    """Create a sequence of key codes, and the referencable name for the sequence"""
    sequence_name = ''
    codes: List[hotkey_chain.StandardKeyCode] = []
    errors: List[UserMessage] = []

    for name in sequence:
        name = name.strip()
        key_codes = keymap.get_vk_keys_for_alias(name, False)
        key_code_len = len(key_codes)
        if key_code_len <= 0:
            errors.append(UserMessage(
                user_messages.TRANSLATION_CATALOG,
                _('unknown key name: {name}'),
                name=name,
            ))
        elif key_code_len > 1:
            errors.append(UserMessage(
                user_messages.TRANSLATION_CATALOG,
                _('key {name} references multiple keys; it cannot be used for a sequence'),
                name=name,
            ))
        else:
            sequence_name += '+' + name.lower()
            codes.append(hotkey_chain.StandardKeyCode(key_codes[0]))

    if errors:
        return StdRet.pass_error(join_errors(*errors))
    return StdRet.pass_ok((codes, sequence_name))
