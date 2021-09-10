"""Test the module."""

import unittest
from .. import model
from ...state import petronia_portal as portal_state
from ...events import window as window_event


class ModelFunctionTest(unittest.TestCase):
    """Test the functions in the module."""

    def test_get_set_size(self) -> None:
        """test get_horiz_size, get_vert_size, set_horiz_size, set_vert_size"""
        tile = model.Portal([], portal_state.Portal(
            0, portal_state.WindowPortalFit('center', 'center', 'none', 'none'),
            0, 0, 0, 0, [],
        ))
        self.assertEqual(tile.pos_x, 0)
        self.assertEqual(tile.pos_y, 0)
        self.assertEqual(tile.width, 0)
        self.assertEqual(tile.height, 0)
        self.assertEqual((0, 0), model.get_horiz_size(tile))
        self.assertEqual((0, 0), model.get_vert_size(tile))

        model.set_horiz_size(tile, 30, 20, 30, 20)
        self.assertEqual(tile.pos_x, 30)
        self.assertEqual(tile.pos_y, 0)
        self.assertEqual(tile.width, 20)
        self.assertEqual(tile.height, 0)
        self.assertEqual((30, 20), model.get_horiz_size(tile))
        self.assertEqual((0, 0), model.get_vert_size(tile))

        model.set_vert_size(tile, 50, 60, 50, 60)
        self.assertEqual(tile.pos_x, 30)
        self.assertEqual(tile.pos_y, 50)
        self.assertEqual(tile.width, 20)
        self.assertEqual(tile.height, 60)
        self.assertEqual((30, 20), model.get_horiz_size(tile))
        self.assertEqual((50, 60), model.get_vert_size(tile))

    def test_get_first(self) -> None:
        """Tests get_first"""
        self.assertEqual(model.get_first(1, 2), 1)

    def test_get_second(self) -> None:
        """Tests get_second"""
        self.assertEqual(model.get_second(1, 2), 2)

    def test_adjust_position(self) -> None:
        """Tests adjust_position"""

        # Shrink and it's long, on the left side
        self.assertEqual(
            model.adjust_position(60, 30, 50, 'left', 'shrink'),
            (30, 50),
        )

        # Shrink but it's already too short.
        self.assertEqual(
            model.adjust_position(20, 30, 50, 'left', 'shrink'),
            (30, 20),
        )

        # Shrink and it's already short, on the right side
        self.assertEqual(
            model.adjust_position(20, 30, 50, 'right', 'shrink'),
            (60, 20),
        )

        # Shrink and it's already short, in the center
        self.assertEqual(
            model.adjust_position(20, 30, 50, 'center', 'shrink'),
            (45, 20),
        )

        # Stretch and it's long, on the left side
        self.assertEqual(
            model.adjust_position(60, 30, 50, 'left', 'stretch'),
            (30, 60),
        )

        # Stretch but it's short.
        self.assertEqual(
            model.adjust_position(20, 30, 50, 'left', 'stretch'),
            (30, 50),
        )

        # Stretch and it's long, on the right side
        self.assertEqual(
            model.adjust_position(80, 30, 50, 'right', 'stretch'),
            (0, 80),
        )

        # Stretch and it's long, in the center
        self.assertEqual(
            model.adjust_position(80, 30, 50, 'center', 'stretch'),
            (15, 80),
        )


class KnownWindowTest(unittest.TestCase):
    """Test the KnownWindow class."""

    def test_getters(self) -> None:
        """Test the getter functions."""
        window_state = window_event.WindowState(
            True, -1, None, window_event.ScreenDimension(1, 2, 3, 4), False, [],
        )
        knw = model.KnownWindow('x', None, True, window_state)
        self.assertEqual(knw.pos_x, 1)
        self.assertEqual(knw.pos_y, 2)
        self.assertEqual(knw.pos_w, 3)
        self.assertEqual(knw.pos_h, 4)
        self.assertEqual(knw.target_id, 'x')
        self.assertEqual(knw.managed, True)
        self.assertIs(knw.unmanaged_native_state, window_state)
        self.assertIs(knw.managed_native_state, window_state)

    def test_update_native_state(self) -> None:
        """Test update_native_state"""
        window_state_1 = window_event.WindowState(
            True, -1, None, window_event.ScreenDimension(1, 2, 3, 4), False, [],
        )
        knw = model.KnownWindow('x', None, True, window_state_1)
        self.assertIs(knw.unmanaged_native_state, window_state_1)
        self.assertIs(knw.managed_native_state, window_state_1)
        window_state_2 = window_event.WindowState(
            True, 0, None, window_event.ScreenDimension(5, 4, 3, 2), False, [],
        )
        knw.update_native_state(window_state_2)
        self.assertIs(knw.unmanaged_native_state, window_state_1)
        self.assertIs(knw.managed_native_state, window_state_2)
        window_state_3 = window_event.WindowState(
            False, 0, None, window_event.ScreenDimension(5, 4, 3, 2), False, [],
        )
        knw.managed = False
        knw.update_native_state(window_state_3)
        self.assertIs(knw.unmanaged_native_state, window_state_3)
        self.assertIs(knw.managed_native_state, window_state_2)

    def test_update_position(self) -> None:
        """Test update_position"""
