
"""
Test the controller.
"""


import unittest
from typing import Tuple, Sequence
from ..controller import (
    TileController,
    Portal,
    MOVE_WINDOW_DIRECTION_EAST,
    MOVE_WINDOW_DIRECTION_SOUTH,
)
from ..config import parse_config
from ..convert_config import convert_config
from .....core.platform.api import (
    VirtualScreenInfo,
    VirtualScreenArea,
)
from .....base.util.simple_type import PersistType, readonly_persistent_copy


class TileControllerTest(unittest.TestCase):
    def test_find_portal_dir_common_ew(self) -> None:
        controller = TestableTileController(readonly_persistent_copy({
            'layouts': [{
                'direction': 'horiz',
                'splits': [{
                    'size': 3,
                }, {
                    'size': 1,
                    'splits': [{
                        'size': 2,
                    }, {
                        'size': 1,
                    }]
                }],
            }]
        }))
        self.assertEqual(
            controller.callable_active_path(),
            [0, 0]
        )
        portal, path = controller.callable_find_portal_dir(
            controller.get_active_portal(), MOVE_WINDOW_DIRECTION_EAST, 1, False
        )
        self.assertEqual(
            path,
            [0, 1, 0]
        )

    def test_find_portal_dir_common_ns(self) -> None:
        controller = TestableTileController(readonly_persistent_copy({
            'layouts': [{
                'direction': 'vertical',
                'splits': [{
                    'size': 3,
                }, {
                    'size': 1,
                    'splits': [{
                        'size': 2,
                    }, {
                        'size': 1,
                    }]
                }],
            }]
        }))
        self.assertEqual(
            controller.callable_active_path(),
            [0, 0]
        )
        portal, path = controller.callable_find_portal_dir(
            controller.get_active_portal(), MOVE_WINDOW_DIRECTION_SOUTH, 1, False
        )
        self.assertEqual(
            path,
            [0, 1, 0]
        )


SCREEN = VirtualScreenInfo([VirtualScreenArea('', (0, 0, 100, 100), True)])


class TestableTileController(TileController):
    def __init__(self, raw_config: PersistType) -> None:
        config_layout, errors = parse_config(raw_config)
        assert not errors, repr(errors)
        root, index, errors = convert_config(config_layout, SCREEN)
        assert not errors, repr(errors)
        TileController.__init__(self, root)
        self.root = root

    def callable_find_portal_dir(
            self, src_portal: Portal, direction: int, count: int, wrap: bool
    ) -> Tuple[Portal, Sequence[int]]:
        return self._find_portal_dir(src_portal, direction, count, wrap)

    def callable_active_path(self) -> Sequence[int]:
        return self._active_path()
