"""Test the module"""

from typing import List, Sequence, Tuple, Dict
import unittest
import os
import sys
import tempfile
import shutil
from configparser import ConfigParser
from petronia_common.event_stream import BinaryReader, BinaryWriter
from petronia_common.event_stream.tests.shared import create_read_stream, SimpleBinaryWriter
from .. import load_launcher
from ....configuration import RuntimeConfig


TEST_MODULE_TEXT = """

MY_MODULE_CONST = 'const value'

def my_module_function(v: str) -> str:
    return MY_MODULE_CONST + v

"""


class LoadLauncherTest(unittest.TestCase):
    """Test the classes and functions."""

    def setUp(self) -> None:
        self.tempdir = tempfile.mkdtemp()
        self.mod_script = os.path.join(self.tempdir, 'test_mod.py')
        with open(self.mod_script, 'w', encoding='utf-8') as f:
            f.write(TEST_MODULE_TEXT)

    def tearDown(self) -> None:
        shutil.rmtree(self.tempdir)

    def test_import_module(self) -> None:
        """Try out loading the not-in-the-path module."""
        cfg = ConfigParser()
        cfg.add_section('local-test')
        cfg.set('local-test', load_launcher.PYTHON_PATH_OPTION, self.tempdir)
        l_conf = RuntimeConfig('local-test', cfg)
        mod = load_launcher.import_module('test_mod', [1], [], l_conf)
        self.assertIsNone(mod.error)
        self.assertTrue(mod.ok)
        self.assertTrue(hasattr(mod.result, 'MY_MODULE_CONST'))
        self.assertEqual(
            'const value',
            getattr(mod.result, 'MY_MODULE_CONST'),
        )
        self.assertEqual(
            'const valueabc',
            getattr(mod.result, 'my_module_function')('abc'),
        )

    def test_connect_launcher__ok(self) -> None:
        """Test out the connect_launcher with a normal exit mode."""
        reader = create_read_stream(b'data')
        writer = SimpleBinaryWriter()
        errors: List[Tuple[str, str, BaseException]] = []
        oks: List[Tuple[str, str]] = []

        def on_error(_mod_name: str, _entry: str, _err: BaseException) -> None:
            raise Exception('should not be called')  # pragma no cover

        def on_ok(mod_name: str, entry: str) -> None:
            oks.append((mod_name, entry))

        thread_res = load_launcher.connect_launcher(
            '_entry_point_ok', sys.modules[__name__],
            on_error, on_ok, ['a', 'b'], reader, writer, {},
        )
        self.assertIsNone(thread_res.error)
        self.assertTrue(thread_res.ok)
        thread_res.result.begin_ok()
        thread_res.result.join(5.0)
        self.assertEqual(
            [],
            errors,
        )
        self.assertEqual(
            [(__name__, '_entry_point_ok')],
            oks,
        )
        self.assertEqual(
            b'',
            reader.read(),
        )
        self.assertEqual(
            b'ok',
            writer.getvalue(),
        )

    def test_connect_launcher__error(self) -> None:
        """Test out the connect_launcher with a normal exit mode."""
        reader = create_read_stream(b'data')
        writer = SimpleBinaryWriter()
        errors: List[Tuple[str, str, BaseException]] = []
        oks: List[Tuple[str, str]] = []

        def on_error(mod_name: str, entry: str, err: BaseException) -> None:
            errors.append((mod_name, entry, err))

        def on_ok(_mod_name: str, _entry: str) -> None:
            raise ValueError('should not be called')  # pragma no cover

        thread_res = load_launcher.connect_launcher(
            '_entry_point_err', sys.modules[__name__],
            on_error, on_ok, ['1', 'abc'], reader, writer, {},
        )
        self.assertIsNone(thread_res.error)
        self.assertTrue(thread_res.ok)
        thread_res.result.begin_ok()
        thread_res.result.join(5.0)
        self.assertEqual(
            [(__name__, '_entry_point_err', RAISED_ERROR)],
            errors,
        )
        self.assertEqual(
            [],
            oks,
        )
        self.assertEqual(
            b'ata',
            reader.read(),
        )
        self.assertEqual(
            b'err',
            writer.getvalue(),
        )


def _entry_point_ok(
        read: BinaryReader, write: BinaryWriter, _config: Dict[str, str], _args: Sequence[str],
) -> None:
    read.read()
    write.write(b'ok')


RAISED_ERROR = OSError('blah')


def _entry_point_err(
        read: BinaryReader, write: BinaryWriter, _config: Dict[str, str], _args: Sequence[str],
) -> None:
    read.read(1)
    write.write(b'err')
    raise RAISED_ERROR
