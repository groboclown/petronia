"""Logger Entrypoint."""

from typing import Sequence, Dict, Any
from petronia_common.event_stream import BinaryReader, BinaryWriter
from petronia_common.util import StdRet, join_errors, RET_OK_NONE
from petronia_ext_lib.runner.simple import SimpleEventRegistryContext
from . import shared_state
from .log_handler import register_log_listener


def extension_entrypoint(
        reader: BinaryReader,
        writer: BinaryWriter,
        config: Dict[str, Any],
        args: Sequence[str],
) -> StdRet[None]:
    """Standardized entrypoint.  arg[1] must be the data directory."""
    shared_state.clear_data()
    res1 = shared_state.load_configuration(args[1], config)
    context = SimpleEventRegistryContext(reader, writer, None)
    res2 = register_log_listener(context)

    if res1.has_error or res2.has_error:
        return StdRet.pass_error(join_errors(
            *res1.error_messages(), *res2.error_messages(),
        ))

    context.process_reader()
    return RET_OK_NONE
