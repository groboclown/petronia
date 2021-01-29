"""Test the module."""

import unittest
from configparser import ConfigParser
from .. import foreman


class ForemanConfigTest(unittest.TestCase):
    """Test the ForemanConfig class."""

    def test__load_config__multiple_empty(self) -> None:
        """Load an empty configuration file."""
        fcg = foreman.ForemanConfig()
        res = fcg.load_config(ConfigParser(), ConfigParser())
        self.assertTrue(res.ok)
        # ensure the boot config is non-null and working.
        boot = fcg.get_boot_config()
        self.assertTrue(boot.is_signals_enabled())

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
        l_c = fcg.get_runtime_config('bad-launcher')
        # Even though the launcher is bad, it still has a configuration.
        self.assertTrue(l_c.has_error)
        self.assertIsNotNone(fcg.get_runtime_config('not-exist').error)

    def test__load_config__good_launchers(self) -> None:
        """Test load_config with good launcher definitions."""
        fcg = foreman.ForemanConfig()
        config_file = ConfigParser()
        config_file.add_section('good-launcher-1')
        config_file.set('good-launcher-1', 'runner', 'runner 1')
        config_file.set('good-launcher-1', 'other', 'tuna')
        config_file.add_section('good-launcher-2')
        config_file.set('good-launcher-2', 'runner', 'runner 2')
        res = fcg.load_config(config_file)
        self.assertTrue(res.ok)
        launchers = fcg.get_registered_runtime_config_names()
        self.assertEqual(
            ['good-launcher-1', 'good-launcher-2'],
            sorted(list(launchers)),
        )
        lc1 = fcg.get_runtime_config('good-launcher-1')
        self.assertTrue(lc1.ok)
        self.assertEqual('runner 1', lc1.result.runner)
        self.assertEqual('good-launcher-1', lc1.result.runtime_name)
        self.assertEqual('tuna', lc1.result.get_option('other').result)
        self.assertTrue(lc1.result.get_option('tuna').has_error)

        lc2 = fcg.get_runtime_config('good-launcher-2')
        self.assertTrue(lc2.ok)

    def test__load_config__boot(self) -> None:
        """Test load_config with good launcher definitions."""
        fcg = foreman.ForemanConfig()
        config_file = ConfigParser()
        config_file.add_section('foreman')
        config_file.set('foreman', 'boot-file-order', 'x, a, b, c')
        config_file.set('foreman', 'root-log-file', 'log file')
        res = fcg.load_config(config_file)
        self.assertIsNone(res.error)
        boot = fcg.get_boot_config()
        self.assertEqual(
            ('x', 'a', 'b', 'c'),
            boot.boot_file_order,
        )
        self.assertEqual(
            'log file',
            boot.root_log_file,
        )
        self.assertEqual(True, boot.is_signals_enabled())
        boot.set_signals_enabled(False)
        self.assertEqual(False, boot.is_signals_enabled())
        boot.set_signals_enabled(True)
        self.assertEqual(True, boot.is_signals_enabled())
