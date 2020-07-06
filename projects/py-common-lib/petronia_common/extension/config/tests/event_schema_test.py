
from typing import List, cast
import unittest
from .. import event_schema
from ....util import UserMessage, i18n


class EventSchemaMiscTest(unittest.TestCase):
    """Extra tests that aren't really covered by the loader_test"""
    def test_getters(self) -> None:
        schema = event_schema.BoolEventDataType('x')
        self.assertEqual('x', schema.description)

    def test_bool(self) -> None:
        schema = event_schema.BoolEventDataType('x')
        self.assertEqual('bool', schema.type_name)
        self.assertIsNone(schema.validate_type())
        self.assertTrue(schema.validate_value(True))
        self.assertTrue(schema.validate_value(False))
        self.assertFalse(schema.validate_value(None))
        self.assertFalse(schema.validate_value({}))

    def test_string__1(self) -> None:
        schema = event_schema.StringEventDataType('y', 1, 5)
        self.assertEqual('string', schema.type_name)
        self.assertEqual('y', schema.description)
        self.assertIsNone(schema.validate_type())
        self.assertTrue(schema.validate_value('1'))
        self.assertTrue(schema.validate_value('abcde'))
        self.assertFalse(schema.validate_value(None))
        self.assertFalse(schema.validate_value({}))
        self.assertFalse(schema.validate_value(''))
        self.assertFalse(schema.validate_value('abcdef'))

    def test_string__2(self) -> None:
        schema = event_schema.StringEventDataType(
            'y', event_schema.MAX_STRING_LENGTH + 2, event_schema.MAX_STRING_LENGTH + 1,
        )
        err = schema.validate_type()
        self.assertIsNotNone(err)
        assert err is not None  # mypy requirement
        self.assertEqual(
            (
                UserMessage(
                    i18n('min_length ({min_length}) must be equal to or less than max_length ({max_length})'),
                    min_length=65537, max_length=65536,
                ),
                UserMessage(
                    i18n('max_length ({max_length}) must be less than or equal to {MAX_STRING_LENGTH}'),
                    max_length=65536, MAX_STRING_LENGTH=65535,
                )
            ),
            err.messages()
        )

    def test_string__3(self) -> None:
        schema = event_schema.StringEventDataType('y', -1, 4)
        err = schema.validate_type()
        self.assertIsNotNone(err)
        assert err is not None  # mypy requirement
        self.assertEqual(
            (UserMessage(
                i18n('min_length ({min_length}) must be greater than or equal to {MIN_STRING_LENGTH}'),
                min_length=-1, MIN_STRING_LENGTH=0,
            ),),
            err.messages()
        )

    def test_int__1(self) -> None:
        schema = event_schema.IntEventDataType('z', -4, 6)
        self.assertEqual('z', schema.description)
        self.assertEqual('int', schema.type_name)
        self.assertEqual(-4, schema.min_value)
        self.assertEqual(6, schema.max_value)
        self.assertIsNone(schema.validate_type())
        self.assertTrue(schema.validate_value(-4))
        self.assertTrue(schema.validate_value(6))
        self.assertFalse(schema.validate_value(-5))
        self.assertFalse(schema.validate_value(7))
        self.assertFalse(schema.validate_value(None))
        self.assertFalse(schema.validate_value({}))
        self.assertFalse(schema.validate_value(False))

        # this is actually okay
        self.assertTrue(schema.validate_value(0.2))

    def test_int__2(self) -> None:
        schema = event_schema.IntEventDataType(None, 90, 1)
        err = schema.validate_type()
        self.assertIsNotNone(err)
        assert err is not None  # mypy requirement
        self.assertEqual(
            (UserMessage(
                i18n('min_value ({min_value}) must be equal to or less than max_value ({max_value})'),
                min_value=90, max_value=1
            ),),
            err.messages()
        )

    def test_int__3(self) -> None:
        schema = event_schema.IntEventDataType(
            None, event_schema.MIN_INT_VALUE - 1, event_schema.MAX_INT_VALUE + 1,
        )
        err = schema.validate_type()
        self.assertIsNotNone(err)
        assert err is not None  # mypy requirement
        self.assertEqual(
            (UserMessage(
                i18n('min_value ({min_value}) must be greater than or equal to {MIN_INT_VALUE}'),
                min_value=-9223372036854775809, MIN_INT_VALUE=-9223372036854775808,
            ), UserMessage(
                i18n('max_value ({max_value}) must be less than or equal to {MAX_INT_VALUE}'),
                max_value=9223372036854775808, MAX_INT_VALUE=9223372036854775807,
            )),
            err.messages()
        )

    def test_float__1(self) -> None:
        schema = event_schema.FloatEventDataType('z', -4, 6)
        self.assertEqual('z', schema.description)
        self.assertEqual('float', schema.type_name)
        self.assertEqual(-4, schema.min_value)
        self.assertEqual(6, schema.max_value)
        self.assertIsNone(schema.validate_type())
        self.assertTrue(schema.validate_value(-4))
        self.assertTrue(schema.validate_value(6))
        self.assertFalse(schema.validate_value(-5))
        self.assertFalse(schema.validate_value(7))
        self.assertFalse(schema.validate_value(None))
        self.assertFalse(schema.validate_value({}))
        self.assertFalse(schema.validate_value(False))
        self.assertTrue(schema.validate_value(0.2))

    def test_float__2(self) -> None:
        schema = event_schema.FloatEventDataType(None, 90, 1)
        err = schema.validate_type()
        self.assertIsNotNone(err)
        assert err is not None  # mypy requirement
        self.assertEqual(
            (UserMessage(
                i18n('min_value ({min_value}) must be equal to or less than max_value ({max_value})'),
                min_value=90, max_value=1
            ),),
            err.messages()
        )

    def test_float__3(self) -> None:
        schema = event_schema.FloatEventDataType(None, None, None)
        self.assertIsNone(schema.description)
        self.assertEqual(None, schema.min_value)
        self.assertEqual(None, schema.max_value)
        self.assertIsNone(schema.validate_type())
        self.assertTrue(schema.validate_value(-4))
        self.assertTrue(schema.validate_value(6))
        self.assertTrue(schema.validate_value(-5))
        self.assertTrue(schema.validate_value(7.33433322423442342342348979081234))
        self.assertFalse(schema.validate_value(None))
        self.assertFalse(schema.validate_value({}))
        self.assertFalse(schema.validate_value(False))
        self.assertTrue(schema.validate_value(0.2))

    def test_enum__1(self) -> None:
        schema = event_schema.EnumEventDataType('a', ['x', 'y'])
        self.assertEqual('a', schema.description)
        self.assertEqual('enum', schema.type_name)
        self.assertEqual(2, len(schema.values))
        self.assertEqual({'x', 'y'}, set(schema.values))
        self.assertIsNone(schema.validate_type())
        self.assertTrue(schema.validate_value('x'))
        self.assertTrue(schema.validate_value('y'))
        self.assertFalse(schema.validate_value('xy'))
        self.assertFalse(schema.validate_value(6))
        self.assertFalse(schema.validate_value(7.33433322423442342342348979081234))
        self.assertFalse(schema.validate_value(None))
        self.assertFalse(schema.validate_value({}))
        self.assertFalse(schema.validate_value(False))

    def test_enum__2(self) -> None:
        schema = event_schema.EnumEventDataType(None, [])
        err = schema.validate_type()
        self.assertIsNotNone(err)
        assert err is not None  # mypy requirement
        self.assertEqual(
            (UserMessage(
                i18n('value list must contain at least 1 item'),
            ),),
            err.messages(),
        )

    def test_enum__3(self) -> None:
        # hack a type value
        schema = event_schema.EnumEventDataType(
            None, cast(List[str], [1, '', 'x' * (event_schema.MAX_ENUM_VALUE_LENGTH + 1)])
        )
        err = schema.validate_type()
        self.assertIsNotNone(err)
        assert err is not None  # mypy requirement
        self.assertEqual(
            {UserMessage(
                i18n('enum value "{value}" must have at least {MIN_ENUM_VALUE_LENGTH} characters'),
                value='', MIN_ENUM_VALUE_LENGTH=1,
            ), UserMessage(
                i18n('enum value "{value}" must have no more than {MAX_ENUM_VALUE_LENGTH} characters'),
                value='x' * (event_schema.MAX_ENUM_VALUE_LENGTH + 1), MAX_ENUM_VALUE_LENGTH=255,
            ), UserMessage(
                i18n('enum value {value} must be a string'),
                value=1,
            )},
            set(err.messages()),
        )

    def test_datetime__1(self) -> None:
        schema = event_schema.DatetimeEventDataType('b')
        self.assertEqual('datetime', schema.type_name)
        self.assertEqual('b', schema.description)
        self.assertIsNone(schema.validate_type())
        self.assertTrue(schema.validate_value('12340101:012345.123:-51'))
        self.assertTrue(schema.validate_value('12340101:012345.123:51'))
        self.assertTrue(schema.validate_value('12340101:012345.123:5'))
        self.assertTrue(schema.validate_value('12340101:012345.123:-5'))
        self.assertTrue(schema.validate_value('12340101:012345.123:+51'))
        self.assertTrue(schema.validate_value('12340101:012345.123:-5'))
        self.assertTrue(schema.validate_value('12340101:012345.123:0'))
        self.assertFalse(schema.validate_value('12340101:012345.123:-'))
        self.assertFalse(schema.validate_value('12340101:012345.:1'))
        self.assertFalse(schema.validate_value('12340101:012345.3:0'))
        self.assertFalse(schema.validate_value('12340101:012345.123:-'))
        self.assertFalse(schema.validate_value('2340101:12345.123:0'))
        self.assertFalse(schema.validate_value(1))
        self.assertFalse(schema.validate_value(1.5))
        self.assertFalse(schema.validate_value(None))
        self.assertFalse(schema.validate_value(False))
