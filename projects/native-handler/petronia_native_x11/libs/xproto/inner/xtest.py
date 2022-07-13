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

CursorType = NewType('CursorType', int)


class CursorValues:
    NONE = CursorType(0)
    CURRENT = CursorType(1)


# ------------------------------------------------------------------
# Aliases



# ------------------------------------------------------------------
# Structures, Events, Requests, Replies


GetVersionRequestCookie = NewType('GetVersionRequestCookie', ctypes.c_uint32)


GetVersionRequestPacket = DataPacket((
    ('major_version', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('minor_version', FixedDataPacketField(MARKER_UINT16)),
))


class GetVersionRequest:
    OPCODE = 0

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
    def from_data(inp: BinaryIO) -> 'GetVersionRequest':
        return GetVersionRequest(**GetVersionRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetVersionRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], GetVersionRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetVersionRequest.lib = library.xtest_getversion
        GetVersionRequest.lib.restype = GetVersionRequestCookie
        GetVersionRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint16)


class GetVersionRequestCType(ctypes.Structure):
    """xtest GetVersion"""
    _fields_ = [
        ("major_version", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
        ("minor_version", ctypes.c_uint16),
    ]


GetVersionReplyReplyPacket = DataPacket((
    ('major_version', FixedDataPacketField(MARKER_UINT8)),
    ('minor_version', FixedDataPacketField(MARKER_UINT16)),
))


class GetVersionReplyReply:
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
    def from_data(inp: BinaryIO) -> 'GetVersionReplyReply':
        return GetVersionReplyReply(**GetVersionReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetVersionReplyReplyPacket.pack(**self.as_dict())


class GetVersionReplyReplyCType(ctypes.Structure):
    """xtest GetVersion_reply"""
    _fields_ = [
        ("major_version", ctypes.c_uint8),
        ("minor_version", ctypes.c_uint16),
    ]


CompareCursorRequestCookie = NewType('CompareCursorRequestCookie', ctypes.c_uint32)


CompareCursorRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('cursor', FixedDataPacketField(MARKER_UINT32)),
))


class CompareCursorRequest:
    OPCODE = 1

    __slots__ = ('window', 'cursor',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            cursor: Optional[int] = None,
    ) -> None:
        self.window = window
        self.cursor = cursor

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'cursor': self.cursor,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CompareCursorRequest':
        return CompareCursorRequest(**CompareCursorRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CompareCursorRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], CompareCursorRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CompareCursorRequest.lib = library.xtest_comparecursor
        CompareCursorRequest.lib.restype = CompareCursorRequestCookie
        CompareCursorRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class CompareCursorRequestCType(ctypes.Structure):
    """xtest CompareCursor"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("cursor", ctypes.c_uint32),
    ]


CompareCursorReplyReplyPacket = DataPacket((
    ('same', FixedDataPacketField(MARKER_UINT8)),
))


class CompareCursorReplyReply:
    __slots__ = ('same',)

    def __init__(
            self, *,
            same: Optional[bool] = None,
    ) -> None:
        self.same = same

    def as_dict(self) -> Dict[str, Any]:
        return {
            'same': self.same,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CompareCursorReplyReply':
        return CompareCursorReplyReply(**CompareCursorReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CompareCursorReplyReplyPacket.pack(**self.as_dict())


class CompareCursorReplyReplyCType(ctypes.Structure):
    """xtest CompareCursor_reply"""
    _fields_ = [
        ("same", ctypes.c_int8),
    ]


FakeInputRequestPacket = DataPacket((
    ('type', FixedDataPacketField(MARKER_INT8)),
    ('detail', FixedDataPacketField(MARKER_INT8)),
    ('pad0', FixedPadDataPacketField(2)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('root', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(8)),
    ('rootX', FixedDataPacketField(MARKER_INT16)),
    ('rootY', FixedDataPacketField(MARKER_INT16)),
    ('pad2', FixedPadDataPacketField(7)),
    ('deviceid', FixedDataPacketField(MARKER_UINT8)),
))


class FakeInputRequest:
    OPCODE = 2

    __slots__ = ('type', 'detail', 'time', 'root', 'rootx', 'rooty', 'deviceid',)

    def __init__(
            self, *,
            type: Optional[int] = None,
            detail: Optional[int] = None,
            time: Optional[int] = None,
            root: Optional[int] = None,
            rootx: Optional[int] = None,
            rooty: Optional[int] = None,
            deviceid: Optional[int] = None,
    ) -> None:
        self.type = type
        self.detail = detail
        self.time = time
        self.root = root
        self.rootx = rootx
        self.rooty = rooty
        self.deviceid = deviceid

    def as_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type,
            'detail': self.detail,
            'time': self.time,
            'root': self.root,
            'rootX': self.rootx,
            'rootY': self.rooty,
            'deviceid': self.deviceid,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'FakeInputRequest':
        return FakeInputRequest(**FakeInputRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return FakeInputRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        FakeInputRequest.lib = library.xtest_fakeinput
        FakeInputRequest.lib.restype = ctypes.c_uint32
        FakeInputRequest.lib.argstype = (ctypes.c_int8, ctypes.c_int8, ctypes.c_uint8 * 2, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8 * 8, ctypes.c_int16, ctypes.c_int16, ctypes.c_uint8 * 7, ctypes.c_uint8)


class FakeInputRequestCType(ctypes.Structure):
    """xtest FakeInput"""
    _fields_ = [
        ("type", ctypes.c_int8),
        ("detail", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 2),
        ("time", ctypes.c_uint32),
        ("root", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 8),
        ("rootX", ctypes.c_int16),
        ("rootY", ctypes.c_int16),
        ("pad2", ctypes.c_uint8 * 7),
        ("deviceid", ctypes.c_uint8),
    ]


GrabControlRequestPacket = DataPacket((
    ('impervious', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class GrabControlRequest:
    OPCODE = 3

    __slots__ = ('impervious',)

    def __init__(
            self, *,
            impervious: Optional[bool] = None,
    ) -> None:
        self.impervious = impervious

    def as_dict(self) -> Dict[str, Any]:
        return {
            'impervious': self.impervious,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GrabControlRequest':
        return GrabControlRequest(**GrabControlRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GrabControlRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[bool], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GrabControlRequest.lib = library.xtest_grabcontrol
        GrabControlRequest.lib.restype = ctypes.c_uint32
        GrabControlRequest.lib.argstype = (ctypes.c_int8, ctypes.c_uint8 * 3)


class GrabControlRequestCType(ctypes.Structure):
    """xtest GrabControl"""
    _fields_ = [
        ("impervious", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


# ------------------------------------------------------------------
# Unions

