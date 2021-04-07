"""Data Store Entrypoint."""

from typing import Sequence, Dict, Any
from petronia_common.event_stream import BinaryReader, BinaryWriter
from petronia_common.util import StdRet, RET_OK_NONE, join_errors
from petronia_ext_lib.runner import LookupEventRegistryContext
from petronia_ext_lib import logging
from . import setup
from .state import petronia_portal as portal_state


def extension_entrypoint(
        reader: BinaryReader,
        writer: BinaryWriter,
        config: Dict[str, Any],
        _args: Sequence[str],
) -> StdRet[None]:
    """Standardized entrypoint."""
    context = LookupEventRegistryContext(reader, writer, None, None)
    config_res = parse_config(config)
    loop_res = setup.setup_context(context, config_res.value)

    # Bad configuration isn't a failure state.

    if loop_res.has_error:
        # ... but report the bad configuration if setup fails.
        return StdRet.pass_error(join_errors(
            *config_res.error_messages(), *loop_res.error_messages(),
        ))
    if config_res.has_error:
        print(f"Portal configuration problem; config = {config}")
        logging.send_user_error(
            context, portal_state.EXTENSION_NAME + ':configuration', config_res.valid_error,
            'invalid-configuration',
        )
    print("[PORTAL] running **")
    context.process_reader()
    return RET_OK_NONE


def parse_config(config: Dict[str, Any]) -> StdRet[portal_state.ConfigurationState]:
    """Parse the configuration dictionary."""
    if not config:
        print("Portal configuration is empty.")
        return StdRet.pass_ok(portal_state.ConfigurationState(
            [], [],
        ))
    return portal_state.ConfigurationState.parse_data(config)
