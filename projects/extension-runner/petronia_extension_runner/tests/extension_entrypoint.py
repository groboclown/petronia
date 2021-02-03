"""A test file for entrypoints."""

from typing import Sequence, List, Dict, Any
from petronia_common.event_stream import BinaryReader, BinaryWriter
from petronia_common.util import StdRet, RET_OK_NONE


CALLED_CONFIGS: List[Dict[str, Any]] = []
CALLED_ARGS: List[Sequence[str]] = []
RETURN: List[StdRet[None]] = [RET_OK_NONE]


def init(ret: StdRet[None] = RET_OK_NONE) -> None:
    """initialize this module for testing."""
    CALLED_CONFIGS.clear()
    CALLED_ARGS.clear()
    RETURN[0] = ret


def extension_entrypoint(
        reader: BinaryReader,
        _writer: BinaryWriter,
        config: Dict[str, Any],
        args: Sequence[str],
) -> StdRet[None]:
    """Standardized Python entrypoint for an extension."""
    CALLED_CONFIGS.append(config)
    CALLED_ARGS.append(args)

    # Finish ourself off.
    reader.read()
    return RETURN[0]
