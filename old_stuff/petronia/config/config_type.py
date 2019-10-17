"""
Manages the user configuration.
"""

from .application import AbstractApplicationConfig
from .chrome import ChromeConfig
from .command import CommandConfig
from .hotkey import HotKeyConfig
from .workgroup import WorkGroupConfig


class ConfigType(object):
    def get_workgroup_for_display(self, monitors):
        """

        :param monitors: list of current monitor definitions.
        :type monitors: tuple(dict)
        :return: the best matching WorkGroupConfig for the monitor layout.
        :rtype: WorkGroupConfig
        """
        raise NotImplementedError()

    @property
    def uses_layout(self):
        """

        :return: whether this configuration changes the window positions.
        :rtype: bool
        """
        raise NotImplementedError()

    @property
    def applications(self):
        """

        :return: the application configuration
        :rtype: AbstractApplicationConfig
        """
        raise NotImplementedError()

    @property
    def hotkeys(self):
        """

        :return: the hotkey configuration
        :rtype: HotKeyConfig
        """
        raise NotImplementedError()

    @property
    def commands(self):
        """

        :return: the command configuration
        :rtype: CommandConfig
        """
        raise NotImplementedError()

    @property
    def chrome(self):
        """

        :return: the chrome configuration
        :rtype: ChromeConfig
        """
        raise NotImplementedError()
