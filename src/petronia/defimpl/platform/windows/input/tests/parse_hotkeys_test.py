
"""
Test the parse_hotkeys functions
"""

import unittest
from ..parse_hotkeys import (
    HotkeyFormatErrorMessage,
    create_master_mkey_and_sequence_combo,
    create_master_modifier_hotkey_combo,
    create_master_modifier,
    create_master_mkey,
)
from ..keymap import STR_VK_MAP
from ....general.hotkey.hotkey_chain import create_stateful_key_code

_VK_LSUPER = STR_VK_MAP['lsuper']
_LSUPER_DOWN = create_stateful_key_code(_VK_LSUPER, True)
_LSUPER_UP = create_stateful_key_code(_VK_LSUPER, False)
_VK_LSHIFT = STR_VK_MAP['lshift']
_LSHIFT_DOWN = create_stateful_key_code(_VK_LSHIFT, True)
_LSHIFT_UP = create_stateful_key_code(_VK_LSHIFT, False)

_VK_A = STR_VK_MAP['a']
_A_DOWN = create_stateful_key_code(_VK_A, True)
_A_UP = create_stateful_key_code(_VK_A, False)
_VK_B = STR_VK_MAP['b']
_B_DOWN = create_stateful_key_code(_VK_B, True)
_B_UP = create_stateful_key_code(_VK_B, False)
_VK_C = STR_VK_MAP['c']
_C_DOWN = create_stateful_key_code(_VK_C, True)
_C_UP = create_stateful_key_code(_VK_C, False)

class ParseHotkeysTest(unittest.TestCase):
    def test_create_master_modifier_hotkey_combo_1(self) -> None:
        master = create_master_modifier('lsuper')
        self.assertEqual(
            master,
            [_VK_LSUPER]
        )
        assert not isinstance(master, HotkeyFormatErrorMessage)
        self.assertEqual(
            create_master_modifier_hotkey_combo(master, 'a'),
            [[_LSUPER_DOWN, _A_DOWN]]
        )
        self.assertEqual(
            create_master_modifier_hotkey_combo(master, 'lshift+a'),
            [
                [_LSUPER_DOWN, _LSHIFT_DOWN, _A_DOWN],
                [_LSHIFT_DOWN, _LSUPER_DOWN, _A_DOWN],
            ]
        )


    def test_create_master_mkey_and_sequence_combo_1(self) -> None:
        master = create_master_mkey('lsuper+a')
        self.assertEqual(
            master,
            ([_VK_LSUPER], _VK_A,)
        )
        assert not isinstance(master, HotkeyFormatErrorMessage)
        self.assertEqual(
            create_master_mkey_and_sequence_combo(master[0], master[1], 'b'),
            [
                [_LSUPER_DOWN, _A_DOWN, _LSUPER_UP, _A_UP, _B_DOWN],
                [_LSUPER_DOWN, _A_DOWN, _A_UP, _LSUPER_UP, _B_DOWN],
            ]
        )



    def test_create_master_modifier_hotkey_combo_fail_1(self) -> None:
        master = create_master_modifier('lsuper')
        self.assertEqual(master, [_VK_LSUPER])
        assert not isinstance(master, HotkeyFormatErrorMessage)
        val = create_master_modifier_hotkey_combo(master, 'a+b')
        self.assertIsInstance(val, HotkeyFormatErrorMessage)
        assert isinstance(val, HotkeyFormatErrorMessage)
        self.assertEqual(val.hotkey, 'a+b')
        self.assertEqual(val.err_args, ('a',))
