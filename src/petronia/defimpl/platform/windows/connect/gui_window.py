
"""
Low-level message handling for a component window created and managed by
Petronia.  Integration of this window into Petronia proper is handled outside
this module.

This performs no pixel transformations.  All dimensions and locations are sent
directly to the underlying native APIs as-is.
"""

from typing import Dict, Callable, Union, Optional
from ..arch import windows_constants
from ..arch.native_funcs.windows_common import (
    HWND, HFONT, HDC,
    WPARAM, LPARAM,
    MessageCallback,
    WindowsErrorMessage,
)
from ..arch.native_funcs import (
    WINDOWS_FUNCTIONS,
)
from .screen import (
    NativeScreenPosition,
    NATIVE_SCREEN_POSITION_X, NATIVE_SCREEN_POSITION_Y,

    NativeScreenSize,

    NativeScreenArea,
    NATIVE_SCREEN_AREA_X, NATIVE_SCREEN_AREA_Y,
    NATIVE_SCREEN_AREA_W, NATIVE_SCREEN_AREA_H,
)
from .....core.platform.api import Color, ScreenRect
import threading


class Painter:
    """Allows a paint function to perform the supported API actions."""
    __slots__ = ('__hwnd', '__hdc', '__size')

    # TODO the ScreenRect should be for virtual pixels, but this is actually native.
    def __init__(self, hwnd: HWND, hdc: HDC, size: ScreenRect) -> None:
        self.__hwnd = hwnd
        self.__hdc = hdc
        self.__size = size

    @property
    def window_size(self) -> ScreenRect:
        return self.__size

    def get_text_size(self, text: str, font_desc: str) -> Union[NativeScreenSize, WindowsErrorMessage]:
        """

        :param text:
        :param font_desc:
        :return: width, height
        """
        if not WINDOWS_FUNCTIONS.window.get_font_for_description or not WINDOWS_FUNCTIONS.window.get_text_size:
            return WindowsErrorMessage('not implemented')
        hfont = WINDOWS_FUNCTIONS.window.get_font_for_description(font_desc, hwnd=self.__hwnd, base_hdc=self.__hdc)
        return WINDOWS_FUNCTIONS.window.get_text_size(hfont, text, hwnd=self.__hwnd, base_hdc=self.__hdc)

    def draw_rect(self, area: NativeScreenArea, color: Color) -> Optional[WindowsErrorMessage]:
        if not WINDOWS_FUNCTIONS.paint.draw_rect:
            return WindowsErrorMessage('not implemented')
        return WINDOWS_FUNCTIONS.paint.draw_rect(
            self.__hdc,
            area[NATIVE_SCREEN_AREA_X], area[NATIVE_SCREEN_AREA_Y],
            area[NATIVE_SCREEN_AREA_W], area[NATIVE_SCREEN_AREA_H],
            color
        )

    def draw_text(
            self, text: str, font_desc: str, area: NativeScreenArea, fg_color: Color, bg_color: Optional[Color]
    ) -> Optional[WindowsErrorMessage]:
        """

        :param text: text to draw
        :param font_desc: string describing the font.
        :param area: position and text box size
        :param fg_color: foreground color
        :param bg_color: background color.  If None, then
            the background will not be drawn.
        :return:
        """
        if not WINDOWS_FUNCTIONS.window.get_font_for_description or not WINDOWS_FUNCTIONS.paint.draw_text:
            return WindowsErrorMessage('not implemented')
        hfont = WINDOWS_FUNCTIONS.window.get_font_for_description(font_desc, base_hdc=self.__hdc)
        return WINDOWS_FUNCTIONS.paint.draw_text(
            self.__hdc,
            hfont, text,
            area[NATIVE_SCREEN_AREA_X], area[NATIVE_SCREEN_AREA_Y],
            area[NATIVE_SCREEN_AREA_W], area[NATIVE_SCREEN_AREA_H],
            fg_color, bg_color
        )

    def draw_outline_text(
            self, text: str, font_desc: str, pos: NativeScreenPosition,
            outline_width: int,
            outline_color: Color, fill_color: Color, bg_color: Optional[Color]
    ) -> Optional[WindowsErrorMessage]:
        if not WINDOWS_FUNCTIONS.window.get_font_for_description or not WINDOWS_FUNCTIONS.paint.draw_outline_text:
            return WindowsErrorMessage('not implemented')
        hfont = WINDOWS_FUNCTIONS.window.get_font_for_description(font_desc, base_hdc=self.__hdc)
        return WINDOWS_FUNCTIONS.paint.draw_outline_text(
            self.__hdc, hfont, text,
            pos[NATIVE_SCREEN_POSITION_X], pos[NATIVE_SCREEN_POSITION_Y],
            outline_width, outline_color, fill_color, bg_color
        )


PaintWindowCallback = Callable[[Painter], None]


class GuiWindow:
    """
    GUI window for showing information to the user.
    """
    __slots__ = (
        '__hwnd',
        '__hfont',
        '__is_position_set',
        '__initial_position',
        '__is_always_on_top',
        '__removing',
        '__has_quit',
        '__on_exit',
        '_message_id_callbacks',
    )
    _message_id_callbacks: Dict[int, MessageCallback]

    def __init__(
            self,
            class_name: str,
            title: str,
            initial_position: NativeScreenArea,
            painter: PaintWindowCallback,
            on_exit: Callable[[], None],
            font: Optional[str] = None,
            has_border: Optional[bool] = True,
            is_always_on_top: Optional[bool] = False,
            is_on_taskbar: Optional[bool] = True,
    ) -> None:
        self.__has_quit = False
        self.__removing = False
        self.__hwnd = None
        self.__hfont = None
        self.__is_always_on_top = is_always_on_top
        self.__on_exit = on_exit

        # Because of multi-threading issues, a resize may come in after initial creation
        self.__is_position_set = False
        self.__initial_position = initial_position

        def do_paint(hwnd: HWND, hdc: HDC) -> None:
            window_size = WINDOWS_FUNCTIONS.window.client_rectangle(hwnd)
            if isinstance(window_size, WindowsErrorMessage):
                # TODO logging
                pass
            else:
                painter(Painter(hwnd, hdc, window_size))

        # noinspection PyUnusedLocal
        def paint(hwnd: HWND, message: int, wparam: WPARAM, lparam: LPARAM) -> bool:
            res = WINDOWS_FUNCTIONS.window.do_paint(hwnd, do_paint)
            if isinstance(res, WindowsErrorMessage):
                # This usually means that the window is no longer available.
                self.close()
            return True

        def on_exit_callback() -> None:
            self.__has_quit = True
            self.close()

        self._message_id_callbacks = {
            windows_constants.WM_PAINT: paint,
        }

        def message_pumper() -> None:
            # These MUST be in the same thread!
            message_callback_handler = WINDOWS_FUNCTIONS.shell.create_global_message_handler(self._message_id_callbacks)

            if has_border:
                self.__hwnd = WINDOWS_FUNCTIONS.window.create_display_window(
                    class_name, title, message_callback_handler, {
                        'border', 'dialog-frame', 'sysmenu-button', 'size-border', 'minimize-button', 'maximize-button'
                    }
                )
            else:
                self.__hwnd = WINDOWS_FUNCTIONS.window.create_borderless_window(
                    class_name, title, message_callback_handler, self._message_id_callbacks,
                    show_on_taskbar=is_on_taskbar, always_on_top=is_always_on_top
                )

            if font is not None:
                self.__hfont = WINDOWS_FUNCTIONS.window.get_font_for_description(font, hwnd=self.__hwnd)

            if is_always_on_top:
                WINDOWS_FUNCTIONS.window.set_position(
                    self.__hwnd, 'topmost',
                    self.__pos_x, self.__pos_y, self.__width, self.__height,
                    ('no-activate',)
                )
            else:
                WINDOWS_FUNCTIONS.window.move_resize(
                    self.__hwnd, self.__pos_x, self.__pos_y, self.__width, self.__height, False
                )

            WINDOWS_FUNCTIONS.shell.pump_messages(on_exit_callback)

            self._log_verbose("Window {0} quit".format(self.cid))
            self.__has_quit = True

        pump_thread = threading.Thread(
            target=message_pumper,
            daemon=True
        )
        pump_thread.start()

    def close(self) -> None:
        if not self.__removing:
            self.__removing = True
            if not self.__has_quit:
                self._log_debug("Sending quit message to window {0} / {1}".format(self.cid, self.__hwnd))
                # window__send_message(self.__hwnd, windows_constants.WM_QUIT, 0, 0)
                WINDOWS_FUNCTIONS.window.post_message(self.__hwnd, windows_constants.WM_CLOSE, 0, 0)
            self.__on_exit()

    def add_message_handler(self, message_id: Union[int, str], handler) -> None:
        if isinstance(message_id, str):
            message_id = windows_constants.WM_MESSAGE_NAMES[message_id]
        self._message_id_callbacks[message_id] = handler

    def draw(self) -> None:
        if not self.__has_quit:
            res = WINDOWS_FUNCTIONS.window.repaint(self.__hwnd)
            if isinstance(res, WindowsErrorMessage):
                # This usually means that the window is no longer available.
                self.close()

    def draw_now(self) -> None:
        def do_paint(hwnd: HWND, hdc: HDC) -> None:
            window_size = WINDOWS_FUNCTIONS.window.client_rectangle(hwnd)
            self._on_paint(hwnd, hdc, window_size.width, window_size.height)
        try:
            window__do_draw(self.__hwnd, do_paint)
        except OSError:
            # This usually means that the window is no longer available.
            self.close()

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
                'topmost',  # 'top',
                pos_x, pos_y, width, height,
                ['no-activate'])
        else:
            # window__move_resize(self.__hwnd, pos_x, pos_y, width, height, False)
            window__set_position(
                self.__hwnd,
                'no-topmost',  # 'top',
                pos_x, pos_y, width, height,
                ['no-activate'])
