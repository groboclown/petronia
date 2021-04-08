
# type: ignore

"""
Unit tests for RWLock
"""

import unittest
from ..hotkey_chain import (
    ACTION_PENDING,
    ACTION_CANCELLED,
    ACTION_COMPLETE,
    IGNORED,
    KeyComboTree,
    HotKeyChain,
    combinations,
    create_stateful_key_code,
    create_primary_chain,
    create_modal_chain,
    modifier_key_permutations,
)


class KeyComboTreeTest(unittest.TestCase):
    """Tests for KeyComboTree"""
    def test_add_simple(self) -> None:
        """Add a simple, 1 key combo, ensure it works as expected, then add another."""
        tree = KeyComboTree()
        self.assertTrue(tree.add_child([1], 's'))
        self.assertEqual(
            tree.get(1),
            's'
        )
        self.assertIsNone(tree.get(5))

        self.assertTrue(tree.add_child([2], 't'))
        self.assertEqual(
            tree.get(1),
            's'
        )
        self.assertEqual(
            tree.get(2),
            't'
        )
        self.assertIsNone(tree.get(5))

    def test_add_chain(self) -> None:
        """Add a chain of keys."""
        tree = KeyComboTree()
        self.assertTrue(tree.add_child([1, 2, 1], 's'))
        child = tree.get(1)
        self.assertIsInstance(child, KeyComboTree)
        if not isinstance(child, KeyComboTree):
            return
        child = child.get(2)
        self.assertIsInstance(child, KeyComboTree)
        if not isinstance(child, KeyComboTree):
            return
        self.assertEqual(
            child.get(1),
            's'
        )

    def test_add_invalid(self) -> None:
        """Test out adding an invalid combo name."""
        tree = KeyComboTree()
        try:
            tree.add_child([], IGNORED)
            self.fail('Did not fail assertion')
        except AssertionError:
            pass


SK_1_DOWN = create_stateful_key_code(1, True)
SK_1_UP = create_stateful_key_code(1, False)
SK_2_DOWN = create_stateful_key_code(2, True)
SK_2_UP = create_stateful_key_code(2, False)
SK_3_DOWN = create_stateful_key_code(3, True)
SK_3_UP = create_stateful_key_code(3, False)
SK_4_DOWN = create_stateful_key_code(4, True)
SK_4_UP = create_stateful_key_code(4, False)


class CreateChainTest(unittest.TestCase):
    """Test the create chain functions."""
    def test_create_stateful_key_code(self) -> None:
        """create_stateful_key_code function"""
        self.assertEqual(
            create_stateful_key_code(0, False),
            0
        )
        self.assertEqual(
            create_stateful_key_code(0, True),
            1
        )
        self.assertEqual(
            create_stateful_key_code(0xffff, False),
            0xffff << 1
        )
        self.assertEqual(
            create_stateful_key_code(0xffff, True),
            (0xffff << 1) | 1
        )

    def test_combinations_1(self) -> None:
        """combinations function"""
        self.assertEqual(
            combinations([]),
            []
        )
        self.assertEqual(
            combinations([1]),
            [[1]]
        )
        self.assertEqual(
            combinations([1, 2]),
            [[1, 2], [2, 1]]
        )


    def test_create_primary_chain_1(self) -> None:
        """create_primary_chain with just 1 modifier."""
        self.assertEqual(
            create_primary_chain([1], [2]),
            [[SK_1_DOWN, SK_2_DOWN]]
        )
        self.assertEqual(
            create_primary_chain([1], [2, 3]),
            [[SK_1_DOWN, SK_2_DOWN, SK_2_UP, SK_3_DOWN]]
        )

    def test_create_primary_chain_2(self) -> None:
        """create_primary_chain with just multiple modifiers."""
        self.assertEqual(
            create_primary_chain([1, 2], [3]),
            [
                [SK_1_DOWN, SK_2_DOWN, SK_3_DOWN],
                [SK_2_DOWN, SK_1_DOWN, SK_3_DOWN],
            ]
        )
        self.assertEqual(
            create_primary_chain([[1, 2]], [3]),
            [
                [SK_1_DOWN, SK_3_DOWN],
                [SK_2_DOWN, SK_3_DOWN]
            ]
        )
        self.assertEqual(
            create_primary_chain([[1, 2], 3], [4]),
            [
                [SK_1_DOWN, SK_3_DOWN, SK_4_DOWN],
                [SK_2_DOWN, SK_3_DOWN, SK_4_DOWN],
                [SK_3_DOWN, SK_1_DOWN, SK_4_DOWN],
                [SK_3_DOWN, SK_2_DOWN, SK_4_DOWN],
            ]
        )

    def test_create_modal_chain_1(self) -> None:
        """create_modal_chain with simple modifiers."""
        self.assertEqual(
            create_modal_chain([1], [2], [3]),
            [
                [SK_1_DOWN, SK_2_DOWN, SK_1_UP, SK_2_UP, SK_3_DOWN],
                [SK_1_DOWN, SK_2_DOWN, SK_2_UP, SK_1_UP, SK_3_DOWN],
            ]
        )


class MiscFunctionTest(unittest.TestCase):
    """Miscellaneous function tests."""
    def test_modifier_key_permutations(self) -> None:
        self.assertEqual(
            modifier_key_permutations([1]),
            [[1]]
        )
        self.assertEqual(
            modifier_key_permutations([1, 2]),
            [[1, 2]]
        )
        self.assertEqual(
            modifier_key_permutations([[1]]),
            [[1]]
        )
        self.assertEqual(
            modifier_key_permutations([[1, 2]]),
            [[1], [2]]
        )
        self.assertEqual(
            modifier_key_permutations([[1, 2], [3, 4]]),
            [[1, 3], [2, 3], [1, 4], [2, 4]]
        )



class HotKeyChainTest(unittest.TestCase):
    """Test out the hotkey chain class."""
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
        self.assertEqual(hotkeys.key_action(1, True), (ACTION_PENDING, {'a', 'b'}))
        self.assertEqual(hotkeys.key_action(2, True), (ACTION_PENDING, {'a'}))
        self.assertEqual(hotkeys.key_action(2, False), (ACTION_COMPLETE, ('a',)))

        # Alternate first hotkey chain.
        self.assertEqual(hotkeys.key_action(2, True), (ACTION_PENDING, {'a', 'b'}))
        self.assertEqual(hotkeys.key_action(3, True), (ACTION_COMPLETE, ('a',)))

        # Second hotkey chain.
        self.assertEqual(hotkeys.key_action(1, True), (ACTION_PENDING, {'a', 'b'}))
        self.assertEqual(hotkeys.key_action(3, True), (ACTION_COMPLETE, ('b',)))

        # Cancelled hotkey chain.
        self.assertEqual(hotkeys.key_action(1, True), (ACTION_PENDING, {'a', 'b'}))
        self.assertEqual(hotkeys.key_action(4, True), (ACTION_CANCELLED, None))

        # Single hotkey chain.
        self.assertEqual(hotkeys.key_action(4, True), (ACTION_COMPLETE, ('c',)))
