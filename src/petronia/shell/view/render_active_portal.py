
from ...system import event_ids
from ...system import target_ids
from ...system.component import Component
from ...config import Config
from ...arch.funcs import window__draw_border_outline
from ...arch import windows_constants
import threading
import time


# noinspection PyUnusedLocal
def render_active_portal_factory(bus, config, id_manager):
    return RenderActivePortal(bus, config)


class RenderActivePortal(Component):
    """
    Renders extra frame stuff for the portal.

    TODO This needs to be much more robust.
    Each portal needs its own renderer, which should be a window that sits under
    the top window.  When a window is created, it should become "owned" by the
    portal outline.
    """
    def __init__(self, bus, config):
        Component.__init__(self, bus)
        assert isinstance(config, Config)

        self.__config = config

        self._listen(event_ids.PORTAL__DEACTIVATED, target_ids.ANY, self._on_render)
        self._listen(event_ids.PORTAL__ACTIVATED, target_ids.ANY, self._on_render)
        self._listen(event_ids.PORTAL__REDRAW, target_ids.ANY, self._on_render)
        self._listen(event_ids.PORTAL__FLASHING, target_ids.ANY, self._on_flash)

    # noinspection PyUnusedLocal
    def _on_render(self, event_id, target_id, event_obj):
        parent_hwnd = event_obj['parent-hwnd']
        size = event_obj['portal-size']
        active = event_obj['portal-active']
        border = self.__config.chrome.portal_chrome_border
        if active:
            border = self.__config.chrome.portal_chrome_active_border
        # print("DEBUG Borders: {0} {1}".format(self.__config.chrome.portal_chrome_border, self.__config.chrome.portal_chrome_active_border))
        _draw_border(size, border, parent_hwnd)

    # noinspection PyUnusedLocal
    def _on_flash(self, event_id, target_id, event_obj):
        parent_hwnd = event_obj['parent-hwnd']
        size = event_obj['portal-size']
        active = event_obj['portal-active']
        border_on = self.__config.chrome.portal_chrome_border
        if active:
            border_on = self.__config.chrome.portal_chrome_active_border
        border_off = {
            'color': (~ border_on['color']) & 0xffffff,
            'top': border_on['top'],
            'left': border_on['left'],
            'right': border_on['right'],
            'bottom': border_on['bottom'],
        }
        # print("DEBUG Borders: {0} {1}".format(self.__config.chrome.portal_chrome_border, self.__config.chrome.portal_chrome_active_border))

        def flash():
            for i in range(self.__config.chrome.flash_count):
                _draw_border(size, border_on, parent_hwnd)
                time.sleep(self.__config.chrome.flash_wait_seconds)
                _draw_border(size, border_off, parent_hwnd)
                time.sleep(self.__config.chrome.flash_wait_seconds)
            _draw_border(size, border_on, parent_hwnd)

        t = threading.Thread(
            target=flash,
            daemon=True
        )
        t.start()


_LAST_SIZE = None


def _draw_border(size, border, parent_hwnd):
    rect_list = []

    global _LAST_SIZE
    if _LAST_SIZE != size:
        print("DEBUG Drawing border {0}, {1}".format(size, border))
        _LAST_SIZE = size

    # Instead of drawing one rectangle around the window, we draw one rectangle per edge.
    # The rectangle "size" is the client size *after* the edge is removed.
    if border['top'] > 0:
        rect_list.append({
            'left': size['x'], 'right': size['x'] + size['width'],
            'top': size['y'], 'bottom': size['y'] + border['top'],
        })
    if border['bottom'] > 0:
        rect_list.append({
            'left': size['x'], 'right': size['x'] + size['width'],
            'top': size['y'] + size['height'] - border['bottom'], 'bottom': size['y'] + size['height'],
        })
    if border['left'] > 0:
        rect_list.append({
            'left': size['x'], 'right': size['x'] + border['left'],
            'top': size['y'], 'bottom': size['y'] + size['height'],
        })
    if border['right'] > 0:
        rect_list.append({
            'left': size['x'] + size['width'] - border['right'], 'right': size['x'] + size['width'],
            'top': size['y'], 'bottom': size['y'] + size['height'],
        })

    for rect in rect_list:
        window__draw_border_outline(rect, border['color'], 1,
                                    line_style=windows_constants.PS_SOLID,
                                    fill_style=windows_constants.BS_SOLID,
                                    parent_hwnd=parent_hwnd)
