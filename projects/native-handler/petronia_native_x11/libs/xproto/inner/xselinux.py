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


QueryVersionRequestCookie = NewType('QueryVersionRequestCookie', ctypes.c_uint32)


QueryVersionRequestPacket = DataPacket((
    ('client_major', FixedDataPacketField(MARKER_UINT8)),
    ('client_minor', FixedDataPacketField(MARKER_UINT8)),
))


class QueryVersionRequest:
    OPCODE = 0

    __slots__ = ('client_major', 'client_minor',)

    def __init__(
            self, *,
            client_major: Optional[int] = None,
            client_minor: Optional[int] = None,
    ) -> None:
        self.client_major = client_major
        self.client_minor = client_minor

    def as_dict(self) -> Dict[str, Any]:
        return {
            'client_major': self.client_major,
            'client_minor': self.client_minor,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryVersionRequest':
        return QueryVersionRequest(**QueryVersionRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryVersionRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], QueryVersionRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryVersionRequest.lib = library.xselinux_queryversion
        QueryVersionRequest.lib.restype = QueryVersionRequestCookie
        QueryVersionRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint8)


class QueryVersionRequestCType(ctypes.Structure):
    """xselinux QueryVersion"""
    _fields_ = [
        ("client_major", ctypes.c_uint8),
        ("client_minor", ctypes.c_uint8),
    ]


QueryVersionReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('server_major', FixedDataPacketField(MARKER_UINT16)),
    ('server_minor', FixedDataPacketField(MARKER_UINT16)),
))


class QueryVersionReplyReply:
    __slots__ = ('server_major', 'server_minor',)

    def __init__(
            self, *,
            server_major: Optional[int] = None,
            server_minor: Optional[int] = None,
    ) -> None:
        self.server_major = server_major
        self.server_minor = server_minor

    def as_dict(self) -> Dict[str, Any]:
        return {
            'server_major': self.server_major,
            'server_minor': self.server_minor,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryVersionReplyReply':
        return QueryVersionReplyReply(**QueryVersionReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryVersionReplyReplyPacket.pack(**self.as_dict())


class QueryVersionReplyReplyCType(ctypes.Structure):
    """xselinux QueryVersion_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("server_major", ctypes.c_uint16),
        ("server_minor", ctypes.c_uint16),
    ]


SetDeviceCreateContextRequestPacket = DataPacket((
    ('context_len', FixedDataPacketField(MARKER_UINT32)),
    ('context', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['context_len'], 0)),
))


class SetDeviceCreateContextRequest:
    OPCODE = 1

    __slots__ = ('context_len', 'context',)

    def __init__(
            self, *,
            context_len: Optional[int] = None,
            context: Optional[Sequence[int]] = None,
    ) -> None:
        self.context_len = context_len
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_len': self.context_len,
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetDeviceCreateContextRequest':
        return SetDeviceCreateContextRequest(**SetDeviceCreateContextRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetDeviceCreateContextRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetDeviceCreateContextRequest.lib = library.xselinux_setdevicecreatecontext
        SetDeviceCreateContextRequest.lib.restype = ctypes.c_uint32
        SetDeviceCreateContextRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_void_p)


class SetDeviceCreateContextRequestCType(ctypes.Structure):
    """xselinux SetDeviceCreateContext"""
    _fields_ = [
        ("context_len", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


GetDeviceCreateContextRequestCookie = NewType('GetDeviceCreateContextRequestCookie', ctypes.c_uint32)


GetDeviceCreateContextRequestPacket = DataPacket((
))


class GetDeviceCreateContextRequest:
    OPCODE = 2

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetDeviceCreateContextRequest':
        return GetDeviceCreateContextRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], GetDeviceCreateContextRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetDeviceCreateContextRequest.lib = library.xselinux_getdevicecreatecontext
        GetDeviceCreateContextRequest.lib.restype = GetDeviceCreateContextRequestCookie
        GetDeviceCreateContextRequest.lib.argstype = ()


class GetDeviceCreateContextRequestCType(ctypes.Structure):
    """xselinux GetDeviceCreateContext"""
    _fields_ = [
    ]


GetDeviceCreateContextReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('context_len', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('context', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['context_len'], 0)),
))


class GetDeviceCreateContextReplyReply:
    __slots__ = ('context_len', 'context',)

    def __init__(
            self, *,
            context_len: Optional[int] = None,
            context: Optional[Sequence[int]] = None,
    ) -> None:
        self.context_len = context_len
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_len': self.context_len,
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetDeviceCreateContextReplyReply':
        return GetDeviceCreateContextReplyReply(**GetDeviceCreateContextReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetDeviceCreateContextReplyReplyPacket.pack(**self.as_dict())


class GetDeviceCreateContextReplyReplyCType(ctypes.Structure):
    """xselinux GetDeviceCreateContext_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("context_len", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


SetDeviceContextRequestPacket = DataPacket((
    ('device', FixedDataPacketField(MARKER_UINT32)),
    ('context_len', FixedDataPacketField(MARKER_UINT32)),
    ('context', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['context_len'], 0)),
))


class SetDeviceContextRequest:
    OPCODE = 3

    __slots__ = ('device', 'context_len', 'context',)

    def __init__(
            self, *,
            device: Optional[int] = None,
            context_len: Optional[int] = None,
            context: Optional[Sequence[int]] = None,
    ) -> None:
        self.device = device
        self.context_len = context_len
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'device': self.device,
            'context_len': self.context_len,
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetDeviceContextRequest':
        return SetDeviceContextRequest(**SetDeviceContextRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetDeviceContextRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetDeviceContextRequest.lib = library.xselinux_setdevicecontext
        SetDeviceContextRequest.lib.restype = ctypes.c_uint32
        SetDeviceContextRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)


class SetDeviceContextRequestCType(ctypes.Structure):
    """xselinux SetDeviceContext"""
    _fields_ = [
        ("device", ctypes.c_uint32),
        ("context_len", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


GetDeviceContextRequestCookie = NewType('GetDeviceContextRequestCookie', ctypes.c_uint32)


GetDeviceContextRequestPacket = DataPacket((
    ('device', FixedDataPacketField(MARKER_UINT32)),
))


class GetDeviceContextRequest:
    OPCODE = 4

    __slots__ = ('device',)

    def __init__(
            self, *,
            device: Optional[int] = None,
    ) -> None:
        self.device = device

    def as_dict(self) -> Dict[str, Any]:
        return {
            'device': self.device,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetDeviceContextRequest':
        return GetDeviceContextRequest(**GetDeviceContextRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetDeviceContextRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetDeviceContextRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetDeviceContextRequest.lib = library.xselinux_getdevicecontext
        GetDeviceContextRequest.lib.restype = GetDeviceContextRequestCookie
        GetDeviceContextRequest.lib.argstype = (ctypes.c_uint32,)


class GetDeviceContextRequestCType(ctypes.Structure):
    """xselinux GetDeviceContext"""
    _fields_ = [
        ("device", ctypes.c_uint32),
    ]


GetDeviceContextReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('context_len', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('context', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['context_len'], 0)),
))


class GetDeviceContextReplyReply:
    __slots__ = ('context_len', 'context',)

    def __init__(
            self, *,
            context_len: Optional[int] = None,
            context: Optional[Sequence[int]] = None,
    ) -> None:
        self.context_len = context_len
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_len': self.context_len,
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetDeviceContextReplyReply':
        return GetDeviceContextReplyReply(**GetDeviceContextReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetDeviceContextReplyReplyPacket.pack(**self.as_dict())


class GetDeviceContextReplyReplyCType(ctypes.Structure):
    """xselinux GetDeviceContext_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("context_len", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


SetWindowCreateContextRequestPacket = DataPacket((
    ('context_len', FixedDataPacketField(MARKER_UINT32)),
    ('context', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['context_len'], 0)),
))


class SetWindowCreateContextRequest:
    OPCODE = 5

    __slots__ = ('context_len', 'context',)

    def __init__(
            self, *,
            context_len: Optional[int] = None,
            context: Optional[Sequence[int]] = None,
    ) -> None:
        self.context_len = context_len
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_len': self.context_len,
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetWindowCreateContextRequest':
        return SetWindowCreateContextRequest(**SetWindowCreateContextRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetWindowCreateContextRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetWindowCreateContextRequest.lib = library.xselinux_setwindowcreatecontext
        SetWindowCreateContextRequest.lib.restype = ctypes.c_uint32
        SetWindowCreateContextRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_void_p)


class SetWindowCreateContextRequestCType(ctypes.Structure):
    """xselinux SetWindowCreateContext"""
    _fields_ = [
        ("context_len", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


GetWindowCreateContextRequestCookie = NewType('GetWindowCreateContextRequestCookie', ctypes.c_uint32)


GetWindowCreateContextRequestPacket = DataPacket((
))


class GetWindowCreateContextRequest:
    OPCODE = 6

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetWindowCreateContextRequest':
        return GetWindowCreateContextRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], GetWindowCreateContextRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetWindowCreateContextRequest.lib = library.xselinux_getwindowcreatecontext
        GetWindowCreateContextRequest.lib.restype = GetWindowCreateContextRequestCookie
        GetWindowCreateContextRequest.lib.argstype = ()


class GetWindowCreateContextRequestCType(ctypes.Structure):
    """xselinux GetWindowCreateContext"""
    _fields_ = [
    ]


GetWindowCreateContextReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('context_len', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('context', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['context_len'], 0)),
))


class GetWindowCreateContextReplyReply:
    __slots__ = ('context_len', 'context',)

    def __init__(
            self, *,
            context_len: Optional[int] = None,
            context: Optional[Sequence[int]] = None,
    ) -> None:
        self.context_len = context_len
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_len': self.context_len,
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetWindowCreateContextReplyReply':
        return GetWindowCreateContextReplyReply(**GetWindowCreateContextReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetWindowCreateContextReplyReplyPacket.pack(**self.as_dict())


class GetWindowCreateContextReplyReplyCType(ctypes.Structure):
    """xselinux GetWindowCreateContext_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("context_len", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


GetWindowContextRequestCookie = NewType('GetWindowContextRequestCookie', ctypes.c_uint32)


GetWindowContextRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class GetWindowContextRequest:
    OPCODE = 7

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
    def from_data(inp: BinaryIO) -> 'GetWindowContextRequest':
        return GetWindowContextRequest(**GetWindowContextRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetWindowContextRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetWindowContextRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetWindowContextRequest.lib = library.xselinux_getwindowcontext
        GetWindowContextRequest.lib.restype = GetWindowContextRequestCookie
        GetWindowContextRequest.lib.argstype = (ctypes.c_uint32,)


class GetWindowContextRequestCType(ctypes.Structure):
    """xselinux GetWindowContext"""
    _fields_ = [
        ("window", ctypes.c_uint32),
    ]


GetWindowContextReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('context_len', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('context', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['context_len'], 0)),
))


class GetWindowContextReplyReply:
    __slots__ = ('context_len', 'context',)

    def __init__(
            self, *,
            context_len: Optional[int] = None,
            context: Optional[Sequence[int]] = None,
    ) -> None:
        self.context_len = context_len
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_len': self.context_len,
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetWindowContextReplyReply':
        return GetWindowContextReplyReply(**GetWindowContextReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetWindowContextReplyReplyPacket.pack(**self.as_dict())


class GetWindowContextReplyReplyCType(ctypes.Structure):
    """xselinux GetWindowContext_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("context_len", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


ListItemStructPacket = DataPacket((
    ('name', FixedDataPacketField(MARKER_UINT32)),
    ('object_context_len', FixedDataPacketField(MARKER_UINT32)),
    ('data_context_len', FixedDataPacketField(MARKER_UINT32)),
    ('object_context', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['object_context_len'], 0)),
    ('pad0', AlignedPadDataPacketField(4)),
    ('data_context', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['data_context_len'], 0)),
    ('pad1', AlignedPadDataPacketField(4)),
))


class ListItemStruct:
    __slots__ = ('name', 'object_context_len', 'data_context_len', 'object_context', 'data_context',)

    def __init__(
            self, *,
            name: Optional[int] = None,
            object_context_len: Optional[int] = None,
            data_context_len: Optional[int] = None,
            object_context: Optional[Sequence[int]] = None,
            data_context: Optional[Sequence[int]] = None,
    ) -> None:
        self.name = name
        self.object_context_len = object_context_len
        self.data_context_len = data_context_len
        self.object_context = object_context
        self.data_context = data_context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'name': self.name,
            'object_context_len': self.object_context_len,
            'data_context_len': self.data_context_len,
            'object_context': self.object_context,
            'data_context': self.data_context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ListItemStruct':
        return ListItemStruct(**ListItemStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ListItemStructPacket.pack(**self.as_dict())


class ListItemStructCType(ctypes.Structure):
    """xselinux ListItem"""
    _fields_ = [
        ("name", ctypes.c_uint32),
        ("object_context_len", ctypes.c_uint32),
        ("data_context_len", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


SetPropertyCreateContextRequestPacket = DataPacket((
    ('context_len', FixedDataPacketField(MARKER_UINT32)),
    ('context', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['context_len'], 0)),
))


class SetPropertyCreateContextRequest:
    OPCODE = 8

    __slots__ = ('context_len', 'context',)

    def __init__(
            self, *,
            context_len: Optional[int] = None,
            context: Optional[Sequence[int]] = None,
    ) -> None:
        self.context_len = context_len
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_len': self.context_len,
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetPropertyCreateContextRequest':
        return SetPropertyCreateContextRequest(**SetPropertyCreateContextRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetPropertyCreateContextRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetPropertyCreateContextRequest.lib = library.xselinux_setpropertycreatecontext
        SetPropertyCreateContextRequest.lib.restype = ctypes.c_uint32
        SetPropertyCreateContextRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_void_p)


class SetPropertyCreateContextRequestCType(ctypes.Structure):
    """xselinux SetPropertyCreateContext"""
    _fields_ = [
        ("context_len", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


GetPropertyCreateContextRequestCookie = NewType('GetPropertyCreateContextRequestCookie', ctypes.c_uint32)


GetPropertyCreateContextRequestPacket = DataPacket((
))


class GetPropertyCreateContextRequest:
    OPCODE = 9

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetPropertyCreateContextRequest':
        return GetPropertyCreateContextRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], GetPropertyCreateContextRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetPropertyCreateContextRequest.lib = library.xselinux_getpropertycreatecontext
        GetPropertyCreateContextRequest.lib.restype = GetPropertyCreateContextRequestCookie
        GetPropertyCreateContextRequest.lib.argstype = ()


class GetPropertyCreateContextRequestCType(ctypes.Structure):
    """xselinux GetPropertyCreateContext"""
    _fields_ = [
    ]


GetPropertyCreateContextReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('context_len', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('context', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['context_len'], 0)),
))


class GetPropertyCreateContextReplyReply:
    __slots__ = ('context_len', 'context',)

    def __init__(
            self, *,
            context_len: Optional[int] = None,
            context: Optional[Sequence[int]] = None,
    ) -> None:
        self.context_len = context_len
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_len': self.context_len,
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetPropertyCreateContextReplyReply':
        return GetPropertyCreateContextReplyReply(**GetPropertyCreateContextReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetPropertyCreateContextReplyReplyPacket.pack(**self.as_dict())


class GetPropertyCreateContextReplyReplyCType(ctypes.Structure):
    """xselinux GetPropertyCreateContext_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("context_len", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


SetPropertyUseContextRequestPacket = DataPacket((
    ('context_len', FixedDataPacketField(MARKER_UINT32)),
    ('context', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['context_len'], 0)),
))


class SetPropertyUseContextRequest:
    OPCODE = 10

    __slots__ = ('context_len', 'context',)

    def __init__(
            self, *,
            context_len: Optional[int] = None,
            context: Optional[Sequence[int]] = None,
    ) -> None:
        self.context_len = context_len
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_len': self.context_len,
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetPropertyUseContextRequest':
        return SetPropertyUseContextRequest(**SetPropertyUseContextRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetPropertyUseContextRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetPropertyUseContextRequest.lib = library.xselinux_setpropertyusecontext
        SetPropertyUseContextRequest.lib.restype = ctypes.c_uint32
        SetPropertyUseContextRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_void_p)


class SetPropertyUseContextRequestCType(ctypes.Structure):
    """xselinux SetPropertyUseContext"""
    _fields_ = [
        ("context_len", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


GetPropertyUseContextRequestCookie = NewType('GetPropertyUseContextRequestCookie', ctypes.c_uint32)


GetPropertyUseContextRequestPacket = DataPacket((
))


class GetPropertyUseContextRequest:
    OPCODE = 11

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetPropertyUseContextRequest':
        return GetPropertyUseContextRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], GetPropertyUseContextRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetPropertyUseContextRequest.lib = library.xselinux_getpropertyusecontext
        GetPropertyUseContextRequest.lib.restype = GetPropertyUseContextRequestCookie
        GetPropertyUseContextRequest.lib.argstype = ()


class GetPropertyUseContextRequestCType(ctypes.Structure):
    """xselinux GetPropertyUseContext"""
    _fields_ = [
    ]


GetPropertyUseContextReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('context_len', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('context', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['context_len'], 0)),
))


class GetPropertyUseContextReplyReply:
    __slots__ = ('context_len', 'context',)

    def __init__(
            self, *,
            context_len: Optional[int] = None,
            context: Optional[Sequence[int]] = None,
    ) -> None:
        self.context_len = context_len
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_len': self.context_len,
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetPropertyUseContextReplyReply':
        return GetPropertyUseContextReplyReply(**GetPropertyUseContextReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetPropertyUseContextReplyReplyPacket.pack(**self.as_dict())


class GetPropertyUseContextReplyReplyCType(ctypes.Structure):
    """xselinux GetPropertyUseContext_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("context_len", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


GetPropertyContextRequestCookie = NewType('GetPropertyContextRequestCookie', ctypes.c_uint32)


GetPropertyContextRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('property', FixedDataPacketField(MARKER_UINT32)),
))


class GetPropertyContextRequest:
    OPCODE = 12

    __slots__ = ('window', 'property',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            property: Optional[int] = None,
    ) -> None:
        self.window = window
        self.property = property

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'property': self.property,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetPropertyContextRequest':
        return GetPropertyContextRequest(**GetPropertyContextRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetPropertyContextRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], GetPropertyContextRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetPropertyContextRequest.lib = library.xselinux_getpropertycontext
        GetPropertyContextRequest.lib.restype = GetPropertyContextRequestCookie
        GetPropertyContextRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class GetPropertyContextRequestCType(ctypes.Structure):
    """xselinux GetPropertyContext"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("property", ctypes.c_uint32),
    ]


GetPropertyContextReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('context_len', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('context', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['context_len'], 0)),
))


class GetPropertyContextReplyReply:
    __slots__ = ('context_len', 'context',)

    def __init__(
            self, *,
            context_len: Optional[int] = None,
            context: Optional[Sequence[int]] = None,
    ) -> None:
        self.context_len = context_len
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_len': self.context_len,
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetPropertyContextReplyReply':
        return GetPropertyContextReplyReply(**GetPropertyContextReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetPropertyContextReplyReplyPacket.pack(**self.as_dict())


class GetPropertyContextReplyReplyCType(ctypes.Structure):
    """xselinux GetPropertyContext_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("context_len", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


GetPropertyDataContextRequestCookie = NewType('GetPropertyDataContextRequestCookie', ctypes.c_uint32)


GetPropertyDataContextRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('property', FixedDataPacketField(MARKER_UINT32)),
))


class GetPropertyDataContextRequest:
    OPCODE = 13

    __slots__ = ('window', 'property',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            property: Optional[int] = None,
    ) -> None:
        self.window = window
        self.property = property

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'property': self.property,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetPropertyDataContextRequest':
        return GetPropertyDataContextRequest(**GetPropertyDataContextRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetPropertyDataContextRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], GetPropertyDataContextRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetPropertyDataContextRequest.lib = library.xselinux_getpropertydatacontext
        GetPropertyDataContextRequest.lib.restype = GetPropertyDataContextRequestCookie
        GetPropertyDataContextRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class GetPropertyDataContextRequestCType(ctypes.Structure):
    """xselinux GetPropertyDataContext"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("property", ctypes.c_uint32),
    ]


GetPropertyDataContextReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('context_len', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('context', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['context_len'], 0)),
))


class GetPropertyDataContextReplyReply:
    __slots__ = ('context_len', 'context',)

    def __init__(
            self, *,
            context_len: Optional[int] = None,
            context: Optional[Sequence[int]] = None,
    ) -> None:
        self.context_len = context_len
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_len': self.context_len,
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetPropertyDataContextReplyReply':
        return GetPropertyDataContextReplyReply(**GetPropertyDataContextReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetPropertyDataContextReplyReplyPacket.pack(**self.as_dict())


class GetPropertyDataContextReplyReplyCType(ctypes.Structure):
    """xselinux GetPropertyDataContext_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("context_len", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


ListPropertiesRequestCookie = NewType('ListPropertiesRequestCookie', ctypes.c_uint32)


ListPropertiesRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class ListPropertiesRequest:
    OPCODE = 14

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
    def from_data(inp: BinaryIO) -> 'ListPropertiesRequest':
        return ListPropertiesRequest(**ListPropertiesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ListPropertiesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ListPropertiesRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ListPropertiesRequest.lib = library.xselinux_listproperties
        ListPropertiesRequest.lib.restype = ListPropertiesRequestCookie
        ListPropertiesRequest.lib.argstype = (ctypes.c_uint32,)


class ListPropertiesRequestCType(ctypes.Structure):
    """xselinux ListProperties"""
    _fields_ = [
        ("window", ctypes.c_uint32),
    ]


ListPropertiesReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('properties_len', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('properties', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['properties_len'], 0)),
))


class ListPropertiesReplyReply:
    __slots__ = ('properties_len', 'properties',)

    def __init__(
            self, *,
            properties_len: Optional[int] = None,
            properties: Optional[Sequence[int]] = None,
    ) -> None:
        self.properties_len = properties_len
        self.properties = properties

    def as_dict(self) -> Dict[str, Any]:
        return {
            'properties_len': self.properties_len,
            'properties': self.properties,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ListPropertiesReplyReply':
        return ListPropertiesReplyReply(**ListPropertiesReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ListPropertiesReplyReplyPacket.pack(**self.as_dict())


class ListPropertiesReplyReplyCType(ctypes.Structure):
    """xselinux ListProperties_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("properties_len", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


SetSelectionCreateContextRequestPacket = DataPacket((
    ('context_len', FixedDataPacketField(MARKER_UINT32)),
    ('context', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['context_len'], 0)),
))


class SetSelectionCreateContextRequest:
    OPCODE = 15

    __slots__ = ('context_len', 'context',)

    def __init__(
            self, *,
            context_len: Optional[int] = None,
            context: Optional[Sequence[int]] = None,
    ) -> None:
        self.context_len = context_len
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_len': self.context_len,
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetSelectionCreateContextRequest':
        return SetSelectionCreateContextRequest(**SetSelectionCreateContextRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetSelectionCreateContextRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetSelectionCreateContextRequest.lib = library.xselinux_setselectioncreatecontext
        SetSelectionCreateContextRequest.lib.restype = ctypes.c_uint32
        SetSelectionCreateContextRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_void_p)


class SetSelectionCreateContextRequestCType(ctypes.Structure):
    """xselinux SetSelectionCreateContext"""
    _fields_ = [
        ("context_len", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


GetSelectionCreateContextRequestCookie = NewType('GetSelectionCreateContextRequestCookie', ctypes.c_uint32)


GetSelectionCreateContextRequestPacket = DataPacket((
))


class GetSelectionCreateContextRequest:
    OPCODE = 16

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetSelectionCreateContextRequest':
        return GetSelectionCreateContextRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], GetSelectionCreateContextRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetSelectionCreateContextRequest.lib = library.xselinux_getselectioncreatecontext
        GetSelectionCreateContextRequest.lib.restype = GetSelectionCreateContextRequestCookie
        GetSelectionCreateContextRequest.lib.argstype = ()


class GetSelectionCreateContextRequestCType(ctypes.Structure):
    """xselinux GetSelectionCreateContext"""
    _fields_ = [
    ]


GetSelectionCreateContextReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('context_len', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('context', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['context_len'], 0)),
))


class GetSelectionCreateContextReplyReply:
    __slots__ = ('context_len', 'context',)

    def __init__(
            self, *,
            context_len: Optional[int] = None,
            context: Optional[Sequence[int]] = None,
    ) -> None:
        self.context_len = context_len
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_len': self.context_len,
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetSelectionCreateContextReplyReply':
        return GetSelectionCreateContextReplyReply(**GetSelectionCreateContextReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetSelectionCreateContextReplyReplyPacket.pack(**self.as_dict())


class GetSelectionCreateContextReplyReplyCType(ctypes.Structure):
    """xselinux GetSelectionCreateContext_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("context_len", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


SetSelectionUseContextRequestPacket = DataPacket((
    ('context_len', FixedDataPacketField(MARKER_UINT32)),
    ('context', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['context_len'], 0)),
))


class SetSelectionUseContextRequest:
    OPCODE = 17

    __slots__ = ('context_len', 'context',)

    def __init__(
            self, *,
            context_len: Optional[int] = None,
            context: Optional[Sequence[int]] = None,
    ) -> None:
        self.context_len = context_len
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_len': self.context_len,
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetSelectionUseContextRequest':
        return SetSelectionUseContextRequest(**SetSelectionUseContextRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetSelectionUseContextRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetSelectionUseContextRequest.lib = library.xselinux_setselectionusecontext
        SetSelectionUseContextRequest.lib.restype = ctypes.c_uint32
        SetSelectionUseContextRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_void_p)


class SetSelectionUseContextRequestCType(ctypes.Structure):
    """xselinux SetSelectionUseContext"""
    _fields_ = [
        ("context_len", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


GetSelectionUseContextRequestCookie = NewType('GetSelectionUseContextRequestCookie', ctypes.c_uint32)


GetSelectionUseContextRequestPacket = DataPacket((
))


class GetSelectionUseContextRequest:
    OPCODE = 18

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetSelectionUseContextRequest':
        return GetSelectionUseContextRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], GetSelectionUseContextRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetSelectionUseContextRequest.lib = library.xselinux_getselectionusecontext
        GetSelectionUseContextRequest.lib.restype = GetSelectionUseContextRequestCookie
        GetSelectionUseContextRequest.lib.argstype = ()


class GetSelectionUseContextRequestCType(ctypes.Structure):
    """xselinux GetSelectionUseContext"""
    _fields_ = [
    ]


GetSelectionUseContextReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('context_len', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('context', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['context_len'], 0)),
))


class GetSelectionUseContextReplyReply:
    __slots__ = ('context_len', 'context',)

    def __init__(
            self, *,
            context_len: Optional[int] = None,
            context: Optional[Sequence[int]] = None,
    ) -> None:
        self.context_len = context_len
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_len': self.context_len,
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetSelectionUseContextReplyReply':
        return GetSelectionUseContextReplyReply(**GetSelectionUseContextReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetSelectionUseContextReplyReplyPacket.pack(**self.as_dict())


class GetSelectionUseContextReplyReplyCType(ctypes.Structure):
    """xselinux GetSelectionUseContext_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("context_len", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


GetSelectionContextRequestCookie = NewType('GetSelectionContextRequestCookie', ctypes.c_uint32)


GetSelectionContextRequestPacket = DataPacket((
    ('selection', FixedDataPacketField(MARKER_UINT32)),
))


class GetSelectionContextRequest:
    OPCODE = 19

    __slots__ = ('selection',)

    def __init__(
            self, *,
            selection: Optional[int] = None,
    ) -> None:
        self.selection = selection

    def as_dict(self) -> Dict[str, Any]:
        return {
            'selection': self.selection,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetSelectionContextRequest':
        return GetSelectionContextRequest(**GetSelectionContextRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetSelectionContextRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetSelectionContextRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetSelectionContextRequest.lib = library.xselinux_getselectioncontext
        GetSelectionContextRequest.lib.restype = GetSelectionContextRequestCookie
        GetSelectionContextRequest.lib.argstype = (ctypes.c_uint32,)


class GetSelectionContextRequestCType(ctypes.Structure):
    """xselinux GetSelectionContext"""
    _fields_ = [
        ("selection", ctypes.c_uint32),
    ]


GetSelectionContextReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('context_len', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('context', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['context_len'], 0)),
))


class GetSelectionContextReplyReply:
    __slots__ = ('context_len', 'context',)

    def __init__(
            self, *,
            context_len: Optional[int] = None,
            context: Optional[Sequence[int]] = None,
    ) -> None:
        self.context_len = context_len
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_len': self.context_len,
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetSelectionContextReplyReply':
        return GetSelectionContextReplyReply(**GetSelectionContextReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetSelectionContextReplyReplyPacket.pack(**self.as_dict())


class GetSelectionContextReplyReplyCType(ctypes.Structure):
    """xselinux GetSelectionContext_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("context_len", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


GetSelectionDataContextRequestCookie = NewType('GetSelectionDataContextRequestCookie', ctypes.c_uint32)


GetSelectionDataContextRequestPacket = DataPacket((
    ('selection', FixedDataPacketField(MARKER_UINT32)),
))


class GetSelectionDataContextRequest:
    OPCODE = 20

    __slots__ = ('selection',)

    def __init__(
            self, *,
            selection: Optional[int] = None,
    ) -> None:
        self.selection = selection

    def as_dict(self) -> Dict[str, Any]:
        return {
            'selection': self.selection,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetSelectionDataContextRequest':
        return GetSelectionDataContextRequest(**GetSelectionDataContextRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetSelectionDataContextRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetSelectionDataContextRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetSelectionDataContextRequest.lib = library.xselinux_getselectiondatacontext
        GetSelectionDataContextRequest.lib.restype = GetSelectionDataContextRequestCookie
        GetSelectionDataContextRequest.lib.argstype = (ctypes.c_uint32,)


class GetSelectionDataContextRequestCType(ctypes.Structure):
    """xselinux GetSelectionDataContext"""
    _fields_ = [
        ("selection", ctypes.c_uint32),
    ]


GetSelectionDataContextReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('context_len', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('context', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['context_len'], 0)),
))


class GetSelectionDataContextReplyReply:
    __slots__ = ('context_len', 'context',)

    def __init__(
            self, *,
            context_len: Optional[int] = None,
            context: Optional[Sequence[int]] = None,
    ) -> None:
        self.context_len = context_len
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_len': self.context_len,
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetSelectionDataContextReplyReply':
        return GetSelectionDataContextReplyReply(**GetSelectionDataContextReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetSelectionDataContextReplyReplyPacket.pack(**self.as_dict())


class GetSelectionDataContextReplyReplyCType(ctypes.Structure):
    """xselinux GetSelectionDataContext_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("context_len", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


ListSelectionsRequestCookie = NewType('ListSelectionsRequestCookie', ctypes.c_uint32)


ListSelectionsRequestPacket = DataPacket((
))


class ListSelectionsRequest:
    OPCODE = 21

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ListSelectionsRequest':
        return ListSelectionsRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], ListSelectionsRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ListSelectionsRequest.lib = library.xselinux_listselections
        ListSelectionsRequest.lib.restype = ListSelectionsRequestCookie
        ListSelectionsRequest.lib.argstype = ()


class ListSelectionsRequestCType(ctypes.Structure):
    """xselinux ListSelections"""
    _fields_ = [
    ]


ListSelectionsReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('selections_len', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('selections', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['selections_len'], 0)),
))


class ListSelectionsReplyReply:
    __slots__ = ('selections_len', 'selections',)

    def __init__(
            self, *,
            selections_len: Optional[int] = None,
            selections: Optional[Sequence[int]] = None,
    ) -> None:
        self.selections_len = selections_len
        self.selections = selections

    def as_dict(self) -> Dict[str, Any]:
        return {
            'selections_len': self.selections_len,
            'selections': self.selections,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ListSelectionsReplyReply':
        return ListSelectionsReplyReply(**ListSelectionsReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ListSelectionsReplyReplyPacket.pack(**self.as_dict())


class ListSelectionsReplyReplyCType(ctypes.Structure):
    """xselinux ListSelections_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("selections_len", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


GetClientContextRequestCookie = NewType('GetClientContextRequestCookie', ctypes.c_uint32)


GetClientContextRequestPacket = DataPacket((
    ('resource', FixedDataPacketField(MARKER_UINT32)),
))


class GetClientContextRequest:
    OPCODE = 22

    __slots__ = ('resource',)

    def __init__(
            self, *,
            resource: Optional[int] = None,
    ) -> None:
        self.resource = resource

    def as_dict(self) -> Dict[str, Any]:
        return {
            'resource': self.resource,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetClientContextRequest':
        return GetClientContextRequest(**GetClientContextRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetClientContextRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetClientContextRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetClientContextRequest.lib = library.xselinux_getclientcontext
        GetClientContextRequest.lib.restype = GetClientContextRequestCookie
        GetClientContextRequest.lib.argstype = (ctypes.c_uint32,)


class GetClientContextRequestCType(ctypes.Structure):
    """xselinux GetClientContext"""
    _fields_ = [
        ("resource", ctypes.c_uint32),
    ]


GetClientContextReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('context_len', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('context', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['context_len'], 0)),
))


class GetClientContextReplyReply:
    __slots__ = ('context_len', 'context',)

    def __init__(
            self, *,
            context_len: Optional[int] = None,
            context: Optional[Sequence[int]] = None,
    ) -> None:
        self.context_len = context_len
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_len': self.context_len,
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetClientContextReplyReply':
        return GetClientContextReplyReply(**GetClientContextReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetClientContextReplyReplyPacket.pack(**self.as_dict())


class GetClientContextReplyReplyCType(ctypes.Structure):
    """xselinux GetClientContext_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("context_len", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


# ------------------------------------------------------------------
# Unions

