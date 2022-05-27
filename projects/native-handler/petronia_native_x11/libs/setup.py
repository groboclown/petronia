"""Sets up the X connection stuff."""

from typing import Sequence, List, Callable
from petronia_common.util import StdRet, PetroniaReturnError, RET_OK_NONE
from .api import XcbApi
from .hook_manager import HookManager
from .event_hook import setup_events, EventApi
from .ewmh_hook import setup_ewmh, EwmhApi
from .dbus_hook import setup_dbus, DbusApi
from .graphics_hook import setup_grapics_context, GraphicsContextApi
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
            events: EventApi,
            ewmh: EwmhApi,
            gc: GraphicsContextApi,
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

    def dispose(self, timeout: float) -> StdRet[None]:
        """Shut everything down."""
        errs: List[PetroniaReturnError] = []
        for callback in self.__shutdown:
            res = callback(self.__xcb, timeout)
            if res.has_error:
                errs.append(res.valid_error)
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
    hook_manager = HookManager()

    dbus_res = setup_dbus(hook_manager.for_hook())
    if dbus_res.has_error:
        return dbus_res.forward()
    # dbus has its own listener for things.

    event_res = setup_events(hook_manager.for_hook())
    if event_res.has_error:
        return event_res.forward()
    events = event_res.result
    # events doesn't have event handlers, because, well, it's the events.

    ewmh_res = setup_ewmh(hook_manager.for_hook())
    if ewmh_res.has_error:
        return ewmh_res.forward()
    events.add_event_hook(ewmh_res.result.get_event_handler())

    gc_res = setup_grapics_context(hook_manager.for_hook())
    if gc_res.has_error:
        return gc_res.forward()
    # gc doesn't have hooks into the event loop... does it?

    kb_res = setup_keyboard(hook_manager.for_hook())
    if kb_res.has_error:
        return kb_res.forward()
    events.add_event_hook(kb_res.result.get_event_handler())

    screen_res = setup_screens(hook_manager.for_hook())
    if screen_res.has_error:
        return screen_res.forward()
    events.add_event_hook(screen_res.result.get_event_handler())

    win_res = setup_windows(hook_manager.for_hook())
    if win_res.has_error:
        return win_res.forward()
    events.add_event_hook(win_res.result.get_event_handler())

    ext_res = setup_x_ext(hook_manager.for_hook())
    if ext_res.has_error:
        return ext_res.forward()
    events.add_event_hook(ext_res.result.get_event_handler())

    wm_res = connect_as_window_manager(
        on_server_init=hook_manager.initializers,
        use_argb_visual=use_argb_visual,
        replace_existing_wm=replace_existing_wm,
    )
    if wm_res.has_error:
        return wm_res.forward()
    # wm sets up connections and the base API.

    wm = wm_res.result
    for event in wm.pending_events:
        events.add_pending_event(event)

    on_shutdown = list(hook_manager.shutdown)
    on_shutdown.extend(wm.shutdown)

    return StdRet.pass_ok(X11Access(
        xcb=wm.xcb,
        dbus=dbus_res.result,
        events=events,
        ewmh=ewmh_res.result,
        gc=gc_res.result,
        keys=kb_res.result,
        windows=win_res.result,
        screens=screen_res.result,
        ext=ext_res.result,
        on_shutdown=on_shutdown,
    ))
