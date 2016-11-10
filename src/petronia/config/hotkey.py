"""
Manages the user configuration.
"""

from .base_config import BaseConfig
from ..util.hotkey_chain import HotKeyChain, KeyOverride

DEFAULT_MODE = "default"


class HotKeyConfig(BaseConfig):
    """
    Associates a hotkey with an action.

    TODO this needs better setup support.
    """
    def __init__(self):
        super()
        self.__key_modes = {
            # Always have at least a default mode
            DEFAULT_MODE: HotKeyChain()
        }

    @property
    def mode_combos(self):
        """

        :return: mapping between the mode name and the key handler.
        """
        return self.__key_modes

    def parse_hotkey_mode_keys(self, mode, config_lines, block_win_key=False):
        assert isinstance(mode, str)
        key_list = []
        for line in config_lines:
            line = line.strip()
            if len(line) > 0 and line.find("=>") > 0:
                keys, command = line.split("=>")
                key_list.append((keys.strip(), command.strip()))
        chain = HotKeyChain(key_list)
        chain.block_win_key = block_win_key
        self.__key_modes[mode] = chain

    def parse_simple_mode_keys(self, mode, config_lines):
        assert isinstance(mode, str)
        key_list = []
        for line in config_lines:
            line = line.strip()
            if len(line) > 0 and line.find("=>") > 0:
                keys, command = line.split("=>")
                key_list.append((keys.strip(), command.strip()))
        self.__key_modes[mode] = KeyOverride(key_list)
