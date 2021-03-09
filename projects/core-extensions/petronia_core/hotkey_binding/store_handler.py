"""Handles storage of the state in the datastore."""

from petronia_common.util import StdRet
from petronia_ext_lib import datastore
from petronia_ext_lib.runner import EventRegistryContext
from . import shared_state
from .events.impl import hotkey_binding as hotkey_events
from .state import hotkey_binding as hotkey_state


def send_bound_keys_state(
        context: EventRegistryContext,
) -> StdRet[None]:
    """Send the data store state structure of the bound keys."""
    return datastore.send_store_data(
        context,
        hotkey_events.BoundKeysState.UNIQUE_TARGET_FQN,
        shared_state.get_bound_keys_state(),
    )


def send_extension_events_state(
        context: EventRegistryContext,
) -> StdRet[None]:
    """Send the registered extension event information into the data store."""
    return datastore.send_store_data(
        context,
        hotkey_events.ExtensionEventsState.UNIQUE_TARGET_FQN,
        hotkey_events.ExtensionEventsState(list(shared_state.get_extension_events())),
    )


def send_configuration_state(
        context: EventRegistryContext,
) -> StdRet[None]:
    """Send the current configuration data into the data store."""
    return datastore.send_store_data(
        context,
        hotkey_state.ConfigurationState.UNIQUE_TARGET_FQN,
        shared_state.get_hotkey_state(),
    )
