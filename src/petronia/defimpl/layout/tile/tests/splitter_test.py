
from typing import List, Any, Union
import unittest
from ..splitter import (
    SplitterTile, Portal, Tile, TileFactory,
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

    def test_mk__1_portal(self) -> None:
        """
        split:
            - portal (0)
        """
        splitter = SplitterTile(
            simple_portal_factory, (0, 0, 10, 10), SPLIT_HORIZONTAL, [1], False
        )
        self.assertEqual(splitter.count(), 1)
        self.assertEqual(splitter.get_area(), (0, 0, 10, 10))
        self.assertIsInstance(splitter[0], Portal)

    def test_mk__2_portals(self) -> None:
        """
        split:
            - portal (0)
            - portal (1)
        """
        splitter = SplitterTile(
            simple_portal_factory, (0, 0, 10, 10), SPLIT_HORIZONTAL, [1, 1], False
        )
        # Preconditions
        self.assertEqual(splitter.count(), 2)
        self.assertEqual(splitter.get_area(), (0, 0, 10, 10))
        self.assertIsInstance(splitter[0], Portal)
        self.assertIsInstance(splitter[1], Portal)

    def test_mk__1_sub_portal(self) -> None:
        """
        split:
             - portal (0)
             - split: (<1>) (opposite direction)
               - portal (1, 0)
             - portal (2)
        """
        splitter = SplitterTile(
            create_sub_portal_factory([0, 1, 0], SPLIT_HORIZONTAL), (0, 0, 10, 10), SPLIT_HORIZONTAL, [1, 1, 1], False
        )
        # Preconditions
        self.assertEqual(splitter.count(), 3)
        self.assertEqual(splitter.get_area(), (0, 0, 10, 10))
        self.assertIsInstance(splitter[0], Portal)
        self.assertIsInstance(splitter[1], SplitterTile)
        # mypy required check
        assert isinstance(splitter[1], SplitterTile)
        self.assertEqual(splitter[1].count(), 1)
        self.assertIsInstance(splitter[1][0], Portal)
        self.assertIsInstance(splitter[2], Portal)

    def test_mk__1_sub_portal_2(self) -> None:
        """
        split:
            - portal (0)
            - split: (<1>) (opposite direction)
                - split: (<1, 0>)
                    - portal (1, 0, 0)
                    - portal (1, 0, 1)
                - portal (1, 1, but skipped because of parent's split direction and 0 being active)
            - portal (2)
        """
        splitter = SplitterTile(
            create_sub_portal_factory([0, [2, 0], 0], SPLIT_HORIZONTAL),
            (0, 0, 10, 10), SPLIT_HORIZONTAL, [1, 1, 1], False
        )
        # Preconditions
        self.assertEqual(splitter.count(), 3)
        self.assertEqual(splitter.get_area(), (0, 0, 10, 10))
        self.assertIsInstance(splitter[0], Portal)
        self.assertIsInstance(splitter[1], SplitterTile)
        # mypy required check
        assert isinstance(splitter[1], SplitterTile)
        self.assertEqual(splitter[1].count(), 2)
        self.assertEqual(splitter[1].get_area(), (3, 0, 3, 10))
        self.assertIsInstance(splitter[1][0], SplitterTile)
        assert isinstance(splitter[1][0], SplitterTile)
        self.assertEqual(splitter[1][0].count(), 2)
        self.assertEqual(splitter[1][0].get_area(), (3, 0, 3, 5))
        self.assertIsInstance(splitter[1][0][0], Portal)
        self.assertIsInstance(splitter[1][0][1], Portal)
        self.assertIsInstance(splitter[1][1], Portal)
        self.assertIsInstance(splitter[2], Portal)


def simple_portal_factory(_index: int, area: ScreenArea) -> Portal:
    return Portal('', area, [], POSITION_FAVOR_FILL, None)


def create_sub_portal_factory(children: List[Any], direction: int) -> TileFactory:
    def ret(index: int, area: ScreenArea) -> Tile:
        kids: List[int] = []
        nd = SPLIT_VERTICAL if direction is SPLIT_HORIZONTAL else SPLIT_HORIZONTAL
        kid: Union[int, List[Any]] = 0
        if 0 <= index <= len(children):
            kid = children[index]
        if isinstance(kid, int):
            if kid <= 0:
                return Portal('', area, [], POSITION_FAVOR_FILL, None)
            for _i in range(kid):
                kids.append(1)
            return SplitterTile(simple_portal_factory, area, nd, kids, False)
        assert isinstance(kid, list)

        for _i in range(len(kid)):
            kids.append(1)

        return SplitterTile(create_sub_portal_factory(kid, nd), area, nd, kids, False)

    return ret
