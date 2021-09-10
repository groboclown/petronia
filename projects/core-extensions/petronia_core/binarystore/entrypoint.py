"""Data Store Entrypoint."""

from typing import Sequence, Dict, Any
from petronia_common.event_stream import BinaryReader, BinaryWriter
from petronia_common.util import StdRet, join_none_results, join_errors
from petronia_ext_lib.runner import SingleThreadedEventRegistryContext
from . import shared_state
from .bin_delete_handler import register_bin_delete_data_listener
from .bin_fetch_handler import register_bin_fetch_data_listener
from .bin_store_handler import register_bin_store_data_listener
from .state import binarystore as binarystore_state


def extension_entrypoint(
        reader: BinaryReader,
        writer: BinaryWriter,
        config: Dict[str, Any],
        _args: Sequence[str],
) -> StdRet[None]:
    """Standardized entrypoint."""
    shared_state.clear_data()
    res1 = shared_state.load_configuration(config)
    context = SingleThreadedEventRegistryContext(reader, writer, None)
    res2 = join_none_results(
        register_bin_delete_data_listener(context),
        register_bin_fetch_data_listener(context),
        register_bin_store_data_listener(context),
    )

    if res1.has_error or res2.has_error:
        return StdRet.pass_error(join_errors(
            *res1.error_messages(), *res2.error_messages(),
        ))

    try:
        return context.process_reader(binarystore_state.EXTENSION_NAME)
    finally:
        # on shutdown, make sure the temporary files are cleaned up.
        shared_state.clear_data()
