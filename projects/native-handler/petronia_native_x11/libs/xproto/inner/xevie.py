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

DatatypeType = NewType('DatatypeType', int)


class DatatypeValues:
    UNMODIFIED = DatatypeType(0)
    MODIFIED = DatatypeType(1)


# ------------------------------------------------------------------
# Aliases



# ------------------------------------------------------------------
# Structures, Events, Requests, Replies


QueryVersionRequestCookie = NewType('QueryVersionRequestCookie', ctypes.c_uint32)


QueryVersionRequestPacket = DataPacket((
    ('client_major_version', FixedDataPacketField(MARKER_UINT16)),
    ('client_minor_version', FixedDataPacketField(MARKER_UINT16)),
))


class QueryVersionRequest:
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
    def from_data(inp: BinaryIO) -> 'QueryVersionRequest':
        return QueryVersionRequest(**QueryVersionRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryVersionRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], QueryVersionRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryVersionRequest.lib = library.xevie_queryversion
        QueryVersionRequest.lib.restype = QueryVersionRequestCookie
        QueryVersionRequest.lib.argstype = (ctypes.c_uint16, ctypes.c_uint16)


class QueryVersionRequestCType(ctypes.Structure):
    """xevie QueryVersion"""
    _fields_ = [
        ("client_major_version", ctypes.c_uint16),
        ("client_minor_version", ctypes.c_uint16),
    ]


QueryVersionReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('server_major_version', FixedDataPacketField(MARKER_UINT16)),
    ('server_minor_version', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(20)),
))


class QueryVersionReplyReply:
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
    def from_data(inp: BinaryIO) -> 'QueryVersionReplyReply':
        return QueryVersionReplyReply(**QueryVersionReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryVersionReplyReplyPacket.pack(**self.as_dict())


class QueryVersionReplyReplyCType(ctypes.Structure):
    """xevie QueryVersion_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("server_major_version", ctypes.c_uint16),
        ("server_minor_version", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 20),
    ]


StartRequestCookie = NewType('StartRequestCookie', ctypes.c_uint32)


StartRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT32)),
))


class StartRequest:
    OPCODE = 1

    __slots__ = ('screen',)

    def __init__(
            self, *,
            screen: Optional[int] = None,
    ) -> None:
        self.screen = screen

    def as_dict(self) -> Dict[str, Any]:
        return {
            'screen': self.screen,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'StartRequest':
        return StartRequest(**StartRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return StartRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], StartRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        StartRequest.lib = library.xevie_start
        StartRequest.lib.restype = StartRequestCookie
        StartRequest.lib.argstype = (ctypes.c_uint32,)


class StartRequestCType(ctypes.Structure):
    """xevie Start"""
    _fields_ = [
        ("screen", ctypes.c_uint32),
    ]


StartReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(24)),
))


class StartReplyReply:
    __slots__ = (,)

    def __init__(
            self, *,
    ) -> None:

    def as_dict(self) -> Dict[str, Any]:
        return {
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'StartReplyReply':
        return StartReplyReply(**StartReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return StartReplyReplyPacket.pack(**self.as_dict())


class StartReplyReplyCType(ctypes.Structure):
    """xevie Start_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 24),
    ]


EndRequestCookie = NewType('EndRequestCookie', ctypes.c_uint32)


EndRequestPacket = DataPacket((
    ('cmap', FixedDataPacketField(MARKER_UINT32)),
))


class EndRequest:
    OPCODE = 2

    __slots__ = ('cmap',)

    def __init__(
            self, *,
            cmap: Optional[int] = None,
    ) -> None:
        self.cmap = cmap

    def as_dict(self) -> Dict[str, Any]:
        return {
            'cmap': self.cmap,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'EndRequest':
        return EndRequest(**EndRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return EndRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], EndRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        EndRequest.lib = library.xevie_end
        EndRequest.lib.restype = EndRequestCookie
        EndRequest.lib.argstype = (ctypes.c_uint32,)


class EndRequestCType(ctypes.Structure):
    """xevie End"""
    _fields_ = [
        ("cmap", ctypes.c_uint32),
    ]


EndReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(24)),
))


class EndReplyReply:
    __slots__ = (,)

    def __init__(
            self, *,
    ) -> None:

    def as_dict(self) -> Dict[str, Any]:
        return {
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'EndReplyReply':
        return EndReplyReply(**EndReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return EndReplyReplyPacket.pack(**self.as_dict())


class EndReplyReplyCType(ctypes.Structure):
    """xevie End_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 24),
    ]


EventStructPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(32)),
))


class EventStruct:
    __slots__ = (,)

    def __init__(
            self, *,
    ) -> None:

    def as_dict(self) -> Dict[str, Any]:
        return {
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'EventStruct':
        return EventStruct(**EventStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return EventStructPacket.pack(**self.as_dict())


class EventStructCType(ctypes.Structure):
    """xevie Event"""
    _fields_ = [
        ("pad0", ctypes.c_uint8 * 32),
    ]


SendRequestCookie = NewType('SendRequestCookie', ctypes.c_uint32)


SendRequestPacket = DataPacket((
    ('event', FixedDataPacketField(MARKER_UINT32)),
    ('data_type', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(64)),
))


class SendRequest:
    OPCODE = 3

    __slots__ = ('event', 'data_type',)

    def __init__(
            self, *,
            event: Optional[int] = None,
            data_type: Optional[int] = None,
    ) -> None:
        self.event = event
        self.data_type = data_type

    def as_dict(self) -> Dict[str, Any]:
        return {
            'event': self.event,
            'data_type': self.data_type,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SendRequest':
        return SendRequest(**SendRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SendRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], SendRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SendRequest.lib = library.xevie_send
        SendRequest.lib.restype = SendRequestCookie
        SendRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8 * 64)


class SendRequestCType(ctypes.Structure):
    """xevie Send"""
    _fields_ = [
        ("event", ctypes.c_uint32),
        ("data_type", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 64),
    ]


SendReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(24)),
))


class SendReplyReply:
    __slots__ = (,)

    def __init__(
            self, *,
    ) -> None:

    def as_dict(self) -> Dict[str, Any]:
        return {
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SendReplyReply':
        return SendReplyReply(**SendReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SendReplyReplyPacket.pack(**self.as_dict())


class SendReplyReplyCType(ctypes.Structure):
    """xevie Send_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 24),
    ]


SelectInputRequestCookie = NewType('SelectInputRequestCookie', ctypes.c_uint32)


SelectInputRequestPacket = DataPacket((
    ('event_mask', FixedDataPacketField(MARKER_UINT32)),
))


class SelectInputRequest:
    OPCODE = 4

    __slots__ = ('event_mask',)

    def __init__(
            self, *,
            event_mask: Optional[int] = None,
    ) -> None:
        self.event_mask = event_mask

    def as_dict(self) -> Dict[str, Any]:
        return {
            'event_mask': self.event_mask,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SelectInputRequest':
        return SelectInputRequest(**SelectInputRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SelectInputRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], SelectInputRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SelectInputRequest.lib = library.xevie_selectinput
        SelectInputRequest.lib.restype = SelectInputRequestCookie
        SelectInputRequest.lib.argstype = (ctypes.c_uint32,)


class SelectInputRequestCType(ctypes.Structure):
    """xevie SelectInput"""
    _fields_ = [
        ("event_mask", ctypes.c_uint32),
    ]


SelectInputReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(24)),
))


class SelectInputReplyReply:
    __slots__ = (,)

    def __init__(
            self, *,
    ) -> None:

    def as_dict(self) -> Dict[str, Any]:
        return {
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SelectInputReplyReply':
        return SelectInputReplyReply(**SelectInputReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SelectInputReplyReplyPacket.pack(**self.as_dict())


class SelectInputReplyReplyCType(ctypes.Structure):
    """xevie SelectInput_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 24),
    ]


# ------------------------------------------------------------------
# Unions

