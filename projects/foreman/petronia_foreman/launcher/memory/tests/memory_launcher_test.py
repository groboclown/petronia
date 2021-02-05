"""Test the module."""

from typing import Optional
import unittest
import concurrent.futures
import threading
import tempfile
import shutil
import time
from configparser import ConfigParser
from petronia_common.event_stream import to_raw_event_object
from petronia_common.event_stream.tests.shared import MockTarget
from petronia_foreman.configuration import RuntimeConfig
from . import entrypoint
from .. import memory_launcher
from ... import AbcLauncherCategory, RuntimeContext
from ...cmd.tests.cmd_launcher_test import TargetWrapper
from ....event_router import EventRouter
from ....events import foreman
from ....routing.foreman_router import LauncherRuntimeContext


class MemoryLauncherCategoryTest(unittest.TestCase):
    """Test the CmdLauncherCategory class and the factory."""

    def setUp(self) -> None:
        self.executor = concurrent.futures.ThreadPoolExecutor()
        self.lock = threading.Semaphore()
        self.mock_target = TargetWrapper(self)
        self.router = EventRouter(self.lock, self.mock_target, self.executor)
        self.tempdir = tempfile.mkdtemp()
        self.cat: Optional[AbcLauncherCategory] = None
        entrypoint.reset_extension()

    def tearDown(self) -> None:
        shutil.rmtree(self.tempdir, ignore_errors=True)
        for channel in self.router.get_registered_channel_names():
            self.router.close_channel(channel)
        if self.cat:
            self.cat.stop()
        self.executor.shutdown(wait=True)

    def test_uninitialized_functionality(self) -> None:
        """Test the functionality of the category before it's initialized."""
        cat = memory_launcher.create_memory_launcher(_mk_config())
        self.assertEqual((), cat.get_active_handler_ids())
        res = cat.stop()
        self.assertIsNone(res.error)
        res = cat.stop_extension('h1')
        self.assertIsNotNone(res.error)
        res = cat.is_valid()
        self.assertIsNone(res.error)
        res = cat.start_extension('e1', foreman.LauncherStartExtensionRequestEvent(
            'n1', [1, 0, 0], [], 'r1', foreman.SendEventAccess([], []), None, [],
        ))
        self.assertIsNotNone(res.error)
        res = cat.stop()
        self.assertIsNone(res.error)

        # stop -> initialize causes an error.
        res = cat.initialize(RuntimeContext())
        self.assertIsNotNone(res.error)
        self.assertEqual(
            ['Launcher already stopped'],
            [m.debug() for m in res.error_messages()],
        )

    def test_invalid_setup(self) -> None:
        """Test the is_valid with an invalid setup."""
        cat = memory_launcher.create_memory_launcher(_mk_config(**{
            memory_launcher.WAIT_FOR_EXTENSION_LOAD_TIMEOUT_OPTION: 'x',
        }))
        res = cat.is_valid()
        self.assertIsNotNone(res.error)
        self.assertEqual(
            ['Invalid option extension-load-timeout; must be a number, found x'],
            [m.debug() for m in res.error_messages()],
        )

    def test_standard_use_case(self) -> None:
        """Test the standard run-an-extension use case."""
        self.cat = memory_launcher.create_memory_launcher(_mk_config())
        # Setup the target anew, in case anything is sitting in it.
        self.mock_target.proxy = MockTarget(self)
        self.mock_target.proxy.can_handle_returns.append(True)
        self.mock_target.proxy.handle_returns.append(False)
        res = self.cat.initialize(LauncherRuntimeContext(self.router, self.executor))
        self.assertIsNone(res.error)
        res = self.cat.start_extension('ch1', foreman.LauncherStartExtensionRequestEvent(
            'petronia_foreman.launcher.memory.tests.entrypoint', [1, 2, 3], [], 'launcher',
            foreman.SendEventAccess(['ev1'], ['ext1:']), None, [],
        ))
        self.assertIsNone(res.error)
        self.assertEqual(('ch1',), self.router.get_registered_channel_names())
        b_res = self.router.add_handler_listener('ch1', 'ev1', 'ext1:b')
        self.assertTrue(b_res)

        self.assertTrue(entrypoint.wait_for_extension_started(2.0))

        res = self.router.inject_event_to_channel(
            'ch1', to_raw_event_object('ev1', 'ext1:a', 'ext1:b', {}),
        )
        self.assertIsNone(res.error)

        self.assertTrue(entrypoint.wait_for_extension_stopped(2.0))

        # Still need to wait for the router read threads to do their job.
        # This is the only real way at the moment to do that.  Sigh.
        time.sleep(2.0)

        b_res = self.router.remove_handler('ch1')
        self.assertTrue(b_res)
        b_res = self.router.close_channel('ch1')
        self.assertTrue(b_res)

        # This is ensuring that the executed command sent this data, not that the event
        # was injected.
        self.mock_target.proxy.assert_next_can_handle('ev1', 'ext1:a', 'ext1:b')
        self.mock_target.proxy.assert_next_handle('ev1', 'ext1:a', 'ext1:b', {})

        # An EOF is explicitly not sent to the target, because the target is for all of the
        # router, not just a single channel.
        # self.mock_target.proxy.assert_next_on_eof()

        self.mock_target.proxy.assert_end()

        self.assertTrue(entrypoint.is_extension_stopped())


def _mk_config(**config_args: str) -> RuntimeConfig:
    config = ConfigParser()
    config.add_section('launcher')
    config.set('launcher', 'runner', 'in-memory')
    for key, val in config_args.items():
        config.set('launcher', key, val)
    return RuntimeConfig('launcher', config)
