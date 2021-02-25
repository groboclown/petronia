"""
Hotkey processing.

The system should allow for only one type of chain to be used at a time.
"""

from typing import Dict, List, Tuple, Sequence, Iterable, Union, Optional, NewType, cast
from petronia_common.util import StdRet, T
from petronia_common.util import i18n as _
from petronia_native.common.user_messages import TRANSLATION_CATALOG


# The platform-specific integer representation of the key press.  It's up to
# the platform to understand whether this is a low-level "scan code" (the key
# position on the keyboard) or a "virtual key code" (a keyboard layout
# translated to a common set of characters).
# The sequence of numbers is for the situation where a user's requested key
# can be one of a multiple of keys (e.g. left vs. right shift key)
StandardKeyCode = NewType('StandardKeyCode', int)
ModifierKeyCode = Union[StandardKeyCode, Sequence[StandardKeyCode]]
KeyCode = Union[ModifierKeyCode, StandardKeyCode]

# Up or down state + the key
# Internally, this is (keycode << 1) | (key_down ? 1 : 0)
StatefulKeyCode = NewType('StatefulKeyCode', int)

# A universal collection of key interpretations for matching a hotkey
# definition.
KeyCombo = Sequence[StatefulKeyCode]


class KeyComboTree:
    """An internal representation of the list of possible keys.  This forms
    a tree of possible results.  Using a tree represented by dictionaries
    is a bit less memory efficient, but prevents the system from having to
    construct new objects on key press."""
    __slots__ = ('children',)
    children: Dict[StatefulKeyCode, Union[str, 'KeyComboTree']]

    def __init__(self) -> None:
        self.children = {}

    def get(self, key: StatefulKeyCode) -> Union[str, 'KeyComboTree', None]:
        """Get the leaf or child tree for the given key-press, or None if no such child."""
        return self.children.get(key, None)

    def leaves(self, store: Optional[List[str]] = None) -> Sequence[str]:
        """All the leaf node values from this point, which are the strings."""
        ret: List[str]
        if store is None:
            ret = []
        else:
            ret = store
        for child in self.children.values():
            if isinstance(child, str):
                ret.append(child)
            else:
                child.leaves(ret)
        return ret

    def add_child(self, keys: KeyCombo, name: str, override: bool = False) -> bool:
        """
        return `True` if the key was added without anything else present, or
        `False` if something else already registered the key combo.  If
        `override` is set, then the new child is added regardless of the
        return value.
        """
        if keys:
            key0: StatefulKeyCode = keys[0]
            key1: Sequence[StatefulKeyCode] = keys[1:]
            if key1:
                if key0 not in self.children:
                    self.children[key0] = KeyComboTree()
                child = self.children[key0]
                if isinstance(child, str):
                    # something else already registered it
                    if override:
                        tree = KeyComboTree()
                        tree.add_child(key1, name, override)
                        self.children[key0] = tree
                    return False

                return child.add_child(key1, name, override)
            # End of the key chain.
            if key0 in self.children:
                if override:
                    self.children[key0] = name
                return False
            self.children[key0] = name
            return True
        return False

    def __repr__(self) -> str:
        # Slow, but consistent and works.  But then, repr(x) should really only be done for
        # debugging or displaying messages, which is itself slow.
        kids = []
        for key, val in sorted(list(self.children.items()), key=lambda x: x[0]):
            nks = f"{(key >> 1) & 0xff:02x}:{key & 1 == 0 and 'up' or 'dn'}"
            kids.append(repr(nks) + '=' + repr(val))
        return "KeyComboTree({0})".format(', '.join(kids))


ACTION_PENDING = 1
ACTION_CANCELLED = 2
ACTION_COMPLETE = 3
IGNORED = 0

MIN_STANDARD_KEY_CODE = 0
MAX_STANDARD_KEY_CODE = 0xffffff


def create_stateful_key_code(standard_key_code: StandardKeyCode, is_down: bool) -> StatefulKeyCode:
    """Helper to construct the key code for the stateful chain.  The
    standard_key_code value MUST be in the range [0, 0xffffff]."""
    assert MIN_STANDARD_KEY_CODE <= standard_key_code <= MAX_STANDARD_KEY_CODE  # nosec
    down_i = 1 if is_down else 0
    return cast(StatefulKeyCode, (standard_key_code << 1) | down_i)


def create_primary_chain(
        modifiers: Sequence[ModifierKeyCode], key_sequence: Sequence[StandardKeyCode],
) -> StdRet[Sequence[KeyCombo]]:
    """
    Primary chain type: the primary modifiers must remain down for the chain
    to work.  Releasing the primary causes the chain to stop.  Each key in the
    key_sequence must be pressed and released before the next one is handled.

    The chain returned is a collection of all possible chains that match this
    request.
    """
    # Key down for each of the modifiers, in any order, followed by the key sequence
    # down-then-up.  This is combinations.  The sequence does not require releasing
    # the modifiers to trigger it.
    if not modifiers:
        return StdRet.pass_errmsg(
            TRANSLATION_CATALOG,
            _('modifiers list cannot be empty'),
        )
    if not key_sequence:
        return StdRet.pass_errmsg(
            TRANSLATION_CATALOG,
            _('key sequence cannot be empty'),
        )
    ret: List[List[StatefulKeyCode]] = []
    for combo in modifier_key_combinations(modifiers):
        # These must be pressed to start.
        key_list = [create_stateful_key_code(key, True) for key in combo]
        for key in key_sequence[:-1]:
            # Press then release.
            key_list.append(create_stateful_key_code(key, True))
            key_list.append(create_stateful_key_code(key, False))
        # The last key just needs to be pressed once.
        key_list.append(create_stateful_key_code(key_sequence[-1], True))
        ret.append(key_list)
    return StdRet.pass_ok(ret)


def create_modal_chain(
        initial_modifiers: Sequence[ModifierKeyCode], initial_keys: Sequence[StandardKeyCode],
        modal_keys: Sequence[StandardKeyCode],
) -> StdRet[Sequence[KeyCombo]]:
    """
    Modal, like screen or tmux.  Pressing the initial key sequence causes the
    rest to be checked.  Those initial keys must all be down together, then released
    in any order,

    The chain returned is a collection of all possible chains that match this
    request.
    """
    # initial = create_primary_chain(initial_modifiers, initial_keys)
    # Can't just reuse the previous one.  Some combination of the modifiers
    # may include an optional set (e.g. "shift" to represent left or right shift),
    # and just arbitrarily releasing any of those isn't right; instead, it must be
    # the one associated with the mapping.
    # All the modifiers must be pressed first in any order, then the initial keys pressed
    # in any order.
    # Additionally, the key release must be done in any order for any of the initial keys.
    if not initial_modifiers:
        return StdRet.pass_errmsg(
            TRANSLATION_CATALOG,
            _('modifiers list cannot be empty'),
        )
    if not modal_keys:
        return StdRet.pass_errmsg(
            TRANSLATION_CATALOG,
            _('modal key list cannot be empty'),
        )

    # List of the initial modifier + keys, and a list of the modifiers that must be released
    ret: List[List[StatefulKeyCode]] = []
    for combo in combinations(initial_modifiers):
        for modifier_key_list in modifier_key_permutations(combo):
            for init_key_list in combinations(initial_keys):
                release_combos = combinations(list(modifier_key_list) + list(init_key_list))
                for rcombo in release_combos:
                    rlist: List[StatefulKeyCode] = []
                    # All the modifiers must be pressed down
                    for key in modifier_key_list:
                        rlist.append(create_stateful_key_code(key, True))
                    # Then all the initial keys must be pressed down
                    for key in init_key_list:
                        rlist.append(create_stateful_key_code(key, True))
                    # Then they must all be released
                    for key in rcombo:
                        rlist.append(create_stateful_key_code(key, False))
                    ret.append(rlist)

    for key in modal_keys[:-1]:
        # There is guaranteed to be at least one key in the return list.
        for key_list in ret:  # pragma no cover
            key_list.append(create_stateful_key_code(key, True))
            key_list.append(create_stateful_key_code(key, False))
    # The last key does not need to be released.
    # There is guaranteed to be at least one key in the return list because of the preconditions.
    for key_list in ret:  # pragma no cover
        key_list.append(create_stateful_key_code(modal_keys[-1], True))

    return StdRet.pass_ok(ret)


class HotKeyChain:
    """
    Keeps track of the current hotkey press progress.

    This doesn't maintain any kind of key up / key down state.  Hotkeys used
    by this *must* follow the convention of press modifier then associated
    keys.  It won't work if they user performs one hotkey combo then tries
    another without releasing the modifier keys.

    Because this doesn't maintain down-state, once a hotkey sequence is pressed,
    down state is forgotten.  This means the technique for pressing a modifier then
    multiple sequences doesn't work (say, super+left).
    """
    __slots__ = ('_root_combos', '_active_combos',)
    _active_combos: Optional[KeyComboTree]

    def __init__(
            self, chain_commands: Optional[List[Tuple[Sequence[KeyCombo], str]]] = None
    ) -> None:
        self._root_combos = KeyComboTree()
        self._active_combos = None

        if chain_commands is not None:
            self.set_key_chains(chain_commands)

    def set_key_chains(self, chain_commands: List[Tuple[Sequence[KeyCombo], str]]) -> None:
        """Set all the hotkey combinations."""
        combos = KeyComboTree()
        for key_list, name in chain_commands:
            for keys in key_list:
                combos.add_child(keys, name, True)
        # print("Set key chain to " + repr(combos))

        # Change the variable in a single command.
        self._root_combos = combos
        self.reset()

    def reset(self) -> None:
        """Reset any active hotkey check."""
        self._active_combos = None

    def key_action(
            self, key_code: StandardKeyCode, is_down: bool,
    ) -> Tuple[int, Optional[Iterable[str]]]:
        """
        Handle the key action.  Note that this MUST be done in-thread when
        the event happens, due to the ordering nature of key press, and how
        Petronia events are not guaranteed to be well-ordered.

        :param is_down:
        :param key_code:
        :return: IGNORED if the key should be passed through,
            ACTION_PENDING if the key should be blocked from passing to
            another application, but does not complete an action,
            ACTION_CANCELLED if the key doesn't continue the current
            hotkey chain, or the action name to run.
        """

        # Construct the stateful key code
        key = create_stateful_key_code(key_code, is_down)

        if self._active_combos:
            # In the middle of handling a hotkey.
            next_part = self._active_combos.get(key)
            if isinstance(next_part, str):
                self._active_combos = None
                return ACTION_COMPLETE, (next_part,)
            if isinstance(next_part, KeyComboTree):
                self._active_combos = next_part
                return ACTION_PENDING, set(next_part.leaves())
            # Not a known key combo.
            self._active_combos = None
            return ACTION_CANCELLED, None

        next_part = self._root_combos.get(key)
        if isinstance(next_part, str):
            # A one-key hotkey.  Shouldn't be allowed, but it is for now.
            return ACTION_COMPLETE, (next_part,)
        if isinstance(next_part, KeyComboTree):
            # Start a combo.
            # print("Starting hotkey combo " + repr(next_part))
            self._active_combos = next_part
            return ACTION_PENDING, set(next_part.leaves())

        # It wasn't a known combo.
        return IGNORED, None


def modifier_key_combinations(
        modifiers: Sequence[ModifierKeyCode]
) -> Sequence[List[StandardKeyCode]]:
    """
    Find all the combinations of the modifier keys, and expand out the
    alternates of modifier keys.
    """
    ret: List[List[StandardKeyCode]] = []
    for combo in combinations(modifiers):
        for perm in modifier_key_permutations(combo):
            ret.append(perm)
    return ret


def modifier_key_permutations(
        modifiers: Sequence[ModifierKeyCode]
) -> Sequence[List[StandardKeyCode]]:
    """
    Splits the list of modifiers into sets of keys, expanding out the possible values of modifiers.

    Each item in the list is:
        0: ordered list of keys pressed
        1: set of modifiers selected, one per modifier group.
    """
    ret: List[List[StandardKeyCode]] = [[]]
    for mkey in modifiers:
        if isinstance(mkey, int):
            for slist in ret:
                slist.append(cast(StandardKeyCode, mkey))
        else:
            new_ret: List[List[StandardKeyCode]] = []
            # Create a copy of ret, once per key possibility
            for key in mkey:
                for slist in ret:
                    new_slist = list(slist)
                    new_slist.append(key)
                    new_ret.append(new_slist)
            ret = new_ret
    return ret


def combinations(src_elements: Sequence[T]) -> Sequence[List[T]]:
    """
    Find all complete combinations of the source elements (each uses all
    source elements).
    """
    if not src_elements:
        return []

    ret: List[List[T]] = []
    source_size = len(src_elements)
    last_index = source_size - 1
    index_stack: List[int] = [-1]  # weird initial state to handle the looping
    while index_stack:
        if len(index_stack) > source_size:
            # Completed filling up the stack, so this is the end of the
            # list.
            data: List[T] = []
            for idx in range(0, source_size):
                data.append(src_elements[index_stack[idx]])
            # ... could also yield ...
            ret.append(data)
            # Remove that last marker...
            index_stack.pop()

            # An internal verification, to make sure the algorithm is working right.
            assert len(index_stack) == source_size  # nosec

            # Continue the process as usual.
        next_idx = index_stack.pop() + 1
        while next_idx in index_stack and next_idx <= last_index:
            next_idx += 1
        if next_idx <= last_index:
            # Advance this item to the next value,
            # and continue to the one after it.
            index_stack.append(next_idx)
            index_stack.append(-1)
        # else exceeded all possible values this position can take.
        # This implicit else will cause a pop-out to the higher stack level.
    return ret
