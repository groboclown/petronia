"""Test the module."""

from typing import Sequence, Tuple, Dict, Set, Union, Any, cast
import unittest
from petronia_common.util import STRING_EMPTY_TUPLE
from .. import embedded_json_data as ejd


class EmbeddedJsonDataTest(unittest.TestCase):
    """Test the functions in the data."""

    def test_embedded_json_data__ok(self) -> None:
        """Test embedded_json_data for ok data."""
        res = ejd.embedded_json_data('{}')
        self.assertIsNone(res.error)
        self.assertEqual({}, res.result)

    def test_embedded_json_data__none(self) -> None:
        """Test embedded_json_data with None input."""
        res = ejd.embedded_json_data(None)
        self.assertIsNone(res.error)
        self.assertIsNone(res.value)

    def test_embedded_json_data__error(self) -> None:
        """Test embedded_json_data for bad data"""
        res = ejd.embedded_json_data('{')
        self.assertIsNotNone(res.error)
        self.assertEqual(
            ['invalid embedded JSON data'],
            [m.debug() for m in res.error_messages()],
        )

    def test_as_structured(self) -> None:
        """Test lots of data types going into as_structured"""
        valid: Sequence[ejd.StructuredDataType] = (
            ['a'], {'x': 'y'}, 'x', 1, 1.4, True, None,
        )
        for val in valid:
            with self.subTest(str(val)):
                self.assertIs(val, ejd.as_structured(val))

        self.assertIsNone(ejd.as_structured(object()))

    def test_json_str(self) -> None:
        """Test lots of data tyeps going into json_str"""
        valid: Sequence[Tuple[ejd.StructuredDataType, str]] = (
            ('abc', 'abc'), (1, '1'), (1.5, '1.5'), (True, 'True'),
        )
        invalid: Sequence[ejd.StructuredDataType] = (
            {'x': 'y'}, [1], None,
        )
        for val, expected in valid:
            with self.subTest(str(val)):
                self.assertEqual(expected, ejd.json_str(val))
        for val in invalid:
            with self.subTest(str(val)):
                self.assertIsNone(ejd.json_str(val))

    def test_json_int(self) -> None:
        """Test lots of data tyeps going into json_int"""
        valid: Sequence[Tuple[ejd.StructuredDataType, int]] = (
            (12, 12),
            (1.2, 1), (1.9, 1),
            ('12', 12), ('0x10', 16), ('0X10', 16), ('0b10', 2), ('0xa', 10), ('-6', -6),
            (True, 1), (False, 0),
        )
        invalid: Sequence[ejd.StructuredDataType] = (
            {'x': 'y'}, [1], 'abc', '1.9', None,
        )
        for val, expected in valid:
            with self.subTest(str(val)):
                self.assertEqual(expected, ejd.json_int(val))
        for val in invalid:
            with self.subTest(str(val)):
                self.assertIsNone(ejd.json_int(val))

    def test_json_float(self) -> None:
        """Test lots of data tyeps going into json_float"""
        valid: Sequence[Tuple[ejd.StructuredDataType, float]] = (
            (12, 12.0),
            (1.2, 1.2), (1.9, 1.9),
            (True, 1.0), (False, 0.0),
            ('1', 1.0), ('1.9', 1.9), ('-1e2', -100.0),
        )
        invalid: Sequence[ejd.StructuredDataType] = (
            {'x': 'y'}, [1], 'abc', None, '0xa',
        )
        for val, expected in valid:
            with self.subTest(str(val)):
                self.assertEqual(expected, ejd.json_float(val))
        for val in invalid:
            with self.subTest(str(val)):
                self.assertIsNone(ejd.json_float(val))

    def test_json_bool(self) -> None:
        """Test lots of data tyeps going into json_bool"""
        valid: Sequence[Tuple[ejd.StructuredDataType, float]] = (
            (12, True), (0, False),
            (1.2, True), (0.0, False),
            (True, True), (False, False),
            ('1', True), ('on', True), ('Active', True), ('no', False),
        )
        invalid: Sequence[ejd.StructuredDataType] = (
            {'x': 'y'}, [1], None,
        )
        for val, expected in valid:
            with self.subTest(str(val)):
                self.assertEqual(expected, ejd.json_bool(val))
        for val in invalid:
            with self.subTest(str(val)):
                self.assertIsNone(ejd.json_bool(val))

    def test_json_array(self) -> None:
        """Test lots of data types going into json_array"""
        valid: Sequence[ejd.StructuredDataType] = (
            ('a',),  [1, 2], ('a', {'x': 1}),
        )
        invalid: Sequence[ejd.StructuredDataType] = (
            {'x': 'y'}, 'abc', None, '0xa', 1, 1.5, False,
        )
        for val in valid:
            with self.subTest(str(val)):
                # MyPy work-around - the casting.
                self.assertEqual(tuple(cast(Sequence[str], val)), ejd.json_array(val))
        for val in invalid:
            with self.subTest(str(val)):
                self.assertIsNone(ejd.json_array(val))

    def test_json_iter_array(self) -> None:
        """Test lots of data types going into json_iter_array"""
        valid: Sequence[Tuple[
            Sequence[str], Sequence[Any], Sequence[Tuple[Sequence[str], ejd.StructuredDataType]],
        ]] = (
            (
                STRING_EMPTY_TUPLE,
                [],
                (),
            ),
            (
                ('a', 'x1',),
                [1, 'b', 3],
                ((('a', 'x1', '0'), 1), (('a', 'x1', '1'), 'b'), (('a', 'x1', '2'), 3)),
            ),
            (
                ('x1',),
                [],
                (),
            ),
            (
                STRING_EMPTY_TUPLE,
                [{'x': 'y'}, 5, [], None],
                ((('0',), {'x': 'y'}), (('1',), 5), (('2',), []), (('3',), None)),
            ),
        )
        for src_path, src_sequence, expected in valid:
            with self.subTest(str(src_path)):
                self.assertEqual(expected, tuple(ejd.json_iter_array(src_path, src_sequence)))

    def test_json_map(self) -> None:
        """Test lots of data types going into json_map"""
        valid: Sequence[ejd.StructuredDataType] = (
            {'x': 'y'}, {'aa': ['1', '2']},
        )
        invalid: Sequence[ejd.StructuredDataType] = (
            'x', 'asdf', ['abc'], [{'1': 2}], None, 5,
        )
        for val in valid:
            with self.subTest(str(val)):
                self.assertIs(val, ejd.json_map(val))
        for val in invalid:
            with self.subTest(str(val)):
                self.assertIsNone(ejd.json_map(val))

    def test_json_iter_map(self) -> None:
        """Test lots of data types going into json_iter_map"""
        valid: Sequence[Tuple[
            Sequence[str],
            Dict[str, Any],
            Set[Any],
        ]] = (
            (
                STRING_EMPTY_TUPLE,
                cast(Dict[str, Any], {}),
                set(),
            ),
            (
                ('a',),
                cast(Dict[str, Any], {}),
                set(),
            ),
            (
                STRING_EMPTY_TUPLE,
                {'x': 'y'},
                {(('x',), 'x', 'y')},
            ),
            (
                ('x1', 'y1',),
                {'a1': 1, 'b2': (1,)},
                {(('x1', 'y1', 'a1'), 'a1', 1), (('x1', 'y1', 'b2'), 'b2', (1,))},
            ),
        )
        for src_path, src_val, expected in valid:
            with self.subTest(str(src_path)):
                self.assertEqual(expected, set(ejd.json_iter_map(src_path, src_val)))

    def test_json_map_value_options(self) -> None:
        """Test json_map_value_options"""
        self.assertIsNone(ejd.json_map_value_options({}, 'abc'))
        self.assertEqual(
            ('abc', 12),
            ejd.json_map_value_options({'abc': 12, '123': 99}, 'abc'),
        )
        self.assertEqual(
            ('abc', 12),
            ejd.json_map_value_options({'abc': 12}, ['123', 'abc']),
        )
        self.assertEqual(
            ('ABC', 12),
            ejd.json_map_value_options({'ABC': 12}, ['123', 'abc', 'def']),
        )

    def test_json_map_str(self) -> None:
        """Test json_map_str"""
        test_data: Sequence[Tuple[
            Sequence[str], Dict[str, Any], Union[str, Sequence[str]], Sequence[str], Any,
        ]] = [
            ((), {}, 'a', (), None),
            ((), {'abc': 'x'}, 'abc', ('abc',), 'x'),
            # str conversion turns 123 into '123'
            (('a', 'b',), {'abc': 123}, ['def', 'abc'], ('a', 'b', 'abc',), '123'),
            (('a', 'b',), {'abc': [6]}, 'abc', ('a', 'b', 'abc',), None),
        ]

        for src_path, src_map, src_key, expected_path, expected_val in test_data:
            with self.subTest(repr(src_path)):
                self.assertEqual(
                    (expected_path, expected_val),
                    ejd.json_map_str(src_path, src_map, src_key),
                )

    def test_json_map_int(self) -> None:
        """Test json_map_int"""
        test_data: Sequence[Tuple[
            Sequence[str], Dict[str, Any], Union[str, Sequence[str]], Sequence[str], Any,
        ]] = [
            ((), {}, 'a', (), None),
            ((), {'abc': 66}, 'abc', ('abc',), 66),
            # str conversion turns '-123' into -123
            (('a', 'b',), {'abc': '-123'}, ['def', 'abc'], ('a', 'b', 'abc',), -123),
        ]

        for src_path, src_map, src_key, expected_path, expected_val in test_data:
            with self.subTest(repr(src_path)):
                self.assertEqual(
                    (expected_path, expected_val),
                    ejd.json_map_int(src_path, src_map, src_key),
                )

    def test_json_map_float(self) -> None:
        """Test json_map_float"""
        test_data: Sequence[Tuple[
            Sequence[str], Dict[str, Any], Union[str, Sequence[str]], Sequence[str], Any,
        ]] = [
            ((), {}, 'a', (), None),
            ((), {'abc': 1.9}, 'abc', ('abc',), 1.9),
            # str conversion turns '-1e-3' into -1e-3
            (('a', 'b',), {'abc': '-1e-3'}, ['def', 'abc'], ('a', 'b', 'abc',), -1e-3),
        ]

        for src_path, src_map, src_key, expected_path, expected_val in test_data:
            with self.subTest(repr(src_path)):
                self.assertEqual(
                    (expected_path, expected_val),
                    ejd.json_map_float(src_path, src_map, src_key),
                )

    def test_json_map_bool(self) -> None:
        """Test json_map_bool"""
        test_data: Sequence[Tuple[
            Sequence[str], Dict[str, Any], Union[str, Sequence[str]], Sequence[str], Any,
        ]] = [
            ((), {}, 'a', (), None),
            ((), {'abc': False}, 'abc', ('abc',), False),
            # str conversion turns '1' into True
            (('a', 'b',), {'abc': '1'}, ['def', 'abc'], ('a', 'b', 'abc',), True),
        ]

        for src_path, src_map, src_key, expected_path, expected_val in test_data:
            with self.subTest(repr(src_path)):
                self.assertEqual(
                    (expected_path, expected_val),
                    ejd.json_map_bool(src_path, src_map, src_key),
                )

    def test_json_map_array(self) -> None:
        """Test json_map_array"""
        test_data: Sequence[Tuple[
            Sequence[str], Dict[str, Any], Union[str, Sequence[str]], Sequence[str], Any,
        ]] = [
            ((), {}, 'a', (), None),
            ((), {'abc': [9, 5]}, 'abc', ('abc',), (9, 5)),
            # str conversion turns '1' into True
            (('a', 'b',), {'abc': ['a', 6]}, ['def', 'abc'], ('a', 'b', 'abc',), ('a', 6)),
        ]

        for src_path, src_map, src_key, expected_path, expected_val in test_data:
            with self.subTest(repr(src_path)):
                self.assertEqual(
                    (expected_path, expected_val),
                    ejd.json_map_array(src_path, src_map, src_key),
                )

    def test_json_map_map(self) -> None:
        """Test json_map_map"""
        test_data: Sequence[Tuple[
            Sequence[str], Dict[str, Any], Union[str, Sequence[str]], Sequence[str], Any,
        ]] = [
            ((), {}, 'a', (), None),
            ((), {'abc': {'x': 'y'}}, 'abc', ('abc',), {'x': 'y'}),
            # str conversion turns '1' into True
            (('a', 'b',), {'abc': {'a': 1}}, ['def', 'abc'], ('a', 'b', 'abc',), {'a': 1}),
        ]

        for src_path, src_map, src_key, expected_path, expected_val in test_data:
            with self.subTest(repr(src_path)):
                self.assertEqual(
                    (expected_path, expected_val),
                    ejd.json_map_map(src_path, src_map, src_key),
                )
