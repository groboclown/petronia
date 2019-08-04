
"""
Unit tests for the extension loader.
"""

import unittest
# from petronia3.system.bus import EventBus
from petronia3.extensions.extensions.api import (
    ExtensionState,
    ANY_VERSION,
)
from petronia3.system.logging import ERROR
from petronia3_root.util.test_helper import BasicQueuer, EnabledLogs
from petronia3_root.bootstrap.bus import bootstrap_event_bus
from ..defs import LoadedExtension
from ..loaders.core import CoreExtensionLoader
from ..loaders.composite import CompositeExtensionLoader
from ..ext_loader import (
    load_additional_extension, load_extensions
)
from .mocks import (
    mk_disc,
    MockLoader,
)


class ExtensionManagerTest(unittest.TestCase):
    def test_load_additional_core(self):
        """Test loading a core module."""
        queuer = BasicQueuer(self)
        bus = bootstrap_event_bus(queuer.pure_queuer)

        ext1 = LoadedExtension('x', True, (1, 0, 0,))
        disc1 = mk_disc('x', (True, ext1.version), [])
        disc2 = mk_disc('y', (False, (1, 2, 3,),), [])
        loader1 = MockLoader(disc1, disc2)
        loader2 = CoreExtensionLoader()
        loader = CompositeExtensionLoader([loader1, loader2])
        with EnabledLogs(ERROR):
            new_state = load_additional_extension(
                'core.timer.api',
                loader, bus, [ext1])

        # 'x' is considered an already-loaded extension, so it is
        # not returned by the load call.
        self.assertEqual(
            list(new_state),
            [LoadedExtension('core.timer.api', True, ANY_VERSION)]
        )
