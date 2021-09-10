"""Test the module."""

import unittest
import os
import sys
import tempfile
import shutil
from .. import platform


class PlatformConfigTest(unittest.TestCase):
    """Test the PlatformConfig class."""

    def setUp(self) -> None:
        self.tempdir = tempfile.mkdtemp()
        self._orig_data_paths = platform.data_paths

    def tearDown(self) -> None:
        shutil.rmtree(self.tempdir)
        platform.data_paths = self._orig_data_paths

    def test_find_data_dir__no_dirs(self) -> None:
        """Find the data directory when there are no paths."""
        platform.data_paths = []
        self.assertIsNone(platform.find_data_dir('my-data-dir'))

    def test_find_data_dir__not_found(self) -> None:
        """Find the data directory when it doesn't exist."""
        platform.data_paths = [self.tempdir]
        self.assertIsNone(platform.find_data_dir('my-data-dir'))

    def test_find_data_dir__found_file(self) -> None:
        """Find the data directory when it exists as a file."""
        with open(os.path.join(self.tempdir, 'file.txt'), 'w', encoding='utf-8') as f:
            f.write('x')
        platform.data_paths = [self.tempdir]
        self.assertIsNone(platform.find_data_dir('file.txt'))

    def test_find_data_dir__found_dir(self) -> None:
        """Find the data directory when it exists as a dir."""
        expected = os.path.join(self.tempdir, 'data-dir')
        os.mkdir(expected)
        platform.data_paths = [self.tempdir]
        self.assertEqual(expected, platform.find_data_dir('data-dir'))


class PlatformFuncTest(unittest.TestCase):
    """Test out platform functions."""

    def setUp(self) -> None:
        self.tempdir = tempfile.mkdtemp()
        self._orig_platform_name = platform.platform_name
        self._orig_data_paths = platform.data_paths
        self._orig_config_paths = platform.configuration_paths
        self._orig_os_category = platform.os_category

    def tearDown(self) -> None:
        shutil.rmtree(self.tempdir)
        if hasattr(sys, 'frozen'):
            delattr(sys, 'frozen')
        if hasattr(sys, '_MEIPASS'):
            delattr(sys, '_MEIPASS')
        platform.platform_name = self._orig_platform_name
        platform.data_paths = self._orig_data_paths
        platform.configuration_paths = self._orig_config_paths
        platform.os_category = self._orig_os_category

    def test_detect_platform__windows10(self) -> None:
        """windows 10 platform detection."""
        res = platform.initial_setup('windows-10')
        self.assertTrue(res.ok)
        self.assertEqual(platform.CATEGORY__WINDOWS, platform.os_category)
        self.assertEqual('windows-10', platform.platform_name)

    def test_detect_platform__linux_x11(self) -> None:
        """X11 platform detection."""
        res = platform.initial_setup('linux-x11')
        self.assertTrue(res.ok)
        self.assertEqual(platform.CATEGORY__LINUX, platform.os_category)
        self.assertEqual('linux-x11', platform.platform_name)

    def test_detect_platform__linux_wayland(self) -> None:
        """X11 platform detection."""
        res = platform.initial_setup('linux-wayland')
        self.assertTrue(res.ok)
        self.assertEqual(platform.CATEGORY__LINUX, platform.os_category)
        self.assertEqual('linux-wayland', platform.platform_name)

    def test_detect_platform__windows(self) -> None:
        """windows 10 platform detection."""
        res = platform.initial_setup('windows')
        # Depending on the underlying OS, this can fail or succeed.
        self.assertIsNotNone(res)

    def test_detect_platform__linux(self) -> None:
        """Linux platform detection."""
        res = platform.initial_setup('linux')
        # Depending on the underlying OS, this can fail or succeed.
        self.assertIsNotNone(res)

    def test_detect_platform__unknown(self) -> None:
        """Unknown platform detection."""
        res = platform.initial_setup('unknown')
        # Depending on the underlying OS, this can fail or succeed.
        self.assertTrue(res.has_error)

    def test_detect_install_dir__bundled_exists(self) -> None:
        """Simulate a bundled environment."""
        setattr(sys, 'frozen', True)
        setattr(sys, '_MEIPASS', self.tempdir)
        res = platform.detect_install_dir()
        self.assertEqual(self.tempdir, res)

    def test_detect_install_dir__bundled_not_exists(self) -> None:
        """Simulate a bundled environment."""
        setattr(sys, 'frozen', True)
        setattr(sys, '_MEIPASS', os.path.join(self.tempdir, 'does-not-exist'))
        res = platform.detect_install_dir()
        self.assertEqual(os.path.abspath(os.path.curdir), res)

    def test_get_petronia_paths__no_paths(self) -> None:
        """Test get_petronia_paths with no paths"""
        res = platform.find_petronia_paths([])
        self.assertEqual([], res)

    def test_get_petronia_paths__full(self) -> None:
        """Test get_petronia_paths with all app_paths"""
        td1 = os.path.abspath(os.path.join(self.tempdir, 'td1'))
        td2 = os.path.abspath(os.path.join(self.tempdir, 'td2'))
        expected_paths = []
        for based in (td1, td2):
            for app in platform.APP_PATHS:
                i = os.path.abspath(os.path.join(based, app))
                os.makedirs(i, exist_ok=True)
                expected_paths.append(i)
        expected_paths.append(td1)
        expected_paths.append(td2)
        res = platform.find_petronia_paths([td1, td2, None])
        self.assertEqual(expected_paths, res)
