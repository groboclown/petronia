"""Test the module."""

import unittest
import os
import tempfile
import shutil
from .. import find_file, platform


class FindFileTest(unittest.TestCase):
    """Test the find file functions."""

    def setUp(self) -> None:
        self.tempdir = tempfile.mkdtemp()
        self._orig_config_path = list(platform.configuration_paths)
        platform.configuration_paths = [self.tempdir]

    def tearDown(self) -> None:
        shutil.rmtree(self.tempdir)
        platform.configuration_paths = self._orig_config_path

    def test__get_config_file__with_file_arg(self) -> None:
        """Test get_config_file with a config argument."""
        f_name = os.path.join(self.tempdir, 'test.txt')
        with open(f_name, 'w') as f:
            f.write('[foo]')
        res = find_file.get_config_file(f_name)
        self.assertTrue(res.ok)
        self.assertEqual(f_name, res.result)

    def test__get_config_file__with_dir_arg__not_exist(self) -> None:
        """Test get_config_file when the argument is a directory."""
        for expected_name in find_file.DEFAULT_PETRONIA_CONFIG_FILE_NAMES:
            self.assertFalse(os.path.isfile(os.path.join(self.tempdir, expected_name)))
        res = find_file.get_config_file(self.tempdir)
        self.assertTrue(res.has_error)

    def test__get_config_file__with_dir_arg__exist(self) -> None:
        """Test get_config_file when the argument is a directory."""
        for expected_name in find_file.DEFAULT_PETRONIA_CONFIG_FILE_NAMES:
            self.assertFalse(os.path.isfile(os.path.join(self.tempdir, expected_name)))
        f_name = os.path.join(self.tempdir, find_file.DEFAULT_PETRONIA_CONFIG_FILE_NAMES[0])
        with open(f_name, 'w') as f:
            f.write('[foo]')

        res = find_file.get_config_file(self.tempdir)
        self.assertTrue(res.ok)
        self.assertEqual(f_name, res.result)

    def test__get_config_file__without_arg(self) -> None:
        """Test get_config_file when the argument is a directory."""
        for expected_name in find_file.DEFAULT_PETRONIA_CONFIG_FILE_NAMES:
            self.assertFalse(os.path.isfile(os.path.join(self.tempdir, expected_name)))
        f_name = os.path.join(self.tempdir, find_file.DEFAULT_PETRONIA_CONFIG_FILE_NAMES[0])
        with open(f_name, 'w') as f:
            f.write('[foo]')
        platform.configuration_paths = [self.tempdir]
        res = find_file.get_config_file(None)
        self.assertIsNone(res.error)
        self.assertEqual(f_name, res.result)

    def test__discover_config_file_in__no_paths(self) -> None:
        """Test discover_config_file_in with no search path."""
        res = find_file.discover_config_file_in([])
        self.assertTrue(res.has_error)

    def test__discover_config_file_in__no_valid_paths(self) -> None:
        """Test get_config_file when the argument is a directory."""
        res = find_file.discover_config_file_in([None, ''])
        self.assertTrue(res.has_error)
