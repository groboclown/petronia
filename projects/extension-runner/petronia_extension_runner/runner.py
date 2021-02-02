"""
Handles running the extension.
"""

from typing import Sequence, Dict, Any
from petronia_common.event_stream import BinaryReader, BinaryWriter
from petronia_common.util import StdRet
from petronia_common.util import i18n as _
from . import setup
from .defs import EntryPointFunctionType


def run_extension(  # pylint:disable=too-many-arguments
        entrypoint: EntryPointFunctionType,
        arguments: Sequence[str],
        reader: BinaryReader,
        writer: BinaryWriter,
        config: Dict[str, Any],
) -> StdRet[None]:
    """Call the module's entrypoint function with the reader, writer, config, and arguments.
    This is done in another thread."""
    try:
        return entrypoint(reader, writer, config, arguments)
    except BaseException as err:  # pylint:disable=broad-except
        return StdRet.pass_exception(
            _('Extension {name} failed with an error'),
            err,
            name=setup.EXTENSION_NAME,
        )
