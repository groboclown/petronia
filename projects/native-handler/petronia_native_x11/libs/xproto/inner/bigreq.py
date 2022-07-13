# GENERATED FILE.  DO NOT EDIT

from typing import Dict, Mapping, Sequence, BinaryIO, NewType, Union, Callable, Optional, Any
import ctypes
from ..packet import (
    DataPacket,
    FixedDataPacketField, SimpleListDataPacketField,
    FixedPadDataPacketField, AlignedPadDataPacketField,
    StructureDataPacketField, ListDataPacketField,
    BitDataPacketField, UnionDataPacketField,
    MARKER_PAD, MARKER_INT8, MARKER_UINT8, MARKER_INT16,
    MARKER_UINT16, MARKER_INT32, MARKER_UINT32, MARKER_INT64,
    MARKER_UINT64, MARKER_FLOAT32, MARKER_FLOAT64, MARKER_FLEXIBLE,
) 

# ------------------------------------------------------------------
# Enums

# ------------------------------------------------------------------
# Aliases



# ------------------------------------------------------------------
# Structures, Events, Requests, Replies


EnableRequestCookie = NewType('EnableRequestCookie', ctypes.c_uint32)


EnableRequestPacket = DataPacket((
))


class EnableRequest:
    OPCODE = 0

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'EnableRequest':
        return EnableRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], EnableRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        EnableRequest.lib = library.bigreq_enable
        EnableRequest.lib.restype = EnableRequestCookie
        EnableRequest.lib.argstype = ()


class EnableRequestCType(ctypes.Structure):
    """bigreq Enable"""
    _fields_ = [
    ]


EnableReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('maximum_request_length', FixedDataPacketField(MARKER_UINT32)),
))


class EnableReplyReply:
    __slots__ = ('maximum_request_length',)

    def __init__(
            self, *,
            maximum_request_length: Optional[int] = None,
    ) -> None:
        self.maximum_request_length = maximum_request_length

    def as_dict(self) -> Dict[str, Any]:
        return {
            'maximum_request_length': self.maximum_request_length,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'EnableReplyReply':
        return EnableReplyReply(**EnableReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return EnableReplyReplyPacket.pack(**self.as_dict())


class EnableReplyReplyCType(ctypes.Structure):
    """bigreq Enable_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("maximum_request_length", ctypes.c_uint32),
    ]


# ------------------------------------------------------------------
# Unions

