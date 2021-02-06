"""Test the module"""

import unittest
from petronia_common.extension.config import (
    ApiExtensionMetadata,
)
from .ext_util import (
    mk_protocol_ext, mk_standalone_ext, mk_impl_ext, mk_api_ext,
)
from .. import order
from ..defs import ExtensionInfo


class GeneralOrderTest(unittest.TestCase):
    """Test the ExtensionDependencyOrder class and the get_load_order function."""

    def test_edo__no_dependencies__no_required_by(self) -> None:
        """Test the methods when the extension has no dependencies and is not required."""
        edo = order.ExtensionDependencyOrder(mk_standalone_ext('n'), [], [])
        self.assertTrue(edo.is_root())
        self.assertEqual([], edo.depends_on)
        self.assertEqual([], edo.required_by)
        self.assertTrue(edo.can_run([]))
        self.assertEqual(
            (),
            tuple(edo.get_everything_requiring({
                'x1': order.ExtensionDependencyOrder(mk_standalone_ext('a1'), [], []),
            })),
        )
        self.assertEqual([], edo.get_ext_dependencies())

    def test_use_case__diamond(self) -> None:
        """Test the ordering when there's a "deadly diamond" dependency tree."""
        impl1 = mk_impl_ext(
            'impl1',
            impl=[('api1', 1, 0, 0, -1, 0, 0)],
            depends=[('api2', 1, 0, 0, -1, 0, 0)],
        )
        impl2 = mk_impl_ext(
            'impl2',
            impl=[('api2', 1, 0, 0, -1, 0, 0)],
        )
        api1 = mk_api_ext(
            'api1',
            ('impl1a', 1, 0, 0, 2, 0, 0),
            depends=[('proto1', 1, 0, 0, -1, 0, 0)],
        )
        api2 = mk_api_ext(
            'api2',
            ('impl1b', 1, 0, 0, 2, 0, 0),
            depends=[('proto1', 1, 0, 0, -1, 0, 0)],
        )
        proto1 = mk_protocol_ext('proto1')
        world = {
            impl1.name: impl1,
            impl2.name: impl2,
            api1.name: api1,
            api2.name: api2,
            proto1.name: proto1,
        }
        order_res = order.get_load_order([impl1, impl2], world.values())
        self.assertIsNone(order_res.error)
        loaded = {
            ext.ext.name: ext
            for ext in order_res.result
        }
        self.assertEqual(
            {'impl1', 'impl2', 'api1', 'api2', 'proto1'},
            set(loaded.keys()),
        )

        self.assertEqual(
            [],
            [info.name for info in loaded['proto1'].depends_on],
        )
        self.assertEqual(
            {'api1', 'api2'},
            {info.name for info in loaded['proto1'].required_by}
        )
        self.assertEqual(
            {'impl1', 'impl2', 'api1', 'api2'},
            {info.name for info in loaded['proto1'].get_everything_requiring(loaded)},
        )
        self.assertTrue(loaded['proto1'].can_run([]))
        self.assertTrue(loaded['proto1'].can_run(world.values()))

        self.assertEqual(
            ['proto1'],
            [info.name for info in loaded['api1'].depends_on],
        )
        self.assertEqual(
            ['impl1'],
            [info.name for info in loaded['api1'].required_by],
        )
        self.assertEqual(
            {'impl1'},
            {info.name for info in loaded['api1'].get_everything_requiring(loaded)},
        )
        self.assertFalse(loaded['impl1'].can_run([]))
        self.assertFalse(loaded['impl1'].can_run([world['proto1']]))
        self.assertTrue(loaded['impl1'].can_run(world.values()))
        self.assertTrue(loaded['impl1'].can_run([
            world['proto1'], world['api1'], world['api2'],
        ]))

        self.assertEqual(
            ['proto1'],
            [info.name for info in loaded['api2'].depends_on],
        )
        self.assertEqual(
            {'impl1', 'impl2'},
            {info.name for info in loaded['api2'].required_by},
        )
        self.assertEqual(
            {'impl1', 'impl2'},
            {info.name for info in loaded['api2'].get_everything_requiring(loaded)},
        )
        self.assertEqual(
            {'proto1'},
            {info.name for info in loaded['api2'].get_ext_dependencies()},
        )

        self.assertEqual(
            {'api1', 'api2'},
            {info.name for info in loaded['impl1'].depends_on},
        )
        self.assertEqual(
            [],
            [info.name for info in loaded['impl1'].required_by],
        )
        self.assertEqual(
            {'api1', 'api2'},
            {info.name for info in loaded['impl1'].get_ext_dependencies()},
        )

        self.assertEqual(
            {'api2'},
            {info.name for info in loaded['impl2'].depends_on},
        )
        self.assertEqual(
            [],
            [info.name for info in loaded['impl2'].required_by],
        )
        self.assertEqual(
            {'api2'},
            {info.name for info in loaded['impl2'].get_ext_dependencies()},
        )

        # Extra interesting test...
        self.assertEqual([], list(loaded['proto1'].get_everything_requiring({})))

    def test_get_load_order__default_impl(self) -> None:
        """Test get_load_order, loading the default impl for an API."""
        impl1 = mk_impl_ext(
            'impl1',
            impl=[('api1', 1, 0, 0, -1, 0, 0)],
            depends=[('api2', 1, 0, 0, -1, 0, 0)],
        )
        impl2 = mk_impl_ext(
            'impl2',
            impl=[('api2', 1, 0, 0, -1, 0, 0)],
        )
        api1 = mk_api_ext(
            'api1',
            ('impl1', 1, 0, 0, 2, 0, 0),
            depends=[('proto1', 1, 0, 0, -1, 0, 0)],
        )
        api2 = mk_api_ext(
            'api2',
            ('impl2', 1, 0, 0, 2, 0, 0),
            depends=[('proto1', 1, 0, 0, -1, 0, 0)],
        )
        proto1 = mk_protocol_ext('proto1')
        world = {
            impl1.name: impl1,
            impl2.name: impl2,
            api1.name: api1,
            api2.name: api2,
            proto1.name: proto1,
        }

        # Check Api -> default impl added.
        order_res = order.get_load_order([api1], world.values())
        self.assertIsNone(order_res.error)
        loaded = {
            ext.ext.name: ext
            for ext in order_res.result
        }
        self.assertEqual(
            {'impl1', 'impl2', 'api1', 'api2', 'proto1'},
            set(loaded.keys()),
        )

    def test_get_load_order__missing(self) -> None:
        """Test get_load_order with a missing dependency."""
        ext = mk_impl_ext('e1', impl=[('a', 1, 0, 0, -1, 0, 0)])
        res = order.get_load_order([ext], [ext])
        self.assertIsNotNone(res.error)
        self.assertEqual(
            ['extension e1 depends on not-found extension a [>=(1, 0, 0), <None]'],
            [m.debug() for m in res.error_messages()],
        )

    def test_get_load_order__api_impl_missing(self) -> None:
        """Test get_load_order with a missing dependency."""
        ext = mk_api_ext(
            'api1',
            ('impl1', 1, 0, 0, 2, 0, 0),
        )
        res = order.get_load_order([ext], [ext])
        self.assertIsNotNone(res.error)
        self.assertEqual(
            [
                'No implementation declared for API extension api1, and default extension '
                'impl1 not installed',
            ],
            [m.debug() for m in res.error_messages()],
        )

    def test_get_load_order__no_api_impl(self) -> None:
        """Test get_load_order with no api impl."""
        ext = ExtensionInfo([], ApiExtensionMetadata(
            'api1', (1, 0, 0), '', '', [], [], [], [], None,
        ))

        res = order.get_load_order([ext], [ext])
        self.assertIsNotNone(res.error)
        self.assertEqual(
            ['No implementation declared for API extension api1'],
            [m.debug() for m in res.error_messages()],
        )


class LoadListTest(unittest.TestCase):
    """Test the LoadList class."""

    def test_state_changes__success(self) -> None:
        """Run through the state change course."""
        load_list = order.LoadList()
        ext = mk_standalone_ext('a')

        self.assertTrue(
            load_list.add_one_pending(order.ExtensionDependencyOrder(ext, [], []))
        )
        self.assertTrue(load_list.is_pending('a'))
        self.assertFalse(load_list.is_loading('a'))
        self.assertFalse(load_list.is_loaded('a'))
        self.assertIsNone(load_list.get_loading_extension('a'))
        self.assertEqual([ext], list(load_list.get_ready_to_load()))
        self.assertEqual([], list(load_list.get_loaded()))
        self.assertFalse(
            load_list.add_one_pending(order.ExtensionDependencyOrder(ext, [], []))
        )

        load_list.mark_loading('a')
        self.assertFalse(load_list.is_pending('a'))
        self.assertTrue(load_list.is_loading('a'))
        self.assertFalse(load_list.is_loaded('a'))
        self.assertIs(ext, load_list.get_loading_extension('a'))
        self.assertEqual([], list(load_list.get_ready_to_load()))
        self.assertEqual([], list(load_list.get_loaded()))

        res = load_list.mark_loaded('a')
        self.assertIsNone(res.error)
        self.assertFalse(load_list.is_pending('a'))
        self.assertFalse(load_list.is_loading('a'))
        self.assertTrue(load_list.is_loaded('a'))
        self.assertIsNone(load_list.get_loading_extension('a'))
        self.assertEqual([], list(load_list.get_ready_to_load()))
        self.assertEqual([ext], list(load_list.get_loaded()))

    def test_state_changes__failure(self) -> None:
        """Run through the state change course."""
        load_list = order.LoadList()
        ext = mk_standalone_ext('a')

        self.assertTrue(
            load_list.add_one_pending(order.ExtensionDependencyOrder(ext, [], []))
        )
        load_list.mark_loading('a')
        res = load_list.mark_failed('a')
        self.assertIsNone(res.error)
        self.assertEqual([], list(res.result))
        self.assertFalse(load_list.is_pending('a'))
        self.assertFalse(load_list.is_loading('a'))
        self.assertFalse(load_list.is_loaded('a'))
        self.assertIsNone(load_list.get_loading_extension('a'))
        self.assertEqual([], list(load_list.get_ready_to_load()))
        self.assertEqual([], list(load_list.get_loaded()))
