
from .base_config import BaseConfig


class ChromeConfig(BaseConfig):
    """
    Controls the "chrome" around the windows.  This is now only used by portals
    to understand how much space they need to leave the windows around the edges.
    """
    def __init__(self):
        super()

        self.__portal_chrome_border = {
            # Used by the portal to figure out how to shrink the
            # window within the portal.  Eventually, the
            # shell or other component will set this to match its
            # own rendering.
            'top': 0, 'bottom': 0, 'left': 0, 'right': 0,
        }
        self.flash_count = 3
        self.flash_wait_seconds = 1.0

    def set_border(self, top, bottom, left, right):
        self.__portal_chrome_border['top'] = int(top)
        self.__portal_chrome_border['bottom'] = int(bottom)
        self.__portal_chrome_border['left'] = int(left)
        self.__portal_chrome_border['right'] = int(right)

    @property
    def portal_chrome_border(self):
        return dict(self.__portal_chrome_border)
