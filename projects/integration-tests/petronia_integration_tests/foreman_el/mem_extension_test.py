"""Load an extension."""

import unittest
import os
import tempfile
import shutil
import sys
import json
import threading
from configparser import ConfigParser
from petronia_foreman.configuration import platform, ForemanConfig
from petronia_foreman.configuration.foreman import BOOT_SECTION
from petronia_foreman.foreman_runner import ForemanRunner
from petronia_integration_tests.foreman_el.integration1.entrypoint import (
    wait_for_extension_alive, reset_extension,
)

# Seconds before the test times out and exits with an error.
# If you're debugging, set this to a large-enough number, like
# 5 hours.
TEST_TIMEOUT_SECONDS = 10.0
# TEST_TIMEOUT_SECONDS = 60.0 * 60.0 * 5.0


class MemoryExtensionTest(unittest.TestCase):
    """Load an extension using the memory launcher,
    starting with an event to the extension loader."""
    def setUp(self) -> None:
        self.tempdir = tempfile.mkdtemp()
        os.makedirs(os.path.join(self.tempdir, 'configs'))
        os.makedirs(os.path.join(self.tempdir, 'data', 'extensions'))
        os.makedirs(os.path.join(self.tempdir, 'data', 'boot-extensions'))
        platform_settings_res = platform.initial_setup(None)
        self.assertIsNone(platform_settings_res.error)
        platform.configuration_paths = [os.path.join(self.tempdir, 'configs')]
        platform.data_paths = [os.path.join(self.tempdir, 'data')]
        self.foreman_config = ForemanConfig()
        with open(os.path.join(
                self.tempdir, 'data', 'boot-extensions', 'extension-loader.json',
        ), 'w') as f:
            json.dump({
                'name': 'petronia.core.impl.extension_loader',
                'version': [1, 0, 0],
                'runtime': {
                    'launcher': 'extension-loader',
                    'permissions': {},
                },
                'produces': [
                    'petronia.core.api.foreman:launcher-start-extension:request',
                    'petronia.core.api.foreman:extension-add-event-listener',
                ],
                'source-prefixes': [
                    'petronia.core.api.extension_loader:',
                    'petronia.core.impl.extension_loader:',
                ],
                'consumes': [
                    {'event-id': 'petronia.core.api.foreman:launcher-start-extension:success'},
                    {'event-id': 'petronia.core.api.foreman:launcher-start-extension:failed'},
                ],
                'configuration': {},
            }, f)
        config = ConfigParser()
        config.add_section(BOOT_SECTION)
        config.set(BOOT_SECTION, 'boot-file-order', 'extension-loader.json')
        config.add_section('extension-loader')
        config.set('extension-loader', 'runner', 'in-memory')
        config.set('extension-loader', 'arg.1', '${CONFIG_PATH}')
        config.set('extension-loader', 'arg.2', os.pathsep.join([
            '${DATA_PATH}',
            # Include python path, so it loads the internal extension.
            *sys.path,
        ]),)
        config.set('extension-loader', 'arg.3', '${TEMP_DIR}')
        config.set('extension-loader', 'arg.4', 'extension-loader')  # launcher_id

        with open(os.path.join(self.tempdir, 'configs', 'config.json'), 'w') as f:
            json.dump({
                'startup': {
                    'extensions': ['petronia_integration_tests.foreman_el.integration1'],
                    'extension-dirs': sys.path,
                },
            }, f)

        config.add_section('integration')
        config.set('integration', 'runner', 'in-memory')
        # config.set('integration', 'module', 'petronia_extension_runner.entrypoint')
        # config.set('integration', 'entrypoint', 'entrypoint')

        self.foreman_config.load_config(config)
        self.foreman_runner = ForemanRunner(self.foreman_config)

    def tearDown(self) -> None:
        print("Starting shutdown")
        self.foreman_runner.shutdown()
        print("Joining runner threads")
        self.foreman_runner.join()
        print("Runner threads complete")
        shutil.rmtree(self.tempdir, ignore_errors=True)
        print("Running threads:")
        for thread in threading.enumerate():
            print(" - " + thread.name + ": alive? " + str(thread.is_alive()))
        reset_extension()

    def test_load_extension(self) -> None:
        """Load the extension."""
        self.assertEqual(0, self.foreman_runner.initialize())
        self.assertEqual(0, self.foreman_runner.boot())
        print("Boot complete")

        self.assertTrue(wait_for_extension_alive(TEST_TIMEOUT_SECONDS))
