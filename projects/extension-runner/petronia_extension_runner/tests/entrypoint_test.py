"""Test the module."""

import unittest
import os
import sys
import tempfile
import shutil
import json
from petronia_common.event_stream.tests.shared import create_read_stream, SimpleBinaryWriter
from petronia_common.util import RET_OK_NONE
from petronia_common.util.error import ExceptionPetroniaReturnError
from . import extension_entrypoint, extension_entrypoint_fails
from .. import entrypoint, setup


class EntrypointTest(unittest.TestCase):  # pylint:disable=too-many-instance-attributes
    """Test the entrypoint functions."""

    def setUp(self) -> None:
        self._orig_handler = setup.HANDLER_ID
        self._orig_config = list(setup.USER_CONFIG_PATH)
        self._orig_data = list(setup.DATA_PATH)
        self._orig_temp = setup.TEMP_DIR
        self._orig_ext_name = setup.EXTENSION_NAME
        self._orig_entry = setup.ENTRYPOINT_NAME
        self._orig_stdout = sys.stdout
        self._orig_sys_path = list(sys.path)
        self.tempdir = tempfile.mkdtemp()

    def tearDown(self) -> None:
        sys.stdout = self._orig_stdout
        sys.path.clear()
        sys.path.extend(self._orig_sys_path)

        # Default TEMP_DIR is the current directory, so never remove that.
        if not os.path.samefile(setup.TEMP_DIR, os.curdir):
            shutil.rmtree(setup.TEMP_DIR, ignore_errors=True)  # pragma no cover
        shutil.rmtree(self.tempdir, ignore_errors=True)

        setup.HANDLER_ID = self._orig_handler
        setup.USER_CONFIG_PATH.clear()
        setup.USER_CONFIG_PATH.extend(self._orig_config)
        setup.DATA_PATH.clear()
        setup.DATA_PATH.extend(self._orig_data)
        setup.TEMP_DIR = self._orig_temp
        setup.EXTENSION_NAME = self._orig_ext_name
        setup.ENTRYPOINT_NAME = self._orig_entry

    def test_entrypoint__bad_init(self) -> None:
        """Run the entrypoint with a bad initialization."""
        config_file = os.path.join(self.tempdir, 'config-file.txt')
        with open(config_file, 'w') as f:
            f.write('x')
        reader = create_read_stream(b'')
        writer = SimpleBinaryWriter()
        res = entrypoint.entrypoint(
            [
                'h1',   # handler
                'cp1',  # user config path
                'dp1',  # data path
                self.tempdir,
                'ex1',  # extension name
                config_file,
            ],
            reader, writer,
        )
        self.assertIsNotNone(res.error)
        self.assertEqual(
            [f'unknown structured file format: {config_file}'],
            [m.debug() for m in res.valid_error.messages()],
        )

    def test_entrypoint__bad_extension(self) -> None:
        """Run the entrypoint with a bad initialization."""
        config_file = os.path.join(self.tempdir, 'config-file.json')
        with open(config_file, 'w') as f:
            f.write('{}')
        reader = create_read_stream(b'')
        writer = SimpleBinaryWriter()
        sys.path.clear()
        res = entrypoint.entrypoint(
            [
                'h1',   # handler
                'cp1',  # user config path
                'dp1',  # data path
                self.tempdir,
                'does-not-exist',  # extension name
                config_file,
            ],
            reader, writer,
        )
        self.assertIsNotNone(res.error)
        self.assertEqual(
            [
                'extension-runner could not load Python module does-not-exist from path []'
            ],
            [m.debug() for m in res.valid_error.messages()],
        )

    def test_entrypoint__run(self) -> None:
        """Run the entrypoint."""
        config = {'a': 'x', 'b': 'y'}
        config_file = os.path.join(self.tempdir, 'config-file.json')
        with open(config_file, 'w') as f:
            json.dump(config, f)
        reader = create_read_stream(b'')
        writer = SimpleBinaryWriter()
        extension_entrypoint.init()
        extension_entrypoint_fails.init()
        res = entrypoint.entrypoint(
            [
                'h1',   # handler
                'cp1',  # user config path
                'dp1',  # data path
                self.tempdir,
                'petronia_extension_runner.tests.extension_entrypoint',  # extension name
                config_file,
                'a', 'b',
            ],
            reader, writer,
        )
        self.assertIs(RET_OK_NONE, res)
        self.assertEqual([['a', 'b']], extension_entrypoint.CALLED_ARGS)
        self.assertEqual([config], extension_entrypoint.CALLED_CONFIGS)

    def test_entrypoint__run_errors(self) -> None:
        """Run the entrypoint."""
        config = {'a': 'x', 'b': 'y'}
        config_file = os.path.join(self.tempdir, 'config-file.json')
        with open(config_file, 'w') as f:
            json.dump(config, f)
        reader = create_read_stream(b'')
        writer = SimpleBinaryWriter()
        extension_entrypoint.init()
        extension_entrypoint_fails.init()
        res = entrypoint.entrypoint(
            [
                'h1',   # handler
                'cp1',  # user config path
                'dp1',  # data path
                self.tempdir,
                'petronia_extension_runner.tests.extension_entrypoint_fails',
                config_file,
                'a', 'b',
            ],
            reader, writer,
        )
        self.assertIsNotNone(res.error)
        self.assertEqual([['a', 'b']], extension_entrypoint_fails.CALLED_ARGS)
        self.assertEqual([config], extension_entrypoint_fails.CALLED_CONFIGS)
        error = res.valid_error
        self.assertIsInstance(
            error,
            ExceptionPetroniaReturnError,
        )
        # mypy required check.
        assert isinstance(error, ExceptionPetroniaReturnError)  # nosec
        self.assertIs(
            error.exception(),
            extension_entrypoint_fails.RETURN[0],
        )
