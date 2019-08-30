
"""
Split the hotkey string into the VK code sets.
"""

from typing import Sequence, Tuple, List, Union, Optional
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


class HotkeyFormatErrorMessage:
    """A problem with the format of a hotkey string."""
    __slots__ = ('__hotkey', '__err_msg', '__err_args',)

    def __init__(
            self, hotkey: str, err_msg: str,
            *err_args: Union[int, str]
    ) -> None:
        self.__hotkey = hotkey
        self.__err_msg = err_msg
        self.__err_args = err_args

    @property
    def hotkey(self) -> str:
        return self.__hotkey

    @property
    def err_msg(self) -> str:
        return self.__err_msg

    @property
    def err_args(self) -> Sequence[Union[int, str]]:
        return self.__err_args

    def __repr__(self) -> str:
        return 'HotkeyFormatErrorMessage(hotkey={0}, err_msg={1}, err_args={2}'.format(
            repr(self.__hotkey), repr(self.__err_msg), repr(self.__err_args)
        )


def create_master_modifier_hotkey_combo(
        master_modifier: Sequence[ModifierKeyCode],
        hotkey: str
) -> Union[Sequence[KeyCombo], HotkeyFormatErrorMessage]:
    """
    Parses the standard master modifier (e.g. Super+Shift) plus a key to go with it
    (e.g. up-arrow or ctrl+1).
    """
    if hotkey.find('+') > 0:
        # At least one modifier...
        simple = parse_simple_modified_key(hotkey, hotkey)
        if isinstance(simple, HotkeyFormatErrorMessage):
            return simple
        modifiers = list(master_modifier) + list(simple[0])
        return create_primary_chain(modifiers, (simple[1],))
    key = convert_standard_key_name(hotkey)
    if key is None:
        return HotkeyFormatErrorMessage(hotkey, 'expected zero or more modifiers plus a normal key')
    return create_primary_chain(master_modifier, (key,))


def create_master_mkey_and_sequence_combo(
        master_modifiers: Sequence[ModifierKeyCode],
        master_key: StandardKeyCode,
        hotkeys: str
) -> Union[Sequence[KeyCombo], HotkeyFormatErrorMessage]:
    """
    Create a modal key sequence.  This is a master modifier + key
    (say, ctrl-a), followed by one or more normal keys.  This is similar to
    how the `screen` program works.
    """
    modal_keys = parse_key_sequence(hotkeys, hotkeys)
    if isinstance(modal_keys, HotkeyFormatErrorMessage):
        return modal_keys
    return create_modal_chain(master_modifiers, (master_key,), modal_keys)


def create_master_modifier(
        master: str
) -> Union[Sequence[ModifierKeyCode], HotkeyFormatErrorMessage]:
    """Creates a primary modifier combination master sequence, such as `super`."""
    return parse_modifier_sequence(master, master)


def create_master_mkey(
        modifier_key: str
) -> Union[Tuple[Sequence[ModifierKeyCode], StandardKeyCode], HotkeyFormatErrorMessage]:
    """Creates a master modifier key sequence, such as `super+a`."""
    return parse_simple_modified_key(modifier_key, modifier_key)


def parse_modifier_sequence(
        original_expression: str, hotkey: str
) -> Union[Sequence[ModifierKeyCode], HotkeyFormatErrorMessage]:
    """
    Parses a simple sequence of modifier keys, separated by '+'.
    """
    keys = hotkey.split('+')
    if not keys:
        return HotkeyFormatErrorMessage(
            original_expression,
            # TODO localize
            'modifier sequence must have at least 1 modifier'
        )
    modifier_vks: List[ModifierKeyCode] = []
    for kname in keys:
        mvk = convert_modifier_key_name(kname)
        if mvk is None:
            return HotkeyFormatErrorMessage(
                original_expression,
                # TODO localize
                'modifier key must have at least 1 modifier; '
                'found normal key or unknown modifier key "{0}"',
                kname
            )
        modifier_vks.append(mvk)
    assert len(modifier_vks) >= 1
    return modifier_vks


def parse_simple_modified_key(
        original_expression: str, hotkey: str
) -> Union[Tuple[Sequence[ModifierKeyCode], StandardKeyCode], HotkeyFormatErrorMessage]:
    """
    Parses a simple sequence of `modifier '+' modifier '+' ... '+' key`.

    Used for the master sequence, or part of a sequence for other things.
    """
    keys = hotkey.split('+')
    if len(keys) < 2:
        return HotkeyFormatErrorMessage(
            original_expression,
            # TODO localize
            'modifier key must have at least 1 modifier and exactly 1 normal key'
        )
    final_vk = convert_standard_key_name(keys[-1])
    if final_vk is None:
        return HotkeyFormatErrorMessage(
            original_expression,
            # TODO localize
            'modifier key must have at least 1 modifier and exactly 1 normal key; '
            'found modifier key or unknown key "{0}" instead of a normal key',
            keys[-1]
        )
    modifier_vks: List[ModifierKeyCode] = []
    for kname in keys[:-1]:
        mvk = convert_modifier_key_name(kname)
        if mvk is None:
            return HotkeyFormatErrorMessage(
                original_expression,
                # TODO localize
                'modifier key must have at least 1 modifier and exactly 1 normal key; '
                'found normal key or unknown key "{0}" instead of a modifier',
                kname
            )
        modifier_vks.append(mvk)
    assert len(modifier_vks) >= 1
    return (modifier_vks, final_vk,)


def parse_key_sequence(
        original_expression: str, hotkey: str
) -> Union[Sequence[StandardKeyCode], HotkeyFormatErrorMessage]:
    """
    Parses a sequence of non-modifier keys.

    These are a simple list of key names separated by a '+'.
    """

    sequence_keys = hotkey.split('+')
    if not sequence_keys:
        return HotkeyFormatErrorMessage(
            original_expression,
            # TODO localize
            'key sequence must have at least 1 normal key'
        )
    sequence_vks: List[StandardKeyCode] = []
    for kname in sequence_keys:
        skv = convert_standard_key_name(kname)
        if skv is None:
            return HotkeyFormatErrorMessage(
                original_expression,
                # TODO localize
                'key sequence must have at least 1 normal key; '
                'found modifier key or unknown key "{0}" instead of a normal key',
                kname
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
