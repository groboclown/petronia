"""
Manages the user configuration.
"""

from collections import defaultdict
from .application import ApplicationListConfig, AbstractApplicationConfig
from .chrome import ChromeConfig
from .command import CommandConfig
from .hotkey import HotKeyConfig
from .workgroup import DisplayWorkGroupsConfig
from .config_type import ConfigType
from .component import ComponentConfig


class Config(ConfigType):
    """
    Stores all the configuration information
    """
    def __init__(self, workgroups=None, applications=None, hotkeys=None, commands=None, chrome=None, component=None):
        assert workgroups is None or isinstance(workgroups, DisplayWorkGroupsConfig)
        assert hotkeys is None or isinstance(hotkeys, HotKeyConfig)
        if commands is None:
            commands = CommandConfig()
        assert commands is None or isinstance(commands, CommandConfig)
        assert chrome is None or isinstance(chrome, ChromeConfig)
        assert component is None or isinstance(component, ComponentConfig)

        if applications is None:
            applications = ApplicationListConfig([])
        elif isinstance(applications, list) or isinstance(applications, tuple):
            applications = ApplicationListConfig(applications)
        else:
            assert isinstance(applications, AbstractApplicationConfig)

        self.__workgroups = workgroups
        self.__applications = applications
        self.__hotkeys = hotkeys is None and HotKeyConfig() or hotkeys
        self.__commands = commands is None and CommandConfig() or commands
        self.__chrome = chrome is None and ChromeConfig() or chrome
        self.__component = component is None and ComponentConfig() or component
        self.__init_options = defaultdict(None)

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

    @property
    def init_options(self):
        return self.__init_options

    def register_components(self, registrar):
        self.__component.register_extensions(registrar)
        self.__component.activate_singletons(registrar)
