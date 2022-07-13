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

ReportLevelType = NewType('ReportLevelType', int)


class ReportLevelValues:
    RAW_RECTANGLES = ReportLevelType(0)
    DELTA_RECTANGLES = ReportLevelType(1)
    BOUNDING_BOX = ReportLevelType(2)
    NON_EMPTY = ReportLevelType(3)


# ------------------------------------------------------------------
# Aliases

Damage = NewType('Damage', ctypes.c_uint32)


# ------------------------------------------------------------------
# Structures, Events, Requests, Replies


QueryVersionRequestCookie = NewType('QueryVersionRequestCookie', ctypes.c_uint32)


QueryVersionRequestPacket = DataPacket((
    ('client_major_version', FixedDataPacketField(MARKER_UINT32)),
    ('client_minor_version', FixedDataPacketField(MARKER_UINT32)),
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
        QueryVersionRequest.lib = library.damage_queryversion
        QueryVersionRequest.lib.restype = QueryVersionRequestCookie
        QueryVersionRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class QueryVersionRequestCType(ctypes.Structure):
    """damage QueryVersion"""
    _fields_ = [
        ("client_major_version", ctypes.c_uint32),
        ("client_minor_version", ctypes.c_uint32),
    ]


QueryVersionReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('major_version', FixedDataPacketField(MARKER_UINT32)),
    ('minor_version', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(16)),
))


class QueryVersionReplyReply:
    __slots__ = ('major_version', 'minor_version',)

    def __init__(
            self, *,
            major_version: Optional[int] = None,
            minor_version: Optional[int] = None,
    ) -> None:
        self.major_version = major_version
        self.minor_version = minor_version

    def as_dict(self) -> Dict[str, Any]:
        return {
            'major_version': self.major_version,
            'minor_version': self.minor_version,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryVersionReplyReply':
        return QueryVersionReplyReply(**QueryVersionReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryVersionReplyReplyPacket.pack(**self.as_dict())


class QueryVersionReplyReplyCType(ctypes.Structure):
    """damage QueryVersion_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("major_version", ctypes.c_uint32),
        ("minor_version", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 16),
    ]


CreateRequestPacket = DataPacket((
    ('damage', FixedDataPacketField(MARKER_UINT32)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('level', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class CreateRequest:
    OPCODE = 1

    __slots__ = ('damage', 'drawable', 'level',)

    def __init__(
            self, *,
            damage: Optional[int] = None,
            drawable: Optional[int] = None,
            level: Optional[int] = None,
    ) -> None:
        self.damage = damage
        self.drawable = drawable
        self.level = level

    def as_dict(self) -> Dict[str, Any]:
        return {
            'damage': self.damage,
            'drawable': self.drawable,
            'level': self.level,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateRequest':
        return CreateRequest(**CreateRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateRequest.lib = library.damage_create
        CreateRequest.lib.restype = ctypes.c_uint32
        CreateRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8 * 3)


class CreateRequestCType(ctypes.Structure):
    """damage Create"""
    _fields_ = [
        ("damage", ctypes.c_uint32),
        ("drawable", ctypes.c_uint32),
        ("level", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


DestroyRequestPacket = DataPacket((
    ('damage', FixedDataPacketField(MARKER_UINT32)),
))


class DestroyRequest:
    OPCODE = 2

    __slots__ = ('damage',)

    def __init__(
            self, *,
            damage: Optional[int] = None,
    ) -> None:
        self.damage = damage

    def as_dict(self) -> Dict[str, Any]:
        return {
            'damage': self.damage,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DestroyRequest':
        return DestroyRequest(**DestroyRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DestroyRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        DestroyRequest.lib = library.damage_destroy
        DestroyRequest.lib.restype = ctypes.c_uint32
        DestroyRequest.lib.argstype = (ctypes.c_uint32,)


class DestroyRequestCType(ctypes.Structure):
    """damage Destroy"""
    _fields_ = [
        ("damage", ctypes.c_uint32),
    ]


SubtractRequestPacket = DataPacket((
    ('damage', FixedDataPacketField(MARKER_UINT32)),
    ('repair', FixedDataPacketField(MARKER_UINT32)),
    ('parts', FixedDataPacketField(MARKER_UINT32)),
))


class SubtractRequest:
    OPCODE = 3

    __slots__ = ('damage', 'repair', 'parts',)

    def __init__(
            self, *,
            damage: Optional[int] = None,
            repair: Optional[int] = None,
            parts: Optional[int] = None,
    ) -> None:
        self.damage = damage
        self.repair = repair
        self.parts = parts

    def as_dict(self) -> Dict[str, Any]:
        return {
            'damage': self.damage,
            'repair': self.repair,
            'parts': self.parts,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SubtractRequest':
        return SubtractRequest(**SubtractRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SubtractRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SubtractRequest.lib = library.damage_subtract
        SubtractRequest.lib.restype = ctypes.c_uint32
        SubtractRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class SubtractRequestCType(ctypes.Structure):
    """damage Subtract"""
    _fields_ = [
        ("damage", ctypes.c_uint32),
        ("repair", ctypes.c_uint32),
        ("parts", ctypes.c_uint32),
    ]


AddRequestPacket = DataPacket((
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('region', FixedDataPacketField(MARKER_UINT32)),
))


class AddRequest:
    OPCODE = 4

    __slots__ = ('drawable', 'region',)

    def __init__(
            self, *,
            drawable: Optional[int] = None,
            region: Optional[int] = None,
    ) -> None:
        self.drawable = drawable
        self.region = region

    def as_dict(self) -> Dict[str, Any]:
        return {
            'drawable': self.drawable,
            'region': self.region,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'AddRequest':
        return AddRequest(**AddRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return AddRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        AddRequest.lib = library.damage_add
        AddRequest.lib.restype = ctypes.c_uint32
        AddRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class AddRequestCType(ctypes.Structure):
    """damage Add"""
    _fields_ = [
        ("drawable", ctypes.c_uint32),
        ("region", ctypes.c_uint32),
    ]


NotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('level', FixedDataPacketField(MARKER_UINT8)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('damage', FixedDataPacketField(MARKER_UINT32)),
    ('timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('area', FixedDataPacketField(MARKER_UINT32)),
    ('geometry', FixedDataPacketField(MARKER_UINT32)),
))


class NotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'level', 'drawable', 'damage', 'timestamp', 'area', 'geometry',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            level: Optional[int] = None,
            drawable: Optional[int] = None,
            damage: Optional[int] = None,
            timestamp: Optional[int] = None,
            area: Optional[int] = None,
            geometry: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.level = level
        self.drawable = drawable
        self.damage = damage
        self.timestamp = timestamp
        self.area = area
        self.geometry = geometry

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'level': self.level,
            'drawable': self.drawable,
            'damage': self.damage,
            'timestamp': self.timestamp,
            'area': self.area,
            'geometry': self.geometry,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'NotifyEvent':
        return NotifyEvent(**NotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return NotifyEventPacket.pack(**self.as_dict())


class NotifyEventCType(ctypes.Structure):
    """damage Notify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("level", ctypes.c_uint8),
        ("drawable", ctypes.c_uint32),
        ("damage", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint32),
        ("area", ctypes.c_uint32),
        ("geometry", ctypes.c_uint32),
    ]


# ------------------------------------------------------------------
# Unions

