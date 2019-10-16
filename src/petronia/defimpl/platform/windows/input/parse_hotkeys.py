
"""
Split the hotkey string into the VK code sets.
"""

from typing import Sequence, Tuple, List, Union, Optional
from .....aid.std import (
    ErrorReport,
    ResultOrError,
    create_user_error,
)
from ...general.hotkey import (
    KeyCombo,
    StandardKeyCode,
    ModifierKeyCode,
    create_modal_chain,
    create_primary_chain,
)
from .keymap import (
    MODIFIERS,
    STR_VK_MAP,
    VK_ALIASES,
)


def create_hotkey_format_error(hotkey: str, err: str, **args: Union[int, str]) -> ErrorReport:
    return create_user_error(
        'parse_hotkeys',
        'invalid hotkey format for "{hotkey}": ' + err,
        hotkey=hotkey, **args
    )


def create_master_modifier_hotkey_combo(
        master_modifier: Sequence[ModifierKeyCode],
        hotkey: str
) -> ResultOrError[Sequence[KeyCombo]]:
    """
    Parses the standard master modifier (e.g. Super+Shift) plus a key to go with it
    (e.g. up-arrow or ctrl+1).
    """
    if hotkey.find('+') > 0:
        # At least one modifier...
        simple = parse_simple_modified_key(hotkey, hotkey)
        if isinstance(simple, ErrorReport):
            return simple
        modifiers = list(master_modifier) + list(simple[0])
        return create_primary_chain(modifiers, (simple[1],))
    key = convert_standard_key_name(hotkey)
    if key is None:
        return create_hotkey_format_error(hotkey, 'expected zero or more modifiers plus a normal key')
    return create_primary_chain(master_modifier, (key,))


def create_master_mkey_and_sequence_combo(
        master_modifiers: Sequence[ModifierKeyCode],
        master_key: StandardKeyCode,
        hotkeys: str
) -> ResultOrError[Sequence[KeyCombo]]:
    """
    Create a modal key sequence.  This is a master modifier + key
    (say, ctrl-a), followed by one or more normal keys.  This is similar to
    how the `screen` program works.
    """
    modal_keys = parse_key_sequence(hotkeys, hotkeys)
    if isinstance(modal_keys, ErrorReport):
        return modal_keys
    return create_modal_chain(master_modifiers, (master_key,), modal_keys)


def create_master_modifier(
        master: str
) -> ResultOrError[Sequence[ModifierKeyCode]]:
    """Creates a primary modifier combination master sequence, such as `super`."""
    return parse_modifier_sequence(master, master)


def create_master_mkey(
        modifier_key: str
) -> ResultOrError[Tuple[Sequence[ModifierKeyCode], StandardKeyCode]]:
    """Creates a master modifier key sequence, such as `super+a`."""
    return parse_simple_modified_key(modifier_key, modifier_key)


def parse_modifier_sequence(
        original_expression: str, hotkey: str
) -> ResultOrError[Sequence[ModifierKeyCode]]:
    """
    Parses a simple sequence of modifier keys, separated by '+'.
    """
    keys = hotkey.split('+')
    if not keys:
        return create_hotkey_format_error(
            original_expression, 'modifier sequence must have at least 1 modifier'
        )
    modifier_vks: List[ModifierKeyCode] = []
    for kname in keys:
        mvk = convert_modifier_key_name(kname)
        if mvk is None:
            return create_hotkey_format_error(
                original_expression,
                'modifier key must have at least 1 modifier; '
                'found normal key or unknown modifier key "{kname}"',
                kname=kname
            )
        modifier_vks.append(mvk)
    assert len(modifier_vks) >= 1
    return modifier_vks


def parse_simple_modified_key(
        original_expression: str, hotkey: str
) -> ResultOrError[Tuple[Sequence[ModifierKeyCode], StandardKeyCode]]:
    """
    Parses a simple sequence of `modifier '+' modifier '+' ... '+' key`.

    Used for the master sequence, or part of a sequence for other things.
    """
    keys = hotkey.split('+')
    if len(keys) < 2:
        return create_hotkey_format_error(
            original_expression,
            'modifier key must have at least 1 modifier and exactly 1 normal key'
        )
    final_vk = convert_standard_key_name(keys[-1])
    if final_vk is None:
        return create_hotkey_format_error(
            original_expression,
            'modifier key must have at least 1 modifier and exactly 1 normal key; '
            'found modifier key or unknown key "{key}" instead of a normal key',
            key=keys[-1]
        )
    modifier_vks: List[ModifierKeyCode] = []
    for kname in keys[:-1]:
        mvk = convert_modifier_key_name(kname)
        if mvk is None:
            return create_hotkey_format_error(
                original_expression,
                # TODO localize
                'modifier key must have at least 1 modifier and exactly 1 normal key; '
                'found normal key or unknown key "{kname}" instead of a modifier',
                kname=kname
            )
        modifier_vks.append(mvk)
    assert len(modifier_vks) >= 1
    return modifier_vks, final_vk


def parse_key_sequence(
        original_expression: str, hotkey: str
) -> ResultOrError[Sequence[StandardKeyCode]]:
    """
    Parses a sequence of non-modifier keys.

    These are a simple list of key names separated by a '+'.
    """

    sequence_keys = hotkey.split('+')
    if not sequence_keys:
        return create_hotkey_format_error(
            original_expression,
            'key sequence must have at least 1 normal key'
        )
    sequence_vks: List[StandardKeyCode] = []
    for kname in sequence_keys:
        skv = convert_standard_key_name(kname)
        if skv is None:
            return create_hotkey_format_error(
                original_expression,
                'key sequence must have at least 1 normal key; '
                'found modifier key or unknown key "{kname}" instead of a normal key',
                kname=kname
            )
        sequence_vks.append(skv)
    return sequence_vks


def convert_modifier_key_name(name: str) -> Optional[ModifierKeyCode]:
    """Convert the modifier key text name into one VK or a collection of VK
    alternatives."""
    name = name.lower().strip()
    if name in VK_ALIASES:
        ret: List[int] = []
        for kname in VK_ALIASES[name]:
            ret.append(STR_VK_MAP[kname])
        return ret
    if name in MODIFIERS:
        return STR_VK_MAP[name]
    return None


def convert_standard_key_name(name: str) -> Optional[StandardKeyCode]:
    """Convert the standard key text name to a VK."""
    name = name.lower().strip()
    if name in VK_ALIASES or name in MODIFIERS or name not in STR_VK_MAP:
        return None
    return STR_VK_MAP[name]
