"""Data Store Entrypoint."""

from typing import Sequence, Dict, Any
from petronia_common.event_stream import BinaryReader, BinaryWriter
from petronia_common.util import StdRet, join_none_results, join_errors
from petronia_ext_lib.runner.simple import SimpleEventRegistryContext
from . import shared_state
from .json_fetch_handler import register_json_fetch_data_listener
from .json_store_handler import register_json_store_data_listener
from .json_delete_handler import register_json_delete_data_listener
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
        register_json_store_data_listener(context),
        register_json_fetch_data_listener(context),
        register_json_delete_data_listener(context),
    )

    if res1.has_error or res2.has_error:
        return StdRet.pass_error(join_errors(
            *res1.error_messages(), *res2.error_messages(),
        ))

    return context.process_reader(datastore_state.EXTENSION_NAME)
