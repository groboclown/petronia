
# Usage: python3 -m unittest petronia.tests.layout_navigation

import unittest

from petronia.system.bus import SingleThreadedBus
from petronia.system.logger import Logger
from petronia.system.id_manager import IdManager
from petronia.system.registrar import Registrar
from petronia.system import event_ids, target_ids
from petronia import config
from petronia.shell.control.root_layout import RootLayout

from .bus_logger import log_events


class NavigationTests(unittest.TestCase):
    def test_root_init_state(self):
        root = RootLayout(self.bus, self.config, self.id_manager)
        self.bus.fire(event_ids.WINDOW__CREATED, root.cid, {
            'window-cid': 'window-0',
            'window-info': {
                'cid': 'window-0',
            }
        })

    def setUp(self):
        self.bus = SingleThreadedBus()
        self.id_manager = IdManager(self.bus)
        self.config = config.load_config()
        Registrar(self.bus, self.id_manager, self.config)
        Logger(self.bus)
        log_events(self.bus)

    def __init__(self, *args):
        super().__init__(*args)
        self.bus = None
        self.id_manager = None
        self.config = None


if __name__ == '__main__':
    unittest.main()
