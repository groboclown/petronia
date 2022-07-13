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


ScreenInfoStructPacket = DataPacket((
    ('x_org', FixedDataPacketField(MARKER_INT16)),
    ('y_org', FixedDataPacketField(MARKER_INT16)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
))


class ScreenInfoStruct:
    __slots__ = ('x_org', 'y_org', 'width', 'height',)

    def __init__(
            self, *,
            x_org: Optional[int] = None,
            y_org: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
    ) -> None:
        self.x_org = x_org
        self.y_org = y_org
        self.width = width
        self.height = height

    def as_dict(self) -> Dict[str, Any]:
        return {
            'x_org': self.x_org,
            'y_org': self.y_org,
            'width': self.width,
            'height': self.height,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ScreenInfoStruct':
        return ScreenInfoStruct(**ScreenInfoStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ScreenInfoStructPacket.pack(**self.as_dict())


class ScreenInfoStructCType(ctypes.Structure):
    """xinerama ScreenInfo"""
    _fields_ = [
        ("x_org", ctypes.c_int16),
        ("y_org", ctypes.c_int16),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
    ]


QueryVersionRequestCookie = NewType('QueryVersionRequestCookie', ctypes.c_uint32)


QueryVersionRequestPacket = DataPacket((
    ('major', FixedDataPacketField(MARKER_UINT8)),
    ('minor', FixedDataPacketField(MARKER_UINT8)),
))


class QueryVersionRequest:
    OPCODE = 0

    __slots__ = ('major', 'minor',)

    def __init__(
            self, *,
            major: Optional[int] = None,
            minor: Optional[int] = None,
    ) -> None:
        self.major = major
        self.minor = minor

    def as_dict(self) -> Dict[str, Any]:
        return {
            'major': self.major,
            'minor': self.minor,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryVersionRequest':
        return QueryVersionRequest(**QueryVersionRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryVersionRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], QueryVersionRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryVersionRequest.lib = library.xinerama_queryversion
        QueryVersionRequest.lib.restype = QueryVersionRequestCookie
        QueryVersionRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint8)


class QueryVersionRequestCType(ctypes.Structure):
    """xinerama QueryVersion"""
    _fields_ = [
        ("major", ctypes.c_uint8),
        ("minor", ctypes.c_uint8),
    ]


QueryVersionReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('major', FixedDataPacketField(MARKER_UINT16)),
    ('minor', FixedDataPacketField(MARKER_UINT16)),
))


class QueryVersionReplyReply:
    __slots__ = ('major', 'minor',)

    def __init__(
            self, *,
            major: Optional[int] = None,
            minor: Optional[int] = None,
    ) -> None:
        self.major = major
        self.minor = minor

    def as_dict(self) -> Dict[str, Any]:
        return {
            'major': self.major,
            'minor': self.minor,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryVersionReplyReply':
        return QueryVersionReplyReply(**QueryVersionReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryVersionReplyReplyPacket.pack(**self.as_dict())


class QueryVersionReplyReplyCType(ctypes.Structure):
    """xinerama QueryVersion_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("major", ctypes.c_uint16),
        ("minor", ctypes.c_uint16),
    ]


GetStateRequestCookie = NewType('GetStateRequestCookie', ctypes.c_uint32)


GetStateRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class GetStateRequest:
    OPCODE = 1

    __slots__ = ('window',)

    def __init__(
            self, *,
            window: Optional[int] = None,
    ) -> None:
        self.window = window

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetStateRequest':
        return GetStateRequest(**GetStateRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetStateRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetStateRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetStateRequest.lib = library.xinerama_getstate
        GetStateRequest.lib.restype = GetStateRequestCookie
        GetStateRequest.lib.argstype = (ctypes.c_uint32,)


class GetStateRequestCType(ctypes.Structure):
    """xinerama GetState"""
    _fields_ = [
        ("window", ctypes.c_uint32),
    ]


GetStateReplyReplyPacket = DataPacket((
    ('state', FixedDataPacketField(MARKER_INT8)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class GetStateReplyReply:
    __slots__ = ('state', 'window',)

    def __init__(
            self, *,
            state: Optional[int] = None,
            window: Optional[int] = None,
    ) -> None:
        self.state = state
        self.window = window

    def as_dict(self) -> Dict[str, Any]:
        return {
            'state': self.state,
            'window': self.window,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetStateReplyReply':
        return GetStateReplyReply(**GetStateReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetStateReplyReplyPacket.pack(**self.as_dict())


class GetStateReplyReplyCType(ctypes.Structure):
    """xinerama GetState_reply"""
    _fields_ = [
        ("state", ctypes.c_int8),
        ("window", ctypes.c_uint32),
    ]


GetScreenCountRequestCookie = NewType('GetScreenCountRequestCookie', ctypes.c_uint32)


GetScreenCountRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class GetScreenCountRequest:
    OPCODE = 2

    __slots__ = ('window',)

    def __init__(
            self, *,
            window: Optional[int] = None,
    ) -> None:
        self.window = window

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetScreenCountRequest':
        return GetScreenCountRequest(**GetScreenCountRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetScreenCountRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetScreenCountRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetScreenCountRequest.lib = library.xinerama_getscreencount
        GetScreenCountRequest.lib.restype = GetScreenCountRequestCookie
        GetScreenCountRequest.lib.argstype = (ctypes.c_uint32,)


class GetScreenCountRequestCType(ctypes.Structure):
    """xinerama GetScreenCount"""
    _fields_ = [
        ("window", ctypes.c_uint32),
    ]


GetScreenCountReplyReplyPacket = DataPacket((
    ('screen_count', FixedDataPacketField(MARKER_INT8)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class GetScreenCountReplyReply:
    __slots__ = ('screen_count', 'window',)

    def __init__(
            self, *,
            screen_count: Optional[int] = None,
            window: Optional[int] = None,
    ) -> None:
        self.screen_count = screen_count
        self.window = window

    def as_dict(self) -> Dict[str, Any]:
        return {
            'screen_count': self.screen_count,
            'window': self.window,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetScreenCountReplyReply':
        return GetScreenCountReplyReply(**GetScreenCountReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetScreenCountReplyReplyPacket.pack(**self.as_dict())


class GetScreenCountReplyReplyCType(ctypes.Structure):
    """xinerama GetScreenCount_reply"""
    _fields_ = [
        ("screen_count", ctypes.c_int8),
        ("window", ctypes.c_uint32),
    ]


GetScreenSizeRequestCookie = NewType('GetScreenSizeRequestCookie', ctypes.c_uint32)


GetScreenSizeRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('screen', FixedDataPacketField(MARKER_UINT32)),
))


class GetScreenSizeRequest:
    OPCODE = 3

    __slots__ = ('window', 'screen',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            screen: Optional[int] = None,
    ) -> None:
        self.window = window
        self.screen = screen

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'screen': self.screen,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetScreenSizeRequest':
        return GetScreenSizeRequest(**GetScreenSizeRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetScreenSizeRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], GetScreenSizeRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetScreenSizeRequest.lib = library.xinerama_getscreensize
        GetScreenSizeRequest.lib.restype = GetScreenSizeRequestCookie
        GetScreenSizeRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class GetScreenSizeRequestCType(ctypes.Structure):
    """xinerama GetScreenSize"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("screen", ctypes.c_uint32),
    ]


GetScreenSizeReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('width', FixedDataPacketField(MARKER_UINT32)),
    ('height', FixedDataPacketField(MARKER_UINT32)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('screen', FixedDataPacketField(MARKER_UINT32)),
))


class GetScreenSizeReplyReply:
    __slots__ = ('width', 'height', 'window', 'screen',)

    def __init__(
            self, *,
            width: Optional[int] = None,
            height: Optional[int] = None,
            window: Optional[int] = None,
            screen: Optional[int] = None,
    ) -> None:
        self.width = width
        self.height = height
        self.window = window
        self.screen = screen

    def as_dict(self) -> Dict[str, Any]:
        return {
            'width': self.width,
            'height': self.height,
            'window': self.window,
            'screen': self.screen,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetScreenSizeReplyReply':
        return GetScreenSizeReplyReply(**GetScreenSizeReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetScreenSizeReplyReplyPacket.pack(**self.as_dict())


class GetScreenSizeReplyReplyCType(ctypes.Structure):
    """xinerama GetScreenSize_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("width", ctypes.c_uint32),
        ("height", ctypes.c_uint32),
        ("window", ctypes.c_uint32),
        ("screen", ctypes.c_uint32),
    ]


IsActiveRequestCookie = NewType('IsActiveRequestCookie', ctypes.c_uint32)


IsActiveRequestPacket = DataPacket((
))


class IsActiveRequest:
    OPCODE = 4

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'IsActiveRequest':
        return IsActiveRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], IsActiveRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        IsActiveRequest.lib = library.xinerama_isactive
        IsActiveRequest.lib.restype = IsActiveRequestCookie
        IsActiveRequest.lib.argstype = ()


class IsActiveRequestCType(ctypes.Structure):
    """xinerama IsActive"""
    _fields_ = [
    ]


IsActiveReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('state', FixedDataPacketField(MARKER_UINT32)),
))


class IsActiveReplyReply:
    __slots__ = ('state',)

    def __init__(
            self, *,
            state: Optional[int] = None,
    ) -> None:
        self.state = state

    def as_dict(self) -> Dict[str, Any]:
        return {
            'state': self.state,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'IsActiveReplyReply':
        return IsActiveReplyReply(**IsActiveReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return IsActiveReplyReplyPacket.pack(**self.as_dict())


class IsActiveReplyReplyCType(ctypes.Structure):
    """xinerama IsActive_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("state", ctypes.c_uint32),
    ]


QueryScreensRequestCookie = NewType('QueryScreensRequestCookie', ctypes.c_uint32)


QueryScreensRequestPacket = DataPacket((
))


class QueryScreensRequest:
    OPCODE = 5

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryScreensRequest':
        return QueryScreensRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], QueryScreensRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryScreensRequest.lib = library.xinerama_queryscreens
        QueryScreensRequest.lib.restype = QueryScreensRequestCookie
        QueryScreensRequest.lib.argstype = ()


class QueryScreensRequestCType(ctypes.Structure):
    """xinerama QueryScreens"""
    _fields_ = [
    ]


QueryScreensReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('number', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('screen_info', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['number'], 0)),
))


class QueryScreensReplyReply:
    __slots__ = ('number', 'screen_info',)

    def __init__(
            self, *,
            number: Optional[int] = None,
            screen_info: Optional[Sequence[int]] = None,
    ) -> None:
        self.number = number
        self.screen_info = screen_info

    def as_dict(self) -> Dict[str, Any]:
        return {
            'number': self.number,
            'screen_info': self.screen_info,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryScreensReplyReply':
        return QueryScreensReplyReply(**QueryScreensReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryScreensReplyReplyPacket.pack(**self.as_dict())


class QueryScreensReplyReplyCType(ctypes.Structure):
    """xinerama QueryScreens_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("number", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


# ------------------------------------------------------------------
# Unions

