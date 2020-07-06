
"""Test the memory module."""

from typing import Dict, cast
import unittest
from .. import memory


class MemoryTest(unittest.TestCase):
    """Test the stand-alone functions and simple classes"""
    def test_value_holder(self) -> None:
        """ValueHolder standard use case test"""
        holder = memory.ValueHolder('x')

        def t1_f() -> None:
            holder.value = 'y'

        def t2_f() -> None:
            holder.value = 'z'

        self.assertEqual('x', holder.value)
        t1_f()
        self.assertEqual('y', holder.value)
        t2_f()
        self.assertEqual('z', holder.value)

    def test_delayed_value_holder(self) -> None:
        """DelayedValueHolder standard use case"""
        holder: memory.DelayedValueHolder[str] = memory.DelayedValueHolder()

        def t1_f() -> None:
            holder.value = 'z'

        self.assertFalse(holder.has_value())
        t1_f()
        self.assertEqual('z', holder.value)
        self.assertEqual('z', holder.non_none)

    def test_readonly_dict_1(self) -> None:
        """readonly_dict normal usage"""
        dv_1 = {"a": 1}
        dv_2 = memory.readonly_dict(dv_1)
        dv_3 = memory.readonly_dict(dv_2)
        self.assertIs(dv_2, dv_3)
        self.assertEqual(dv_1, dv_2)
        self.assertEqual(["a"], list(dv_2.keys()))
        self.assertEqual([1], list(dv_2.values()))
        self.assertEqual(1, dv_2["a"])
        self.assertEqual(1, dv_2.get("a"))
        self.assertEqual(2, dv_2.get("b", 2))
        self.assertIsNone(dv_2.get("c"))

    def test_readonly_dict_2(self) -> None:
        """readonly_dict unsupported actions"""
        dv_1: Dict[str, int] = {"a": 1}
        dv_2: Dict[str, int] = cast(Dict[str, int], memory.readonly_dict(dv_1))
        try:
            del dv_2['a']
            self.fail('Should have thrown a runtime error')  # pragma: no cover
        except RuntimeError:
            pass

    def test_readonly_dict_3(self) -> None:
        """readonly_dict unsupported actions"""
        dv_1: Dict[str, int] = {"a": 1}
        dv_2: Dict[str, int] = cast(Dict[str, int], memory.readonly_dict(dv_1))

        try:
            dv_2['a'] = 1
            self.fail('Should have thrown a runtime error')  # pragma: no cover
        except RuntimeError:
            pass

    def test_readonly_dict_4(self) -> None:
        """readonly_dict unsupported actions"""
        dv_1: Dict[str, int] = {"a": 1}
        dv_2: Dict[str, int] = cast(Dict[str, int], memory.readonly_dict(dv_1))

        try:
            dv_2.pop('a')
            self.fail('Should have thrown a runtime error')  # pragma: no cover
        except RuntimeError:
            pass

    def test_readonly_dict_5(self) -> None:
        """readonly_dict unsupported actions"""
        dv_1: Dict[str, int] = {"a": 1}
        dv_2: Dict[str, int] = cast(Dict[str, int], memory.readonly_dict(dv_1))

        try:
            dv_2.popitem()
            self.fail('Should have thrown a runtime error')  # pragma: no cover
        except RuntimeError:
            pass

    def test_readonly_dict_6(self) -> None:
        """readonly_dict unsupported actions"""
        dv_1: Dict[str, int] = {"a": 1}
        dv_2: Dict[str, int] = cast(Dict[str, int], memory.readonly_dict(dv_1))

        try:
            dv_2.update({'x': 1})
            self.fail('Should have thrown a runtime error')  # pragma: no cover
        except RuntimeError:
            pass

    def test_readonly_dict_7(self) -> None:
        """readonly_dict unsupported actions"""
        dv_1: Dict[str, int] = {"a": 1}
        dv_2: Dict[str, int] = cast(Dict[str, int], memory.readonly_dict(dv_1))

        try:
            dv_2.clear()
            self.fail('Should have thrown a runtime error')  # pragma: no cover
        except RuntimeError:
            pass

    def test_readonly_dict_8(self) -> None:
        """readonly_dict unsupported actions"""
        dv_1: Dict[str, int] = {"a": 1}
        dv_2: Dict[str, int] = cast(Dict[str, int], memory.readonly_dict(dv_1))

        try:
            dv_2.setdefault("b", 2)
            self.fail('Should have thrown a runtime error')  # pragma: no cover
        except RuntimeError:
            pass
