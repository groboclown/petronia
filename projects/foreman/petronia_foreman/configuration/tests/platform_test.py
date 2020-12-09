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

    def tearDown(self) -> None:
        shutil.rmtree(self.tempdir)

    def test_find_data_dir__no_dirs(self) -> None:
        """Find the data directory when there are no paths."""
        pst = platform.PlatformSettings('n', 0, [], [], 'x')
        self.assertIsNone(pst.find_data_dir('my-data-dir'))

    def test_find_data_dir__not_found(self) -> None:
        """Find the data directory when it doesn't exist."""
        pst = platform.PlatformSettings('n', 0, [], [self.tempdir], 'x')
        self.assertIsNone(pst.find_data_dir('my-data-dir'))

    def test_find_data_dir__found_file(self) -> None:
        """Find the data directory when it exists as a file."""
        with open(os.path.join(self.tempdir, 'file.txt'), 'w') as f:
            f.write('x')
        pst = platform.PlatformSettings('n', 0, [], [self.tempdir], 'x')
        self.assertIsNone(pst.find_data_dir('file.txt'))

    def test_find_data_dir__found_dir(self) -> None:
        """Find the data directory when it exists as a dir."""
        expected = os.path.join(self.tempdir, 'data-dir')
        os.mkdir(expected)
        pst = platform.PlatformSettings('n', 0, [], [self.tempdir], 'x')
        self.assertEqual(expected, pst.find_data_dir('data-dir'))


class PlatformFuncTest(unittest.TestCase):
    """Test out platform functions."""

    def setUp(self) -> None:
        self.tempdir = tempfile.mkdtemp()

    def tearDown(self) -> None:
        shutil.rmtree(self.tempdir)
        if hasattr(sys, 'frozen'):
            delattr(sys, 'frozen')
        if hasattr(sys, '_MEIPASS'):
            delattr(sys, '_MEIPASS')

    def test_detect_platform__windows10(self) -> None:
        """windows 10 platform detection."""
        res = platform.detect_platform('windows-10')
        self.assertTrue(res.ok)
        self.assertEqual(platform.CATEGORY__WINDOWS, res.result.category)
        self.assertEqual('windows-10', res.result.name)

    def test_detect_platform__linux_x11(self) -> None:
        """X11 platform detection."""
        res = platform.detect_platform('linux-x11')
        self.assertTrue(res.ok)
        self.assertEqual(platform.CATEGORY__LINUX, res.result.category)
        self.assertEqual('linux-x11', res.result.name)

    def test_detect_platform__linux_wayland(self) -> None:
        """X11 platform detection."""
        res = platform.detect_platform('linux-wayland')
        self.assertTrue(res.ok)
        self.assertEqual(platform.CATEGORY__LINUX, res.result.category)
        self.assertEqual('linux-wayland', res.result.name)

    def test_detect_platform__windows(self) -> None:
        """windows 10 platform detection."""
        res = platform.detect_platform('windows')
        # Depending on the underlying OS, this can fail or succeed.
        self.assertIsNotNone(res)

    def test_detect_platform__linux(self) -> None:
        """Linux platform detection."""
        res = platform.detect_platform('linux')
        # Depending on the underlying OS, this can fail or succeed.
        self.assertIsNotNone(res)

    def test_detect_platform__unknown(self) -> None:
        """Unknown platform detection."""
        res = platform.detect_platform('unknown')
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
        res = platform.get_petronia_paths([])
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
        res = platform.get_petronia_paths([td1, td2, None])
        self.assertEqual(expected_paths, res)
