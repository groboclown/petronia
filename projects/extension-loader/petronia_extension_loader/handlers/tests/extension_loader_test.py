"""Test the module."""

import unittest
import unittest.mock
import tempfile
import shutil

from petronia_common.extension.config import StandAloneExtensionMetadata
from petronia_common.extension.config.extension_schema import ExtensionRuntime
from petronia_common.extension.runner import EventRegistryContext
from petronia_common.util import RET_OK_NONE
from .. import extension_loader
from ... import setup
from ...defs import ExtensionInfo
from ...order import ExtensionDependencyOrder
from ...shared_state import ExtLoaderSharedState


class ExtensionLoaderFunctionTest(unittest.TestCase):
    """Test the functions in the module."""

    def setUp(self) -> None:
        self._orig = setup.for_unittest_backup()
        self.tempdir = tempfile.mkdtemp()
        setup.for_unittest_restore({
            **self._orig,
            'b': [self.tempdir],
        })

    def tearDown(self) -> None:
        shutil.rmtree(self.tempdir, ignore_errors=True)
        setup.for_unittest_restore(self._orig)

    def test_initiate_load_extension__not_loadable(self) -> None:
        """Test initiate_load_extension when the extension is not loadable."""
        state = ExtLoaderSharedState()
        context = unittest.mock.Mock(EventRegistryContext())
        res = extension_loader.initiate_load_extension(
            state, context, None, 'ex1', None, None, None,
        )
        self.assertIsNotNone(res.error)
        context.send_event.assert_not_called()
        self.assertEqual(
            ['no extension installed matches ex1 [>=None, <None]'],
            [m.debug() for m in res.error_messages()],
        )

    def test_initiate_load_extension__find_extensions_not_found(self) -> None:
        """Test initiate_load_extension when the extension list must be loaded, but
        the requested extension is not loadable."""
        state = ExtLoaderSharedState()
        ext_info = ExtensionInfo([], StandAloneExtensionMetadata(
            'ex1', (1, 2, 3), '', '', [], [], [], ExtensionRuntime('x', {}),
        ))
        context = unittest.mock.Mock(EventRegistryContext())
        context.configure_mock(**{
            'send_event.return_value': RET_OK_NONE,
        })
        self.assertTrue(
            state.load_list().add_one_pending(ExtensionDependencyOrder(ext_info, [], []))
        )
        state.load_list().mark_loading(ext_info.name)
        res = extension_loader.initiate_load_extension(
            state, context, None, 'ex1', None, None, None,
        )
        self.assertIsNotNone(res.error)
        context.send_event.assert_not_called()
        self.assertEqual(
            ['no extension installed matches ex1 [>=None, <None]'],
            [m.debug() for m in res.error_messages()],
        )

    def test_initiate_load_extension__find_extensions_min_max(self) -> None:
        """Test initiate_load_extension when the extension list must be loaded, but
        the requested extension is not loadable."""
        state = ExtLoaderSharedState()
        context = unittest.mock.Mock(EventRegistryContext())
        context.configure_mock(**{
            'send_event.return_value': RET_OK_NONE,
        })
        res = extension_loader.initiate_load_extension(
            state, context, None, 'ex1', [1, 0, 0], [2, 0, 0], None,
        )
        self.assertIsNotNone(res.error)
        context.send_event.assert_not_called()
        self.assertEqual(
            ['no extension installed matches ex1 [>=[1, 0, 0], <[2, 0, 0]]'],
            [m.debug() for m in res.error_messages()],
        )

    def test_initiate_load_extension__already_loaded(self) -> None:
        """Test initiate_load_extension when the extension list must be loaded, but
        the requested extension is not loadable."""
        state = ExtLoaderSharedState()
        ext_info = ExtensionInfo([], StandAloneExtensionMetadata(
            'ex1', (1, 2, 3), '', '', [], [], [], ExtensionRuntime('x', {}),
        ))
        self.assertTrue(
            state.load_list().add_one_pending(ExtensionDependencyOrder(ext_info, [], []))
        )
        state.load_list().mark_loading(ext_info.name)
        state.load_list().mark_loaded(ext_info.name)
        context = unittest.mock.Mock(EventRegistryContext())
        res = extension_loader.initiate_load_extension(
            state, context, None, 'ex1', [1, 0, 0], [2, 0, 0], None,
        )
        self.assertIsNone(res.error)
        context.send_event.assert_not_called()
        self.assertEqual((1, 2, 3), res.result)

    def test_initiate_load_extension__found(self) -> None:
        """Test initiate_load_extension where the extension is found, and there's another
        extension pending to run."""
        state = ExtLoaderSharedState()
        ext1_info = ExtensionInfo([], StandAloneExtensionMetadata(
            'ex1', (1, 2, 3), '', '', [], [], [], ExtensionRuntime('x', {}),
        ))
        state.load_list().add_one_pending(ExtensionDependencyOrder(ext1_info, [], []))
        state.load_list().mark_loading(ext1_info.name)
        ext2_info = ExtensionInfo([], StandAloneExtensionMetadata(
            'ex2', (3, 2, 1), '', '', [], [], [], ExtensionRuntime('x', {}),
        ))
        state.load_list().add_one_pending(ExtensionDependencyOrder(ext2_info, [], []))
        context = unittest.mock.Mock(EventRegistryContext())
        context.configure_mock(**{
            'send_event.return_value': RET_OK_NONE,
        })
        res = extension_loader.initiate_load_extension(
            state, context, 's1', 'ex1', None, None, [ext1_info],
        )
        self.assertIsNone(res.error)
        context.send_event.assert_called_once()
