
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

    chrome = config.ChromeConfig()
    chrome.has_title = False
    chrome.has_resize_border = False
    chrome.scrollbar_width = 4
    chrome.scrollbar_height = 4
    chrome.border_width = 0
    chrome.border_padding = 0
    chrome.portal_chrome_border['width'] = 0
    chrome.portal_chrome_active_border['width'] = 0

    return config.Config(
        applications=applications,
        chrome=chrome)
