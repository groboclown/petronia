"""
Manages the user configuration.
"""

from .base_config import BaseConfig
from ..script import command_builder
from ..script.command import Command


class CommandConfig(BaseConfig):
    """
    Associates a command with an action; usually it's kind
    of a script.
    """
    def __init__(self):
        super()
        self.__commands = list(command_builder.create_all_commands())

    @property
    def commands(self):
        return self.__commands

    def add_command(self, cmd):
        assert isinstance(cmd, Command)
        self.__commands.append(cmd)
