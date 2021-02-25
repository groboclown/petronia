"""Test the module"""

from typing import cast
import unittest
import unittest.mock
import json
from petronia_common.util import RET_OK_NONE
from petronia_ext_lib.runner import EventRegistryContext
from petronia_ext_lib.events import datastore
from .. import monitor_screen
from ...events.impl import screen as screen_event
from ...events.impl import monitor as monitor_event
from ... import defs, virtual_screen


class MonitorScreenTest(unittest.TestCase):
    """Test classes and functions in the module."""

    def test_create_monitor_state(self) -> None:
        """Test create_monitor_state"""
        res = monitor_screen.create_monitor_state(
            1, 'desc',
            (cast(defs.MonitorUnit, 2), cast(defs.MonitorUnit, 3)),
            6, 7, True,
        )
        self.assertEqual(1, res.identifier)
        self.assertEqual('desc', res.description)
        self.assertEqual(2, res.real_pixel_width)
        self.assertEqual(3, res.real_pixel_height)
        self.assertEqual(6, res.dpi_x)
        self.assertEqual(7, res.dpi_y)
        self.assertEqual(True, res.supports_rotation)

    def test_store_screen_configuration__not_changed__no_source__empty(self) -> None:
        """Test store_screen_configuration"""
        context = unittest.mock.Mock(EventRegistryContext())
        context.send_event.return_value = RET_OK_NONE
        config = virtual_screen.VirtualScreenSettings()
        monitor_screen.store_screen_configuration(context, None, -1, config, False)
        context.send_event.assert_called_once()
        self.assertEqual(
            (
                screen_event.ConfigurationState.UNIQUE_TARGET_FQN,
                datastore.StoreDataEvent.UNIQUE_TARGET_FQN,
            ),
            context.send_event.call_args[0][0:2],
        )
        event = context.send_event.call_args[0][2]
        self.assertIsInstance(event, datastore.StoreDataEvent)
        assert isinstance(event, datastore.StoreDataEvent)  # nosec  # mypy requirement
        self.assertEqual(json.loads(event.json), {"mapped_screens_by_monitors": []})

    def test_store_screen_configuration__changed__source__configs(self) -> None:
        """Test store_screen_configuration"""
        context = unittest.mock.Mock(EventRegistryContext())
        context.send_event.return_value = RET_OK_NONE
        config = virtual_screen.VirtualScreenSettings()
        config.set_active_monitors([
            monitor_event.Monitor(1, 'm1', 100, 101, 102, 103, False),
            monitor_event.Monitor(2, 'm2', 200, 201, 202, 203, True),
        ])
        config.update_configuration([
            virtual_screen.VirtualScreenConfig(
                'c1', [(1, cast(defs.MonitorUnit, 2), cast(defs.MonitorUnit, 3))],
                virtual_screen.VirtualScreen([virtual_screen.VirtualScreenBlock(
                    (
                        1, defs.ZERO_MONITOR_UNIT, defs.ZERO_MONITOR_UNIT,
                        cast(defs.MonitorUnit, 2), cast(defs.MonitorUnit, 3),
                    ),
                    (
                        cast(defs.ScreenUnit, 5), cast(defs.ScreenUnit, 6),
                        cast(defs.ScreenUnit, 7), cast(defs.ScreenUnit, 8),
                    ), 0,
                )]),
            ),
            virtual_screen.VirtualScreenConfig(
                'c2', [(10, cast(defs.MonitorUnit, 11), cast(defs.MonitorUnit, 12))],
                virtual_screen.VirtualScreen([virtual_screen.VirtualScreenBlock(
                    (
                        10, defs.ZERO_MONITOR_UNIT, defs.ZERO_MONITOR_UNIT,
                        cast(defs.MonitorUnit, 12), cast(defs.MonitorUnit, 13),
                    ),
                    (
                        cast(defs.ScreenUnit, 15), cast(defs.ScreenUnit, 16),
                        cast(defs.ScreenUnit, 17), cast(defs.ScreenUnit, 18),
                    ), 0,
                )]),
            ),
        ])

        monitor_screen.store_screen_configuration(context, 's1', 199, config, True)
        context.send_event.assert_called()

        # Should be called with store virtual screen state, store configuration, success
        self.assertEqual(3, len(context.send_event.mock_calls))

        # store virtual state
        call_1 = context.send_event.mock_calls[0]
        self.assertEqual(
            (
                screen_event.VirtualScreenState.UNIQUE_TARGET_FQN,
                datastore.StoreDataEvent.UNIQUE_TARGET_FQN,
            ),
            call_1.args[0:2],
        )
        event = call_1.args[2]
        self.assertIsInstance(event, datastore.StoreDataEvent)
        assert isinstance(event, datastore.StoreDataEvent)  # nosec  # mypy requirement
        self.assertEqual(json.loads(event.json), {"area": [
            # This is the manufactured screen layout.
            {
                "nw_x_pixel": 0, "nw_y_pixel": 0, "width": 100, "height": 101,
                "ratio_x": 1, "ratio_y": 1,
            },
            {
                "nw_x_pixel": 100, "nw_y_pixel": 0, "width": 200, "height": 201,
                "ratio_x": 1, "ratio_y": 1,
            },
        ]})

        # store configuration
        call_2 = context.send_event.mock_calls[1]
        self.assertEqual(
            (
                screen_event.ConfigurationState.UNIQUE_TARGET_FQN,
                datastore.StoreDataEvent.UNIQUE_TARGET_FQN,
            ),
            call_2.args[0:2],
        )
        event = call_2.args[2]
        self.assertIsInstance(event, datastore.StoreDataEvent)
        assert isinstance(event, datastore.StoreDataEvent)  # nosec  # mypy requirement
        self.assertEqual(json.loads(event.json), {"mapped_screens_by_monitors": [
            {
                "description": "c1", "monitors": [
                    {"identifier": 1, "width": 2, "height": 3},
                ],
                "screen": [
                    {
                        "source_monitor": 1, "source_nw_x_pixel": 0, "source_nw_y_pixel": 0,
                        "source_pixel_width": 2, "source_pixel_height": 3, "rotation": 0,
                        "virtual_nw_x_pixel": 5, "virtual_nw_y_pixel": 6, "virtual_width": 7,
                        "virtual_height": 8,
                    },
                ],
            },
            {
                "description": "c2", "monitors": [
                    {"identifier": 10, "width": 11, "height": 12},
                ],
                "screen": [
                    {
                        "source_monitor": 10, "source_nw_x_pixel": 0, "source_nw_y_pixel": 0,
                        "source_pixel_width": 12, "source_pixel_height": 13, "rotation": 0,
                        "virtual_nw_x_pixel": 15, "virtual_nw_y_pixel": 16, "virtual_width": 17,
                        "virtual_height": 18,
                    },
                ],
            },
            {
                "description": "default-2", "monitors": [
                    {"identifier": 1, "width": 100, "height": 101},
                    {"identifier": 2, "width": 200, "height": 201},
                ],
                "screen": [
                    {
                        "source_monitor": 1, "source_nw_x_pixel": 0, "source_nw_y_pixel": 0,
                        "source_pixel_width": 1, "source_pixel_height": 100, "rotation": 0,
                        "virtual_nw_x_pixel": 0, "virtual_nw_y_pixel": 0, "virtual_width": 100,
                        "virtual_height": 101,
                    },
                    {
                        "source_monitor": 2, "source_nw_x_pixel": 0, "source_nw_y_pixel": 0,
                        "source_pixel_width": 2, "source_pixel_height": 200, "rotation": 0,
                        "virtual_nw_x_pixel": 100, "virtual_nw_y_pixel": 0, "virtual_width": 200,
                        "virtual_height": 201,
                    },
                ],
            },
        ]})

        # success
        call_3 = context.send_event.mock_calls[2]
        self.assertEqual(
            (
                screen_event.SetScreenConfigurationRequestEvent.UNIQUE_TARGET_FQN,
                's1',
            ),
            call_3.args[0:2],
        )
        event = call_3.args[2]
        self.assertIsInstance(event, screen_event.SetScreenConfigurationSuccessEvent)
        assert isinstance(  # nosec  # mypy requirement
            event, screen_event.SetScreenConfigurationSuccessEvent,
        )
        self.assertEqual(event.request_id, 199)
