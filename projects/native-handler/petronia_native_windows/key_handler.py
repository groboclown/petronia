"""A key press handler + hotkey integration."""

from typing import List, Sequence, Iterable, Set, Tuple, Optional, Dict
import threading
from concurrent.futures import ThreadPoolExecutor
from petronia_common.util import EMPTY_TUPLE
from petronia_ext_lib.runner import EventRegistryContext
from petronia_native.common import handlers, hotkey_chain, user_messages, hotkey_parser
from .arch.native_funcs.windows_common import WPARAM, LPARAM
from .arch import windows_constants
from .datastore.petronia_native_windows import Hotkeys as HotkeyConfig
from . import configuration
from . import message_loop
from . import hook_messages
from . import keymap


class WindowsKeyHandler(handlers.hotkey.HotkeyHandler):  # pylint:disable=too-many-instance-attributes
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
            self,
            master_sequence_type: str,
            master_sequence: List[str],
            key_sequences: Sequence[Sequence[str]],
    ) -> handlers.hotkey.BoundKeyProblems:
        is_ok, ret, names, chains = hotkey_parser.parse_bindings(
            master_sequence_type,
            master_sequence, key_sequences,
            keymap.WINDOWS_KEY_MAP,
        )
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

                print('[KEY] updated key bindings')

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
            vk_code: int, _scan_code: int, is_key_up: bool, is_key_injected: bool,
    ) -> Tuple[bool, Sequence[Tuple[int, bool]]]:
        """Handle the low-level key events.  This function is passed to the message_loop's
        set_key_handler.

        This MUST be done all in-process, because if the key sequence is not a bound hotkey,
        then it must be re-injected into the Windows system (if the config says so).

        Also, because this is done in-process, it shouldn't grab a lock... but it does.
        The only real thing that can be done to accommodate this is to ensure everything else
        spends very little time in the lock.

        Returns a tuple of
        (bool - true if cancel propagation of key, false if let it go through,
        list of (scancode, is_key_up) injected keys).
        """

        # Cache values before we go into the lock.
        own_super_key = self.get_config().own_super_key
        is_modifier = keymap.is_vk_modifier(vk_code)
        is_super = keymap.is_specially_handled_vk_key(vk_code)
        cancel_propagation_on_ignore = own_super_key and is_super

        # Ignore injected keys.  This is a self preservation attempt to prevent Petronia
        # from cycling around and retrying key chains that are ignored and re-injected back.
        if is_key_injected:
            return cancel_propagation_on_ignore, EMPTY_TUPLE

        with self.__lock:
            if is_modifier:
                if is_key_up:
                    if vk_code in self.__down_modifiers:
                        self.__down_modifiers.remove(vk_code)
                else:
                    self.__down_modifiers.add(vk_code)

            state, next_parts = self.__chain.key_action(
                hotkey_chain.StandardKeyCode(vk_code),
                not is_key_up,
            )

            if state == hotkey_chain.IGNORED:
                # Not in a hot key chain.
                # print(f'[KEY] ignoring {vk_code}')
                return cancel_propagation_on_ignore, EMPTY_TUPLE

            if state == hotkey_chain.ACTION_CANCELLED:
                # Started off as maybe in a chain, but ended up not being in one.
                # This means all the keys up to this point need to be sent back.
                res: Sequence[Tuple[int, bool]]
                if own_super_key and (is_super or self.__super_in_active):
                    res = EMPTY_TUPLE
                else:
                    res = tuple([*self.__active_keys, (vk_code, is_key_up)])
                self.__active_keys.clear()
                self.__super_in_active = False
                # print(f'[KEY] cancelled with {vk_code}; regenerating {res}')
                return cancel_propagation_on_ignore, res

            if state == hotkey_chain.ACTION_PENDING:
                # This key is part of a chain.
                # print(f'[KEY] part of chain ({vk_code})')
                self.__super_in_active = self.__super_in_active or is_super
                self.__active_keys.append((vk_code, is_key_up))
                return True, EMPTY_TUPLE

            # Final state: ACTION_COMPLETE
            # Clear out our key chain state
            # print(f'[KEY] chain complete with {vk_code} - {next_parts}')
            self.__super_in_active = False
            self.__active_keys.clear()

            # Send the hotkey action.  This needs to be done in a worker thread, so that
            # it doesn't block the message loop.
            self.__executor.submit(self.send_hotkey, next_parts)
            return True, EMPTY_TUPLE

    def send_hotkey(self, next_parts: Iterable[str]) -> None:
        """Send the hotkey associated with this sequence name."""
        sequence_name = tuple(next_parts)[0]
        sequence = self.__sequence_names.get(sequence_name)
        if sequence:
            # print(f'[KEY] sending chain {sequence_name} / {sequence}')
            user_messages.report_send_receive_problems(
                handlers.hotkey.send_hotkey_pressed(self.__context, sequence)
            )
        else:
            # TODO This should be a programmer error.
            print(f'[KEY] unknown chain {sequence_name} / {sequence}')
            print(f'[KEY] known chain names: {self.__sequence_names.keys()}')
