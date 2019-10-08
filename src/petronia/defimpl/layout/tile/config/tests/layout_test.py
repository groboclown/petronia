
import unittest
from ..layout import (
    match_layouts_to_screens,
    ScreenTileLayout, VirtualScreenArea,
)


class MatchLayoutsTest(unittest.TestCase):
    def test_match_one_exact(self):
        layout1 = mk_screen_tile_layout('a', 100, 200)
        screen1 = mk_virtual_screen_area('1', 100, 200)
        m = match_layouts_to_screens(
            [[layout1]],
            [screen1]
        )
        self.assertEqual(
            m,
            ((layout1, screen1,),)
        )

    def test_match_two_distant_layouts_one_screen(self):
        layout1 = mk_screen_tile_layout('a', 100, 200)
        layout2 = mk_screen_tile_layout('b', 200, 100)
        screen1 = mk_virtual_screen_area('1', 100, 200)
        m = match_layouts_to_screens(
            [[layout1], [layout2]],
            [screen1]
        )
        self.assertEqual(
            m,
            ((layout1, screen1,),)
        )

    def test_match_two_screens_index_match(self):
        layout1 = mk_screen_tile_layout('a', 100, 200)
        layout2 = mk_screen_tile_layout('b', 200, 100)
        screen1 = mk_virtual_screen_area('1', 100, 200)
        screen2 = mk_virtual_screen_area('2', 200, 100)
        m = match_layouts_to_screens(
            [[layout1, layout2], [layout2, layout1]],
            [screen1, screen2]
        )
        self.assertEqual(
            m,
            ((layout1, screen1,), (layout2, screen2),)
        )
        m = match_layouts_to_screens(
            [[layout2, layout1], [layout1, layout2]],
            [screen1, screen2]
        )
        self.assertEqual(
            m,
            ((layout1, screen1,), (layout2, screen2),)
        )


def mk_screen_tile_layout(name: str, w: int, h: int, direct: bool = True, primary: bool = True) -> ScreenTileLayout:
    return ScreenTileLayout(name, direct, primary, (w, h))


def mk_virtual_screen_area(
        name: str, w: int, h: int, x: int = 0, y: int = 0, primary: bool = True
) -> VirtualScreenArea:
    return VirtualScreenArea(name, (x, y, w, h,), primary)
