"""Test the module"""

import unittest
import os
import tempfile
import shutil
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
        self.assertEqual(None, setup.get_extension_config('x'))
        self.assertEqual((extension_dir,), setup.get_extension_dirs())
        self.assertEqual((), setup.get_boot_extensions())
        self.assertEqual('extension-loader', setup.get_extension_handler_id())
