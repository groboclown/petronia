"""A test file for entrypoints."""

from typing import Sequence, List, Dict, Any
from petronia_common.event_stream import BinaryReader, BinaryWriter
from petronia_common.util import StdRet


CALLED_CONFIGS: List[Dict[str, Any]] = []
CALLED_ARGS: List[Sequence[str]] = []
STANDARD_ERROR = OSError('error')
RETURN: List[Exception] = [STANDARD_ERROR]


def init(raises: Exception = STANDARD_ERROR) -> None:
    """initialize this module for testing."""
    CALLED_CONFIGS.clear()
    CALLED_ARGS.clear()
    RETURN[0] = raises


def extension_entrypoint(
        _reader: BinaryReader,
        _writer: BinaryWriter,
        config: Dict[str, Any],
        args: Sequence[str],
) -> StdRet[None]:
    """Standardized Python entrypoint for an extension."""
    CALLED_CONFIGS.append(config)
    CALLED_ARGS.append(args)

    raise RETURN[0]
