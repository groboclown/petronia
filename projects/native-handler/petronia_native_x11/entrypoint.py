"""X11 Entrypoint."""

from typing import Sequence, Dict, Any
from petronia_common.event_stream import BinaryReader, BinaryWriter
from petronia_common.util import StdRet, join_errors, RET_OK_NONE
from petronia_ext_lib.runner.lookup import LookupEventRegistryContext
from petronia_ext_lib import logging
from .datastore.petronia_native_x11 import (
    ConfigurationState, VirtualScreens, EXTENSION_NAME,
)
from . import setup
from .datastore import petronia_native_x11 as native_windows_state


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
        print(f"Windows Native configuration problem; config = {config}")
        logging.send_user_error(
            context, EXTENSION_NAME + ':configuration', config_res.valid_error,
            'invalid-configuration',
        )

    res = loop_res.result.start()
    if res.has_error:
        print('X11 Native startup problem.')
        return res

    try:
        context.process_reader(native_windows_state.EXTENSION_NAME)
    finally:
        loop_res.result.dispose(-1)
    return RET_OK_NONE


def parse_config(config: Dict[str, Any]) -> StdRet[ConfigurationState]:
    """Parse the configuration dictionary."""
    if not config:
        print("X11 Native configuration is empty.")
        return StdRet.pass_ok(ConfigurationState(VirtualScreens([])))
    return ConfigurationState.parse_data(config)
