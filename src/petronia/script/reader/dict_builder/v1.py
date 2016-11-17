
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

        'applications': [
            {
                'matchers': [
                    {
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
            },
        ],

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

        'chrome': {
            // todo
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

    if 'applications' in d:
        applications = _load_applications([*section, 'applications'], d['applications'], logger)
    else:
        applications = None

    if 'keysets' in d:
        hotkeys = _load_hotkeys([*section, 'keysets'], d['keysets'], logger)
    else:
        hotkeys = None

    if 'chrome' in d:
        chrome = _load_chrome([*section, 'chrome'], d['chrome'], logger)
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

    if d is None:
        return config.DisplayWorkGroupsConfig()

    if isinstance(d, str) or isinstance(d, dict):
        raise ConfigLoadException(section, "Must be a list of dictionaries")

    groups = []
    for group in d:
        if not isinstance(group, dict):
            raise ConfigLoadException(section, "must be a list of dictionaries")
        name = None
        if 'name' in group and group['name'] is not None:
            if not isinstance(group['name'], str):
                raise ConfigLoadException([*section, "name"], "must be string, if given")
            name = group['name']
        display_list = None
        if 'display' in group and group['display'] is not None:
            display_list = _load_work_groups_display([*section, 'display'], group['display'], logger)

        if 'layouts' not in group:
            raise ConfigLoadException([*section, 'layouts'], "must provide layouts in a workgroup")
        layouts = _load_work_groups_layout([*section, 'layouts'], group['layouts'], logger)

        groups.append({
            'name': name,
            'monitors': display_list,
            'workgroup': config.WorkGroupConfig(layouts)
        })

    return config.DisplayWorkGroupsConfig(groups=groups)


def _load_work_groups_display(section, d, logger):
    """
    'display': [ //optional
        { // monitor 1
            'width': 1024,
            'height': 768
        }, ...
    ],


    :param section:
    :param d:
    :param logger:
    :return:
    """
    if isinstance(d, str) or isinstance(d, dict):
        raise ConfigLoadException(section, "must be a list of dictionaries")
    display_list = []
    for display in d:
        if not isinstance(display, dict):
            raise ConfigLoadException(section, "must be a list of dictionaries")
        try:
            width = int(display['width'])
        except (ValueError, KeyError):
            raise ConfigLoadException([*section, 'width'], "must be int")
        try:
            height = int(display['height'])
        except (ValueError, KeyError):
            raise ConfigLoadException([*section, 'height'], "must be int")
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
    if not isinstance(d, dict):
        raise ConfigLoadException(section, "must be dictionary")
    ret = {}

    for name, layout in d.items():
        if isinstance(layout, str) or isinstance(layout, dict):
            raise ConfigLoadException([*section, name], "must be list of dictionaries")
        setup = _load_layout_list([*section, name], layout, logger, False)
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
    if isinstance(layout_list, dict) or isinstance(layout_list, str):
        raise ConfigLoadException(section, "must be list of dictionaries")
    ret = []
    for li in range(len(layout_list)):
        sec = [*section, str(li)]
        part = layout_list[li]
        if not isinstance(part, dict):
            raise ConfigLoadException(sec, "must be dictionary")
        name = 'name' in part and part['name'] or None
        if name is not None and not isinstance(name, str):
            raise ConfigLoadException([*sec, 'name'], "must be string")
        if 'type' not in part or not isinstance(part['type'], str):
            raise ConfigLoadException([*sec, 'type'], "must be string")
        p_type = part['type'].strip().lower()
        if p_type not in _LAYOUT_TYPES:
            raise ConfigLoadException([*sec, 'type'], 'must be one of {0}, found {1}'.format(
                _LAYOUT_TYPES.keys(), p_type))
        category, orientation = _LAYOUT_TYPES[p_type]
        child_splits = None
        if 'children' in part:
            kids = part['children']
            sec = [*sec, kids]
            if kids is None or isinstance(kids, dict) or isinstance(kids, str):
                raise ConfigLoadException(sec, 'must be list')
            child_splits = _load_layout_list([*sec, 'children'], kids, logger, True)
        layout_def = config.LayoutConfig(name, category, orientation, child_splits)
        if as_child_splits:
            size = 1
            if 'size' in part:
                size = int(part['size'])
            ret.append(config.ChildSplitConfig(size, layout_def))
        else:
            ret.append(layout_def)

    return ret


# ----------------------------------------------------------------------------
# Applications

def _load_applications(section, d, logger):
    """
    'applications': [
    { // optional
        'default-setup': {
            'is-chromed': true,
            'is-tiled': false,
            'display': '+chromed -tiled',
        }
    },
    {
        'matchers': [
            {
                'exec_path': 'blah',
                'exec_path_re': 'blah',
                'class_name': 'blah',
                'class_name_re': 'blah',
                'title': 'blah',
                'title_re': 'blah',

                'matches': true // optional, defaults to true
            }
        ],

        'is-chromed': true,
        'is-tiled': false,
        'display': '+chromed -tiled',
        'location': [ 'portal 1', 'portal 2', ... ]
    },
    ],

    :param section:
    :param d:
    :param logger:
    :return:
    """
    if d is None or isinstance(d, str) or isinstance(d, dict):
        raise ConfigLoadException(section, 'must be a list of dictionaries')
    app_configs = []
    default_is_tiled = True
    default_is_managed_chrome = True

    for li in range(len(d)):
        sec = [*section, str(li)]
        app = d[li]
        if not isinstance(app, dict):
            raise ConfigLoadException(sec, 'must be dictionary')
        if 'default-setup' in app:
            is_managed_chrome, is_tiled, was_set = _parse_app_display(sec, app)
            if was_set:
                default_is_managed_chrome = is_managed_chrome
                default_is_tiled = is_tiled
        else:
            msec = [*sec, 'matchers']
            if 'matchers' not in app:
                raise ConfigLoadException(msec, 'must be list of dictionaries')
            matchers = _load_application_matchers(msec, app['matchers'], logger)
            is_chromed, is_tiled, was_set = _parse_app_display(sec, app)
            if was_set:
                app_configs.append(config.ApplicationChromeConfig(
                    is_managed_chrome=is_chromed, is_tiled=is_tiled, app_matchers=matchers))
            if 'location' in app:
                app_configs.append(config.ApplicationPositionConfig(app['location'], matchers))

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


def _load_application_matchers(section, d, logger):
    """
    'matchers': [
        {   // all of these are optional
            'exec_path': 'blah',
            'exec_path_re': 'blah',
            'class_name': 'blah',
            'class_name_re': 'blah',
            'title': 'blah',
            'title_re': 'blah',

            'matches': true // optional, defaults to true
        }
    ],

    :param section:
    :param d:
    :param logger:
    :return:
    """
    if d is None or isinstance(d, str) or isinstance(d, dict):
        raise ConfigLoadException(section, 'must be list of dictionaries')
    raise NotImplementedError()


# ----------------------------------------------------------------------------
# Hot Keys

def _load_hotkeys(section, d, logger):
    return config.HotKeyConfig()


# ----------------------------------------------------------------------------
# Chrome

def _load_chrome(config_name, d, logger):
    return config.ChromeConfig()
