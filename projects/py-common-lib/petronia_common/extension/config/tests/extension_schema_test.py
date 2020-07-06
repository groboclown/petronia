
"""Tests the extension schema module."""

from typing import List
import unittest
from datetime import timedelta, datetime, timezone
from .. import extension_schema, event_schema
from ....util import UserMessage, i18n
from ....util.test_helpers import verified_not_none


class ExtensionSchemaMiscTest(unittest.TestCase):
    """Extra tests that aren't really covered by the loader_test"""
    def setUp(self) -> None:
        # Make sure, after the tests are done, we restore the original
        # timezone constant.  Some of the tests mess with it to get
        # consistency, regardless of where you run this test.
        self.__orig_tz = event_schema.LOCAL_TIMEZONE

    def tearDown(self) -> None:
        event_schema.LOCAL_TIMEZONE = self.__orig_tz

    def test_validate_dependencies__duplicates(self) -> None:
        """Tests dependency duplicate check"""
        deps = (
            extension_schema.ExtensionDependency('n', (1, 0, 0,), None,),
            extension_schema.ExtensionDependency('n', (2, 0, 0,), None,),
        )
        messages: List[UserMessage] = []
        extension_schema.validate_dependencies(deps, messages)
        self.assertEqual(
            [UserMessage(i18n('duplicate dependency: {name}'), name='n')],
            messages,
        )

    def test_dependency_is_within__no_below(self) -> None:
        """Tests dependency `is_within`"""
        dep = extension_schema.ExtensionDependency('n', (1, 0, 0,), None)
        self.assertTrue(dep.is_within((1, 2, 0,)))
        self.assertTrue(dep.is_within((1, 0, 0,)))
        self.assertFalse(dep.is_within((0, 0, 0,)))

    def test_dependency_is_within__below(self) -> None:
        """Tests dependency `is_within`"""
        dep = extension_schema.ExtensionDependency('n', (1, 0, 0,), (2, 0, 0))
        self.assertTrue(dep.is_within((1, 2, 0,)))
        self.assertTrue(dep.is_within((1, 0, 0,)))
        self.assertFalse(dep.is_within((0, 0, 0,)))
        self.assertFalse(dep.is_within((2, 0, 0,)))
        self.assertFalse(dep.is_within((2, 0, 1,)))

    def test_base_extension_getters(self) -> None:
        """Tests some of the basic getters in the parent class."""
        ext = extension_schema.StandAloneExtensionMetadata(
            'x', (1, 0, 0,), 'a1', 'd1', [], [], [],
        )
        self.assertEqual('standalone', ext.extension_type)
        self.assertEqual('x', ext.name)
        self.assertEqual((1, 0, 0,), ext.version)
        self.assertEqual('a1', ext.about)
        self.assertEqual('d1', ext.description)

    def test_api_extension_getters(self) -> None:
        """Test some of the getters for the api extension."""
        ext = extension_schema.ApiExtensionMetadata(
            'avid', (0, 0, 0,), 'a1', 'b1', [], [], [], [],
            extension_schema.ExtensionDependency('core', (10, 0, 5,), None)
        )
        default_impl = verified_not_none(ext.default_implementation, self)
        self.assertEqual(default_impl.name, 'core')
        self.assertEqual(default_impl.minimum_version, (10, 0, 5,))
        self.assertIsNone(default_impl.below_version)

    def test_api_duplicate_events(self) -> None:
        """This is a situation that can't happen via the loader, but can
        happen through the way the event objects are built and passed in."""
        ext = extension_schema.ApiExtensionMetadata(
            name='x', version=(1, 0, 0,), about='a1', description='d1',
            depends=[], licenses=[], authors=[], default_implementation=None,
            events=[
                event_schema.EventType(
                    'e1', 'high', 'public', 'public',
                    event_schema.StructureEventDataType(None, {}),
                ),
                event_schema.EventType(
                    'e1', 'high', 'public', 'public',
                    event_schema.StructureEventDataType(None, {}),
                ),
                event_schema.EventType(
                    '-e', 'high', 'public', 'public',
                    event_schema.StructureEventDataType(None, {}),
                ),
            ],
        )
        err = verified_not_none(ext.validate_type(), self)
        self.assertEqual(
            (
                UserMessage(
                    i18n(
                        'extension name ({name}) must be {MIN_EXTENSION_NAME_LENGTH} to '
                        '{MAX_EXTENSION_NAME_LENGTH} long'
                    ),
                    name='x', MIN_EXTENSION_NAME_LENGTH=2, MAX_EXTENSION_NAME_LENGTH=255,
                ),
                UserMessage(i18n('duplicate event name: {name}'), name='e1'),
                UserMessage(
                    i18n(
                        'event name ({event_name}) must conform '
                        'to the pattern `[a-z0-9][a-z0-9-]*`',
                    ),
                    event_name='-e',
                )
            ),
            err.messages(),
        )

    def test_datetime_convert__1(self) -> None:
        """Convert string to datetime, using tz hhmmss.ssssss"""
        dtm = event_schema.DatetimeEventDataType.str_to_datetime(
            "19990206:212322.123:+110512.123456"
        )
        self.assertTrue(dtm.ok)
        self.assertEqual(1999, dtm.result.year)
        self.assertEqual(2, dtm.result.month)
        self.assertEqual(6, dtm.result.day)
        self.assertEqual(21, dtm.result.hour)
        self.assertEqual(23, dtm.result.minute)
        self.assertEqual(123000, dtm.result.microsecond)
        self.assertEqual(
            timedelta(hours=11, minutes=5, seconds=12, microseconds=123456),
            dtm.result.utcoffset()
        )

    def test_datetime_convert__2(self) -> None:
        """Convert string -> datetime, with timezone hhmm."""
        dtm = event_schema.DatetimeEventDataType.str_to_datetime(
            "19991124:212322.123:+1105"
        )
        self.assertTrue(dtm.ok)
        self.assertEqual(1999, dtm.result.year)
        self.assertEqual(11, dtm.result.month)
        self.assertEqual(24, dtm.result.day)
        self.assertEqual(21, dtm.result.hour)
        self.assertEqual(23, dtm.result.minute)
        self.assertEqual(123000, dtm.result.microsecond)
        self.assertEqual(
            timedelta(hours=11, minutes=5),
            dtm.result.utcoffset()
        )

    def test_datetime_convert__3(self) -> None:
        """string -> datetime, error!"""
        dtm = event_schema.DatetimeEventDataType.str_to_datetime("20110229")
        self.assertFalse(dtm.ok)
        error = verified_not_none(dtm.error, self)
        self.assertEqual(1, len(error.messages()))
        message = error.messages()[0]
        self.assertEqual(
            'invalid formatted date string ({date})',
            message.message
        )
        self.assertEqual(
            {'date', 'exception'},
            set(message.arguments.keys()),
        )
        self.assertEqual('20110229', message.arguments['date'])
        self.assertIsInstance(message.arguments['exception'], ValueError)

    def test_datetime_convert__4(self) -> None:
        """datetime -> string"""
        res = event_schema.DatetimeEventDataType.datetime_to_str(
            datetime(
                year=2012, month=2, day=29, hour=23, minute=59, second=1,
                microsecond=100, tzinfo=timezone(-timedelta(hours=5, minutes=30)),
            )
        )
        self.assertEqual(
            "20120229:235901.000100:-0530",
            res,
        )

    def test_datetime_convert__5(self) -> None:
        """datetime -> string, no TZ info."""
        # Force the local time zone...
        event_schema.LOCAL_TIMEZONE = timezone(timedelta(hours=5))
        res = event_schema.DatetimeEventDataType.datetime_to_str(
            datetime(
                year=2012, month=2, day=29, hour=23, minute=59, second=1,
                microsecond=100, tzinfo=None,
            )
        )
        self.assertEqual(
            "20120229:235901.000100:+0500",
            res,
        )
