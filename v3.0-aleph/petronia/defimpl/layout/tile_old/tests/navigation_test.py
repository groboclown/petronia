
from typing import Sequence, Tuple, Optional
import unittest
from ..portal import Portal, POSITION_FAVOR_FILL
from ..navigation import (
    Navigator,
    PortalNav,
    create_navs,
)


class CreateNavsTest(unittest.TestCase):
    def test_one_portal_wrap_none(self) -> None:
        p0 = mk_portal(index=0, x=0, y=0, w=100, h=100)
        self.assertEqual(
            list(create_navs([p0], False, False)),
            [PortalNav(p0[0], 0, -1, -1, -1, -1, p0[1])]
        )

    def test_one_portal_wrap_xy(self) -> None:
        p0 = mk_portal(index=0, x=0, y=0, w=100, h=100)
        self.assertEqual(
            list(create_navs([p0], True, True)),
            [PortalNav(p0[0], 0, -1, -1, -1, -1, p0[1])]
        )

    def test_east_west_portal_wrap_none(self) -> None:
        p0 = mk_portal(index=0, x=0, y=0, w=100, h=100)
        p1 = mk_portal(index=1, x=100, y=0, w=100, h=100)
        self.assertEqual(
            list(create_navs([p0, p1], True, True)),
            [
                PortalNav(p0[0], 0, -1, 1, -1, -1, p0[1]),
                PortalNav(p1[0], 1, -1, -1, -1, 1, p1[1]),
            ]
        )


class NavigatorTest(unittest.TestCase):

    pass


def mk_portal(index: int, x: int, y: int, w: int, h: int, name: Optional[str] = None) -> Tuple[Portal, Sequence[int]]:
    return Portal(
        name=name or '',
        initial_size=(x, y, w, h),
        matchers=[], default_position=POSITION_FAVOR_FILL, background=None
    ), [index]
