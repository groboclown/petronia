
from .base_config import BaseConfig


class ChromeConfig(BaseConfig):
    """
    Controls the "chrome" around the windows.
    """
    def __init__(self, border_width=4, border_color=0xff0000):
        super()
        self.border_width = border_width
        self.border_padding = 0
        self.border_color = border_color
        self.scrollbar_width = 0
        self.scrollbar_height = 0
        self.has_title = False
        self.has_resize_border = False
        self.portal_chrome_border = {
            'color': 0x404040, 'width': 2,  # Placeholders
            'top': 0, 'bottom': 0, 'left': 0, 'right': 0,
        }
        self.portal_chrome_active_border = {
            'color': 0x808000, 'width': 4,  # Placeholders
            'top': 0, 'bottom': 0, 'left': 0, 'right': 0,
        }

    def get_system_window_settings(self):
        # see shell__set_window_metrics
        ret = {}
        if self.border_width > 0:
            ret['border-width'] = self.border_width
        if self.border_padding >= 0:
            ret['padded-border-width'] = self.border_padding
        if self.scrollbar_width > 0:
            ret['scroll-width'] = self.scrollbar_width
        if self.scrollbar_height > 0:
            ret['scroll-height'] = self.scrollbar_height
        # All other chrome is ignored for this call
        return ret

    @property
    def remove_decoration(self):
        """

        :return: True if the windows should not have wide borders or title bars with the
            controls (system menu, minimize, maximize, restore).
        """
        return not self.has_title

    @property
    def remove_resize_border(self):
        """

        :return: True if the window borders should not be resizable.
        """
        return not self.has_resize_border

    @property
    def show_taskbar_with_start_menu(self):
        """

        :return: True if the task bar is shown whenever the user requests the start menu to be shown;
            False if default OS behavior is used.
        """
        return True
