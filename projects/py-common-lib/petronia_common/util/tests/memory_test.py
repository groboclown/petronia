
from typing import Dict, cast
import unittest
from .. import memory


class MemoryTest(unittest.TestCase):
    def test_value_holder(self) -> None:
        # Standard use case.
        holder = memory.ValueHolder('x')

        def t1() -> None:
            holder.value = 'y'

        def t2() -> None:
            holder.value = 'z'

        self.assertEqual('x', holder.value)
        t1()
        self.assertEqual('y', holder.value)
        t2()
        self.assertEqual('z', holder.value)

    def test_delayed_value_holder(self) -> None:
        # Standard use case
        holder: memory.DelayedValueHolder[str] = memory.DelayedValueHolder()

        def t1() -> None:
            holder.value = 'z'

        self.assertFalse(holder.has_value())
        t1()
        self.assertEqual('z', holder.value)
        self.assertEqual('z', holder.non_none)

    def test_readonly_dict_1(self) -> None:
        d1 = {"a": 1}
        d2 = memory.readonly_dict(d1)
        d3 = memory.readonly_dict(d2)
        self.assertIs(d2, d3)
        self.assertEqual(d1, d2)
        self.assertEqual(["a"], list(d2.keys()))
        self.assertEqual([1], list(d2.values()))
        self.assertEqual(1, d2["a"])
        self.assertEqual(1, d2.get("a"))
        self.assertEqual(2, d2.get("b", 2))
        self.assertIsNone(d2.get("c"))

    def test_readonly_dict_2(self) -> None:
        d1: Dict[str, int] = {"a": 1}
        d2: Dict[str, int] = cast(Dict[str, int], memory.readonly_dict(d1))
        try:
            del d2['a']
            self.fail('Should have thrown a runtime error')  # pragma: no cover
        except RuntimeError:
            pass

    def test_readonly_dict_3(self) -> None:
        d1: Dict[str, int] = {"a": 1}
        d2: Dict[str, int] = cast(Dict[str, int], memory.readonly_dict(d1))

        try:
            d2['a'] = 1
            self.fail('Should have thrown a runtime error')  # pragma: no cover
        except RuntimeError:
            pass

    def test_readonly_dict_4(self) -> None:
        d1: Dict[str, int] = {"a": 1}
        d2: Dict[str, int] = cast(Dict[str, int], memory.readonly_dict(d1))

        try:
            d2.pop('a')
            self.fail('Should have thrown a runtime error')  # pragma: no cover
        except RuntimeError:
            pass

    def test_readonly_dict_5(self) -> None:
        d1: Dict[str, int] = {"a": 1}
        d2: Dict[str, int] = cast(Dict[str, int], memory.readonly_dict(d1))

        try:
            d2.popitem()
            self.fail('Should have thrown a runtime error')  # pragma: no cover
        except RuntimeError:
            pass

    def test_readonly_dict_6(self) -> None:
        d1: Dict[str, int] = {"a": 1}
        d2: Dict[str, int] = cast(Dict[str, int], memory.readonly_dict(d1))

        try:
            d2.update({'x': 1})
            self.fail('Should have thrown a runtime error')  # pragma: no cover
        except RuntimeError:
            pass

    def test_readonly_dict_7(self) -> None:
        d1: Dict[str, int] = {"a": 1}
        d2: Dict[str, int] = cast(Dict[str, int], memory.readonly_dict(d1))

        try:
            d2.clear()
            self.fail('Should have thrown a runtime error')  # pragma: no cover
        except RuntimeError:
            pass

    def test_readonly_dict_8(self) -> None:
        d1: Dict[str, int] = {"a": 1}
        d2: Dict[str, int] = cast(Dict[str, int], memory.readonly_dict(d1))

        try:
            d2.setdefault("b", 2)
            self.fail('Should have thrown a runtime error')  # pragma: no cover
        except RuntimeError:
            pass
