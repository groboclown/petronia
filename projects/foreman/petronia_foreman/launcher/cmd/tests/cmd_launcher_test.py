"""Test the module."""

from typing import Dict, Optional, Any, cast
import unittest
import os
import sys
import tempfile
import shutil
import concurrent.futures
import threading
from configparser import ConfigParser
from petronia_common.event_stream import (
    EventForwarderTarget, RawBinaryReader, to_raw_event_object,
)
from petronia_common.event_stream.tests.shared import MockTarget
from petronia_common.util import PetroniaReturnError
from petronia_foreman.configuration import RuntimeConfig
from .. import cmd_launcher
from ... import AbcLauncherCategory
from ....configuration import platform
from ....event_router import EventRouter
from ....events import foreman
from ....routing.foreman_router import LauncherRuntimeContext


class CmdLauncherCategoryTest(unittest.TestCase):  # pylint:disable=too-many-instance-attributes
    """Test the CmdLauncherCategory class and the factory."""

    def setUp(self) -> None:
        platform.initial_setup(None)
        self.executor = concurrent.futures.ThreadPoolExecutor()
        self.lock = threading.Semaphore()
        self.mock_target = TargetWrapper(self)
        self.router = EventRouter(self.lock, self.mock_target, self.executor)
        self.tempdir = tempfile.mkdtemp()
        self.cat: Optional[AbcLauncherCategory] = None
        self._orig_platform_config = list(platform.configuration_paths)
        self._orig_platform_data = list(platform.data_paths)

    def tearDown(self) -> None:
        platform.configuration_paths.clear()
        platform.configuration_paths.extend(self._orig_platform_config)
        platform.data_paths.clear()
        platform.data_paths.extend(self._orig_platform_data)
        shutil.rmtree(self.tempdir, ignore_errors=True)
        for channel in self.router.get_registered_channel_names():
            self.router.close_channel(channel)
        if self.cat:
            self.cat.stop()
        self.executor.shutdown(wait=True)

    def test_safe_location_convert(self) -> None:
        """Test all kinds of combinations for the location conversion."""
        config_dir = os.path.join(self.tempdir, 'configs')
        os.makedirs(config_dir)
        data_dir = os.path.join(self.tempdir, 'data')
        os.makedirs(data_dir)
        platform.configuration_paths.clear()
        platform.configuration_paths.append(config_dir)
        platform.data_paths.clear()
        platform.data_paths.append(data_dir)
        config_dir_1 = os.path.join(config_dir, '1')
        os.makedirs(config_dir_1)
        data_dir_1 = os.path.join(data_dir, '1')
        os.makedirs(data_dir_1)
        config_file_1 = os.path.join(config_dir, 'x.txt')
        with open(config_file_1, 'w') as f:
            f.write('x')
        data_file_1 = os.path.join(data_dir, 'x.txt')
        with open(data_file_1, 'w') as f:
            f.write('x')

        res = cmd_launcher.safe_location_convert([])
        self.assertEqual((), res)

        res = cmd_launcher.safe_location_convert([os.path.abspath(os.curdir)])
        self.assertEqual((), res)

        res = cmd_launcher.safe_location_convert(['${DATA_PATH}/does-not-exist'])
        self.assertEqual((), res)

        res = cmd_launcher.safe_location_convert(['${CONFIG_PATH}/does-not-exist'])
        self.assertEqual((), res)

        res = cmd_launcher.safe_location_convert(['${DATA_PATH}/x.txt'])
        self.assertEqual((data_file_1,), res)

        res = cmd_launcher.safe_location_convert(['${CONFIG_PATH}/x.txt'])
        self.assertEqual((config_file_1,), res)

        res = cmd_launcher.safe_location_convert(['${DATA_PATH}/1'])
        self.assertEqual((data_dir_1,), res)

        res = cmd_launcher.safe_location_convert(['${CONFIG_PATH}/1'])
        self.assertEqual((config_dir_1,), res)

        res = cmd_launcher.safe_location_convert([
            '${DATA_PATH}/1', '${CONFIG_PATH}/1', '${DATA_PATH}/x.txt', os.curdir,
        ])
        self.assertEqual((data_dir_1, config_dir_1, data_file_1), res)

    def test_uninitialized_functionality(self) -> None:
        """Test the functionality of the category before it's initialized."""
        self.cat = cmd_launcher.create_cmd_launcher(_mk_config())
        self.assertEqual((), self.cat.get_active_handler_ids())
        res = self.cat.stop()
        self.assertIsNone(res.error)
        res = self.cat.stop_extension('h1')
        self.assertIsNotNone(res.error)
        res = self.cat.is_valid()
        self.assertIsNone(res.error)
        res = self.cat.start_extension('e1', foreman.LauncherStartExtensionRequestEvent(
            'n1', [1, 0, 0], [], 'r1', foreman.SendEventAccess([], []), None, [],
        ))
        self.assertIsNotNone(res.error)

    def test_py_handler_use_case_1(self) -> None:
        """Test the start + send + receive + end functionality with an explicit extension
        exit before the stop request is sent."""
        self.cat = cast(
            cmd_launcher.CmdLauncherCategory,
            cmd_launcher.create_cmd_launcher(_mk_config(
                exe='py', module='petronia_foreman.process_mgmt.tests.runner',
                path=os.pathsep.join(sys.path), args='${WRITE_FD}',
            )),
        )
        # Setup the target anew, in case anything is sitting in it.
        self.mock_target.proxy = MockTarget(self)
        self.mock_target.proxy.can_handle_returns.append(True)
        self.mock_target.proxy.handle_returns.append(False)
        res = self.cat.initialize(LauncherRuntimeContext(self.router, self.executor))
        self.assertIsNone(res.error)
        res = self.cat.start_extension('ch1', foreman.LauncherStartExtensionRequestEvent(
            'ext1', [1, 2, 3],
            sys.path, 'launcher',
            foreman.SendEventAccess(['ev1'], ['ext1:']), None, [],
        ))
        self.assertIsNone(res.error)
        self.assertEqual(('ch1',), self.router.get_registered_channel_names())
        b_res = self.router.add_handler_listener('ch1', 'ev1', 'ext1:b')
        self.assertTrue(b_res)
        res = self.router.inject_event_to_channel(
            'ch1', to_raw_event_object('ev1', 'ext1:a', 'ext1:b', {}),
        )
        self.assertIsNone(res.error)

        # For the proper use case, we want to leave the process running until we
        # explicitly stop it, but that isn't reliable on all platforms.
        self.assertTrue(self.cat.wait_for_process_to_end('ch1', 10.0))

        # This is ensuring that the executed command sent this data, not that the event
        # was injected.
        self.mock_target.proxy.assert_next_can_handle('ev1', 'ext1:a', 'ext1:b')
        self.mock_target.proxy.assert_next_handle('ev1', 'ext1:a', 'ext1:b', {})
        # The category has stopped, because we waited for the process to end.
        self.mock_target.proxy.assert_next_on_eof()
        self.mock_target.proxy.assert_end()

        # Removing the handler after it has stopped fails, because it is already stopped.
        b_res = self.router.remove_handler('ch1')
        self.assertFalse(b_res)

        # Closing the channel after it has stopped fails, because it is already stopped.
        b_res = self.router.close_channel('ch1')
        self.assertFalse(b_res)

        self.cat.stop()

        # Because the category was stopped, an EOF is added to the stream.
        self.mock_target.proxy.assert_end()


def _mk_config(**config_args: str) -> RuntimeConfig:
    config = ConfigParser()
    config.add_section('launcher')
    config.set('launcher', 'runner', 'cmd-launcher')
    for key, val in config_args.items():
        config.set('launcher', key, val)
    return RuntimeConfig('launcher', config)


class TargetWrapper(EventForwarderTarget):
    """Wraps another target."""

    def __init__(self, base_test: unittest.TestCase) -> None:
        self.proxy: MockTarget = MockTarget(base_test)

    def can_consume(self, event_id: str, source_id: str, target_id: str) -> bool:
        return self.proxy.can_consume(event_id, source_id, target_id)

    def on_error(self, error: PetroniaReturnError) -> bool:
        return self.proxy.on_error(error)

    def on_eof(self) -> None:
        self.proxy.on_eof()

    def consume_object(
            self, event_id: str, source_id: str, target_id: str, event_data: Dict[str, Any],
    ) -> bool:
        return self.proxy.consume_object(event_id, source_id, target_id, event_data)

    def consume_binary(
            self, event_id: str, source_id: str, target_id: str, size: int,
            data_reader: RawBinaryReader,
    ) -> bool:
        return self.proxy.consume_binary(event_id, source_id, target_id, size, data_reader)
