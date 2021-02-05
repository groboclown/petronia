"""Test the module"""

import unittest
import unittest.mock
from petronia_common.extension.config import StandAloneExtensionMetadata
from petronia_common.extension.config.extension_schema import ExtensionRuntime
from petronia_common.extension.runner import EventRegistryContext
from petronia_common.util import StdRet, i18n, RET_OK_NONE
from .. import shared_state, setup
from ..defs import ExtensionInfo
from ..order import ExtensionDependencyOrder


class ExtLoaderSharedStateTest(unittest.TestCase):
    """Test the ExtLoaderSharedState class"""

    def setUp(self) -> None:
        self._orig = setup.for_unittest_backup()

    def tearDown(self) -> None:
        setup.for_unittest_restore(self._orig)

    def test_getters(self) -> None:
        """Test the getter methods."""
        state = shared_state.ExtLoaderSharedState()
        self.assertIsNotNone(state.load_list())

    def test_start_ready_extensions__empty(self) -> None:
        """Test the start_ready_extensions method with no extensions to load."""
        state = shared_state.ExtLoaderSharedState()
        context = unittest.mock.Mock(EventRegistryContext())
        res = state.start_ready_extensions(context)
        self.assertIsNone(res.error)
        context.send_event.assert_not_called()

    def test_start_ready_extensions__one(self) -> None:
        """Test the start_ready_extensions method with no extensions to load."""
        state = shared_state.ExtLoaderSharedState()
        state.load_list().add_one_pending(ExtensionDependencyOrder(
            ExtensionInfo([], StandAloneExtensionMetadata(
                'ex1', (1, 2, 3), '', '', [], [], [], ExtensionRuntime('x', {}),
            )),
            [], [],
        ))
        context = unittest.mock.Mock(EventRegistryContext())
        context.configure_mock(**{
            'send_event.return_value': RET_OK_NONE,
        })
        res = state.start_ready_extensions(context)
        self.assertIsNone(res.error)
        context.send_event.assert_called_once()

    def test_start_ready_extensions__send_errors(self) -> None:
        """Test the start_ready_extensions method with no extensions to load."""
        state = shared_state.ExtLoaderSharedState()
        state.load_list().add_one_pending(ExtensionDependencyOrder(
            ExtensionInfo([], StandAloneExtensionMetadata(
                'ex1', (1, 2, 3), '', '', [], [], [], ExtensionRuntime('x', {}),
            )),
            [], [],
        ))
        context = unittest.mock.Mock(EventRegistryContext())
        send_error: StdRet[None] = StdRet.pass_errmsg('x', i18n('y'))
        context.configure_mock(**{
            'send_event.return_value': send_error,
        })
        res = state.start_ready_extensions(context)
        context.send_event.assert_called_once()
        self.assertIsNotNone(res.error)
        self.assertEqual(
            ['y'],
            [m.debug() for m in res.error_messages()],
        )

    def test_on_extension_loaded__not_loading(self) -> None:
        """Test on_extension_loaded when the extension is not loading."""
        state = shared_state.ExtLoaderSharedState()
        context = unittest.mock.Mock(EventRegistryContext())
        res = state.on_extension_loaded('a', context)
        context.send_event.assert_not_called()
        self.assertIsNotNone(res.error)
        self.assertEqual(
            ['extension not in loading state: a'],
            [m.debug() for m in res.error_messages()],
        )

    def test_on_extension_loaded__no_sources(self) -> None:
        """Test on_extension_loaded when the extension is not loading."""
        state = shared_state.ExtLoaderSharedState()
        state.load_list().add_one_pending(ExtensionDependencyOrder(
            ExtensionInfo([], StandAloneExtensionMetadata(
                'ex1', (1, 2, 3), '', '', [], [], [], ExtensionRuntime('x', {}),
            )),
            [], [],
        ))
        state.load_list().mark_loading('ex1')

        context = unittest.mock.Mock(EventRegistryContext())
        res = state.on_extension_loaded('ex1', context)
        context.send_event.assert_not_called()
        self.assertIsNone(res.error)

    def test_on_extension_loaded__sources(self) -> None:
        """Test on_extension_loaded when the extension is not loading."""
        state = shared_state.ExtLoaderSharedState()
        ext_info = ExtensionInfo([], StandAloneExtensionMetadata(
            'ex1', (1, 2, 3), '', '', [], [], [], ExtensionRuntime('x', {}),
        ))
        ext_info.add_request_source_id('s1')
        ext_info.add_request_source_id('s2')
        state.load_list().add_one_pending(ExtensionDependencyOrder(ext_info, [], []))
        state.load_list().mark_loading('ex1')

        context = unittest.mock.Mock(EventRegistryContext())
        context.configure_mock(**{
            'send_event.return_value': RET_OK_NONE,
        })
        res = state.on_extension_loaded('ex1', context)
        context.send_event.assert_called()
        self.assertIsNone(res.error)

    def test_on_extension_loaded__boot_extension(self) -> None:
        """Test on_extension_loaded when the extension is not loading."""
        with_boot_extension = dict(self._orig)
        self._orig['b'] = ['ex1']
        setup.for_unittest_restore(with_boot_extension)
        state = shared_state.ExtLoaderSharedState()
        ext_info = ExtensionInfo([], StandAloneExtensionMetadata(
            'ex1', (1, 2, 3), '', '', [], [], [], ExtensionRuntime('x', {}),
        ))
        ext_info.add_request_source_id('s1')
        ext_info.add_request_source_id('s2')
        state.load_list().add_one_pending(ExtensionDependencyOrder(ext_info, [], []))
        state.load_list().mark_loading('ex1')

        context = unittest.mock.Mock(EventRegistryContext())
        context.configure_mock(**{
            'send_event.return_value': RET_OK_NONE,
        })
        res = state.on_extension_loaded('ex1', context)
        context.send_event.assert_called()
        self.assertIsNone(res.error)
