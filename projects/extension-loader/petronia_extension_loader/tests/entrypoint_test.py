"""Test the module"""

import unittest
import os
import tempfile
import shutil
from petronia_common.event_stream.tests.shared import create_read_stream, SimpleBinaryWriter
from .. import entrypoint, setup


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
            [m.debug() for m in res.error_messages()]
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
