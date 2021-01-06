"""Test the module."""

import unittest
import os
import sys
from .. import run_native


class RunNativeTest(unittest.TestCase):
    """Test the functions in the module."""

    def setUp(self) -> None:
        self._exec = sys.executable
        self._path = sys.path
        self._platform = sys.platform
        self._frozen = getattr(sys, 'frozen', None)
        self._env = os.environ.copy()

    def tearDown(self) -> None:
        sys.executable = self._exec
        sys.path = self._path
        sys.platform = self._platform
        if self._frozen is not None:
            setattr(sys, 'frozen', self._frozen)  # pragma nocover
        elif hasattr(sys, 'frozen'):
            delattr(sys, 'frozen')  # pragma nocover
        os.environ.clear()
        os.environ.update(self._env)

    def test_get_native_exec_args__no_split__win_not_frozen(self) -> None:
        """Test the function without needing to split the command."""
        sys.platform = 'win32'
        setattr(sys, 'frozen', False)
        os.environ.clear()
        os.environ.update({
            'LD_LIBRARY_PATH': 'blah',
            'LD_LIBRARY_PATH_ORIG': 'blah2',
        })
        res = run_native.get_native_exec_args('the-command')
        self.assertIsNone(res.error)
        self.assertTrue(res.ok)
        self.assertEqual(
            (
                ['the-command'],
                {
                    'LD_LIBRARY_PATH': 'blah',
                    'LD_LIBRARY_PATH_ORIG': 'blah2',
                },
            ),
            res.result,
        )

    def test_get_native_exec_args__no_split__win_frozen(self) -> None:
        """Test the function without needing to split the command."""
        sys.platform = 'win32'
        setattr(sys, 'frozen', True)
        os.environ.clear()
        os.environ.update({
            'LD_LIBRARY_PATH': 'blah',
            'LD_LIBRARY_PATH_ORIG': 'blah2',
        })
        res = run_native.get_native_exec_args('the-command')
        self.assertIsNone(res.error)
        self.assertTrue(res.ok)
        self.assertEqual(
            (
                ['the-command'],
                {
                    'LD_LIBRARY_PATH': 'blah',
                    'LD_LIBRARY_PATH_ORIG': 'blah2',
                },
            ),
            res.result,
        )

    def test_get_native_exec_args__no_split__win_no_frozen(self) -> None:
        """Test the function without needing to split the command."""
        sys.platform = 'win32'
        if hasattr(sys, 'frozen'):
            delattr(sys, 'frozen')  # pragma nocover
        os.environ.clear()
        os.environ.update({
            'LD_LIBRARY_PATH': 'blah',
            'LD_LIBRARY_PATH_ORIG': 'blah2',
        })
        res = run_native.get_native_exec_args('the-command')
        self.assertIsNone(res.error)
        self.assertTrue(res.ok)
        self.assertEqual(
            (
                ['the-command'],
                {
                    'LD_LIBRARY_PATH': 'blah',
                    'LD_LIBRARY_PATH_ORIG': 'blah2',
                },
            ),
            res.result,
        )

    def test_get_native_exec_args__no_split__linux_not_frozen(self) -> None:
        """Test the function without needing to split the command."""
        sys.platform = 'linux'
        setattr(sys, 'frozen', False)
        os.environ.clear()
        os.environ.update({
            'LD_LIBRARY_PATH': 'blah',
            'LD_LIBRARY_PATH_ORIG': 'blah2',
        })
        res = run_native.get_native_exec_args('the-command')
        self.assertIsNone(res.error)
        self.assertTrue(res.ok)
        self.assertEqual(
            (
                ['the-command'],
                {
                    'LD_LIBRARY_PATH': 'blah',
                    'LD_LIBRARY_PATH_ORIG': 'blah2',
                },
            ),
            res.result,
        )

    def test_get_native_exec_args__no_split__linux_frozen(self) -> None:
        """Test the function without needing to split the command."""
        sys.platform = 'linux'
        setattr(sys, 'frozen', True)
        os.environ.clear()
        os.environ.update({
            'LD_LIBRARY_PATH': 'blah',
            'LD_LIBRARY_PATH_ORIG': 'blah2',
        })
        res = run_native.get_native_exec_args('the-command')
        self.assertIsNone(res.error)
        self.assertTrue(res.ok)
        self.assertEqual(
            (
                ['the-command'],
                {
                    'LD_LIBRARY_PATH': 'blah2',
                    'LD_LIBRARY_PATH_ORIG': 'blah2',
                },
            ),
            res.result,
        )
