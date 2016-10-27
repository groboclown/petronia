
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

    applications = config.ApplicationListConfig([
        # Apps that should not  belong to the tiling, because it messes up the
        # display.  These come before the general non-chromed apps, because it
        # they both include a matching entry, but this one contains a more
        # precise entry.

        # If you end up missing an application that should have gone here, and
        # now the dialog is always in a super-size, you'll have to poke around
        # to figure out how to fix it.  For example, the reminder dialog below
        # can be restored to its default size and position by removing the
        # registry key
        # HKEY_CURRENT_USER\Software\Microsoft\Office\(version)\Options\Reminders
        config.ApplicationConfig(is_managed_chrome=False, is_tiled=False, app_matchers=[
            config.AppMatcher(class_re=r'#\d+', title_re=r'\d+ reminder\(s\)', exec_re=r'.*?\\outlook\.exe$'),
        ]),

        # General non-chromed apps.
        config.ApplicationConfig(is_managed_chrome=False, is_tiled=True, app_matchers=[
            config.AppMatcher(exec_re=r'.*?\\firefox\.exe$'),
            config.AppMatcher(exec_re=r'.*?\\chrome\.exe$'),
            config.AppMatcher(exec_re=r'.*?\\explorer\.exe$'),
            config.AppMatcher(exec_re=r'.*?\\outlook\.exe$'),
        ]),
    ])

    # See petronia.util.hotkey_chain for the key names.
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

            "win+pgup => move-window-to-other-portal next",
            "win+pgdn => move-window-to-other-portal previous",

            "win+tab => minimize",

            # Launch a CMD.exe command prompt in a stand alone window.
            "win+launch_app1 => cmd cmd.exe /c start cmd.exe",

            "win+f11 => quit",

            "win+esc => open-start-menu",
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
    chrome.has_title = False
    chrome.portal_chrome_border = {
        'color': 0x404040, 'width': 0,  # 0 width means that it's not drawn.
        'top': 0, 'bottom': 0, 'left': 0, 'right': 0,
    }
    chrome.portal_chrome_active_border = {
        'color': 0x808000, 'width': 0,  # 0 width means that it's not drawn.
        'top': 0, 'bottom': 0, 'left': 0, 'right': 0,
    }

    return config.Config(
        layouts_by_display,
        applications,
        hotkeys,
        command,
        chrome)
