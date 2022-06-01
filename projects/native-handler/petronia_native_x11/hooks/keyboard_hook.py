"""Keyboard setup handler."""
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, Sequence, List, Tuple, Set, Iterable, Union, Optional
import threading
from petronia_common.util import StdRet, UserMessage, RET_OK_NONE
from petronia_native.common import handlers, hotkey_chain, user_messages, hotkey_parser
from petronia_native.common.handlers.hotkey import HotkeyHandler
from ..datastore.petronia_native_x11 import EXTENSION_NAME
from ..libs import libxcb_types, keys, ct_util
from ..common_data import Libraries, WindowManagerData
from ..running_data import RunningData
from ..hook_types import Hook


class KeyboardHook(Hook, HotkeyHandler):
    """Interact with the keyboard stuff."""
    __slots__ = (
        '__data', '__keymap', '__chain', '__sequence_names',
        '__active_keys', '__lock', '__binding_data', '__executor',
    )

    def __init__(
            self,
            executor: Optional[ThreadPoolExecutor] = None,
    ) -> None:
        self.__lock = threading.Lock()
        self.__data: Optional[RunningData] = None

        # Mapping of keycodes -> utf characters.
        self.__keymap: Optional[hotkey_parser.KeyMap] = None

        self.__chain = hotkey_chain.HotKeyChain()
        self.__sequence_names: Dict[str, Sequence[str]] = {}
        self.__active_keys: List[Tuple[int, bool]] = []
        self.__down_modifiers: Set[int] = set()

        self.__binding_data: Optional[Tuple[str, List[str], Sequence[Sequence[str]]]] = None
        self.__executor = executor or ThreadPoolExecutor(1)

    def setup_wm_screen(self, data: WindowManagerData) -> StdRet[None]:
        self._update_keymap(data)
        return RET_OK_NONE

    def setup_pre_event_loop(self, data: RunningData) -> StdRet[None]:
        self.__data = data
        data.event_loop.get_event_registrar().register_keypress_callback(self._key_pressed)
        data.event_loop.get_event_registrar().register_keyrelease_callback(self._key_released)
        data.event_loop.get_event_registrar().register_keymap_callback(self._keymap)
        return RET_OK_NONE

    def shutdown(self, data: RunningData) -> StdRet[None]:
        self.__data = data
        return RET_OK_NONE

    def send_hotkey(self, next_parts: Iterable[str]) -> None:
        """Send the hotkey associated with this sequence name."""
        data = self.__data
        if not data:
            return
        sequence_name = tuple(next_parts)[0]
        sequence = self.__sequence_names.get(sequence_name)
        if sequence:
            # print(f'[KEY] sending chain {sequence_name} / {sequence}')
            user_messages.report_send_receive_problems(
                handlers.hotkey.send_hotkey_pressed(data.context, sequence)
            )
        else:
            # TODO This should be a programmer error.
            print(f'[KEY] unknown chain {sequence_name} / {sequence}')
            print(f'[KEY] known chain names: {self.__sequence_names.keys()}')

    def set_hotkey_bindings(
            self,
            master_sequence_type: str,
            master_sequence: List[str],
            key_sequences: Sequence[Sequence[str]],
    ) -> handlers.hotkey.BoundKeyProblems:
        self.__binding_data = (master_sequence_type, master_sequence, key_sequences)
        return self._rebind_hotkeys()

    def _key_pressed(self, event: libxcb_types.XcbKeyPressEventP) -> Optional[bool]:
        keymap = self.__keymap
        data = self.__data
        if not keymap or not data:
            return None

        # Cache values before we go into the lock.
        keycode = ct_util.as_py_int(event.contents.detail)
        is_modifier = keymap.is_meta_code(keycode)
        print(f"[KEY] pressed {keymap.get_key_aliases(keycode)}{is_modifier and ' *' or ''}")

        # May want to ignore injected codes.  How to detect this?  It seems to be
        #   related to the event handler itself, perhaps?

        with self.__lock:
            if is_modifier:
                self.__down_modifiers.add(keycode)

            state, next_parts = self.__chain.key_action(
                hotkey_chain.StandardKeyCode(keycode),
                True,
            )

            if state == hotkey_chain.IGNORED:
                # Not in a hot key chain.
                # print(f'[KEY] ignoring {vk_code}')
                return False

            if state == hotkey_chain.ACTION_CANCELLED:
                # Started off as maybe in a chain, but ended up not being in one.
                # This means all the keys up to this point need to be sent back (injected)
                _inject_keys(data.window_manager_data, [*self.__active_keys, (keycode, True)])
                self.__active_keys.clear()
                # print(f'[KEY] cancelled with {vk_code}; regenerating {res}')
                return True

            if state == hotkey_chain.ACTION_PENDING:
                # This key is part of a chain.
                # print(f'[KEY] part of chain ({vk_code})')
                self.__active_keys.append((keycode, True))
                return True

            # Final state: ACTION_COMPLETE
            # Clear out our key chain state
            # print(f'[KEY] chain complete with {vk_code} - {next_parts}')
            self.__active_keys.clear()

            # Send the hotkey action.  This needs to be done in a worker thread, so that
            # it doesn't block the message loop.
            self.__executor.submit(self.send_hotkey, next_parts)
            return True

    def _key_released(self, event: libxcb_types.XcbKeyReleaseEventP) -> Optional[bool]:
        keymap = self.__keymap
        data = self.__data
        if not keymap or not data:
            return None

        # Cache values before we go into the lock.
        keycode = ct_util.as_py_int(event.contents.detail)
        is_modifier = keymap.is_meta_code(keycode)
        print(f"[KEY] released {keymap.get_key_aliases(keycode)}{is_modifier and ' *' or ''}")

        # May want to ignore injected codes.  How to detect this?  It seems to be
        #   related to the event handler itself, perhaps?

        with self.__lock:
            if is_modifier:
                if keycode in self.__down_modifiers:
                    self.__down_modifiers.remove(keycode)

            state, next_parts = self.__chain.key_action(
                hotkey_chain.StandardKeyCode(keycode),
                False,
            )

            if state == hotkey_chain.IGNORED:
                # Not in a hot key chain.
                # print(f'[KEY] ignoring {vk_code}')
                return True

            if state == hotkey_chain.ACTION_CANCELLED:
                # Started off as maybe in a chain, but ended up not being in one.
                # This means all the keys up to this point need to be sent back.
                _inject_keys(data.window_manager_data, [*self.__active_keys, (keycode, False)])
                self.__active_keys.clear()
                # print(f'[KEY] cancelled with {vk_code}; regenerating {res}')
                return True

            if state == hotkey_chain.ACTION_PENDING:
                # This key is part of a chain.
                # print(f'[KEY] part of chain ({vk_code})')
                self.__active_keys.append((keycode, False))
                return True

            # Final state: ACTION_COMPLETE
            # Clear out our key chain state
            # print(f'[KEY] chain complete with {vk_code} - {next_parts}')
            self.__active_keys.clear()

            # Send the hotkey action.  This needs to be done in a worker thread, so that
            # it doesn't block the message loop.
            self.__executor.submit(self.send_hotkey, next_parts)
            return True

    def _keymap(self, _event: libxcb_types.XcbKeymapNotifyEventP) -> Optional[bool]:
        if self.__data:
            self._update_keymap(self.__data.window_manager_data)
        return None

    def _rebind_hotkeys(self) -> handlers.hotkey.BoundKeyProblems:
        if self.__keymap and self.__binding_data:
            master_sequence_type, master_sequence, key_sequences = self.__binding_data
            is_ok, ret, names, chains = hotkey_parser.parse_bindings(
                master_sequence_type, master_sequence, key_sequences, self.__keymap,
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
        # No keymap or binding data, so we can't conclude anything yet.
        return handlers.hotkey.BoundKeyProblems()

    def _update_keymap(self, wm_data: WindowManagerData) -> None:
        self.__keymap = keys.grab_keymap(wm_data.libs.xcb, wm_data.libs.clib, wm_data.connection)
        self._rebind_hotkeys()


def _inject_keys(wm_data: WindowManagerData, key_events: Sequence[Tuple[int, bool]]) -> None:
    """Inject the keycode, is_pressed back into X."""


def keyboard_factory(libs: Libraries) -> StdRet[Union[Hook, UserMessage]]:
    """Set up the keyboard."""
    keys.generate_keysym_table()
    hook = KeyboardHook()

    res = handlers.hotkey.register_hotkey_listeners(
        libs.context,
        EXTENSION_NAME,
        hook,
    )
    if res.has_error:
        return res.forward()

    return StdRet.pass_ok(hook)
