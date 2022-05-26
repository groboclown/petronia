"""Tests for the portal handler"""

from typing import Optional
import unittest
from petronia_common.event_stream.tests.shared import (
    create_read_stream, SimpleBinaryWriter,
)
from petronia_ext_lib.runner import SimpleEventRegistryContext
from .. import portal_handler
from .. import shared_state
from ..events import window as window_event
from ..state import petronia_portal as portal_state
from ..state import screen as screen_state
from ..tree import model


class PortalHandlerTest(unittest.TestCase):
    """Test the portal handler functions"""

    def test_handle_move_window_to_portal_through_split(self) -> None:
        """Test a simple handle_move_window_to_portal call, with one window moved to
        another portal."""
        screen_block = screen_state.VirtualScreenBlock(0, 0, 21, 24, 1, 1)
        configuration_res = portal_state.ConfigurationState.parse_data(TRIPLE_LAYOUT)
        self.assertEqual((), configuration_res.error_messages())
        shared_state.clear_data(configuration_res.result)
        writer = SimpleBinaryWriter()
        context = SimpleEventRegistryContext(create_read_stream(b''), writer, None)
        window_id = 'test:window'
        window_state = window_event.WindowState(
            True, 1, None, window_event.ScreenDimension(0, 0, 10, 10), False, [],
        )

        portal_1: Optional[model.Portal]
        portal_2: Optional[model.Portal]
        portal_3: Optional[model.Portal]
        with shared_state.layout_root() as root:
            changed_windows = root.change_screen_layout(
                [(screen_block, shared_state.configuration().workspaces[0].screens[0].layout)],
                lambda x, y: [],
            )

            # No windows have been added yet, so nothing was changed.
            self.assertEqual(0, len(changed_windows))

            known_window = root.register_window(window_id, None, window_state)
            portal_1 = root.get_portal_by_alias('p1')
            portal_2 = root.get_portal_by_alias('p2')
            portal_3 = root.get_portal_by_alias('p3')
            changed = root.move_window_to_portal_id(window_id, portal_1.portal_id, True, True)

        assert known_window is not None  # nosec  # for mypy
        self.assertEqual(window_id, known_window.target_id)
        self.assertIsNotNone(portal_1)
        assert portal_1 is not None  # nosec  # for mypy
        self.assertIsNotNone(portal_2)
        assert portal_2 is not None  # nosec  # for mypy
        self.assertIsNotNone(portal_3)
        assert portal_3 is not None  # nosec  # for mypy
        self.assertEqual(changed, [known_window])

        shared_state.set_active_portal_id(portal_1.portal_id)
        shared_state.set_focused_window_id(window_id)
        self.assertEqual(portal_1.portal_id, shared_state.get_active_portal_id())
        collector = writer.collect_events()
        collector.next_as_eof(self)
        writer.clear()

        res = portal_handler.handle_move_window_to_portal(context, 'east', True)
        self.assertEqual((), res.error_messages())
        collector = writer.collect_events()
        collector.assert_next_event_equal(
            self,
            (
                window_event.SetFocusedWindowEvent.FULL_EVENT_NAME,
                portal_state.EXTENSION_NAME + ':focus-window',  # source id
                window_id,  # target id
                window_event.SetFocusedWindowEvent(0).export_data(),
            ),
        )
        collector.assert_next_event_equal(
            self,
            (
                window_event.SetWindowPositionsEvent.FULL_EVENT_NAME,
                portal_state.EXTENSION_NAME + ':move-windows',  # source id
                window_event.SetWindowPositionsEvent.UNIQUE_TARGET_FQN,  # target id
                window_event.SetWindowPositionsEvent([
                    window_event.WindowIdPositions(window_id, window_event.ScreenDimension(
                        x=15, y=0, width=6, height=14,
                    )),
                ]).export_data(),
            ),
        )
        collector.next_as_eof(self)
        self.assertEqual(portal_2.portal_id, shared_state.get_active_portal_id())

    def test_handle_rotate_active_window__no_window(self) -> None:
        """Test a simple handle_rotate_active_window call with no active window."""
        screen_block = screen_state.VirtualScreenBlock(0, 0, 21, 24, 1, 1)
        configuration_res = portal_state.ConfigurationState.parse_data(TRIPLE_LAYOUT)
        self.assertEqual((), configuration_res.error_messages())
        shared_state.clear_data(configuration_res.result)
        writer = SimpleBinaryWriter()
        context = SimpleEventRegistryContext(create_read_stream(b''), writer, None)

        portal_1: Optional[model.Portal]
        with shared_state.layout_root() as root:
            changed_windows = root.change_screen_layout(
                [(screen_block, shared_state.configuration().workspaces[0].screens[0].layout)],
                lambda x, y: [],
            )

            # No windows have been added yet, so nothing was changed.
            self.assertEqual(0, len(changed_windows))

            portal_1 = root.get_portal_by_alias('p1')

        self.assertIsNotNone(portal_1)
        assert portal_1 is not None  # nosec  # for mypy
        shared_state.set_active_portal_id(portal_1.portal_id)
        self.assertEqual(portal_1.portal_id, shared_state.get_active_portal_id())
        collector = writer.collect_events()
        collector.next_as_eof(self)
        writer.clear()

        res = portal_handler.handle_rotate_active_window(context, 'forward')
        self.assertEqual((), res.error_messages())
        collector = writer.collect_events()
        collector.next_as_eof(self)
        self.assertEqual(portal_1.portal_id, shared_state.get_active_portal_id())

    def test_handle_rotate_active_window__1_window(self) -> None:
        """Test a simple handle_rotate_active_window call with only 1 window."""
        screen_block = screen_state.VirtualScreenBlock(0, 0, 21, 24, 1, 1)
        configuration_res = portal_state.ConfigurationState.parse_data(TRIPLE_LAYOUT)
        self.assertEqual((), configuration_res.error_messages())
        shared_state.clear_data(configuration_res.result)
        writer = SimpleBinaryWriter()
        context = SimpleEventRegistryContext(create_read_stream(b''), writer, None)
        window_id = 'test:window'
        window_state = window_event.WindowState(
            True, 1, None, window_event.ScreenDimension(0, 0, 10, 10), False, [],
        )

        portal_1: Optional[model.Portal]
        with shared_state.layout_root() as root:
            changed_windows = root.change_screen_layout(
                [(screen_block, shared_state.configuration().workspaces[0].screens[0].layout)],
                lambda x, y: [],
            )

            # No windows have been added yet, so nothing was changed.
            self.assertEqual(0, len(changed_windows))

            known_window = root.register_window(window_id, None, window_state)
            portal_1 = root.get_portal_by_alias('p1')
            changed = root.move_window_to_portal_id(window_id, portal_1.portal_id, True, True)

        assert known_window is not None  # nosec  # for mypy
        self.assertEqual(window_id, known_window.target_id)
        self.assertIsNotNone(portal_1)
        assert portal_1 is not None  # nosec  # for mypy
        self.assertEqual(changed, [known_window])
        shared_state.set_active_portal_id(portal_1.portal_id)
        shared_state.set_focused_window_id(window_id)
        self.assertEqual(portal_1.portal_id, shared_state.get_active_portal_id())
        collector = writer.collect_events()
        collector.next_as_eof(self)
        writer.clear()

        res = portal_handler.handle_rotate_active_window(context, 'forward')
        self.assertEqual((), res.error_messages())
        collector = writer.collect_events()
        collector.assert_next_event_equal(
            self,
            (
                window_event.SetFocusedWindowEvent.FULL_EVENT_NAME,
                portal_state.EXTENSION_NAME + ':focus-window',  # source id
                window_id,  # target id
                window_event.SetFocusedWindowEvent(0).export_data(),
            ),
        )
        collector.next_as_eof(self)
        self.assertEqual(portal_1.portal_id, shared_state.get_active_portal_id())

    def test_handle_rotate_active_window__5_windows(self) -> None:
        """Test a simple handle_rotate_active_window call with 3 windows in the first
        portal, and 1 in each of the other portals."""
        screen_block = screen_state.VirtualScreenBlock(0, 0, 21, 24, 1, 1)
        configuration_res = portal_state.ConfigurationState.parse_data(TRIPLE_LAYOUT)
        self.assertEqual((), configuration_res.error_messages())
        shared_state.clear_data(configuration_res.result)
        writer = SimpleBinaryWriter()
        context = SimpleEventRegistryContext(create_read_stream(b''), writer, None)
        window1_id = 'test:window1'
        window1_state = window_event.WindowState(
            True, 1, None, window_event.ScreenDimension(0, 0, 10, 10), False, [],
        )
        window2_id = 'test:window2'
        window2_state = window_event.WindowState(
            True, 0, None, window_event.ScreenDimension(0, 0, 10, 10), False, [],
        )
        window3_id = 'test:window3'
        window3_state = window_event.WindowState(
            True, 0, None, window_event.ScreenDimension(0, 0, 10, 10), False, [],
        )
        window4_id = 'test:window4'
        window4_state = window_event.WindowState(
            True, 0, None, window_event.ScreenDimension(0, 0, 10, 10), False, [],
        )
        window5_id = 'test:window5'
        window5_state = window_event.WindowState(
            True, 0, None, window_event.ScreenDimension(0, 0, 10, 10), False, [],
        )

        portal_1: Optional[model.Portal]
        portal_2: Optional[model.Portal]
        portal_3: Optional[model.Portal]
        with shared_state.layout_root() as root:
            changed_windows = root.change_screen_layout(
                [(screen_block, shared_state.configuration().workspaces[0].screens[0].layout)],
                lambda x, y: [],
            )

            # No windows have been added yet, so nothing was changed.
            self.assertEqual(0, len(changed_windows))

            known_window1 = root.register_window(window1_id, None, window1_state)
            known_window2 = root.register_window(window2_id, None, window2_state)
            known_window3 = root.register_window(window3_id, None, window3_state)
            known_window4 = root.register_window(window4_id, None, window4_state)
            known_window5 = root.register_window(window5_id, None, window5_state)

            portal_1 = root.get_portal_by_alias('p1')
            portal_2 = root.get_portal_by_alias('p1')
            portal_3 = root.get_portal_by_alias('p1')

            # Add in reverse order, so that window 5 is on the bottom.
            changed5 = root.move_window_to_portal_id(window5_id, portal_3.portal_id, True, True)
            changed4 = root.move_window_to_portal_id(window4_id, portal_2.portal_id, True, True)
            changed3 = root.move_window_to_portal_id(window3_id, portal_1.portal_id, True, True)
            changed2 = root.move_window_to_portal_id(window2_id, portal_1.portal_id, True, True)
            changed1 = root.move_window_to_portal_id(window1_id, portal_1.portal_id, True, True)

        assert known_window1 is not None  # nosec  # for mypy
        self.assertEqual(window1_id, known_window1.target_id)
        assert known_window2 is not None  # nosec  # for mypy
        self.assertEqual(window2_id, known_window2.target_id)
        assert known_window3 is not None  # nosec  # for mypy
        self.assertEqual(window3_id, known_window3.target_id)
        assert known_window4 is not None  # nosec  # for mypy
        self.assertEqual(window4_id, known_window4.target_id)
        assert known_window5 is not None  # nosec  # for mypy
        self.assertEqual(window5_id, known_window5.target_id)

        self.assertEqual(changed1, [known_window1])
        self.assertEqual(changed2, [known_window2])
        self.assertEqual(changed3, [known_window3])
        self.assertEqual(changed4, [known_window4])
        self.assertEqual(changed5, [known_window5])

        self.assertIsNotNone(portal_1)
        assert portal_1 is not None  # nosec  # for mypy
        self.assertIsNotNone(portal_2)
        assert portal_2 is not None  # nosec  # for mypy
        self.assertIsNotNone(portal_3)
        assert portal_3 is not None  # nosec  # for mypy

        self.assertEqual(window1_id, known_window1.target_id)
        self.assertEqual(window2_id, known_window2.target_id)
        self.assertEqual(window3_id, known_window3.target_id)
        self.assertEqual(window4_id, known_window4.target_id)
        self.assertEqual(window5_id, known_window5.target_id)

        shared_state.set_active_portal_id(portal_1.portal_id)
        shared_state.set_focused_window_id(window1_id)
        self.assertEqual(portal_1.portal_id, shared_state.get_active_portal_id())
        self.assertEqual(window1_id, shared_state.get_focused_window_id())

        collector = writer.collect_events()
        collector.next_as_eof(self)
        writer.clear()

        res = portal_handler.handle_rotate_active_window(context, 'forward')
        self.assertEqual((), res.error_messages())
        collector = writer.collect_events()
        collector.assert_next_event_equal(
            self,
            (
                window_event.SetFocusedWindowEvent.FULL_EVENT_NAME,
                portal_state.EXTENSION_NAME + ':focus-window',  # source id
                window2_id,  # target id
                window_event.SetFocusedWindowEvent(0).export_data(),
            ),
        )
        collector.next_as_eof(self)
        self.assertEqual(portal_1.portal_id, shared_state.get_active_portal_id())

        # Even though the state setup has window2 on top, the native handler
        #   hasn't received the event and sent the focused window response.
        self.assertEqual(window2_id, shared_state.get_focused_window_id())


TRIPLE_LAYOUT = {
    'workspaces': [{
        'screens': [{
            "block": {
                "x": 0, "y": 0, "width": 100, "height": 100,
            },
            "layout": {
                "size": 1,
                "direction": "horizontal",
                "contents": [
                    {
                        "type": "portal",
                        "value": {
                            "size": 2, "portal_aliases": ["p1"],
                            "padding_top": 0, "padding_bottom": 0,
                            "padding_left": 0, "padding_right": 0,
                            "preferred_location": {
                                "justify_horizontal": "left",
                                "justify_vertical": "top",
                                "fit_horizontal": "fit",
                                "fit_vertical": "fit",
                            },
                        },
                    },
                    {
                        "type": "split",
                        "value": {
                            "size": 1,
                            "direction": "vertical",
                            "contents": [
                                {
                                    "type": "portal",
                                    "value": {
                                        "size": 1, "portal_aliases": ["p2"],
                                        "padding_top": 0, "padding_bottom": 0,
                                        "padding_left": 0, "padding_right": 0,
                                        "preferred_location": {
                                            "justify_horizontal": "left",
                                            "justify_vertical": "top",
                                            "fit_horizontal": "fit",
                                            "fit_vertical": "fit",
                                        },
                                    },
                                },
                                {
                                    "type": "portal",
                                    "value": {
                                        "size": 2, "portal_aliases": ["p3"],
                                        "padding_top": 0, "padding_bottom": 0,
                                        "padding_left": 0, "padding_right": 0,
                                        "preferred_location": {
                                            "justify_horizontal": "left",
                                            "justify_vertical": "top",
                                            "fit_horizontal": "fit",
                                            "fit_vertical": "fit",
                                        },
                                    },
                                },
                            ],
                        },
                    },
                ],
            },
        }],
    }],
    'default_window_behavior': [],
}
