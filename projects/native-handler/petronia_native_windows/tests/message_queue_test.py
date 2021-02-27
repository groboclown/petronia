"""Test the module"""

import unittest
import unittest.mock
import time

from petronia_common.util import RET_OK_NONE
from .. import message_queue
from ..message_loop import WindowsMessageLoop


class UserMessageQueueTest(unittest.TestCase):
    """Test the UserMessageQueue class."""

    def test_cleanup_messages__none(self) -> None:
        """Test cleanup_messages with no messages"""
        loop = WindowsMessageLoop()
        queue = message_queue.UserMessageQueue(loop, 1)
        self.assertEqual(0, queue.cleanup_messages(1))

    def test_cleanup_messages__some(self) -> None:
        """Test cleanup_messages with messages, but not all are expired"""
        loop = unittest.mock.Mock(WindowsMessageLoop())
        loop.send_custom_message_to_self.return_value = RET_OK_NONE
        queue = message_queue.UserMessageQueue(loop, 1)
        self.assertIsNone(queue.add_handler(1, lambda x: None).error)
        self.assertIsNone(queue.queue_message(1, 'x').error)
        self.assertIsNone(queue.queue_message(1, 'y').error)
        time.sleep(0.2)
        self.assertIsNone(queue.queue_message(1, 'x').error)
        self.assertIsNone(queue.queue_message(1, 'y').error)

        # Yep.  Negative number means we pick them up without needing to sleep.
        self.assertEqual(2, queue.cleanup_messages(0.1))

    def test_cleanup_messages__all(self) -> None:
        """Test cleanup_messages with messages that are all expired"""
        loop = unittest.mock.Mock(WindowsMessageLoop())
        loop.send_custom_message_to_self.return_value = RET_OK_NONE
        queue = message_queue.UserMessageQueue(loop, 1)
        self.assertIsNone(queue.add_handler(1, lambda x: None).error)
        self.assertIsNone(queue.queue_message(1, 'x').error)
        self.assertIsNone(queue.queue_message(1, 'y').error)
        self.assertEqual(2, queue.cleanup_messages(1.0))
