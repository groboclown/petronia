
"""
Tests out the configuration parser.
"""

import unittest
from ..layout import (
    TileLayout,
    RootTileLayout,
    ScreenTileLayout,
    PortalLayout,
)
from ..config import TileLayoutConfig
from ..parser import (
    parse_config,
)
from ...splitter import (
    SPLIT_HORIZONTAL,
    SPLIT_VERTICAL,
)
from ......base.util.simple_type import PersistType


class ParseConfigTest(unittest.TestCase):

    def test_empty(self) -> None:
        config: PersistType = {}
        res, errors = parse_config(config)
        self.assertEqual(
            repr(res),
            repr(TileLayoutConfig([], []))
        )
        self.assertEqual(
            errors, []
        )

    def test_empty_top_lists(self) -> None:
        config: PersistType = {"layouts": [], "matchers": []}
        res, errors = parse_config(config)
        self.assertEqual(
            repr(res),
            repr(TileLayoutConfig([], []))
        )
        self.assertEqual(
            errors, []
        )

    def test_one_top_layout(self) -> None:
        config: PersistType = {
            "layouts": [{
                "direction": "top-down",
            }],
        }
        res, errors = parse_config(config)
        self.assertEqual(
            repr(res),
            repr(TileLayoutConfig([RootTileLayout([ScreenTileLayout(None, SPLIT_VERTICAL, False, (0, 0,), [])])], []))
        )

    def test_one_screen_layout(self) -> None:
        config: PersistType = {
            "layouts": [{
                "screens": [{
                    "direction": "left-right",
                }],
            }],
        }
        res, errors = parse_config(config)
        self.assertEqual(
            repr(res),
            repr(TileLayoutConfig([RootTileLayout([ScreenTileLayout(None, SPLIT_HORIZONTAL, False, (0, 0,), [])])], []))
        )
