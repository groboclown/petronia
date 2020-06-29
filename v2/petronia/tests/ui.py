
import sys
from petronia.util import worker_thread
from petronia.shell.native.gui_window import GuiWindow
from petronia import config

from petronia.system.bus import Bus
from petronia.system.id_manager import IdManager
from petronia.system.registrar import Registrar
from petronia.system.logger import Logger, LEVEL_DEBUG, LEVEL_VERBOSE, LEVEL_WARN
from petronia.shell.native.windows_hook_event import WindowsHookEvent
from petronia.shell.native.window_mapper import WindowMapper
from petronia.tests.bus_logger import log_events


class BgGuiWindow(GuiWindow):
    def _on_paint(self, hwnd, hdc, width, height):
        print("ON PAINT! {0} {1}".format(width, height))
        self._draw_rect(hdc, -1, -1, width + 2, height + 2, 0)


def setup():
    hotkeys = config.HotKeyConfig()
    hotkeys.parse_hotkey_mode_keys(
        config.DEFAULT_MODE,
        {
            "win+f4": ["quit"],
        }
    )

    my_config = config.Config(hotkeys=hotkeys)
    my_config.init_options['layout-name'] = None
    my_config.init_options['config-file'] = None
    my_config.init_options['log-level'] = LEVEL_VERBOSE
    # my_config.init_options['log-level'] = LEVEL_DEBUG

    bus = Bus()
    id_mgr = IdManager(bus)
    registrar = Registrar(bus, id_mgr, my_config)
    my_config.register_components(registrar)

    # Important: Mapper before Hook Event
    # WindowMapper(bus, id_mgr, config)

    # Important: Hook Event after Mapper
    WindowsHookEvent(bus, my_config)

    window = BgGuiWindow('gui window', bus, 'ChromeWindow', 'Chrome Window', {
        'width': 200, 'height': 200
    }, has_border=False)


if __name__ == '__main__':
    setup()

    sys.stdin.read(1)

    worker_thread.stop_all_threads()
    sys.exit(0)
