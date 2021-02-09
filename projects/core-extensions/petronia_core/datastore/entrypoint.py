"""Data Store Entrypoint."""

from typing import Sequence, Dict, Any
from petronia_common.event_stream import BinaryReader, BinaryWriter
from petronia_common.util import StdRet, join_errors, RET_OK_NONE
from petronia_ext_lib.runner.simple import SimpleEventRegistryContext
from . import shared_state
from .post_handler import register_post_data_listener
from .store_handler import register_store_data_listener
from .delete_handler import register_delete_data_listener


def extension_entrypoint(
        reader: BinaryReader,
        writer: BinaryWriter,
        _config: Dict[str, Any],
        _args: Sequence[str],
) -> StdRet[None]:
    """Standardized entrypoint."""
    shared_state.clear_data()
    context = SimpleEventRegistryContext(reader, writer, None)
    res1 = register_post_data_listener(context)
    res2 = register_delete_data_listener(context)
    res3 = register_store_data_listener(context)

    # This is very tricky to test.  This would only occur on future changes
    # to the code, which should trigger unit test failures.
    if res1.has_error or res2.has_error or res3.has_error:  # pragma no cover
        return StdRet.pass_error(join_errors(  # pragma no cover
            *res1.error_messages(), *res2.error_messages(), *res3.error_messages(),
        ))

    context.process_reader()
    return RET_OK_NONE
