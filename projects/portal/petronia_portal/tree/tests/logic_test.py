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
            window_event.ScreenDimension(10, 10, 20, 20),
            False, [],
        )
        known1 = tree.register_window('w1', None, window1)
        self.assertIsNotNone(known1)
        tree.move_window_to_portal_id(
            known1.target_id, tree.get_default_portal().portal_id, True, True,
        )
        self.assertTrue(known1.managed)
        screen_block = screen_state.VirtualScreenBlock(0, 0, 20, 20, 1, 1)
        main_portal = portal_state.Portal(
            1, portal_state.WindowPortalFit('left', 'top', 'none', 'none'),
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




