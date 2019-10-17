
"""
Registration of hotkeys.
"""

from typing import Dict, Sequence, List, Tuple, Optional
from .....aid.std import (
    EventBus,
    ValueHolder,
    ParticipantId,
    EventId,
    ListenerId,
    as_state_change_listener,
    StateStoreUpdatedEvent,
    log,
    DEBUG,
    ErrorReport,
    create_user_error,
    report_error,
)
from .....core.platform.api.user_input.hotkey import (
    set_hotkey_state,
    CONFIGURATION_ID_HOTKEYS,
    HotkeyConfig,
)
from ...general.hotkey import HotKeyChain, KeyCombo
from ..connect import WindowsHookEvent
from ..input import (
    create_hotkey_handler,
    create_pass_through_win_key_set,
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
            report_error(bus, c_error)
        hotkey_chain.set_key_chains(c_cmd)

    resend_invalid_hotkey = ValueHolder(True)
    pass_through_keys = ValueHolder(create_pass_through_win_key_set(False))
    key_hook = create_hotkey_handler(bus, hotkey_chain, resend_invalid_hotkey, pass_through_keys)
    hooks.set_key_handler(key_hook)

    # -----------------------------------------------------------------------
    # Config Change Handler
    def on_hotkeys_config(
            _event_id: EventId, _target_id: ParticipantId,
            event_obj: StateStoreUpdatedEvent[HotkeyConfig]
    ) -> None:
        if event_obj.state_id != CONFIGURATION_ID_HOTKEYS:
            return

        # TODO Could change the behavior of the stop win key...
        #   But that will be a different configuration event.

        chain_commands: List[Tuple[Sequence[KeyCombo], str]] = []
        errors = _parse_keys(event_obj.state.master_sequence, event_obj.state.hotkeys, chain_commands)
        if errors:
            for error in errors:
                report_error(bus, error)
            return
        log(DEBUG, on_hotkeys_config, 'Setting hotkeys.')
        hotkey_chain.set_key_chains(chain_commands)
        set_hotkey_state(bus, event_obj.state.master_sequence, event_obj.state.hotkeys)

    listeners.append(bus.add_listener(  # type: ignore
        CONFIGURATION_ID_HOTKEYS,
        as_state_change_listener, on_hotkeys_config
    ))

    return listeners


def _parse_keys(
        master_seq: str, hotkeys: Dict[str, str],
        chain_commands: List[Tuple[Sequence[KeyCombo], str]]
) -> Sequence[ErrorReport]:
    errors: List[ErrorReport] = []

    if master_seq.lower().startswith('seq:'):
        master_mkey = create_master_mkey(master_seq[4:])
        if isinstance(master_mkey, ErrorReport):
            errors.append(create_user_error(
                'parse_hotkeys',
                'Invalid master key sequence "{master_seq}"',
                master_seq=master_seq
            ))
            errors.append(master_mkey)
            # No state change.
            return errors
        for key, name in hotkeys.items():
            combo = create_master_mkey_and_sequence_combo(master_mkey[0], master_mkey[1], key)
            if isinstance(combo, ErrorReport):
                errors.append(create_user_error(
                    'parse_hotkeys',
                    'Invalid key sequence: "{key}" (for command {name})',
                    key=key, name=name
                ))
                errors.append(combo)
                # No state change.
                return errors
            chain_commands.append((combo, name,))
    elif master_seq.lower().startswith('meta:'):
        master_mod = create_master_modifier(master_seq[5:])
        if isinstance(master_mod, ErrorReport):
            errors.append(create_user_error(
                'parse_hotkeys',
                'Invalid master modifier keys "{master_seq}"',
                master_seq=master_seq
            ))
            errors.append(master_mod)
            return errors
        for key, name in hotkeys.items():
            combo = create_master_modifier_hotkey_combo(master_mod, key)
            if isinstance(combo, ErrorReport):
                errors.append(create_user_error(
                    'parse_hotkeys',
                    'Invalid key sequence: "{key}" (for command {name})',
                    key=key, name=name
                ))
                errors.append(combo)
                # No state change
                return errors
            chain_commands.append((combo, name,))
    else:
        errors.append(create_user_error(
            'parse_hotkeys',
            'Invalid master "{master_seq}"; must start with "seq:" or "meta:"',
            master_seq=master_seq
        ))
        return errors

    return errors
