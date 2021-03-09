"""Shared settings."""

from typing import Dict, Sequence, List, Tuple, Optional, Any
from petronia_common.util import StdRet, RET_OK_NONE
from .events.impl import hotkey_binding as hotkey_events
from .events.ext import hotkey as native_events
from .state import hotkey_binding as hotkey_state


def clear_data() -> None:
    """Clear the shared state data."""
    _MASTER_SEQUENCE.clear()
    _MASTER_SEQUENCE_TYPE[0] = 'meta'
    _BOUND_KEYS.clear()
    _EXTENSION_EVENTS.clear()


def load_configuration(config: Dict[str, Any]) -> StdRet[None]:
    """Load the configuration data."""
    parsed_res = hotkey_state.ConfigurationState.parse_data(config)
    if parsed_res.has_error:
        return parsed_res.forward()
    set_hotkey_state(parsed_res.result)

    return RET_OK_NONE


_MASTER_SEQUENCE: List[str] = []
_MASTER_SEQUENCE_TYPE = ['meta']
_BOUND_KEYS: Dict[Sequence[str], Tuple[Optional[str], hotkey_events.BoundEvent]] = {}
_EXTENSION_EVENTS: Dict[str, hotkey_events.Events] = {}


def set_master_sequence(sequence_type: str, sequence: Sequence[str]) -> None:
    """Set the shared state master sequence.  Does not send events."""
    _MASTER_SEQUENCE_TYPE[0] = sequence_type
    _MASTER_SEQUENCE.clear()
    _MASTER_SEQUENCE.extend(sequence)


def set_bound_key(
        keys: Sequence[str], comment: Optional[str], event: hotkey_events.BoundEvent,
) -> None:
    """Set a single bound key.  Does not send events."""
    _BOUND_KEYS[tuple(keys)] = (comment, event)


def set_extension_event(event: hotkey_events.Events) -> None:
    """Set a single extension event."""
    _EXTENSION_EVENTS[event.name] = event


def get_extension_events() -> Sequence[hotkey_events.Events]:
    """Get all registered extension events."""
    return tuple(_EXTENSION_EVENTS.values())


def get_bound_event(
        keys: Sequence[str],
) -> Optional[hotkey_events.BoundEvent]:
    """Get the event bound to the hotkey sequence, if any."""
    res = _BOUND_KEYS.get(tuple(keys))
    if res:
        return res[1]
    return None


def get_hotkey_state() -> hotkey_state.ConfigurationState:
    """Generate the configuration state from the internal data."""
    return hotkey_state.ConfigurationState(hotkey_state.BoundKeys(
        _MASTER_SEQUENCE_TYPE[0], list(_MASTER_SEQUENCE), [
            hotkey_state.BoundHotkey(
                list(seq), hotkey_state.BoundEvent(
                    co_evt[1].target_id, [
                        hotkey_state.BoundEventParameter(param.key, param.value)
                        for param in co_evt[1].parameters
                    ],
                ), co_evt[0],
            )
            for seq, co_evt in _BOUND_KEYS.items()
        ]
    ))


def get_bound_keys_state() -> hotkey_events.BoundKeysState:
    """Generate the bound keys state from the internal data."""
    return hotkey_events.BoundKeysState(
        _MASTER_SEQUENCE_TYPE[0],
        list(_MASTER_SEQUENCE),
        [
            hotkey_events.BoundHotkey(
                list(seq), hotkey_events.BoundEvent(
                    co_evt[1].target_id, [
                        hotkey_events.BoundEventParameter(param.key, param.value)
                        for param in co_evt[1].parameters
                    ]
                ), co_evt[0],
            )
            for seq, co_evt in _BOUND_KEYS.items()
        ]
    )


def set_hotkey_state(config: hotkey_state.ConfigurationState) -> None:
    """Set the internal state from the configuration state object."""
    clear_data()
    set_master_sequence(config.bindings.sequence_type, config.bindings.master_sequence)
    for binding in config.bindings.bindings:
        set_bound_key(binding.keys, binding.comment, hotkey_events.BoundEvent(
            binding.event.target_id, [
                hotkey_events.BoundEventParameter(param.key, param.value)
                for param in binding.event.parameters
            ]
        ))


def get_native_binding_event(request_id: int) -> native_events.SetHotkeyBindingsEvent:
    """Create the native event object based on the internal state."""
    return native_events.SetHotkeyBindingsEvent(
        request_id,
        native_events.MasterHotkeySequence(
            _MASTER_SEQUENCE_TYPE[0],
            list(_MASTER_SEQUENCE),
        ),
        [
            native_events.BoundHotkey(list(keys))
            for keys in _BOUND_KEYS.keys()
        ],
    )
