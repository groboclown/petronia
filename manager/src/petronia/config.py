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


class BaseConfig(object):
    pass


class Config(object):
    """
    Stores all the configuration information
    """
    def __init__(self, workgroups=None, applications=None, hotkeys=None, commands=None, chrome=None):
        assert workgroups is None or isinstance(workgroups, DisplayWorkGroupsConfig)
        assert hotkeys is None or isinstance(hotkeys, HotKeyConfig)
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
    """
    To make a child "floating" (some layout types are floating), set the
    child split "size" to 0.
    """
    def __init__(self, size, layout_def):
        assert isinstance(size, int)
        assert layout_def is None or isinstance(layout_def, LayoutConfig)
        self.size = size
        self.layout_def = layout_def


class AbstractApplicationConfig(BaseConfig):
    def is_managed_chrome(self, window_info):
        """

        :param window_info:
        :return: True if the window should be "managed" by the system, in terms of
            look-and-feel of the application.  None if the configuration has no information
            about  this window.
        """
        raise NotImplementedError()

    def is_tiled(self, window_info):
        """

        :param window_info:
        :return: True if the window should belong to a tile, False if it acts like a floating, traditional window.
            None if the configuration has no information about  this window.
        """
        raise NotImplementedError()

    def get_best_portal_match(self, portal_aliases, window_info):
        """

        Examines the list of portal aliases, and return the best match for this application's
        initial placement.  This can return None if it doesn't know anything about the input
        application.

        :param portal_aliases:
        :param window_info: information about the application's window.
        :return: The portal alias to place the given window.
        """
        raise NotImplementedError()


class ApplicationListConfig(AbstractApplicationConfig):
    def __init__(self, app_configs, default_is_tiled=True, default_is_managed_chrome=True):
        assert isinstance(app_configs, list) or isinstance(app_configs, tuple)
        for app in app_configs:
            assert isinstance(app, AbstractApplicationConfig)
        self.__app_configs = app_configs
        self.default_is_tiled = default_is_tiled
        self.default_is_managed_chrome = default_is_managed_chrome

    def is_tiled(self, window_info):
        for app in self.__app_configs:
            res = app.is_tiled(window_info)
            if res is not None:
                return res
        return self.default_is_tiled

    def is_managed_chrome(self, window_info):
        for app in self.__app_configs:
            res = app.is_managed_chrome(window_info)
            if res is not None:
                return res
        return self.default_is_managed_chrome

    def get_best_portal_match(self, portal_aliases, window_info):
        for app in self.__app_configs:
            res = app.get_best_portal_match(portal_aliases, window_info)
            if res is not None:
                return res
        return None


class ApplicationChromeConfig(AbstractApplicationConfig):
    """
    Matches any number of applications (through the matcher regex), and associates
    it with one or more panels.
    """
    def __init__(self,
                 is_managed_chrome=True,
                 is_tiled=True,
                 app_matchers=None):
        if app_matchers is None:
            app_matchers = tuple()
        elif isinstance(app_matchers, AppMatcher):
            app_matchers = (app_matchers,)
        for matcher in app_matchers:
            assert isinstance(matcher, AppMatcher)

        self.__is_managed_chrome = is_managed_chrome
        self.__is_tiled = is_tiled
        self.__app_matchers = app_matchers

    def is_managed_chrome(self, window_info):
        """

        :param window_info:
        :return: True if the window should be "managed" by the system, in terms of
            look-and-feel of the application.
        """
        for matcher in self.__app_matchers:
            if matcher.matches(window_info):
                # print("DEBUG Matched managed chrome: {0}".format(window_info))
                return self.__is_managed_chrome
        return None

    def is_tiled(self, window_info):
        for matcher in self.__app_matchers:
            if matcher.matches(window_info):
                return self.__is_tiled
        return None

    def get_best_portal_match(self, portal_aliases, window_info):
        return None


class ApplicationPositionConfig(AbstractApplicationConfig):
    """
    Matches any number of applications (through the matcher regex), and associates
    it with one or more panels.
    """
    def __init__(self, portal_names, app_matchers):
        if not isinstance(app_matchers, list) and not isinstance(app_matchers, tuple):
            assert isinstance(app_matchers, AppMatcher)
            app_matchers = (app_matchers,)
        for matcher in app_matchers:
            assert isinstance(matcher, AppMatcher)
        self.__app_matchers = app_matchers

        self.__portal_matchers = []
        if not isinstance(portal_names, list) and not isinstance(portal_names, tuple):
            portal_names = (portal_names,)
        for name in portal_names:
            if isinstance(name, str):
                name = re.compile(re.escape(name))
            assert hasattr(name, 'match') and callable(name.match)
            self.__portal_matchers.append(name)

    def is_managed_chrome(self, window_info):
        return None

    def is_tiled(self, window_info):
        return None

    def get_best_portal_match(self, portal_aliases, window_info):
        for app_matcher in self.__app_matchers:
            if app_matcher.matches(window_info):
                for portal_matcher in self.__portal_matchers:
                    for portal_alias in portal_aliases:
                        if portal_matcher.match(portal_alias) is not None:
                            return portal_alias
                # Application matched, but no portal matched.  Return
                # None, in case this is matched by another ApplicationConfig.
                return None
        return None


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
    def __init__(self, match_returns=True, title=None, title_re=None, module_path=None, module_path_re=None,
                 exec_path=None, exec_path_re=None, class_name=None, class_name_re=None):
        """

        :param match_returns: the value to return if a match happens; otherwise, the Not of this is returned.
        :param title: either use this or title_re
        :param title_re:
        :param module_path:
        :param module_path_re:
        :param exec_path:
        :param exec_path_re:
        :param class_name:
        :param class_name_re:
        """
        self.match_returns = match_returns

        self.re_matchers = {}

        def add_matcher(name, exact, regex):
            if exact is not None:
                assert regex is None
                assert isinstance(exact, str)
                self.re_matchers[name] = re.compile(r'.*?\\' + re.escape(regex) + '$', re.IGNORECASE)
            elif regex is not None:
                if isinstance(regex, str):
                    regex = re.compile(regex, re.IGNORECASE)
                assert (hasattr(regex, "match") and callable(regex.match))
                self.re_matchers[name] = regex
        add_matcher('title', title, title_re)
        add_matcher('module_filename', module_path, module_path_re)
        add_matcher('exec_filename', exec_path, exec_path_re)
        add_matcher('class', class_name, class_name_re)

    def matches(self, window_info):
        # Default to not knowing about this window
        ret = None
        for key, value in window_info.items():
            if key in self.re_matchers:
                if ret is None:
                    ret = self.re_matchers[key].match(value) is not None
                else:
                    ret = ret and (self.re_matchers[key].match(value) is not None)
        if ret is None:
            return ret
        if ret:
            return self.match_returns
        return not self.match_returns


class HotKeyConfig(BaseConfig):
    """
    Associates a hotkey with an action.

    TODO this needs better setup support.
    """
    def __init__(self):
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
        self.has_resize_border = False
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
        return not self.has_title

    @property
    def remove_resize_border(self):
        """

        :return: True if the window borders should not be resizable.
        """
        return not self.has_resize_border

    @property
    def show_taskbar_with_start_menu(self):
        """

        :return: True if the task bar is shown whenever the user requests the start menu to be shown;
            False if default OS behavior is used.
        """
        return True
