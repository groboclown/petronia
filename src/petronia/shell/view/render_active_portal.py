
from ...system import event_ids
from ...system import target_ids
from ...system.component import Component
from ...config import Config
from ...arch.funcs import window__draw_border_outline
import threading
import time


# noinspection PyUnusedLocal
def render_active_portal_factory(bus, config, id_manager):
    return RenderActivePortal(bus, config)


class RenderActivePortal(Component):
    """
    The displayed monocle view with name tabs for each internal Top Window.  The top window itself is
    updated via the top_window.TopWindow class.
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
        size = event_obj['portal-size']
        active = event_obj['portal-active']
        border = self.__config.chrome.portal_chrome_border
        if active:
            border = self.__config.chrome.portal_chrome_active_border
        _draw_border(size, border)

    # noinspection PyUnusedLocal
    def _on_flash(self, event_id, target_id, event_obj):
        size = event_obj['portal-size']
        active = event_obj['portal-active']
        border_on = self.__config.chrome.portal_chrome_border
        if active:
            border_on = self.__config.chrome.portal_chrome_active_border
        border_off = {
            'width': border_on['width'],
            'color': (~ border_on['color']) & 0xffffff
        }

        def flash():
            # TODO make configurable via chrome.
            for i in range(3):
                _draw_border(size, border_on)
                time.sleep(1000)
                _draw_border(size, border_off)
                time.sleep(1000)
            _draw_border(size, border_on)

        t = threading.Thread(
            target=flash,
            daemon=True
        )
        t.start()


def _draw_border(size, border):
    # if 'status' in border:

    if border['width'] >= 0:
        # Drawing a border around the window causes all kinds of refresh
        # glitches.  So instead, we'll draw each side of the border.
        # This is 4x slower, though.
        # rect = {
        #     'left': size['x'], 'right': size['x'] + size['width'],
        #     'top': size['y'], 'bottom': size['y'] + size['height']
        # }
        # window__draw_border_outline(rect, border['color'], border['width'])
        border_width = border['width']
        margin = min(border['width'] // 2, 1)
        border_width = margin * 2
        rect_list = [
            # Left bar
            {
                'left': size['x'], 'right': size['x'] + margin,
                'top': size['y'], 'bottom': size['y'] + size['height']
            },
            # Right bar
            {
                'left': size['x'] + size['width'] - margin, 'right': size['x'] + size['width'],
                'top': size['y'], 'bottom': size['y'] + size['height']
            },
            # Top bar
            {
                'left': size['x'], 'right': size['x'] + size['width'],
                'top': size['y'], 'bottom': size['y'] + margin
            },
            # Bottom bar
            {
                'left': size['x'], 'right': size['x'] + size['width'],
                'top': size['y'] + size['height'] - margin, 'bottom': size['y'] + size['height']
            },
        ]
        for rect in rect_list:
            window__draw_border_outline(rect, border['color'], border_width)
