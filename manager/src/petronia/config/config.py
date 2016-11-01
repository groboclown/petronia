"""
Manages the user configuration.
"""

from .application import ApplicationListConfig
from .chrome import ChromeConfig
from .command import CommandConfig
from .hotkey import HotKeyConfig
from .workgroup import DisplayWorkGroupsConfig


class Config(object):
    """
    Stores all the configuration information
    """
    def __init__(self, workgroups=None, applications=None, hotkeys=None, commands=None, chrome=None):
        assert workgroups is None or isinstance(workgroups, DisplayWorkGroupsConfig)
        assert hotkeys is None or isinstance(hotkeys, HotKeyConfig)
        if commands is None:
            commands = CommandConfig()
        assert commands is None or isinstance(commands, CommandConfig)
        assert chrome is None or isinstance(chrome, ChromeConfig)

        if applications is None:
            applications = ApplicationListConfig([])
        elif isinstance(applications, list) or isinstance(applications, tuple):
            applications = ApplicationListConfig(applications)
        elif not isinstance(applications, ApplicationListConfig):
            applications = ApplicationListConfig([applications])

        self.__workgroups = workgroups
        self.__applications = applications
        self.__hotkeys = hotkeys is None and HotKeyConfig() or hotkeys
        self.__commands = commands is None and CommandConfig() or commands
        self.__chrome = chrome is None and ChromeConfig() or chrome

    def get_workgroup_for_display(self, monitors):
        if self.__workgroups is None:
            return []
        return self.__workgroups.get_workgroup_for_display(monitors)

    @property
    def uses_layout(self):
        return self.__workgroups is not None

    @property
    def applications(self):
        return self.__applications

    @property
    def hotkeys(self):
        return self.__hotkeys

    @property
    def commands(self):
        return self.__commands

    @property
    def chrome(self):
        return self.__chrome
