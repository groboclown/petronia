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
        configuration_res = portal_state.ConfigurationState.parse_data({
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
        })
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
            known_window = root.register_window(window_id, None, window_state)
            portal_1 = root.get_portal_by_alias('p1')
            portal_2 = root.get_portal_by_alias('p2')
            portal_3 = root.get_portal_by_alias('p3')

        # TODO this doesn't look right.
        self.assertEqual(0, len(changed_windows))

        assert known_window is not None  # nosec  # for mypy
        self.assertEqual(window_id, known_window.target_id)
        self.assertIsNotNone(portal_1)
        assert portal_1 is not None  # nosec  # for mypy
        self.assertIsNotNone(portal_2)
        assert portal_2 is not None  # nosec  # for mypy
        self.assertIsNotNone(portal_3)
        assert portal_3 is not None  # nosec  # for mypy
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
        collector.next_as_eof(self)
        self.assertEqual(portal_2.portal_id, shared_state.get_active_portal_id())
