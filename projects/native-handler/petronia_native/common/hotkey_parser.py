"""
Parse a hotkey request string into combo sequences.
"""

from typing import List, Sequence, Dict, Set, Tuple, Union
from petronia_common.util import StdRet, UserMessage, join_errors, EMPTY_TUPLE
from petronia_common.util import i18n as _
from . import user_messages, handlers, hotkey_chain


class KeyMap:
    """Maps key codes to key characters.  Some keys can be aliases for multiple keys,
    such as 'shift' meaning either left or right shift key."""
    def get_key_aliases(self, code: int) -> Sequence[str]:
        """Get the UTF key aliases mapped to the key code."""
        raise NotImplementedError

    def get_codes_for_alias(self, key: str) -> Sequence[int]:
        """Get the key codes mapped to the given UTF key.  If there are no mappings,
        then this returns an empty list."""
        raise NotImplementedError

    def is_meta_code(self, code: int) -> bool:
        """Checks whether the code is a meta character (shift, ctrl, etc)"""
        raise NotImplementedError

    def get_meta_codes_for_alias(self, key: str) -> Sequence[int]:
        """Get the key code mapped to the given UTF key, but only if the key code is
        a meta-character."""
        ret: List[int] = []
        for code in self.get_codes_for_alias(key):
            if self.is_meta_code(code):
                ret.append(code)
        return ret

    def get_normal_codes_for_alias(self, key: str) -> Sequence[int]:
        """Get the key code mapped to the given UTF key, but only if the key code is
        not a meta-character."""
        ret: List[int] = []
        for code in self.get_codes_for_alias(key):
            if not self.is_meta_code(code):
                ret.append(code)
        return ret


class StaticKeyMap(KeyMap):
    """Maps key codes to key characters.  Some keys can be aliases for multiple keys,
    such as 'shift' meaning either left or right shift key."""
    __slots__ = ('__key_to_code', '__code_to_key', '__meta_keys')

    def __init__(
            self, *,
            key_to_code: Dict[str, Sequence[int]],
            code_to_key: Dict[int, Sequence[str]],
            meta_keys: Set[int],
    ) -> None:
        self.__key_to_code = key_to_code
        self.__code_to_key = code_to_key
        self.__meta_keys = meta_keys

    def get_key_aliases(self, code: int) -> Sequence[str]:
        return self.__code_to_key.get(code) or EMPTY_TUPLE

    def get_codes_for_alias(self, key: str) -> Sequence[int]:
        return self.__key_to_code.get(key) or EMPTY_TUPLE

    def is_meta_code(self, code: int) -> bool:
        return code in self.__meta_keys


def parse_bindings(
        master_sequence_type: str,
        master_sequence_keys: List[str],
        key_sequences: Sequence[Sequence[str]],
        keymap: KeyMap,
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

    problems = handlers.hotkey.BoundKeyProblems()

    # Valid sequence type keys are 'sequence' and 'meta'.
    # This currently only parses "meta".
    if master_sequence_type != 'meta':
        problems.master_problem = StdRet.pass_errmsg(
            user_messages.TRANSLATION_CATALOG,
            _(
                'This native handler currently only handles the "meta" key sequences; '
                'requested {name}.'
            ),
            name=master_sequence_type,
        )
        return (
            False, problems, {}, [],
        )

    valid = True
    sequence_names: Dict[str, Sequence[str]] = {}
    sequences: List[Tuple[Sequence[hotkey_chain.KeyCombo], str]] = []

    master_keys_res = parse_primary_master_sequence(master_sequence_keys, keymap)
    if master_keys_res.has_error:
        problems.master_problem = master_keys_res.forward()
        valid = False

    # Parse sequences
    for key_sequence in key_sequences:
        sequence_res = parse_sequence(key_sequence, keymap)
        if sequence_res.has_error:
            problems.sequence_problems[tuple(key_sequence)] = sequence_res.forward()
            valid = False
        elif master_keys_res.ok:
            # For a primary chain, these keys are down-then-up.  If an included code is a
            # modifier, then it needs to be included in the master keys.
            modifier_codes, std_codes, name = sequence_res.result
            modifiers = [*master_keys_res.result, *modifier_codes]
            combo = hotkey_chain.create_primary_chain(modifiers, std_codes)
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
        master_sequence_keys: List[str],
        keymap: KeyMap,
) -> StdRet[Sequence[hotkey_chain.ModifierKeyCode]]:
    """Parse a primary chain master key as a sequence of meta-keys.

    This returns a list of the keys to press.  If a key has multiple choices
    (say, lshift or rshift), then that is one of the internal lists."""

    errors: List[UserMessage] = []
    ret: List[hotkey_chain.ModifierKeyCode] = []

    for name in master_sequence_keys:
        codes = keymap.get_meta_codes_for_alias(name)
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


def parse_sequence(sequence: Sequence[str], keymap: KeyMap) -> StdRet[
    Tuple[
        Sequence[hotkey_chain.StandardKeyCode],
        Sequence[hotkey_chain.StandardKeyCode],
        str,
    ]
]:
    """Create a sequence of key codes, and the referencable name for the sequence"""
    sequence_name = ''
    modifier_codes: List[hotkey_chain.StandardKeyCode] = []
    std_codes: List[hotkey_chain.StandardKeyCode] = []
    errors: List[UserMessage] = []

    for name in sequence:
        name = name.strip()
        key_codes = keymap.get_codes_for_alias(name)
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
            if keymap.is_meta_code(key_codes[0]):
                modifier_codes.append(hotkey_chain.StandardKeyCode(key_codes[0]))
            else:
                std_codes.append(hotkey_chain.StandardKeyCode(key_codes[0]))

    if errors:
        return StdRet.pass_error(join_errors(*errors))
    return StdRet.pass_ok((modifier_codes, std_codes, sequence_name))
