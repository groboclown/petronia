
"""
Ties the native OS window handle (hwnd) to an internal ID.
Also keeps track of the window information.

This needs to be one of the last components created, because it
sends out events at creation time that other components will want.
"""

from ...system import event_ids
from ...system import target_ids
from ...system.component import Component, Identifiable
from ...system.id_manager import IdManager
from ...config import Config
from ...arch.funcs import (
    window__find_handles, window__get_style, window__set_style, window__border_rectangle,
    window__redraw, window__get_process_id, process__get_username_domain_for_pid,
    window__get_module_filename, process__get_executable_filename,
    window__get_class_name, window__is_visible, window__set_position,
    window__activate, window__get_title, window__get_visibility_states,
    window__get_active_window, window__maximize, window__minimize,
    process__get_current_pid, process__get_username_domain_for_pid,
    shell__set_window_metrics
)
import atexit

_CURRENT_PROCESS_ID = process__get_current_pid()
_CURRENT_USER_DOMAIN = process__get_username_domain_for_pid(_CURRENT_PROCESS_ID)


class WindowMapper(Identifiable, Component):
    def __init__(self, bus, id_manager, config):
        Component.__init__(self, bus)
        Identifiable.__init__(self, target_ids.WINDOW_MAPPER)
        assert isinstance(id_manager, IdManager)
        assert isinstance(config, Config)
        self.__id_manager = id_manager
        self.__config = config

        # Pre-populate existing windows

        hwnd_list = window__find_handles()
        self.__handle_map = {}
        self.__cid_to_handle = {}
        self.__hwnd_restore_state = {}
        for hwnd in hwnd_list:
            try:
                self._init_window(hwnd)
            except BaseException as e:
                self._log_error("WindowMapper failed to initialize window {0}".format(hwnd), e)
        self._log_verbose("===== Finished existing window registration =====")

        self._listen(event_ids.OS__WINDOW_CREATED, target_ids.ANY, self._on_window_created)
        self._listen(event_ids.OS__WINDOW_DESTROYED, target_ids.ANY, self._on_window_destroyed)
        self._listen(event_ids.OS__WINDOW_FOCUSED, target_ids.ANY, self._on_window_focused)
        # self._listen(event_ids.OS__SHELL_WINDOW_FOCUSED, target_ids.ANY, None)
        self._listen(event_ids.OS__WINDOW_MINIMIZED, target_ids.ANY, self._on_window_minimized)
        self._listen(event_ids.OS__WINDOW_REDRAW, target_ids.ANY, self._on_window_redraw)
        # self._listen(event_ids.OS__TASK_MANAGER_FOCUSED, target_ids.ANY, None)
        # self._listen(event_ids.OS__LANGUAGE, target_ids.ANY, None)
        # self._listen(event_ids.OS__SYS_MENU, target_ids.ANY, None)
        self._listen(event_ids.OS__WINDOW_FORCED_END, target_ids.ANY, self._on_window_forced_end)

        # These two occur when a window comes back from being hung
        self._listen(event_ids.OS__WINDOW_REPLACING, target_ids.ANY, self._on_window_replacing)
        self._listen(event_ids.OS__WINDOW_REPLACED, target_ids.ANY, self._on_window_replaced)

        # self._listen(event_ids.OS__WINDOW_MONITOR_CHANGED, target_ids.ANY, None)
        self._listen(event_ids.OS__WINDOW_FLASH, target_ids.ANY, self._on_window_flash)
        # self._listen(event_ids.OS__APP_COMMAND, target_ids.ANY, None)

        # Events from the system that request OS actions.
        self._listen(event_ids.LAYOUT__SET_RECTANGLE, target_ids.ANY, self._on_window_move_resize)
        self._listen(event_ids.TELL_WINDOWS__FOCUS_WINDOW, target_ids.ANY, self._on_set_window_focus)
        self._listen(event_ids.ZORDER__SET_WINDOW_ON_TOP, target_ids.ANY, self._on_set_window_top)
        self._listen(event_ids.TELL_WINDOWS__MINIMIZE_WINDOW, target_ids.ANY, self._on_minimize_window)
        self._listen(event_ids.TELL_WINDOWS__MAXIMIZE_WINDOW, target_ids.ANY, self._on_maximize_window)

        # Requests that require knowing OS states of windows
        self._listen(event_ids.FOCUS__MAKE_OWNED_PORTAL_ACTIVE, target_ids.WINDOW_MAPPER,
                     self._on_make_owned_portal_active)

        self._listen(event_ids.LAYOUT__RESEND_WINDOW_CREATED_EVENTS, target_ids.ANY,
                     self._on_resend_window_created_events)

        # Setup Chrome
        shell__set_window_metrics(config.chrome.get_system_window_settings())

    def close(self):
        try:
            for hwnd, state in self.__hwnd_restore_state.items():
                _restore_window_state(hwnd, state[0], state[1])
        finally:
            super().close()

    def _setup_window_style(self, info):
        if 'title' not in info:
            info['title'] = window__get_title(info['hwnd'])
        if info['visible'] and self.__config.applications.is_managed_chrome(info):
            hwnd = info['hwnd']
            orig_size = window__border_rectangle(hwnd)
            orig_style = window__get_style(hwnd)
            self.__hwnd_restore_state[hwnd] = (orig_size, orig_style)
            # Always, always restore window state at exit.  This ensures it.
            atexit.register(_restore_window_state, hwnd, orig_size, orig_style)
            style_data = {}
            if self.__config.chrome.remove_decoration:
                style_data['border'] = False
                style_data['dialog-frame'] = False
            if self.__config.chrome.remove_resize_border:
                style_data['size-border'] = False
            if len(style_data) > 0:
                try:
                    window__set_style(hwnd, style_data)
                except OSError as e:
                    self._log_debug("Problem setting style for {0}".format(info['class']), e)
                window__redraw(hwnd)

    def _init_window(self, hwnd):
        pid = window__get_process_id(hwnd)
        if _CURRENT_PROCESS_ID == pid:
            return None
        try:
            username_domain = process__get_username_domain_for_pid(pid)
            self._log_debug("window {0}, pid {1}, owned by [{2}@{3}]".format(
                hwnd, pid, username_domain[0], username_domain[1]))
        except OSError as e:
            # Most probably an access problem.  We don't want to manage programs
            # that we can't access.
            self._log_debug("username/domain problem; ignoring window {0}, pid {1}".format(hwnd, pid), e)
            return None
        # TODO only manage windows that the user owns.
        # At the moment, the username_domain call returns empty strings.  This is
        # probably a bug in the underlying winapi calls.
        # if username_domain != _CURRENT_USER_DOMAIN:
        #     print(" - ignoring {0} from other user {1}@{2}".format(pid, username_domain[0], username_domain[1]))
        cid = self.__id_manager.allocate('hwnd')
        key = str(hwnd)
        module_filename = ""
        try:
            module_filename = window__get_module_filename(hwnd)
        except OSError as e:
            self._log_debug("Ignoring problem from window__get_module_filename", e)
        exec_filename = ""
        try:
            exec_filename = process__get_executable_filename(pid)
        except OSError as e:
            self._log_debug("Ignoring problem from process__get_executable_filename", e)
        visible = window__is_visible(hwnd)
        if visible:
            info = {
                'cid': cid,
                'hwnd': hwnd,
                'class': window__get_class_name(hwnd),
                'module_filename': module_filename,
                'exec_filename': exec_filename,
                'pid': pid,
                'visible': visible,
            }
            self._setup_window_style(info)
            self.__handle_map[key] = info
            self.__cid_to_handle[cid] = hwnd
            self._log_debug("Registered {0} ({1}) ({2}) ({3}) as {4}".format(
                hex(hwnd), module_filename, exec_filename, pid, cid))
            if self.__config.applications.is_tiled(info):
                self._fire_for_window(event_ids.WINDOW__CREATED, info)
            return info
        return None

    # noinspection PyUnusedLocal
    def _on_window_created(self, event_id, target_id, obj):
        hwnd = obj['target_hwnd']
        self._init_window(hwnd)

    # noinspection PyUnusedLocal
    def _on_window_destroyed(self, event_id, target_id, obj):
        hwnd = obj['target_hwnd']
        key = str(hwnd)
        # No need to check if the window is registered
        if key in self.__handle_map:
            info = self.__handle_map[key]
            self._fire_for_window(event_ids.WINDOW__CLOSED, info)
            del self.__handle_map[key]
            del self.__cid_to_handle[info['cid']]
            if hwnd in self.__hwnd_restore_state:
                # FIXME this handle is different types depending on the call.
                # Need to unify these correctly, so we don't have this "if" statement.
                del self.__hwnd_restore_state[hwnd]

    # noinspection PyUnusedLocal
    def _on_window_focused(self, event_id, target_id, obj):
        if 'target_hwnd' in obj:
            hwnd = obj['target_hwnd']
        elif 'source_hwnd' in obj:
            # TODO this should be handled better in the generating event.
            hwnd = obj['source_hwnd']
        else:
            return
        key = str(hwnd)
        if key in self.__handle_map:
            info = self.__handle_map[key]
            self._fire_for_window(event_ids.WINDOW__FOCUSED, info)

    # noinspection PyUnusedLocal
    def _on_window_minimized(self, event_id, target_id, obj):
        hwnd = obj['target_hwnd']
        key = str(hwnd)
        if key in self.__handle_map:
            info = self.__handle_map[key]
            # TODO do something

    # noinspection PyUnusedLocal
    def _on_window_redraw(self, event_id, target_id, obj):
        hwnd = obj['target_hwnd']
        key = str(hwnd)
        if key in self.__handle_map:
            info = self.__handle_map[key]
            self._fire_for_window(event_ids.WINDOW__REDRAW, info)

    # noinspection PyUnusedLocal
    def _on_window_forced_end(self, event_id, target_id, obj):
        hwnd = obj['target_hwnd']
        key = str(hwnd)
        if key in self.__handle_map:
            info = self.__handle_map[key]
            # TODO do something

    # noinspection PyUnusedLocal
    def _on_window_replacing(self, event_id, target_id, obj):
        hwnd = obj['target_hwnd']
        key = str(hwnd)
        if key in self.__handle_map:
            info = self.__handle_map[key]
            # TODO do something

    # noinspection PyUnusedLocal
    def _on_window_replaced(self, event_id, target_id, obj):
        hwnd = obj['target_hwnd']
        key = str(hwnd)
        if key in self.__handle_map:
            info = self.__handle_map[key]
            # TODO do something

    # noinspection PyUnusedLocal
    def _on_window_flash(self, event_id, target_id, obj):
        hwnd = obj['target_hwnd']
        key = str(hwnd)
        if key in self.__handle_map:
            info = self.__handle_map[key]
            self._fire_for_window(event_ids.WINDOW__FLASHING, info)

    # noinspection PyUnusedLocal
    def _on_window_move_resize(self, event_id, target_id, obj):
        if target_id in self.__cid_to_handle:
            hwnd = self.__cid_to_handle[target_id]
            if 'x' in obj and 'y' in obj and 'height' in obj and 'width' in obj:
                # print("DEBUG setting window {0} to ({1}, {2}) @ ({3}, {4})  {5}".format(
                #     target_id, obj['width'], obj['height'], obj['x'], obj['y'], obj
                # ))
                window__set_position(
                    hwnd, None, obj['x'], obj['y'], obj['width'], obj['height'],
                    ['frame-changed', 'draw-frame', 'async-window-pos']
                )
            if 'make-focused' in obj:
                window__activate(hwnd)

    # noinspection PyUnusedLocal
    def _on_set_window_focus(self, event_id, target_id, obj):
        if target_id in self.__cid_to_handle:
            hwnd = self.__cid_to_handle[target_id]
            window__activate(hwnd)

    # noinspection PyUnusedLocal
    def _on_set_window_top(self, event_id, target_id, obj):
        if target_id in self.__cid_to_handle:
            hwnd = self.__cid_to_handle[target_id]
            position = window__border_rectangle(hwnd)
            window__set_position(
                hwnd, ["top"],
                position['x'], position['y'], position['width'], position['height'],
                ["show-window"])

    # noinspection PyUnusedLocal
    def _on_maximize_window(self, event_id, target_id, obj):
        if target_id in self.__cid_to_handle:
            hwnd = self.__cid_to_handle[target_id]
        else:
            hwnd = window__get_active_window()

        if hwnd:
            window__maximize(hwnd)

    # noinspection PyUnusedLocal
    def _on_minimize_window(self, event_id, target_id, obj):
        if target_id in self.__cid_to_handle:
            print("Using a known window handle")
            hwnd = self.__cid_to_handle[target_id]
        else:
            print("getting the active window handle")
            hwnd = window__get_active_window()

        if hwnd is not None:
            # print("DEBUG minimizing handle " + hwnd)
            window__minimize(hwnd)
        # else:
        #     print("DEBUG nothing to minimize")

    # noinspection PyUnusedLocal
    def _on_make_owned_portal_active(self, event_id, target_id, obj):
        focused_window_hwnd = window__get_active_window()
        key = str(focused_window_hwnd)
        if key in self.__handle_map:
            info = self.__handle_map[key]
            # By sending the window__focused event for the window cid, the owned
            # portal activates itself
            self._fire_for_window(event_ids.WINDOW__FOCUSED, info)
        else:
            self._log_warn("Could not find window CID that is active; handle is {0}".format(key))

    # noinspection PyUnusedLocal
    def _on_resend_window_created_events(self, event_id, target_id, obj):
        for info in self.__handle_map.values():
            if self.__config.applications.is_tiled(info):
                self._fire_for_window(event_ids.WINDOW__CREATED, info)

    def _fire_for_window(self, event_id, info):
        # Only fire for visible windows
        if info['visible']:
            hwnd = info['hwnd']
            full_info = {
                # Some things we load every time.
                'cid': info['cid'],
                'title': window__get_title(hwnd),
                'border': window__border_rectangle(hwnd),
                'visibility': window__get_visibility_states(hwnd),

                # Others are static
                'hwnd': hwnd,
                'class': info['class'],
                'module_filename': info['module_filename'],
                'exec_filename': info['exec_filename'],
                'pid': info['pid'],
                'visible': info['visible'],
            }
            self._fire(event_id, info['cid'], {
                'window-cid': info['cid'],
                'window-info': full_info,
            })


def _restore_window_state(hwnd, size, style):
    try:
        window__set_style(hwnd, style)
    except OSError:
        pass

    # Set position to redraw the window AFTER setting the style.
    try:
        window__set_position(
            hwnd, None, size['x'], size['y'], size['width'], size['height'],
            ["frame-changed", "no-zorder", "async-window-pos"])
    except OSError:
        pass
