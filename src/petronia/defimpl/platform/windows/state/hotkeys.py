
"""
Registration of hotkeys.
"""

from typing import Dict, Sequence, List, Tuple, Optional
from .....aid.simp import (
    EventBus,
    ValueHolder,
    ParticipantId,
    EventId,
    ListenerId,
    as_state_change_listener,
    StateStoreUpdatedEvent,
    log,
    ERROR,
    DEBUG,
)
from .....core.platform.api.user_input.hotkey import (
    set_hotkey_state,

    CONFIGURATION_ID_HOTKEYS,
    HotkeyConfig,
)
from ...general.hotkey import HotKeyChain, KeyCombo
from ..connect import WindowsHookEvent
from ..input import (
    HotkeyFormatErrorMessage,
    create_hotkey_handler,
    create_master_mkey,
    create_master_modifier,
    create_master_modifier_hotkey_combo,
    create_master_mkey_and_sequence_combo,
)


def bootstrap_hotkeys(
        bus: EventBus, hooks: WindowsHookEvent,
        initial_keys: Optional[Tuple[str, Dict[str, str]]] = None
) -> List[ListenerId]:
    listeners: List[ListenerId] = []

    hotkey_chain = HotKeyChain()
    if initial_keys:
        c_cmd: List[Tuple[Sequence[KeyCombo], str]] = []
        c_errors = _parse_keys(initial_keys[0], initial_keys[1], c_cmd)
        for c_error in c_errors:
            log(ERROR, bootstrap_hotkeys, c_error[0])
        hotkey_chain.set_key_chains(c_cmd)

    resend_invalid_hotkey = ValueHolder(True)
    pass_through_win_key = ValueHolder(False)
    key_hook = create_hotkey_handler(bus, hotkey_chain, resend_invalid_hotkey, pass_through_win_key)
    hooks.set_key_handler(key_hook)

    # -----------------------------------------------------------------------
    # Config Change Handler
    def on_hotkeys_config(
            _event_id: EventId, _target_id: ParticipantId,
            obj: StateStoreUpdatedEvent[HotkeyConfig]
    ) -> None:
        if obj.state_id != CONFIGURATION_ID_HOTKEYS:
            return

        # Could change the behavior of the stop win key...
        # But that will be a different configuration event.

        chain_commands: List[Tuple[Sequence[KeyCombo], str]] = []
        errors = _parse_keys(obj.state.master_sequence, obj.state.hotkeys, chain_commands)
        if errors:
            for error in errors:
                log(ERROR, on_hotkeys_config, error[0])
            return
        log(DEBUG, on_hotkeys_config, 'Setting hotkeys.')
        hotkey_chain.set_key_chains(chain_commands)
        set_hotkey_state(bus, obj.state.master_sequence, obj.state.hotkeys)

    listeners.append(bus.add_listener(  # type: ignore
        CONFIGURATION_ID_HOTKEYS,
        as_state_change_listener, on_hotkeys_config
    ))

    return listeners


def _parse_keys(
        master_seq: str, hotkeys: Dict[str, str],
        chain_commands: List[Tuple[Sequence[KeyCombo], str]]
) -> Sequence[Tuple[str, HotkeyFormatErrorMessage]]:
    # TODO make this return a localizable string for errors.
    errors: List[Tuple[str, HotkeyFormatErrorMessage]] = []

    if master_seq.lower().startswith('seq:'):
        master_mkey = create_master_mkey(master_seq[4:])
        if isinstance(master_mkey, HotkeyFormatErrorMessage):
            errors.append(('Invalid master key sequence "{0}": {1}'.format(master_seq, master_mkey), master_mkey))
            # No state change.
            return errors
        for key, name in hotkeys.items():
            combo = create_master_mkey_and_sequence_combo(master_mkey[0], master_mkey[1], key)
            if isinstance(combo, HotkeyFormatErrorMessage):
                errors.append(('Invalid key sequence: "{0}": {1} (for command {2})'.format(key, combo, name), combo))
                # No state change.
                return errors
            chain_commands.append((combo, name,))
    elif master_seq.lower().startswith('meta:'):
        master_mod = create_master_modifier(master_seq[5:])
        if isinstance(master_mod, HotkeyFormatErrorMessage):
            errors.append(('Invalid master modifier keys "{0}": {1}'.format(master_seq, master_mod), master_mod))
            return errors
        for key, name in hotkeys.items():
            combo = create_master_modifier_hotkey_combo(master_mod, key)
            if isinstance(combo, HotkeyFormatErrorMessage):
                errors.append(('Invalid key sequence: "{0}": {1} (for command {2})'.format(key, combo, name), combo))
                # No state change
                return errors
            chain_commands.append((combo, name,))
    else:
        log(ERROR, 'windows.hotkeys_config', 'Invalid master "{0}"; must start with "seq:" or "meta:"', master_seq)
        return errors

    return errors
