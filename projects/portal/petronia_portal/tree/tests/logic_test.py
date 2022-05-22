"""Test the module."""

from typing import List, Sequence, Iterable, Tuple
import unittest
from .. import logic, model
from ...events import window as window_event
from ...state import petronia_portal as portal_state
from ...state import screen as screen_state


class OptimizedTileTreeTest(unittest.TestCase):
    """Test the OptimizedTileTree class."""

    def test_uninitializied(self) -> None:
        """Test functionality while uninitialized."""
        tree = logic.OptimizedTileTree()
        self.assertFalse(tree.is_initialized())
        self.assertIsNone(tree.get_portal_by_id(1))
        assert tree is not None  # nosec  # for mypy
        self.assertEqual(
            tuple(tree.get_known_windows()),
            tuple(),
        )
        self.assertIsNotNone(tree.get_default_portal())

    def test_single_layout(self) -> None:
        """Test a single portal in the layout."""
        tree = logic.OptimizedTileTree()
        window1 = window_event.WindowState(
            True, 0, None,
            window_event.ScreenDimension(10, 11, 5, 6),
            False, [],
        )
        known1 = tree.register_window('w1', None, window1)
        self.assertIsNotNone(known1)
        assert known1 is not None  # nosec  # for mypy
        tree.move_window_to_portal_id(
            known1.target_id, tree.get_default_portal().portal_id, True, True,
        )
        self.assertTrue(known1.managed)
        screen_block = screen_state.VirtualScreenBlock(0, 0, 21, 22, 1, 1)
        main_portal = portal_state.Portal(
            1, portal_state.WindowPortalFit('left', 'top', 'fit', 'fit'),
            0, 0, 0, 0, ['a1'],
        )
        top_layout = portal_state.LayoutSplit(1, 'horizontal', [
            portal_state.SplitContent('a', main_portal),
        ])

        called_windows: List[Tuple[portal_state.Portal, Sequence[model.KnownWindow]]] = []

        def portal_window_callback(
                portal: portal_state.Portal, windows: Sequence[model.KnownWindow],
        ) -> Iterable[model.KnownWindow]:
            called_windows.append((portal, windows))
            return []

        changed_windows = tree.change_screen_layout(
            [(screen_block, top_layout)], portal_window_callback,
        )
        self.assertEqual(changed_windows, [known1])
        self.assertEqual(
            [(main_portal, [known1])],
            called_windows
        )
        # was: (10, 11) x (5, 6)
        # should now match screen size.
        self.assertEqual(known1.pos_x, 0)
        self.assertEqual(known1.pos_y, 0)
        self.assertEqual(known1.pos_w, 21)
        self.assertEqual(known1.pos_h, 22)

    def test_split_layout(self) -> None:
        """Test two portals in the layout."""
        tree = logic.OptimizedTileTree()
        window1 = window_event.WindowState(
            True, 0, None,
            window_event.ScreenDimension(10, 11, 5, 6),
            False, [],
        )
        known1 = tree.register_window('w1', None, window1)
        self.assertIsNotNone(known1)
        assert known1 is not None  # nosec  # for mypy
        tree.move_window_to_portal_id(
            known1.target_id, tree.get_default_portal().portal_id, True, True,
        )
        self.assertTrue(known1.managed)
        # Use an even divisor...
        screen_block = screen_state.VirtualScreenBlock(0, 0, 21, 24, 1, 1)
        portal1 = portal_state.Portal(
            2, portal_state.WindowPortalFit('left', 'top', 'fit', 'fit'),
            0, 0, 0, 0, ['default'],
        )
        portal2 = portal_state.Portal(
            1, portal_state.WindowPortalFit('left', 'top', 'fit', 'fit'),
            0, 0, 0, 0, ['b'],
        )
        top_layout = portal_state.LayoutSplit(1, 'horizontal', [
            portal_state.SplitContent('x', portal_state.LayoutSplit(
                1, 'horizontal', [
                    portal_state.SplitContent('default', portal1),
                    portal_state.SplitContent('b', portal2),
                ],
            ))
        ])

        called_windows: List[Tuple[portal_state.Portal, Sequence[model.KnownWindow]]] = []

        def portal_window_callback(
                portal: portal_state.Portal, windows: Sequence[model.KnownWindow],
        ) -> Iterable[model.KnownWindow]:
            called_windows.append((portal, windows))
            return []

        changed_windows = tree.change_screen_layout(
            [(screen_block, top_layout)], portal_window_callback,
        )
        self.assertEqual(changed_windows, [known1])
        self.assertEqual(
            [(portal1, [known1]), (portal2, [known1])],
            called_windows
        )

        # Ensure the portals are correctly sized.
        port_mod_1 = tree.get_portal_by_alias('default')
        self.assertIsNotNone(port_mod_1)
        assert port_mod_1 is not None  # nosec  # for mypy
        port_mod_2 = tree.get_portal_by_alias('b')
        self.assertIsNotNone(port_mod_2)
        assert port_mod_2 is not None  # nosec  # for mypy
        self.assertEqual(port_mod_1.pos_x, 0)
        self.assertEqual(port_mod_1.pos_y, 0)
        self.assertEqual(port_mod_1.width, 15)
        self.assertEqual(port_mod_1.height, 24)
        self.assertEqual(port_mod_2.pos_x, 15)
        self.assertEqual(port_mod_2.pos_y, 0)
        self.assertEqual(port_mod_2.width, 6)  # 15 + 6 = 21
        self.assertEqual(port_mod_2.height, 24)

        # Ensure the window is correctly positioned
        # was: (10, 11) x (5, 6)
        # should now match portal 1.
        self.assertEqual(known1.pos_x, 0)
        self.assertEqual(known1.pos_y, 0)
        self.assertEqual(known1.pos_w, 15)
        self.assertEqual(known1.pos_h, 24)

        # Now move the window to the second portal to ensure the positioning.

        portal_b = tree.get_portal_by_alias('b')
        self.assertIsNotNone(portal_b)
        assert portal_b is not None  # nosec  # for mypy
        tree.move_window_to_portal_id(
            'w1', portal_b.portal_id, True, True,
        )

        self.assertEqual(known1.pos_x, 15)
        self.assertEqual(known1.pos_y, 0)
        self.assertEqual(known1.pos_w, 6)
        self.assertEqual(known1.pos_h, 24)

    def test_move_window_to_portal_single_split(self) -> None:
        tree = logic.OptimizedTileTree()
        screen_block = screen_state.VirtualScreenBlock(0, 0, 21, 24, 1, 1)
        portal1 = portal_state.Portal(
            2, portal_state.WindowPortalFit('left', 'top', 'fit', 'fit'),
            0, 0, 0, 0, ['default'],
        )
        portal2 = portal_state.Portal(
            1, portal_state.WindowPortalFit('left', 'top', 'fit', 'fit'),
            0, 0, 0, 0, ['b'],
        )
        top_layout = portal_state.LayoutSplit(1, 'horizontal', [
            portal_state.SplitContent('x', portal_state.LayoutSplit(
                1, 'horizontal', [
                    portal_state.SplitContent('default', portal1),
                    portal_state.SplitContent('b', portal2),
                ],
            ))
        ])

        window1 = window_event.WindowState(
            True, 0, None,
            window_event.ScreenDimension(10, 11, 5, 6),
            False, [],
        )
        known1 = tree.register_window('w1', None, window1)
        self.assertIsNotNone(known1)
        assert known1 is not None  # nosec  # for mypy
        tree.move_window_to_portal_id(
            known1.target_id, tree.get_default_portal().portal_id, True, True,
        )
        self.assertTrue(known1.managed)
        # Use an even divisor...

        called_windows: List[Tuple[portal_state.Portal, Sequence[model.KnownWindow]]] = []

        def portal_window_callback(
                portal: portal_state.Portal, windows: Sequence[model.KnownWindow],
        ) -> Iterable[model.KnownWindow]:
            called_windows.append((portal, windows))
            return []

        changed_windows = tree.change_screen_layout(
            [(screen_block, top_layout)], portal_window_callback,
        )
        self.assertEqual(changed_windows, [known1])
        self.assertEqual(
            [(portal1, [known1]), (portal2, [known1])],
            called_windows
        )

    def test_get_target_portal_single_split(self) -> None:
        tree = logic.OptimizedTileTree()
        screen_block = screen_state.VirtualScreenBlock(0, 0, 21, 24, 1, 1)
        portal1 = portal_state.Portal(
            2, portal_state.WindowPortalFit('left', 'top', 'fit', 'fit'),
            0, 0, 0, 0, ['p1'],
        )
        portal2 = portal_state.Portal(
            1, portal_state.WindowPortalFit('left', 'top', 'fit', 'fit'),
            0, 0, 0, 0, ['p2'],
        )
        top_layout = portal_state.LayoutSplit(1, 'horizontal', [
            portal_state.SplitContent('x', portal_state.LayoutSplit(
                1, 'horizontal', [
                    portal_state.SplitContent('default', portal1),
                    portal_state.SplitContent('b', portal2),
                ],
            ))
        ])

        def portal_window_callback(
                portal: portal_state.Portal, windows: Sequence[model.KnownWindow],
        ) -> Iterable[model.KnownWindow]:
            return []

        changed_windows = tree.change_screen_layout(
            [(screen_block, top_layout)], portal_window_callback,
        )
        self.assertEqual(changed_windows, [])

        origin_portal = tree.get_portal_by_alias('p1')
        self.assertIsNotNone(origin_portal)
        assert origin_portal is not None  # nosec  # for mypy
        target_portal = tree.get_portal_by_alias('p2')
        self.assertIsNotNone(target_portal)
        assert target_portal is not None  # nosec  # for mypy
        target_id = tree.get_target_portal(origin_portal.portal_id, 'east')
        self.assertEqual(target_id, target_portal.portal_id)
