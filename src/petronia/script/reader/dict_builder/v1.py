
from .... import config
from .exceptions import ConfigLoadException
from importlib import import_module


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
                'has-title': true,
                'has-border': true,
                'is-tiled': false,
                'display': '+title +border -tiled',
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

                    'has-title': false,
                    'has-border': true,
                    'is-tiled': false,
                    'display': '-title +border -tiled',
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

        'components': {
            'singletons': [
                {
                    'factory': 'petronia.components.portal_chrome',
                    'settings': {
                        'key': 'value'
                    }
                }
            ],
            'extensions': [
            ]
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

    singletons = None
    extensions = None
    if 'components' in d:
        singletons, extensions = _load_components([*section, 'components'], d['components'])
    component = config.ComponentConfig(singletons=singletons, extensions=extensions)

    # Not configurable yet
    commands = config.CommandConfig()
    shell = config.WindowsShellConfig()

    conf = config.Config(
        workgroups=workgroups,
        applications=applications,
        hotkeys=hotkeys,
        commands=commands,
        component=component,
        shell=shell
    )

    return conf


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

_SNAP_TYPES = {
    'right': ('right', 'center'),
    'left': ('left', 'center'),
    'top': ('center', 'top'),
    'bottom': ('center', 'bottom'),
    'top left': ('left', 'top'),
    'bottom left': ('left', 'bottom'),
    'top right': ('right', 'top'),
    'bottom right': ('right', 'bottom'),
    'center left': ('left', 'center'),
    'center right': ('right', 'center'),
    'top center': ('center', 'top'),
    'bottom center': ('center', 'bottom'),
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
            kids = _key_as_list(sec, part, 'children', False)
            if kids is not None:
                child_splits = _load_layout_list([*sec, 'children'], kids, logger, True)

        layout_def = config.LayoutConfig(name, category, orientation, child_splits)

        snap = _key_as_str(sec, part, 'snap')
        if snap is not None:
            snap = snap.strip().lower()
            if snap not in _SNAP_TYPES:
                raise ConfigLoadException([*sec, 'snap'], 'must be one of {0}, found {1}'.format(
                    _SNAP_TYPES.keys(), snap
                ))
            layout_def.snap_horizontal, layout_def.snap_vertical = _SNAP_TYPES[snap]

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
            'has-title': true,
            'has-border': true,
            'is-tiled': false,
            'display': '+title +border -tiled',
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

                'has-title': true,
                'has-border': true,
                'is-tiled': false,
                'display': '+title +border -tiled',
                'location': [ 'portal 1', 'portal 2', ... ]
            }, ...
        ]
    },

    :param section:
    :param d:
    :return:
    """
    d = _ensure_dict(section, d, False)

    defaults = _parse_app_display([*section, 'defaults'], _key_as_dict(section, d, 'defaults'))

    app_configs = []
    applications = _key_as_list(section, d, 'applications', False)
    for li in range(len(applications)):
        sec = [*section, str(li)]
        app = _ensure_dict(sec, applications[li], False)
        matchers = _load_application_matchers([*sec, 'matchers'], _key_as_list(sec, app, 'matchers', False))
        display = _parse_app_display(sec, app)
        assert isinstance(display, AppDisplay)
        if display.was_set:
            app_configs.append(config.ApplicationChromeConfig(
                has_border=display.has_border,
                has_title=display.has_title,
                is_tiled=display.is_tiled,
                is_resizable=display.is_resizable,
                app_matchers=matchers))
        locations = _key_as_list(sec, app, 'location')
        if locations is not None:
            for ll in range(len(locations)):
                _ensure_str([*sec, 'location', str(ll)], locations[ll], False)
            app_configs.append(config.ApplicationPositionConfig(locations, matchers))

    return config.ApplicationListConfig(
        app_configs,
        default_is_tiled=defaults.is_tiled,
        default_has_border=defaults.has_border,
        default_has_title=defaults.has_title,
        default_is_resizable=defaults.is_resizable)


class AppDisplay(object):
    def __init__(self, is_tiled=None, has_border=None, has_title=None, is_resizable=None):
        self.is_tiled = is_tiled
        self.has_border = has_border
        self.has_title = has_title
        self.is_resizable = is_resizable

    @property
    def was_set(self):
        return not (
            self.is_tiled is None
            and self.has_border is None
            and self.has_title is None
            and self.is_resizable is None
        )


def _parse_app_display(section, d):
    ret = AppDisplay()
    if d is None:
        return ret
    ret.has_title = _key_as_bool(section, d, 'has-title')
    ret.has_border = _key_as_bool(section, d, 'has-border')
    ret.is_tiled = _key_as_bool(section, d, 'is-tiled')
    ret.is_resizable = _key_as_bool(section, d, 'resizable')

    display = _key_as_str(section, d, 'display')
    if display is not None:
        for p in display.strip().lower().split():
            if p[0] == '+':
                val = True
            elif p[0] == '-':
                val = False
            else:
                raise ConfigLoadException(
                    [*section, 'display'], 'each item must start with "+" or "-" (display is `{0}`)'.format(display))
            p = p[1:]
            if p == 'title':
                ret.has_title = val
            elif p == 'border':
                ret.has_border = val
            elif p == 'tiled':
                ret.is_tiled = val
            elif p == 'resize' or p == 'resizable':
                ret.is_resizable = val
            else:
                raise ConfigLoadException([*section, 'display'], 'unknown item `{0}` in display `{1}`'.format(
                    p, display
                ))
    return ret


def _load_application_matchers(section, d):
    """
    'matchers': [
        {   // all of these are optional
            'exec-path': 'blah',
            'exec-path-re': 'blah',
            'class-name': 'blah',
            'class-name-re': 'blah',
            'title': 'blah',
            'title-re': 'blah',
            'module-path': 'blah',
            'module-path-re': 'blah',

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
            title_re=_key_as_str(sec, matcher, 'title-re'),
            module_path=_key_as_str(sec, matcher, 'module-path'),
            module_path_re=_key_as_str(sec, matcher, 'module-path-re'),
            exec_path=_key_as_str(sec, matcher, 'exec-path'),
            exec_path_re=_key_as_str(sec, matcher, 'exec-path-re'),
            class_name=_key_as_str(sec, matcher, 'class-name'),
            class_name_re=_key_as_str(sec, matcher, 'class-name-re'),
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
            ret.parse_exclusive_mode_keys(mode_id, _key_as_dict(sec, mode, 'commands', False))
        else:
            raise ConfigLoadException(sec, '"type" must be one of [hotkey, exclusive], found `{0}`'.format(mode_type))

    return ret


# ----------------------------------------------------------------------------
def _load_components(section, d):
    """
    'components': {
        'singletons': [
            {
                'factory': 'petronia.components.portal_chrome',
                'settings': {
                    'key': 'value'
                }
            }
        ],
        'extensions': {
            'type_a': {
                'factory': 'petronia.components.my_component',
                'settings': {
                    'key': 'value'
                }
            }
        }
    }

    :param section:
    :param d:
    :return:
    """
    singletons = None
    if 'singletons' in d:
        singletons = _load_singleton_components([*section, 'singletons'], _key_as_list(section, d, 'singletons', False))

    extensions = None
    if 'extensions' in d:
        extensions = _load_extension_components([*section, 'extensions'], _key_as_dict(section, d, 'extensions', False))

    return singletons, extensions


def _load_singleton_components(section, singletons):
    ret = []
    for i in range(len(singletons)):
        ret.append(_load_component_factory([*section, str(i)], singletons[i]))
    return ret


def _load_extension_components(section, extensions):
    ret = {}
    for k, desc in extensions.items():
        _ensure_str(section, k, False)
        ret[k] = _load_component_factory([*section, k], desc)
    return ret


def _load_component_factory(section, desc):
    factory_module_name = _key_as_str(section, desc, 'factory', False)
    settings = _key_as_dict(section, desc, 'settings')
    try:
        factory_module = import_module(factory_module_name)
        if not hasattr(factory_module, 'get_factory') or not callable(getattr(factory_module, 'get_factory')):
            raise ConfigLoadException([*section, 'factory'], 'invalid factory module {0}: {1}'.format(
                factory_module_name, 'does not provide function `get_factory`'
            ))
        return getattr(factory_module, 'get_factory')(settings)
    except ImportError as e:
        raise ConfigLoadException([*section, 'factory'], 'could not import module {0}: {1}'.format(
            factory_module_name, repr(e)
        ))


# ----------------------------------------------------------------------------
# Basic utilities


def _key_as_bool(sec, d, k, allow_none=True):
    if k in d:
        return _ensure_bool([*sec, k], d[k], allow_none)
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
    raise ConfigLoadException(sec, 'must be bool, found {0} ({1})'.format(type(v), v))


def _key_as_str(sec, d, k, allow_none=True):
    if k in d:
        return _ensure_str([*sec, k], d[k], allow_none)
    if allow_none:
        return None
    raise ConfigLoadException([*sec, k], 'must be string')


def _ensure_str(sec, v, allow_none=True):
    if v is None:
        if allow_none:
            return True
        raise ConfigLoadException(sec, 'must be string, found None')
    if not isinstance(v, str):
        raise ConfigLoadException(sec, 'must be string, found {0} ({1})'.format(type(v), v))
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
        raise ConfigLoadException(sec, 'must be dictionary, found {0} ({1})'.format(type(d), d))
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
        raise ConfigLoadException(sec, 'must be list, found {0} ({1})'.format(type(v), v))
    if not hasattr(v, '__iter__') or not callable(getattr(v, '__iter__')):
        raise ConfigLoadException(sec, 'must be list, found {0} ({1})'.format(type(v), v))
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
        raise ConfigLoadException(sec, 'must be int, found {0} ({1})'.format(type(v), v))


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
        raise ConfigLoadException(sec, 'must be float, found {0} ({1})'.format(type(v), v))
