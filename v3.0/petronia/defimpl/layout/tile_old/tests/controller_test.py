
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
        original_active_portal, original_active_path = controller.callable_active_portal_path()
        self.assertEqual(
            original_active_path,
            (0, 0,)
        )
        src_portal, tgt_portal, window_cid = controller.move_portal_focus(
            MOVE_WINDOW_DIRECTION_EAST, 1
        )
        self.assertIs(original_active_portal, src_portal)
        self.assertEqual(
            controller.get_portal_path(tgt_portal),
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
        original_active_portal, original_active_path = controller.callable_active_portal_path()
        self.assertEqual(
            original_active_path,
            (0, 0)
        )
        src_portal, tgt_portal, window_cid = controller.move_portal_focus(
            MOVE_WINDOW_DIRECTION_SOUTH, 1
        )
        self.assertIs(original_active_portal, src_portal)
        self.assertEqual(
            controller.get_portal_path(tgt_portal),
            [0, 0]
        )
        src_portal, tgt_portal, window_cid = controller.move_portal_focus(
            MOVE_WINDOW_DIRECTION_EAST, 1
        )
        self.assertIs(original_active_portal, src_portal)
        self.assertEqual(
            controller.get_portal_path(tgt_portal),
            [0, 1, 0]
        )
        src_portal, tgt_portal, window_cid = controller.move_portal_focus(
            MOVE_WINDOW_DIRECTION_SOUTH, 1
        )
        self.assertIs(original_active_portal, src_portal)
        self.assertEqual(
            controller.get_portal_path(tgt_portal),
            [0, 1, 1]
        )


SCREEN = VirtualScreenInfo([VirtualScreenArea('', (0, 0, 100, 100), True)])


class TestableTileController(TileController):
    def __init__(self, raw_config: PersistType) -> None:
        config_layout, errors = parse_config(raw_config)
        assert not errors, repr(errors)
        root, index, errors = convert_config(config_layout, SCREEN)
        assert not errors, repr(errors)
        TileController.__init__(self, root, None)
        self.root = root

    def callable_active_portal_path(self) -> Tuple[Portal, Sequence[int]]:
        return self._active_portal_path()

    def get_portal_path(self, portal: Portal) -> Sequence[int]:
        for tgt_portal, tgt_path in self.root.get_portals_with_paths():
            if tgt_portal is portal:
                return tgt_path
        raise ValueError('no such portal ' + repr(portal))
