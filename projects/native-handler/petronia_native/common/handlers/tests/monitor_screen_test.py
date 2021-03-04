"""Test the module"""

from typing import Sequence, List, Tuple, cast
import unittest
import unittest.mock
import json
from petronia_common.util import RET_OK_NONE, possible_error, not_none, UserMessage, i18n, StdRet
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


class AbstractScreenHandlerTest(unittest.TestCase):
    """Test the AbstractScreenHandler class."""

    def test_closed(self) -> None:
        """Test the functions when the instance is closed."""
        context = unittest.mock.Mock(EventRegistryContext())
        handler = monitor_screen.AbstractScreenHandler(context)
        handler.close()
        res = handler.detected_monitor_changed([])
        self.assertIsNone(res.error)
        res = handler.on_configuration_update(None, -1, [])
        self.assertIsNone(res.error)

    def test_detected_monitor_changed(self) -> None:  # pylint:disable=too-many-statements
        """Test detected_monitor_changed."""
        context = unittest.mock.Mock(EventRegistryContext())
        context.send_event.return_value = RET_OK_NONE
        handler = MockScreenHandler(context)
        monitor_set_1 = [
            monitor.Monitor(1, 'x', 2, 3, 4, 5, False),
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
                    'nw_x_pixel': 0, 'nw_y_pixel': 0, 'width': 2, 'height': 3,

                    # This ratio isn't right; it need to take DPI into account.
                    'ratio_x': 1, 'ratio_y': 1,
                },
            ]}),
            event_obj.json,
        )

        # Perform the same update, and ensure that the screen handler correctly ignored the
        # update.
        monitor_set_2 = [
            monitor.Monitor(1, 'x', 2, 3, 4, 5, False),
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
                    'identifier': 1, 'description': 'x', 'real_pixel_width': 2,
                    'real_pixel_height': 3, 'dpi_x': 4, 'dpi_y': 5, 'supports_rotation': False,
                },
            ]}),
            event_obj.json,
        )

        # Perform a different monitor configuration update, and ensure that the screen handler
        # correctly identifies the update.
        monitor_set_3 = [
            monitor.Monitor(7, 'x', 7, 12, 15, 99, False),
            monitor.Monitor(17, 'y', 9, 8, 7, 6, False),
        ]
        context.reset_mock()
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
            json.dumps({'area': [
                {
                    'nw_x_pixel': 0, 'nw_y_pixel': 0, 'width': 7, 'height': 12,
                    'ratio_x': 1, 'ratio_y': 1,
                },
                {
                    'nw_x_pixel': 7, 'nw_y_pixel': 0, 'width': 9, 'height': 8,
                    'ratio_x': 1, 'ratio_y': 1,
                },
            ]}),
            event_obj.json,
        )

    def test_on_configuration_update(self) -> None:
        """Test the on_configuration_update method."""
        context = unittest.mock.Mock(EventRegistryContext())
        context.send_event.return_value = RET_OK_NONE
        handler = MockScreenHandler(context)
        # Setup the initial monitors
        monitor_set = [
            monitor.Monitor(7, 'x', 7, 12, 15, 99, False),
            monitor.Monitor(17, 'y', 9, 8, 7, 6, False),
        ]
        res = handler.detected_monitor_changed(monitor_set)
        self.assertIsNone(res.error)
        context.reset_mock()

        res = handler.on_configuration_update(
            's1', 12, [
                virtual_screen.VirtualScreenConfig(
                    'not-used',
                    [(7, defs.MonitorUnit(7), defs.MonitorUnit(12))],
                    virtual_screen.VirtualScreen([
                        virtual_screen.VirtualScreenBlock(
                            (
                                7, defs.MonitorUnit(0), defs.MonitorUnit(0),
                                defs.MonitorUnit(7), defs.MonitorUnit(12),
                            ),
                            (
                                defs.ScreenUnit(0), defs.ScreenUnit(0),
                                defs.ScreenUnit(7), defs.ScreenUnit(12),
                            ),
                            0,
                        )
                    ]),
                ),
                virtual_screen.VirtualScreenConfig(
                    'used',
                    [
                        (7, defs.MonitorUnit(7), defs.MonitorUnit(12)),
                        (17, defs.MonitorUnit(9), defs.MonitorUnit(8)),
                    ],
                    virtual_screen.VirtualScreen([
                        virtual_screen.VirtualScreenBlock(
                            (
                                7, defs.MonitorUnit(1), defs.MonitorUnit(2),
                                defs.MonitorUnit(5), defs.MonitorUnit(8),
                            ),
                            (
                                defs.ScreenUnit(0), defs.ScreenUnit(0),
                                defs.ScreenUnit(5), defs.ScreenUnit(8),
                            ),
                            0,
                        ),
                        virtual_screen.VirtualScreenBlock(
                            (
                                17, defs.MonitorUnit(0), defs.MonitorUnit(1),
                                defs.MonitorUnit(8), defs.MonitorUnit(2),
                            ),
                            (
                                defs.ScreenUnit(2), defs.ScreenUnit(8),
                                defs.ScreenUnit(8), defs.ScreenUnit(2),
                            ),
                            0,
                        ),
                    ]),
                )
            ],
        )
        self.assertIsNone(res.error)
        calls = context.send_event.call_args_list
        self.assertEqual(3, len(calls))


class MockScreenHandler(monitor_screen.AbstractScreenHandler):
    """Captures input to the handler."""

    def __init__(self, context: EventRegistryContext) -> None:
        monitor_screen.AbstractScreenHandler.__init__(self, context)
        self.args__on_screen_configuration_settings_changed: List[Tuple[
            EventRegistryContext, Sequence[virtual_screen.VirtualScreenConfig],
        ]] = []
        self.ret__on_screen_configuration_settings_changed: StdRet[None] = RET_OK_NONE
        self.args__callback_virtual_screen_update: List[Tuple[
            EventRegistryContext, virtual_screen.VirtualScreen,
        ]] = []
        self.ret__callback_virtual_screen_update: StdRet[None] = RET_OK_NONE

    def on_screen_configuration_settings_changed(
            self, context: EventRegistryContext,
            screen_configs: Sequence[virtual_screen.VirtualScreenConfig],
    ) -> StdRet[None]:
        self.args__on_screen_configuration_settings_changed.append(
            (context, screen_configs)
        )
        return self.ret__on_screen_configuration_settings_changed

    def callback_virtual_screen_update(
            self, context: EventRegistryContext,
            active_screen: virtual_screen.VirtualScreen,
    ) -> StdRet[None]:
        self.args__callback_virtual_screen_update.append((context, active_screen))
        return self.ret__callback_virtual_screen_update
