
from .shell_type import ShellType
from ...arch.funcs import (
    shell__open_start_menu, shell__lock_workstation,
    monitor__find_monitors, window__send_message,
    shell__get_task_bar_window_handles, window__border_rectangle,
)


class ShellExplorer(ShellType):
    """
    A component interface for the Windows shell.

    """
    def __init__(self, bus, config):
        ShellType.__init__(self, bus, config)

    # noinspection PyUnusedLocal,PyMethodMayBeStatic
    def _on_open_start_menu(self, event_id, target_id, event_obj):
        shell__open_start_menu(self._config.chrome.show_taskbar_with_start_menu)

    # noinspection PyUnusedLocal,PyMethodMayBeStatic
    def _on_lock_screen(self, event_id, target_id, event_obj):
        shell__lock_workstation()


def get_taskbar_position():
    hwnd_list = shell__get_task_bar_window_handles()
    for hwnd in hwnd_list:
        try:
            rect = window__border_rectangle(hwnd)
            if rect is not None:
                return rect
        except OSError:
            # Ignore
            pass
    return {'top': 0, 'left': 0, 'right': 0, 'bottom': 0, 'x': 0, 'y': 0, 'width': 0, 'height': 0}
