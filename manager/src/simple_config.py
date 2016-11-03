
from petronia import config


def load_config():
    chrome = config.ChromeConfig()
    chrome.has_title = False
    chrome.has_resize_border = False
    chrome.scrollbar_width = 4
    chrome.scrollbar_height = 4
    chrome.border_width = 0
    chrome.border_padding = 0
    chrome.portal_chrome_border['width'] = 0
    chrome.portal_chrome_active_border['width'] = 0

    # Need to be able to stop the program.
    hotkeys = config.HotKeyConfig()
    hotkeys.parse_hotkey_mode_keys(
        config.DEFAULT_MODE,
        [
            "win+f4 => quit",
        ]
    )

    return config.Config(
        chrome=chrome,
        hotkeys=hotkeys)
