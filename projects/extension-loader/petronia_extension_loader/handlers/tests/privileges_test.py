"""Test the module"""

from typing import Set
import unittest
from petronia_common.extension.config import ExtensionDependency, StandAloneExtensionMetadata
from petronia_common.extension.config.extension_schema import (
    ExtensionRuntime, ImplExtensionMetadata,
)
from .. import privileges
from ...defs import ExtensionInfo


class PrivilegesTest(unittest.TestCase):
    """Test the functions."""

    def test_create_source_id_prefix(self) -> None:
        """Test create_source_id_prefix"""
        dep = ExtensionDependency('n.b.c', (1, 2, 3), None)
        res = privileges.create_source_id_prefix(dep)
        self.assertEqual('n.b.c:', res)

    def test_get_source_id_prefix_access(self) -> None:
        """Test get_source_id_prefix_access"""
        standalone = ExtensionInfo([], StandAloneExtensionMetadata(
            'n.a', (1, 2, 3), '', '', [], [], [], ExtensionRuntime('l', {}),
        ))
        res = privileges.get_source_id_prefix_access(standalone)
        self.assertEqual({'n.a:'}, res)
        impl = ExtensionInfo([], ImplExtensionMetadata(
            'n.b', (3, 2, 1), '', '', [], [], [],
            [ExtensionDependency('b.q', (1, 0, 0), None)], ExtensionRuntime('x', {}),
        ))
        res = privileges.get_source_id_prefix_access(impl)
        self.assertEqual({'n.b:', 'b.q:'}, res)

    def test_add_event_send_access__standalone_no_deps(self) -> None:
        """Test add_event_send_access for a standalone extension with no dependencies"""
        standalone = ExtensionInfo([], StandAloneExtensionMetadata(
            'n.a', (1, 2, 3), '', '', [], [], [], ExtensionRuntime('l', {}),
        ))
        res: Set[str] = set()
        privileges.add_event_send_access(res, standalone, False, set(), [])
        self.assertEqual(set(), res)
