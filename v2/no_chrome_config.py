
from petronia import config


def load_config():
    """
    An example of a configuration that only strips off the extra
    "chrome" on the Windows windows that work well without the
    borders.  You can still use the native Windows tiling-like
    keys (win-left, win-right, win-up, win-down).

    :return:
    """

    applications = config.ApplicationListConfig([
        # Apps that should not  belong to the tiling, because it messes up the
        # display.  These come before the general non-chromed apps, because it
        # they both include a matching entry, but this one contains a more
        # precise entry.
        config.ApplicationChromeConfig(is_managed_chrome=False, app_matchers=[
            config.AppMatcher(exec_path='firefox.exe'),
            config.AppMatcher(exec_path='chrome.exe'),
            config.AppMatcher(exec_path='explorer.exe'),
            config.AppMatcher(exec_path='outlook.exe'),
        ]),
    ])

    chrome = config.ChromeConfig()
    chrome.has_title = False
    chrome.has_resize_border = False
    chrome.scrollbar_width = 4
    chrome.scrollbar_height = 4
    chrome.border_width = 0
    chrome.border_padding = 0

    # Need to be able to stop the program.
    hotkeys = config.HotKeyConfig()
    hotkeys.parse_hotkey_mode_keys(
        config.DEFAULT_MODE,
        {
            "win+f4": ["quit"],
        }
    )

    return config.Config(
        applications=applications,
        chrome=chrome,
        hotkeys=hotkeys)
