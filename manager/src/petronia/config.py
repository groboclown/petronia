"""
Manages the user configuration.
"""

from .util.hotkey_chain import HotKeyChain, KeyOverride
from .script import command_builder
from .script.command import Command
import traceback
import re

MODE_CHANGE_COMMAND = "change mode"
DEFAULT_MODE = "default"
LAYOUT_MANAGEMENT_MODE = "Layout Management"


def load_config():
    # TODO actually load a config
    return Config(DisplayWorkGroupsConfig(), ApplicationConfig(), HotKeyConfig(), CommandConfig(), ChromeConfig())


class BaseConfig(object):
    pass


class Config(object):
    """
    Stores all the configuration information
    """
    def __init__(self, workgroups, applications, hotkeys, commands, chrome):
        assert isinstance(workgroups, DisplayWorkGroupsConfig)
        assert isinstance(applications, ApplicationConfig)
        assert isinstance(hotkeys, HotKeyConfig)
        assert isinstance(commands, CommandConfig)
        assert isinstance(chrome, ChromeConfig)

        self.__workgroups = workgroups
        self.__applications = applications
        self.__hotkeys = hotkeys
        self.__commands = commands
        self.__chrome = chrome

    def get_workgroup_for_display(self, monitors):
        return self.__workgroups.get_workgroup_for_display(monitors)

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


class DisplayWorkGroupsConfig(BaseConfig):
    """
    Contains all the work group configs for each display setting.

    Groups: list of dicts:
        * 'name': just a name.  "default" is special.
        * 'monitors': list of MonitorResConfig objects.
        * 'workgroup': WorkGroupConfig object.
    """
    def __init__(self, groups=None):
        if groups is None:
            groups = []

        self.__groups = []
        for g in groups:
            group = {
                'name': 'name' in g and g['name'] or 'n/a',
                'monitors': list(g['monitors']),
                'workgroup': g['workgroup']
            }
            # Make sure the monitors are sorted.
            sorted(group['monitors'], key=lambda m: m.monitor_index)
            self.__groups.append(group)

    def get_workgroup_for_display(self, monitors):
        default_workgroup = None
        best_match = None
        best_rank = 0
        for group in self.__groups:
            if group['name'] == 'default':
                default_workgroup = group['workgroup']
                continue
            current_rank = 0.0
            for m_index in range(len(monitors)):
                if m_index < len(group['monitors']):
                    assert isinstance(group['monitors'][m_index], MonitorResConfig)
                    current_rank += group['monitors'][m_index].find_match_rank(m_index, monitors[m_index])
            if current_rank > best_rank:
                best_rank = current_rank
                best_match = group['workgroup']
        if best_match is None:
            if default_workgroup is None:
                # TODO better logging
                print("<<CONFIG ERROR: no default workgroup; creating one layout per monitor>>")
                layouts = []
                for m_index in range(len(monitors)):
                    layouts.append(LayoutConfig(str(m_index), "split-layout", ORIENTATION_VERTICAL, []))
                return WorkGroupConfig({"default": layouts})
            return default_workgroup
        return best_match


class WorkGroupConfig(BaseConfig):
    """
    Contains all the configurations for the current monitor set.
    """
    def __init__(self, groups_of_layouts_by_name=None):
        if groups_of_layouts_by_name is None:
            groups_of_layouts_by_name = {}
        assert isinstance(groups_of_layouts_by_name, dict)
        self.__workgroup_groups = groups_of_layouts_by_name

    @property
    def layout_groups_by_name(self):
        """
        dict where the key points to a list of layouts
        :return:
        """
        return self.__workgroup_groups

    @property
    def default_layout_group(self):
        if len(self.__workgroup_groups) <= 0:
            return LayoutConfig("default", "split-layout", ORIENTATION_VERTICAL, [])
        if 'default' in self.__workgroup_groups:
            return self.__workgroup_groups['default']
        # print("Getting first workgroup item from {0}".format(self.__workgroup_groups))
        return list(self.__workgroup_groups.items())[0][1]

    def get_layout_group(self, name):
        if name in self.layout_groups_by_name:
            return self.layout_groups_by_name[name]
        return self.default_layout_group


class MonitorResConfig(BaseConfig):
    """
    The configuration for a single monitor at a specific resolution.  Used by the
    DisplayWorkGroupConfig to map a monitor setup to a workgroup.
    """
    def __init__(self, monitor_index, res_x, res_y, show_bar):
        """

        :param monitor_index: monitor index (starts with 0)
        :param res_x: monitor x resolution
        :param res_y: monitor y resolution
        :param show_bar: show the start bar?
        """
        self.monitor_index = monitor_index
        self.res_x = res_x
        self.res_y = res_y
        self.id = str(monitor_index) + "x" + str(res_x) + "x" + str(res_y)
        self.show_bar = show_bar
        self.top_panel = None

    def find_match_rank(self, index, monitor_description):
        """

        :param index: monitor_description's index
        :param monitor_description: the dict from the OS event
        :return: rank of how good a match this is.  0 == bad
        """
        rank = 0

        # Monitor position match: 2 points
        if index == self.monitor_index:
            rank += 2

        # Width match: 10 points, based on ratio of the
        # actual monitor vs. this monitor.
        rank += (
            10.0 * (
                1.0 - (abs(self.res_x - monitor_description['width']) / max(self.res_x, monitor_description['width']))
            )
        )

        rank += (
            10.0 * (
                1.0 - (abs(self.res_y - monitor_description['height']) / max(self.res_y, monitor_description['height']))
            )
        )

        return rank


# How the panel splits its children.
ORIENTATION_VERTICAL = "vertical"
ORIENTATION_HORIZONTAL = "horizontal"
ORIENTATION_CENTER = "none"


class LayoutConfig(BaseConfig):
    """
    A single panel that can contain children and/or applications.
    The panel can either show the child panels or a single application
    at a time.

    child_splits:
        Array of descriptions for each child, each is a ChildSplitConfig.
    """
    def __init__(self, name, category, orientation, child_splits):
        assert orientation in [ORIENTATION_HORIZONTAL, ORIENTATION_VERTICAL, None], (
            "bad orientation: {0}".format(orientation))
        self.name = name
        self.category = category
        self.id = str(name)
        self.orientation = orientation
        self.child_splits = child_splits
        self.is_main_layout_sibling = name == 'main'

        # Until we get it working cleanly...
        self.include_initial_windows = True


class ChildSplitConfig(BaseConfig):
    def __init__(self, size, layout_def):
        assert isinstance(size, int)
        assert layout_def is None or isinstance(layout_def, LayoutConfig)
        self.size = size
        self.layout_def = layout_def


class ApplicationConfig(BaseConfig):
    """
    Matches any number of applications (through the matcher regex), and associates
    it with one or more panels.
    """
    def __init__(self, managed_chrome_default_match=True,
                 managed_chrome_matchers=None,
                 managed_chome_not_matchers=None):
        self.managed_chrome_default_match = managed_chrome_default_match
        if managed_chrome_matchers is None:
            managed_chrome_matchers = tuple()
        if managed_chome_not_matchers is None:
            managed_chome_not_matchers = tuple()
        assert isinstance(managed_chrome_matchers, list) or isinstance(managed_chrome_matchers, tuple)
        self.managed_chrome_matchers = managed_chrome_matchers
        assert isinstance(managed_chome_not_matchers, list) or isinstance(managed_chome_not_matchers, tuple)
        self.managed_chome_not_matchers = managed_chome_not_matchers

    def is_managed_chrome(self, window_info):
        """

        :param window_info:
        :return: True if the window should be "managed" by the system, in terms of
            look-and-feel of the application.
        """
        for matcher in self.managed_chrome_matchers:
            if matcher.matches(window_info):
                print("*** Matched managed chrome: {0}".format(window_info))
                return True
        for matcher in self.managed_chome_not_matchers:
            if matcher.matches(window_info):
                print("*** Matched not managed chrome: {0}".format(window_info))
                return False
        return self.managed_chrome_default_match

    def is_contained_in(self, layout_id, window_info):
        return True


class AppMatcher(BaseConfig):
    """
    Matches an application either by a regex or a string, against the window's class,
    executable name, or module name.

    Example window_info: {'pid': c_ulong(2944), 'class': 'SunAwtFrame',
        'exec_filename': '\\Device\\HarddiskVolume2\\Windows\\cmd.exe',
        'border': {'right': 1366, 'top': 0, 'x': 0, 'width': 1366,
        'y': 0, 'left': 0, 'height': 768, 'bottom': 768}, 'hwnd': 263444,
        'cid': 'hwnd_199', 'visible': True,
        'title': 'win-py-shell - cmd.exe',
        'module_filename': None, 'visibility': ['shown', 'maximized', 'active']}}
    """
    def __init__(self, match_returns=True, title_exact=None, title_re=None, module_exact=None, module_re=None,
                 exec_exact=None, exec_re=None):
        """

        :param match_returns: the value to return if a match happens; otherwise, the Not of this is returned.
        :param title_exact:
        :param title_re:
        :param module_exact:
        :param module_re:
        :param exec_exact:
        :param exec_re:
        """
        self.match_returns = match_returns

        assert title_exact is None or isinstance(title_exact, str)
        self.title_exact = title_exact
        if isinstance(title_re, str):
            title_re = re.compile(title_re)
        assert title_re is None or (hasattr(title_re, "match") and callable(title_re.match))
        self.title_re = title_re

        assert module_exact is None or isinstance(module_exact, str)
        self.module_exact = module_exact
        if isinstance(module_re, str):
            module_re = re.compile(module_re)
        assert module_re is None or (hasattr(module_re, "match") and callable(module_re.match))
        self.module_re = module_re

        assert exec_exact is None or isinstance(exec_exact, str)
        self.exec_exact = exec_exact
        if isinstance(exec_re, str):
            exec_re = re.compile(exec_re)
        assert exec_re is None or (hasattr(exec_re, "match") and callable(exec_re.match))
        self.exec_re = exec_re

    def matches(self, window_info):
        if window_info['title'] is not None:
            if self.title_exact is not None:
                if self.title_exact == window_info['title']:
                    return self.match_returns
            if self.title_re is not None:
                if self.title_re.match(window_info['title']) is not None:
                    return self.match_returns

        if window_info['module_filename'] is not None:
            if self.module_exact is not None:
                if self.module_exact == window_info['module_filename']:
                    return self.match_returns
            if self.module_re is not None:
                if self.module_re.match(window_info['module_filename']) is not None:
                    return self.match_returns

        if window_info['exec_filename'] is not None:
            if self.exec_exact is not None:
                if self.exec_exact == window_info['exec_filename']:
                    return self.match_returns
            if self.exec_re is not None:
                if self.exec_re.match(window_info['exec_filename']) is not None:
                    return self.match_returns

        return not self.match_returns


class HotKeyConfig(BaseConfig):
    """
    Associates a hotkey with an action.

    TODO this needs to be modal.
    """
    def __init__(self):
        self.__key_modes = {}

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


class CommandConfig(BaseConfig):
    """
    Associates a command with an action; usually it's kind
    of a script.
    """
    def __init__(self):
        self.__commands = list(command_builder.create_all_commands())

    @property
    def commands(self):
        return self.__commands

    def add_command(self, cmd):
        assert isinstance(cmd, Command)
        self.__commands.append(cmd)


class ChromeConfig(BaseConfig):
    """
    Controls the "chrome" around the windows.
    """
    def __init__(self, border_width=4, border_color=0xff0000):
        self.border_width = border_width
        self.border_padding = 0
        self.border_color = border_color
        self.scrollbar_width = 0
        self.scrollbar_height = 0
        self.has_title = False
        self.portal_chrome_border = {
            'color': 0x404040, 'width': 2,  # Placeholders
            'top': 0, 'bottom': 0, 'left': 0, 'right': 0,
        }
        self.portal_chrome_active_border = {
            'color': 0x808000, 'width': 4,  # Placeholders
            'top': 0, 'bottom': 0, 'left': 0, 'right': 0,
        }

    def get_system_window_settings(self):
        # see shell__set_window_metrics
        ret = {}
        if self.border_width > 0:
            ret['border-width'] = self.border_width
        if self.border_padding >= 0:
            ret['padded-border-width'] = self.border_padding
        if self.scrollbar_width > 0:
            ret['scroll-width'] = self.scrollbar_width
        if self.scrollbar_height > 0:
            ret['scroll-height'] = self.scrollbar_height
        # All other chrome is ignored for this call
        return ret

    @property
    def remove_decoration(self):
        """

        :return: True if the windows should not have wide borders or title bars with the
            controls (system menu, minimize, maximize, restore).
        """
        return True

    @property
    def remove_resize_border(self):
        """

        :return: True if the window borders should not be resizable.
        """
        return True

    @property
    def show_taskbar_with_start_menu(self):
        """

        :return: True if the task bar is shown whenever the user requests the start menu to be shown;
            False if default OS behavior is used.
        """
        return True
