
"""
Unit tests for the extension loader.
"""

import unittest
# from petronia3.system.bus import EventBus
from ....aid.simp import ERROR
from ....aid.bootstrap import ANY_VERSION
from ....aid.test_helper import BasicQueuer, EnabledLogs
from ....boot.bootstrap.bus import bootstrap_event_bus
from ....core.state.api.bootstrap import bootstrap_state_store_api
from ..defs import LoadedExtension
from ..loaders.core import CoreExtensionLoader
from ..loaders.composite import CompositeExtensionLoader
from ..ext_loader import (
    load_additional_extension
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
        # The extension loader sends out a state event, so that needs to be registered.
        bootstrap_state_store_api(bus)

        ext1 = LoadedExtension('x', True, (1, 0, 0,))
        disc1 = mk_disc('x', (True, ext1.version), [], stand_alone=True)
        disc2 = mk_disc('y', (False, (1, 2, 3,),), [], stand_alone=True)
        loader1 = MockLoader(disc1, disc2)
        loader2 = CoreExtensionLoader()
        loader = CompositeExtensionLoader([loader1, loader2])
        with EnabledLogs(ERROR):
            new_state = load_additional_extension(
                'core.timer.api',
                loader, bus, [ext1])

        # 'x' is considered an already-loaded extension, so it is
        # not returned by the load call.
        self.maxDiff = None
        self.assertEqual(len(new_state), 4)

        # These two must be added, but there is no reason to have one before
        # the other, so their ordering doesn't matter for these two items.
        # Therefore, to make the big assert equal to work, we'll force a
        # swap.
        if new_state[2].name == 'default.timer':
            tmp = new_state[2]
            new_state[2] = new_state[3]
            new_state[3] = tmp

        self.assertEqual(
            list(new_state),
            [
                LoadedExtension('core.timer.api', True, ANY_VERSION),

                # Timer declares a dependency on the shutdown API.
                LoadedExtension('core.shutdown.api', True, ANY_VERSION),

                # Extension loads the default implementations.
                # The order here doesn't matter.
                LoadedExtension('default.shutdown.timer', True, ANY_VERSION),
                LoadedExtension('default.timer', True, ANY_VERSION),
            ]
        )
