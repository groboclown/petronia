
# type: ignore

"""
Unit tests for RWLock
"""

from typing import cast
import unittest
from ..hotkey_chain import (
    ACTION_PENDING,
    ACTION_CANCELLED,
    ACTION_COMPLETE,
    IGNORED,
    MAX_STANDARD_KEY_CODE,
    StatefulKeyCode,
    StandardKeyCode,
    KeyComboTree,
    HotKeyChain,
    combinations,
    create_stateful_key_code,
    create_primary_chain,
    create_modal_chain,
    modifier_key_permutations,
)


SKC_1 = cast(StatefulKeyCode, 1)
SKC_2 = cast(StatefulKeyCode, 2)
# SKC_3 = cast(StatefulKeyCode, 3)
# SKC_4 = cast(StatefulKeyCode, 4)
SKC_5 = cast(StatefulKeyCode, 5)

STK_0 = cast(StandardKeyCode, 0)
STK_1 = cast(StandardKeyCode, 1)
STK_2 = cast(StandardKeyCode, 2)
STK_3 = cast(StandardKeyCode, 3)
STK_4 = cast(StandardKeyCode, 4)
STK_5 = cast(StandardKeyCode, 5)
STK_MAX = cast(StandardKeyCode, MAX_STANDARD_KEY_CODE)


class KeyComboTreeTest(unittest.TestCase):
    """Tests for KeyComboTree"""
    def test_add_simple(self) -> None:
        """Add a simple, 1 key combo, ensure it works as expected, then add another."""
        tree = KeyComboTree()
        self.assertTrue(tree.add_child([SKC_1], 's'))
        self.assertEqual(
            tree.get(SKC_1),
            's'
        )
        self.assertIsNone(tree.get(SKC_5))

        self.assertTrue(tree.add_child([SKC_2], 't'))
        self.assertEqual(
            tree.get(SKC_1),
            's'
        )
        self.assertEqual(
            tree.get(SKC_2),
            't'
        )
        self.assertIsNone(tree.get(SKC_5))

    def test_add_chain(self) -> None:
        """Add a chain of keys."""
        tree = KeyComboTree()
        self.assertTrue(tree.add_child([SKC_1, SKC_2, SKC_1], 's'))
        child = tree.get(SKC_1)
        self.assertIsInstance(child, KeyComboTree)
        assert isinstance(child, KeyComboTree)  # nosec  # mypy required
        child = child.get(SKC_2)
        self.assertIsInstance(child, KeyComboTree)
        assert isinstance(child, KeyComboTree)  # nosec  # mypy required
        self.assertEqual(
            child.get(SKC_1),
            's',
        )

        # Additional deep tree
        self.assertTrue(tree.add_child([SKC_1, SKC_2, SKC_5], 'a', False))
        self.assertEqual(
            tree.get(SKC_1).get(SKC_2).get(SKC_1),
            's',
        )
        self.assertEqual(
            tree.get(SKC_1).get(SKC_2).get(SKC_5),
            'a',
        )

        # Override testing
        self.assertFalse(tree.add_child([SKC_1, SKC_2, SKC_1], 'x', False))
        self.assertEqual(
            tree.get(SKC_1).get(SKC_2).get(SKC_1),
            's',
        )
        self.assertFalse(tree.add_child([SKC_1, SKC_2, SKC_1], 'x', True))
        self.assertEqual(
            tree.get(SKC_1).get(SKC_2).get(SKC_1),
            'x',
        )

        # Change a branch to a leaf
        self.assertFalse(tree.add_child([SKC_1, SKC_2], 'y', False))
        self.assertEqual(
            tree.get(SKC_1).get(SKC_2).get(SKC_1),
            'x',
        )
        self.assertFalse(tree.add_child([SKC_1, SKC_2], 'y', True))
        self.assertEqual(
            tree.get(SKC_1).get(SKC_2),
            'y',
        )

        # Change a leaf to a branch
        self.assertFalse(tree.add_child([SKC_1, SKC_2, SKC_5], 'b', False))
        self.assertEqual(
            tree.get(SKC_1).get(SKC_2),
            'y',
        )
        self.assertFalse(tree.add_child([SKC_1, SKC_2, SKC_5], 'b', True))
        self.assertEqual(
            tree.get(SKC_1).get(SKC_2).get(SKC_5),
            'b',
        )

    def test_add_invalid(self) -> None:
        """Test out adding an invalid combo name."""
        tree = KeyComboTree()
        self.assertFalse(tree.add_child([], IGNORED))

    def test_repr(self) -> None:
        """Test repr"""
        tree = KeyComboTree()
        self.assertEqual('KeyComboTree()', repr(tree))
        tree.add_child([SKC_1, SKC_2, SKC_1], 'a')
        tree.add_child([SKC_1, SKC_2, SKC_5], 'b')
        self.assertEqual(
            "KeyComboTree('00:dn'=KeyComboTree('01:up'=KeyComboTree('00:dn'='a', '02:dn'='b')))",
            repr(tree),
        )


SK_1_DOWN = create_stateful_key_code(STK_1, True)
SK_1_UP = create_stateful_key_code(STK_1, False)
SK_2_DOWN = create_stateful_key_code(STK_2, True)
SK_2_UP = create_stateful_key_code(STK_2, False)
SK_3_DOWN = create_stateful_key_code(STK_3, True)
SK_3_UP = create_stateful_key_code(STK_3, False)
SK_4_DOWN = create_stateful_key_code(STK_4, True)
SK_4_UP = create_stateful_key_code(STK_4, False)


class CreateChainTest(unittest.TestCase):
    """Test the create chain functions."""
    def test_create_stateful_key_code(self) -> None:
        """create_stateful_key_code function"""
        self.assertEqual(
            create_stateful_key_code(STK_0, False),
            0,
        )
        self.assertEqual(
            create_stateful_key_code(STK_0, True),
            1,
        )
        self.assertEqual(
            create_stateful_key_code(STK_MAX, False),
            MAX_STANDARD_KEY_CODE << 1,
        )
        self.assertEqual(
            create_stateful_key_code(STK_MAX, True),
            (MAX_STANDARD_KEY_CODE << 1) | 1,
        )

    def test_combinations_1(self) -> None:
        """combinations function"""
        self.assertEqual(
            combinations([]),
            [],
        )
        self.assertEqual(
            combinations([1]),
            [[1]],
        )
        self.assertEqual(
            combinations([1, 2]),
            [[1, 2], [2, 1]],
        )

    def test_create_primary_chain_1(self) -> None:
        """create_primary_chain with just 1 modifier."""
        self.assertEqual(
            create_primary_chain([STK_1], [STK_2]).value,
            [[SK_1_DOWN, SK_2_DOWN]],
        )
        self.assertEqual(
            create_primary_chain([STK_1], [STK_2, STK_3]).value,
            [[SK_1_DOWN, SK_2_DOWN, SK_2_UP, SK_3_DOWN]],
        )

    def test_create_primary_chain_2(self) -> None:
        """create_primary_chain with just multiple modifiers."""
        self.assertEqual(
            create_primary_chain([STK_1, STK_2], [STK_3]).value,
            [
                [SK_1_DOWN, SK_2_DOWN, SK_3_DOWN],
                [SK_2_DOWN, SK_1_DOWN, SK_3_DOWN],
            ],
        )
        self.assertEqual(
            create_primary_chain([[STK_1, STK_2]], [STK_3]).value,
            [
                [SK_1_DOWN, SK_3_DOWN],
                [SK_2_DOWN, SK_3_DOWN]
            ],
        )
        self.assertEqual(
            create_primary_chain([[STK_1, STK_2], STK_3], [STK_4]).value,
            [
                [SK_1_DOWN, SK_3_DOWN, SK_4_DOWN],
                [SK_2_DOWN, SK_3_DOWN, SK_4_DOWN],
                [SK_3_DOWN, SK_1_DOWN, SK_4_DOWN],
                [SK_3_DOWN, SK_2_DOWN, SK_4_DOWN],
            ],
        )

    def test_create_primary_chain__errors(self) -> None:
        """create_primary_chain under bad pre-conditions."""
        self.assertEqual(
            ['modifiers list cannot be empty'],
            [m.debug() for m in create_primary_chain([], [STK_3]).error_messages()],
        )
        self.assertEqual(
            ['key sequence cannot be empty'],
            [m.debug() for m in create_primary_chain([STK_3], []).error_messages()],
        )

    def test_create_modal_chain_1(self) -> None:
        """create_modal_chain with simple modifiers."""
        self.assertEqual(
            create_modal_chain([STK_1], [STK_2], [STK_3]).value,
            [
                [SK_1_DOWN, SK_2_DOWN, SK_1_UP, SK_2_UP, SK_3_DOWN],
                [SK_1_DOWN, SK_2_DOWN, SK_2_UP, SK_1_UP, SK_3_DOWN],
            ],
        )

    def test_create_modal_chain__errors(self) -> None:
        """create_modal_chain with bad preconditions."""
        self.assertEqual(
            ['modifiers list cannot be empty'],
            [m.debug() for m in create_modal_chain([], [STK_0], [STK_1]).error_messages()],
        )
        self.assertEqual(
            ['modal key list cannot be empty'],
            [m.debug() for m in create_modal_chain([STK_0], [STK_1], []).error_messages()],
        )
        self.assertIsNone(create_modal_chain([STK_0], [], [STK_1]).error)


class MiscFunctionTest(unittest.TestCase):
    """Miscellaneous function tests."""
    def test_modifier_key_permutations(self) -> None:
        """Test different permutations of the keys."""
        self.assertEqual(
            modifier_key_permutations([STK_1]),
            [[1]],
        )
        self.assertEqual(
            modifier_key_permutations([STK_1, STK_2]),
            [[1, 2]],
        )
        self.assertEqual(
            modifier_key_permutations([[STK_1]]),
            [[1]],
        )
        self.assertEqual(
            modifier_key_permutations([[STK_1, STK_2]]),
            [[1], [2]],
        )
        self.assertEqual(
            modifier_key_permutations([[STK_1, STK_2], [STK_3, STK_4]]),
            [[1, 3], [2, 3], [1, 4], [2, 4]],
        )


class HotKeyChainTest(unittest.TestCase):
    """Test out the hotkey chain class."""

    def test_constructor_none(self) -> None:
        """Test a constructor with no initial setup."""
        hotkeys = HotKeyChain()
        action, bound = hotkeys.key_action(STK_1, True)
        self.assertEqual(IGNORED, action)
        self.assertIsNone(bound)

    def test_key_action_1(self) -> None:
        """A series of valid key actions."""
        hotkeys = HotKeyChain([
            ([
                [SK_1_DOWN, SK_2_DOWN, SK_2_UP],
                [SK_2_DOWN, SK_3_DOWN],
            ], 'a'),
            ([
                 [SK_1_DOWN, SK_3_DOWN],
                 [SK_2_DOWN, SK_1_DOWN],
             ], 'b'),

            # May not be allowed in the future.
            ([
                [SK_4_DOWN],
            ], 'c'),
        ])

        # First hotkey chain.
        self.assertEqual(hotkeys.key_action(STK_1, True), (ACTION_PENDING, {'a', 'b'}))
        self.assertEqual(hotkeys.key_action(STK_2, True), (ACTION_PENDING, {'a'}))
        self.assertEqual(hotkeys.key_action(STK_2, False), (ACTION_COMPLETE, ('a',)))

        # Alternate first hotkey chain.
        self.assertEqual(hotkeys.key_action(STK_2, True), (ACTION_PENDING, {'a', 'b'}))
        self.assertEqual(hotkeys.key_action(STK_3, True), (ACTION_COMPLETE, ('a',)))

        # Second hotkey chain.
        self.assertEqual(hotkeys.key_action(STK_1, True), (ACTION_PENDING, {'a', 'b'}))
        self.assertEqual(hotkeys.key_action(STK_3, True), (ACTION_COMPLETE, ('b',)))

        # Cancelled hotkey chain.
        self.assertEqual(hotkeys.key_action(STK_1, True), (ACTION_PENDING, {'a', 'b'}))
        self.assertEqual(hotkeys.key_action(STK_4, True), (ACTION_CANCELLED, None))

        # Single hotkey chain.
        self.assertEqual(hotkeys.key_action(STK_4, True), (ACTION_COMPLETE, ('c',)))
