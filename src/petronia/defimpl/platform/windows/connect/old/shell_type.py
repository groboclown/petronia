
from ..arch.windows_constants import PETRONIA_CREATED_WINDOW__CLASS_PREFIX
from ..arch.funcs import (
    window__find_handles, window__get_style, window__set_style, window__border_rectangle,
    window__redraw, window__get_process_id, process__get_username_domain_for_pid,
    window__get_module_filename, process__get_executable_filename,
    window__get_class_name, window__is_visible, window__set_position,
    window__activate, window__get_title, window__get_visibility_states,
    window__get_active_window, window__maximize, window__minimize, window__move_resize,
    process__get_current_pid, process__get_username_domain_for_pid,
    shell__set_window_metrics
)
import atexit


class ShellType(Identifiable, Component):
    """
    Defines the basic interaction between the Petronia event system and the
    OS-level shell application.
    """
    def __init__(self, bus, config):
        Component.__init__(self, bus)
        Identifiable.__init__(self, target_ids.SHELL)
        assert isinstance(config, Config)
        self._config = config

        self._listen(event_ids.TELL_WINDOWS__OPEN_START_MENU, target_ids.ANY, self._on_open_start_menu)
        self._listen(event_ids.TELL_WINDOWS__LOCK_SCREEN, target_ids.ANY, self._on_lock_screen)

    # noinspection PyUnusedLocal,PyMethodMayBeStatic
    def _on_open_start_menu(self, event_id, target_id, event_obj):
        raise NotImplementedError()

    # noinspection PyUnusedLocal,PyMethodMayBeStatic
    def _on_lock_screen(self, event_id, target_id, event_obj):
        raise NotImplementedError()
