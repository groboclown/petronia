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


GetVersionRequestCookie = NewType('GetVersionRequestCookie', ctypes.c_uint32)


GetVersionRequestPacket = DataPacket((
    ('client_major_version', FixedDataPacketField(MARKER_UINT16)),
    ('client_minor_version', FixedDataPacketField(MARKER_UINT16)),
))


class GetVersionRequest:
    OPCODE = 0

    __slots__ = ('client_major_version', 'client_minor_version',)

    def __init__(
            self, *,
            client_major_version: Optional[int] = None,
            client_minor_version: Optional[int] = None,
    ) -> None:
        self.client_major_version = client_major_version
        self.client_minor_version = client_minor_version

    def as_dict(self) -> Dict[str, Any]:
        return {
            'client_major_version': self.client_major_version,
            'client_minor_version': self.client_minor_version,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetVersionRequest':
        return GetVersionRequest(**GetVersionRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetVersionRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], GetVersionRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetVersionRequest.lib = library.xc_misc_getversion
        GetVersionRequest.lib.restype = GetVersionRequestCookie
        GetVersionRequest.lib.argstype = (ctypes.c_uint16, ctypes.c_uint16)


class GetVersionRequestCType(ctypes.Structure):
    """xc_misc GetVersion"""
    _fields_ = [
        ("client_major_version", ctypes.c_uint16),
        ("client_minor_version", ctypes.c_uint16),
    ]


GetVersionReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('server_major_version', FixedDataPacketField(MARKER_UINT16)),
    ('server_minor_version', FixedDataPacketField(MARKER_UINT16)),
))


class GetVersionReplyReply:
    __slots__ = ('server_major_version', 'server_minor_version',)

    def __init__(
            self, *,
            server_major_version: Optional[int] = None,
            server_minor_version: Optional[int] = None,
    ) -> None:
        self.server_major_version = server_major_version
        self.server_minor_version = server_minor_version

    def as_dict(self) -> Dict[str, Any]:
        return {
            'server_major_version': self.server_major_version,
            'server_minor_version': self.server_minor_version,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetVersionReplyReply':
        return GetVersionReplyReply(**GetVersionReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetVersionReplyReplyPacket.pack(**self.as_dict())


class GetVersionReplyReplyCType(ctypes.Structure):
    """xc_misc GetVersion_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("server_major_version", ctypes.c_uint16),
        ("server_minor_version", ctypes.c_uint16),
    ]


GetXidrangeRequestCookie = NewType('GetXidrangeRequestCookie', ctypes.c_uint32)


GetXidrangeRequestPacket = DataPacket((
))


class GetXidrangeRequest:
    OPCODE = 1

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetXidrangeRequest':
        return GetXidrangeRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], GetXidrangeRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetXidrangeRequest.lib = library.xc_misc_getxidrange
        GetXidrangeRequest.lib.restype = GetXidrangeRequestCookie
        GetXidrangeRequest.lib.argstype = ()


class GetXidrangeRequestCType(ctypes.Structure):
    """xc_misc GetXIDRange"""
    _fields_ = [
    ]


GetXidrangeReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('start_id', FixedDataPacketField(MARKER_UINT32)),
    ('count', FixedDataPacketField(MARKER_UINT32)),
))


class GetXidrangeReplyReply:
    __slots__ = ('start_id', 'count',)

    def __init__(
            self, *,
            start_id: Optional[int] = None,
            count: Optional[int] = None,
    ) -> None:
        self.start_id = start_id
        self.count = count

    def as_dict(self) -> Dict[str, Any]:
        return {
            'start_id': self.start_id,
            'count': self.count,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetXidrangeReplyReply':
        return GetXidrangeReplyReply(**GetXidrangeReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetXidrangeReplyReplyPacket.pack(**self.as_dict())


class GetXidrangeReplyReplyCType(ctypes.Structure):
    """xc_misc GetXIDRange_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("start_id", ctypes.c_uint32),
        ("count", ctypes.c_uint32),
    ]


GetXidlistRequestCookie = NewType('GetXidlistRequestCookie', ctypes.c_uint32)


GetXidlistRequestPacket = DataPacket((
    ('count', FixedDataPacketField(MARKER_UINT32)),
))


class GetXidlistRequest:
    OPCODE = 2

    __slots__ = ('count',)

    def __init__(
            self, *,
            count: Optional[int] = None,
    ) -> None:
        self.count = count

    def as_dict(self) -> Dict[str, Any]:
        return {
            'count': self.count,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetXidlistRequest':
        return GetXidlistRequest(**GetXidlistRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetXidlistRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetXidlistRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetXidlistRequest.lib = library.xc_misc_getxidlist
        GetXidlistRequest.lib.restype = GetXidlistRequestCookie
        GetXidlistRequest.lib.argstype = (ctypes.c_uint32,)


class GetXidlistRequestCType(ctypes.Structure):
    """xc_misc GetXIDList"""
    _fields_ = [
        ("count", ctypes.c_uint32),
    ]


GetXidlistReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('ids_len', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('ids', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['ids_len'], 0)),
))


class GetXidlistReplyReply:
    __slots__ = ('ids_len', 'ids',)

    def __init__(
            self, *,
            ids_len: Optional[int] = None,
            ids: Optional[Sequence[int]] = None,
    ) -> None:
        self.ids_len = ids_len
        self.ids = ids

    def as_dict(self) -> Dict[str, Any]:
        return {
            'ids_len': self.ids_len,
            'ids': self.ids,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetXidlistReplyReply':
        return GetXidlistReplyReply(**GetXidlistReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetXidlistReplyReplyPacket.pack(**self.as_dict())


class GetXidlistReplyReplyCType(ctypes.Structure):
    """xc_misc GetXIDList_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("ids_len", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


# ------------------------------------------------------------------
# Unions

