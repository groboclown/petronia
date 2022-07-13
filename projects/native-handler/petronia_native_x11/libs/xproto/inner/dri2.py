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

AttachmentType = NewType('AttachmentType', int)


class AttachmentValues:
    BUFFER_FRONT_LEFT = AttachmentType(0)
    BUFFER_BACK_LEFT = AttachmentType(1)
    BUFFER_FRONT_RIGHT = AttachmentType(2)
    BUFFER_BACK_RIGHT = AttachmentType(3)
    BUFFER_DEPTH = AttachmentType(4)
    BUFFER_STENCIL = AttachmentType(5)
    BUFFER_ACCUM = AttachmentType(6)
    BUFFER_FAKE_FRONT_LEFT = AttachmentType(7)
    BUFFER_FAKE_FRONT_RIGHT = AttachmentType(8)
    BUFFER_DEPTH_STENCIL = AttachmentType(9)
    BUFFER_HIZ = AttachmentType(10)


DriverTypeType = NewType('DriverTypeType', int)


class DriverTypeValues:
    DRI = DriverTypeType(0)
    VDPAU = DriverTypeType(1)


EventTypeType = NewType('EventTypeType', int)


class EventTypeValues:
    EXCHANGE_COMPLETE = EventTypeType(1)
    BLIT_COMPLETE = EventTypeType(2)
    FLIP_COMPLETE = EventTypeType(3)


# ------------------------------------------------------------------
# Aliases



# ------------------------------------------------------------------
# Structures, Events, Requests, Replies


Dri2BufferStructPacket = DataPacket((
    ('attachment', FixedDataPacketField(MARKER_UINT32)),
    ('name', FixedDataPacketField(MARKER_UINT32)),
    ('pitch', FixedDataPacketField(MARKER_UINT32)),
    ('cpp', FixedDataPacketField(MARKER_UINT32)),
    ('flags', FixedDataPacketField(MARKER_UINT32)),
))


class Dri2BufferStruct:
    __slots__ = ('attachment', 'name', 'pitch', 'cpp', 'flags',)

    def __init__(
            self, *,
            attachment: Optional[int] = None,
            name: Optional[int] = None,
            pitch: Optional[int] = None,
            cpp: Optional[int] = None,
            flags: Optional[int] = None,
    ) -> None:
        self.attachment = attachment
        self.name = name
        self.pitch = pitch
        self.cpp = cpp
        self.flags = flags

    def as_dict(self) -> Dict[str, Any]:
        return {
            'attachment': self.attachment,
            'name': self.name,
            'pitch': self.pitch,
            'cpp': self.cpp,
            'flags': self.flags,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'Dri2BufferStruct':
        return Dri2BufferStruct(**Dri2BufferStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return Dri2BufferStructPacket.pack(**self.as_dict())


class Dri2BufferStructCType(ctypes.Structure):
    """dri2 DRI2Buffer"""
    _fields_ = [
        ("attachment", ctypes.c_uint32),
        ("name", ctypes.c_uint32),
        ("pitch", ctypes.c_uint32),
        ("cpp", ctypes.c_uint32),
        ("flags", ctypes.c_uint32),
    ]


AttachFormatStructPacket = DataPacket((
    ('attachment', FixedDataPacketField(MARKER_UINT32)),
    ('format', FixedDataPacketField(MARKER_UINT32)),
))


class AttachFormatStruct:
    __slots__ = ('attachment', 'format',)

    def __init__(
            self, *,
            attachment: Optional[int] = None,
            format: Optional[int] = None,
    ) -> None:
        self.attachment = attachment
        self.format = format

    def as_dict(self) -> Dict[str, Any]:
        return {
            'attachment': self.attachment,
            'format': self.format,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'AttachFormatStruct':
        return AttachFormatStruct(**AttachFormatStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return AttachFormatStructPacket.pack(**self.as_dict())


class AttachFormatStructCType(ctypes.Structure):
    """dri2 AttachFormat"""
    _fields_ = [
        ("attachment", ctypes.c_uint32),
        ("format", ctypes.c_uint32),
    ]


QueryVersionRequestCookie = NewType('QueryVersionRequestCookie', ctypes.c_uint32)


QueryVersionRequestPacket = DataPacket((
    ('major_version', FixedDataPacketField(MARKER_UINT32)),
    ('minor_version', FixedDataPacketField(MARKER_UINT32)),
))


class QueryVersionRequest:
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
    def from_data(inp: BinaryIO) -> 'QueryVersionRequest':
        return QueryVersionRequest(**QueryVersionRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryVersionRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], QueryVersionRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryVersionRequest.lib = library.dri2_queryversion
        QueryVersionRequest.lib.restype = QueryVersionRequestCookie
        QueryVersionRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class QueryVersionRequestCType(ctypes.Structure):
    """dri2 QueryVersion"""
    _fields_ = [
        ("major_version", ctypes.c_uint32),
        ("minor_version", ctypes.c_uint32),
    ]


QueryVersionReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('major_version', FixedDataPacketField(MARKER_UINT32)),
    ('minor_version', FixedDataPacketField(MARKER_UINT32)),
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
    """dri2 QueryVersion_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("major_version", ctypes.c_uint32),
        ("minor_version", ctypes.c_uint32),
    ]


ConnectRequestCookie = NewType('ConnectRequestCookie', ctypes.c_uint32)


ConnectRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('driver_type', FixedDataPacketField(MARKER_UINT32)),
))


class ConnectRequest:
    OPCODE = 1

    __slots__ = ('window', 'driver_type',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            driver_type: Optional[int] = None,
    ) -> None:
        self.window = window
        self.driver_type = driver_type

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'driver_type': self.driver_type,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ConnectRequest':
        return ConnectRequest(**ConnectRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ConnectRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ConnectRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ConnectRequest.lib = library.dri2_connect
        ConnectRequest.lib.restype = ConnectRequestCookie
        ConnectRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class ConnectRequestCType(ctypes.Structure):
    """dri2 Connect"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("driver_type", ctypes.c_uint32),
    ]


ConnectReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('driver_name_length', FixedDataPacketField(MARKER_UINT32)),
    ('device_name_length', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(16)),
    ('driver_name', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['driver_name_length'], 0)),
    ('alignment_pad', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: (((d['driver_name_length']) + (3)) & (~(3))) - (d['driver_name_length']), 0)),
    ('device_name', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['device_name_length'], 0)),
))


class ConnectReplyReply:
    __slots__ = ('driver_name_length', 'device_name_length', 'driver_name', 'alignment_pad', 'device_name',)

    def __init__(
            self, *,
            driver_name_length: Optional[int] = None,
            device_name_length: Optional[int] = None,
            driver_name: Optional[Sequence[int]] = None,
            alignment_pad: Optional[Sequence[None]] = None,
            device_name: Optional[Sequence[int]] = None,
    ) -> None:
        self.driver_name_length = driver_name_length
        self.device_name_length = device_name_length
        self.driver_name = driver_name
        self.alignment_pad = alignment_pad
        self.device_name = device_name

    def as_dict(self) -> Dict[str, Any]:
        return {
            'driver_name_length': self.driver_name_length,
            'device_name_length': self.device_name_length,
            'driver_name': self.driver_name,
            'alignment_pad': self.alignment_pad,
            'device_name': self.device_name,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ConnectReplyReply':
        return ConnectReplyReply(**ConnectReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ConnectReplyReplyPacket.pack(**self.as_dict())


class ConnectReplyReplyCType(ctypes.Structure):
    """dri2 Connect_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("driver_name_length", ctypes.c_uint32),
        ("device_name_length", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 16),
        ("var_data", ctypes.c_void_p),
    ]


AuthenticateRequestCookie = NewType('AuthenticateRequestCookie', ctypes.c_uint32)


AuthenticateRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('magic', FixedDataPacketField(MARKER_UINT32)),
))


class AuthenticateRequest:
    OPCODE = 2

    __slots__ = ('window', 'magic',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            magic: Optional[int] = None,
    ) -> None:
        self.window = window
        self.magic = magic

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'magic': self.magic,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'AuthenticateRequest':
        return AuthenticateRequest(**AuthenticateRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return AuthenticateRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], AuthenticateRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        AuthenticateRequest.lib = library.dri2_authenticate
        AuthenticateRequest.lib.restype = AuthenticateRequestCookie
        AuthenticateRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class AuthenticateRequestCType(ctypes.Structure):
    """dri2 Authenticate"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("magic", ctypes.c_uint32),
    ]


AuthenticateReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('authenticated', FixedDataPacketField(MARKER_UINT32)),
))


class AuthenticateReplyReply:
    __slots__ = ('authenticated',)

    def __init__(
            self, *,
            authenticated: Optional[int] = None,
    ) -> None:
        self.authenticated = authenticated

    def as_dict(self) -> Dict[str, Any]:
        return {
            'authenticated': self.authenticated,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'AuthenticateReplyReply':
        return AuthenticateReplyReply(**AuthenticateReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return AuthenticateReplyReplyPacket.pack(**self.as_dict())


class AuthenticateReplyReplyCType(ctypes.Structure):
    """dri2 Authenticate_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("authenticated", ctypes.c_uint32),
    ]


CreateDrawableRequestPacket = DataPacket((
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
))


class CreateDrawableRequest:
    OPCODE = 3

    __slots__ = ('drawable',)

    def __init__(
            self, *,
            drawable: Optional[int] = None,
    ) -> None:
        self.drawable = drawable

    def as_dict(self) -> Dict[str, Any]:
        return {
            'drawable': self.drawable,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateDrawableRequest':
        return CreateDrawableRequest(**CreateDrawableRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateDrawableRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateDrawableRequest.lib = library.dri2_createdrawable
        CreateDrawableRequest.lib.restype = ctypes.c_uint32
        CreateDrawableRequest.lib.argstype = (ctypes.c_uint32,)


class CreateDrawableRequestCType(ctypes.Structure):
    """dri2 CreateDrawable"""
    _fields_ = [
        ("drawable", ctypes.c_uint32),
    ]


DestroyDrawableRequestPacket = DataPacket((
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
))


class DestroyDrawableRequest:
    OPCODE = 4

    __slots__ = ('drawable',)

    def __init__(
            self, *,
            drawable: Optional[int] = None,
    ) -> None:
        self.drawable = drawable

    def as_dict(self) -> Dict[str, Any]:
        return {
            'drawable': self.drawable,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DestroyDrawableRequest':
        return DestroyDrawableRequest(**DestroyDrawableRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DestroyDrawableRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        DestroyDrawableRequest.lib = library.dri2_destroydrawable
        DestroyDrawableRequest.lib.restype = ctypes.c_uint32
        DestroyDrawableRequest.lib.argstype = (ctypes.c_uint32,)


class DestroyDrawableRequestCType(ctypes.Structure):
    """dri2 DestroyDrawable"""
    _fields_ = [
        ("drawable", ctypes.c_uint32),
    ]


GetBuffersRequestCookie = NewType('GetBuffersRequestCookie', ctypes.c_uint32)


GetBuffersRequestPacket = DataPacket((
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('count', FixedDataPacketField(MARKER_UINT32)),
    ('attachments', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 1, 0)),
))


class GetBuffersRequest:
    OPCODE = 5

    __slots__ = ('drawable', 'count', 'attachments',)

    def __init__(
            self, *,
            drawable: Optional[int] = None,
            count: Optional[int] = None,
            attachments: Optional[Sequence[int]] = None,
    ) -> None:
        self.drawable = drawable
        self.count = count
        self.attachments = attachments

    def as_dict(self) -> Dict[str, Any]:
        return {
            'drawable': self.drawable,
            'count': self.count,
            'attachments': self.attachments,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetBuffersRequest':
        return GetBuffersRequest(**GetBuffersRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetBuffersRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int]], GetBuffersRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetBuffersRequest.lib = library.dri2_getbuffers
        GetBuffersRequest.lib.restype = GetBuffersRequestCookie
        GetBuffersRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)


class GetBuffersRequestCType(ctypes.Structure):
    """dri2 GetBuffers"""
    _fields_ = [
        ("drawable", ctypes.c_uint32),
        ("count", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


GetBuffersReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('width', FixedDataPacketField(MARKER_UINT32)),
    ('height', FixedDataPacketField(MARKER_UINT32)),
    ('count', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(12)),
    ('buffers', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['count'], 0)),
))


class GetBuffersReplyReply:
    __slots__ = ('width', 'height', 'count', 'buffers',)

    def __init__(
            self, *,
            width: Optional[int] = None,
            height: Optional[int] = None,
            count: Optional[int] = None,
            buffers: Optional[Sequence[int]] = None,
    ) -> None:
        self.width = width
        self.height = height
        self.count = count
        self.buffers = buffers

    def as_dict(self) -> Dict[str, Any]:
        return {
            'width': self.width,
            'height': self.height,
            'count': self.count,
            'buffers': self.buffers,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetBuffersReplyReply':
        return GetBuffersReplyReply(**GetBuffersReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetBuffersReplyReplyPacket.pack(**self.as_dict())


class GetBuffersReplyReplyCType(ctypes.Structure):
    """dri2 GetBuffers_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("width", ctypes.c_uint32),
        ("height", ctypes.c_uint32),
        ("count", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


CopyRegionRequestCookie = NewType('CopyRegionRequestCookie', ctypes.c_uint32)


CopyRegionRequestPacket = DataPacket((
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('region', FixedDataPacketField(MARKER_UINT32)),
    ('dest', FixedDataPacketField(MARKER_UINT32)),
    ('src', FixedDataPacketField(MARKER_UINT32)),
))


class CopyRegionRequest:
    OPCODE = 6

    __slots__ = ('drawable', 'region', 'dest', 'src',)

    def __init__(
            self, *,
            drawable: Optional[int] = None,
            region: Optional[int] = None,
            dest: Optional[int] = None,
            src: Optional[int] = None,
    ) -> None:
        self.drawable = drawable
        self.region = region
        self.dest = dest
        self.src = src

    def as_dict(self) -> Dict[str, Any]:
        return {
            'drawable': self.drawable,
            'region': self.region,
            'dest': self.dest,
            'src': self.src,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CopyRegionRequest':
        return CopyRegionRequest(**CopyRegionRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CopyRegionRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int], CopyRegionRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CopyRegionRequest.lib = library.dri2_copyregion
        CopyRegionRequest.lib.restype = CopyRegionRequestCookie
        CopyRegionRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class CopyRegionRequestCType(ctypes.Structure):
    """dri2 CopyRegion"""
    _fields_ = [
        ("drawable", ctypes.c_uint32),
        ("region", ctypes.c_uint32),
        ("dest", ctypes.c_uint32),
        ("src", ctypes.c_uint32),
    ]


CopyRegionReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
))


class CopyRegionReplyReply:
    __slots__ = (,)

    def __init__(
            self, *,
    ) -> None:

    def as_dict(self) -> Dict[str, Any]:
        return {
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CopyRegionReplyReply':
        return CopyRegionReplyReply(**CopyRegionReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CopyRegionReplyReplyPacket.pack(**self.as_dict())


class CopyRegionReplyReplyCType(ctypes.Structure):
    """dri2 CopyRegion_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
    ]


GetBuffersWithFormatRequestCookie = NewType('GetBuffersWithFormatRequestCookie', ctypes.c_uint32)


GetBuffersWithFormatRequestPacket = DataPacket((
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('count', FixedDataPacketField(MARKER_UINT32)),
    ('attachments', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 1, 0)),
))


class GetBuffersWithFormatRequest:
    OPCODE = 7

    __slots__ = ('drawable', 'count', 'attachments',)

    def __init__(
            self, *,
            drawable: Optional[int] = None,
            count: Optional[int] = None,
            attachments: Optional[Sequence[int]] = None,
    ) -> None:
        self.drawable = drawable
        self.count = count
        self.attachments = attachments

    def as_dict(self) -> Dict[str, Any]:
        return {
            'drawable': self.drawable,
            'count': self.count,
            'attachments': self.attachments,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetBuffersWithFormatRequest':
        return GetBuffersWithFormatRequest(**GetBuffersWithFormatRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetBuffersWithFormatRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int]], GetBuffersWithFormatRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetBuffersWithFormatRequest.lib = library.dri2_getbufferswithformat
        GetBuffersWithFormatRequest.lib.restype = GetBuffersWithFormatRequestCookie
        GetBuffersWithFormatRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)


class GetBuffersWithFormatRequestCType(ctypes.Structure):
    """dri2 GetBuffersWithFormat"""
    _fields_ = [
        ("drawable", ctypes.c_uint32),
        ("count", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


GetBuffersWithFormatReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('width', FixedDataPacketField(MARKER_UINT32)),
    ('height', FixedDataPacketField(MARKER_UINT32)),
    ('count', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(12)),
    ('buffers', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['count'], 0)),
))


class GetBuffersWithFormatReplyReply:
    __slots__ = ('width', 'height', 'count', 'buffers',)

    def __init__(
            self, *,
            width: Optional[int] = None,
            height: Optional[int] = None,
            count: Optional[int] = None,
            buffers: Optional[Sequence[int]] = None,
    ) -> None:
        self.width = width
        self.height = height
        self.count = count
        self.buffers = buffers

    def as_dict(self) -> Dict[str, Any]:
        return {
            'width': self.width,
            'height': self.height,
            'count': self.count,
            'buffers': self.buffers,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetBuffersWithFormatReplyReply':
        return GetBuffersWithFormatReplyReply(**GetBuffersWithFormatReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetBuffersWithFormatReplyReplyPacket.pack(**self.as_dict())


class GetBuffersWithFormatReplyReplyCType(ctypes.Structure):
    """dri2 GetBuffersWithFormat_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("width", ctypes.c_uint32),
        ("height", ctypes.c_uint32),
        ("count", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


SwapBuffersRequestCookie = NewType('SwapBuffersRequestCookie', ctypes.c_uint32)


SwapBuffersRequestPacket = DataPacket((
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('target_msc_hi', FixedDataPacketField(MARKER_UINT32)),
    ('target_msc_lo', FixedDataPacketField(MARKER_UINT32)),
    ('divisor_hi', FixedDataPacketField(MARKER_UINT32)),
    ('divisor_lo', FixedDataPacketField(MARKER_UINT32)),
    ('remainder_hi', FixedDataPacketField(MARKER_UINT32)),
    ('remainder_lo', FixedDataPacketField(MARKER_UINT32)),
))


class SwapBuffersRequest:
    OPCODE = 8

    __slots__ = ('drawable', 'target_msc_hi', 'target_msc_lo', 'divisor_hi', 'divisor_lo', 'remainder_hi', 'remainder_lo',)

    def __init__(
            self, *,
            drawable: Optional[int] = None,
            target_msc_hi: Optional[int] = None,
            target_msc_lo: Optional[int] = None,
            divisor_hi: Optional[int] = None,
            divisor_lo: Optional[int] = None,
            remainder_hi: Optional[int] = None,
            remainder_lo: Optional[int] = None,
    ) -> None:
        self.drawable = drawable
        self.target_msc_hi = target_msc_hi
        self.target_msc_lo = target_msc_lo
        self.divisor_hi = divisor_hi
        self.divisor_lo = divisor_lo
        self.remainder_hi = remainder_hi
        self.remainder_lo = remainder_lo

    def as_dict(self) -> Dict[str, Any]:
        return {
            'drawable': self.drawable,
            'target_msc_hi': self.target_msc_hi,
            'target_msc_lo': self.target_msc_lo,
            'divisor_hi': self.divisor_hi,
            'divisor_lo': self.divisor_lo,
            'remainder_hi': self.remainder_hi,
            'remainder_lo': self.remainder_lo,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SwapBuffersRequest':
        return SwapBuffersRequest(**SwapBuffersRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SwapBuffersRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int], SwapBuffersRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SwapBuffersRequest.lib = library.dri2_swapbuffers
        SwapBuffersRequest.lib.restype = SwapBuffersRequestCookie
        SwapBuffersRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class SwapBuffersRequestCType(ctypes.Structure):
    """dri2 SwapBuffers"""
    _fields_ = [
        ("drawable", ctypes.c_uint32),
        ("target_msc_hi", ctypes.c_uint32),
        ("target_msc_lo", ctypes.c_uint32),
        ("divisor_hi", ctypes.c_uint32),
        ("divisor_lo", ctypes.c_uint32),
        ("remainder_hi", ctypes.c_uint32),
        ("remainder_lo", ctypes.c_uint32),
    ]


SwapBuffersReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('swap_hi', FixedDataPacketField(MARKER_UINT32)),
    ('swap_lo', FixedDataPacketField(MARKER_UINT32)),
))


class SwapBuffersReplyReply:
    __slots__ = ('swap_hi', 'swap_lo',)

    def __init__(
            self, *,
            swap_hi: Optional[int] = None,
            swap_lo: Optional[int] = None,
    ) -> None:
        self.swap_hi = swap_hi
        self.swap_lo = swap_lo

    def as_dict(self) -> Dict[str, Any]:
        return {
            'swap_hi': self.swap_hi,
            'swap_lo': self.swap_lo,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SwapBuffersReplyReply':
        return SwapBuffersReplyReply(**SwapBuffersReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SwapBuffersReplyReplyPacket.pack(**self.as_dict())


class SwapBuffersReplyReplyCType(ctypes.Structure):
    """dri2 SwapBuffers_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("swap_hi", ctypes.c_uint32),
        ("swap_lo", ctypes.c_uint32),
    ]


GetMscRequestCookie = NewType('GetMscRequestCookie', ctypes.c_uint32)


GetMscRequestPacket = DataPacket((
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
))


class GetMscRequest:
    OPCODE = 9

    __slots__ = ('drawable',)

    def __init__(
            self, *,
            drawable: Optional[int] = None,
    ) -> None:
        self.drawable = drawable

    def as_dict(self) -> Dict[str, Any]:
        return {
            'drawable': self.drawable,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetMscRequest':
        return GetMscRequest(**GetMscRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetMscRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetMscRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetMscRequest.lib = library.dri2_getmsc
        GetMscRequest.lib.restype = GetMscRequestCookie
        GetMscRequest.lib.argstype = (ctypes.c_uint32,)


class GetMscRequestCType(ctypes.Structure):
    """dri2 GetMSC"""
    _fields_ = [
        ("drawable", ctypes.c_uint32),
    ]


GetMscReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('ust_hi', FixedDataPacketField(MARKER_UINT32)),
    ('ust_lo', FixedDataPacketField(MARKER_UINT32)),
    ('msc_hi', FixedDataPacketField(MARKER_UINT32)),
    ('msc_lo', FixedDataPacketField(MARKER_UINT32)),
    ('sbc_hi', FixedDataPacketField(MARKER_UINT32)),
    ('sbc_lo', FixedDataPacketField(MARKER_UINT32)),
))


class GetMscReplyReply:
    __slots__ = ('ust_hi', 'ust_lo', 'msc_hi', 'msc_lo', 'sbc_hi', 'sbc_lo',)

    def __init__(
            self, *,
            ust_hi: Optional[int] = None,
            ust_lo: Optional[int] = None,
            msc_hi: Optional[int] = None,
            msc_lo: Optional[int] = None,
            sbc_hi: Optional[int] = None,
            sbc_lo: Optional[int] = None,
    ) -> None:
        self.ust_hi = ust_hi
        self.ust_lo = ust_lo
        self.msc_hi = msc_hi
        self.msc_lo = msc_lo
        self.sbc_hi = sbc_hi
        self.sbc_lo = sbc_lo

    def as_dict(self) -> Dict[str, Any]:
        return {
            'ust_hi': self.ust_hi,
            'ust_lo': self.ust_lo,
            'msc_hi': self.msc_hi,
            'msc_lo': self.msc_lo,
            'sbc_hi': self.sbc_hi,
            'sbc_lo': self.sbc_lo,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetMscReplyReply':
        return GetMscReplyReply(**GetMscReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetMscReplyReplyPacket.pack(**self.as_dict())


class GetMscReplyReplyCType(ctypes.Structure):
    """dri2 GetMSC_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("ust_hi", ctypes.c_uint32),
        ("ust_lo", ctypes.c_uint32),
        ("msc_hi", ctypes.c_uint32),
        ("msc_lo", ctypes.c_uint32),
        ("sbc_hi", ctypes.c_uint32),
        ("sbc_lo", ctypes.c_uint32),
    ]


WaitMscRequestCookie = NewType('WaitMscRequestCookie', ctypes.c_uint32)


WaitMscRequestPacket = DataPacket((
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('target_msc_hi', FixedDataPacketField(MARKER_UINT32)),
    ('target_msc_lo', FixedDataPacketField(MARKER_UINT32)),
    ('divisor_hi', FixedDataPacketField(MARKER_UINT32)),
    ('divisor_lo', FixedDataPacketField(MARKER_UINT32)),
    ('remainder_hi', FixedDataPacketField(MARKER_UINT32)),
    ('remainder_lo', FixedDataPacketField(MARKER_UINT32)),
))


class WaitMscRequest:
    OPCODE = 10

    __slots__ = ('drawable', 'target_msc_hi', 'target_msc_lo', 'divisor_hi', 'divisor_lo', 'remainder_hi', 'remainder_lo',)

    def __init__(
            self, *,
            drawable: Optional[int] = None,
            target_msc_hi: Optional[int] = None,
            target_msc_lo: Optional[int] = None,
            divisor_hi: Optional[int] = None,
            divisor_lo: Optional[int] = None,
            remainder_hi: Optional[int] = None,
            remainder_lo: Optional[int] = None,
    ) -> None:
        self.drawable = drawable
        self.target_msc_hi = target_msc_hi
        self.target_msc_lo = target_msc_lo
        self.divisor_hi = divisor_hi
        self.divisor_lo = divisor_lo
        self.remainder_hi = remainder_hi
        self.remainder_lo = remainder_lo

    def as_dict(self) -> Dict[str, Any]:
        return {
            'drawable': self.drawable,
            'target_msc_hi': self.target_msc_hi,
            'target_msc_lo': self.target_msc_lo,
            'divisor_hi': self.divisor_hi,
            'divisor_lo': self.divisor_lo,
            'remainder_hi': self.remainder_hi,
            'remainder_lo': self.remainder_lo,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'WaitMscRequest':
        return WaitMscRequest(**WaitMscRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return WaitMscRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int], WaitMscRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        WaitMscRequest.lib = library.dri2_waitmsc
        WaitMscRequest.lib.restype = WaitMscRequestCookie
        WaitMscRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class WaitMscRequestCType(ctypes.Structure):
    """dri2 WaitMSC"""
    _fields_ = [
        ("drawable", ctypes.c_uint32),
        ("target_msc_hi", ctypes.c_uint32),
        ("target_msc_lo", ctypes.c_uint32),
        ("divisor_hi", ctypes.c_uint32),
        ("divisor_lo", ctypes.c_uint32),
        ("remainder_hi", ctypes.c_uint32),
        ("remainder_lo", ctypes.c_uint32),
    ]


WaitMscReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('ust_hi', FixedDataPacketField(MARKER_UINT32)),
    ('ust_lo', FixedDataPacketField(MARKER_UINT32)),
    ('msc_hi', FixedDataPacketField(MARKER_UINT32)),
    ('msc_lo', FixedDataPacketField(MARKER_UINT32)),
    ('sbc_hi', FixedDataPacketField(MARKER_UINT32)),
    ('sbc_lo', FixedDataPacketField(MARKER_UINT32)),
))


class WaitMscReplyReply:
    __slots__ = ('ust_hi', 'ust_lo', 'msc_hi', 'msc_lo', 'sbc_hi', 'sbc_lo',)

    def __init__(
            self, *,
            ust_hi: Optional[int] = None,
            ust_lo: Optional[int] = None,
            msc_hi: Optional[int] = None,
            msc_lo: Optional[int] = None,
            sbc_hi: Optional[int] = None,
            sbc_lo: Optional[int] = None,
    ) -> None:
        self.ust_hi = ust_hi
        self.ust_lo = ust_lo
        self.msc_hi = msc_hi
        self.msc_lo = msc_lo
        self.sbc_hi = sbc_hi
        self.sbc_lo = sbc_lo

    def as_dict(self) -> Dict[str, Any]:
        return {
            'ust_hi': self.ust_hi,
            'ust_lo': self.ust_lo,
            'msc_hi': self.msc_hi,
            'msc_lo': self.msc_lo,
            'sbc_hi': self.sbc_hi,
            'sbc_lo': self.sbc_lo,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'WaitMscReplyReply':
        return WaitMscReplyReply(**WaitMscReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return WaitMscReplyReplyPacket.pack(**self.as_dict())


class WaitMscReplyReplyCType(ctypes.Structure):
    """dri2 WaitMSC_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("ust_hi", ctypes.c_uint32),
        ("ust_lo", ctypes.c_uint32),
        ("msc_hi", ctypes.c_uint32),
        ("msc_lo", ctypes.c_uint32),
        ("sbc_hi", ctypes.c_uint32),
        ("sbc_lo", ctypes.c_uint32),
    ]


WaitSbcRequestCookie = NewType('WaitSbcRequestCookie', ctypes.c_uint32)


WaitSbcRequestPacket = DataPacket((
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('target_sbc_hi', FixedDataPacketField(MARKER_UINT32)),
    ('target_sbc_lo', FixedDataPacketField(MARKER_UINT32)),
))


class WaitSbcRequest:
    OPCODE = 11

    __slots__ = ('drawable', 'target_sbc_hi', 'target_sbc_lo',)

    def __init__(
            self, *,
            drawable: Optional[int] = None,
            target_sbc_hi: Optional[int] = None,
            target_sbc_lo: Optional[int] = None,
    ) -> None:
        self.drawable = drawable
        self.target_sbc_hi = target_sbc_hi
        self.target_sbc_lo = target_sbc_lo

    def as_dict(self) -> Dict[str, Any]:
        return {
            'drawable': self.drawable,
            'target_sbc_hi': self.target_sbc_hi,
            'target_sbc_lo': self.target_sbc_lo,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'WaitSbcRequest':
        return WaitSbcRequest(**WaitSbcRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return WaitSbcRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], WaitSbcRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        WaitSbcRequest.lib = library.dri2_waitsbc
        WaitSbcRequest.lib.restype = WaitSbcRequestCookie
        WaitSbcRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class WaitSbcRequestCType(ctypes.Structure):
    """dri2 WaitSBC"""
    _fields_ = [
        ("drawable", ctypes.c_uint32),
        ("target_sbc_hi", ctypes.c_uint32),
        ("target_sbc_lo", ctypes.c_uint32),
    ]


WaitSbcReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('ust_hi', FixedDataPacketField(MARKER_UINT32)),
    ('ust_lo', FixedDataPacketField(MARKER_UINT32)),
    ('msc_hi', FixedDataPacketField(MARKER_UINT32)),
    ('msc_lo', FixedDataPacketField(MARKER_UINT32)),
    ('sbc_hi', FixedDataPacketField(MARKER_UINT32)),
    ('sbc_lo', FixedDataPacketField(MARKER_UINT32)),
))


class WaitSbcReplyReply:
    __slots__ = ('ust_hi', 'ust_lo', 'msc_hi', 'msc_lo', 'sbc_hi', 'sbc_lo',)

    def __init__(
            self, *,
            ust_hi: Optional[int] = None,
            ust_lo: Optional[int] = None,
            msc_hi: Optional[int] = None,
            msc_lo: Optional[int] = None,
            sbc_hi: Optional[int] = None,
            sbc_lo: Optional[int] = None,
    ) -> None:
        self.ust_hi = ust_hi
        self.ust_lo = ust_lo
        self.msc_hi = msc_hi
        self.msc_lo = msc_lo
        self.sbc_hi = sbc_hi
        self.sbc_lo = sbc_lo

    def as_dict(self) -> Dict[str, Any]:
        return {
            'ust_hi': self.ust_hi,
            'ust_lo': self.ust_lo,
            'msc_hi': self.msc_hi,
            'msc_lo': self.msc_lo,
            'sbc_hi': self.sbc_hi,
            'sbc_lo': self.sbc_lo,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'WaitSbcReplyReply':
        return WaitSbcReplyReply(**WaitSbcReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return WaitSbcReplyReplyPacket.pack(**self.as_dict())


class WaitSbcReplyReplyCType(ctypes.Structure):
    """dri2 WaitSBC_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("ust_hi", ctypes.c_uint32),
        ("ust_lo", ctypes.c_uint32),
        ("msc_hi", ctypes.c_uint32),
        ("msc_lo", ctypes.c_uint32),
        ("sbc_hi", ctypes.c_uint32),
        ("sbc_lo", ctypes.c_uint32),
    ]


SwapIntervalRequestPacket = DataPacket((
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('interval', FixedDataPacketField(MARKER_UINT32)),
))


class SwapIntervalRequest:
    OPCODE = 12

    __slots__ = ('drawable', 'interval',)

    def __init__(
            self, *,
            drawable: Optional[int] = None,
            interval: Optional[int] = None,
    ) -> None:
        self.drawable = drawable
        self.interval = interval

    def as_dict(self) -> Dict[str, Any]:
        return {
            'drawable': self.drawable,
            'interval': self.interval,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SwapIntervalRequest':
        return SwapIntervalRequest(**SwapIntervalRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SwapIntervalRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SwapIntervalRequest.lib = library.dri2_swapinterval
        SwapIntervalRequest.lib.restype = ctypes.c_uint32
        SwapIntervalRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class SwapIntervalRequestCType(ctypes.Structure):
    """dri2 SwapInterval"""
    _fields_ = [
        ("drawable", ctypes.c_uint32),
        ("interval", ctypes.c_uint32),
    ]


GetParamRequestCookie = NewType('GetParamRequestCookie', ctypes.c_uint32)


GetParamRequestPacket = DataPacket((
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('param', FixedDataPacketField(MARKER_UINT32)),
))


class GetParamRequest:
    OPCODE = 13

    __slots__ = ('drawable', 'param',)

    def __init__(
            self, *,
            drawable: Optional[int] = None,
            param: Optional[int] = None,
    ) -> None:
        self.drawable = drawable
        self.param = param

    def as_dict(self) -> Dict[str, Any]:
        return {
            'drawable': self.drawable,
            'param': self.param,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetParamRequest':
        return GetParamRequest(**GetParamRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetParamRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], GetParamRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetParamRequest.lib = library.dri2_getparam
        GetParamRequest.lib.restype = GetParamRequestCookie
        GetParamRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class GetParamRequestCType(ctypes.Structure):
    """dri2 GetParam"""
    _fields_ = [
        ("drawable", ctypes.c_uint32),
        ("param", ctypes.c_uint32),
    ]


GetParamReplyReplyPacket = DataPacket((
    ('is_param_recognized', FixedDataPacketField(MARKER_UINT8)),
    ('value_hi', FixedDataPacketField(MARKER_UINT32)),
    ('value_lo', FixedDataPacketField(MARKER_UINT32)),
))


class GetParamReplyReply:
    __slots__ = ('is_param_recognized', 'value_hi', 'value_lo',)

    def __init__(
            self, *,
            is_param_recognized: Optional[bool] = None,
            value_hi: Optional[int] = None,
            value_lo: Optional[int] = None,
    ) -> None:
        self.is_param_recognized = is_param_recognized
        self.value_hi = value_hi
        self.value_lo = value_lo

    def as_dict(self) -> Dict[str, Any]:
        return {
            'is_param_recognized': self.is_param_recognized,
            'value_hi': self.value_hi,
            'value_lo': self.value_lo,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetParamReplyReply':
        return GetParamReplyReply(**GetParamReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetParamReplyReplyPacket.pack(**self.as_dict())


class GetParamReplyReplyCType(ctypes.Structure):
    """dri2 GetParam_reply"""
    _fields_ = [
        ("is_param_recognized", ctypes.c_int8),
        ("value_hi", ctypes.c_uint32),
        ("value_lo", ctypes.c_uint32),
    ]


BufferSwapCompleteEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(1)),
    ('event_type', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(2)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('ust_hi', FixedDataPacketField(MARKER_UINT32)),
    ('ust_lo', FixedDataPacketField(MARKER_UINT32)),
    ('msc_hi', FixedDataPacketField(MARKER_UINT32)),
    ('msc_lo', FixedDataPacketField(MARKER_UINT32)),
    ('sbc', FixedDataPacketField(MARKER_UINT32)),
))


class BufferSwapCompleteEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'event_type', 'drawable', 'ust_hi', 'ust_lo', 'msc_hi', 'msc_lo', 'sbc',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            event_type: Optional[int] = None,
            drawable: Optional[int] = None,
            ust_hi: Optional[int] = None,
            ust_lo: Optional[int] = None,
            msc_hi: Optional[int] = None,
            msc_lo: Optional[int] = None,
            sbc: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.event_type = event_type
        self.drawable = drawable
        self.ust_hi = ust_hi
        self.ust_lo = ust_lo
        self.msc_hi = msc_hi
        self.msc_lo = msc_lo
        self.sbc = sbc

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'event_type': self.event_type,
            'drawable': self.drawable,
            'ust_hi': self.ust_hi,
            'ust_lo': self.ust_lo,
            'msc_hi': self.msc_hi,
            'msc_lo': self.msc_lo,
            'sbc': self.sbc,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'BufferSwapCompleteEvent':
        return BufferSwapCompleteEvent(**BufferSwapCompleteEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return BufferSwapCompleteEventPacket.pack(**self.as_dict())


class BufferSwapCompleteEventCType(ctypes.Structure):
    """dri2 BufferSwapComplete"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8),
        ("event_type", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 2),
        ("drawable", ctypes.c_uint32),
        ("ust_hi", ctypes.c_uint32),
        ("ust_lo", ctypes.c_uint32),
        ("msc_hi", ctypes.c_uint32),
        ("msc_lo", ctypes.c_uint32),
        ("sbc", ctypes.c_uint32),
    ]


InvalidateBuffersEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(1)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
))


class InvalidateBuffersEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'drawable',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            drawable: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.drawable = drawable

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'drawable': self.drawable,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'InvalidateBuffersEvent':
        return InvalidateBuffersEvent(**InvalidateBuffersEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return InvalidateBuffersEventPacket.pack(**self.as_dict())


class InvalidateBuffersEventCType(ctypes.Structure):
    """dri2 InvalidateBuffers"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8),
        ("drawable", ctypes.c_uint32),
    ]


# ------------------------------------------------------------------
# Unions

