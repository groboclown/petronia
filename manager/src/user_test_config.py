
from petronia import config


def load_config():
    layouts_by_display = config.DisplayWorkGroupsConfig(groups=[{
        'name': 'laptop-screen',
        'monitors': [config.MonitorResConfig(0, 1366, 768, False)],
        'workgroup': config.WorkGroupConfig({
            'default': [config.LayoutConfig('default', 'split-layout', config.ORIENTATION_HORIZONTAL, [
                # Initial window is a floating full-screen
                config.ChildSplitConfig(0, config.LayoutConfig('main', 'portal', None, None)),

                config.ChildSplitConfig(1, config.LayoutConfig('left', 'portal', None, None)),
                config.ChildSplitConfig(1, config.LayoutConfig('right', 'split-layout', config.ORIENTATION_VERTICAL, [
                    # Testing out split navigation.
                    # Looks like a single nagigation request is triggering mutiple moves.s
                    config.ChildSplitConfig(5, config.LayoutConfig('right-top', 'portal', None, None)),
                    config.ChildSplitConfig(1, config.LayoutConfig('right-bottom', 'portal', None, None)),
                ]))
            ])]
        })
    }, {
        'name': '2-monitors, docked',
        'monitors': [
            config.MonitorResConfig(0, 1920, 1080, False),
            config.MonitorResConfig(1, 1280, 1024, False)
        ],
        'workgroup': config.WorkGroupConfig({
            'default': [
                config.LayoutConfig('default', 'split-layout', config.ORIENTATION_HORIZONTAL, [
                    config.ChildSplitConfig(3, config.LayoutConfig('web', 'portal', None, None)),
                    config.ChildSplitConfig(2, config.LayoutConfig('irc', 'split-layout', config.ORIENTATION_VERTICAL, [
                        config.ChildSplitConfig(3, None),
                        config.ChildSplitConfig(1, None),
                    ]))
                ]),
                config.LayoutConfig('left', 'split-layout', config.ORIENTATION_HORIZONTAL, [
                    config.ChildSplitConfig(1, config.LayoutConfig('main', 'portal', None, None)),
                ]),
            ]
        })
    }, {
        'name': 'remote desktop 1024x768',
        'monitors': [config.MonitorResConfig(0, 1024, 768, False)],
        'workgroup': config.WorkGroupConfig({
            'default': [config.LayoutConfig('default', 'split-layout', config.ORIENTATION_HORIZONTAL, [
                config.ChildSplitConfig(3, config.LayoutConfig('main', 'portal', None, None)),
                config.ChildSplitConfig(2, config.LayoutConfig('right', 'split-layout', config.ORIENTATION_VERTICAL, [
                    config.ChildSplitConfig(3, None),
                    config.ChildSplitConfig(2, None),
                ]))
            ])]
        })
    }])

    application = config.ApplicationConfig(managed_chome_not_matchers=[
        config.AppMatcher(exec_re=r'.*?\\firefox.exe$'),
        config.AppMatcher(exec_re=r'.*?\\chrome.exe$'),
        config.AppMatcher(exec_re=r'.*?\\outlook.exe$'),
        config.AppMatcher(exec_re=r'.*?\\explorer.exe$'),
    ])

    hotkeys = config.HotKeyConfig()
    hotkeys.parse_hotkey_mode_keys(
        config.DEFAULT_MODE,
        [
            # Mode tests
            "win+f1 => " + config.MODE_CHANGE_COMMAND + " mode1",
            "win+f2 => " + config.MODE_CHANGE_COMMAND + " mode2",

            "win+up => move-window-to-other-portal north",
            "win+down => move-window-to-other-portal south",
            "win+left => move-window-to-other-portal west",
            "win+right => move-window-to-other-portal east",

            "win+f11 => quit",

            "win+esc => open-start-menu",

            # TODO include command to open the start menu,
            # and block the win key from being passed on.
        ],
        True  # block the windows key, because we remapped it to win+esc
        # False
    )
    hotkeys.parse_simple_mode_keys(
        "mode1",
        [
            "esc => " + config.MODE_CHANGE_COMMAND + " " + config.DEFAULT_MODE,
            "f2 => " + config.MODE_CHANGE_COMMAND + " mode2",
            "f11 => quit",
        ]
    )
    hotkeys.parse_simple_mode_keys(
        "mode2",
        [
            "esc => " + config.MODE_CHANGE_COMMAND + " " + config.DEFAULT_MODE,
            "f1 => " + config.MODE_CHANGE_COMMAND + " mode1",
            "f11 => quit",
        ]
    )

    command = config.CommandConfig()

    chrome = config.ChromeConfig()

    return config.Config(
        layouts_by_display,
        application,
        hotkeys,
        command,
        chrome)
