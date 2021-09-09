"""Data Store Entrypoint."""

from typing import Sequence, Dict, Any
from petronia_common.event_stream import BinaryReader, BinaryWriter
from petronia_common.util import StdRet, join_none_results, join_errors
from petronia_ext_lib.runner.simple import SimpleEventRegistryContext
from . import shared_state
from .post_handler import register_post_data_listener
from .store_handler import register_store_data_listener
from .delete_handler import register_delete_data_listener
from .state import datastore as datastore_state


def extension_entrypoint(
        reader: BinaryReader,
        writer: BinaryWriter,
        config: Dict[str, Any],
        _args: Sequence[str],
) -> StdRet[None]:
    """Standardized entrypoint."""
    shared_state.clear_data()
    res1 = shared_state.load_configuration(config)
    context = SimpleEventRegistryContext(reader, writer, None)
    res2 = join_none_results(
        register_store_data_listener(context),
        register_post_data_listener(context),
        register_delete_data_listener(context),
    )

    if res1.has_error or res2.has_error:
        return StdRet.pass_error(join_errors(
            *res1.error_messages(), *res2.error_messages(),
        ))

    try:
        return context.process_reader(datastore_state.EXTENSION_NAME)
    finally:
        # on shutdown, make sure the temporary files are cleaned up.
        shared_state.clear_data()
