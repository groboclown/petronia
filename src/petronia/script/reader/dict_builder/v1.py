
from .... import config
from .exceptions import ConfigLoadException


def load_config(section, d, logger):
    """
    Format:

    ```
    {
        'version': 1,

        'workgroups': [
            {
                'name': 'optional', // 'default' has special meaning
                'display': [ //optional
                    { // monitor 1
                        'width': 1024,
                        'height': 768
                    }, ...
                ],

                'layouts': {
                    'layout 1': [
                        {
                            'name': 'left', // optional
                            'type': 'vertical split',
                            'children': [
                                {
                                    'name': 'left-top', // optional
                                    'type': 'portal'
                                }, ...
                            ]
                        }, ...
                    ], ...
                }
            }
        ],

        'application-setup': {
            'defaults': {
                'is-chromed': true,
                'is-tiled': false,
                'display': '+chromed -tiled',
            },
            'applications': [
                {
                    'matchers': [
                        {
                            'module_path': 'blah',
                            'module_path_re': 'blah',
                            'exec_path': 'blah',
                            'exec_path_re': 'blah',
                            'class_name': 'blah',
                            'class_name_re': 'blah',
                            'title': 'blah',
                            'title_re': 'blah',

                            'matches': true
                        }
                    ],

                    'is-chromed': true,
                    'is-tiled': false,
                    'display': '+chromed -tiled',
                    'location': [ 'portal 1', 'portal 2', ... ]
                }, ...
            ]
        },

        'keysets': {
            'mode 1': {
                'type': 'hotkey',
                'options': {
                    'block-win-key': false
                },
                'commands': {
                    'win+f1': ['command', 'text']
                }
                // todo
            },
            'mode 2': {
                'type': 'exclusive',
                'commands': {
                    'f1': ['cmd', 'explorer.exe']
                }
            }, ...
        },

        'chrome': { // all optional
            'border-width': 1,
            'border-padding': 1,
            'border-color': '#ff00dd',
            'scrollbar-width': 4,
            'scrollbar-height': 4,
            'has-title': false,
            'has-resize-border': true,
            'flash-count': 3,
            'flash-wait-seconds': 0.5,
        }
    }
    ```

    :param section:
    :param d:
    :param logger:
    :return:
    """
    if 'workgroups' in d:
        workgroups = _load_work_groups([*section, 'workgroups'], d['workgroups'], logger)
    else:
        workgroups = None

    if 'application-setup' in d:
        applications = _load_application_setup([*section, 'application-setup'], d['application-setup'])
    else:
        applications = None

    if 'keysets' in d:
        hotkeys = _load_hotkeys([*section, 'keysets'], d['keysets'])
    else:
        hotkeys = None

    if 'chrome' in d:
        chrome = _load_chrome([*section, 'chrome'], d['chrome'])
    else:
        chrome = None

    # Not configurable yet
    commands = config.CommandConfig()
    component = config.ComponentConfig()
    shell = config.WindowsShellConfig()

    conf = config.Config(
        workgroups=workgroups,
        applications=applications,
        hotkeys=hotkeys,
        commands=commands,
        chrome=chrome,
        component=component,
        shell=shell
    )

    def loader():
        return conf

    return loader


# ----------------------------------------------------------------------------
# work groups

def _load_work_groups(section, d, logger):
    """
    'workgroups': [
        {
            'display': [ //optional
                { // monitor 1
                    'width': 1024,
                    'height': 768
                }, ...
            ],

            'layouts': {
                'layout 1': [
                    {
                        'name': 'left', // optional
                        'type': 'vertical split',
                        'children': [
                            {
                                'name': 'left-top', // optional
                                'type': 'portal'
                            }, ...
                        ]
                    }, ...
                ], ...
            }
        }
    ]

    :param section:
    :param d:
    :param logger:
    :return:
    """

    d = _ensure_list(section, d)
    if d is None:
        return config.DisplayWorkGroupsConfig()

    groups = []
    for li in range(len(d)):
        sec = [*section, str(li)]
        group = _ensure_dict(sec, d[li])
        name = _key_as_str(sec, group, 'name')
        display_list = _load_work_groups_display([*sec, 'display'], _key_as_list(sec, group, 'display'))

        layouts = _load_work_groups_layout([*sec, 'layouts'], _key_as_dict(sec, group, 'layouts', False), logger)

        groups.append({
            'name': name,
            'monitors': display_list,
            'workgroup': config.WorkGroupConfig(layouts)
        })

    return config.DisplayWorkGroupsConfig(groups=groups)


def _load_work_groups_display(section, d):
    """
    'display': [ //optional
        { // monitor 1
            'width': 1024,
            'height': 768
        }, ...
    ],


    :param section:
    :param d:
    :return:
    """
    d = _ensure_list(section, d)
    if d is None:
        return None

    display_list = []
    for li in range(len(d)):
        sec = [*section, str(li)]
        display = _ensure_dict(sec, d[li])
        width = _key_as_int(sec, display, 'width', False)
        height = _key_as_int(sec, display, 'height', False)
        display_list.append(config.MonitorResConfig(width, height))

    return display_list


def _load_work_groups_layout(section, d, logger):
    """
    'layouts': {
        'layout 1': [
            {
                'name': 'left', // optional
                'type': 'vertical split',
                'children': [
                    {
                        'name': 'left-top', // optional
                        'type': 'portal'
                    }, ...
                ]
            }, ...
        ], ...
    }

    :param section:
    :param d:
    :param logger:
    :return:
    """
    d = _ensure_dict(section, d)
    ret = {}

    for name, layout in d.items():
        sec = [*section, name]
        layout = _ensure_list(sec, layout, False)
        setup = _load_layout_list(sec, layout, logger, False)
        ret[name] = setup

    return ret


_LAYOUT_TYPES = {
    'vertical split': ('split-layout', config.ORIENTATION_VERTICAL),
    'horizontal split': ('split-layout', config.ORIENTATION_HORIZONTAL),
    'portal': ('portal', None)
}


def _load_layout_list(section, layout_list, logger, as_child_splits):
    """
    'children': [
        {
            'name': 'left', // optional
            'type': 'vertical split',
            'children': [
                {
                    'name': 'left-top', // optional
                    'type': 'portal'
                }, ...
            ]
        }, ...
    ], ...

    :param section:
    :param layout_list:
    :param logger:
    :return:
    """
    layout_list = _ensure_list(section, layout_list, False)
    ret = []
    for li in range(len(layout_list)):
        sec = [*section, str(li)]
        part = _ensure_dict(sec, layout_list[li], False)
        name = _key_as_str(sec, part, 'name')
        p_type = _key_as_str(sec, part, 'type', False).strip().lower()
        if p_type not in _LAYOUT_TYPES:
            raise ConfigLoadException([*sec, 'type'], 'must be one of {0}, found {1}'.format(
                _LAYOUT_TYPES.keys(), p_type))
        category, orientation = _LAYOUT_TYPES[p_type]
        child_splits = None
        if 'children' in part:
            kids = _key_as_dict(sec, part, 'children', False)
            if kids is not None:
                child_splits = _load_layout_list([*sec, 'children'], kids, logger, True)
        layout_def = config.LayoutConfig(name, category, orientation, child_splits)
        if as_child_splits:
            size = _key_as_int(sec, part, 'size')
            if size is None:
                size = 1
            ret.append(config.ChildSplitConfig(size, layout_def))
        else:
            ret.append(layout_def)

    return ret


# ----------------------------------------------------------------------------
# Applications

def _load_application_setup(section, d):
    """
    'application-setup': {
        'defaults': {
            'is-chromed': true,
            'is-tiled': false,
            'display': '+chromed -tiled',
        },
        'applications': [
            {
                'matchers': [
                    {
                        'module_path': 'blah',
                        'module_path_re': 'blah',
                        'exec_path': 'blah',
                        'exec_path_re': 'blah',
                        'class_name': 'blah',
                        'class_name_re': 'blah',
                        'title': 'blah',
                        'title_re': 'blah',

                        'matches': true
                    }
                ],

                'is-chromed': true,
                'is-tiled': false,
                'display': '+chromed -tiled',
                'location': [ 'portal 1', 'portal 2', ... ]
            }, ...
        ]
    },

    :param section:
    :param d:
    :return:
    """
    d = _ensure_list(section, d, False)

    default_is_tiled = True
    default_is_managed_chrome = True
    defaults = _key_as_dict(section, d, 'defaults')
    if defaults is not None:
        is_managed_chrome, is_tiled, was_set = _parse_app_display([*section, 'defaults'], defaults)
        if was_set:
            default_is_managed_chrome = is_managed_chrome
            default_is_tiled = is_tiled

    app_configs = []
    applications = _key_as_list(section, d, 'applications', False)
    for li in range(len(applications)):
        sec = [*section, str(li)]
        app = _ensure_dict(sec, applications[li], False)
        matchers = _load_application_matchers([*sec, 'matchers'], _key_as_list(sec, app, 'matchers', False))
        is_chromed, is_tiled, was_set = _parse_app_display(sec, app)
        if was_set:
            app_configs.append(config.ApplicationChromeConfig(
                is_managed_chrome=is_chromed, is_tiled=is_tiled, app_matchers=matchers))
        locations = _key_as_list(sec, app, 'location')
        if locations is not None:
            for ll in range(len(locations)):
                _ensure_str([*sec, 'location', str(ll)], locations[ll], False)
            app_configs.append(config.ApplicationPositionConfig(locations, matchers))

    return config.ApplicationListConfig(
        app_configs,
        default_is_tiled=default_is_tiled,
        default_is_managed_chrome=default_is_managed_chrome)


def _parse_app_display(section, d):
    is_chromed = False
    is_tiled = False
    was_set = False
    if 'is-chromed' in d:
        if not isinstance(d['is-chromed'], bool):
            raise ConfigLoadException([*section, 'is-chromed'], 'must be boolean')
        is_chromed = d['is-chromed']
        was_set = True
    if 'is-tiled' in d:
        if not isinstance(d['is-tiled'], bool):
            raise ConfigLoadException([*section, 'is-tiled'], 'must be boolean')
        is_chromed = d['is-tiled']
        was_set = True

    if 'display' in d:
        display = d['display']
        if not isinstance(display, str):
            raise ConfigLoadException([*section, 'display'], 'must be string')
        for p in display.strip().lower().split():
            if p == '+chromed':
                is_chromed = True
                was_set = True
            elif p == '-chromed':
                is_chromed = False
                was_set = True
            elif p == '+tiled':
                is_tiled = True
                was_set = True
            elif p == '-tiled':
                is_tiled = False
                was_set = True
    return is_chromed, is_tiled, was_set


def _load_application_matchers(section, d):
    """
    'matchers': [
        {   // all of these are optional
            'exec_path': 'blah',
            'exec_path_re': 'blah',
            'class_name': 'blah',
            'class_name_re': 'blah',
            'title': 'blah',
            'title_re': 'blah',
            'module_path': 'blah',
            'module_path_re': 'blah',

            'matches': true // optional, defaults to true
        }
    ],

    :param section:
    :param d:
    :return:
    """
    d = _ensure_list(section, d, False)

    ret = []
    for li in range(len(d)):
        sec = [*section, str(li)]
        matcher = _ensure_dict(sec, d[li], False)
        matches = _key_as_bool(sec, matcher, 'matches')
        matches = matches is None and True or matches
        ret.append(config.AppMatcher(
            match_returns=matches,
            title=_key_as_str(sec, matcher, 'title'),
            title_re=_key_as_str(sec, matcher, 'title_re'),
            module_path=_key_as_str(sec, matcher, 'module_path'),
            module_path_re=_key_as_str(sec, matcher, 'module_path_re'),
            exec_path=_key_as_str(sec, matcher, 'exec_path'),
            exec_path_re=_key_as_str(sec, matcher, 'exec_path_re'),
            class_name=_key_as_str(sec, matcher, 'class_name'),
            class_name_re=_key_as_str(sec, matcher, 'class_name_re'),
        ))
    return ret


# ----------------------------------------------------------------------------
# Hot Keys

def _load_hotkeys(section, d):
    """
        'keysets': {
            'mode 1': {
                'type': 'hotkey',
                'options': {
                    'block-win-key': false
                },
                'commands': {
                    'win+f1': ['command', 'text']
                }
                // todo
            },
            'mode 2': {
                'type': 'exclusive',
                'commands': {
                    'f1': ['cmd', 'explorer.exe']
                }
            }, ...
        },


    :param section:
    :param d:
    :return:
    """
    ret = config.HotKeyConfig()
    d = _ensure_dict(section, d)
    if d is None:
        return ret

    for mode_id, mode in d.items():
        sec = [*section, mode_id]
        mode = _ensure_dict(sec, mode, False)
        mode_type = _key_as_str(sec, mode, 'type', False).strip().lower()
        if mode_type == 'hotkey':
            options = _key_as_dict(sec, mode, 'options')
            block_win_key = None
            if options is not None:
                block_win_key = _key_as_bool([*sec, 'options'], options, 'block-win-key')
            block_win_key = block_win_key is None and False or block_win_key
            ret.parse_hotkey_mode_keys(mode_id, _key_as_dict(sec, mode, 'commands', False), block_win_key=block_win_key)
        elif mode_type == 'exclusive':
            ret.parse_simple_mode_keys(mode_id, _key_as_dict(sec, mode, 'commands', False))
        else:
            raise ConfigLoadException(sec, '"type" must be one of [hotkey, exclusive], found `{0}`'.format(mode_type))

    return ret


# ----------------------------------------------------------------------------
# Chrome

def _load_chrome(section, d):
    """
    'chrome': { // all optional
        'border-width': 1,
        'border-padding': 1,
        'border-color': '#ff00dd',
        'scrollbar-width': 4,
        'scrollbar-height': 4,
        'has-title': false,
        'has-resize-border': true,
        'flash-count': 3,
        'flash-wait-seconds': 0.5,
    }

    :param section:
    :param d:
    :return:
    """
    ret = config.ChromeConfig()

    d = _ensure_dict(section, d)
    if d is None:
        return ret

    border_width = _key_as_int(section, d, 'border-width')
    if border_width is not None:
        ret.border_width = border_width

    border_padding = _key_as_int(section, d, 'border-padding')
    if border_padding is not None:
        ret.border_padding = border_padding

    border_color = _key_as_int(section, d, 'border-color')
    if border_color is not None:
        ret.border_color = border_color

    scrollbar_width = _key_as_int(section, d, 'scrollbar-width')
    if scrollbar_width is not None:
        ret.scrollbar_width = scrollbar_width

    scrollbar_height = _key_as_int(section, d, 'scrollbar-height')
    if scrollbar_width is not None:
        ret.scrollbar_height = scrollbar_height

    has_title = _key_as_bool(section, d, 'has-title')
    if has_title is not None:
        ret.has_title = has_title

    has_resize_border = _key_as_bool(section, d, 'has-resize-border')
    if has_resize_border is not None:
        ret.has_resize_border = has_resize_border

    flash_count = _key_as_int(section, d, 'flash-count')
    if flash_count is not None:
        ret.flash_count = flash_count

    flash_wait_seconds = _key_as_float(section, d, 'flash-wait-seconds')
    if flash_wait_seconds is not None:
        ret.flash_wait_seconds = flash_wait_seconds

    # Border definition is updated by the border object.

    return ret


# ----------------------------------------------------------------------------
# Basic utilities


def _key_as_bool(sec, d, k, allow_none=True):
    if k in d:
        return _ensure_bool([*sec, k], d, allow_none)
    if allow_none:
        return None
    raise ConfigLoadException([*sec, k], 'must be bool')


def _ensure_bool(sec, v, allow_none=True):
    if v is None:
        if allow_none:
            return True
        raise ConfigLoadException(sec, 'must be bool, found None')
    if isinstance(v, str):
        v2 = v.strip().lower()
        if v2 in {'true', 'on', 'yes'}:
            return True
        if v2 in {'false', 'off', 'no'}:
            return False
        raise ConfigLoadException(sec, 'must be bool, found `{0}`'.format(v))
    if isinstance(v, bool):
        return v
    raise ConfigLoadException(sec, 'must be bool, found {0}'.format(type(v)))


def _key_as_str(sec, d, k, allow_none=True):
    if k in d:
        return _ensure_str([*sec, k], d, allow_none)
    if allow_none:
        return None
    raise ConfigLoadException([*sec, k], 'must be string')


def _ensure_str(sec, v, allow_none=True):
    if v is None:
        if allow_none:
            return True
        raise ConfigLoadException(sec, 'must be string, found None')
    if not isinstance(v, str):
        raise ConfigLoadException(sec, 'must be string, found {0}'.format(type(v)))
    return v


def _key_as_dict(sec, d, k, allow_none=True):
    if k in d:
        return _ensure_dict([*sec, k], d[k], allow_none)
    if allow_none:
        return None
    raise ConfigLoadException([*sec, k], 'must be dictionary')


def _ensure_dict(sec, d, allow_none=True):
    if d is None:
        if allow_none:
            return True
        raise ConfigLoadException(sec, 'must be dictionary, found None')
    if not isinstance(d, dict):
        raise ConfigLoadException(sec, 'must be dictionary, found {0}'.format(type(d)))
    return d


def _key_as_list(sec, d, k, allow_none=True):
    if k in d:
        return _ensure_list([*sec, k], d[k], allow_none)
    if allow_none:
        return None
    raise ConfigLoadException([*sec, k], 'must be list')


def _ensure_list(sec, v, allow_none=True):
    if v is None:
        if allow_none:
            return None
        raise ConfigLoadException(sec, 'must be list, found None')
    if v is None or isinstance(v, str) or isinstance(v, dict):
        raise ConfigLoadException(sec, 'must be list, found {0}'.format(type(v)))
    if not hasattr(v, '__iter__') or not callable(getattr(v, '__iter__')):
        raise ConfigLoadException(sec, 'must be list, found {0}'.format(type(v)))
    return v


def _key_as_int(sec, d, k, allow_none=True):
    if k in d:
        return _ensure_int([*sec, k], d[k], allow_none)
    if allow_none:
        return None
    raise ConfigLoadException([*sec, k], 'must be int')


def _ensure_int(sec, v, allow_none=True):
    if v is None:
        if allow_none:
            return None
        raise ConfigLoadException(sec, 'must be int, found None')
    try:
        if isinstance(v, str) and v.strip()[0] == '#':
            return int(v.strip()[1:], 16)
        return int(v)
    except ValueError:
        raise ConfigLoadException(sec, 'must be int, found {0}'.format(type(v)))


def _key_as_float(sec, d, k, allow_none=True):
    if k in d:
        return _ensure_float([*sec, k], d[k], allow_none)
    if allow_none:
        return None
    raise ConfigLoadException([*sec, k], 'must be float')


def _ensure_float(sec, v, allow_none=True):
    if v is None:
        if allow_none:
            return None
        raise ConfigLoadException(sec, 'must be float, found None')
    try:
        return float(v)
    except ValueError:
        raise ConfigLoadException(sec, 'must be float, found {0}'.format(type(v)))
