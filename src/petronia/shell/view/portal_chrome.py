
from ...system.component import Identifiable, Component
from ...system import event_ids
from ...system import target_ids
from ...shell.native.gui_window import GuiWindow
import threading
import time


# noinspection PyUnusedLocal
def portal_chrome_factory(bus, config, id_manager):
    if config.uses_layout:
        PortalChromeManager(bus, config)


class _PortalGuiWindow(GuiWindow):
    def __init__(self, portal_id, bus, pos_x, pos_y, width, height):
        GuiWindow.__init__(self, 'chrome-' + portal_id, bus, 'chrome-' + portal_id, portal_id, {
            'x': pos_x, 'y': pos_y, 'width': width, 'height': height, 'padding': 0,
        }, has_border=False, is_transparent_bg=True, is_always_on_top=False)

        # Make configuration better
        self.color_1 = 0
        self.color_2 = 0
        self.width = 4
        self.flash_time = 1.2
        self.flash_count = 3

    def _on_paint(self, hwnd, hdc, width, height):
        self._draw_rect(hdc, 0, 0, width, height, self.color_1)
        if width >= self.width * 3:
            if height >= self.width * 3:
                # 4 corners of color
                self._draw_rect(hdc, 0, 0, self.width, self.width, self.color_2)
                self._draw_rect(hdc, width - self.width, 0, self.width, self.width, self.color_2)
                self._draw_rect(hdc, 0, height - self.width, self.width, self.width, self.color_2)
                self._draw_rect(hdc, width - self.width, height - self.width, self.width, self.width, self.color_2)
            else:
                # Vertical bars of color
                self._draw_rect(hdc, 0, 0, self.width, height, self.color_2)
                self._draw_rect(hdc, width - self.width, 0, self.width, height, self.color_2)
        elif height >= self.width * 3:
            # Horizontal bars of color
            self._draw_rect(hdc, 0, 0, width, self.width, self.color_2)
            self._draw_rect(hdc, 0, height - self.width, width, self.width, self.color_2)

    def flash_window(self):
        color_c1 = self.color_1
        color_c2 = self.color_2
        color_f1 = _brighten_color(self.color_1)
        color_f2 = _brighten_color(self.color_2)

        def flash():
            for i in range(self.flash_count):
                self.color_1 = color_f1
                self.color_2 = color_f2
                self.draw_now()
                time.sleep(self.flash_time)
                self.color_1 = color_c1
                self.color_2 = color_c2
                self.draw_now()
                time.sleep(self.flash_time)

        threading.Thread(
            target=flash,
            daemon=True
        ).start()


def _brighten_color(c):
    c = int(c)
    r = (c >> 16) & 0xff
    g = (c >> 8) & 0xff
    b = c & 0xff
    return ((max(0xff, r << 1) << 16) & 0xff0000) | ((max(0xff, g << 1) << 8) & 0xff00) | (max(0xff, b << 1) & 0xff)


def _darken_color(c):
    c = int(c)
    r = (c >> 16) & 0xff
    g = (c >> 8) & 0xff
    b = c & 0xff
    # Divide each component by 2 to be the secondary color
    return ((r << 15) & 0xff0000) | ((g << 7) & 0xff00) | ((b >> 1) & 0xff)


class PortalChromeManager(Identifiable, Component):
    def __init__(self, bus, config):
        Component.__init__(self, bus)
        Identifiable.__init__(self, target_ids.PORTAL_CHROME_MANAGER)

        self.__portal_map = {}

        self._listen(event_ids.PORTAL__CREATED, target_ids.ANY, self._on_portal_registered)
        self._listen(event_ids.PORTAL__DESTROYED, target_ids.ANY, self._on_portal_removed)
        self._listen(event_ids.LAYOUT__SET_RECTANGLE, target_ids.ANY, self._on_portal_resized)
        self._listen(event_ids.PORTAL__FLASHING, target_ids.ANY, self._on_portal_flashing)
        self._listen(event_ids.PORTAL__ACTIVATED, target_ids.ANY, self._on_portal_activated)
        self._listen(event_ids.PORTAL__DEACTIVATED, target_ids.ANY, self._on_portal_deactivated)

        self._config = config
        self.__border = {
            'active_color1': 0x0070f0,
            'active_color2': 0x003878,
            'inactive_color1': 0x808080,
            'inactive_color2': 0x404040,
            'left': 2,
            'right': 2,
            'top': 2,
            'bottom': 6
        }
        self.update_border()

    def update_border(self, active_color=None, inactive_color=None, left=None, right=None, top=None, bottom=None):
        if active_color is not None:
            self.__border['active_color1'] = int(active_color)
            self.__border['active_color2'] = _darken_color(active_color)
        if inactive_color is not None:
            self.__border['inactive_color1'] = int(inactive_color)
            self.__border['inactive_color2'] = _darken_color(inactive_color)
        if left is not None:
            self.__border['left'] = int(left)
        if right is not None:
            self.__border['right'] = int(right)
        if top is not None:
            self.__border['top'] = int(top)
        if bottom is not None:
            self.__border['bottom'] = int(bottom)
        self._config.chrome.set_border(
            left=self.__border['left'],
            right=self.__border['right'],
            top=self.__border['top'],
            bottom=self.__border['bottom']
        )
        self._fire(event_ids.PORTAL__CHANGE_BORDER_SIZE, target_ids.BROADCAST, self._config.chrome.portal_chrome_border)

    def close(self):
        super().close()

    def _on_portal_registered(self, event_id, target_id, event_obj):
        if target_id not in self.__portal_map:
            self.__portal_map[target_id] = {'gui': None}
            # Wait for a size call before creating the GUI.

    def _on_portal_removed(self, event_id, target_id, event_obj):
        if target_id in self.__portal_map:
            gui = self.__portal_map[target_id]['gui']
            if gui is not None:
                # TODO is this the right call?
                gui.close()
            del self.__portal_map[target_id]

    def _on_portal_resized(self, event_id, target_id, event_obj):
        if target_id in self.__portal_map:
            pos_x = event_obj['x']
            pos_y = event_obj['y']
            width = event_obj['width']
            height = event_obj['height']

            gui = self.__portal_map[target_id]['gui']
            if gui is None:
                gui = _PortalGuiWindow(target_id, self._bus, pos_x, pos_y, width, height)
                gui.color_1 = self.__border['inactive_color1']
                gui.color_2 = self.__border['inactive_color2']
                # TODO setup flash
                self.__portal_map[target_id]['gui'] = gui
            else:
                gui.move_resize(pos_x, pos_y, width, height)
            gui.draw()

    def _on_portal_flashing(self, event_id, target_id, event_obj):
        portal_cid = target_id
        portal_size = event_obj['portal-size']
        portal_active = event_obj['portal-active']
        parent_hwnd = event_obj['parent-hwnd']

        if portal_cid in self.__portal_map:
            gui = self.__portal_map[target_id]['gui']
            if gui is not None:
                gui.flash_window()

    def _on_portal_activated(self, event_id, target_id, event_obj):
        portal_cid = target_id
        portal_size = event_obj['portal-size']
        portal_active = event_obj['portal-active']
        parent_hwnd = event_obj['parent-hwnd']

        if portal_cid in self.__portal_map:
            gui = self.__portal_map[target_id]['gui']
            if gui is not None:
                gui.color_1 = self.__border['active_color1']
                gui.color_2 = self.__border['active_color2']

                pos_x = portal_size['x']
                pos_y = portal_size['y']
                width = portal_size['width']
                height = portal_size['height']

                gui.move_resize(pos_x, pos_y, width, height, True)

    def _on_portal_deactivated(self, event_id, target_id, event_obj):
        portal_cid = target_id
        portal_size = event_obj['portal-size']
        portal_active = event_obj['portal-active']
        parent_hwnd = event_obj['parent-hwnd']

        if portal_cid in self.__portal_map:
            gui = self.__portal_map[target_id]['gui']
            if gui is not None:
                gui.color_1 = self.__border['inactive_color1']
                gui.color_2 = self.__border['inactive_color2']
                gui.draw()
