# GENERATED CODE - DO NOT MODIFY

"""
Tests for the foreman_announcement module.
Extension petronia.core.api.foreman_announcement, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long,unused-import

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import foreman_announcement


class ExtensionStartupCompleteEventTest(unittest.TestCase):
    """
    Tests for ExtensionStartupCompleteEvent
    """
    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in EXTENSION_STARTUP_COMPLETE_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman_announcement.ExtensionStartupCompleteEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


EXTENSION_STARTUP_COMPLETE_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    ('basic-parse', {}),
]
