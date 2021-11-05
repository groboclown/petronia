"""Test the key handler"""

from typing import List, Sequence, Dict, Callable, TypeVar, Any
import unittest
from concurrent.futures import ThreadPoolExecutor, Future
from petronia_common.event_stream.tests.shared import SimpleBinaryWriter, create_read_stream
from petronia_ext_lib.runner import SimpleEventRegistryContext
from .. import key_handler
from ..keymap import STR_VK_MAP
from ..configuration import ConfigurationStore


class WindowsKeyHandlerTest(unittest.TestCase):
    """Test the windows key handler.  This needs to ensure that key combinations
    are correctly managed with state."""

    def test_single_key(self) -> None:
        """A single key on a meta key is registered, and pressing the single key fires a
        message."""
        writer = SimpleBinaryWriter()
        context = SimpleEventRegistryContext(
            create_read_stream(b''), writer, None,
        )
        store = ConfigurationStore(None)
        submitted = TestableEventSubmit()
        handler = key_handler.WindowsKeyHandler(context, store, submitted)
        handler.set_hotkey_bindings('meta', ['lsuper'], [['q']])

        # Try the bare key by itself.  It shouldn't be handled.
        cancel_prop, injected = handler.key_handler(STR_VK_MAP['q'], -1, False, False)
        self.assertFalse(cancel_prop)
        self.assertEqual((), injected)
        self.assertTrue(submitted.has_no_submits())

        cancel_prop, injected = handler.key_handler(STR_VK_MAP['lsuper'], -1, False, False)
        self.assertTrue(cancel_prop)
        self.assertEqual((), injected)
        self.assertTrue(submitted.has_no_submits())

        cancel_prop, injected = handler.key_handler(STR_VK_MAP['q'], -1, False, False)
        self.assertTrue(cancel_prop)
        self.assertEqual((), injected)
        # Should have submitted the event.
        self.assertEqual([handler.send_hotkey], submitted.submitted_funcs)
        self.assertEqual([{}], submitted.submitted_kwargs)
        self.assertEqual([(
            ('+q',),
        )], submitted.submitted_args)

        # Another call to the key should not generate an event.
        submitted.clear_submits()
        cancel_prop, injected = handler.key_handler(STR_VK_MAP['q'], -1, False, False)
        self.assertFalse(cancel_prop)
        self.assertEqual((), injected)
        self.assertTrue(submitted.has_no_submits())

    def test_double_linked_key(self) -> None:
        """Two keys with a shared meta prefix beyond the base meta key."""
        writer = SimpleBinaryWriter()
        context = SimpleEventRegistryContext(
            create_read_stream(b''), writer, None,
        )
        store = ConfigurationStore(None)
        submitted = TestableEventSubmit()
        handler = key_handler.WindowsKeyHandler(context, store, submitted)
        handler.set_hotkey_bindings('meta', ['lsuper'], [['lshift', 'q'], ['lshift', 't']])

        # First key path
        cancel_prop, injected = handler.key_handler(STR_VK_MAP['lsuper'], -1, False, False)
        self.assertTrue(cancel_prop)
        self.assertEqual((), injected)
        self.assertTrue(submitted.has_no_submits())

        cancel_prop, injected = handler.key_handler(STR_VK_MAP['lshift'], -1, False, False)
        self.assertTrue(cancel_prop)
        self.assertEqual((), injected)
        self.assertTrue(submitted.has_no_submits())

        cancel_prop, injected = handler.key_handler(STR_VK_MAP['q'], -1, False, False)
        self.assertTrue(cancel_prop)
        self.assertEqual((), injected)
        # Should have submitted the event.
        self.assertEqual([handler.send_hotkey], submitted.submitted_funcs)
        self.assertEqual([{}], submitted.submitted_kwargs)
        self.assertEqual([(
            ('+lshift+q',),
        )], submitted.submitted_args)

        # Second key path
        submitted.clear_submits()
        cancel_prop, injected = handler.key_handler(STR_VK_MAP['lsuper'], -1, False, False)
        self.assertTrue(cancel_prop)
        self.assertEqual((), injected)
        self.assertTrue(submitted.has_no_submits())

        cancel_prop, injected = handler.key_handler(STR_VK_MAP['lshift'], -1, False, False)
        self.assertTrue(cancel_prop)
        self.assertEqual((), injected)
        self.assertTrue(submitted.has_no_submits())

        cancel_prop, injected = handler.key_handler(STR_VK_MAP['t'], -1, False, False)
        self.assertTrue(cancel_prop)
        self.assertEqual((), injected)
        # Should have submitted the event.
        self.assertEqual([handler.send_hotkey], submitted.submitted_funcs)
        self.assertEqual([{}], submitted.submitted_kwargs)
        self.assertEqual([(
            ('+lshift+t',),
        )], submitted.submitted_args)


_T = TypeVar("_T")


class ImmediateEventSubmit(ThreadPoolExecutor):
    """Runs the stuff right now."""

    def submit(self, fn: Callable[..., _T], *args: Any, **kwargs: Any) -> Future[_T]:
        fn(*args, **kwargs)
        return Future()


class TestableEventSubmit(ThreadPoolExecutor):
    """Captures submitted requests."""
    __slots__ = ('submitted_args', 'submitted_funcs', 'submitted_kwargs',)

    def __init__(self) -> None:
        ThreadPoolExecutor.__init__(self)
        self.submitted_funcs: List[Callable[..., _T]] = []
        self.submitted_args: List[Sequence[Any]] = []
        self.submitted_kwargs: List[Dict[str, Any]] = []

    def submit(self, fn: Callable[..., _T], *args: Any, **kwargs: Any) -> Future[_T]:
        self.submitted_funcs.append(fn)
        self.submitted_args.append(args)
        self.submitted_kwargs.append(kwargs)
        return Future()

    def has_no_submits(self) -> bool:
        """Has any call to submit been made?"""
        return len(self.submitted_args) <= 0

    def clear_submits(self) -> None:
        """Clear the recorded submit calls."""
        self.submitted_funcs.clear()
        self.submitted_args.clear()
        self.submitted_kwargs.clear()
