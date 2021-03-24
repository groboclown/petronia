"""Test the module"""

from typing import Sequence, List, Optional, cast
import unittest
import unittest.mock
import json
from petronia_common.util import RET_OK_NONE, possible_error, not_none, UserMessage, i18n
from petronia_ext_lib.runner import EventRegistryContext
from petronia_ext_lib.events import datastore as datastore_events
from .. import monitor_screen
from ...events.impl import monitor, screen
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

    def test_store_monitor_state(self) -> None:
        """Test store_monitor_state"""
        context = unittest.mock.Mock(EventRegistryContext())
        context.send_event.return_value = RET_OK_NONE
        res = monitor_screen.store_monitor_state(
            context, [],
        )
        self.assertIsNone(res.error)
        context.send_event.assert_called_once()
        args = context.send_event.call_args.args
        self.assertEqual(args[0], monitor.ActiveMonitorsState.UNIQUE_TARGET_FQN)
        self.assertEqual(args[1], datastore_events.StoreDataEvent.UNIQUE_TARGET_FQN)
        event_obj = args[2]
        self.assertIsInstance(event_obj, datastore_events.StoreDataEvent)
        assert isinstance(event_obj, datastore_events.StoreDataEvent)  # nosec  # mypy required
        self.assertEqual(json.dumps({'monitors': []}), event_obj.json)

    def test_store_virtual_screen_state(self) -> None:
        """Test store_virtual_screen_state"""
        context = unittest.mock.Mock(EventRegistryContext())
        context.send_event.return_value = RET_OK_NONE
        res = monitor_screen.store_virtual_screen_state(
            context, virtual_screen.VirtualScreen([]),
        )
        self.assertIsNone(res.error)
        context.send_event.assert_called_once()
        args = context.send_event.call_args.args
        self.assertEqual(args[0], screen.VirtualScreenState.UNIQUE_TARGET_FQN)
        self.assertEqual(args[1], datastore_events.StoreDataEvent.UNIQUE_TARGET_FQN)
        event_obj = args[2]
        self.assertIsInstance(event_obj, datastore_events.StoreDataEvent)
        assert isinstance(event_obj, datastore_events.StoreDataEvent)  # nosec  # mypy required
        self.assertEqual(json.dumps({'area': []}), event_obj.json)

    def test_send_screen_configuration_bad(self) -> None:
        """Test send_screen_configuration_bad"""
        context = unittest.mock.Mock(EventRegistryContext())
        context.send_event.return_value = RET_OK_NONE
        res = monitor_screen.send_screen_configuration_bad(
            context, 's1', 12, not_none(possible_error([UserMessage('c', i18n('m'))])),
        )
        self.assertIsNone(res.error)
        context.send_event.assert_called_once()
        args = context.send_event.call_args.args
        self.assertEqual(args[0], screen.SetScreenConfigurationRequestEvent.UNIQUE_TARGET_FQN)
        self.assertEqual(args[1], 's1')
        event_obj = args[2]
        self.assertIsInstance(event_obj, screen.SetScreenConfigurationFailureEvent)

        # mypy required
        assert isinstance(event_obj, screen.SetScreenConfigurationFailureEvent)  # nosec

        self.assertEqual(
            {
                'error': {
                    'categories': ['invalid-user-action'],
                    'identifier': 'bad-config',
                    'messages': [{'arguments': [], 'catalog': 'c', 'message': 'm'}],
                    'source': 'native-screen',
                },
                'request_id': 12,
            },
            event_obj.export_data(),
        )

    def test_create_screen_config_from_mapped_screen__empty(self) -> None:
        """Test the create_screen_config_from_mapped_screen function"""
        empty_group = screen.ScreenMonitorMappingConfigGroup(None, [], [])
        res = monitor_screen.create_screen_config_from_mapped_screen(empty_group)
        self.assertEqual('screen-config', res.name)
        self.assertEqual(0, len(res.monitor_defs))
        self.assertEqual(0, len(res.screen.blocks))

    def test_create_screen_config_from_mapped_screen__two(self) -> None:
        """Test the create_screen_config_from_mapped_screen function"""
        monitor_screens = screen.ScreenMonitorMappingConfigGroup(
            'desc',
            [
                screen.SourceMonitor(0, 10, 20),
                screen.SourceMonitor(1, 100, 90),
            ],
            [
                screen.ScreenMonitorMapping(None, 0, 0, 10, 20, 0, 0, 0, 10, 20),
                screen.ScreenMonitorMapping(1, 0, 0, 100, 90, 10, 10, 0, 100, 90),
                screen.ScreenMonitorMapping(None, 80, 60, 40, 50, 0, 1, 2, 20, 30),
            ],
        )
        res = monitor_screen.create_screen_config_from_mapped_screen(monitor_screens)
        self.assertEqual('desc', res.name)
        self.assertEqual(
            ((0, 10, 20), (1, 100, 90)),
            res.monitor_defs
        )
        self.assertEqual(
            (
                virtual_screen.VirtualScreenBlock(
                    (
                        0, cast(defs.MonitorUnit, 0), cast(defs.MonitorUnit, 0),
                        cast(defs.MonitorUnit, 10), cast(defs.MonitorUnit, 20),
                    ),
                    (
                        cast(defs.ScreenUnit, 0), cast(defs.ScreenUnit, 0),
                        cast(defs.ScreenUnit, 10), cast(defs.ScreenUnit, 20),
                    ),
                    0,
                ),
                virtual_screen.VirtualScreenBlock(
                    (
                        1, cast(defs.MonitorUnit, 0), cast(defs.MonitorUnit, 0),
                        cast(defs.MonitorUnit, 100), cast(defs.MonitorUnit, 90),
                    ),
                    (
                        cast(defs.ScreenUnit, 10), cast(defs.ScreenUnit, 0),
                        cast(defs.ScreenUnit, 100), cast(defs.ScreenUnit, 90),
                    ),
                    0,
                ),
                virtual_screen.VirtualScreenBlock(
                    (
                        2, cast(defs.MonitorUnit, 80), cast(defs.MonitorUnit, 60),
                        cast(defs.MonitorUnit, 40), cast(defs.MonitorUnit, 50),
                    ),
                    (
                        cast(defs.ScreenUnit, 1), cast(defs.ScreenUnit, 2),
                        cast(defs.ScreenUnit, 20), cast(defs.ScreenUnit, 30),
                    ),
                    10,
                ),
            ),
            res.screen.blocks,
        )


class AbstractMonitorHandlerTest(unittest.TestCase):
    """Test the AbstractScreenHandler and ScreenConfigChangedEventListener class."""

    def test_closed(self) -> None:
        """Test the functions when the instance is closed."""
        context = unittest.mock.Mock(EventRegistryContext())
        handler = monitor_screen.AbstractMonitorHandler[MockNativeMonitor](
            context, monitor_screen.WindowScreenMapper([], virtual_screen.VirtualScreen([])),
        )
        handler.close()
        res = handler.detected_monitor_changed([])
        self.assertIsNone(res.error)
        res = handler.detected_screen_changed(virtual_screen.VirtualScreen([]))
        self.assertIsNone(res.error)

    def test_detected_monitor_changed(self) -> None:  # pylint:disable=too-many-statements
        """Test detected_monitor_changed."""
        context = unittest.mock.Mock(EventRegistryContext())
        context.send_event.return_value = RET_OK_NONE
        handler = MockScreenHandler(context)
        handler.ret__get_virtual_screen_for_monitors = virtual_screen.VirtualScreen([
            _create_virtual_screen_block(100, 200),
        ])
        monitor_set_1: List[MockNativeMonitor] = [
            MockNativeMonitor(monitor.Monitor(1, 'x', 2, 3, 4, 5, False)),
        ]
        res = handler.detected_monitor_changed(monitor_set_1)
        self.assertIsNone(res.error)
        context.send_event.assert_called()
        self.assertEqual(2, len(context.send_event.call_args_list))

        call1_args = context.send_event.call_args_list[0].args
        self.assertEqual(call1_args[0], monitor.ActiveMonitorsState.UNIQUE_TARGET_FQN)
        self.assertEqual(call1_args[1], datastore_events.StoreDataEvent.UNIQUE_TARGET_FQN)
        event_obj = call1_args[2]
        self.assertIsInstance(event_obj, datastore_events.StoreDataEvent)
        assert isinstance(event_obj, datastore_events.StoreDataEvent)  # nosec  # mypy required
        self.assertEqual(
            json.dumps({'monitors': [
                {
                    'identifier': 1, 'description': 'x', 'real_pixel_width': 2,
                    'real_pixel_height': 3, 'dpi_x': 4, 'dpi_y': 5, 'supports_rotation': False,
                },
            ]}),
            event_obj.json,
        )

        call2_args = context.send_event.call_args_list[1].args
        self.assertEqual(call2_args[0], screen.VirtualScreenState.UNIQUE_TARGET_FQN)
        self.assertEqual(call2_args[1], datastore_events.StoreDataEvent.UNIQUE_TARGET_FQN)
        event_obj = call2_args[2]
        self.assertIsInstance(event_obj, datastore_events.StoreDataEvent)
        assert isinstance(event_obj, datastore_events.StoreDataEvent)  # nosec  # mypy required
        self.assertEqual(
            json.dumps({'area': [
                {
                    'nw_x_pixel': 0, 'nw_y_pixel': 0, 'width': 100, 'height': 200,

                    # This ratio isn't right; it need to take DPI into account.
                    'ratio_x': 1, 'ratio_y': 1,
                },
            ]}),
            event_obj.json,
        )

        # Perform the same update, and ensure that the screen handler correctly ignored the
        # update.
        monitor_set_2: List[MockNativeMonitor] = [
            MockNativeMonitor(monitor.Monitor(1, 'x', 20, 3, 4, 5, False)),
        ]
        context.reset_mock()
        res = handler.detected_monitor_changed(monitor_set_2)
        self.assertIsNone(res.error)
        context.send_event.assert_called()
        self.assertEqual(1, len(context.send_event.call_args_list))
        call1_args = context.send_event.call_args_list[0].args
        self.assertEqual(call1_args[0], monitor.ActiveMonitorsState.UNIQUE_TARGET_FQN)
        self.assertEqual(call1_args[1], datastore_events.StoreDataEvent.UNIQUE_TARGET_FQN)
        event_obj = call1_args[2]
        self.assertIsInstance(event_obj, datastore_events.StoreDataEvent)
        assert isinstance(event_obj, datastore_events.StoreDataEvent)  # nosec  # mypy required
        self.assertEqual(
            json.dumps({'monitors': [
                {
                    'identifier': 1, 'description': 'x', 'real_pixel_width': 20,
                    'real_pixel_height': 3, 'dpi_x': 4, 'dpi_y': 5, 'supports_rotation': False,
                },
            ]}),
            event_obj.json,
        )

        # Perform a different monitor configuration update, and ensure that the screen handler
        # correctly identifies the update.
        monitor_set_3: List[MockNativeMonitor] = [
            MockNativeMonitor(monitor.Monitor(7, 'x', 7, 12, 15, 99, False)),
            MockNativeMonitor(monitor.Monitor(17, 'y', 9, 8, 7, 6, False)),
        ]
        context.reset_mock()
        handler.ret__get_virtual_screen_for_monitors = virtual_screen.VirtualScreen([
            _create_virtual_screen_block(7, 12),
            _create_virtual_screen_block(9, 8),
        ])
        res = handler.detected_monitor_changed(monitor_set_3)
        self.assertIsNone(res.error)
        context.send_event.assert_called()
        self.assertEqual(2, len(context.send_event.call_args_list))

        call1_args = context.send_event.call_args_list[0].args
        self.assertEqual(call1_args[0], monitor.ActiveMonitorsState.UNIQUE_TARGET_FQN)
        self.assertEqual(call1_args[1], datastore_events.StoreDataEvent.UNIQUE_TARGET_FQN)
        event_obj = call1_args[2]
        self.assertIsInstance(event_obj, datastore_events.StoreDataEvent)
        assert isinstance(event_obj, datastore_events.StoreDataEvent)  # nosec  # mypy required
        self.assertEqual(
            json.dumps({'monitors': [
                {
                    'identifier': 7, 'description': 'x', 'real_pixel_width': 7,
                    'real_pixel_height': 12, 'dpi_x': 15, 'dpi_y': 99, 'supports_rotation': False,
                },
                {
                    'identifier': 17, 'description': 'y', 'real_pixel_width': 9,
                    'real_pixel_height': 8, 'dpi_x': 7, 'dpi_y': 6, 'supports_rotation': False,
                },
            ]}),
            event_obj.json,
        )

        call2_args = context.send_event.call_args_list[1].args
        self.assertEqual(call2_args[0], screen.VirtualScreenState.UNIQUE_TARGET_FQN)
        self.assertEqual(call2_args[1], datastore_events.StoreDataEvent.UNIQUE_TARGET_FQN)
        event_obj = call2_args[2]
        self.assertIsInstance(event_obj, datastore_events.StoreDataEvent)
        assert isinstance(event_obj, datastore_events.StoreDataEvent)  # nosec  # mypy required
        self.assertEqual(
            # This is based on the ret__get value set above.
            json.dumps({'area': [
                {
                    'nw_x_pixel': 0, 'nw_y_pixel': 0, 'width': 7, 'height': 12,
                    'ratio_x': 1, 'ratio_y': 1,
                },
                {
                    'nw_x_pixel': 0, 'nw_y_pixel': 0, 'width': 9, 'height': 8,
                    'ratio_x': 1, 'ratio_y': 1,
                },
            ]}),
            event_obj.json,
        )


def _create_virtual_screen_block(
        mon_w: int, mon_h: int,
        screen_id: int = 1,
) -> virtual_screen.VirtualScreenBlock:
    return virtual_screen.VirtualScreenBlock(
        (
            screen_id, defs.ZERO_MONITOR_UNIT, defs.ZERO_MONITOR_UNIT,
            cast(defs.MonitorUnit, mon_w), cast(defs.MonitorUnit, mon_h),
        ),
        (
            defs.ZERO_SCREEN_UNIT, defs.ZERO_SCREEN_UNIT,
            cast(defs.ScreenUnit, mon_w), cast(defs.ScreenUnit, mon_h),
        ),
        0,
    )


class MockNativeMonitor(monitor_screen.NativeMonitor):
    """Basic implementation."""

    def __init__(self, mon: monitor.Monitor) -> None:
        self.monitor = mon

    def get_petronia_monitor(self) -> monitor.Monitor:
        return self.monitor


class MockScreenHandler(monitor_screen.AbstractMonitorHandler[MockNativeMonitor]):
    """Captures input to the handler."""

    def __init__(
            self, context: EventRegistryContext,
            mapper: Optional[MockNativeMonitor] = None,
    ) -> None:
        monitor_screen.AbstractMonitorHandler.__init__(
            self, context, monitor_screen.WindowScreenMapper(
                [mapper or MockNativeMonitor(monitor.Monitor(
                    0, 'x', 600, 400, 96, 96, False,
                ))], virtual_screen.VirtualScreen([]),
            ),
        )
        self.args__get_virtual_screen_for_monitors: List[Sequence[MockNativeMonitor]] = []
        self.ret__get_virtual_screen_for_monitors = virtual_screen.VirtualScreen([])

    def get_virtual_screen_for_monitors(
            self, active: Sequence[MockNativeMonitor],
    ) -> virtual_screen.VirtualScreen:
        self.args__get_virtual_screen_for_monitors.append(active)
        return self.ret__get_virtual_screen_for_monitors
