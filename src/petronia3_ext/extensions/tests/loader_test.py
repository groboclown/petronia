
"""
Unit tests for the extension loader.
"""

import unittest
# from petronia3.system.bus import EventBus
from petronia3.extensions.extensions import ExtensionState, ExtensionConfiguration
from petronia3.util.tests.test_helper import BasicQueuer, EnabledLogs
from petronia3_root.bootstrap.core import create_core_system
from ..loader import load_extension


class ExtensionManagerTest(unittest.TestCase):
    def test_load_core(self):
        """Test loading a core module."""
        queuer = BasicQueuer(self)
        bus = create_core_system(queuer.pure_queuer)
        orig_state = ExtensionState(['x'])
        config = ExtensionConfiguration()
        with EnabledLogs():
            new_state = load_extension('core.timer', bus, config, orig_state)
        self.assertEqual(
            new_state.loaded_extensions,
            ('x', 'core.timer',)
        )
