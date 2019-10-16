
"""
General input handling code.
"""

from .hotkeys import (
    create_hotkey_handler,
)
from .keymap import (
    vk_to_names,
)
from .parse_hotkeys import (
    create_master_mkey,
    create_master_modifier,
    create_master_mkey_and_sequence_combo,
    create_master_modifier_hotkey_combo,
)
