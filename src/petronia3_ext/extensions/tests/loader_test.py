
"""
Unit tests for the extension loader.
"""

import unittest
# from petronia3.system.bus import EventBus
from petronia3.extensions.extensions import ExtensionState
from petronia3_root.util.test_helper import BasicQueuer, EnabledLogs
from petronia3_root.bootstrap.core import create_core_system
from ..loaders.core import CoreExtensionLoader
from ..defs import LoadedExtension
from ..ext_loader import load_additional_extension, load_extensions


class ExtensionManagerTest(unittest.TestCase):
    def test_load_additional_core(self):
        """Test loading a core module."""
        queuer = BasicQueuer(self)
        bus = create_core_system(queuer.pure_queuer)
        ext1 = LoadedExtension('x', True, (1, 0, 0,))
        with EnabledLogs():
            loader = CoreExtensionLoader()
            new_state = load_additional_extension(
                'core.timer.api',
                loader, bus, [ext1])
        self.assertEqual(
            new_state,
            (ext1, LoadedExtension('core.timer.api', True, (1, 0, 0,)),)
        )
