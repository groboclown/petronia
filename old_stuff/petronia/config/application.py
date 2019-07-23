"""
Manages the user configuration.
"""

from .base_config import BaseConfig
import re


class AbstractApplicationConfig(BaseConfig):
    def has_title(self, window_info):
        """

        :param window_info:
        :return: True if the title bar should be kept on the window, or False if it should be removed, or
            None if the configuration has no information about this window.
        """
        raise NotImplementedError()

    def has_border(self, window_info):
        """

        :param window_info:
        :return: True if the resize border should be kept on the window, or False if it should be removed, or
            None if the configuration has no information about this window.
        """
        raise NotImplementedError()

    def is_tiled(self, window_info):
        """

        :param window_info:
        :return: True if the window should belong to a tile, False if it acts like a floating, traditional window.
            None if the configuration has no information about  this window.
        """
        raise NotImplementedError()

    def is_resizable(self, window_info):
        """

        :param window_info:
        :return: True if the window should be resized when put into a portal.
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
    def __init__(self, app_configs, default_is_tiled=True, default_has_border=True,
                 default_has_title=True, default_is_resizable=True):
        assert isinstance(app_configs, list) or isinstance(app_configs, tuple)
        super()
        for app in app_configs:
            assert isinstance(app, AbstractApplicationConfig)
        self.__app_configs = app_configs
        self.default_is_tiled = default_is_tiled is None and True or default_is_tiled
        self.default_has_border = default_has_border is None and True or default_has_border
        self.default_has_title = default_has_title is None and True or default_has_title
        self.default_is_resizable = default_is_resizable is None and True or default_is_resizable

    def is_tiled(self, window_info):
        for app in self.__app_configs:
            assert isinstance(app, AbstractApplicationConfig)
            res = app.is_tiled(window_info)
            if res is not None:
                return res
        return self.default_is_tiled

    def has_title(self, window_info):
        for app in self.__app_configs:
            assert isinstance(app, AbstractApplicationConfig)
            res = app.has_title(window_info)
            if res is not None:
                return res
        return self.default_has_title

    def has_border(self, window_info):
        for app in self.__app_configs:
            assert isinstance(app, AbstractApplicationConfig)
            res = app.has_border(window_info)
            if res is not None:
                return res
        return self.default_has_border

    def is_resizable(self, window_info):
        for app in self.__app_configs:
            assert isinstance(app, AbstractApplicationConfig)
            res = app.is_resizable(window_info)
            if res is not None:
                return res
        return self.default_is_resizable

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
                 has_border=True,
                 has_title=True,
                 is_tiled=True,
                 is_resizable=True,
                 app_matchers=None):
        super()
        if app_matchers is None:
            app_matchers = tuple()
        elif isinstance(app_matchers, AppMatcher):
            app_matchers = (app_matchers,)
        for matcher in app_matchers:
            assert isinstance(matcher, AppMatcher)

        self.__has_border = has_border
        self.__has_title = has_title
        self.__is_tiled = is_tiled
        self.__is_resizable = is_resizable
        self.__app_matchers = app_matchers

    def has_border(self, window_info):
        for matcher in self.__app_matchers:
            if matcher.matches(window_info):
                return self.__has_border
        return None

    def has_title(self, window_info):
        for matcher in self.__app_matchers:
            if matcher.matches(window_info):
                return self.__has_title
        return None

    def is_tiled(self, window_info):
        for matcher in self.__app_matchers:
            if matcher.matches(window_info):
                return self.__is_tiled
        return None

    def is_resizable(self, window_info):
        for matcher in self.__app_matchers:
            if matcher.matches(window_info):
                return self.__is_resizable
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

    def has_border(self, window_info):
        return None

    def has_title(self, window_info):
        return None

    def is_tiled(self, window_info):
        return None

    def is_resizable(self, window_info):
        return None

    def get_best_portal_match(self, portal_aliases, window_info):
        for app_matcher in self.__app_matchers:
            if app_matcher.matches(window_info):
                # The portal matchers are in-order of preference;
                # if any portal alias matches the first matcher, use
                # that portal alias first.
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
                regex = re.escape(exact)
                if name.endswith("_filename"):
                    regex = r'.*?\\' + regex + '$'
                else:
                    regex = '^' + regex + '$'
                self.re_matchers[name] = re.compile(str(regex), re.IGNORECASE)
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
            if value is None:
                print("ERROR: 'none' value for {0}".format(key))
                continue
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

    def __repr__(self):
        return "AppMatcher({0})".format(repr(self.re_matchers))
