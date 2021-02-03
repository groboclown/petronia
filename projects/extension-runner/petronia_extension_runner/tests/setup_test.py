"""Test the module"""

import unittest
import sys
import os
import tempfile
import shutil
import json
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
            shutil.rmtree(setup.TEMP_DIR, ignore_errors=True)  # pragma no cover
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
        self.assertFalse(os.path.samefile(setup.TEMP_DIR, os.curdir))
        self.assertEqual('<unset>', setup.HANDLER_ID)
        self.assertEqual('<unset>', setup.EXTENSION_NAME)
        self.assertEqual(self._orig_entry, setup.ENTRYPOINT_NAME)
        self.assertEqual([os.curdir], setup.USER_CONFIG_PATH)
        self.assertEqual([os.curdir], setup.DATA_PATH)

    def test_initialize__complete(self) -> None:
        """Test initialize with all the options given."""
        new_temp_dir = os.path.join(self.tempdir, 'abc')
        os.makedirs(new_temp_dir, exist_ok=True)
        config_file = os.path.join(self.tempdir, 'config-file.json')
        with open(config_file, 'w') as f:
            json.dump({
                'i': ['j', 'k'],
            }, f)
        res = setup.initialize(
            'h1',
            os.pathsep.join(['x1', 'y1']),
            os.pathsep.join(['a2', 'b2']),
            new_temp_dir,
            'ex1',
            config_file,
            'a1', 'a2',
        )
        self.assertIsNone(res.error)
        args, config = res.result
        self.assertEqual(['a1', 'a2'], args)
        self.assertEqual({'i': ['j', 'k']}, config)
        self.assertTrue(os.path.samefile(setup.TEMP_DIR, new_temp_dir))
        self.assertEqual('h1', setup.HANDLER_ID)
        self.assertEqual('ex1', setup.EXTENSION_NAME)
        self.assertEqual(self._orig_entry, setup.ENTRYPOINT_NAME)
        self.assertEqual(['x1', 'y1'], setup.USER_CONFIG_PATH)
        self.assertEqual(['a2', 'b2'], setup.DATA_PATH)

    def test_initialize__alternate_config_1(self) -> None:
        """Test an alternate, valid configuration setup"""
        config_file = os.path.join(self.tempdir, 'config-file.json')
        with open(config_file, 'w') as f:
            json.dump([{
                'i': ['j', 'k'],
            }], f)
        res = setup.initialize(config_file=config_file)
        self.assertIsNone(res.error)
        args, config = res.result
        self.assertEqual([], args)
        self.assertEqual({'i': ['j', 'k']}, config)

    def test_initialize__alternate_config_2(self) -> None:
        """Test an alternate, valid configuration setup"""
        config_file = os.path.join(self.tempdir, 'config-file.json')
        with open(config_file, 'w') as f:
            json.dump([
                {'i': ['j', 'k']},
                {'w': 'z'},
            ], f)
        res = setup.initialize(config_file=config_file)
        self.assertIsNone(res.error)
        args, config = res.result
        self.assertEqual([], args)
        self.assertEqual({'i': ['j', 'k']}, config)

    def test_initialize__alternate_config_3(self) -> None:
        """Test an alternate, valid configuration setup"""
        config_file = os.path.join(self.tempdir, 'config-file.json')
        with open(config_file, 'w') as f:
            json.dump([], f)
        res = setup.initialize(config_file=config_file)
        self.assertIsNone(res.error)
        args, config = res.result
        self.assertEqual([], args)
        self.assertEqual({}, config)

    def test_initialize__bad_config_1(self) -> None:
        """Test an alternate, valid configuration setup"""
        config_file = os.path.join(self.tempdir, 'config-file.txt')
        with open(config_file, 'w') as f:
            f.write('x')
        res = setup.initialize(config_file=config_file)
        self.assertIsNotNone(res.error)
        self.assertEqual(
            [f'unknown structured file format: {config_file}'],
            [m.debug() for m in res.valid_error.messages()],
        )

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
