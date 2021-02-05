"""Tests the module."""

from typing import List
import unittest
import os
import time
import threading
import tempfile
import shutil
import configparser
from .. import foreman_runner
from ..configuration import ForemanConfig, platform
from ..configuration.foreman import BOOT_SECTION

LAUNCH_TIMEOUT_SECONDS = 2.0


class ForemanRunnerTest(unittest.TestCase):
    """Test the ForemanRunner class."""

    def setUp(self) -> None:
        self.threads: List[threading.Thread] = []
        self.tempdir = tempfile.mkdtemp()

    def tearDown(self) -> None:
        shutil.rmtree(self.tempdir, ignore_errors=True)
        for thread in self.threads:
            thread.join(timeout=2.0)

    def test__before_startup(self) -> None:
        """Test different functionality before startup happens."""
        platform_res = platform.initial_setup(None)
        self.assertIsNone(platform_res.error)
        conf = configparser.ConfigParser()
        conf.add_section(BOOT_SECTION)
        foreman_config = ForemanConfig()
        res = foreman_config.load_config(conf)
        self.assertIsNone(res.error)
        runner = foreman_runner.ForemanRunner(foreman_config)
        runner.join()
        self.assertRaisesRegex(
            AttributeError,
            r'can only be run after booted and not stopping',
            runner.start_restart,
        )

    def test_valid__no_log_file(self) -> None:
        """Test the standard use case of the runner with everything ok, with no log file."""
        platform_res = platform.initial_setup(None)
        self.assertIsNone(platform_res.error)
        conf = configparser.ConfigParser()
        conf.add_section(BOOT_SECTION)
        foreman_config = ForemanConfig()
        res = foreman_config.load_config(conf)
        self.assertIsNone(res.error)
        foreman_config.get_boot_config().set_signals_enabled(False)
        runner = foreman_runner.ForemanRunner(foreman_config)

        def runner_func() -> None:
            self.assertEqual(0, runner.run())

        thread = threading.Thread(target=runner_func, name='foreman runner', daemon=True)
        self.threads.append(thread)
        thread.start()
        _wait_until_running(self, runner)
        runner.start_restart()
        runner.start_shutdown()
        thread.join(timeout=2.0)

    def test_invalid_log_file(self) -> None:
        """Test the standard use case of the runner with an invalid log file."""
        bad_log_file = os.path.join(self.tempdir, 'does-not-exist', 'log.txt')
        platform_res = platform.initial_setup(None)
        self.assertIsNone(platform_res.error)
        conf = configparser.ConfigParser()
        conf.add_section(BOOT_SECTION)
        conf.set(BOOT_SECTION, 'root-log-file', bad_log_file)
        foreman_config = ForemanConfig()
        res = foreman_config.load_config(conf)
        self.assertIsNone(res.error)
        runner = foreman_runner.ForemanRunner(foreman_config)

        self.assertEqual(1, runner.run())

    def test_valid_log_file(self) -> None:
        """Test the standard use case of the runner with everything ok, with no log file."""
        log_file = os.path.join(self.tempdir, 'log.txt')
        platform_res = platform.initial_setup(None)
        self.assertIsNone(platform_res.error)
        conf = configparser.ConfigParser()
        conf.add_section(BOOT_SECTION)
        conf.set(BOOT_SECTION, 'root-log-file', log_file)
        conf.add_section('runner1')
        conf.set('runner1', 'runner', 'invalid')
        foreman_config = ForemanConfig()
        res = foreman_config.load_config(conf)
        self.assertIsNone(res.error)
        runner = foreman_runner.ForemanRunner(foreman_config)

        def runner_func() -> None:
            self.assertEqual(0, runner.run())

        thread = threading.Thread(target=runner_func, name='foreman runner', daemon=True)
        self.threads.append(thread)
        thread.start()
        _wait_until_running(self, runner)
        runner.start_shutdown()
        thread.join(timeout=2.0)

    def test_invalid_launcher_config(self) -> None:
        """Test the standard use case of the runner with an invalid log file."""
        platform_res = platform.initial_setup(None)
        self.assertIsNone(platform_res.error)
        conf = configparser.ConfigParser()
        conf.add_section(BOOT_SECTION)
        conf.add_section('invalid')
        foreman_config = ForemanConfig()
        res = foreman_config.load_config(conf)
        # We want the configuration to have an error, because that puts the run in the right
        # state for this test.
        self.assertIsNotNone(res.error)
        runner = foreman_runner.ForemanRunner(foreman_config)

        self.assertEqual(2, runner.run())

    def test_invalid_boot_extension_config(self) -> None:
        """Test the standard use case of the runner with an invalid log file."""
        platform_res = platform.initial_setup(None)
        self.assertIsNone(platform_res.error)
        conf = configparser.ConfigParser()
        conf.add_section(BOOT_SECTION)
        conf.set(BOOT_SECTION, 'boot-file-order', 'does-not-exist.json')
        foreman_config = ForemanConfig()
        res = foreman_config.load_config(conf)
        self.assertIsNone(res.error)
        runner = foreman_runner.ForemanRunner(foreman_config)

        self.assertEqual(3, runner.run())


def _wait_until_running(test: unittest.TestCase, runner: foreman_runner.ForemanRunner) -> None:
    expires = time.time() + LAUNCH_TIMEOUT_SECONDS
    while time.time() < expires and not runner.is_router_running():
        time.sleep(0.2)
    test.assertTrue(runner.is_router_running())
