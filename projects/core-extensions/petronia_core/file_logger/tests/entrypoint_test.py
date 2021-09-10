"""Test the module"""

import unittest
import os
import tempfile
import shutil
from petronia_common.event_stream.tests.shared import create_read_stream, SimpleBinaryWriter
from petronia_common.util import UserMessage, i18n
from petronia_ext_lib.runner import SimpleEventRegistryContext
from petronia_ext_lib.logging import send_log_message
from .. import entrypoint


class EntrypointTest(unittest.TestCase):
    """Test the entrypoint function."""

    def setUp(self) -> None:
        self.tempdir = tempfile.mkdtemp()

    def tearDown(self) -> None:
        shutil.rmtree(self.tempdir, ignore_errors=True)

    def test_bad_config(self) -> None:
        """Test where the configuration is bad."""
        read = create_read_stream(b'')
        write = SimpleBinaryWriter()
        res = entrypoint.extension_entrypoint(
            read, write, {'files': [{'filename': 1, 'message_format': 1}]}, ['x', self.tempdir],
        )
        self.assertEqual(
            ['Field filename must be of type str for structure LogfileSettings'],
            [m.debug() for m in res.error_messages()],
        )

    def test_good_config(self) -> None:
        """Test where the configuration is good."""
        send_writer = SimpleBinaryWriter()
        send_context = SimpleEventRegistryContext(
            create_read_stream(b''), send_writer, None,
        )
        send_log_message(send_context, 's1', 'debug', [UserMessage('c1', i18n('m1'))])

        log_reader = create_read_stream(send_writer.getvalue())
        log_writer = SimpleBinaryWriter()
        res = entrypoint.extension_entrypoint(
            log_reader, log_writer, {'files': [
                {'filename': 'f.log', 'message_format': '{source} {text}'},
            ]}, ['x', self.tempdir],
        )
        self.assertIsNone(res.error)

        log_file = os.path.join(self.tempdir, 'logs', 'f.log')
        self.assertTrue(os.path.isfile(log_file))
        with open(log_file, 'r', encoding='utf-8') as f:
            log_contents = f.read()
        self.assertEqual(
            's1 m1\n',
            log_contents,
        )
