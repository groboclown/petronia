"""
Basic definitions
"""
from typing import Sequence, Dict, Callable, Any
from petronia_common.event_stream import (
    BinaryReader, BinaryWriter,
)
from petronia_common.util import StdRet

TRANSLATION_CATALOG = 'extension-runner'


EntryPointFunctionType = Callable[
    [BinaryReader, BinaryWriter, Dict[str, Any], Sequence[str]],
    StdRet[None],
]
