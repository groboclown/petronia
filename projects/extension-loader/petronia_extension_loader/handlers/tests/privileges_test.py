"""Test the module"""

from typing import Set
import unittest
from petronia_common.extension.config import ExtensionDependency, StandAloneExtensionMetadata
from petronia_common.extension.config.event_schema import (
    PUBLIC_ACCESS, IMPLEMENTATIONS_ACCESS, TARGET_ACCESS, INTERNAL_ACCESS,
)
from petronia_common.extension.config.extension_schema import ExtensionRuntime
from .. import privileges
from ...tests.ext_util import (
    mk_standalone_ext, mk_protocol_ext, mk_impl_ext, mk_api_ext,
)
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
        standalone = mk_standalone_ext('n.a')
        res = privileges.get_source_id_prefix_access(standalone)
        self.assertEqual({'n.a:'}, res)
        impl = mk_impl_ext('n.b', impl=[('b.q', 1, 0, 0, -1, 0, 0)])
        res = privileges.get_source_id_prefix_access(impl)
        self.assertEqual({'n.b:', 'b.q:'}, res)

    def test_add_event_send_access__found(self) -> None:
        """Test add_event_send_access when the send has already been found."""
        standalone = mk_standalone_ext('n.a', depends=[('b.q', 1, 0, 0, -1, 0, 0)])
        res: Set[str] = set()
        privileges.add_event_send_access(res, standalone, False, {'n.a'}, [])
        self.assertEqual(set(), res)

    def test_add_event_send_access__standalone_no_deps(self) -> None:
        """Test add_event_send_access for a standalone extension with no dependencies"""
        standalone = ExtensionInfo([], StandAloneExtensionMetadata(
            'n.a', (1, 2, 3), '', '', [], [], [], ExtensionRuntime('l', {}),
        ))
        res: Set[str] = set()
        privileges.add_event_send_access(res, standalone, False, set(), [])
        self.assertEqual(set(), res)

    def test_add_event_send_access__api_impl(self) -> None:
        """Test add_event_send_access for an implementation of an api"""
        api = mk_api_ext(
            'n.api', ('n.impl', 1, 0, 0, -1, 0, 0), events=[
                ('ev_pub_pub', PUBLIC_ACCESS, PUBLIC_ACCESS),
                ('ev_pub_impl', PUBLIC_ACCESS, IMPLEMENTATIONS_ACCESS),
                ('ev_pub_target', PUBLIC_ACCESS, TARGET_ACCESS),
                ('ev_pub_internal', PUBLIC_ACCESS, INTERNAL_ACCESS),
                ('ev_impl_pub', IMPLEMENTATIONS_ACCESS, PUBLIC_ACCESS),
                ('ev_impl_impl', IMPLEMENTATIONS_ACCESS, IMPLEMENTATIONS_ACCESS),
                ('ev_impl_target', IMPLEMENTATIONS_ACCESS, TARGET_ACCESS),
                ('ev_impl_internal', IMPLEMENTATIONS_ACCESS, INTERNAL_ACCESS),
                ('ev_target_pub', TARGET_ACCESS, PUBLIC_ACCESS),
                ('ev_target_impl', TARGET_ACCESS, IMPLEMENTATIONS_ACCESS),
                ('ev_target_target', TARGET_ACCESS, TARGET_ACCESS),
                ('ev_target_internal', TARGET_ACCESS, INTERNAL_ACCESS),
                ('ev_internal_pub', INTERNAL_ACCESS, PUBLIC_ACCESS),
                ('ev_internal_impl', INTERNAL_ACCESS, IMPLEMENTATIONS_ACCESS),
                ('ev_internal_target', INTERNAL_ACCESS, TARGET_ACCESS),
                ('ev_internal_internal', INTERNAL_ACCESS, INTERNAL_ACCESS),
            ],
        )
        res: Set[str] = set()
        privileges.add_event_send_access(res, api, True, set(), [])
        self.assertEqual({
            'ev_impl_impl',
            'ev_impl_internal',
            'ev_impl_pub',
            'ev_impl_target',
            'ev_pub_impl',
            'ev_pub_internal',
            'ev_pub_pub',
            'ev_pub_target',
            'ev_target_impl',
            'ev_target_internal',
            'ev_target_pub',
            'ev_target_target',
        }, res)

    def test_add_event_send_access__api_depend(self) -> None:
        """Test add_event_send_access for an extension that depends on an api"""
        api = mk_api_ext(
            'n.api', ('n.impl', 1, 0, 0, -1, 0, 0), events=[
                ('ev_pub_pub', PUBLIC_ACCESS, PUBLIC_ACCESS),
                ('ev_pub_impl', PUBLIC_ACCESS, IMPLEMENTATIONS_ACCESS),
                ('ev_pub_target', PUBLIC_ACCESS, TARGET_ACCESS),
                ('ev_pub_internal', PUBLIC_ACCESS, INTERNAL_ACCESS),
                ('ev_impl_pub', IMPLEMENTATIONS_ACCESS, PUBLIC_ACCESS),
                ('ev_impl_impl', IMPLEMENTATIONS_ACCESS, IMPLEMENTATIONS_ACCESS),
                ('ev_impl_target', IMPLEMENTATIONS_ACCESS, TARGET_ACCESS),
                ('ev_impl_internal', IMPLEMENTATIONS_ACCESS, INTERNAL_ACCESS),
                ('ev_target_pub', TARGET_ACCESS, PUBLIC_ACCESS),
                ('ev_target_impl', TARGET_ACCESS, IMPLEMENTATIONS_ACCESS),
                ('ev_target_target', TARGET_ACCESS, TARGET_ACCESS),
                ('ev_target_internal', TARGET_ACCESS, INTERNAL_ACCESS),
                ('ev_internal_pub', INTERNAL_ACCESS, PUBLIC_ACCESS),
                ('ev_internal_impl', INTERNAL_ACCESS, IMPLEMENTATIONS_ACCESS),
                ('ev_internal_target', INTERNAL_ACCESS, TARGET_ACCESS),
                ('ev_internal_internal', INTERNAL_ACCESS, INTERNAL_ACCESS),
            ],
        )
        res: Set[str] = set()
        privileges.add_event_send_access(res, api, False, set(), [])
        self.assertEqual({
            'ev_pub_impl',
            'ev_pub_internal',
            'ev_pub_pub',
            'ev_pub_target',
            'ev_target_impl',
            'ev_target_internal',
            'ev_target_pub',
            'ev_target_target',
        }, res)

    def test_add_event_send_access__protocol(self) -> None:
        """Test add_event_send_access for a dependency on a protocol"""
        protocol = mk_protocol_ext(
            'n.protocol', events=[
                ('ev1', PUBLIC_ACCESS, PUBLIC_ACCESS),
                ('ev2', PUBLIC_ACCESS, PUBLIC_ACCESS),
            ],
        )
        res: Set[str] = set()
        privileges.add_event_send_access(res, protocol, True, set(), [])
        self.assertEqual({'ev1', 'ev2'}, res)

    def test_add_event_send_access__impl(self) -> None:
        """Test add_event_send_access for an implementation that also has a dependency"""
        protocol = mk_protocol_ext(
            'n.protocol', events=[
                ('ev1', PUBLIC_ACCESS, PUBLIC_ACCESS),
                ('ev2', PUBLIC_ACCESS, PUBLIC_ACCESS),
            ],
        )
        api1 = mk_api_ext(
            'n.api1', ('n.impl', 1, 0, 0, -1, 0, 0), events=[
                ('ev3', IMPLEMENTATIONS_ACCESS, PUBLIC_ACCESS),
                ('ev4', PUBLIC_ACCESS, IMPLEMENTATIONS_ACCESS),
            ],
        )
        api2 = mk_api_ext(
            'n.api2', ('n.impl', 1, 0, 0, -1, 0, 0), events=[
                ('ev5', IMPLEMENTATIONS_ACCESS, PUBLIC_ACCESS),
                ('ev6', PUBLIC_ACCESS, IMPLEMENTATIONS_ACCESS),
            ],
        )
        impl1 = mk_impl_ext(
            'n.impl1',
            depends=[],
            impl=[('n.api1', 0, 9, 0, 1, 9, 9)],
        )
        impl2 = mk_impl_ext(
            'n.impl2',
            depends=[
                ('n.protocol', 0, 1, 0, 2, 0, 0),
                ('n.impl1', 0, 1, 0, 2, 0, 0),

                # A dependency that isn't registered.  The code silently
                # ignores this problem.
                ('n.does-not-exist', 0, 1, 0, 2, 0, 0),
            ],
            impl=[('n.api2', 0, 9, 0, 1, 9, 9)],
        )
        res: Set[str] = set()
        privileges.add_event_send_access(res, impl2, True, set(), [
            protocol, api1, api2, impl1, impl2,
        ])
        self.assertEqual({'ev1', 'ev2', 'ev4', 'ev5', 'ev6'}, res)
