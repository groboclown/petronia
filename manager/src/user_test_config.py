
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
        config.ApplicationChromeConfig(is_managed_chrome=False, is_tiled=False, app_matchers=[
            config.AppMatcher(class_name_re=r'#\d+', title_re=r'\d+ reminder\(s\)', exec_path='outlook.exe'),
        ]),

        # General non-chromed apps.  These ones appear on the default screen.
        config.ApplicationChromeConfig(is_managed_chrome=False, is_tiled=True, app_matchers=[
            config.AppMatcher(exec_path='firefox.exe'),
            config.AppMatcher(exec_path='chrome.exe'),
            config.AppMatcher(exec_path='explorer.exe'),
            config.AppMatcher(exec_path='outlook.exe'),
        ]),

        # If there is enough space, these go to the big side panel.
        # If that isn't in the workgroup, then these are put int the
        # default layout.
        config.ApplicationPositionConfig(
            portal_names=['left'],
            app_matchers=[
                config.AppMatcher(exec_path='firefox.exe'),
                config.AppMatcher(exec_path='chrome.exe'),
                config.AppMatcher(exec_path='explorer.exe'),
                config.AppMatcher(exec_path='outlook.exe'),
            ]
        ),
    ])

    # See petronia.util.hotkey_chain for the key names.
    hotkeys = config.HotKeyConfig()
    hotkeys.parse_hotkey_mode_keys(
        config.DEFAULT_MODE,
        [
            # Mode tests
            "win+~ => " + config.MODE_CHANGE_COMMAND + " simple-windows-mode",
            "win+F11 => " + config.MODE_CHANGE_COMMAND + " resize-window-mode",

            "win+up => move-window-to-other-portal north",
            "win+down => move-window-to-other-portal south",
            "win+left => move-window-to-other-portal west",
            "win+right => move-window-to-other-portal east",

            # "next" and "previous" window movement bypasses how layouts
            # think about directions, and just moves in order through the
            # portals.
            "win+pgup => move-window-to-other-portal next",
            "win+pgdn => move-window-to-other-portal previous",

            "win+tab => minimize",

            # Redefine the Windows lock screen keystroke.
            # This doesn't actually do anything, because Windows reads in
            # the Win+L key combination before anything can interrupt it.
            "win+l => lock-screen",

            # Launch a CMD.exe command prompt in a stand alone window.
            "win+launch_app1 => cmd cmd.exe /c start cmd.exe",

            # Launch a CMD with nice colors and an initial directory.
            # Note that the backslash character must be escaped, once for
            # being within a Python string, and again due to the parsing of the command
            # line args, so a total of 4 backslashes to equal 1 real backslash.
            'win+p => cmd cmd.exe /c start cmd.exe /E:ON /V:ON /T:17 /K cd \\\\',

            "win+f4 => quit",

            # load-config, with no arguments, just reloads the current config file.
            "win+alt+f2 => load-config",

            "win+esc => open-start-menu",

            # Test, for screen sharing of tutorials
            "win+shift+f10 => toggle-show-key-action 0xffffff 0x000000 bottom-left"
        ],
        block_win_key=True  # block the windows key, because we remapped it to win+esc
        # False
    )

    # Just use Windows without any special parsing.  The windows key acts as Windows intends.
    hotkeys.parse_hotkey_mode_keys(
        "simple-windows-mode",
        [
            "win+~ => " + config.MODE_CHANGE_COMMAND + " " + config.DEFAULT_MODE,
        ],
        block_win_key=False
    )

    # "simple mode" is exclusive mode for this application. It sucks in all
    # input.  This is useful for an operation that controls how Petronia
    # works, such as manipulating the layout.
    hotkeys.parse_simple_mode_keys(
        "resize-window-mode",
        [
            "esc => " + config.MODE_CHANGE_COMMAND + " " + config.DEFAULT_MODE,
            "enter => " + config.MODE_CHANGE_COMMAND + " " + config.DEFAULT_MODE,
            "up => resize 0 -16",
            "down => resize 0 16",
            "left => resize -16 0",
            "right => resize 16 0",
            "j => resize 0 -1",
            "k => resize 0 1",
            "h => resize -1 0",
            "l => resize 1 0",

            # Numpad equivalents
            "separator => " + config.MODE_CHANGE_COMMAND + " " + config.DEFAULT_MODE,
            "numpad8 => resize 0 -4",
            "numpad2 => resize 0 4",
            "numpad4 => resize -4 0",
            "numpad6 => resize 4 0",
            "add => resize 4 4",
            "subtract => resize -4 -4",
        ]
    )

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
        workgroups=layouts_by_display,
        applications=applications,
        hotkeys=hotkeys,
        chrome=chrome)
