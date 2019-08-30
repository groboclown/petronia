
"""
Helpers for managing hotkeys.
"""

from .hotkey_chain import (
    ACTION_PENDING,
    ACTION_CANCELLED,
    ACTION_COMPLETE,
    IGNORED,
    HotKeyChain,
    KeyCombo,
    KeyCode,
    StandardKeyCode,
    ModifierKeyCode,
    StatefulKeyCode,
    create_primary_chain,
    create_modal_chain,
    create_independent_key_chain,
)
