
"""
Tests out the configuration parser.
"""

import unittest
from ..layout import (
    RootTileLayout,
    ScreenTileLayout,
    SplitTileLayout,
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
            repr(TileLayoutConfig([RootTileLayout('top', [ScreenTileLayout(None, SPLIT_VERTICAL, False, (0, 0,), [
                PortalLayout('default', 1, 'r-ne')
            ])])], []))
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
            repr(TileLayoutConfig([RootTileLayout('0', [ScreenTileLayout(None, SPLIT_HORIZONTAL, False, (0, 0,), [
                PortalLayout('default', 1, 'r-ne')
            ])])], []))
        )

    def test_basic_split_layout(self) -> None:
        self.maxDiff = None
        config: PersistType = {
            "layouts": [{
                "direction": "left-right",
                "splits": [{
                    "size": 2,
                }, {
                    "target": True,
                    "size": 1,
                    "splits": [{
                        "size": 3,
                        "position": "r-nw",
                    }, {
                        "size": 2,
                    }],
                }],
            }],
        }
        res, errors = parse_config(config)
        self.assertEqual(
            repr(res),
            repr(TileLayoutConfig([RootTileLayout('top', [ScreenTileLayout(None, SPLIT_HORIZONTAL, False, (0, 0,), [
                PortalLayout('default', 2, 'r-ne'),
                SplitTileLayout(None, 1, [
                    PortalLayout('default', 3, 'r-nw'),
                    PortalLayout('default', 2, 'r-ne'),
                ], True),
            ])])], []))
        )
