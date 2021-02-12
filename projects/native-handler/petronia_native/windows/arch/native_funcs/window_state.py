"""Native Window state information."""

from typing import Iterable, List
from typing import cast as t_cast
from .windows_common import (
    GUITHREADINFO,
    HWND, RECT,
)
from ..windows_constants import (
    GUI_CARETBLINKING,
    GUI_INMENUMODE,
    GUI_INMOVESIZE,
    GUI_POPUPMENUMODE,
    GUI_SYSTEMMENUMODE,
)
from ....common import defs


def convert_rect(rect: RECT) -> defs.OsScreenRect:
    """Convert a Windows RECT structure into the common NativeScreenRect structure."""
    return defs.OsScreenRect(
        x=t_cast(int, rect.left),
        y=t_cast(int, rect.top),
        width=t_cast(int, rect.right) - t_cast(int, rect.left),
        height=t_cast(int, rect.bottom) - t_cast(int, rect.top),
        left=t_cast(int, rect.left),
        right=t_cast(int, rect.right),
        top=t_cast(int, rect.top),
        bottom=t_cast(int, rect.bottom),
    )


class WindowsWindowState:  # pylint:disable=too-many-instance-attributes
    """Windows information on the state of a GUI window."""

    __slots__ = (
        '__flags', '__active', '__focus', '__capture',
        '__menu_owner', '__move_size', '__caret', '__caret_rect',
    )

    def __init__(  # pylint:disable=too-many-arguments
            self,
            flags: Iterable[str],
            active: HWND,
            focus: HWND,
            capture: HWND,
            menu_owner: HWND,
            move_size: HWND,
            caret: HWND,
            caret_rect: defs.OsScreenRect,
     ) -> None:
        self.__flags = tuple(flags)
        self.__active = active
        self.__focus = focus
        self.__capture = capture
        self.__menu_owner = menu_owner
        self.__move_size = move_size
        self.__caret = caret
        self.__caret_rect = caret_rect

    @property
    def flags(self) -> Iterable[str]:
        """List of window flags"""
        return self.__flags

    @property
    def active(self) -> HWND:
        """Active UI element handle"""
        return self.__active

    @property
    def focus(self) -> HWND:
        """Focused UI element handle"""
        return self.__focus

    @property
    def capture(self) -> HWND:
        """?"""
        return self.__capture

    @property
    def menu_owner(self) -> HWND:
        """Owner of the top menu."""
        return self.__menu_owner

    @property
    def move_size(self) -> HWND:
        """?"""
        return self.__move_size

    @property
    def caret(self) -> HWND:
        """The kind of text caret to show?"""
        return self.__caret

    @property
    def caret_rect(self) -> defs.OsScreenRect:
        """Location of the drawn text caret."""
        return self.__caret_rect


def create_windows_window_state(gui_info: GUITHREADINFO) -> WindowsWindowState:
    """Create the windows state based on the GUI information structure."""
    flags: List[str] = []

    if gui_info.flags & GUI_CARETBLINKING == GUI_CARETBLINKING:
        flags.append('caret-blinking')
    if gui_info.flags & GUI_INMENUMODE == GUI_INMENUMODE:
        flags.append('in-menu-mode')
    if gui_info.flags & GUI_INMOVESIZE == GUI_INMOVESIZE:
        flags.append('in-move-size')
    if gui_info.flags & GUI_POPUPMENUMODE == GUI_POPUPMENUMODE:
        flags.append('popup-menu-mode')
    if gui_info.flags & GUI_SYSTEMMENUMODE == GUI_SYSTEMMENUMODE:
        flags.append('in-system-menu-mode')

    return WindowsWindowState(
        flags=flags,
        active=gui_info.hwndActive,
        focus=gui_info.hwndFocus,
        capture=gui_info.hwndCapture,
        menu_owner=gui_info.hwndMenuOwner,
        move_size=gui_info.hwndMoveSize,
        caret=gui_info.hwndCaret,
        caret_rect=convert_rect(gui_info.rcCaret),
    )
