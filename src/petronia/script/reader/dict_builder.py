
from ... import config


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

    :param d:
    :param logger:
    :return:
    """
    assert isinstance(d, dict)
    if 'version' in d:
        v = d['version']
        if v == 1:
            return _load_v1(config_name, d, logger)
    logger.error("Unknown config file version for {0}".format(config_name))


def _load_v1(config_name, d, logger):
    if 'workgroups' in d:
        workgroups = _load_workgroups_v1(d['workgroups'], logger)
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


def _load_workgroups_v1(config_name, d, logger):
    return config.DisplayWorkGroupsConfig()


def _load_applications_v1(config_name, d, logger):
    return config.ApplicationListConfig()


def _load_hotkeys_v1(config_name, d, logger):
    return config.HotKeyConfig()


def _load_chrome_v1(config_name, d, logger):
    return config.ChromeConfig()
