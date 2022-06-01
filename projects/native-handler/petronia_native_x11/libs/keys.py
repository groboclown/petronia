"""Maps keys and codes.

Simple test:
>>> from petronia_native_x11.libs import keys, libxcb, ct_util, libc, libxcb_consts
>>> import ctypes
>>> xcb_lib = libxcb.LibXcb()
>>> c_lib = libc.LibC()
>>> conn = xcb_lib.xcb_connect(ct_util.NULL__c_char_p, ctypes.byref(ctypes.c_int(0)))
>>> keys.generate_keysym_table()
>>> keymap = keys.grab_keymap(xcb_lib, c_lib, conn)
"""

from typing import Dict, Set, Sequence
from petronia_common.util import EMPTY_TUPLE
from petronia_native.common import hotkey_parser
from .xcb_library import xcb, xcb_types, xcb_consts, keysyms_table
from . import ct_util, libc


def grab_keymap(
        xcb_lib: xcb.LibXcb,
        c_lib: libc.LibC,
        connection: xcb_types.XcbConnectionP,
) -> hotkey_parser.KeyMap:
    setup_p = xcb_lib.xcb_get_setup(connection)
    setup = setup_p.contents
    min_keycode = setup.min_keycode
    max_keycode = setup.max_keycode

    # get modifiers
    modifier_keycodes_p = xcb_lib.xcb_get_modifier_mapping_reply(
        connection,
        xcb_lib.xcb_get_modifier_mapping(connection),
        xcb_consts.NULL__XcbGenericErrorPP,
    )
    modifier_keycode_count = modifier_keycodes_p.contents.length
    modifier_keycodes_array = xcb_lib.xcb_get_modifier_mapping_keycodes(modifier_keycodes_p)

    meta_keys: Set[int] = set()
    for mod_idx in range(0, modifier_keycode_count):
        mod = ct_util.as_py_int(modifier_keycodes_array[mod_idx])
        if mod != 0:
            meta_keys.add(mod)
    c_lib.force_free(modifier_keycodes_p)

    # get keycodes to symbols
    keycode_count = ct_util.as_py_int(max_keycode) - ct_util.as_py_int(min_keycode) + 1
    request_cookie = xcb_lib.xcb_get_keyboard_mapping(
        connection,
        min_keycode,
        ct_util.as_uint8(keycode_count),
    )
    keyboard_mapping_p = xcb_lib.xcb_get_keyboard_mapping_reply(
        connection, request_cookie,
        # Should look at real error checking.
        xcb_consts.NULL__XcbGenericErrorPP,
    )
    keysym_array = xcb_lib.xcb_get_keyboard_mapping_keysyms(keyboard_mapping_p)
    keyboard_mapping = keyboard_mapping_p.contents
    keysym_count = ct_util.as_py_int(keyboard_mapping.length)
    keysyms_per_keycode = ct_util.as_py_int(keyboard_mapping.keysyms_per_keycode)
    keycode_count = keysym_count // keysyms_per_keycode

    key_to_code: Dict[str, Set[int]] = {}
    code_to_key: Dict[int, Sequence[str]] = {}

    keysym_idx = 0
    for keycode_idx in range(0, keycode_count):
        keycode = min_keycode + keycode_idx
        syms: Set[str] = set()
        for keysym_keycode_idx in range(0, keysyms_per_keycode):
            # Note, however, that this is not proper UTF-8 conversion.
            # A keysym is not a UTF character, and must be looked up separate from this.
            # See xkb utf32-to-keysym.
            keysym = keysym_array[keysym_idx]
            keysym_idx += 1
            key_names = keysym_to_str(keysym)
            syms.update(key_names)
            for key_name in key_names:
                keys = key_to_code.get(key_name)
                if keys is None:
                    keys = set()
                    key_to_code[key_name] = keys
                keys.add(keycode)
        code_to_key[keycode] = tuple(syms)
    c_lib.force_free(keyboard_mapping_p)

    return hotkey_parser.StaticKeyMap(
        key_to_code={
            k: tuple(v)
            for k, v in key_to_code.items()
        },
        code_to_key=code_to_key,
        meta_keys=meta_keys,
    )


def keysym_to_str(keysym: xcb_types.XcbKeysym) -> Sequence[str]:
    """Convert the key symbol to a character / string.
    This is slow."""
    sym = ct_util.as_py_int(keysym)

    res = _KEYSYM_TABLE.get(sym)
    if res:
        return res

    # Latin-1 characters
    #   mapped 1-to-1
    if (0x0020 <= sym <= 0x007e) or (0x00a0 <= sym <= 0x00ff):
        return (chr(sym).lower(),)
    # Unicode standard
    #   mapped + 0x01000000
    #   ... but Python can only handle 16 bit unicode.
    if 0x01000000 <= sym <= 0x0100ffff:
        return (chr(sym & 0x0ffffff).lower(),)
    res = _KEYSYM_TABLE.get(sym & 0xffff)
    if res:
        return res

    # In addition, vendor-specific KeySyms in the hexadecimal range
    #   0x11000000 to 0x1100FFFF are also keypad KeySyms.
    if 0x11000000 <= sym <= 0x1100ffff:
        sym = sym & 0xffff
        return (f'kp_v_{sym:x}',)

    print(f"[KEY] unknown keysym {sym:08x}")
    return EMPTY_TUPLE


_KEYSYM_TABLE: Dict[int, Sequence[str]] = {}


def generate_keysym_table() -> None:
    """Generate the keysym to symbol lookup table."""
    table: Dict[int, Set[str]] = {}
    for keysym, alias in keysyms_table.KEYSYM_LOOKUP:
        alias_list = table.get(keysym)
        if alias_list is None:
            alias_list = set()
            table[keysym] = alias_list
        alias_list.add(alias)

    _KEYSYM_TABLE.clear()
    for keysym, alias_list in table.items():
        _KEYSYM_TABLE[keysym] = tuple(alias_list)

    # Some special aliases.
    _KEYSYM_TABLE[0] = EMPTY_TUPLE  # NO_SYMBOL
    _KEYSYM_TABLE[ord(' ')] = ('space', 'spacebar', ' ')

    print(f"[KEY] Generated keysym table with {len(_KEYSYM_TABLE)} entries")
    # print("[KEY] keysyms: " + repr(_KEYSYM_TABLE.keys()))

# Latin characters are 1-to-1
# These occupy the range #x01000100 to #x0110FFFF and represent the ISO
# 10646 / Unicode characters U+0100 to U+10FFFF, respectively. The
# numeric value of a Unicode KEYSYM is the Unicode position of the
# corresponding character plus #x01000000. In the interest of backwards
# compatibility, clients should be able to process both the Unicode
# KEYSYM and the Legacy KEYSYM for those characters where both exist.
