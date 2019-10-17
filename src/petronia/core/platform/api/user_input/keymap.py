
"""
Definitions for key names that must be recognized by the platform.

This is just a collection of strings.  What are we even doing with this?
"""

# Built-in alias VK keys for user-specified keys
MODIFIER_ALIASES = {
    "win": ("lsuper", "rsuper",),
    "shift": ("lshift", "rshift",),
    "control": ("lcontrol", "rcontrol",),
    "ctrl": ("lcontrol", "rcontrol",),
    "alt": ("lalt", "ralt",),
    "menu": ("lmenu", "rmenu",),
}


# Set of all recognized modifiers
# Some systems do not use all of these.
MODIFIERS = (
    "lshift",
    "rshift",
    "lcontrol",
    "rcontrol",
    "lalt",
    "ralt",
    "lsuper",
    "rsuper",
    "lmenu",
    "rmenu",
    "apps",
    "caps-lock",
    "scroll-lock",
    "num-lock",
)

KEY_ALIASES = {
    "esc": "escape",
    "lwin": "lsuper",
    "rwin": "rsuper",
    "lctrl": "lcontrol",
    "rctrl": "rcontrol",
    "prior": "pageup",
    "pgup": "pageup",
    "next": "pagedown",
    "pgdn": "pagedown",
    ":": "colon",
    ";": "semi-colon",
    ",": "comma",
    "<": "less-than",
    ".": "period",
    ">": "greater-than",
    "/": "slash",
    "?": "question",
    "question-mark": "question",
    "+": "plus",
    "=": "equal",
    "equals": "equal",
    "-": "dash",
    "hyphen": "dash",
    "_": "underscore",
    "~": "tilde",
    "`": "back-tick",

    "[": "left-bracket",
    "left-square-bracket": "left-bracket",
    "open-square-bracket": "left-bracket",
    "left-brace": "left-bracket",
    "open-brace": "left-bracket",
    "left-square-brace": "left-bracket",
    "open-square-brace": "left-bracket",
    "{": "left-curly-bracket",
    "left-curly-brace": "left-curly-bracket",
    "open-curly-brace": "left-curly-bracket",

    "]": "right-bracket",
    "right-square-bracket": "right-bracket",
    "close-square-bracket": "right-bracket",
    "right-brace": "right-bracket",
    "close-brace": "right-bracket",
    "right-square-brace": "right-bracket",
    "close-square-brace": "right-bracket",
    "}": "right-curly-bracket",
    "right-curly-brace": "right-curly-bracket",
    "close-curly-brace": "right-curly-bracket",

    "|": "pipe",
    "\\": "backslash",
    "back-slash": "backslash",
    '"': "quote",
    "double-quote": "quote",
    "'": "tick",
    "single-quote": "tick",
}

# List of all recognized key names.
# https://msdn.microsoft.com/en-us/library/windows/desktop/dd375731(v=vs.85).aspx
# Some keys will overlap, or will not be supported,
# depending on the system.  For example, in many cases,
# using the shift-variant won't be different than the other,
# because the level above the key handler manages that
# mapping of the keyboard keys to the letter on the screen.
# It's up to the platform to understand the user's keyboard and
# translate that key name to the key code.

# The user can also use key codes, if the corresponding key isn't
# given a name.  These are represented as '#0a'

KEY_NAMES = (
    "lmb",                  # VK_LBUTTON  Left mouse button
    "rmb",                  # VK_RBUTTON  Right mouse button
    "break",                # VK_CANCEL   Control-break processing
    "mmb",                  # VK_MBUTTON  Middle mouse button (three-button mouse)
    "x1mb",                 # VK_XBUTTON1 X1 mouse button
    "x2mb",                 # VK_XBUTTON2 X2 mouse button
    "x3mb",                 # -           Undefined
    "back",                 # VK_BACK     BACKSPACE key
    "backspace",            # VK_BACK     BACKSPACE key
    "tab",                  # VK_TAB      TAB key
    "clear",                # VK_CLEAR    CLEAR key
    "return",               # VK_RETURN   ENTER key
    "enter",                # VK_RETURN   ENTER key
    "cr",                   # VK_RETURN   ENTER key
    "lf",                   # VK_RETURN   ENTER key
    "pause",                # VK_PAUSE    PAUSE key
    "caps-lock",            # VK_CAPITAL  CAPS LOCK key
    "kana",                 # VK_KANA     IME Kana mode
    "hanguel",              # VK_HANGUEL  IME Hanguel mode (maintained for compatibility; use VK_HANGUL)
    "hangul",               # VK_HANGUL   IME Hangul mode
    "junja",                # VK_JUNJA    IME Junja mode
    "final",                # VK_FINAL    IME final mode
    "hanja",                # VK_HANJA    IME Hanja mode
    "kanji",                # VK_KANJI    IME Kanji mode
    "escape",               # VK_ESCAPE    ESC key
    "convert",              # VK_CONVERT    IME convert
    "nonconvert",           # VK_NONCONVERT    IME nonconvert
    "accept",               # VK_ACCEPT    IME accept
    "modechange",           # VK_MODECHANGE    IME mode change request
    "space",                # VK_SPACE    SPACEBAR
    "pageup",               # VK_PRIOR    PAGE UP key
    "pagedown",             # VK_NEXT    PAGE DOWN key
    "end",                  # VK_END    END key
    "home",                 # VK_HOME    HOME key
    "left",                 # VK_LEFT    LEFT ARROW key
    "up",                   # VK_UP    UP ARROW key
    "right",                # VK_RIGHT    RIGHT ARROW key
    "down",                 # VK_DOWN    DOWN ARROW key
    "select",               # VK_SELECT    SELECT key
    "print",                # VK_PRINT    PRINT key
    "execute",              # VK_EXECUTE    EXECUTE key
    "snapshot",             # VK_SNAPSHOT    PRINT SCREEN key
    "insert",               # VK_INSERT    INS key
    "delete",               # VK_DELETE    DEL key
    "del",                  # VK_DELETE    DEL key
    "help",                 # VK_HELP    HELP key
    "lsuper",               # VK_LWIN    Left Windows key (Natural keyboard)
    "rsuper",               # VK_RWIN    Right Windows key (Natural keyboard)
    "apps",                 # VK_APPS    Applications key (Natural keyboard)
    "sleep",                # VK_SLEEP    Computer Sleep key
    "numpad0",              # VK_NUMPAD0    Numeric keypad 0 key
    "numpad1",              # VK_NUMPAD1    Numeric keypad 1 key
    "numpad2",              # VK_NUMPAD2    Numeric keypad 2 key
    "numpad3",              # VK_NUMPAD3    Numeric keypad 3 key
    "numpad4",              # VK_NUMPAD4    Numeric keypad 4 key
    "numpad5",              # VK_NUMPAD5    Numeric keypad 5 key
    "numpad6",              # VK_NUMPAD6    Numeric keypad 6 key
    "numpad7",              # VK_NUMPAD7    Numeric keypad 7 key
    "numpad8",              # VK_NUMPAD8    Numeric keypad 8 key
    "numpad9",              # VK_NUMPAD9    Numeric keypad 9 key
    "multiply",             # VK_MULTIPLY    Multiply key
    "add",                  # VK_ADD    Add key
    "separator",            # VK_SEPARATOR    Separator key
    "subtract",             # VK_SUBTRACT    Subtract key
    "decimal",              # VK_DECIMAL    Decimal key
    "divide",               # VK_DIVIDE    Divide key
    "f1",                   # VK_F1    F1 key
    "f2",                   # VK_F2    F2 key
    "f3",                   # VK_F3    F3 key
    "f4",                   # VK_F4    F4 key
    "f5",                   # VK_F5    F5 key
    "f6",                   # VK_F6    F6 key
    "f7",                   # VK_F7    F7 key
    "f8",                   # VK_F8    F8 key
    "f9",                   # VK_F9    F9 key
    "f10",                  # VK_F10    F10 key
    "f11",                  # VK_F11    F11 key
    "f12",                  # VK_F12    F12 key
    "f13",                  # VK_F13    F13 key
    "f14",                  # VK_F14    F14 key
    "f15",                  # VK_F15    F15 key
    "f16",                  # VK_F16    F16 key
    "f17",                  # VK_F17    F17 key
    "f18",                  # VK_F18    F18 key
    "f19",                  # VK_F19    F19 key
    "f20",                  # VK_F20    F20 key
    "f21",                  # VK_F21    F21 key
    "f22",                  # VK_F22    F22 key
    "f23",                  # VK_F23    F23 key
    "f24",                  # VK_F24    F24 key
    "num-lock",             # VK_NUMLOCK    NUM LOCK key
    "scroll-lock",          # VK_SCROLL    SCROLL LOCK key
    "lshift",               # VK_LSHIFT    Left SHIFT key
    "rshift",               # VK_RSHIFT    Right SHIFT key
    "lcontrol",             # VK_LCONTROL    Left CONTROL key
    "rcontrol",             # VK_RCONTROL    Right CONTROL key
    "lmenu",                # VK_LMENU    Left MENU key
    "lalt",                 # VK_LMENU    Left MENU key
    "rmenu",                # VK_RMENU    Right MENU key
    "ralt",                 # VK_RMENU    Right MENU key
    "browser-back",         # VK_BROWSER_BACK    Browser Back key
    "browser-forward",      # VK_BROWSER_FORWARD    Browser Forward key
    "browser-refresh",      # VK_BROWSER_REFRESH    Browser Refresh key
    "browser-stop",         # VK_BROWSER_STOP    Browser Stop key
    "browser-search",       # VK_BROWSER_SEARCH    Browser Search key
    "browser-favorites",    # VK_BROWSER_FAVORITES    Browser Favorites key
    "browser-home",         # VK_BROWSER_HOME    Browser Start and Home key
    "volume-mute",          # VK_VOLUME_MUTE    Volume Mute key
    "volume-down",          # VK_VOLUME_DOWN    Volume Down key
    "volume-up",            # VK_VOLUME_UP    Volume Up key
    "media-next-track",     # VK_MEDIA_NEXT_TRACK    Next Track key
    "media-prev-track",     # VK_MEDIA_PREV_TRACK    Previous Track key
    "media-stop",           # VK_MEDIA_STOP    Stop Media key
    "media-play-pause",     # VK_MEDIA_PLAY_PAUSE    Play/Pause Media key
    "launch-mail",          # VK_LAUNCH_MAIL    Start Mail key
    "launch-media-select",  # VK_LAUNCH_MEDIA_SELECT    Select Media key
    "launch-app1",          # VK_LAUNCH_APP1    Start Application 1 key
    "launch-app2",          # VK_LAUNCH_APP2    Start Application 2 key
    "colon",                # VK_OEM_1    Used for miscellaneous characters;
    "semi-colon",
    "plus",                 # VK_OEM_PLUS    For any country/region, the '+' key
    "comma",                # VK_OEM_COMMA    For any country/region, the ',' key
    "less-than",
    "minus",                # VK_OEM_MINUS    For any country/region, the '-' key
    "period",               # VK_OEM_PERIOD    For any country/region, the '.' key
    "greater-than",
    "slash",                # VK_OEM_2    Used for miscellaneous characters;
    "question",
    "tilde",                # VK_OEM_3    Used for miscellaneous characters;
    "back-tick",
    "left-bracket",         # VK_OEM_4    Used for miscellaneous characters;
    "left-curly-bracket",   # VK_OEM_4    Used for miscellaneous characters;
    "pipe",                 # VK_OEM_5    Used for miscellaneous characters;
    "backslash",
    "right-bracket",        # VK_OEM_6    Used for miscellaneous characters;
    "right-curley-bracket",
    "quote",                # VK_OEM_7    Used for miscellaneous characters;
    "tick",
    "oem-8",                # VK_OEM_8    Used for miscellaneous characters; it can vary by keyboard.
    "oem-102",              # VK_OEM_102    Either the angle bracket key or the backslash key on
                            # the RT 102-key keyboard
    "processkey",           # VK_PROCESSKEY    IME PROCESS key
    "packet",               # VK_PACKET    Used to pass Unicode characters as if they were
                            # keystrokes. The VK_PACKET key is the low word of a 32-bit Virtual
                            # Key value used for non-keyboard input methods. For more
                            # information, see Remark in KEYBDINPUT, SendInput, WM_KEYDOWN, and WM_KEYUP
    "attn",                 # VK_ATTN    Attn key
    "crsel",                # VK_CRSEL    CrSel key
    "exsel",                # VK_EXSEL    ExSel key
    "ereof",                # VK_EREOF    Erase EOF key
    "play",                 # VK_PLAY    Play key
    "zoom",                 # VK_ZOOM    Zoom key
    "noname",               # VK_NONAME    Reserved
    "pa1",                  # VK_PA1    PA1 key
    "oem-clear",            # VK_OEM_CLEAR    Clear key
    "0",                    # 0 key
    "1",                    # 1 key
    "2",                    # 2 key
    "3",                    # 3 key
    "4",                    # 4 key
    "5",                    # 5 key
    "6",                    # 6 key
    "7",                    # 7 key
    "8",                    # 8 key
    "9",                    # 9 key
    "a",                    # A key
    "b",                    # B key
    "c",                    # C key
    "d",                    # D key
    "e",                    # E key
    "f",                    # F key
    "g",                    # G key
    "h",                    # H key
    "i",                    # I key
    "j",                    # J key
    "k",                    # K key
    "l",                    # L key
    "m",                    # M key
    "n",                    # N key
    "o",                    # O key
    "p",                    # P key
    "q",                    # Q key
    "r",                    # R key
    "s",                    # S key
    "t",                    # T key
    "u",                    # U key
    "v",                    # V key
    "w",                    # W key
    "x",                    # X key
    "y",                    # Y key
    "z",                    # Z key
)
