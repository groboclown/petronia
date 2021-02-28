"""Data Store Entrypoint."""

from typing import Sequence, Dict, Any
from petronia_common.event_stream import BinaryReader, BinaryWriter
from petronia_common.util import StdRet, join_errors, RET_OK_NONE
from petronia_ext_lib.runner.lookup import LookupEventRegistryContext
from petronia_ext_lib import logging
from .datastore.petronia_native_windows import ConfigurationState, EXTENSION_NAME
from . import setup


def extension_entrypoint(
        reader: BinaryReader,
        writer: BinaryWriter,
        config: Dict[str, Any],
        _args: Sequence[str],
) -> StdRet[None]:
    """Standardized entrypoint."""
    context = LookupEventRegistryContext(reader, writer, None, None)
    config_res = ConfigurationState.parse_data(config)
    loop_res = setup.setup_context(context, config_res.value)

    # Bad configuration isn't a failure state.

    if loop_res.has_error:
        # ... but report the bad configuration if setup fails.
        return StdRet.pass_error(join_errors(
            *config_res.error_messages(), *loop_res.error_messages(),
        ))
    if config_res.has_error:
        logging.send_user_error(
            context, EXTENSION_NAME + ':configuration', config_res.valid_error,
            'invalid-configuration',
        )

    loop_res.result.start()
    try:
        context.process_reader()
    finally:
        loop_res.result.dispose(-1)
    return RET_OK_NONE
