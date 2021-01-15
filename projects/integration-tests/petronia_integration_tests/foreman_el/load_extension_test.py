"""Load an extension."""

import unittest
import os
import tempfile
import shutil
import sys
import json
import threading
from configparser import ConfigParser
from petronia_foreman.configuration import detect_platform, ForemanConfig
from petronia_foreman.configuration.foreman import BOOT_SECTION
from petronia_foreman.foreman_runner import ForemanRunner
from petronia_integration_tests.foreman_el.launcher.entrypoint import (
    wait_for_launcher_alive, reset_launcher,
)


class LoadExtensionTest(unittest.TestCase):
    """Load an extension, starting with an event to the extension loader."""
    def setUp(self) -> None:
        self.tempdir = tempfile.mkdtemp()
        os.makedirs(os.path.join(self.tempdir, 'configs'))
        os.makedirs(os.path.join(self.tempdir, 'data', 'extensions'))
        platform_settings_res = detect_platform(None)
        self.assertIsNone(platform_settings_res.error)
        self.platform_settings = platform_settings_res.result
        self.platform_settings.config_paths = (os.path.join(self.tempdir, 'configs'),)
        self.platform_settings.data_paths = (os.path.join(self.tempdir, 'data'),)
        self.foreman_config = ForemanConfig()
        config = ConfigParser()
        config.add_section(BOOT_SECTION)
        config.set(BOOT_SECTION, 'boot-order', 'extension-loader')
        config.set(BOOT_SECTION, 'native-launcher', 'native')
        config.add_section('extension-loader')
        config.set('extension-loader', 'runner', 'in-memory')
        config.set('extension-loader', 'boot-channel', 'extension-loader')
        config.set('extension-loader', 'module', 'petronia_extension_loader.entrypoint')
        config.set('extension-loader', 'entrypoint', 'entrypoint')
        config.set('extension-loader', 'arg.1', '${CONFIG_PATH}')
        config.set('extension-loader', 'arg.2', os.pathsep.join([
            '${DATA_PATH}',
            # Include python path, so it loads the internal extension.
            *sys.path,
        ]),)
        config.set('extension-loader', 'arg.3', '${TEMP_DIR}')
        config.set('extension-loader', 'arg.4', 'extension-loader')  # launcher_id
        config.set(
            'extension-loader', 'boot-launcher-produces-event.1',
            'petronia.core.api.datastore:data-update',
        )
        config.set(
            'extension-loader', 'boot-launcher-produces-event.2',
            'petronia.core.api.extension_loader:load-extension:success',
        )
        config.set(
            'extension-loader', 'boot-launcher-produces-event.3',
            'petronia.core.api.extension_loader:load-extension:failed',
        )
        config.set(
            'extension-loader', 'boot-launcher-produces-event.4',
            'petronia.core.api.extension_loader:system-started',
        )
        config.set(
            'extension-loader', 'boot-launcher-produces-event.5',
            'petronia.core.api.foreman:start-launcher:request',
        )
        config.set(
            'extension-loader', 'boot-launcher-produces-event.6',
            'petronia.core.api.foreman:launcher-load-extension:request',
        )
        config.set(
            'extension-loader', 'boot-launcher-produces-event.7',
            'petronia.core.api.foreman:extension-add-event-listener',
        )
        config.set(
            'extension-loader', 'boot-launcher-produces-event.8',
            'petronia.core.api.foreman:extension-remove-event-listener',
        )

        config.add_section('native')
        config.set('native', 'runner', 'in-memory')
        config.set('native', 'boot-channel', 'native')
        config.set('native', 'module', 'petronia_integration_tests.foreman_el.launcher.entrypoint')
        config.set('native', 'entrypoint', 'entrypoint')
        config.set('native', 'arg.1', 'native')
        with open(os.path.join(self.tempdir, 'configs', 'config.json'), 'w') as f:
            json.dump({
                'startup': {
                    'extensions': ['petronia_integration_tests.foreman_el.integration1'],
                    'extension-dirs': sys.path,
                },
            }, f)
        config.add_section('integration')
        config.set('integration', 'runner', 'in-memory')
        config.set('integration', 'module', 'petronia_extension_runner.entrypoint')
        config.set('integration', 'entrypoint', 'entrypoint')

        self.foreman_config.load_config(config)
        self.foreman_runner = ForemanRunner(self.platform_settings, self.foreman_config)

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
        reset_launcher()

    def test_load_extension(self) -> None:
        """Load the extension."""
        self.assertEqual(0, self.foreman_runner.initialize())
        self.assertEqual(0, self.foreman_runner.boot())
        print("Boot complete")

        self.assertTrue(wait_for_launcher_alive(10000.0))
