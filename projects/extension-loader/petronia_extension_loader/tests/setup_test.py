"""Test the module"""

import unittest
import os
import tempfile
import shutil
import json
from .. import setup


class ExtensionLoaderSetupTest(unittest.TestCase):
    """Test the functions in the module."""

    def setUp(self) -> None:
        self._orig = setup.for_unittest_backup()
        self.tempdir = tempfile.mkdtemp()

    def tearDown(self) -> None:
        shutil.rmtree(self.tempdir, ignore_errors=True)
        setup.for_unittest_restore(self._orig)

    def test_initialize__no_args(self) -> None:
        """Test out the initialize function with no arguments."""
        res = setup.initialize()
        self.assertIsNotNone(res.error)
        self.assertEqual(
            ['No extension directory found.'],
            [m.debug() for m in res.error_messages()]
        )

    def test_initialize_minimal(self) -> None:
        """Test out initialize with minimal arguments."""
        extension_dir = os.path.join(self.tempdir, 'extensions')
        os.makedirs(extension_dir)
        res = setup.initialize(
            '.',  # user_config_path
            self.tempdir,  # data_path
            None,  # temp_dir
            None,  # launcher_id
        )
        self.assertIsNone(res.error)
        self.assertEqual({}, setup.get_extension_config('x'))
        self.assertEqual((extension_dir,), setup.get_extension_dirs())
        self.assertEqual((), setup.get_boot_extensions())
        self.assertEqual('extension-loader', setup.get_extension_handler_id())

    def test_initialize_user_config_file_valid(self) -> None:
        """Test out initialize with a user configuration file."""
        extension_dir = os.path.join(self.tempdir, 'extensions')
        os.makedirs(extension_dir)
        data_dir = os.path.join(self.tempdir, 'data')
        os.makedirs(data_dir)
        config_dir = os.path.join(self.tempdir, 'configs')
        os.makedirs(config_dir)
        with open(os.path.join(config_dir, 'config.json'), 'w') as f:
            json.dump({
                'startup': {
                    'extensions': ['ext1'],
                    'priority-extensions': ['ext2'],
                    'extension-dirs': [extension_dir],
                },
                'ext': {
                    'extension': 'p.e.1',
                    'enabled': True,
                    'properties': {'y': 2},
                },
                'ext1': {
                    'extension': 'ext1',
                    'properties': {'x': 1},
                },
            }, f)
        res = setup.initialize(config_dir, data_dir, None, None)
        self.assertIsNone(res.error)
        self.assertEqual({'y': 2}, setup.get_extension_config('p.e.1'))
        self.assertEqual({'x': 1}, setup.get_extension_config('ext1'))
        self.assertEqual({}, setup.get_extension_config('ext2'))
        self.assertEqual((extension_dir,), setup.get_extension_dirs())
        self.assertEqual({'ext1', 'ext2', 'p.e.1'}, set(setup.get_boot_extensions()))
        self.assertEqual('ext2', setup.get_boot_extensions()[0])
        self.assertEqual('extension-loader', setup.get_extension_handler_id())
