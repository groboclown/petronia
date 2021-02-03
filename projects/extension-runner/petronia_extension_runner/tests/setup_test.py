"""Test the module"""

import unittest
import sys
import os
import tempfile
import shutil
from .. import setup


class SetupTest(unittest.TestCase):
    """Test the functions in the module."""

    def setUp(self) -> None:
        self._orig_handler = setup.HANDLER_ID
        self._orig_config = list(setup.USER_CONFIG_PATH)
        self._orig_data = list(setup.DATA_PATH)
        self._orig_temp = setup.TEMP_DIR
        self._orig_ext_name = setup.EXTENSION_NAME
        self._orig_entry = setup.ENTRYPOINT_NAME
        self.tempdir = tempfile.mkdtemp()

    def tearDown(self) -> None:
        # Default TEMP_DIR is the current directory, so never remove that.
        if not os.path.samefile(setup.TEMP_DIR, os.curdir):
            shutil.rmtree(setup.TEMP_DIR, ignore_errors=True)
        shutil.rmtree(self.tempdir)

        setup.HANDLER_ID = self._orig_handler
        setup.USER_CONFIG_PATH.clear()
        setup.USER_CONFIG_PATH.extend(self._orig_config)
        setup.DATA_PATH.clear()
        setup.DATA_PATH.extend(self._orig_data)
        setup.TEMP_DIR = self._orig_temp
        setup.EXTENSION_NAME = self._orig_ext_name
        setup.ENTRYPOINT_NAME = self._orig_entry

    def test_initialize__no_options(self) -> None:
        """Test initialize with no options given."""
        res = setup.initialize()
        self.assertIsNone(res.error)
        args, config = res.result
        self.assertEqual([], args)
        self.assertEqual({}, config)

    def test_get_module_name(self) -> None:
        """Test the get_module_name function."""
        setup.EXTENSION_NAME = 'my-extension'
        self.assertEqual('my-extension', setup.get_module_name())

    def test_get_entrypoint_name(self) -> None:
        """Test the get_entrypoint_name function."""
        setup.ENTRYPOINT_NAME = 'my-entrypoint'
        self.assertEqual('my-entrypoint', setup.get_entrypoint_name())

    def test_get_python_path(self) -> None:
        """Test the get_python_path function."""
        self.assertEqual(
            list(sys.path),
            setup.get_python_path(),
        )
