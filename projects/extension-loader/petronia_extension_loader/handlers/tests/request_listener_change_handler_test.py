"""Test the module"""

import unittest
import unittest.mock
from petronia_common.util import RET_OK_NONE
from petronia_ext_lib.runner import EventRegistryContext
from .. import request_listener_change_handler
from ... import shared_state
from ...events.impl import extension_loader as extension_loader_event


class RequestListenerChangeHandlerTest(unittest.TestCase):
    """Tests for functions and classes in the module."""

    def test_register_ext_not_found(self) -> None:
        """Test extension listener registration when the extension name is not known."""
        context = unittest.mock.Mock(EventRegistryContext())
        context.send_event.return_value = RET_OK_NONE
        state = shared_state.ExtLoaderSharedState()
        handler = request_listener_change_handler.RegisterExtensionListenersHandler(state, context)
        self.assertFalse(handler.on_context_event(
            context, 's1:s2', 't1:t2', extension_loader_event.RegisterExtensionListenersEvent(
                [],
            ),
        ))
        # Nothing should be sent.
        context.send_event.assert_not_called()
