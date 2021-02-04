"""Test the module"""

import unittest
import os
import tempfile
import shutil
from .. import config_files


class ConfigFilesTest(unittest.TestCase):
    """Test the module functions."""

    def setUp(self) -> None:
        self.tempdir = tempfile.mkdtemp()

    def tearDown(self) -> None:
        shutil.rmtree(self.tempdir, ignore_errors=True)

    def test_find_config_files__no_path(self) -> None:
        """Test find_config_files with no path."""
        res = config_files.find_config_files('')
        self.assertEqual([], res)

    def test_find_config_files__invalid_dirs(self) -> None:
        """Test find_config_files with no path."""
        res = config_files.find_config_files(os.path.join(self.tempdir, 'does-not-exist'))
        self.assertEqual([], res)

    def test_find_config_files__config_of_different_types(self) -> None:
        """Test find_config_files with lots of file types and names."""
        cf1 = os.path.join(self.tempdir, 'config.yaml')
        with open(cf1, 'w') as f:
            f.write('x: {}')
        cf2 = os.path.join(self.tempdir, 'config.json')
        with open(cf2, 'w') as f:
            f.write('{}')
        not_cf3 = os.path.join(self.tempdir, 'ignore-me-config.json')
        with open(not_cf3, 'w') as f:
            f.write('{}')
        not_cf4 = os.path.join(self.tempdir, 'ignore-me-config.yaml')
        with open(not_cf4, 'w') as f:
            f.write('{}')
        cf5 = os.path.join(self.tempdir, 'my-config.json')
        with open(cf5, 'w') as f:
            f.write('{}')
        cf6 = os.path.join(self.tempdir, 'another-config.yaml')
        with open(cf6, 'w') as f:
            f.write('{}')

        res = config_files.find_config_files(self.tempdir)
        self.assertEqual(
            {cf1, cf2, cf5, cf6},
            set(res),
        )
