"""Tests for the module."""


from typing import List
import unittest
import os
import sys
from .. import run_python
from ....configuration.platform import detect_install_dir


class TestRunPython(unittest.TestCase):
    """Test the functions."""

    def setUp(self) -> None:
        self._exec = sys.executable
        self._path = sys.path
        self._env = os.environ.copy()
        self.install_dir = detect_install_dir()

    def tearDown(self) -> None:
        sys.executable = self._exec
        sys.path = self._path
        os.environ.clear()
        os.environ.update(self._env)

    def test_get_python_exec_args__no_reuse(self) -> None:
        """Test get_python_exec_args with no reuse of the python path."""
        sys.executable = 'foo'
        sys.path = ['16', '32']
        os.environ.clear()
        os.environ.update({
            'PYTHONPATH': 'abc',
            'OTHER_VALUE': 'yes',
        })
        res = run_python.get_python_exec_args(
            'my_module',
            ['a', 'b'],
            False,
            None,
        )
        self.assertIsNone(res.error)
        self.assertTrue(res.ok)
        self.assertEqual(
            (
                ('foo', '-m', 'my_module'),
                {
                    'PYTHONPATH': _abspath_list(['a', 'b']),
                    'OTHER_VALUE': 'yes',
                },
            ),
            res.result,
        )

    def test_get_python_exec_args__reuse_without_install_dir(self) -> None:
        """Test get_python_exec_args with no reuse of the python path."""
        sys.executable = 'foo'
        sys.path = ['c22', 'd11']
        os.environ.clear()
        os.environ.update({
            'PYTHONPATH': 'abc',
            'OTHER_VALUE': 'yes',
        })
        res = run_python.get_python_exec_args(
            'my_module',
            ['a33', 'b/55'],
            True,
            'x y z',
        )
        self.assertIsNone(res.error)
        self.assertTrue(res.ok)
        self.assertEqual(
            (
                ('foo', '-m', 'my_module', 'x', 'y', 'z'),
                {
                    'PYTHONPATH': _abspath_list(['c22', 'd11', self.install_dir, 'a33', 'b/55']),
                    'OTHER_VALUE': 'yes',
                },
            ),
            res.result,
        )

    def test_get_python_exec_args__reuse_with_install_dir(self) -> None:
        """Test get_python_exec_args with no reuse of the python path."""
        sys.executable = 'foo bar'
        sys.path = ['c22', 'd11', 'd11']
        os.environ.clear()
        os.environ.update({
            'PYTHONPATH': 'abc',
            'OTHER_VALUE': 'yes',
        })
        res = run_python.get_python_exec_args(
            'my_module',
            ['a33', 'b55'],
            True,
            '"A VALUE" b ${EXTENSION_NAME} c',
        )
        self.assertIsNone(res.error)
        self.assertTrue(res.ok)
        self.assertEqual(
            (
                ('foo bar', '-m', 'my_module', 'A VALUE', 'b', '${EXTENSION_NAME}', 'c'),
                {
                    'PYTHONPATH': _abspath_list(['c22', 'd11', self.install_dir, 'a33', 'b55']),
                    'OTHER_VALUE': 'yes',
                },
            ),
            res.result,
        )


def _abspath_list(values: List[str]) -> str:
    return os.pathsep.join([
        os.path.abspath(value)
        for value in values
    ])
