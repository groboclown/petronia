
import unittest
from ..splitter import (
    SplitterTile, Portal,
    SPLIT_HORIZONTAL, SPLIT_VERTICAL,
)
from ..portal import (
    POSITION_FAVOR_FILL,
)
from .....core.platform.api import ScreenArea


class SplitterTileTest(unittest.TestCase):
    def test_no_inner_splits(self) -> None:
        """Make sure we catch the no-splits case"""
        try:
            SplitterTile(
                simple_portal_factory,
                (0, 0, 1, 1), SPLIT_HORIZONTAL, [], True
            )
            self.fail('Did not raise an AssertionError for no splits')
        except AssertionError:
            pass

    def test_zero_sized_splits(self) -> None:
        """Make sure we don't have a divide by zero"""
        splitter = SplitterTile(
            simple_portal_factory,
            (0, 0, 1, 1), SPLIT_HORIZONTAL, [0, 0], True
        )
        self.assertIsNotNone(splitter)

    def test_odd_size(self) -> None:
        """Ensure that any remainder in position is correctly split."""
        splitter = SplitterTile(
            simple_portal_factory, (0, 0, 3, 3), SPLIT_HORIZONTAL, [1, 1], False
        )
        self.assertEqual(splitter.count(), 2)
        p1 = splitter[0]
        p2 = splitter[-1]
        self.assertIsNot(p1, p2)
        self.assertEqual(p1.get_area(), (0, 0, 1, 3))
        self.assertEqual(p2.get_area(), (1, 0, 2, 3))


def simple_portal_factory(_index: int, area: ScreenArea) -> Portal:
    return Portal('', area, [], POSITION_FAVOR_FILL, None)
