"""Test the module"""

import unittest
import os
import sys
import tempfile
import shutil
import importlib
from petronia_common.event_stream.tests.shared import create_read_stream, SimpleBinaryWriter
from petronia_common.extension.config import load_extension
from petronia_common.util import load_structured_file
from .. import entrypoint, setup

CORE_IMPL_FILE_NAME = 'core-extension-loader-extension.yaml'


class ExtensionLoaderEntrypointTest(unittest.TestCase):
    """Test the functions in the module."""

    def setUp(self) -> None:
        self._orig = setup.for_unittest_backup()
        self.tempdir = tempfile.mkdtemp()

    def tearDown(self) -> None:
        shutil.rmtree(self.tempdir, ignore_errors=True)
        setup.for_unittest_restore(self._orig)

    def test_entrypoint__invalid_args(self) -> None:
        """Run the entrypoint with invalid arguments."""
        reader = create_read_stream(b'')
        writer = SimpleBinaryWriter()
        res = entrypoint.extension_entrypoint(reader, writer, {}, [])
        self.assertIsNotNone(res.error)
        self.assertEqual(
            ['No extension directory found.'],
            [m.debug() for m in res.error_messages()],
        )

    def test_entrypoint__valid_args(self) -> None:
        """Run the entrypoint with valid arguments."""
        os.makedirs(os.path.join(self.tempdir, 'extensions'))
        reader = create_read_stream(b'')
        writer = SimpleBinaryWriter()
        res = entrypoint.extension_entrypoint(reader, writer, {}, [
            '.',  # user_config_path
            self.tempdir,  # data_path
            self.tempdir,  # temp_dir
            'l-id',  # launcher_id
        ])
        self.assertIsNone(res.error)

    def test_extension_loader_package(self) -> None:
        """Test that the extension loader package that matches the extension doc exists."""
        filename = ''
        for pel in sys.path:
            fqn = os.path.join(pel, CORE_IMPL_FILE_NAME)
            if os.path.isfile(fqn):
                filename = fqn
        self.assertIsNot('', filename)
        contents_res = load_structured_file(filename)
        self.assertIsNone(contents_res.error)
        contents = contents_res.result
        extension_info = load_extension(list(contents)[0])
        self.assertIsNone(extension_info.error)
        module = importlib.import_module(extension_info.result.name)
        self.assertTrue(hasattr(module, 'extension_entrypoint'))
        self.assertTrue(
            callable(getattr(module, 'extension_entrypoint'))
        )
