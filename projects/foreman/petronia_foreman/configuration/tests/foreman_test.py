"""Test the module."""

import unittest
from configparser import ConfigParser
from .. import foreman
from ..platform import detect_platform
from ..launcher_parameters import BOOT_CHANNEL_OPTION, is_boot_launcher


class ForemanConfigTest(unittest.TestCase):
    """Test the ForemanConfig class."""

    def test__load_config__multiple_empty(self) -> None:
        """Load an empty configuration file."""
        fcg = foreman.ForemanConfig()
        res = fcg.load_config(ConfigParser(), ConfigParser())
        self.assertTrue(res.ok)
        # ensure the boot config is non-null and working.
        boot = fcg.get_boot_config()
        platform = detect_platform(None)
        self.assertEqual(
            platform.result.native_launcher_name,
            boot.get_native_launcher(platform.result),
        )

    def test__load_config__bad_launchers(self) -> None:
        """Test load_config with bad launcher definitions."""
        fcg = foreman.ForemanConfig()
        config_file = ConfigParser()
        config_file.add_section('bad-launcher')
        config_file.set('bad-launcher', 'bad-runner', 'bad-value')
        res = fcg.load_config(config_file)
        self.assertIsNotNone(res.error)
        message = ';'.join([msg.debug() for msg in res.valid_error.messages()])
        self.assertEqual('`runner` not specified for launcher bad-launcher', message)
        l_c = fcg.get_launcher_config('bad-launcher')
        # Even though the launcher is bad, it still has a configuration.
        self.assertTrue(l_c.has_error)
        self.assertIsNotNone(fcg.get_launcher_config('not-exist').error)

    def test__load_config__good_launchers(self) -> None:
        """Test load_config with good launcher definitions."""
        fcg = foreman.ForemanConfig()
        config_file = ConfigParser()
        config_file.add_section('good-launcher-1')
        config_file.set('good-launcher-1', 'runner', 'runner 1')
        config_file.set('good-launcher-1', 'other', 'tuna')
        config_file.add_section('good-launcher-2')
        config_file.set('good-launcher-2', 'runner', 'runner 2')
        config_file.set('good-launcher-2', BOOT_CHANNEL_OPTION, 'some-boot-channel')
        res = fcg.load_config(config_file)
        self.assertTrue(res.ok)
        launchers = fcg.get_registered_launcher_config_names()
        self.assertEqual(
            ['good-launcher-1', 'good-launcher-2'],
            sorted(list(launchers)),
        )
        lc1 = fcg.get_launcher_config('good-launcher-1')
        self.assertTrue(lc1.ok)
        self.assertEqual('runner 1', lc1.result.runner)
        self.assertIsNone(lc1.result.boot_channel)
        self.assertFalse(is_boot_launcher(lc1.result.options))
        self.assertEqual('good-launcher-1', lc1.result.launcher_name)
        self.assertEqual('tuna', lc1.result.get_option('other').result)
        self.assertTrue(lc1.result.get_option('tuna').has_error)

        lc2 = fcg.get_launcher_config('good-launcher-2')
        self.assertTrue(lc2.ok)
        self.assertEqual('some-boot-channel', lc2.result.boot_channel)
        self.assertTrue(is_boot_launcher(lc2.result.options))

    def test__load_config__boot(self) -> None:
        """Test load_config with good launcher definitions."""
        fcg = foreman.ForemanConfig()
        config_file = ConfigParser()
        config_file.add_section('boot')
        config_file.set('boot', 'boot-order', 'x, a, b, c')
        config_file.set('boot', 'root-log-file', 'log file')
        config_file.set('boot', 'native-launcher', 'xyz')
        res = fcg.load_config(config_file)
        self.assertTrue(res.ok)
        boot = fcg.get_boot_config()
        self.assertEqual(
            ('x', 'a', 'b', 'c'),
            boot.boot_order,
        )
        self.assertEqual(
            'log file',
            boot.root_log_file,
        )
        self.assertEqual(
            'xyz',
            boot.get_native_launcher(detect_platform(None).result),
        )
        self.assertEqual(True, boot.is_signals_enabled())
        boot.set_signals_enabled(False)
        self.assertEqual(False, boot.is_signals_enabled())
        boot.set_signals_enabled(True)
        self.assertEqual(True, boot.is_signals_enabled())
