
from ...system import event_ids
from ...system import target_ids
from ...system.component import Component, Identifiable
from ...arch import windows_constants
from ...arch.funcs import (
    window__create_display_window,
    window__client_rectangle,
    window__set_layered_attributes,
    window__set_position,
    window__set_style,
    window__get_text_size,
    window__get_font_for_description,
    window__move_resize,
    window__send_message,
    window__repaint,
    window__do_paint,
    window__do_draw,
    window__get_font_for_description,
    window__get_text_size,
    monitor__find_monitors,
    paint__draw_rect,
    paint__draw_text,
    paint__draw_outline_text,
    shell__create_global_message_handler,
    shell__pump_messages,
)
import threading


class GuiWindow(Identifiable, Component):
    """
    Abstract GUI window for showing information to the user.
    """
    def __init__(self, cid, bus, class_name, title, position_details,
                 font=None,
                 has_border=True,
                 is_transparent_bg=False,
                 is_always_on_top=False):
        Component.__init__(self, bus)
        Identifiable.__init__(self, cid)

        self.__has_quit = False
        self.__removing = False
        self.__hwnd = None
        self.__hfont = None
        self.__is_always_on_top = is_always_on_top

        # Because of multi-threading issues, a resize may come in after initial creation
        self.__size_set = False
        self.__pos_x = None
        self.__pos_y = None
        self.__width = None
        self.__height = None

        def do_paint(hwnd, hdc):
            print("DEBUG: on paint callback")
            window_size = window__client_rectangle(hwnd)
            self._on_paint(hwnd, hdc, window_size['width'], window_size['height'])

        # noinspection PyUnusedLocal
        def paint(hwnd, message, wparam, lparam):
            window__do_paint(hwnd, do_paint)

        self.__message_id_callbacks = {
            windows_constants.WM_PAINT: paint
        }

        style_flags = {
            # WS_OVERLAPPEDWINDOW
            'border', 'dialog-frame', 'sysmenu-button', 'size-border', 'minimize-button', 'maximize-button'
        }
        ex_style_flags = {
            # WS_EX_OVERLAPPEDWINDOW
            'window-edge': True, 'client-edge': True
        }
        if is_transparent_bg:
            style_flags.add('popup')
            ex_style_flags['layered'] = True
        if not has_border:
            style_flags.remove('border')
            style_flags.remove('dialog-frame')
            style_flags.remove('size-border')
            style_flags.remove('maximize-button')
            style_flags.remove('minimize-button')
            style_flags.add('popup')
            style_flags.add('visible')
        if is_always_on_top:
            ex_style_flags['topmost'] = True

        def on_exit_callback():
            self.__has_quit = True
            self.close()

        def message_pumper():
            print("DEBUG message pumper enter")
            # These MUST be in the same thread!
            message_callback_handler = shell__create_global_message_handler(self.__message_id_callbacks)
            self.__hwnd = window__create_display_window(class_name, title, message_callback_handler, style_flags)

            # TODO fix the set_layered_attributes call
            # if is_invisible:
            #     window__set_layered_attributes(self.__hwnd, 0, 0, 0, 0)

            if font is not None:
                self.__hfont = window__get_font_for_description(font, hwnd=self.__hwnd)
            if not self.__size_set:
                self.__pos_x, self.__pos_y, self.__width, self.__height = _parse_window_pos_details(
                    position_details, self.__hwnd, self.__hfont)
            print("DEBUG setting window to ({0}, {1}) :: {2}x{3}".format(
                self.__pos_x, self.__pos_y, self.__width, self.__height))

            if is_always_on_top:
                window__set_position(
                    self.__hwnd, 'topmost',
                    self.__pos_x, self.__pos_y, self.__width, self.__height,
                    ['no-activate'])
            else:
                window__move_resize(self.__hwnd, self.__pos_x, self.__pos_y, self.__width, self.__height, False)

            window__set_style(self.__hwnd, ex_style_flags)

            shell__pump_messages(on_exit_callback)

            print("window quit")
            self.__has_quit = True

        pump_thread = threading.Thread(
            target=message_pumper,
            daemon=True
        )
        pump_thread.start()

        self._listen(event_ids.REGISTRAR__OBJECT_REMOVED, cid, self._on_removed)

    # noinspection PyUnusedLocal
    def _on_removed(self, event_id, target_id, event_obj):
        # Prevent recursion
        if not self.__removing:
            self.__removing = True
            self.close()

    def close(self):
        try:
            self.__removing = True
            if not self.__has_quit:
                window__send_message(self.__hwnd, windows_constants.WM_QUIT, 0, 0)
        finally:
            super().close()

    def add_message_handler(self, message_id, handler):
        if isinstance(message_id, str):
            message_id = windows_constants.WM_MESSAGE_NAMES[message_id]
        self.__message_id_callbacks[message_id] = handler

    def draw(self):
        if not self.__has_quit:
            window__repaint(self.__hwnd)

    def draw_now(self):
        def do_paint(hwnd, hdc):
            window_size = window__client_rectangle(hwnd)
            self._on_paint(hwnd, hdc, window_size['width'], window_size['height'])
        window__do_draw(self.__hwnd, do_paint)

    def move_resize(self, pos_x, pos_y, width, height, force_on_top=False):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__width = width
        self.__height = height
        self.__size_set = True

        if self.__hwnd is None:
            # Nothing to do yet.
            return
        if self.__is_always_on_top:
            window__set_position(
                self.__hwnd, 'topmost',
                pos_x, pos_y, width, height,
                ['no-activate'])
        elif force_on_top:
            window__set_position(
                self.__hwnd,
                'top',
                pos_x, pos_y, width, height,
                ['no-activate'])
        else:
            window__move_resize(self.__hwnd, pos_x, pos_y, width, height, False)

    def _on_paint(self, hwnd, hdc, width, height):
        pass

    @staticmethod
    def _get_text_size(text, font_desc, hwnd=None, hdc=None):
        """

        :param text:
        :param font_desc:
        :param hwnd: (optional) the window's handle
        :param hdc: (optional) the paint dc handle
        :return: width, height
        """
        hfont = window__get_font_for_description(font_desc, hwnd=hwnd, base_hdc=hdc)
        return window__get_text_size(hfont, text, hwnd=hwnd, base_hdc=hdc)

    @staticmethod
    def _draw_rect(hdc, pos_x, pos_y, width, height, color):
        paint__draw_rect(hdc, pos_x, pos_y, width, height, color)

    @staticmethod
    def _draw_text(hdc, text, font_desc, pos_x, pos_y, width, height, fg_color, bg_color):
        """

        :param hdc: paint hdc
        :param font_desc: string describing the font.
        :param pos_x: logical x position
        :param pos_y: logical y position
        :param width: text box width
        :param height: text box height
        :param fg_color: foreground color, in 0xRRGGBB format.
        :param bg_color: background color, in 0xRRGGBB format.  If None, then
            the background will not be drawn.
        :return:
        """
        hfont = window__get_font_for_description(font_desc, base_hdc=hdc)
        paint__draw_text(hdc, hfont, text, pos_x, pos_y, width, height, fg_color, bg_color)

    @staticmethod
    def _draw_outline_text(hdc, text, font_desc, pos_x, pos_y,
                           outline_width, outline_color, fill_color, bg_color):
        hfont = window__get_font_for_description(font_desc, base_hdc=hdc)
        paint__draw_outline_text(hdc, hfont, text, pos_x, pos_y, outline_width, outline_color, fill_color, bg_color)


def _parse_window_pos_details(pos, hwnd, hfont):
    pos_x = 'x' in pos and pos['x'] or 0
    pos_y = 'y' in pos and pos['y'] or 0
    width = 'width' in pos and pos['width'] or 100
    height = 'height' in pos and pos['height'] or 100
    if 'left' in pos:
        pos_x = pos['left']
    if 'top' in pos:
        pos_y = pos['top']

    padding = 'padding' in pos and pos['padding'] or 4

    if 'text-size' in pos and hfont is not None:
        text = pos['text-size']
        width, height = window__get_text_size(hwnd, hfont, text)

    if 'relative' in pos:
        relative = pos['relative'].split('-')
        if 'monitor' in pos:
            monitor_index = pos['monitor']
        else:
            monitor_index = 0

        monitors = monitor__find_monitors()
        if monitor_index < 0 or monitor_index >= len(monitors):
            monitor_index = 0

        if 'bottom' in relative:
            pos_y = monitors[monitor_index]['bottom'] - height - padding
        elif 'top' in relative:
            pos_y = monitors[monitor_index]['top'] + padding

        if 'right' in relative:
            pos_x = monitors[monitor_index]['right'] - width - padding
        elif 'left' in relative:
            pos_x = monitors[monitor_index]['left'] + padding

    if 'right' in pos:
        width = pos['right'] - pos_x
    if 'bottom' in pos:
        height = pos['bottom'] - pos_y

    print("DEBUG translated {0} into ({1},{2}) {3}x{4}".format(
        pos, pos_x, pos_y, width, height
    ))
    return pos_x, pos_y, width, height
