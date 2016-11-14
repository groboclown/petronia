
from ... import config


class ConfigLoadException(Exception):
    def __init__(self, file, section, msg):
        super("Problem loading configuration {0} in {1}: {2}".format(file, section, msg))


def build_config_loader_from_dict(config_name, d, logger):
    """
    Allows building a configuration from a dictionary structure.
    This way, you can use any kind of these data format file types to load
    the configuration.

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

    :param config_name:
    :param d:
    :param logger:
    :return:
    """
    if not isinstance(d, dict):
        raise ConfigLoadException(config_name, "(root)", "Configuration must be a dictionary")
    if 'version' in d:
        v = d['version']
        if v == 1:
            return _load_v1(config_name, d, logger)
    raise ConfigLoadException(config_name, "(root)", "Unknown configuration file version")


def _load_v1(config_name, d, logger):
    if 'workgroups' in d:
        workgroups = _load_work_groups_v1(config_name, d['workgroups'], logger)
    else:
        workgroups = None

    if 'applications' in d:
        applications = _load_applications_v1(config_name, d['applications'], logger)
    else:
        applications = None

    if 'keysets' in d:
        hotkeys = _load_hotkeys_v1(config_name, d['keysets'], logger)
    else:
        hotkeys = None

    if 'chrome' in d:
        chrome = _load_chrome_v1(config_name, d['chrome'], logger)
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

def _load_work_groups_v1(config_name, d, logger):
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

    :param config_name:
    :param d:
    :param logger:
    :return:
    """

    if d is None:
        return config.DisplayWorkGroupsConfig()

    if isinstance(d, str) or isinstance(d, dict):
        raise ConfigLoadException(config_name, ["workgroups"], "Must be a list of dictionaries")

    groups = []
    for group in d:
        if not isinstance(group, dict):
            raise ConfigLoadException(config_name, ["workgroups"], "must be a list of dictionaries")
        name = None
        if 'name' in group and group['name'] is not None:
            if not isinstance(group['name'], str):
                raise ConfigLoadException(config_name, ["workgroups", "name"], "must be string, if given")
            name = group['name']
        display_list = None
        if 'display' in group and group['display'] is not None:
            display_list = _load_work_groups_display_v1(config_name, group['display'], logger)

        if 'layouts' not in group:
            raise ConfigLoadException(config_name, ["workgroups", "layouts"], "must provide layouts in a workgroup")
        layouts = _load_work_groups_layout_v1(config_name, group['layouts'], logger)

        groups.append({
            'name': name,
            'monitors': display_list,
            'workgroup': config.WorkGroupConfig(layouts)
        })

    return config.DisplayWorkGroupsConfig(groups=groups)


def _load_work_groups_display_v1(config_name, d, logger):
    """
    'display': [ //optional
        { // monitor 1
            'width': 1024,
            'height': 768
        }, ...
    ],


    :param config_name:
    :param d:
    :param logger:
    :return:
    """
    if isinstance(d, str) or isinstance(d, dict):
        raise ConfigLoadException(config_name, ['workgroups', 'display'], "must be a list of dictionaries")
    display_list = []
    for display in d:
        if not isinstance(display, dict):
            raise ConfigLoadException(config_name, ['workgroups', 'display'], "must be a list of dictionaries")
        try:
            width = int(display['width'])
        except (ValueError, KeyError):
            raise ConfigLoadException(config_name, ['workgroups', 'display', 'width'], "must be int")
        try:
            height = int(display['height'])
        except (ValueError, KeyError):
            raise ConfigLoadException(config_name, ['workgroups', 'display', 'height'], "must be int")
        display_list.append(config.MonitorResConfig(width, height))

    return display_list


def _load_work_groups_layout_v1(config_name, d, logger):
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

    :param config_name:
    :param d:
    :param logger:
    :return:
    """
    if not isinstance(d, dict):
        raise ConfigLoadException(config_name, ["workgroups", "layouts"], "must be dictionary")
    ret = {}

    for name, layout in d.items():
        if isinstance(layout, str) or isinstance(layout, dict):
            raise ConfigLoadException(config_name, ["workgroups", "layouts", name], "must be list of dictionaries")


    return ret


# ----------------------------------------------------------------------------
# Applications

def _load_applications_v1(config_name, d, logger):
    return config.ApplicationListConfig()


# ----------------------------------------------------------------------------
# Hot Keys

def _load_hotkeys_v1(config_name, d, logger):
    return config.HotKeyConfig()


# ----------------------------------------------------------------------------
# Chrome

def _load_chrome_v1(config_name, d, logger):
    return config.ChromeConfig()
