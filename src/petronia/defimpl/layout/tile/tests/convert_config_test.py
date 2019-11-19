
"""

"""

import unittest
from .....core.platform.api import (
    VirtualScreenInfo,
    VirtualScreenArea,
)
from ..config import (
    TileLayoutConfig,
    RootTileLayout,
    ScreenTileLayout,
    SplitTileLayout,
    PortalLayout,
)
from ..convert_config import (
    convert_config,
)
from ..splitter import (
    SPLIT_VERTICAL,
    SPLIT_HORIZONTAL,
    SplitterTile,
)
from ..portal import (
    Portal,
    POSITION_FAVOR_FILL,
    POSITION_FAVOR_RESTRICTED_NE,
    POSITION_FAVOR_RESTRICTED_NW,
)


class ConvertConfigTest(unittest.TestCase):
    def test_convert_basic_split_layout(self):
        config = TileLayoutConfig([RootTileLayout('', [ScreenTileLayout(None, SPLIT_HORIZONTAL, False, (0, 0,), [
            PortalLayout(None, 2, 'fill'),
            SplitTileLayout(None, 1, [
                PortalLayout(None, 3, 'r-ne'),
                PortalLayout(None, 2, 'r-nw'),
            ], True),
        ])])], [])

        parsed, primary_index, errs = convert_config(config, ONE_SCREEN)
        self.assertEqual(list(errs), [])
        # print("Converted to {0}".format(parsed))
        self.assertEqual(primary_index, 0)
        self.assertEqual(parsed.count(), 1)
        root = parsed.get_child(0)
        self.assertIsInstance(root, SplitterTile)
        self.assertEqual(root.count(), 2)
        primary = root.get_child(0)
        split = root.get_child(1)
        if isinstance(split, Portal):
            # The ordering doesn't matter.
            t = primary
            primary = split
            split = t
        self.assertIsInstance(primary, Portal)
        self.assertEqual(primary.get_area(), (0, 0, 682, 768))
        self.assertEqual(primary.get_name(), '0')
        self.assertEqual(primary.default_position, POSITION_FAVOR_FILL)

        self.assertIsInstance(split, SplitterTile)
        # +1 due to remainder
        self.assertEqual(split.get_area(), (682, 0, 342, 768))
        self.assertEqual(split.count(), 2)
        ch1 = split[0]
        ch2 = split.get_child(1)
        self.assertNotEqual(ch1, ch2)
        self.assertIsInstance(ch1, Portal)
        self.assertIsInstance(ch2, Portal)
        self.assertEqual(ch1.get_area(), (682, 0, 342, 459))
        self.assertEqual(ch1.default_position, POSITION_FAVOR_RESTRICTED_NE)
        # +3 due to remainder: 459 + 309 = 768.
        self.assertEqual(ch2.get_area(), (682, 459, 342, 309))
        self.assertEqual(ch2.default_position, POSITION_FAVOR_RESTRICTED_NW)


ONE_SCREEN = VirtualScreenInfo([
    VirtualScreenArea("primary", (0, 0, 1024, 768), True),
])

TWO_SCREENS = VirtualScreenInfo([
    VirtualScreenArea("secondary", (0, 0, 768, 1024), True),
    VirtualScreenArea("primary", (768, -384, 1024, 768), True),
])
