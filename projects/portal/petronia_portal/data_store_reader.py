"""Handles data that comes in from data store announcements."""
from petronia_common.util import StdRet
from petronia_ext_lib import datastore
from petronia_ext_lib.runner import EventRegistryContext
from . import user_messages
from .state import petronia_portal as portal_state


_CACHE_STORE = [datastore.CacheStore(
    portal_state.EXTENSION_NAME, user_messages.report_send_receive_problems,
)]


def get_cache_store() -> datastore.CacheStore:
    """Get the data cache store."""
    return _CACHE_STORE[0]


def setup(context: EventRegistryContext) -> StdRet[None]:
    """Setup the data store handler."""
    return get_cache_store().register(context)
