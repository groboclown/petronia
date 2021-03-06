
from petronia import config


def load_config():
    layouts_by_display = config.DisplayWorkGroupsConfig(groups=[{
        'name': 'laptop-screen',
        'monitors': [config.MonitorResConfig(1366, 768)],
        'workgroup': config.WorkGroupConfig({
            'default': [config.LayoutConfig('primary', 'split-layout', config.ORIENTATION_HORIZONTAL, [
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
            config.MonitorResConfig(1920, 1080),
            config.MonitorResConfig(1280, 1024)
        ],
        'workgroup': config.WorkGroupConfig({
            'default': [
                config.LayoutConfig('primary', 'split-layout', config.ORIENTATION_HORIZONTAL, [
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
        'monitors': [config.MonitorResConfig(1024, 768)],
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

    applications = config.ApplicationListConfig(
        default_is_tiled=True,
        default_has_border=False,
        default_has_title=False,
        app_configs=[
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
            config.ApplicationChromeConfig(has_title=True, has_border=True, is_tiled=False, app_matchers=[
                config.AppMatcher(class_name_re=r'#\d+', title_re=r'\d+ reminder\(s\)', exec_path='outlook.exe'),

                # This is an invisible application that queries think is actually a visible application.
                config.AppMatcher(class_name='MSO_BORDEREFFECT_WINDOW_CLASS', title='', exec_path='outlook.exe'),
            ]),

            # General non-chromed apps.  These ones appear on the default screen.
            config.ApplicationChromeConfig(has_title=True, has_border=True, is_tiled=True, app_matchers=[
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
        {
            "win+~": [config.MODE_CHANGE_COMMAND, "simple-windows-mode"],
            "win+f11": [config.MODE_CHANGE_COMMAND, "resize-window-mode"],

            # Move windows to other portals using the arrow keys.
            # This isn't configured to use numpad keys.
            "win+alt+up": ["move-window-to-other-portal", "north"],
            "win+alt+down": ["move-window-to-other-portal", "south"],
            "win+alt+left": ["move-window-to-other-portal", "west"],
            "win+alt+right": ["move-window-to-other-portal", "east"],

            # "next" and "previous" window movement bypasses how layouts
            # think about directions, and just moves in order through the
            # portals.
            "win+alt+pgup": ["move-window-to-other-portal", "next"],
            "win+alt+pgdn": ["move-window-to-other-portal", "previous"],

            # Flip between windows within the currently focused portal
            "win+<": ["switch-top-window", "previous"],
            "win+>": ["switch-top-window", "next"],

            # Change focused portal to an adjacent portal
            "win+up": ["move-focus", "north"],
            "win+down": ["move-focus", "south"],
            "win+left": ["move-focus", "west"],
            "win+right": ["move-focus", "east"],
            "win+pgup": ["move-focus", "previous"],
            "win+pgdn": ["move-focus", "next"],

            # A set of quick keys to swap between portals.  Hold down
            # win+shift+(number key) to assign a portal to that number, and
            # win+(number key) to jump to the top window in that portal.
            "win+shift+1": ["create-current-portal-alias", "P1"],
            "win+shift+2": ["create-current-portal-alias", "P2"],
            "win+shift+3": ["create-current-portal-alias", "P3"],
            "win+shift+4": ["create-current-portal-alias", "P4"],
            "win+shift+5": ["create-current-portal-alias", "P5"],
            "win+shift+6": ["create-current-portal-alias", "P6"],
            "win+shift+7": ["create-current-portal-alias", "P7"],
            "win+shift+8": ["create-current-portal-alias", "P8"],
            "win+shift+9": ["create-current-portal-alias", "P9"],
            "win+shift+0": ["create-current-portal-alias", "P0"],
            "win+1": ["focus-portal-by-alias", "P1"],
            "win+2": ["focus-portal-by-alias", "P2"],
            "win+3": ["focus-portal-by-alias", "P3"],
            "win+4": ["focus-portal-by-alias", "P4"],
            "win+5": ["focus-portal-by-alias", "P5"],
            "win+6": ["focus-portal-by-alias", "P6"],
            "win+7": ["focus-portal-by-alias", "P7"],
            "win+8": ["focus-portal-by-alias", "P8"],
            "win+9": ["focus-portal-by-alias", "P9"],
            "win+0": ["focus-portal-by-alias", "P0"],

            # Bring to front, and give focus, to the most recently flashing window.
            "win+tab": ["focus-last-flashing-window"],

            # Redefine the Windows lock screen keystroke.
            # This doesn't actually do anything, because Windows reads in
            # the Win+L key combination before anything can interrupt it.
            "win+l": ["lock-screen"],

            # Launch a CMD.exe command prompt in a stand alone window.
            "win+launch-app1": ["cmd", "cmd.exe /c start cmd.exe"],

            # Launch a CMD with nice colors and an initial directory.
            # Note that the backslash character must be escaped, because
            # it's in a python string, so a total of 2 backslashes to equal 1
            # real backslash.
            "win+p": ["cmd", "cmd.exe /c start cmd.exe /E:ON /V:ON /T:17 /K cd \\"],

            "win+n": ["cmd", '"c:\\Program Files (x86)\\Notepad++\\notepad++"'],

            # Replace the old "win+e" to open an explorer window.
            "win+e": ["cmd", "explorer.exe c:\\"],

            "win+f4": ["quit"],

            # load-config, with no arguments, just reloads the current config file.
            "win+alt+f2": ["load-config"],

            # Because the windows key is blocked from being used as normal, this
            # gives you a way to still open the start menu.
            "win+esc": ["open-start-menu"],
        },

        # Block the windows key, because we remapped it to win+esc.
        # Note that this disables the standard windows hot keys, except
        # for a few critical ones (like win+L, which always works).
        block_win_key=True
    )

    # Just use Windows without any special parsing.  The windows key acts as Windows intends.
    # Well, "Win+~" will switch you back to the default mode.
    hotkeys.parse_hotkey_mode_keys(
        "simple-windows-mode",
        {
            "win+~": [config.MODE_CHANGE_COMMAND, config.DEFAULT_MODE],
        }
        # By default, the windows key is not blocked.
    )

    # "exclusive mode" is exclusive mode for this application. It sucks in all
    # input.  This is useful for an operation that controls how Petronia
    # works, such as manipulating the layout.
    hotkeys.parse_exclusive_mode_keys(
        "resize-window-mode",
        {
            "esc": [config.MODE_CHANGE_COMMAND, config.DEFAULT_MODE],
            "enter": [config.MODE_CHANGE_COMMAND, config.DEFAULT_MODE],
            "up": ["resize", 0, -16],
            "down": ["resize", 0, 16],
            "left": ["resize", -16, 0],
            "right": ["resize", 16, 0],
            "j": ["resize", 0, -1],
            "k": ["resize", 0, 1],
            "h": ["resize", -1, 0],
            "l": ["resize", 1, 0],

            # Numpad equivalents
            "separator": [config.MODE_CHANGE_COMMAND, config.DEFAULT_MODE],
            "numpad8": ["resize", 0, -4],
            "numpad2": ["resize", 0, 4],
            "numpad4": ["resize", -4, 0],
            "numpad6": ["resize", 4, 0],
            "add": ["resize", 4, 4],
            "subtract": ["resize", -4, -4],
        }
    )

    return config.Config(
        workgroups=layouts_by_display,
        applications=applications,
        hotkeys=hotkeys)
