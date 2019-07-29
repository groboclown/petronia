
import unittest
from typing import Optional
from ..serial.converter import (
    serialize_to_json,
    deserialize_from_json,
    #serialize_value,
    #deserialize_value,
    create_instance,
)

class TestCreateInstance(unittest.TestCase):
    def test_valid_simple(self) -> None:
        val = create_instance(__name__ + '.SimpleInstance', {})
        self.assertIsInstance(val, SimpleInstance)

    def test_valid_with_args(self) -> None:
        val = create_instance(__name__ + '.WithArguments', {
            'v1': 'this is v1',
            'v2': 2,
        })
        self.assertIsInstance(val, WithArguments)
        self.assertEqual(val.v1, 'this is v1')
        self.assertEqual(val.v2, 2)

    def test_invalid_no_module(self) -> None:
        create_instance('object', {})

    def test_invalid_too_many_args(self) -> None:
        create_instance(__name__ + '.SimpleInstance', { 'x': 1 })

    def test_invalid_too_few_args(self) -> None:
        create_instance(__name__ + '.WithArguments', { 'v2': 1 })

    def test_invalid_wrong_args(self) -> None:
        create_instance(__name__ + '.WithArguments', { 'x': 1 })


class TestSerialize(unittest.TestCase):
    def test_reserialize_int(self) -> None:
        serialized = serialize_to_json(1)
        back = deserialize_from_json(serialized)
        self.assertEqual(back, 1)

    def test_reserialize_simple(self) -> None:
        serialized = serialize_to_json(SimpleInstance())
        back = deserialize_from_json(serialized)
        self.assertIsInstance(back, SimpleInstance)

    def test_reserialize_args(self) -> None:
        serialized = serialize_to_json(WithArguments('x', 2))
        back = deserialize_from_json(serialized)
        self.assertIsInstance(back, WithArguments)
        self.assertEqual(back.v1, 'x')
        self.assertEqual(back.v2, 2)

    def test_reserialize_recursive(self) -> None:
        r1 = Recursive(0, None, None)
        r2 = Recursive(1, r1, r1)
        r3 = Recursive(2, r1, r2)
        serialized = serialize_to_json(r3)
        back = deserialize_from_json(serialized)
        self.assertIsInstance(back, Recursive)
        self.assertEqual(back.v, 2)
        self.assertEqual(back.r1.v, 0)
        self.assertEqual(back.r2.v, 1)
        self.assertIsNone(back.r1.r1)
        self.assertIsNone(back.r1.r2)
        self.assertIs(back.r1, back.r2.r1)
        self.assertIs(back.r1, back.r2.r2)



class SimpleInstance:
    __slots__ = ()
    def __init__(self) -> None:
        pass

class WithArguments:
    __slots__ = ('_v1', '_v2',)

    def __init__(self, v1: str, v2: int) -> None:
        self._v1 = v1
        self._v2 = v2

    @property
    def v1(self) -> str:
        return self._v1

    @property
    def v2(self) -> int:
        return self._v2

class Recursive:
    __slots__ = ('__r1', '__r2', '__v')

    def __init__(self, v: int, r1: Optional['Recursive'], r2: Optional['Recursive']) -> None:
        self.__v = v
        self.__r1 = r1
        self.__r2 = r2

    @property
    def v(self) -> int:
        return self.__v

    @property
    def r1(self) -> Optional['Recursive']:
        return self.__r1

    @property
    def r2(self) -> Optional['Recursive']:
        return self.__r2
