"""Event loop handler."""

from typing import List, Mapping, Tuple, Hashable, Union, Optional
import threading
import ctypes
from petronia_common.util import (
    StdRet, UserMessage, V,
    join_errors,
    RET_OK_NONE, RET_OK_FALSE, RET_OK_TRUE,
)
from petronia_common.util import i18n as _
from petronia_ext_lib import logging
from petronia_native.common import user_messages
from petronia_native.common.defs import ScreenRect
from petronia_native.common.events.impl.window import ScreenDimension
from petronia_native.common.handlers import window
from petronia_native.common.events.impl import window as window_events
from ..datastore.petronia_native_x11 import EXTENSION_NAME
from ..hook_types import Hook
from ..common_data import (
    Libraries, WindowManagerData,
    ROOT_WINDOW_EVENT_MASK__c, CLIENT_WINDOW_EVENT_MASK__c,
)
from ..running_data import RunningData
from ..libs import libxcb_types, libxcb_consts, ct_util


class X11WindowHandler(window.ActiveWindow[libxcb_types.XcbWindow]):
    """An active window with Windows data."""
    __slots__ = (
        '__request', '__size_state',
        '__request_border', '__request_sibling', '__request_stack_mode',
        '__override_redirect', '__frame_window', '__owner_window_id',
        'mapped',
    )

    def __init__(
            self,
            window_id: str,
            wid: libxcb_types.XcbWindow,
            state: window_events.WindowState,
            border: int,
            override_redirect: bool,
    ) -> None:
        window.ActiveWindow.__init__(
            self, window_id, wid,
            _hashable_native_id(wid),
            state,
        )
        self.__request = state.location
        self.__request_border = border
        self.mapped = False
        self.__request_sibling: Optional[int] = None
        self.__request_stack_mode: Optional[int] = None
        self.__override_redirect = override_redirect
        self.__owner_window_id = wid
        self.__frame_window: Optional[libxcb_types.XcbWindow] = None
        self._update_meta_value(
            WINDOW_SETTING__METRICS_BORDER_WIDTH, str(border), WINDOW_META_STYLES,
        )
        print(f"[X11 WINDOW] Constructor {wid}- set border to {border}")

    def copy_as_mapped_id(
            self, new_id: libxcb_types.XcbWindow,
            is_now_override: Optional[bool] = None,
    ) -> 'X11WindowHandler':
        """Create a copy of this window, using the new ID as the new native ID for the
        window.  Called when the window is remapped."""
        ret = X11WindowHandler(
            window_id=self.window_id,
            wid=new_id,
            state=self.state,
            border=self.__request_border,
            override_redirect=(
                self.__override_redirect if is_now_override is None
                else is_now_override
            ),
        )
        ret.__request = self.__request
        ret.__request_border = self.__request_border
        ret.mapped = self.mapped  # don't set to true yet...
        ret.__request_sibling = self.__request_sibling
        ret.__request_stack_mode = self.__request_stack_mode
        # self.__override_redirect handled in constructor
        ret.__owner_window_id = self.__owner_window_id
        ret.__frame_window = self.__frame_window
        ret._update_meta_value(
            WINDOW_SETTING__METRICS_BORDER_WIDTH, str(self.__request_border), WINDOW_META_STYLES,
        )
        ret._update_meta_value(
            WINDOW_SETTING__METRICS_SIBLING, str(self.__request_sibling), WINDOW_META_STYLES,
        )
        ret._update_meta_value(
            WINDOW_SETTING__METRICS_STACK_MODE, str(self.__request_stack_mode), WINDOW_META_STYLES,
        )
        print(f"[X11 WINDOW] Copy {new_id}- set border to {self.__request_border}")

        return ret

    @property
    def owner_window_id(self) -> libxcb_types.XcbWindow:
        return self.__owner_window_id

    @property
    def frame_window_id(self) -> Optional[libxcb_types.XcbWindow]:
        return self.__frame_window

    def set_frame_window(self, window_id: libxcb_types.XcbWindow) -> StdRet[None]:
        if self.__frame_window is not None:
            return StdRet.pass_errmsg(
                user_messages.TRANSLATION_CATALOG,
                _('window {wid} {native} already has an active frame'),
                wid=self.window_id,
                native=str(self.hashable_native_id),
            )
        self.__frame_window = window_id
        return RET_OK_NONE

    def removed_frame(self) -> None:
        # Do a check?
        self.__frame_window = None

    @property
    def override_redirect(self) -> bool:
        return self.__override_redirect

    def get_border_width(self) -> int:
        """Get the stored border width."""
        return self.__request_border

    def get_sibling(self) -> Optional[int]:
        """Get the sibling state, if set."""
        return self.__request_sibling

    def get_stack_mode(self) -> Optional[int]:
        """Get the stack mode, if set."""
        return self.__request_stack_mode

    def send_state(self, data: WindowManagerData) -> StdRet[None]:
        """Sends the state to Petronia and to X."""
        mask = (
                libxcb_consts.XCB_CONFIG_WINDOW_X
                | libxcb_consts.XCB_CONFIG_WINDOW_Y
                | libxcb_consts.XCB_CONFIG_WINDOW_WIDTH
                | libxcb_consts.XCB_CONFIG_WINDOW_HEIGHT
                | libxcb_consts.XCB_CONFIG_WINDOW_BORDER_WIDTH
        )
        user_messages.low_println(
            f"[X11] Setting window {self.window_id} / {self.native_id} to position "
            f"({self.__request.x}, {self.__request.y}) sized "
            f"({self.__request.width}, {self.__request.height}) with "
            f"border {self.__request_border} "
            f"sibling {self.__request_sibling} "
            f"stack {self.__request_stack_mode}"
        )
        value_list = [
            ctypes.c_int32(self.__request.x),
            ctypes.c_int32(self.__request.y),
            ctypes.c_int32(self.__request.width),  # WRONG should be uint32, but ctypes fails
            ctypes.c_int32(self.__request.height),  # WRONG should be uint32, but ctypes fails
            ctypes.c_int32(self.__request_border),  # WRONG should be uint32, but ctypes fails
        ]
        if self.__request_sibling is not None:
            mask |= libxcb_consts.XCB_CONFIG_WINDOW_SIBLING
            value_list.append(ctypes.c_int32(self.__request_sibling))
        if self.__request_stack_mode is not None:
            mask |= libxcb_consts.XCB_CONFIG_WINDOW_STACK_MODE
            value_list.append(ctypes.c_int32(self.__request_stack_mode))
        values = ct_util.as_int32_list(*value_list)

        if self.__frame_window:
            data.libs.xcb.xcb_configure_window(data.connection, self.__frame_window, mask, values)
        else:
            data.libs.xcb.xcb_configure_window(data.connection, self.native_id, mask, values)
        return window.store_window_details(
            data.libs.context, self.window_id, self.state,
        )

    def update_settings(self, new_settings: Mapping[str, str]) -> StdRet[bool]:
        changed = False
        problems: List[UserMessage] = []
        for key, val in new_settings.items():
            if key == WINDOW_SETTING__METRICS_BORDER_WIDTH:
                try:
                    int_val = int(val)
                    if int_val < 0:
                        # Caught by outer except
                        raise ValueError()
                    self._update_meta_value(key, val, WINDOW_META_STYLES)
                    print(f"[X11 WINDOW] Update settings {self.native_id}- set border to {int_val}")
                    self.__request_border = int_val
                    changed = True
                except ValueError:
                    problems.append(UserMessage(
                        user_messages.TRANSLATION_CATALOG,
                        _('invalid {setting} = "{value}" (must be a non-negative integer)'),
                        setting=key,
                        value=val,
                    ))
            elif key == WINDOW_SETTING__METRICS_SIBLING:
                try:
                    int_val = int(val)
                    self._update_meta_value(key, val, WINDOW_META_STYLES)
                    self.__request_sibling = int_val
                    changed = True
                except ValueError:
                    problems.append(UserMessage(
                        user_messages.TRANSLATION_CATALOG,
                        _('invalid {setting} = "{value}" (must be an integer)'),
                        setting=key,
                        value=val,
                    ))
            elif key == WINDOW_SETTING__METRICS_STACK_MODE:
                try:
                    int_val = int(val)
                    self._update_meta_value(key, val, WINDOW_META_STYLES)
                    self.__request_stack_mode = int_val
                    changed = True
                except ValueError:
                    problems.append(UserMessage(
                        user_messages.TRANSLATION_CATALOG,
                        _('invalid {setting} = "{value}" (must be an integer)'),
                        setting=key,
                        value=val,
                    ))
            else:
                problems.append(UserMessage(
                    user_messages.TRANSLATION_CATALOG,
                    _('unknown {setting} = "{value}"'),
                    setting=key,
                    value=val,
                ))
        if problems:
            return StdRet.pass_error(join_errors(*problems))
        if changed:
            return RET_OK_TRUE
        return RET_OK_FALSE

    def update_from_explicit(
            self, from_x: bool,
            pos_x: int, pos_y: int, width: int, height: int,
            border_width: Optional[int] = None,
            sibling: Optional[int] = None,
            stack_mode: Optional[int] = None,
    ) -> None:
        """Update the internal state data position of the window."""

        if border_width is None:
            border_width = self.__request_border
        else:
            self._update_meta_value(
                WINDOW_SETTING__METRICS_BORDER_WIDTH, str(border_width), WINDOW_META_STYLES,
            )
        if sibling is None:
            sibling = self.__request_sibling
        else:
            self._update_meta_value(
                WINDOW_SETTING__METRICS_SIBLING, str(sibling), WINDOW_META_STYLES,
            )
        if stack_mode is None:
            stack_mode = self.__request_stack_mode
        else:
            self._update_meta_value(
                WINDOW_SETTING__METRICS_STACK_MODE, str(stack_mode), WINDOW_META_STYLES,
            )

        if not (from_x and self.mapped) or self.__override_redirect:
            # If the client sent this request and the client is mapped, then don't
            #   use the request (use our own settings).
            # However, if the window bypasses the window manager, then ignore Petronia settings.
            self.__request = ScreenDimension(
                x=pos_x, y=pos_y, width=width, height=height,
            )
            self.__request_border = border_width
            self.__request_sibling = sibling
            self.__request_stack_mode = stack_mode
            self.state.location = ScreenDimension(
                x=pos_x, y=pos_y, width=width, height=height,
            )
            print(
                f"[X11 WINDOW] Update {self.native_id} - set window to "
                f"({pos_x}, {pos_y}) sized ({width}, {height}) border {border_width}"
            )
        else:
            print(
                f"[X11 WINDOW] Update {self.native_id} - ignored because "
                f"from_x={from_x}, mapped={self.mapped}, override={self.__override_redirect}"
            )


GLOBAL_SETTING__METRICS_BORDER_WIDTH = 'border-width'
DEFAULT_GLOBAL_SETTING__METRICS_BORDER_WIDTH = 2

DEFAULT_GLOBAL_SETTINGS: Mapping[str, str] = {
    GLOBAL_SETTING__METRICS_BORDER_WIDTH: str(DEFAULT_GLOBAL_SETTING__METRICS_BORDER_WIDTH),
}
GLOBAL_SETTINGS_DESCRIPTIONS: Mapping[str, str] = {
    GLOBAL_SETTING__METRICS_BORDER_WIDTH: 'The thickness of the sizing border, in pixels.',
}

WINDOW_SETTING__METRICS_BORDER_WIDTH = 'border-width'
WINDOW_SETTING__METRICS_STACK_MODE = 'stack-mode'
WINDOW_SETTING__METRICS_SIBLING = 'sibling'
WINDOW_META_STYLES: Mapping[str, str] = {
    WINDOW_SETTING__METRICS_BORDER_WIDTH: 'The thickness of the sizing border, in pixels.',
    WINDOW_SETTING__METRICS_STACK_MODE: 'The stack mode enum; read-only',
    WINDOW_SETTING__METRICS_SIBLING: 'The sibling value; read-only',
}


class WindowHook(Hook, window.AbstractWindowHandler[X11WindowHandler, libxcb_types.XcbWindow]):
    """Connections between the X11 event loop and Petronia.  All Petronia events are
    handled in the Petronia event loop thread, so the X11 requests must be sent
    to that thread via an enqueue call.  All X11 events are handled in the X11 thread,
    but the entrypoint sets up the context so that writes are performed in another
    thread, making it safe to be called from the X11 event loop."""

    __slots__ = (
        '__lock',
        '__data',
    )

    def __init__(self) -> None:
        window.AbstractWindowHandler.__init__(
            self,
            initial_global_settings=DEFAULT_GLOBAL_SETTINGS,
            global_meta_desc=GLOBAL_SETTINGS_DESCRIPTIONS,
            window_meta_desc=WINDOW_META_STYLES,
        )
        self.__lock = threading.Lock()
        self.__data: Optional[RunningData] = None

    def setup_wm_screen(self, data: WindowManagerData) -> StdRet[None]:
        return RET_OK_NONE

    def setup_pre_event_loop(self, data: RunningData) -> StdRet[None]:
        self.__data = data

        # We have all the running data at this point, so find the existing
        #   windows.
        screen_tree_cookie = data.xcb.xcb_query_tree_unchecked(
            data.connection,
            data.screen_root,
        )
        trees = data.xcb.xcb_query_tree_reply(
            data.connection, screen_tree_cookie, libxcb_consts.NULL__XcbGenericErrorPP,
        )
        window_count = ct_util.as_py_int(data.xcb.xcb_query_tree_children_length(trees))
        tree_windows = data.xcb.xcb_query_tree_children(trees)
        win_requests: List[Tuple[
            libxcb_types.XcbWindow,
            libxcb_types.XcbGetWindowAttributesCookie,
            libxcb_types.XcbGetGeometryCookie,
        ]] = []
        for idx in range(0, window_count):
            win_requests.append((
                tree_windows[idx],
                data.xcb.xcb_get_window_attributes_unchecked(data.connection, tree_windows[idx]),
                data.xcb.xcb_get_geometry(data.connection, tree_windows[idx]),
            ))
        data.clib.force_free(trees)

        for window_id, geom_cookie, attribute_cookie in win_requests:
            attributes = data.xcb.xcb_get_window_attributes_reply(
                data.connection, attribute_cookie, libxcb_consts.NULL__XcbGenericErrorPP,
            )
            attribute_data = attributes.contents
            geom = data.xcb.xcb_get_geometry_reply(
                data.connection, geom_cookie, libxcb_consts.NULL__XcbGenericErrorPP,
            )
            geom_data = geom.contents
            self._internal_create_window(
                native_id=window_id, pos_x=geom_data.x, pos_y=geom_data.y,
                width=geom_data.width, height=geom_data.height,
                border_width=geom_data.border_width,
                override_redirect=ct_util.as_py_int(attribute_data.override_redirect) == 1,
            )
            data.clib.force_free(geom)
            data.clib.force_free(attributes)
            if (
                    ct_util.as_py_int(attribute_data.map_state)
                    != libxcb_consts.XCB_MAP_STATE_UNVIEWABLE
            ):
                self._internal_map_window(window_id, _req(self.get_window_by_native(window_id)))
            else:
                user_messages.low_println(f"[X11] Not mapping unviewable window {window_id}")

        registrar = data.event_loop.get_event_registrar()
        registrar.register_buttonpress_callback(self._x11_buttonpress_event)
        registrar.register_buttonrelease_callback(self._x11_buttonrelease_event)
        registrar.register_window_create_callback(self._x11_create_event)
        registrar.register_window_destroy_callback(self._x11_destroy_event)
        registrar.register_map_request_callback(self._x11_map_request_event)
        registrar.register_configure_request_callback(self._x11_configure_request_event)
        registrar.register_motion_callback(self._x11_motion_event)
        registrar.register_enter_callback(self._x11_enter_event)
        registrar.register_leave_callback(self._x11_leave_event)
        registrar.register_focus_in_callback(self._x11_focusin_event)
        registrar.register_focus_out_callback(self._x11_focusout_event)
        registrar.register_unmap_callback(self._x11_unmap_event)

        return RET_OK_NONE

    def shutdown(self, data: RunningData) -> StdRet[None]:
        # No need to tell X to move the windows back, because we
        #   save their state at map time, which means when this
        #   shuts down, their state is restored.

        with self.__lock:
            for win in self.get_active_windows():
                user_messages.report_send_receive_problems(win.send_state(data.window_manager_data))

            self.__data = None

        return RET_OK_NONE

    def _on_error(self, request: str, res: StdRet[V]) -> bool:
        if self.__data and res.has_error:
            logging.send_system_error(
                self.__data.context, f'{EXTENSION_NAME}:system',
                res.valid_error, request, ('os',),
            )
            return True
        return False

    def _on_missing_window(self, request: str, window_id: libxcb_types.XcbWindow) -> bool:
        if self.__data:
            logging.send_log_message(
                self.__data.context, f'{EXTENSION_NAME}:system', 'warning',
                [UserMessage(
                    user_messages.TRANSLATION_CATALOG,
                    _('{request} for unknown window {window_id}'),
                    request=request,
                    window_id=ct_util.as_py_int(window_id),
                )],
            )
        return True

    # =======================================================================
    # AbstractWindowHandler
    #   Called from within Petronia listener thread.
    def hash_native_id(self, native_id: libxcb_types.XcbWindow) -> Hashable:
        return _hashable_native_id(native_id)

    def on_set_window_position_request(  # pylint:disable=arguments-differ
            self, native_window: X11WindowHandler, new_location: window_events.ScreenDimension,
    ) -> StdRet[None]:
        data = self.__data
        if data and data.connection:
            print(
                f"[X11] Petronia requesting to move window {native_window.native_id} to "
                f"({new_location.x}, {new_location.y}) sized "
                f"({new_location.width}, {new_location.height})"
            )
            native_window.update_from_explicit(
                from_x=False,
                pos_x=new_location.x,
                pos_y=new_location.y,
                width=new_location.width,
                height=new_location.height,
            )
            # Send the update, even if the window is unmapped.
            return native_window.send_state(data.window_manager_data)
        return _on_not_set_up()

    def on_close_window_request(  # pylint:disable=arguments-differ
            self, native_window: X11WindowHandler,
    ) -> StdRet[None]:
        print(f"[X11] Petronia request to close window {native_window.native_id}")
        # TODO IMPLEMENT
        return RET_OK_NONE

    def on_minimize_window_request(  # pylint:disable=arguments-differ
            self, native_window: X11WindowHandler,
    ) -> StdRet[None]:
        print(f"[X11] Petronia request to minimize window {native_window.native_id}")
        # TODO IMPLEMENT
        return RET_OK_NONE

    def on_maximize_window_request(  # pylint:disable=arguments-differ
            self, native_window: X11WindowHandler,
    ) -> StdRet[None]:
        print(f"[X11] Petronia request to maximize window {native_window.native_id}")
        # TODO IMPLEMENT
        return RET_OK_NONE

    def on_restore_window_request(self, native_window: X11WindowHandler) -> StdRet[None]:
        print(f"[X11] Petronia request to restore window {native_window.native_id}")
        # TODO IMPLEMENT
        return RET_OK_NONE

    def on_set_window_settings(
            self, native_window: X11WindowHandler, settings: Mapping[str, str],
    ) -> StdRet[None]:
        print(f"[X11] Petronia request to change window {native_window.native_id} settings")
        res = native_window.update_settings(settings)
        if res.has_error:
            return res.forward()
        data = self.__data
        if res.result and data and data.connection:
            return native_window.send_state(data.window_manager_data)
        return RET_OK_NONE

    def on_set_focused_window(
            self, native_window: X11WindowHandler, focus_id: int,
    ) -> StdRet[None]:
        print(f"[X11] Petronia request to focus window {native_window.native_id}")
        # TODO IMPLEMENT
        return RET_OK_NONE

    def on_set_global_settings(self, settings: Mapping[str, str]) -> StdRet[None]:
        print(f"[X11] Petronia request to change global settings")
        # TODO IMPLEMENT
        return RET_OK_NONE

    # =======================================================================
    # X11 Callbacks
    #  All these run in the x server thread.
    #  The event value will be invalid once the function returns.  If it calls
    #  into any thread, then the used event data will need to be copied
    #  out before calling into the thread.  This means the data contained in
    #  event.contents, as that will be an invalid memory reference.

    # ButtonPressEventCallback
    def _x11_buttonpress_event(self, event: libxcb_types.XcbButtonPressEventP) -> Optional[bool]:
        pass

    # ButtonReleaseEventCallback
    def _x11_buttonrelease_event(
            self, event: libxcb_types.XcbButtonReleaseEventP,
    ) -> Optional[bool]:
        pass

    # ConfigureEventCallback
    def _x11_configure_request_event(
            self, event: libxcb_types.XcbConfigureRequestEventP,
    ) -> Optional[bool]:
        # This is the big event.  It determines the name, position, size, and all kind of
        # things that the window wants to set about itself.
        data = self.__data
        if not data:
            return False
        event_data = _req(event.contents)

        window_id = event_data.window

        win = self.get_window_by_native(window_id)
        if not win:
            window_id = event_data.parent
            win = self.get_window_by_native(window_id)
            if not win:
                return self._on_missing_window('configure', window_id)
        if win.mapped:
            # Ignore configure request
            user_messages.low_println(f"[X11] Ignoring X request to configure {win.window_id}")
            return False

        # Cache values
        req_x = event_data.x
        req_y = event_data.y
        req_w = event_data.width
        req_h = event_data.height
        req_b = event_data.border_width
        req_sib = event_data.sibling
        req_stx = event_data.stack_mode
        value_mask = ct_util.as_py_int(event_data.value_mask)

        new_x = win.state.location.x
        new_y = win.state.location.y
        new_w = win.state.location.width
        new_h = win.state.location.height
        new_b = win.get_border_width()
        new_sib = win.get_sibling()
        new_stx = win.get_stack_mode()

        resp_mask = 0
        resp_list: List[ctypes.c_int32] = []

        # Note: order of bit checking is extremely important.
        if value_mask & libxcb_consts.XCB_CONFIG_WINDOW_X != 0:
            new_x = ct_util.as_py_int(req_x)
            resp_mask |= libxcb_consts.XCB_CONFIG_WINDOW_X
            resp_list.append(req_x)
        if value_mask & libxcb_consts.XCB_CONFIG_WINDOW_Y != 0:
            new_y = ct_util.as_py_int(req_y)
            resp_mask |= libxcb_consts.XCB_CONFIG_WINDOW_Y
            resp_list.append(req_y)
        if value_mask & libxcb_consts.XCB_CONFIG_WINDOW_WIDTH != 0:
            new_w = ct_util.as_py_int(req_w)
            resp_mask |= libxcb_consts.XCB_CONFIG_WINDOW_WIDTH
            resp_list.append(req_w)
        if value_mask & libxcb_consts.XCB_CONFIG_WINDOW_HEIGHT != 0:
            new_h = ct_util.as_py_int(req_h)
            resp_mask |= libxcb_consts.XCB_CONFIG_WINDOW_HEIGHT
            resp_list.append(req_h)
        if value_mask & libxcb_consts.XCB_CONFIG_WINDOW_BORDER_WIDTH != 0:
            new_b = ct_util.as_py_int(req_b)
            resp_mask |= libxcb_consts.XCB_CONFIG_WINDOW_BORDER_WIDTH
            resp_list.append(req_b)
        if value_mask & libxcb_consts.XCB_CONFIG_WINDOW_SIBLING != 0:
            new_sib = ct_util.as_py_int(req_sib)
            resp_mask |= libxcb_consts.XCB_CONFIG_WINDOW_SIBLING
            resp_list.append(req_sib)
        if value_mask & libxcb_consts.XCB_CONFIG_WINDOW_STACK_MODE != 0:
            new_stx = ct_util.as_py_int(req_stx)
            resp_mask |= libxcb_consts.XCB_CONFIG_WINDOW_STACK_MODE
            resp_list.append(req_stx)

        print(
            f"[X11] X configuration request for {win.window_id}: "
            f"({new_x}, {new_y}) sized ({new_w}, {new_h}) border {new_b}"
        )
        win.update_from_explicit(
            from_x=True,
            pos_x=new_x,
            pos_y=new_y,
            width=new_w,
            height=new_h,
            border_width=new_b,
            sibling=new_sib,
            stack_mode=new_stx,
        )
        user_messages.report_send_receive_problems(win.send_state(data.window_manager_data))
        # Because this is a configure, we don't pass this on to actually move the thing.
        return True

    # MapRequestEventCallback
    def _x11_map_request_event(self, event: libxcb_types.XcbMapRequestEventP) -> Optional[bool]:
        # Window is now visible.  More importantly, our window manager must now start
        #   managing it.
        user_messages.low_println(f"[X11] handling map request")

        event_data = event.contents
        data = self.__data
        if not data or not data.connection:
            user_messages.low_println(
                f"[X11] ignored map window {event_data.parent} child {event_data.window}"
            )
            return False

        owner_window_id = event_data.parent
        mapped_window_id = event_data.window

        # This mapped window ID is the new window ID.
        old_win = self.get_window_by_native(owner_window_id)
        if not old_win:
            self._on_missing_window('map-request', owner_window_id)
            return False

        # Note: this is getting/capturing the attributes by itself, which is
        #   inefficient.  If this method were to do otherwise, it must tell xcb to
        #   throw away the request cookies that aren't handled.

        # Need to load the window attributes based on the new mapped window id.
        window_attributes_cookie = data.xcb.xcb_get_window_attributes_unchecked(
            data.connection, mapped_window_id,
        )
        win: Optional[X11WindowHandler] = None
        if window_attributes_cookie:
            # Get the real override-redirect setting, and see if it's mapped to
            #   be visible.
            window_attributes = data.xcb.xcb_get_window_attributes_reply(
                data.connection, window_attributes_cookie, libxcb_consts.NULL__XcbGenericErrorPP,
            )
            if window_attributes:
                # Check if it's mapped.  It could have been mapped then immediately not
                #   mapped.
                if (
                        ct_util.as_py_int(window_attributes.contents.map_state)
                        != libxcb_consts.XCB_MAP_STATE_UNVIEWABLE
                ):
                    win = old_win.copy_as_mapped_id(
                        mapped_window_id,
                        ct_util.as_py_int(window_attributes.contents.override_redirect) == 1,
                    )
                else:
                    user_messages.low_println(
                        f"[X11] Mapping unviewable window {mapped_window_id}: "
                        f"{window_attributes.contents.map_state}."
                    )
                    return
                data.clib.force_free(window_attributes)
        if win is None:
            win = old_win.copy_as_mapped_id(mapped_window_id)
        self.replace_native_id(old_win, win)
        user_messages.low_println(
            f"[X11] map request for old {owner_window_id} new {mapped_window_id}"
        )
        return self._internal_map_window(mapped_window_id, win)

    def _internal_map_window(
            self, mapped_window_id: libxcb_types.XcbWindow, win: X11WindowHandler,
    ) -> Optional[bool]:
        data = _req(self.__data)

        if win.override_redirect:
            # Don't do anything with this window.
            # user_messages.report_send_receive_problems(win.send_state(data.window_manager_data))
            # data.xcb.xcb_map_window(data.connection, owner_window_id)
            user_messages.low_println("[X11] override redirect window; will not manage")
            return True

        # Request to load settings.

        # Atoms to look at getting:
        #  _NET_WM_WINDOW_TYPE
        #  _NET_WM_STRUT_PARTIAL
        #  _NET_WM_STATE
        #  _NET_WM_NAME (title)
        #  WM_CLIENT_LEADER
        #  XCB_ATOM_WM_TRANSIENT_FOR
        #  XCB_ATOM_WM_NAME
        #  XCB_ATOM_WM_CLASS
        #  WM_WINDOW_ROLE
        #  xcb_icccm_get_wm_hints()
        #  xcb_icccm_get_wm_normal_hints()
        #  _MOTIF_WM_HINTS
        #  _NET_WM_USER_TIME
        #  _NET_WM_DESKTOP
        #  XCB_ATOM_WM_CLIENT_MACHINE
        #  _NET_WM_ICON

        # NET_WM_STATE xcb_reply_contains_atom:
        #  _NET_WM_STATE_FULLSCREEN
        #  _NET_WM_WINDOW_TYPE_DOCK
        #  _NET_WM_STATE_MODAL
        #  _NET_WM_STATE_STICKY

        # _NET_WM_WINDOW_TYPE xcb_reply_contains_atom:
        #  _NET_WM_WINDOW_TYPE_DIALOG
        #  _NET_WM_WINDOW_TYPE_UTILITY
        #  _NET_WM_WINDOW_TYPE_TOOLBAR
        #  _NET_WM_WINDOW_TYPE_SPLASH

        # Get the startup id
        print("1")
        startup_id_cookie = data.xcb.xcb_get_property(
            data.connection,
            ctypes.c_uint8(0),  # delete
            mapped_window_id,  # requested window
            data.atoms.NET_STARTUP_ID,  # property
            libxcb_consts.XCB_GET_PROPERTY_TYPE_ANY,  # property type
            ctypes.c_uint32(0),  # offset
            libxcb_consts.UINT_MAX__c,  # length
        )
        geom_cookie = data.xcb.xcb_get_geometry(data.connection, mapped_window_id)

        # Ensure the window is automatically mapped in case we crash
        print("2")
        data.xcb.xcb_change_save_set(
            data.connection, libxcb_consts.XCB_SET_MODE_INSERT__c, mapped_window_id,
        )
        # TODO add in shapes extension
        # if data.window_manager_data.libs.has_xcb_shapes():
        #     data.window_manager_data.libs.shapes.xcb_shape_select_input(
        #         data.connection, mapped_window_id, 1,
        #     )

        # Create frame window to put the mapped window into.
        print("3")
        frame_id = data.xcb.xcb_generate_id(data.connection)
        print("4")
        res = win.set_frame_window(frame_id)
        if not res:
            user_messages.low_println("[X11] - failed to set the frame window.  Aborting manage.")
            user_messages.report_send_receive_problems(res)
            data.event_loop.ignore_event(startup_id_cookie.sequence, -1)
            data.event_loop.ignore_event(geom_cookie.sequence, -1)
            return False
        print('5')
        # Don't believe the original window size requests; it's usually wrong.
        geom = data.xcb.xcb_get_geometry_reply(
            data.connection, geom_cookie, libxcb_consts.NULL__XcbGenericErrorPP,
        )
        if geom:
            geom_data = geom.contents
            win.update_from_explicit(
                from_x=True,
                pos_x=geom_data.x, pos_y=geom_data.y,
                width=geom_data.width, height=geom_data.height,
                border_width=geom_data.border_width,
            )
            data.clib.force_free(geom)

        data.xcb.xcb_create_window(
            data.connection,
            data.default_depth_raw,
            frame_id,
            data.screen_root,
            ctypes.c_int16(win.state.location.x),
            ctypes.c_int16(win.state.location.y),
            ctypes.c_uint16(win.state.location.width),
            ctypes.c_uint16(win.state.location.height),
            ctypes.c_uint16(win.get_border_width()),
            libxcb_consts.XCB_COPY_FROM_PARENT__c,
            data.visual_id,

            # Value Mask
            ctypes.c_int32(
                libxcb_consts.XCB_CW_BORDER_PIXEL
                | libxcb_consts.XCB_CW_BIT_GRAVITY
                | libxcb_consts.XCB_CW_WIN_GRAVITY
                | libxcb_consts.XCB_CW_OVERRIDE_REDIRECT
                | libxcb_consts.XCB_CW_EVENT_MASK
                | libxcb_consts.XCB_CW_COLORMAP
            ),

            # Values
            ct_util.as_int32_list(
                data.screen.contents.black_pixel,
                libxcb_consts.XCB_GRAVITY_NORTH_WEST__c,
                libxcb_consts.XCB_GRAVITY_NORTH_WEST__c,
                ctypes.c_int32(1),

                # register for key events on F and event window.
                ctypes.c_int32(
                    libxcb_consts.XCB_EVENT_MASK_STRUCTURE_NOTIFY
                    | libxcb_consts.XCB_EVENT_MASK_ENTER_WINDOW
                    | libxcb_consts.XCB_EVENT_MASK_LEAVE_WINDOW
                    | libxcb_consts.XCB_EVENT_MASK_EXPOSURE
                    | libxcb_consts.XCB_EVENT_MASK_SUBSTRUCTURE_REDIRECT
                    | libxcb_consts.XCB_EVENT_MASK_POINTER_MOTION
                    | libxcb_consts.XCB_EVENT_MASK_BUTTON_PRESS
                    | libxcb_consts.XCB_EVENT_MASK_BUTTON_RELEASE
                ),
                ctypes.c_int32(data.default_colormap),
            ),
        )
        print(f"6 - frame {frame_id}")

        # ... ensure we don't lose any events.
        data.xcb.xcb_grab_server(data.connection)
        try:
            # Ensure an unmap notify isn't sent back to the event loop due to a reparent call.
            print("7")
            data.xcb.xcb_change_window_attributes(
                data.connection,
                data.screen_root,
                libxcb_consts.XCB_CW_EVENT_MASK__c,
                ct_util.as_uint32_list(ctypes.c_uint32(0)),
            )
            # make event window a child of F with reparent window
            print("8")
            reparent_cookie = data.xcb.xcb_reparent_window(
                data.connection,
                mapped_window_id,
                frame_id,
                ctypes.c_int16(0), ctypes.c_int16(0),  # relative x,y position in the frame.
            )

            # render F and event window with map_window
            print("9")
            # data.xcb.xcb_map_window(data.connection, mapped_window_id)
            data.xcb.xcb_map_window(data.connection, frame_id)
            win.mapped = True

            # Bring back normal event handling to the window.
            print("10")
            data.xcb.xcb_change_window_attributes(
                data.connection,
                data.screen_root,
                libxcb_consts.XCB_CW_EVENT_MASK__c,
                ct_util.as_uint32_list(ROOT_WINDOW_EVENT_MASK__c),
            )
        finally:
            print("11")
            data.xcb.xcb_ungrab_server(data.connection)

        # Perform another window attribute change so that we don't receive false
        #   events from the above actions.
        print("12")
        data.xcb.xcb_change_window_attributes(
            data.connection, mapped_window_id,
            libxcb_consts.XCB_CW_EVENT_MASK__c,
            ct_util.as_uint32_list(CLIENT_WINDOW_EVENT_MASK__c),
        )

        # Ensure the client doesn't get the border.
        print("13")
        data.xcb.xcb_change_window_attributes(
            data.connection, mapped_window_id,
            libxcb_consts.XCB_CONFIG_WINDOW_BORDER_WIDTH__c,
            ct_util.as_uint32_list(ctypes.c_uint32(0)),  # 0 border width
        )

        # Prevent a tiny flicker by putting this window on the bottom of the stack.
        print("14")
        data.xcb.xcb_change_window_attributes(
            data.connection, mapped_window_id,
            libxcb_consts.XCB_CONFIG_WINDOW_STACK_MODE__c,
            ct_util.as_uint32_list(libxcb_consts.XCB_STACK_MODE_BELOW__c),
        )

        # Put the window in normal state with XCB_ICCCM_WM_STATE_NORMAL.
        # Check clients hints with ewmh.

        # Response checking.
        print("15")
        startup_reply = data.xcb.xcb_get_property_reply(
            data.connection, startup_id_cookie, libxcb_consts.NULL__XcbGenericErrorPP,
        )
        print("16")
        startup_id = data.get_reply_text(startup_reply)
        print(f"17 - {startup_id}")
        data.clib.force_free(startup_reply)

        # if startup_id is none, and WM_CLIENT_LEADER is valid for the window,
        #   then use the startup id for the WM_CLIENT_LEADER window.

        user_messages.low_println(
            f"[X11] new window {win.window_id} has startup [{startup_id}]"
        )

        err = data.xcb.xcb_request_check(data.connection, reparent_cookie)
        if err:
            res = StdRet.pass_errmsg(
                user_messages.TRANSLATION_CATALOG,
                _('Failed to reparent window {window}: response type {error}'),
                window=repr(mapped_window_id),
                error=repr(err.contents.response_type),
            )
            logging.send_system_error(
                context=data.context, source_id=win.window_id,
                system_error=res.valid_error,
                identifier='client-window-reparent',
                categories='os',
            )
            self.window_destroyed(mapped_window_id, 'Failed during setup')
            return False

        print("18")
        user_messages.report_send_receive_problems(win.send_state(data.window_manager_data))
        print("19 - all done")
        return True

    # UnmapEventCallback
    def _x11_unmap_event(self, event: libxcb_types.XcbUnmapNotifyEventP) -> Optional[bool]:
        # Window is now invisible.
        event_data = event.contents
        event_win_id = event_data.event
        win_id = event_data.window
        win = self.get_window_by_native(win_id)
        if not win:
            win = self.get_window_by_native(event_win_id)
            if not win:
                self._on_missing_window('unmap-event', win_id)
                return False
        win.mapped = False
        data = self.__data

        # Close the frame.
        if data and data.connection:
            data.xcb.xcb_unmap_window(data.connection, win.native_id)
            data.xcb.xcb_reparent_window(
                data.connection, win.native_id, data.screen_root,
                ctypes.c_int16(0), ctypes.c_int16(0),
            )
            # Should wait until reparent completes?
            if win.frame_window_id:
                data.xcb.xcb_destroy_window(data.connection, win.frame_window_id)
                win.removed_frame()
        user_messages.low_println(f"[X11] unmap window {win_id} child {event.contents.window}")
        # TODO update state to make it look minimized.
        user_messages.report_send_receive_problems(self.update_window_state(win))
        return True

    # MotionEventCallback
    def _x11_motion_event(self, event: libxcb_types.XcbMotionNotifyEventP) -> Optional[bool]:
        pass

    # EnterEventCallback
    def _x11_enter_event(self, event: libxcb_types.XcbEnterNotifyEventP) -> Optional[bool]:
        pass

    # LeaveEventCallback
    def _x11_leave_event(self, event: libxcb_types.XcbLeaveNotifyEventP) -> Optional[bool]:
        pass

    # FocusInEventCallback
    def _x11_focusin_event(self, event: libxcb_types.XcbFocusInEventP) -> Optional[bool]:
        pass

    # FocusOutEventCallback
    def _x11_focusout_event(self, event: libxcb_types.XcbFocusOutEventP) -> Optional[bool]:
        pass

    # WinCreateEventCallback
    def _x11_create_event(self, event_p: libxcb_types.XcbCreateNotifyEventP) -> Optional[bool]:
        # A window was just created by the client.
        #   As a notify event, it means that the window manager is just told of this
        #   happening.  We need to set up our data structures to handle this window
        #   in the future.
        event_data = event_p.contents
        data = self.__data
        if not data:
            user_messages.low_println(
                f"[X11] failed to created window {event_data.window} - not initialized"
            )
            return False

        native_id = event_data.window
        pos_x = event_data.x
        pos_y = event_data.y
        width = event_data.width
        height = event_data.height
        border_width = event_data.border_width
        # Window managers should ignore this window if override_redirect is 1.
        override_redirect = ct_util.as_py_int(event_data.override_redirect) == 1
        print(
            f"[X11] X11 window create event: {native_id} to "
            f"({pos_x}, {pos_y}) sized ({width}, {height}) border {border_width}"
        )
        self._internal_create_window(
            native_id=native_id, pos_x=pos_x, pos_y=pos_y, width=width, height=height,
            border_width=border_width, override_redirect=override_redirect,
        )

    def _internal_create_window(
            self,
            native_id: libxcb_types.XcbWindow,
            pos_x: ctypes.c_int32, pos_y: ctypes.c_int32,
            width: ctypes.c_uint32, height: ctypes.c_uint32,
            border_width: ctypes.c_uint32, override_redirect: bool,
    ) -> Optional[bool]:
        user_messages.low_println(
            f"[X11] created window {native_id} with override {override_redirect} border {border_width}"
        )
        win = X11WindowHandler(
            window_id=self.create_next_window_id(),
            wid=native_id,
            state=window.create_window_state(
                is_active=True, has_focus=0, parent_id=None,
                location=ScreenRect.from_xywh(
                    pos_x=ct_util.as_py_int(pos_x),
                    pos_y=ct_util.as_py_int(pos_y),
                    width=ct_util.as_py_int(width),
                    height=ct_util.as_py_int(height),
                ),
                minimized=True,

                # These may be from other events...
                resizable=True,
                full_screen=False,
                meta={
                    WINDOW_SETTING__METRICS_BORDER_WIDTH:
                        str(ct_util.as_py_int(border_width)),
                },
                meta_description=WINDOW_META_STYLES,
            ),
            border=ct_util.as_py_int(border_width),
            override_redirect=override_redirect,
        )

        # Put this window into the internal data structures, and send
        #   Petronia events notifying of this change.
        user_messages.report_send_receive_problems(self.window_created(
            window=win,
            delay_send_active_ids=False,
        ))
        return True

    # WinDestroyEventCallback
    def _x11_destroy_event(self, event: libxcb_types.XcbDestroyNotifyEventP) -> Optional[bool]:
        # The client tells us the window is destroyed.
        #   As a notify event, this is letting the window manager know that the
        #   action occurred, and all we can do is update our internal data structures
        #   to reflect this state.
        event_data = event.contents
        event_win_id = event_data.event
        win_id = event_data.window
        win = self.get_window_by_native(win_id)
        if not win:
            win = self.get_window_by_native(event_win_id)
            if not win:
                self._on_missing_window('destroy-event', win_id)
                return False
        user_messages.report_send_receive_problems(self.window_destroyed(
            native_id=win.native_id,
            reason='destroyed',
        ))

        win.mapped = False
        data = self.__data

        # Close the frame.
        if data and data.connection:
            if win.frame_window_id:
                data.xcb.xcb_destroy_window(data.connection, win.frame_window_id)
                win.removed_frame()
        user_messages.low_println(f"[X11] deleted window {win_id}")
        return False


def _get_int(value: Optional[str], default: int) -> int:
    if value:
        try:
            return int(value)
        except ValueError:
            pass
    return default


def _req(value: Optional[V]) -> V:
    if value is None:
        raise ValueError('value is None')
    return value


def _on_not_set_up() -> StdRet[V]:
    """Returns an error when the data object or some aspect of it is not available."""
    return StdRet.pass_errmsg(
        user_messages.TRANSLATION_CATALOG,
        _('Window hook disconnected'),
    )


def _hashable_native_id(wid: libxcb_types.XcbWindow) -> Hashable:
    return ct_util.as_py_int(wid)


def window_factory(libs: Libraries) -> StdRet[Union[Hook, UserMessage]]:
    """Set up the events."""
    hook = WindowHook()
    hook.register_listeners(libs.context, EXTENSION_NAME)

    return StdRet.pass_ok(hook)
