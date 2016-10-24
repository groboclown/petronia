
from ...system import event_ids
from ...system import target_ids
from ...system.component import Component
from ...config import Config
from ...arch import funcs


class RenderActivePortal(Component):
    """
    The displayed monocle view with name tabs for each internal Top Window.  The top window itself is
    updated via the top_window.TopWindow class.
    """
    def __init__(self, bus, config):
        Component.__init__(self, bus)
        assert isinstance(config, Config)

        self.__config = config

        self._listen(event_ids.PORTAL__DEACTIVATED, target_ids.ANY, self._on_render1)
        self._listen(event_ids.PORTAL__ACTIVATED, target_ids.ANY, self._on_render2)
        self._listen(event_ids.PORTAL__REDRAW, target_ids.ANY, self._on_render3)

    def _on_render1(self, event_id, target_id, event_obj):
        self._on_render(event_id, target_id, event_obj)
    def _on_render2(self, event_id, target_id, event_obj):
        self._on_render(event_id, target_id, event_obj)
    def _on_render3(self, event_id, target_id, event_obj):
        self._on_render(event_id, target_id, event_obj)

    def _on_render(self, event_id, target_id, event_obj):
        size = event_obj['portal-size']
        active = event_obj['portal-active']
        border = self.__config.chrome.portal_chrome_border
        if active:
            border = self.__config.chrome.portal_chrome_active_border
        if border['width'] > 0:
            rect = {
                'left': size['x'], 'right': size['x'] + size['width'],
                'top': size['y'], 'bottom': size['y'] + size['height']
            }
            print("DEBUG Rendering portal outline {0} {1} {2}".format(rect, hex(border['color']), border['width']))
            funcs.window__draw_border_outline(rect, border['color'], border['width'])
        else:
            print("DEBUG === Skipping because border is {0} ({1}) {2}".format(border['width'], active and "Active" or "Deactivated", event_obj))
