"""Timer Entrypoint."""

from typing import Sequence, Dict, Any
from petronia_common.event_stream import BinaryReader, BinaryWriter
from petronia_common.util import StdRet, RET_OK_NONE


def extension_entrypoint(
        reader: BinaryReader,
        _writer: BinaryWriter,
        _config: Dict[str, Any],
        _args: Sequence[str],
) -> StdRet[None]:
    """Standardized entrypoint."""
    # Timer doesn't read any data right now; it only publishes data.
    reader.read()
    return RET_OK_NONE
