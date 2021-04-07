"""Setup the extension."""

from typing import Optional
from petronia_common.util import StdRet, join_none_results
from petronia_ext_lib.datastore import register_datastore_update_parsers
from petronia_ext_lib.runner import EventRegistryContext
from . import shared_state, native_window_handler, screen_state_handler
from .state import petronia_portal as portal_state


def setup_context(
        context: EventRegistryContext, config: Optional[portal_state.ConfigurationState],
) -> StdRet[None]:
    """Setup the initial context and state."""
    shared_state.clear_data(config)
    return join_none_results(
        register_datastore_update_parsers(context),

        native_window_handler.setup(context),
        screen_state_handler.setup(context),
    )
