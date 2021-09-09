
from typing import Optional
import unittest
from ..layout import (
    match_layouts_to_screens,
    ScreenTileLayout, VirtualScreenArea,
)


class MatchLayoutsTest(unittest.TestCase):
    def test_match_one_exact(self) -> None:
        layout1 = mk_screen_tile_layout('a', 100, 200)
        screen1 = mk_virtual_screen_area('1', 100, 200)
        mpack, errs = match_layouts_to_screens(
            [[layout1]],
            [screen1]
        )
        i, m = mpack
        self.assertEqual(list(errs), [])
        self.assertEqual(
            m,
            ((layout1, screen1,),)
        )

    def test_match_two_distant_layouts_one_screen(self) -> None:
        layout1 = mk_screen_tile_layout('a', 100, 200)
        layout2 = mk_screen_tile_layout('b', 200, 100)
        screen1 = mk_virtual_screen_area('1', 100, 200)
        mpack, errs = match_layouts_to_screens(
            [[layout1], [layout2]],
            [screen1]
        )
        i, m = mpack
        self.assertEqual(list(errs), [])
        self.assertEqual(
            m,
            ((layout1, screen1,),)
        )

    def test_match_two_screens_index_match(self) -> None:
        self.maxDiff = None
        layout1 = mk_screen_tile_layout('a', 100, 200)
        layout2 = mk_screen_tile_layout('b', 200, 100)
        screen1 = mk_virtual_screen_area('1', 100, 200)
        screen2 = mk_virtual_screen_area('2', 200, 100)
        mpack, errs = match_layouts_to_screens(
            [[layout1, layout2], [layout2, layout1]],
            [screen1, screen2]
        )
        i, m = mpack
        self.assertEqual(list(errs), [])
        self.assertEqual(
            m,
            ((layout1, screen1,), (layout2, screen2),)
        )
        mpack, errs = match_layouts_to_screens(
            [[layout2, layout1], [layout1, layout2]],
            [screen1, screen2]
        )
        i, m = mpack
        self.assertEqual(list(errs), [])
        self.assertEqual(
            m,
            ((layout1, screen1,), (layout2, screen2),)
        )

    def test_std_config(self) -> None:
        screen1 = mk_virtual_screen_area('primary', 1024, 768)
        layout1 = mk_screen_tile_layout(None, 0, 0, False, True)
        mpack, errs = match_layouts_to_screens(
            [[layout1]],
            [screen1]
        )
        i, m = mpack
        self.assertEqual(list(errs), [])
        self.assertEqual(
            m,
            ((layout1, screen1,),)
        )

    def test_two_layouts_one_screen_vs_two(self) -> None:
        screen = mk_virtual_screen_area('primary', 1024, 768)
        layout1_screen1 = mk_screen_tile_layout(None, 2440, 1980, False, True)
        layout1_screen2 = mk_screen_tile_layout(None, 1080, 1920, False, False)
        layout2_screen1 = mk_screen_tile_layout(None, 1920, 1080, False, True)
        mpack, errs = match_layouts_to_screens(
            [[layout1_screen1, layout1_screen2], [layout2_screen1]],
            [screen]
        )
        i, m = mpack
        self.assertEqual(list(errs), [])
        self.assertEqual(
            m,
            ((layout2_screen1, screen,),)
        )


def mk_screen_tile_layout(
        name: Optional[str], w: int, h: int, direct: bool = True, primary: bool = True
) -> ScreenTileLayout:
    return ScreenTileLayout(name, direct, primary, (w, h))


def mk_virtual_screen_area(
        name: str, w: int, h: int, x: int = 0, y: int = 0, primary: bool = True
) -> VirtualScreenArea:
    return VirtualScreenArea(name, (x, y, w, h,), primary)
