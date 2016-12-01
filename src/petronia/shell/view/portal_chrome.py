
from ...system.component import Identifiable, Component
from ...system import event_ids
from ...system import target_ids
from ...shell.native.gui_window import GuiWindow
import threading
import time


# noinspection PyUnusedLocal
def portal_chrome_factory(bus, config, id_manager, component_settings):
    if config.uses_layout:
        mgr = PortalChromeManager(bus, config)
        position = 'position' in component_settings and component_settings['position'] or None
        width = 'width' in component_settings and component_settings['width'] or None
        active_color = _color_as_int(
            'active-color' in component_settings and component_settings['active-color'] or None)
        inactive_color = _color_as_int(
            'inactive-color' in component_settings and component_settings['inactive-color'] or None)
        mgr.update_border(active_color=active_color, inactive_color=inactive_color, position=position, width=width)


def _color_as_int(c):
    if c is None:
        return None
    if isinstance(c, str):
        if c[0] == '#':
            return int(c[1:], 16)
    return int(c)


class _PortalGuiWindow(GuiWindow):
    def __init__(self, portal_id, bus, pos_x, pos_y, width, height, manager):
        self._portal_x = pos_x
        self._portal_y = pos_y
        self._portal_width = width
        self._portal_height = height

        self._manager = manager

        self._is_active = False

        # Make configuration better
        self.color_1 = 0
        self.color_2 = 0
        self.accent_width = 64

        left, right, top, bottom = manager.get_chrome_size(pos_x, pos_y, width, height)
        GuiWindow.__init__(self, 'chrome-' + portal_id, bus, 'chrome-' + portal_id, None, {
            'left': left, 'right': right, 'top': top, 'bottom': bottom, 'padding': 0,
        }, has_border=False, is_always_on_top=False, is_on_taskbar=False)

        self._listen(event_ids.PORTAL__CHANGE_BORDER_SIZE, target_ids.ANY, self._on_border_size_change)

        self._listen(event_ids.PORTAL__DESTROYED, portal_id, self._on_portal_removed)
        self._listen(event_ids.LAYOUT__SET_RECTANGLE, portal_id, self._on_portal_size_change)
        self._listen(event_ids.PORTAL__FLASHING, portal_id, self._on_portal_flashing)
        self._listen(event_ids.PORTAL__ACTIVATED, portal_id, self._on_portal_activated)
        self._listen(event_ids.PORTAL__DEACTIVATED, portal_id, self._on_portal_deactivated)

    def set_portal_size(self, pos_x, pos_y, width, height):
        self._portal_x = pos_x
        self._portal_y = pos_y
        self._portal_width = width
        self._portal_height = height

        left, right, top, bottom = self._manager.get_chrome_size(pos_x, pos_y, width, height)
        # If the portal is active, then bring the chrome to the top, otherwise, leave it as-is.
        self.move_resize(left, top, right - left, bottom - top, self._is_active)

    def _on_paint(self, hwnd, hdc, width, height):
        self._draw_rect(hdc, 0, 0, width, height, self.color_1)
        if width >= self.accent_width * 3:
            if height >= self.accent_width * 3:
                # 4 corners of color
                self._draw_rect(hdc, 0, 0, self.accent_width, self.accent_width, self.color_2)
                self._draw_rect(hdc, width - self.accent_width, 0, self.accent_width, self.accent_width, self.color_2)
                self._draw_rect(hdc, 0, height - self.accent_width, self.accent_width, self.accent_width, self.color_2)
                self._draw_rect(hdc, width - self.accent_width, height - self.accent_width, self.accent_width,
                                self.accent_width, self.color_2)
            else:
                # Vertical bars of color
                self._draw_rect(hdc, 0, 0, self.accent_width, height, self.color_2)
                self._draw_rect(hdc, width - self.accent_width, 0, self.accent_width, height, self.color_2)
        elif height >= self.accent_width * 3:
            # Horizontal bars of color
            self._draw_rect(hdc, 0, 0, width, self.accent_width, self.color_2)
            self._draw_rect(hdc, 0, height - self.accent_width, width, self.accent_width, self.color_2)

    # noinspection PyUnusedLocal
    def _on_portal_removed(self, event_id, target_id, event_obj):
        # TODO is this the right call?
        self.close()

    # noinspection PyUnusedLocal
    def _on_portal_size_change(self, event_id, target_id, event_obj):
        self.set_portal_size(
            pos_x=event_obj['x'],
            pos_y=event_obj['y'],
            width=event_obj['width'],
            height=event_obj['height']
        )

    # noinspection PyUnusedLocal
    def _on_border_size_change(self, event_id, target_id, event_obj):
        self.set_portal_size(self._portal_x, self._portal_y, self._portal_width, self._portal_height)

    # noinspection PyUnusedLocal
    def _on_portal_flashing(self, event_id, target_id, event_obj):
        color_c1 = self.color_1
        color_c2 = self.color_2
        color_f1 = _brighten_color(self.color_1)
        color_f2 = _brighten_color(self.color_2)

        def flash():
            for i in range(self._manager.flash_count):
                self.color_1 = color_f1
                self.color_2 = color_f2
                self.draw()
                time.sleep(self._manager.flash_time)
                self.color_1 = color_c1
                self.color_2 = color_c2
                self.draw()
                time.sleep(self._manager.flash_time)

        threading.Thread(
            target=flash,
            daemon=True
        ).start()

    # noinspection PyUnusedLocal
    def _on_portal_activated(self, event_id, target_id, event_obj):
        self._log_debug("Activating chrome portal")
        self._is_active = True
        portal_size = event_obj['portal-size']
        portal_active = event_obj['portal-active']
        parent_hwnd = event_obj['parent-hwnd']

        pos_x = portal_size['x']
        pos_y = portal_size['y']
        width = portal_size['width']
        height = portal_size['height']

        self.color_1, self.color_2 = self._manager.active_colors
        self.set_portal_size(pos_x, pos_y, width, height)
        self.draw()

    # noinspection PyUnusedLocal
    def _on_portal_deactivated(self, event_id, target_id, event_obj):
        self._log_debug("Deactivating chrome portal")
        self._is_active = False
        portal_size = event_obj['portal-size']
        portal_active = event_obj['portal-active']
        parent_hwnd = event_obj['parent-hwnd']

        pos_x = portal_size['x']
        pos_y = portal_size['y']
        width = portal_size['width']
        height = portal_size['height']

        self.color_1, self.color_2 = self._manager.inactive_colors
        self.set_portal_size(pos_x, pos_y, width, height)
        self.draw()


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

        self._config = config
        self._active_color1 = 0x0070f0
        self._active_color2 = 0x003878
        self._inactive_color1 = 0x808080
        self._inactive_color2 = 0x404040
        self._position = 'bottom'
        self._width = 10
        self.flash_time = 1.2
        self.flash_count = 3
        self.update_border()

    @property
    def active_colors(self):
        return self._active_color1, self._active_color2

    @property
    def inactive_colors(self):
        return self._inactive_color1, self._inactive_color2

    def get_chrome_size(self, pos_x, pos_y, width, height):
        """

        :param pos_x:
        :param pos_y:
        :param width:
        :param height:
        :return: (left, right, top, bottom)
        """
        if self._position == 'left':
            return pos_x, pos_x + self._width, pos_y, pos_y + height
        elif self._position == 'right':
            return pos_x + width - self._width, pos_x + width, pos_y, pos_y + height
        elif self._position == 'top':
            return pos_x, pos_x + width, pos_y, pos_y + self._width
        elif self._position == 'bottom':
            return pos_x, pos_x + width, pos_y + height - self._width, pos_y + height
        raise ValueError('position {0}'.format(self._position))

    def update_border(self, active_color=None, inactive_color=None, position=None, width=None):
        if active_color is not None:
            self._active_color1 = int(active_color)
            self._active_color2 = _darken_color(active_color)
        if inactive_color is not None:
            self._inactive_color1 = int(inactive_color)
            self._inactive_color2 = _darken_color(inactive_color)
        if position is not None:
            assert position in ['left', 'right', 'top', 'bottom']
            self._position = position
        if width is not None:
            assert width > 0
            self._width = int(width)
        if self._position == 'left':
            self._config.chrome.set_border(left=self._width, right=0, top=0, bottom=0)
        elif self._position == 'right':
            self._config.chrome.set_border(left=0, right=self._width, top=0, bottom=0)
        elif self._position == 'top':
            self._config.chrome.set_border(left=0, right=0, top=self._width, bottom=0)
        elif self._position == 'bottom':
            self._config.chrome.set_border(left=0, right=0, top=0, bottom=self._width)
        self._fire(event_ids.PORTAL__CHANGE_BORDER_SIZE, target_ids.BROADCAST, {
            'left': self._config.chrome.portal_chrome_border['left'],
            'right': self._config.chrome.portal_chrome_border['right'],
            'top': self._config.chrome.portal_chrome_border['top'],
            'bottom': self._config.chrome.portal_chrome_border['bottom'],
            'width': self._width,
            'position': self._position,
        })

    def close(self):
        super().close()

    # noinspection PyUnusedLocal
    def _on_portal_registered(self, event_id, target_id, event_obj):
        if target_id not in self.__portal_map:
            self.__portal_map[target_id] = {'gui': None}
            # Wait for a size call before creating the GUI.

    # noinspection PyUnusedLocal
    def _on_portal_removed(self, event_id, target_id, event_obj):
        if target_id in self.__portal_map:
            del self.__portal_map[target_id]

    # noinspection PyUnusedLocal
    def _on_portal_resized(self, event_id, target_id, event_obj):
        if target_id in self.__portal_map:
            pos_x = event_obj['x']
            pos_y = event_obj['y']
            width = event_obj['width']
            height = event_obj['height']

            gui = self.__portal_map[target_id]['gui']
            if gui is None:
                gui = _PortalGuiWindow(target_id, self._bus, pos_x, pos_y, width, height, self)
                gui.color_1 = self._inactive_color1
                gui.color_2 = self._inactive_color2
                # TODO setup flash
                self.__portal_map[target_id]['gui'] = gui
