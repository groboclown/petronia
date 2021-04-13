"""Data Store Entrypoint."""

from typing import Sequence, Dict, Any
from petronia_common.event_stream import BinaryReader, BinaryWriter
from petronia_common.util import StdRet, join_none_results
from petronia_ext_lib.runner.simple import SimpleEventRegistryContext
from . import shared_state
from .post_handler import register_post_data_listener
from .store_handler import register_store_data_listener
from .delete_handler import register_delete_data_listener
from .state import datastore as datastore_state


def extension_entrypoint(
        reader: BinaryReader,
        writer: BinaryWriter,
        _config: Dict[str, Any],
        _args: Sequence[str],
) -> StdRet[None]:
    """Standardized entrypoint."""
    shared_state.clear_data()
    context = SimpleEventRegistryContext(reader, writer, None)
    res = join_none_results(
        register_store_data_listener(context),
        register_post_data_listener(context),
        register_delete_data_listener(context),
    )

    # This is very tricky to test.  This would only occur on future changes
    # to the code, which should trigger unit test failures.
    if res.has_error:  # pragma no cover
        return res  # pragma no cover

    return context.process_reader(datastore_state.EXTENSION_NAME)
