
"""Tests the event schema module."""

from typing import List, Dict, cast
import unittest
from .. import event_schema
from ....util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from ....util.test_helpers import verified_not_none


class EventSchemaBoolTest(unittest.TestCase):
    """Extra tests that aren't really covered by the loader_test"""

    def test_bool(self) -> None:
        """Test the bool type value validation"""
        schema = event_schema.BoolEventDataType('x')
        self.assertEqual('bool', schema.type_name)
        self.assertEqual('x', schema.description)
        self.assertIsNone(schema.validate_type())
        self.assertTrue(schema.validate_value(True))
        self.assertTrue(schema.validate_value(False))
        self.assertFalse(schema.validate_value(None))
        self.assertFalse(schema.validate_value({}))


class EventSchemaStringTest(unittest.TestCase):
    """Extra tests that aren't really covered by the loader_test"""

    def test_string__1(self) -> None:
        """Test the string type value validation"""
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
        """Test the string type validation"""
        schema = event_schema.StringEventDataType(
            'y', event_schema.MAX_STRING_LENGTH + 2, event_schema.MAX_STRING_LENGTH + 1,
        )
        err = verified_not_none(schema.validate_type(), self)
        self.assertEqual(
            (
                UserMessage(
                    STANDARD_PETRONIA_CATALOG,
                    i18n(
                        'min_length ({min_length}) must be equal to or '
                        'less than max_length ({max_length})',
                    ),
                    min_length=65537, max_length=65536,
                ),
                UserMessage(
                    STANDARD_PETRONIA_CATALOG,
                    i18n(
                        'max_length ({max_length}) must be less than '
                        'or equal to {MAX_STRING_LENGTH}',
                    ),
                    max_length=65536, MAX_STRING_LENGTH=65535,
                ),
            ),
            err.messages(),
        )

    def test_string__3(self) -> None:
        """Test the string type validation"""
        schema = event_schema.StringEventDataType('y', -1, 4)
        err = verified_not_none(schema.validate_type(), self)
        self.assertEqual(
            (UserMessage(
                STANDARD_PETRONIA_CATALOG,
                i18n(
                    'min_length ({min_length}) must be greater '
                    'than or equal to {MIN_STRING_LENGTH}',
                ),
                min_length=-1, MIN_STRING_LENGTH=0,
            ),),
            err.messages(),
        )


class EventSchemaIntTest(unittest.TestCase):
    """Extra tests that aren't really covered by the loader_test"""

    def test_int__1(self) -> None:
        """Test the int type value validation"""
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
        """Test the int type validation"""
        schema = event_schema.IntEventDataType(None, 90, 1)
        err = verified_not_none(schema.validate_type(), self)
        self.assertEqual(
            (UserMessage(
                STANDARD_PETRONIA_CATALOG,
                i18n(
                    'min_value ({min_value}) must be equal to or less than max_value ({max_value})',
                ),
                min_value=90, max_value=1,
            ),),
            err.messages(),
        )

    def test_int__3(self) -> None:
        """Test the int type validation"""
        schema = event_schema.IntEventDataType(
            None, event_schema.MIN_INT_VALUE - 1, event_schema.MAX_INT_VALUE + 1,
        )
        err = schema.validate_type()
        self.assertIsNotNone(err)
        assert err is not None  # mypy requirement
        self.assertEqual(
            (UserMessage(
                STANDARD_PETRONIA_CATALOG,
                i18n('min_value ({min_value}) must be greater than or equal to {MIN_INT_VALUE}'),
                min_value=-9223372036854775809, MIN_INT_VALUE=-9223372036854775808,
            ), UserMessage(
                STANDARD_PETRONIA_CATALOG,
                i18n('max_value ({max_value}) must be less than or equal to {MAX_INT_VALUE}'),
                max_value=9223372036854775808, MAX_INT_VALUE=9223372036854775807,
            )),
            err.messages(),
        )


class EventSchemaFloatTest(unittest.TestCase):
    """Extra tests that aren't really covered by the loader_test"""

    def test_float__1(self) -> None:
        """Test the float type value validation"""
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
        """Test the float type validation"""
        schema = event_schema.FloatEventDataType(None, 90, 1)
        err = verified_not_none(schema.validate_type(), self)
        self.assertEqual(
            (UserMessage(
                STANDARD_PETRONIA_CATALOG,
                i18n(
                    'min_value ({min_value}) must be equal to or less than max_value ({max_value})',
                ),
                min_value=90, max_value=1,
            ),),
            err.messages(),
        )

    def test_float__3(self) -> None:
        """Test the float type value validation"""
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


class EventSchemaEnumTest(unittest.TestCase):
    """Extra tests that aren't really covered by the loader_test"""

    def test_enum__1(self) -> None:
        """Test the enum type value validation"""
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
        """Test the enum type validation with no values"""
        schema = event_schema.EnumEventDataType(None, [])
        err = verified_not_none(schema.validate_type(), self)
        self.assertEqual(
            (UserMessage(
                STANDARD_PETRONIA_CATALOG,
                i18n('enum must contain at least 1 item ({description})'),
                description='no description',
            ),),
            err.messages(),
        )

    def test_enum__3(self) -> None:
        """Test the enum type validation with bad data types"""
        # Hack up a type value, because it's prevented from being formed in the
        # loader, but code can allow it.
        schema = event_schema.EnumEventDataType(
            None, cast(List[str], [1, '', 'x' * (event_schema.MAX_ENUM_VALUE_LENGTH + 1)]),
        )
        err = verified_not_none(schema.validate_type(), self)
        self.assertEqual(
            {UserMessage(
                STANDARD_PETRONIA_CATALOG,
                i18n('enum value "{value}" must have at least {MIN_ENUM_VALUE_LENGTH} characters'),
                value='', MIN_ENUM_VALUE_LENGTH=1,
            ), UserMessage(
                STANDARD_PETRONIA_CATALOG,
                i18n(
                    'enum value "{value}" must have no more than '
                    '{MAX_ENUM_VALUE_LENGTH} characters',
                ),
                value='x' * (event_schema.MAX_ENUM_VALUE_LENGTH + 1), MAX_ENUM_VALUE_LENGTH=255,
            ), UserMessage(
                STANDARD_PETRONIA_CATALOG,
                i18n('enum value {value} must be a string'),
                value=1,
            )},
            set(err.messages()),
        )


class EventSchemaDatetimeTest(unittest.TestCase):
    """Extra tests that aren't really covered by the loader_test"""

    def test_datetime__1(self) -> None:
        """Test the datetime type value validation"""
        schema = event_schema.DatetimeEventDataType('b')
        self.assertEqual('datetime', schema.type_name)
        self.assertEqual('b', schema.description)
        self.assertIsNone(schema.validate_type())
        self.assertTrue(schema.validate_value('12340101:012345.123:-0051'))
        self.assertTrue(schema.validate_value('12340101:012345.123:0051'))
        self.assertTrue(schema.validate_value('12340101:012345.123:0500'))
        self.assertTrue(schema.validate_value('12340101:012345.123:-0500'))
        self.assertTrue(schema.validate_value('12340101:012345.123:+0051'))
        self.assertTrue(schema.validate_value('12340101:012345.123:-0521'))
        self.assertTrue(schema.validate_value('12340101:012345.123:0000'))
        self.assertFalse(schema.validate_value('12340101:012345.123:-'))
        self.assertFalse(schema.validate_value('12340101:012345.123:-5'))
        self.assertFalse(schema.validate_value('12340101:012345.123:-21'))
        self.assertFalse(schema.validate_value('12340101:012345.:1000'))
        self.assertFalse(schema.validate_value('12340101:012345.-:0000'))
        self.assertFalse(schema.validate_value('12340101:012345.123:-'))
        self.assertFalse(schema.validate_value('2340101:12345.123:0000'))
        self.assertFalse(schema.validate_value(1))
        self.assertFalse(schema.validate_value(1.5))
        self.assertFalse(schema.validate_value(None))
        self.assertFalse(schema.validate_value(False))


class EventSchemaReferenceTest(unittest.TestCase):
    """Extra tests that aren't really covered by the loader_test"""

    def test_reference__1(self) -> None:
        """Simple methods on the reference type, and valid type validation."""
        schema = event_schema.ReferenceEventDataType('ab', 'my-ref')
        self.assertEqual('reference', schema.type_name)
        self.assertEqual('ab', schema.description)
        self.assertEqual('my-ref', schema.reference)
        self.assertEqual("ReferenceEventDataType('ab', ref='my-ref')", repr(schema))
        # references are never valid.
        error = verified_not_none(schema.validate_type(), self)
        self.assertEqual(
            (
                UserMessage(STANDARD_PETRONIA_CATALOG, i18n('`reference` type not replaced')),
            ),
            error.messages(),
        )
        self.assertFalse(schema.validate_value(None))


class EventSchemaArrayTest(unittest.TestCase):
    """Extra tests that aren't really covered by the loader_test"""

    def test_array__1(self) -> None:
        """Simple type and value checks for arrays"""
        # Just use a trivial, valid type.
        inner_type = event_schema.BoolEventDataType(None)
        schema = event_schema.ArrayEventDataType(
            'xxz', inner_type, 1, 11,
        )
        self.assertEqual('array', schema.type_name)
        self.assertEqual('xxz', schema.description)
        self.assertIs(inner_type, schema.value_type)
        self.assertEqual(1, schema.min_length)
        self.assertEqual(11, schema.max_length)
        self.assertIsNone(schema.validate_type())

        # min count
        self.assertTrue(schema.validate_value([True]))
        # max count
        self.assertTrue(schema.validate_value([
            True, True, False, True, False, True,
            False, False, True, False, True,
        ]))
        # < min count
        self.assertFalse(schema.validate_value([]))
        # > max count
        self.assertFalse(schema.validate_value([
            True, True, False, True, False, True,
            False, False, True, False, True, False,
        ]))
        # tuple, not array
        self.assertTrue(schema.validate_value((True,)))

        # non-sequential
        self.assertFalse(schema.validate_value(None))
        self.assertFalse(schema.validate_value(True))
        self.assertFalse(schema.validate_value(1.0))
        self.assertFalse(schema.validate_value({"x": 1}))
        self.assertFalse(schema.validate_value(object()))
        self.assertFalse(schema.validate_value({True}))

        # non-correct inner values.
        self.assertFalse(schema.validate_value([1.0]))
        self.assertFalse(schema.validate_value([object()]))
        self.assertFalse(schema.validate_value([{"x": False}]))

    def test_array__2(self) -> None:
        """type validation issues for an array"""
        schema = event_schema.ArrayEventDataType(
            None, event_schema.ReferenceEventDataType(None, 'x'), 1, 2,
        )
        error = verified_not_none(schema.validate_type(), self)
        self.assertEqual(
            (
                UserMessage(STANDARD_PETRONIA_CATALOG, i18n('`reference` type not replaced')),
            ),
            error.messages(),
        )

    def test_array__3(self) -> None:
        """type validation issues for an array"""
        schema = event_schema.ArrayEventDataType(
            None, event_schema.BoolEventDataType(None), 2, 1,
        )
        error = verified_not_none(schema.validate_type(), self)
        self.assertEqual(
            (
                UserMessage(
                    STANDARD_PETRONIA_CATALOG,
                    i18n(
                        'min_length ({min_length}) must be equal to '
                        'or less than max_length ({max_length})',
                    ),
                    min_length=2, max_length=1,
                ),
            ),
            error.messages(),
        )

    def test_array__4(self) -> None:
        """type validation issues for an array"""
        schema = event_schema.ArrayEventDataType(
            None, event_schema.BoolEventDataType(None), -1, 100,
        )
        error = verified_not_none(schema.validate_type(), self)
        self.assertEqual(
            (UserMessage(
                STANDARD_PETRONIA_CATALOG,
                i18n(
                    'min_length ({min_length}) must be greater than or equal to {MIN_ARRAY_LENGTH}',
                ),
                min_length=-1, MIN_ARRAY_LENGTH=0,
            ),),
            error.messages(),
        )

    def test_array__5(self) -> None:
        """type validation issues for an array"""
        schema = event_schema.ArrayEventDataType(
            None, event_schema.BoolEventDataType(None), 0, event_schema.MAX_ARRAY_LENGTH + 1,
        )
        error = verified_not_none(schema.validate_type(), self)
        self.assertEqual(
            (
                UserMessage(
                    STANDARD_PETRONIA_CATALOG,
                    i18n(
                        'max_length ({max_length}) must be less than or '
                        'equal to {MAX_ARRAY_LENGTH}',
                    ),
                    max_length=event_schema.MAX_ARRAY_LENGTH + 1,
                    MAX_ARRAY_LENGTH=event_schema.MAX_ARRAY_LENGTH,
                ),
            ),
            error.messages(),
        )


class EventSchemaStructureTest(unittest.TestCase):
    """Extra tests that aren't really covered by the loader_test"""

    def test_structure__1(self) -> None:
        """type validation and method invocations for structure"""
        field1 = event_schema.IntEventDataType(None, 0, 10)
        field2 = event_schema.BoolEventDataType(None)
        schema = event_schema.StructureEventDataType(
            'x', {
                "abc": event_schema.StructureFieldType(field1, False),
                "def": event_schema.StructureFieldType(field2, True),
            },
        )
        self.assertEqual('x', schema.description)
        self.assertEqual('structure', schema.type_name)
        self.assertEqual({'abc', 'def'}, set(schema.field_names()))
        self.assertIs(
            field1,
            verified_not_none(schema.get_field_type('abc'), self).data_type,
        )
        self.assertIs(
            field2,
            verified_not_none(schema.get_field_type('def'), self).data_type,
        )
        self.assertIsNone(schema.get_field_type('xyz'))
        self.assertIsNone(schema.validate_type())

        self.assertTrue(schema.validate_value({"abc": 1}))
        self.assertTrue(schema.validate_value({"abc": 0, "def": False}))
        # extra values are ok.
        self.assertTrue(schema.validate_value({"abc": 10, "def": True, "qed": 1}))

        self.assertFalse(schema.validate_value(None))
        self.assertFalse(schema.validate_value(True))
        self.assertFalse(schema.validate_value(1.0))
        self.assertFalse(schema.validate_value([1]))
        self.assertFalse(schema.validate_value({"def": False}))
        self.assertFalse(schema.validate_value({"abc": -1}))
        self.assertFalse(schema.validate_value({"abc": 11}))
        self.assertFalse(schema.validate_value({"abc": 0, "def": 10}))

        schema2 = event_schema.StructureEventDataType(
            'x', {
                "abc": event_schema.StructureFieldType(field1, False),
                "def": event_schema.StructureFieldType(field2, True),
            },
        )
        schema3 = event_schema.StructureEventDataType(
            'y', {
                "abc": event_schema.StructureFieldType(field1, False),
                "def": event_schema.StructureFieldType(field2, True),
            },
        )
        self.assertTrue(schema.__eq__(schema))
        self.assertFalse(schema.__ne__(schema))
        self.assertTrue(schema == schema2)
        self.assertFalse(schema != schema2)
        self.assertFalse(schema == schema3)
        self.assertTrue(schema != schema3)
        self.assertFalse(schema == 'blah')

    def test_hash(self) -> None:
        """Test that the object has a hash code, and is thus capable of being hashed"""
        schema = event_schema.StructureEventDataType(
            'y', {
                "abc": event_schema.StructureFieldType(event_schema.BoolEventDataType(None), False),
            },
        )
        res = {schema: 1}
        self.assertEqual(1, len(res))

    def test_validate_type_bad_1(self) -> None:
        """bad schema validation."""
        schema = event_schema.StructureEventDataType(
            None, {
                "": event_schema.StructureFieldType(event_schema.BoolEventDataType(None), False),
                ("x" * event_schema.MAX_FIELD_NAME_LENGTH): event_schema.StructureFieldType(
                    event_schema.BoolEventDataType(None), False,
                ),
                "_": event_schema.StructureFieldType(event_schema.BoolEventDataType(None), False),
                "$": event_schema.StructureFieldType(event_schema.BoolEventDataType(None), False),
                "a%": event_schema.StructureFieldType(event_schema.BoolEventDataType(None), False),
            },
        )
        error = verified_not_none(schema.validate_type(), self)
        self.assertEqual(
            (
                UserMessage(
                    STANDARD_PETRONIA_CATALOG,
                    i18n(
                        'field name ({field_name}) must have {MIN_FIELD_NAME_LENGTH} to '
                        '{MAX_FIELD_NAME_LENGTH} characters',
                    ),
                    field_name='', MIN_FIELD_NAME_LENGTH=1, MAX_FIELD_NAME_LENGTH=255,
                ),
                UserMessage(
                    STANDARD_PETRONIA_CATALOG,
                    i18n('field name ({field_name}) must match `[a-z][a-z0-9_]*`'),
                    field_name='_',
                ),
                UserMessage(
                    STANDARD_PETRONIA_CATALOG,
                    i18n('field name ({field_name}) must match `[a-z][a-z0-9_]*`'),
                    field_name='$',
                ),
                UserMessage(
                    STANDARD_PETRONIA_CATALOG,
                    i18n('field name ({field_name}) must match `[a-z][a-z0-9_]*`'),
                    field_name='a%',
                ),
            ),
            error.messages(),
        )

    def test_invalid_subtype(self) -> None:
        """bad subtype in fields."""
        schema = event_schema.StructureEventDataType(
            None, {
                "x": event_schema.StructureFieldType(
                    event_schema.ReferenceEventDataType(None, "x"), False,
                ),
            },
        )
        error = verified_not_none(schema.validate_type(), self)
        self.assertEqual(
            (
                UserMessage(STANDARD_PETRONIA_CATALOG, i18n('`reference` type not replaced')),
            ),
            error.messages(),
        )


class StructureFieldTypeTest(unittest.TestCase):
    """Tests for StructureFieldType"""
    def test_eq(self) -> None:
        """Test the equality function."""
        dt_bool1 = event_schema.BoolEventDataType(None)
        dt_bool2 = event_schema.BoolEventDataType('other')
        field1a = event_schema.StructureFieldType(dt_bool1, False)
        field1b = event_schema.StructureFieldType(dt_bool1, False)
        field2 = event_schema.StructureFieldType(dt_bool1, True)
        field3 = event_schema.StructureFieldType(dt_bool2, False)

        self.assertTrue(field1a.__eq__(field1a))
        self.assertFalse(field1a.__ne__(field1a))
        self.assertTrue(field1a == field1b)
        self.assertFalse(field1a != field1b)
        self.assertFalse(field1a == field2)
        self.assertTrue(field1a != field2)
        self.assertFalse(field1a == field3)
        self.assertTrue(field1a != field3)
        self.assertFalse(field1a == 'blah')
        self.assertTrue(field1a != 'blah')

    def test_hash(self) -> None:
        """Test that the object has a hash code, and is thus capable of being hashed"""
        res = {event_schema.StructureFieldType(event_schema.BoolEventDataType(None), False): 1}
        self.assertEqual(1, len(res))


class EventSchemaSelectorTest(unittest.TestCase):
    """Validations for selectors"""
    def test_validate_type_and_values(self) -> None:
        """the type and value validations"""
        type_1 = event_schema.BoolEventDataType(None)
        type_2 = event_schema.StringEventDataType(None, 0, 10)
        schema = event_schema.SelectorEventDataType(
            'des', {"t1": type_1, "2": type_2},
        )
        self.assertEqual('des', schema.description)
        self.assertEqual('selector', schema.type_name)
        self.assertEqual({'t1', '2'}, set(schema.selectors))
        self.assertEqual(type_1, schema.get_type_for('t1'))
        self.assertEqual(type_2, schema.get_type_for('2'))
        self.assertIsNone(schema.get_type_for('t2'))
        self.assertIsNone(schema.validate_type())

        self.assertTrue(schema.validate_value({"^": "t1", "$": True}))
        self.assertTrue(schema.validate_value({"^": "2", "$": "abc"}))

        self.assertFalse(schema.validate_value(None))
        self.assertFalse(schema.validate_value(1.0))
        self.assertFalse(schema.validate_value([1]))
        self.assertFalse(schema.validate_value("x"))
        self.assertFalse(schema.validate_value(set()))
        self.assertFalse(schema.validate_value({"x": "1"}))
        self.assertFalse(schema.validate_value({"^": "3", "$": 1}))
        self.assertFalse(schema.validate_value({"^": "2"}))
        self.assertFalse(schema.validate_value({"^": "2", "$": False}))

    def test_bad_type__1(self) -> None:
        """wrong number of selectors"""
        schema = event_schema.SelectorEventDataType('des', {})
        error = verified_not_none(schema.validate_type(), self)
        self.assertEqual(
            (
                UserMessage(
                    STANDARD_PETRONIA_CATALOG,
                    i18n(
                        'must have {MIN_TYPE_MAPPING_VALUES} to '
                        '{MAX_TYPE_MAPPING_VALUES} selectors ({count})',
                    ),
                    count=0, MIN_TYPE_MAPPING_VALUES=1, MAX_TYPE_MAPPING_VALUES=255,
                ),
            ),
            error.messages(),
        )

    def test_ok_type__2(self) -> None:
        """max number of selectors"""
        type_mapping: Dict[str, event_schema.AbcEventDataType] = {}
        for i in range(0, event_schema.MAX_TYPE_MAPPING_VALUES):
            type_mapping[str(i)] = event_schema.BoolEventDataType(None)
        schema = event_schema.SelectorEventDataType(None, type_mapping)
        self.assertIsNone(schema.validate_type())

    def test_bad_type__2(self) -> None:
        """wrong number of selectors"""
        type_mapping: Dict[str, event_schema.AbcEventDataType] = {}
        for i in range(0, event_schema.MAX_TYPE_MAPPING_VALUES + 1):
            type_mapping[str(i)] = event_schema.BoolEventDataType(None)
        schema = event_schema.SelectorEventDataType(None, type_mapping)
        error = verified_not_none(schema.validate_type(), self)
        self.assertEqual(
            (
                UserMessage(
                    STANDARD_PETRONIA_CATALOG,
                    i18n(
                        'must have {MIN_TYPE_MAPPING_VALUES} to '
                        '{MAX_TYPE_MAPPING_VALUES} selectors ({count})',
                    ),
                    count=256, MIN_TYPE_MAPPING_VALUES=1, MAX_TYPE_MAPPING_VALUES=255,
                ),
            ),
            error.messages(),
        )

    def test_bad_type__3(self) -> None:
        """wrong selector name size"""
        schema = event_schema.SelectorEventDataType(None, {
            "": event_schema.BoolEventDataType(None),
            ("x" * (event_schema.MAX_TYPE_MAPPING_KEY_LENGTH + 1)):
                event_schema.BoolEventDataType(None),
        })
        error = verified_not_none(schema.validate_type(), self)
        self.assertEqual(
            {
                UserMessage(
                    STANDARD_PETRONIA_CATALOG,
                    i18n('selector ({selector}) must have {n} to {x} characters'),
                    selector='', n=1, x=255,
                ),
                UserMessage(
                    STANDARD_PETRONIA_CATALOG,
                    i18n('selector ({selector}) must have {n} to {x} characters'),
                    selector='x' * 256,
                    n=1, x=255,
                ),
            },
            set(error.messages()),
        )

    def test_bad_type__4(self) -> None:
        """bad subtype"""
        schema = event_schema.SelectorEventDataType(None, {
            "x": event_schema.ReferenceEventDataType(None, "x"),
        })
        error = verified_not_none(schema.validate_type(), self)
        self.assertEqual(
            (
                UserMessage(STANDARD_PETRONIA_CATALOG, i18n('`reference` type not replaced')),
            ),
            error.messages(),
        )


class EventTypeTest(unittest.TestCase):
    """Test out the EventType class"""

    def test_getters(self) -> None:
        """Test out the getter functions."""
        schema = event_schema.StructureEventDataType('data', {})
        event = event_schema.EventType(
            'event-name', 'high', 'public', 'internal', schema, 'the-target',
        )
        self.assertEqual('event-name', event.name)
        self.assertEqual('high', event.priority)
        self.assertEqual('public', event.send_access)
        self.assertEqual('internal', event.receive_access)
        self.assertIs(schema, event.structure)
        self.assertEqual('the-target', event.unique_target)

    def test_validate_type__ok(self) -> None:
        """Test out the validate_type with no problems."""
        schema = event_schema.StructureEventDataType('data', {})
        event = event_schema.EventType(
            'event-name', 'high', 'public', 'internal', schema, 'the-target',
        )
        self.assertIsNone(event.validate_type())

    def test_validate_type__bad(self) -> None:
        """Test out the validate_type with a bad schema."""
        schema_bad = event_schema.SelectorEventDataType('des', {})
        schema = event_schema.StructureEventDataType(None, {
            'foo': event_schema.StructureFieldType(schema_bad, False),
        })
        event = event_schema.EventType(
            'event-name', 'high', 'public', 'internal', schema, 'the-target',
        )
        results = event.validate_type()
        self.assertIsNotNone(results)
        assert results is not None  # mypy requirement
        self.assertEqual(1, len(results.messages()))
        # We don't care what the message is (that's tested above), just that the
        # inner bad message is added.
