"""Test the module"""

import unittest
from petronia_common.util import UserMessage, StdRet, i18n, not_none
from petronia_common.util.error import SimplePetroniaReturnError
from .. import error
from ...events import logging


class ErrorEventTest(unittest.TestCase):
    """Test the functions in the module."""

    def test_create_error_message_data__none(self) -> None:
        """Test create_error_message_data with no error messages."""
        res = error.create_error_message_data(
            logging.Error, logging.LocalizableMessage, logging.MessageArgument,
            logging.MessageArgumentValue, [], [], 'x',
        )
        self.assertIsNone(res)

    def test_create_error_message_data__one(self) -> None:
        """Test create_error_message_data with one error messages."""
        res = error.create_error_message_data(
            logging.Error, logging.LocalizableMessage, logging.MessageArgument,
            logging.MessageArgumentValue,
            [UserMessage('c1', i18n('m1'), b=1)],
            [error.FILE_ERROR_CATEGORY, error.OS_ERROR_CATEGORY], 'x1',
        )
        self.assertIsNotNone(res)
        err = not_none(res)
        self.assertEqual(
            err.identifier, 'x1',
        )
        self.assertIsNone(err.source)
        self.assertEqual(
            err.categories, [error.FILE_ERROR_CATEGORY, error.OS_ERROR_CATEGORY],
        )
        self.assertEqual(1, len(err.messages))

    def test_create_error_message__none(self) -> None:
        """Test create_error_message_data with one error messages."""
        res = error.create_error_data(
            logging.Error, logging.LocalizableMessage, logging.MessageArgument,
            logging.MessageArgumentValue,
            StdRet.pass_ok(1),
            [error.FILE_ERROR_CATEGORY, error.OS_ERROR_CATEGORY], 'x1',
        )
        self.assertIsNone(res)

    def test_create_error_message__two(self) -> None:
        """Test create_error_message_data with one error messages."""
        res = error.create_error_data(
            logging.Error, logging.LocalizableMessage, logging.MessageArgument,
            logging.MessageArgumentValue,
            StdRet.pass_error(SimplePetroniaReturnError(
                UserMessage('c1', i18n('m1')),
                UserMessage('c2', i18n('m2')),
            )),
            [error.FILE_ERROR_CATEGORY, error.OS_ERROR_CATEGORY], 'x1',
        )
        self.assertIsNotNone(res)
        err = not_none(res)
        self.assertEqual(
            err.identifier, 'x1',
        )
        self.assertIsNone(err.source)
        self.assertEqual(
            err.categories, [error.FILE_ERROR_CATEGORY, error.OS_ERROR_CATEGORY],
        )
        self.assertEqual(2, len(err.messages))
