"""Setup the extension."""

from typing import Optional
from petronia_common.util import StdRet, join_none_results
from petronia_ext_lib.runner import EventRegistryContext
from . import (
    shared_state, native_window_handler, screen_state_handler, portal_handler, hotkey_handler,
    data_store_reader,
)
from .state import petronia_portal as portal_state


def setup_context(
        context: EventRegistryContext, config: Optional[portal_state.ConfigurationState],
) -> StdRet[None]:
    """Setup the initial context and state."""
    shared_state.clear_data(config)
    return join_none_results(
        data_store_reader.setup(context),
        native_window_handler.setup(context),
        screen_state_handler.setup(context),
        portal_handler.setup(context),
        hotkey_handler.setup(context),
    )
