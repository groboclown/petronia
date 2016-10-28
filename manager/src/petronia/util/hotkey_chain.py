
IGNORED = None
ACTION_PENDING = 1

# Bigger than necessary
_MAX_VK_KEY = 0x200
_VK_KEY_MASK = 0x1ff
_CURRENT_KEY_STATE = [False] * _MAX_VK_KEY
_MODIFIERS = set()


def on_key_hook(vk_code, is_down):
    """
    Module-wide storage for the current key state.

    :param vk_code:
    :param is_down:
    :return: True if it's a recognized key, False if it isn't known.
    """
    if 0 <= vk_code <= _MAX_VK_KEY:
        _CURRENT_KEY_STATE[vk_code] = is_down
        if vk_code in _MODIFIER_KEYS:
            if is_down:
                _MODIFIERS.add(vk_code)
            else:
                _MODIFIERS.remove(vk_code)
        return True
    return False


class KeyOverride(object):
    """
    Captures all key presses.  Certain keys map to actions.

    All keys are simple (straight up keys; modifiers are considered keys).
    One key per action.
    """
    def __init__(self, key_commands=None):
        self.__keys = {}

        if key_commands is not None:
            self.set_key_actions(key_commands)

    def set_key_actions(self, actions):
        # TODO in the future we may allow "shift+left" type keys here.
        # The implementation in key_action would just check the _MODIFIERS
        # state.
        new_key_actions = {}
        for key_action in actions:
            key = key_action[0].strip().lower()
            if key in VK_ALIASES:
                for k in VK_ALIASES[key]:
                    if k in MODIFIERS:
                        # TODO better error / warning
                        # Note use of user's value "key", rather than internal "k"
                        print("CONFIG ERROR: Simple keys are not allowed to be modifiers: {0}".format(key))
                    elif k in STR_VK_MAP:
                        # print("DEBUG KeyOverride: assigning {0} = `{1}`".format(hex(STR_VK_MAP[k]), key_action[1]))
                        new_key_actions[STR_VK_MAP[k]] = key_action[1]
                    else:
                        # TODO better error / warning
                        print("ERROR IN SETUP: alias {0} not in vk map".format(k))
            elif key in MODIFIERS:
                # TODO better error / warning
                print("CONFIG ERROR: Simple keys are not allowed to be modifiers: {0}".format(key))
            elif key in STR_VK_MAP:
                new_key_actions[STR_VK_MAP[key]] = key_action[1]
            else:
                # TODO better error / warning
                print("CONFIG ERROR: Simple key not a known key: {0}".format(key))
        self.__keys = new_key_actions

    def reset(self):
        pass

    def key_action(self, vk_code, is_down):
        if vk_code in _MODIFIER_KEYS:
            # Ignore all modifier keys, so the "release" from a mode switch works right.
            # This ties in with modifiers not allowed as simple keys.
            return IGNORED
        if not is_down and vk_code in self.__keys:
            return self.__keys[vk_code]
        # Prevent all other keys from working
        return ACTION_PENDING


class HotKeyChain(object):
    """
    Takes a keypress, and manages the state of the keys.
    It stores a list of key chains to action pairs.

    There should be one of these per system "mode".
    """

    def __init__(self, chain_commands=None):
        self.__combos = []

        # The modifiers which are down and associated with the active combos
        self.__active_modifiers = []

        # The previous key in the combo chain; we're waiting for it to be off.
        self.__active_key = None

        # The active combo chains.  Index 0 in each item is the remaining list
        # of key down actions to look for ([0] meaning the next one).  Index 1
        # in each item is the command to return.
        self.__active_combos = []

        # Set to True to prevent the OS shell from using the "windows" key.
        self.block_win_key = False

        if chain_commands is not None:
            self.set_key_chains(chain_commands)

    def set_key_chains(self, chain_commands):
        assert hasattr(chain_commands, '__iter__')

        combos = []
        for chain_command in chain_commands:
            assert len(chain_command) == 2
            keys = parse_combo_str(chain_command[0])
            if len(keys) > 0:
                # We store modifiers a little differently.
                # Rather than having a list of lists, which must be
                # carefully examined, we instead construct the
                # permutations of the keys, and store each of those as
                # their own combo.
                permutation_keys = []
                _key_permutations(keys[0], 0, [], permutation_keys)
                for perm in permutation_keys:
                    # print("DEBUG Combo {0} + {1} => {2}".format(perm, keys[1:], chain_command[1]))
                    combos.append((perm, keys[1:], chain_command[1]))

        # Change the variable in a single command.
        self.__combos = combos
        self.reset()

    def reset(self):
        self.__active_combos = []
        self.__active_modifiers = []
        self.__active_key = None

    def key_action(self, vk_code, is_down):
        """

        :param is_down:
        :param vk_code:
        :return: IGNORED if the key should be passed through,
            ACTION_PENDING if the key should be blocked from passing to
            another application, but does not complete an action, or
            a string for the action to run.
        """
        if _MODIFIERS == self.__active_modifiers:
            if self.__active_key is None or not _CURRENT_KEY_STATE[self.__active_key]:
                # The previous key is no longer down.
                self.__active_key = None

                next_combos = []
                for ac in self.__active_combos:
                    if vk_code in ac[0][0]:
                        ac[0].pop(0)
                        if len(ac[0]) <= 0:
                            # We have our key
                            command = ac[1]
                            self.reset()
                            return command
                        next_combos.append(ac)
                if len(next_combos) > 0:
                    self.__active_key = vk_code
                    self.__active_combos = next_combos
                    return ACTION_PENDING
                elif is_down:
                    # A new key was pressed, which isn't a key in a pending
                    # combo.  Reset our hot keys, and return an ignored.
                    self.reset()
            # else, the previous active key is still down; wait for it
            # to come up.
        else:
            # Discover which combo matches the modifiers.
            self.reset()
            new_active = []
            for combo in self.__combos:
                if combo[0] == _MODIFIERS:
                    new_active.append((list(combo[1]), combo[2]))
            if len(new_active) > 0:
                self.__active_key = None
                self.__active_combos = new_active
                self.__active_modifiers = set(_MODIFIERS)
                # We still pass on the modifiers to the OS, just in case it's not
                # a match.

        if self.block_win_key and vk_code in _WIN_KEYS:
            return ACTION_PENDING
        return IGNORED


def parse_combo_str(chain_description):
    """
    Special compact form of the string.  For each key combo part,
    we make a "string" of the only VK codes that must be "down" in
    order to trigger the next part of the chain.

    The format is "primary + primary + ... + key, key, key, ..."

    :param chain_description:
    :return: list of aliased combo lists.  So, the return will be
        [primary, key1, key2, ...], where "primary" are the primary
        keys that must be pressed through the whole action.  Key1 and
        key2 (and so on) are the keys that must be pressed and released
        in order (the last key will respond on key down).  Each key
        in the list is itself a list of alternate keys.
    """
    assert isinstance(chain_description, str)

    key_parts = chain_description.split(",")
    # Parse the primary first.  These are separated by "+".
    # The last key in the list is the "non-always-down" key,
    # meaning it's the first in the key chain.
    primary_list = []
    primary_keys = key_parts[0].split("+")
    secondary_keys = [primary_keys[-1]]
    secondary_keys.extend(key_parts[1:])
    for key_text in primary_keys[:-1]:
        primary_key = []
        key_text = key_text.strip().lower()
        if key_text in VK_ALIASES:
            for k in VK_ALIASES[key_text]:
                if k in STR_VK_MAP:
                    if k in MODIFIERS:
                        primary_key.append(STR_VK_MAP[k])
                    else:
                        # TODO better error / warning
                        print("CONFIG ERROR: Primary key not a modifier {0}".format(k))
                else:
                    print("ERROR IN SETUP: alias {0} not in vk map".format(k))
        elif key_text in STR_VK_MAP:
            if key_text in MODIFIERS:
                primary_key.append(STR_VK_MAP[key_text])
            else:
                # TODO better error / warning
                print("CONFIG ERROR: Primary key not a modifier {0}".format(key_text))
        else:
            # TODO better error / warning
            print("CONFIG ERROR: unknown key code {0}".format(key_text))
        if len(primary_key) > 0:
            primary_list.append(primary_key)

    chain = [primary_list]

    for key_text in secondary_keys:
        key = []
        key_text = key_text.strip().lower()
        if key_text in VK_ALIASES:
            for k in VK_ALIASES[key_text]:
                if k in STR_VK_MAP:
                    if k in MODIFIERS:
                        # TODO better error / warning
                        print("CONFIG ERROR: secondary key is a modifier {0}".format(k))
                    else:
                        key.append(STR_VK_MAP[k])
                else:
                    print("ERROR IN SETUP: alias {0} not in vk map".format(k))
        elif key_text in STR_VK_MAP:
            if key_text in MODIFIERS:
                # TODO better error / warning
                print("CONFIG ERROR: secondary key is a modifier {0}".format(key_text))
            else:
                key.append(STR_VK_MAP[key_text])
        else:
            # TODO better error / warning
            print("CONFIG ERROR: unknown key code {0}".format(key_text))
        if len(key) > 0:
            chain.append(key)
    return chain


def _key_permutations(key_alt_list, alt_index, current_list, final_list):
    """
    Takes a list of key alternates ([ [k1a, k1b, ...], [k2a, k2b, ...], ...])
    and transforms this into the

    :param key_alt_list:
    :return:
    """
    for key in key_alt_list[alt_index]:
        next_list = list(current_list)
        next_list.append(key)
        if alt_index + 1 >= len(key_alt_list):
            final_list.append(set(next_list))
        else:
            _key_permutations(key_alt_list, alt_index + 1, next_list, final_list)


# Built-in alias VK keys for user-specified keys
VK_ALIASES = {
    "win": ["lwin", "rwin"],
    "shift": ["lshift", "rshift"],
    "control": ["lcontrol", "rcontrol"],
    "alt": ["lalt", "ralt"],
    "menu": ["lmenu", "rmenu"],
}


# Set of all recognized modifiers
MODIFIERS = {
    "shift",
    "lshift",
    "rshift",
    "control",
    "lcontrol",
    "rcontrol",
    "alt",
    "lalt",
    "ralt",
    "lwin",
    "rwin",
    "lmenu",
    "rmenu",
    "apps",
    "caps-lock",
}

# https://msdn.microsoft.com/en-us/library/windows/desktop/dd375731(v=vs.85).aspx
STR_VK_MAP = {
    "lmb": 0x01,                  # VK_LBUTTON  Left mouse button
    "rmb": 0x02,                  # VK_RBUTTON  Right mouse button
    "break": 0x03,                # VK_CANCEL   Control-break processing
    "mmb": 0x04,                  # VK_MBUTTON  Middle mouse button (three-button mouse)
    "x1mb": 0x05,                 # VK_XBUTTON1 X1 mouse button
    "x2mb": 0x06,                 # VK_XBUTTON2 X2 mouse button
    "x3mb": 0x07,                 # -           Undefined
    "back": 0x08,                 # VK_BACK     BACKSPACE key
    "backspace": 0x08,            # VK_BACK     BACKSPACE key
    "tab": 0x09,                  # VK_TAB      TAB key
    # - 0x0A-0B Reserved
    "clear": 0x0C,                # VK_CLEAR    CLEAR key
    "return": 0x0D,               # VK_RETURN   ENTER key
    "enter": 0x0D,                # VK_RETURN   ENTER key
    "cr": 0x0D,                   # VK_RETURN   ENTER key
    "lf": 0x0D,                   # VK_RETURN   ENTER key
    # - 0x0E-0F Undefined

    # These VK keys don't seem to get generated by the global key handler;
    # instead, the more low-level (lcontrol, rcontrol, etc) ones are.
    "shift": 0x10,                # VK_SHIFT    SHIFT key
    "sft": 0x10,                  # VK_SHIFT    SHIFT key
    "control": 0x11,              # VK_CONTROL  CTRL key
    "ctr": 0x11,                  # VK_CONTROL  CTRL key
    "menu": 0x12,                 # VK_MENU     ALT key
    "alt": 0x12,                  # VK_MENU     ALT key

    "pause": 0x13,                # VK_PAUSE    PAUSE key
    "caps-lock": 0x14,            # VK_CAPITAL  CAPS LOCK key
    "kana": 0x15,                 # VK_KANA     IME Kana mode
    "hanguel": 0x15,              # VK_HANGUEL  IME Hanguel mode (maintained for compatibility; use VK_HANGUL)
    "hangul": 0x15,               # VK_HANGUL   IME Hangul mode
    # - 0x16 Undefined
    "junja": 0x17,                # VK_JUNJA    IME Junja mode
    "final": 0x18,                # VK_FINAL    IME final mode
    "hanja": 0x19,                # VK_HANJA    IME Hanja mode
    "kanji": 0x19,                # VK_KANJI    IME Kanji mode
    # 0x1A - Undefined
    "escape": 0x1B,               # VK_ESCAPE    ESC key
    "esc": 0x1B,                  # VK_ESCAPE    ESC key
    "convert": 0x1C,              # VK_CONVERT    IME convert
    "nonconvert": 0x1D,           # VK_NONCONVERT    IME nonconvert
    "accept": 0x1E,               # VK_ACCEPT    IME accept
    "modechange": 0x1F,           # VK_MODECHANGE    IME mode change request
    "space": 0x20,                # VK_SPACE    SPACEBAR
    "prior": 0x21,                # VK_PRIOR    PAGE UP key
    "pgup": 0x21,                 # VK_PRIOR    PAGE UP key
    "pageup": 0x21,               # VK_PRIOR    PAGE UP key
    "next": 0x22,                 # VK_NEXT    PAGE DOWN key
    "pgdn": 0x22,                 # VK_NEXT    PAGE DOWN key
    "pagedown": 0x22,             # VK_NEXT    PAGE DOWN key
    "end": 0x23,                  # VK_END    END key
    "home": 0x24,                 # VK_HOME    HOME key
    "left": 0x25,                 # VK_LEFT    LEFT ARROW key
    "up": 0x26,                   # VK_UP    UP ARROW key
    "right": 0x27,                # VK_RIGHT    RIGHT ARROW key
    "down": 0x28,                 # VK_DOWN    DOWN ARROW key
    "select": 0x29,               # VK_SELECT    SELECT key
    "print": 0x2A,                # VK_PRINT    PRINT key
    "execute": 0x2B,              # VK_EXECUTE    EXECUTE key
    "snapshot": 0x2C,             # VK_SNAPSHOT    PRINT SCREEN key
    "insert": 0x2D,               # VK_INSERT    INS key
    "delete": 0x2E,               # VK_DELETE    DEL key
    "del": 0x2E,                  # VK_DELETE    DEL key
    "help": 0x2F,                 # VK_HELP    HELP key
    "lwin": 0x5B,                 # VK_LWIN    Left Windows key (Natural keyboard)
    "rwin": 0x5C,                 # VK_RWIN    Right Windows key (Natural keyboard)
    "apps": 0x5D,                 # VK_APPS    Applications key (Natural keyboard)
    # 0x5E - Reserved
    "sleep": 0x5F,                # VK_SLEEP    Computer Sleep key
    "numpad0": 0x60,              # VK_NUMPAD0    Numeric keypad 0 key
    "numpad1": 0x61,              # VK_NUMPAD1    Numeric keypad 1 key
    "numpad2": 0x62,              # VK_NUMPAD2    Numeric keypad 2 key
    "numpad3": 0x63,              # VK_NUMPAD3    Numeric keypad 3 key
    "numpad4": 0x64,              # VK_NUMPAD4    Numeric keypad 4 key
    "numpad5": 0x65,              # VK_NUMPAD5    Numeric keypad 5 key
    "numpad6": 0x66,              # VK_NUMPAD6    Numeric keypad 6 key
    "numpad7": 0x67,              # VK_NUMPAD7    Numeric keypad 7 key
    "numpad8": 0x68,              # VK_NUMPAD8    Numeric keypad 8 key
    "numpad9": 0x69,              # VK_NUMPAD9    Numeric keypad 9 key
    "multiply": 0x6A,             # VK_MULTIPLY    Multiply key
    "add": 0x6B,                  # VK_ADD    Add key
    "separator": 0x6C,            # VK_SEPARATOR    Separator key
    "subtract": 0x6D,             # VK_SUBTRACT    Subtract key
    "decimal": 0x6E,              # VK_DECIMAL    Decimal key
    "divide": 0x6F,               # VK_DIVIDE    Divide key
    "f1": 0x70,                   # VK_F1    F1 key
    "f2": 0x71,                   # VK_F2    F2 key
    "f3": 0x72,                   # VK_F3    F3 key
    "f4": 0x73,                   # VK_F4    F4 key
    "f5": 0x74,                   # VK_F5    F5 key
    "f6": 0x75,                   # VK_F6    F6 key
    "f7": 0x76,                   # VK_F7    F7 key
    "f8": 0x77,                   # VK_F8    F8 key
    "f9": 0x78,                   # VK_F9    F9 key
    "f10": 0x79,                  # VK_F10    F10 key
    "f11": 0x7A,                  # VK_F11    F11 key
    "f12": 0x7B,                  # VK_F12    F12 key
    "f13": 0x7C,                  # VK_F13    F13 key
    "f14": 0x7D,                  # VK_F14    F14 key
    "f15": 0x7E,                  # VK_F15    F15 key
    "f16": 0x7F,                  # VK_F16    F16 key
    "f17": 0x80,                  # VK_F17    F17 key
    "f18": 0x81,                  # VK_F18    F18 key
    "f19": 0x82,                  # VK_F19    F19 key
    "f20": 0x83,                  # VK_F20    F20 key
    "f21": 0x84,                  # VK_F21    F21 key
    "f22": 0x85,                  # VK_F22    F22 key
    "f23": 0x86,                  # VK_F23    F23 key
    "f24": 0x87,                  # VK_F24    F24 key
    # 0x88-8F - Unassigned
    "numlock": 0x90,              # VK_NUMLOCK    NUM LOCK key
    "scroll": 0x91,               # VK_SCROLL    SCROLL LOCK key
    # 0x92-96 - OEM specific
    # 0x97-9F - Unassigned
    "lshift": 0xA0,               # VK_LSHIFT    Left SHIFT key
    "rshift": 0xA1,               # VK_RSHIFT    Right SHIFT key
    "lcontrol": 0xA2,             # VK_LCONTROL    Left CONTROL key
    "rcontrol": 0xA3,             # VK_RCONTROL    Right CONTROL key
    "lmenu": 0xA4,                # VK_LMENU    Left MENU key
    "lalt": 0xA4,                # VK_LMENU    Left MENU key
    "rmenu": 0xA5,                # VK_RMENU    Right MENU key
    "ralt": 0xA5,                # VK_RMENU    Right MENU key
    "browser_back": 0xA6,         # VK_BROWSER_BACK    Browser Back key
    "browser_forward": 0xA7,      # VK_BROWSER_FORWARD    Browser Forward key
    "browser_refresh": 0xA8,      # VK_BROWSER_REFRESH    Browser Refresh key
    "browser_stop": 0xA9,         # VK_BROWSER_STOP    Browser Stop key
    "browser_search": 0xAA,       # VK_BROWSER_SEARCH    Browser Search key
    "browser_favorites": 0xAB,    # VK_BROWSER_FAVORITES    Browser Favorites key
    "browser_home": 0xAC,         # VK_BROWSER_HOME    Browser Start and Home key
    "volume_mute": 0xAD,          # VK_VOLUME_MUTE    Volume Mute key
    "volume_down": 0xAE,          # VK_VOLUME_DOWN    Volume Down key
    "volume_up": 0xAF,            # VK_VOLUME_UP    Volume Up key
    "media_next_track": 0xB0,     # VK_MEDIA_NEXT_TRACK    Next Track key
    "media_prev_track": 0xB1,     # VK_MEDIA_PREV_TRACK    Previous Track key
    "media_stop": 0xB2,           # VK_MEDIA_STOP    Stop Media key
    "media_play_pause": 0xB3,     # VK_MEDIA_PLAY_PAUSE    Play/Pause Media key
    "launch_mail": 0xB4,          # VK_LAUNCH_MAIL    Start Mail key
    "launch_media_select": 0xB5,  # VK_LAUNCH_MEDIA_SELECT    Select Media key
    "launch_app1": 0xB6,          # VK_LAUNCH_APP1    Start Application 1 key
    "launch_app2": 0xB7,          # VK_LAUNCH_APP2    Start Application 2 key
    # 0xB8-B9 - Reserved
    "oem_1": 0xBA,                # VK_OEM_1    Used for miscellaneous characters;
                                  # it can vary by keyboard.  For the US standard keyboard, the ';:' key
    ":": 0xBA,
    ";": 0xBA,
    "colon": 0xBA,
    "oem_plus": 0xBB,             # VK_OEM_PLUS    For any country/region, the '+' key
    "plus": 0xBB,
    "oem_comma": 0xBC,            # VK_OEM_COMMA    For any country/region, the ',' key
    "comma": 0xBC,
    ",": 0xBC,
    "<": 0xBC,
    "oem_minus": 0xBD,            # VK_OEM_MINUS    For any country/region, the '-' key
    "minus": 0xBD,
    "oem_period": 0xBE,           # VK_OEM_PERIOD    For any country/region, the '.' key
    ".": 0xBE,
    "period": 0xBE,
    ">": 0xBE,
    "oem_2": 0xBF,                # VK_OEM_2    Used for miscellaneous characters;
                                  # it can vary by keyboard.  For the US standard keyboard, the '/?' key
    "/": 0xBF,
    "slash": 0xBF,
    "?": 0xBF,
    "question": 0xBF,
    "question-mark": 0xBF,
    "oem2": 0xBF,
    "oem_3": 0xC0,                # VK_OEM_3    Used for miscellaneous characters;
                                  # it can vary by keyboard.  For the US standard keyboard, the '`~' key
    "oem3": 0xC0,
    "~": 0xC0,
    "tilde": 0xC0,
    "twiddle": 0xC0,
    "`": 0xC0,
    "back-tick": 0xC0,
    # 0xC1-D7 - Reserved
    # 0xD8-DA - Unassigned
    "oem_4": 0xDB,                # VK_OEM_4    Used for miscellaneous characters;
                                  # it can vary by keyboard.  For the US standard keyboard, the '[{' key
    "oem4": 0xDB,
    "[": 0xDB,
    "{": 0xDB,
    "left-bracket": 0xDB,
    "oem_5": 0xDC,                # VK_OEM_5    Used for miscellaneous characters;
                                  # it can vary by keyboard.  For the US standard keyboard, the '\|' key
    "oem5": 0xDC,
    "|": 0xDC,
    "\\": 0xDC,
    "pipe": 0xDC,
    "backslash": 0xDC,
    "oem_6": 0xDD,                # VK_OEM_6    Used for miscellaneous characters;
                                  # it can vary by keyboard.  For the US standard keyboard, the ']}' key
    "oem6": 0xDD,
    "]": 0xDD,
    "}": 0xDD,
    "right-bracket": 0xDD,
    "oem_7": 0xDE,                # VK_OEM_7    Used for miscellaneous characters;
                                  # it can vary by keyboard.  For the US standard keyboard,
                                  # the 'single-quote/double-quote' key
    "oem7": 0xDE,
    '"': 0xDE,
    "'": 0xDE,
    "quote": 0xDE,
    "tick": 0xDE,
    "oem_8": 0xDF,                # VK_OEM_8    Used for miscellaneous characters; it can vary by keyboard.
    "oem8": 0xDF,
    # 0xE0 - Reserved
    # 0xE1 - OEM specific
    "oem_102": 0xE2,              # VK_OEM_102    Either the angle bracket key or the backslash key on
                                  # the RT 102-key keyboard
    "oem102": 0xE2,
    # 0xE3-E4 - OEM specific
    "processkey": 0xE5,           # VK_PROCESSKEY    IME PROCESS key
    # 0xE6 - OEM specific
    "packet": 0xE7,               # VK_PACKET    Used to pass Unicode characters as if they were
                                  # keystrokes. The VK_PACKET key is the low word of a 32-bit Virtual
                                  # Key value used for non-keyboard input methods. For more
                                  # information, see Remark in KEYBDINPUT, SendInput, WM_KEYDOWN, and WM_KEYUP
    # 0xE8 - Unassigned
    # 0xE9-F5 - OEM specific
    "attn": 0xF6,                 # VK_ATTN    Attn key
    "crsel": 0xF7,                # VK_CRSEL    CrSel key
    "exsel": 0xF8,                # VK_EXSEL    ExSel key
    "ereof": 0xF9,                # VK_EREOF    Erase EOF key
    "play": 0xFA,                 # VK_PLAY    Play key
    "zoom": 0xFB,                 # VK_ZOOM    Zoom key
    "noname": 0xFC,               # VK_NONAME    Reserved
    "pa1": 0xFD,                  # VK_PA1    PA1 key
    "oem_clear": 0xFE,            # VK_OEM_CLEAR    Clear key
    # 0x3A-40 - Undefined
    "0": 0x30,                    # 0 key
    "1": 0x31,                    # 1 key
    "2": 0x32,                    # 2 key
    "3": 0x33,                    # 3 key
    "4": 0x34,                    # 4 key
    "5": 0x35,                    # 5 key
    "6": 0x36,                    # 6 key
    "7": 0x37,                    # 7 key
    "8": 0x38,                    # 8 key
    "9": 0x39,                    # 9 key
    "A": 0x41,                    # A key
    "B": 0x42,                    # B key
    "C": 0x43,                    # C key
    "D": 0x44,                    # D key
    "E": 0x45,                    # E key
    "F": 0x46,                    # F key
    "G": 0x47,                    # G key
    "H": 0x48,                    # H key
    "I": 0x49,                    # I key
    "J": 0x4A,                    # J key
    "K": 0x4B,                    # K key
    "L": 0x4C,                    # L key
    "M": 0x4D,                    # M key
    "N": 0x4E,                    # N key
    "O": 0x4F,                    # O key
    "P": 0x50,                    # P key
    "Q": 0x51,                    # Q key
    "R": 0x52,                    # R key
    "S": 0x53,                    # S key
    "T": 0x54,                    # T key
    "U": 0x55,                    # U key
    "V": 0x56,                    # V key
    "W": 0x57,                    # W key
    "X": 0x58,                    # X key
    "Y": 0x59,                    # Y key
    "Z": 0x5A,                    # Z key
}

_MODIFIER_KEYS = set()
for __k in MODIFIERS:
    _MODIFIER_KEYS.add(STR_VK_MAP[__k])

_WIN_KEYS = [STR_VK_MAP['lwin'], STR_VK_MAP['rwin']]
