"""Test the module"""

from typing import List
import unittest
import os
import shutil
import tempfile
from petronia_ext_lib.events import logging as logging_event
from .. import log_handler, shared_state


class LogHandlerTest(unittest.TestCase):
    """Test the function and classes in the module."""

    def setUp(self) -> None:
        self.tempdir = tempfile.mkdtemp()
        os.makedirs(os.path.join(self.tempdir, 'logs'))
        self.logfile = os.path.join(self.tempdir, 'logs', 'logfile.txt')
        shared_state.clear_data()
        shared_state.load_configuration(self.tempdir, {
            'files': [{
                'filename': 'logfile.txt',
                'message_format': '({source}) ({text})',
            }],
        })

    def tearDown(self) -> None:
        shutil.rmtree(self.tempdir, ignore_errors=True)

    def test_user_message(self) -> None:
        """Test UserMessageTarget"""
        target = log_handler.UserMessageTarget()
        event = logging_event.UserErrorEvent(logging_event.Error(
            'i1', ['debug'], 's1', [logging_event.LocalizableMessage('c1', 'm1', None)],
        ))
        self.assertFalse(
            target.on_event('s2', 't2', event)
        )
        self.assertEqual(
            ['(s2) (m1)'],
            self._get_messages(),
        )

    def test_system_message(self) -> None:
        """Test SystemMessageTarget"""
        target = log_handler.SystemMessageTarget()
        event = logging_event.SystemErrorEvent(logging_event.Error(
            'i1', ['debug'], 's1', [logging_event.LocalizableMessage('c1', 'm1', None)],
        ))
        self.assertFalse(
            target.on_event('s2', 't2', event)
        )
        self.assertEqual(
            ['(s2) (m1)'],
            self._get_messages(),
        )

    def test_log(self) -> None:
        """Test LogTarget"""
        target = log_handler.LogTarget()
        event = logging_event.LogEvent(
            'debug', [logging_event.LocalizableMessage('c1', 'm1', None)],
        )
        self.assertFalse(
            target.on_event('s2', 't2', event)
        )
        self.assertEqual(
            ['(s2) (m1)'],
            self._get_messages(),
        )

    def _get_messages(self) -> List[str]:
        self.assertTrue(os.path.isfile(self.logfile))
        with open(self.logfile) as f:
            return [line.strip() for line in f.readlines()]
