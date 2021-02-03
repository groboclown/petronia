"""Test the module."""

from typing import List
import unittest
import os
import sys
import tempfile
import shutil
from petronia_common.event_stream.tests.shared import create_read_stream, SimpleBinaryWriter
from petronia_common.util import RET_OK_NONE
from .. import importer

TEST_MODULE_TEXT = """

from petronia_common.util import StdRet, RET_OK_NONE
MY_MODULE_CONST = 'const value'

def my_module_function(v: str) -> str:
    return MY_MODULE_CONST + v

def entrypoint_function(r, w, c, a):
    a.append('x')
    return RET_OK_NONE

"""


class ImporterTest(unittest.TestCase):
    """Test the importer module functions."""

    def setUp(self) -> None:
        self._orig_sys_path = list(sys.path)
        self.tempdir = tempfile.mkdtemp()

    def tearDown(self) -> None:
        sys.path.clear()
        sys.path.extend(self._orig_sys_path)
        shutil.rmtree(self.tempdir, ignore_errors=True)

    def test_add_item_to_path__not_exist(self) -> None:
        """Test add_item_to_path"""
        sys.path.clear()
        item = os.path.join(self.tempdir, 'does-not-exist')
        importer.add_item_to_path(item)
        self.assertEqual([], sys.path)

    def test_add_item_to_path__in_path(self) -> None:
        """Test add_item_to_path"""
        sys.path.clear()
        item = os.path.abspath(os.path.join(self.tempdir, 'exists'))
        os.makedirs(item)
        sys.path.append(item)
        importer.add_item_to_path(item)
        self.assertEqual([item], sys.path)

    def test_add_item_to_path__add(self) -> None:
        """Test add_item_to_path"""
        sys.path.clear()
        item = os.path.abspath(os.path.join(self.tempdir, 'exists'))
        os.makedirs(item)
        importer.add_item_to_path(item)
        self.assertEqual([item], sys.path)

    def test_load_module_from_path__new_path(self) -> None:
        """Test load_module_from_path with a new file not in the current sys path."""
        with open(os.path.join(self.tempdir, 'test-module-1.py'), 'w') as f:
            f.write(TEST_MODULE_TEXT)
        res = importer.load_module_from_path('test-module-1', [self.tempdir])
        self.assertIsNone(res.error)
        self.assertTrue(hasattr(res.result, 'MY_MODULE_CONST'))
        self.assertEqual(
            'const value',
            getattr(res.result, 'MY_MODULE_CONST'),
        )
        self.assertEqual(
            'const valueabc',
            getattr(res.result, 'my_module_function')('abc'),
        )

    def test_load_module_from_path__not_found(self) -> None:
        """Test load_module_from_path with a not-existent module."""
        res = importer.load_module_from_path('does-not-exist', [self.tempdir])
        self.assertIsNotNone(res.error)
        self.assertEqual(
            [
                f'extension-runner could not load Python module '
                f'does-not-exist from path {repr([self.tempdir])}'
            ],
            [m.debug() for m in res.error_messages()],
        )

    def test_get_entrypoint_function__module_error(self) -> None:
        """Test get_entrypoint_function with a module load error."""
        res = importer.get_entrypoint_function(
            'does-not-exist', 'entrypoint', [self.tempdir],
        )
        self.assertIsNotNone(res.error)
        self.assertEqual(
            [
                f'extension-runner could not load Python module '
                f'does-not-exist from path {repr([self.tempdir])}'
            ],
            [m.debug() for m in res.error_messages()],
        )

    def test_get_entrypoint_function__entrypoint_name_error(self) -> None:
        """Test get_entrypoint_function with a missing entrypoint error."""
        with open(os.path.join(self.tempdir, 'test-module-2.py'), 'w') as f:
            f.write(TEST_MODULE_TEXT)
        res = importer.get_entrypoint_function(
            'test-module-2', 'entrypoint', [self.tempdir],
        )
        self.assertIsNotNone(res.error)
        self.assertEqual(
            ['No such entrypoint entrypoint in module test-module-2'],
            [m.debug() for m in res.error_messages()],
        )

    def test_get_entrypoint_function__entrypoint_callable_error(self) -> None:
        """Test get_entrypoint_function with an entrypoint not being callable error."""
        with open(os.path.join(self.tempdir, 'test-module-3.py'), 'w') as f:
            f.write(TEST_MODULE_TEXT)
        res = importer.get_entrypoint_function(
            'test-module-3', 'MY_MODULE_CONST', [self.tempdir],
        )
        self.assertIsNotNone(res.error)
        self.assertEqual(
            ['Entrypoint MY_MODULE_CONST in module test-module-3 is not a function'],
            [m.debug() for m in res.error_messages()],
        )

    def test_get_entrypoint_function__ok(self) -> None:
        """Test get_entrypoint_function with an entrypoint not being callable error."""
        with open(os.path.join(self.tempdir, 'test-module-4.py'), 'w') as f:
            f.write(TEST_MODULE_TEXT)
        res = importer.get_entrypoint_function(
            'test-module-4', 'entrypoint_function', [self.tempdir],
        )
        self.assertIsNone(res.error)
        args: List[str] = []
        self.assertEqual(
            RET_OK_NONE,
            res.result(create_read_stream(b''), SimpleBinaryWriter(), {}, args),
        )
        self.assertEqual(['x'], args)
