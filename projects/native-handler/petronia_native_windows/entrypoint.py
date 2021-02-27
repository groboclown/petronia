"""Data Store Entrypoint."""

from typing import Sequence, Dict, Any
from petronia_common.event_stream import BinaryReader, BinaryWriter
from petronia_common.util import StdRet, join_errors, RET_OK_NONE
from petronia_ext_lib.runner.lookup import LookupEventRegistryContext
from petronia_ext_lib import logging
from petronia_native.common.events.impl import screen
from . import setup


EXTENSION_NAME = 'petronia_native_windows'


def extension_entrypoint(
        reader: BinaryReader,
        writer: BinaryWriter,
        config: Dict[str, Any],
        _args: Sequence[str],
) -> StdRet[None]:
    """Standardized entrypoint."""
    context = LookupEventRegistryContext(reader, writer, None, None)
    res1 = screen.ConfigurationState.parse_data(config)
    res2 = setup.setup_context(context)

    # Bad configuration isn't a failure state.

    if res2.has_error:
        # ... but report the bad configuration if setup fails.
        return StdRet.pass_error(join_errors(
            *res1.error_messages(), *res2.error_messages(),
        ))
    if res1.has_error:
        logging.send_user_error(
            context, EXTENSION_NAME + ':configuration', res1.valid_error,
            'invalid-configuration',
        )

    context.process_reader()
    return RET_OK_NONE
