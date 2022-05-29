"""Sets up the X connection stuff."""

from typing import Sequence, List, Callable
from petronia_common.util import StdRet, PetroniaReturnError, RET_OK_NONE
from .api import XcbApi
from .event_handler import EventHandlerLoop
from .hook_manager import HookManager
from .ewmh_hook import setup_ewmh, EwmhApi
from .dbus_hook import setup_dbus, DbusApi
from .pui_hook import setup_petronia_ui, PetroniaUiApi
from .keyboard_hook import setup_keyboard, KeyboardAPI
from .screens_hook import setup_screens, ScreenApi
from .window_hook import setup_windows, WindowApi
from .x_extension_hook import setup_x_ext, XExtensionApi
from .wm_connect import connect_as_window_manager


class X11Access:
    __slots__ = (
        '__xcb', '__dbus', '__events', '__ewmh', '__gc',
        '__keys', '__ext', '__windows', '__screens',
        '__shutdown',
    )

    def __init__(
            self, *,
            xcb: XcbApi,
            dbus: DbusApi,
            events: EventHandlerLoop,
            ewmh: EwmhApi,
            gc: PetroniaUiApi,
            keys: KeyboardAPI,
            windows: WindowApi,
            screens: ScreenApi,
            ext: XExtensionApi,
            on_shutdown: Sequence[Callable[[XcbApi, float], StdRet[None]]],
    ) -> None:
        self.__xcb = xcb
        self.__dbus = dbus
        self.__events = events
        self.__ewmh = ewmh
        self.__gc = gc
        self.__keys = keys
        self.__windows = windows
        self.__screens = screens
        self.__ext = ext
        self.__shutdown = on_shutdown

    def is_running(self) -> bool:
        """Is the event loop fully up and running?"""
        return self.__events.is_running()

    def start(self) -> None:
        """Start the event listener."""
        self.__events.start()

    def dispose(self, timeout: float) -> StdRet[None]:
        """Shut everything down."""
        errs: List[PetroniaReturnError] = []
        for callback in self.__shutdown:
            res = callback(self.__xcb, timeout)
            if res.has_error:
                errs.append(res.valid_error)
        self.__events.stop(timeout)
        if not errs:
            return RET_OK_NONE
        return StdRet.pass_error(*errs)


def setup_x11(
        *,
        use_argb_visual: bool,
        replace_existing_wm: bool,
) -> StdRet[X11Access]:
    """Set up the connection, attach as the window manager,
    set up all the hooks, and return the API."""

    # TODO should the errors be accumulated rather than
    #   returning right away?

    hook_manager = HookManager()

    dbus_res = setup_dbus(hook_manager.for_hook())
    if dbus_res.has_error:
        return dbus_res.forward()

    ewmh_res = setup_ewmh(hook_manager.for_hook())
    if ewmh_res.has_error:
        return ewmh_res.forward()

    gc_res = setup_petronia_ui(hook_manager.for_hook())
    if gc_res.has_error:
        return gc_res.forward()

    kb_res = setup_keyboard(hook_manager.for_hook())
    if kb_res.has_error:
        return kb_res.forward()

    screen_res = setup_screens(hook_manager.for_hook())
    if screen_res.has_error:
        return screen_res.forward()

    win_res = setup_windows(hook_manager.for_hook())
    if win_res.has_error:
        return win_res.forward()

    ext_res = setup_x_ext(hook_manager.for_hook())
    if ext_res.has_error:
        return ext_res.forward()

    # wm sets up connections and the base API.
    wm_res = connect_as_window_manager(
        on_server_init=hook_manager.screen_initializers,
        use_argb_visual=use_argb_visual,
        replace_existing_wm=replace_existing_wm,
    )
    if wm_res.has_error:
        return wm_res.forward()

    wm = wm_res.result
    # After the screen grab, and before the event loop starts running,
    #   run the next initializer set.
    for pre_event_callback in hook_manager.pre_event_initializers:
        pre_event_res = pre_event_callback(wm.xcb)
        if pre_event_res.has_error:
            return pre_event_res.forward()

    on_shutdown = list(hook_manager.shutdown)
    on_shutdown.extend(wm.shutdown)

    return StdRet.pass_ok(X11Access(
        xcb=wm.xcb,
        dbus=dbus_res.result,
        events=wm.event_loop,
        ewmh=ewmh_res.result,
        gc=gc_res.result,
        keys=kb_res.result,
        windows=win_res.result,
        screens=screen_res.result,
        ext=ext_res.result,
        on_shutdown=on_shutdown,
    ))
