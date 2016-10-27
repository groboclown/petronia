
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
        # General non-chromed apps.
        config.ApplicationConfig(is_managed_chrome=False, is_tiled=True, app_matchers=[
            config.AppMatcher(exec_re=r'.*?\\firefox\.exe$'),
            config.AppMatcher(exec_re=r'.*?\\chrome\.exe$'),
            config.AppMatcher(exec_re=r'.*?\\explorer\.exe$'),
            config.AppMatcher(exec_re=r'.*?\\outlook\.exe$'),
        ]),
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
