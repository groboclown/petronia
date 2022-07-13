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


DrmClipRectStructPacket = DataPacket((
    ('x1', FixedDataPacketField(MARKER_INT16)),
    ('y1', FixedDataPacketField(MARKER_INT16)),
    ('x2', FixedDataPacketField(MARKER_INT16)),
    ('x3', FixedDataPacketField(MARKER_INT16)),
))


class DrmClipRectStruct:
    __slots__ = ('x1', 'y1', 'x2', 'x3',)

    def __init__(
            self, *,
            x1: Optional[int] = None,
            y1: Optional[int] = None,
            x2: Optional[int] = None,
            x3: Optional[int] = None,
    ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.x3 = x3

    def as_dict(self) -> Dict[str, Any]:
        return {
            'x1': self.x1,
            'y1': self.y1,
            'x2': self.x2,
            'x3': self.x3,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DrmClipRectStruct':
        return DrmClipRectStruct(**DrmClipRectStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DrmClipRectStructPacket.pack(**self.as_dict())


class DrmClipRectStructCType(ctypes.Structure):
    """xf86dri DrmClipRect"""
    _fields_ = [
        ("x1", ctypes.c_int16),
        ("y1", ctypes.c_int16),
        ("x2", ctypes.c_int16),
        ("x3", ctypes.c_int16),
    ]


QueryVersionRequestCookie = NewType('QueryVersionRequestCookie', ctypes.c_uint32)


QueryVersionRequestPacket = DataPacket((
))


class QueryVersionRequest:
    OPCODE = 0

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryVersionRequest':
        return QueryVersionRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], QueryVersionRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryVersionRequest.lib = library.xf86dri_queryversion
        QueryVersionRequest.lib.restype = QueryVersionRequestCookie
        QueryVersionRequest.lib.argstype = ()


class QueryVersionRequestCType(ctypes.Structure):
    """xf86dri QueryVersion"""
    _fields_ = [
    ]


QueryVersionReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('dri_major_version', FixedDataPacketField(MARKER_UINT16)),
    ('dri_minor_version', FixedDataPacketField(MARKER_UINT16)),
    ('dri_minor_patch', FixedDataPacketField(MARKER_UINT32)),
))


class QueryVersionReplyReply:
    __slots__ = ('dri_major_version', 'dri_minor_version', 'dri_minor_patch',)

    def __init__(
            self, *,
            dri_major_version: Optional[int] = None,
            dri_minor_version: Optional[int] = None,
            dri_minor_patch: Optional[int] = None,
    ) -> None:
        self.dri_major_version = dri_major_version
        self.dri_minor_version = dri_minor_version
        self.dri_minor_patch = dri_minor_patch

    def as_dict(self) -> Dict[str, Any]:
        return {
            'dri_major_version': self.dri_major_version,
            'dri_minor_version': self.dri_minor_version,
            'dri_minor_patch': self.dri_minor_patch,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryVersionReplyReply':
        return QueryVersionReplyReply(**QueryVersionReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryVersionReplyReplyPacket.pack(**self.as_dict())


class QueryVersionReplyReplyCType(ctypes.Structure):
    """xf86dri QueryVersion_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("dri_major_version", ctypes.c_uint16),
        ("dri_minor_version", ctypes.c_uint16),
        ("dri_minor_patch", ctypes.c_uint32),
    ]


QueryDirectRenderingCapableRequestCookie = NewType('QueryDirectRenderingCapableRequestCookie', ctypes.c_uint32)


QueryDirectRenderingCapableRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT32)),
))


class QueryDirectRenderingCapableRequest:
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
    def from_data(inp: BinaryIO) -> 'QueryDirectRenderingCapableRequest':
        return QueryDirectRenderingCapableRequest(**QueryDirectRenderingCapableRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryDirectRenderingCapableRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], QueryDirectRenderingCapableRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryDirectRenderingCapableRequest.lib = library.xf86dri_querydirectrenderingcapable
        QueryDirectRenderingCapableRequest.lib.restype = QueryDirectRenderingCapableRequestCookie
        QueryDirectRenderingCapableRequest.lib.argstype = (ctypes.c_uint32,)


class QueryDirectRenderingCapableRequestCType(ctypes.Structure):
    """xf86dri QueryDirectRenderingCapable"""
    _fields_ = [
        ("screen", ctypes.c_uint32),
    ]


QueryDirectRenderingCapableReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('is_capable', FixedDataPacketField(MARKER_UINT8)),
))


class QueryDirectRenderingCapableReplyReply:
    __slots__ = ('is_capable',)

    def __init__(
            self, *,
            is_capable: Optional[bool] = None,
    ) -> None:
        self.is_capable = is_capable

    def as_dict(self) -> Dict[str, Any]:
        return {
            'is_capable': self.is_capable,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryDirectRenderingCapableReplyReply':
        return QueryDirectRenderingCapableReplyReply(**QueryDirectRenderingCapableReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryDirectRenderingCapableReplyReplyPacket.pack(**self.as_dict())


class QueryDirectRenderingCapableReplyReplyCType(ctypes.Structure):
    """xf86dri QueryDirectRenderingCapable_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("is_capable", ctypes.c_int8),
    ]


OpenConnectionRequestCookie = NewType('OpenConnectionRequestCookie', ctypes.c_uint32)


OpenConnectionRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT32)),
))


class OpenConnectionRequest:
    OPCODE = 2

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
    def from_data(inp: BinaryIO) -> 'OpenConnectionRequest':
        return OpenConnectionRequest(**OpenConnectionRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return OpenConnectionRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], OpenConnectionRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        OpenConnectionRequest.lib = library.xf86dri_openconnection
        OpenConnectionRequest.lib.restype = OpenConnectionRequestCookie
        OpenConnectionRequest.lib.argstype = (ctypes.c_uint32,)


class OpenConnectionRequestCType(ctypes.Structure):
    """xf86dri OpenConnection"""
    _fields_ = [
        ("screen", ctypes.c_uint32),
    ]


OpenConnectionReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('sarea_handle_low', FixedDataPacketField(MARKER_UINT32)),
    ('sarea_handle_high', FixedDataPacketField(MARKER_UINT32)),
    ('bus_id_len', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(12)),
    ('bus_id', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['bus_id_len'], 0)),
))


class OpenConnectionReplyReply:
    __slots__ = ('sarea_handle_low', 'sarea_handle_high', 'bus_id_len', 'bus_id',)

    def __init__(
            self, *,
            sarea_handle_low: Optional[int] = None,
            sarea_handle_high: Optional[int] = None,
            bus_id_len: Optional[int] = None,
            bus_id: Optional[Sequence[int]] = None,
    ) -> None:
        self.sarea_handle_low = sarea_handle_low
        self.sarea_handle_high = sarea_handle_high
        self.bus_id_len = bus_id_len
        self.bus_id = bus_id

    def as_dict(self) -> Dict[str, Any]:
        return {
            'sarea_handle_low': self.sarea_handle_low,
            'sarea_handle_high': self.sarea_handle_high,
            'bus_id_len': self.bus_id_len,
            'bus_id': self.bus_id,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'OpenConnectionReplyReply':
        return OpenConnectionReplyReply(**OpenConnectionReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return OpenConnectionReplyReplyPacket.pack(**self.as_dict())


class OpenConnectionReplyReplyCType(ctypes.Structure):
    """xf86dri OpenConnection_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("sarea_handle_low", ctypes.c_uint32),
        ("sarea_handle_high", ctypes.c_uint32),
        ("bus_id_len", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


CloseConnectionRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT32)),
))


class CloseConnectionRequest:
    OPCODE = 3

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
    def from_data(inp: BinaryIO) -> 'CloseConnectionRequest':
        return CloseConnectionRequest(**CloseConnectionRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CloseConnectionRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CloseConnectionRequest.lib = library.xf86dri_closeconnection
        CloseConnectionRequest.lib.restype = ctypes.c_uint32
        CloseConnectionRequest.lib.argstype = (ctypes.c_uint32,)


class CloseConnectionRequestCType(ctypes.Structure):
    """xf86dri CloseConnection"""
    _fields_ = [
        ("screen", ctypes.c_uint32),
    ]


GetClientDriverNameRequestCookie = NewType('GetClientDriverNameRequestCookie', ctypes.c_uint32)


GetClientDriverNameRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT32)),
))


class GetClientDriverNameRequest:
    OPCODE = 4

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
    def from_data(inp: BinaryIO) -> 'GetClientDriverNameRequest':
        return GetClientDriverNameRequest(**GetClientDriverNameRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetClientDriverNameRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetClientDriverNameRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetClientDriverNameRequest.lib = library.xf86dri_getclientdrivername
        GetClientDriverNameRequest.lib.restype = GetClientDriverNameRequestCookie
        GetClientDriverNameRequest.lib.argstype = (ctypes.c_uint32,)


class GetClientDriverNameRequestCType(ctypes.Structure):
    """xf86dri GetClientDriverName"""
    _fields_ = [
        ("screen", ctypes.c_uint32),
    ]


GetClientDriverNameReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('client_driver_major_version', FixedDataPacketField(MARKER_UINT32)),
    ('client_driver_minor_version', FixedDataPacketField(MARKER_UINT32)),
    ('client_driver_patch_version', FixedDataPacketField(MARKER_UINT32)),
    ('client_driver_name_len', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(8)),
    ('client_driver_name', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['client_driver_name_len'], 0)),
))


class GetClientDriverNameReplyReply:
    __slots__ = ('client_driver_major_version', 'client_driver_minor_version', 'client_driver_patch_version', 'client_driver_name_len', 'client_driver_name',)

    def __init__(
            self, *,
            client_driver_major_version: Optional[int] = None,
            client_driver_minor_version: Optional[int] = None,
            client_driver_patch_version: Optional[int] = None,
            client_driver_name_len: Optional[int] = None,
            client_driver_name: Optional[Sequence[int]] = None,
    ) -> None:
        self.client_driver_major_version = client_driver_major_version
        self.client_driver_minor_version = client_driver_minor_version
        self.client_driver_patch_version = client_driver_patch_version
        self.client_driver_name_len = client_driver_name_len
        self.client_driver_name = client_driver_name

    def as_dict(self) -> Dict[str, Any]:
        return {
            'client_driver_major_version': self.client_driver_major_version,
            'client_driver_minor_version': self.client_driver_minor_version,
            'client_driver_patch_version': self.client_driver_patch_version,
            'client_driver_name_len': self.client_driver_name_len,
            'client_driver_name': self.client_driver_name,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetClientDriverNameReplyReply':
        return GetClientDriverNameReplyReply(**GetClientDriverNameReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetClientDriverNameReplyReplyPacket.pack(**self.as_dict())


class GetClientDriverNameReplyReplyCType(ctypes.Structure):
    """xf86dri GetClientDriverName_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("client_driver_major_version", ctypes.c_uint32),
        ("client_driver_minor_version", ctypes.c_uint32),
        ("client_driver_patch_version", ctypes.c_uint32),
        ("client_driver_name_len", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 8),
        ("var_data", ctypes.c_void_p),
    ]


CreateContextRequestCookie = NewType('CreateContextRequestCookie', ctypes.c_uint32)


CreateContextRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT32)),
    ('visual', FixedDataPacketField(MARKER_UINT32)),
    ('context', FixedDataPacketField(MARKER_UINT32)),
))


class CreateContextRequest:
    OPCODE = 5

    __slots__ = ('screen', 'visual', 'context',)

    def __init__(
            self, *,
            screen: Optional[int] = None,
            visual: Optional[int] = None,
            context: Optional[int] = None,
    ) -> None:
        self.screen = screen
        self.visual = visual
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'screen': self.screen,
            'visual': self.visual,
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateContextRequest':
        return CreateContextRequest(**CreateContextRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateContextRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], CreateContextRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateContextRequest.lib = library.xf86dri_createcontext
        CreateContextRequest.lib.restype = CreateContextRequestCookie
        CreateContextRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class CreateContextRequestCType(ctypes.Structure):
    """xf86dri CreateContext"""
    _fields_ = [
        ("screen", ctypes.c_uint32),
        ("visual", ctypes.c_uint32),
        ("context", ctypes.c_uint32),
    ]


CreateContextReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('hw_context', FixedDataPacketField(MARKER_UINT32)),
))


class CreateContextReplyReply:
    __slots__ = ('hw_context',)

    def __init__(
            self, *,
            hw_context: Optional[int] = None,
    ) -> None:
        self.hw_context = hw_context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'hw_context': self.hw_context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateContextReplyReply':
        return CreateContextReplyReply(**CreateContextReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateContextReplyReplyPacket.pack(**self.as_dict())


class CreateContextReplyReplyCType(ctypes.Structure):
    """xf86dri CreateContext_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("hw_context", ctypes.c_uint32),
    ]


DestroyContextRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT32)),
    ('context', FixedDataPacketField(MARKER_UINT32)),
))


class DestroyContextRequest:
    OPCODE = 6

    __slots__ = ('screen', 'context',)

    def __init__(
            self, *,
            screen: Optional[int] = None,
            context: Optional[int] = None,
    ) -> None:
        self.screen = screen
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'screen': self.screen,
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DestroyContextRequest':
        return DestroyContextRequest(**DestroyContextRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DestroyContextRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        DestroyContextRequest.lib = library.xf86dri_destroycontext
        DestroyContextRequest.lib.restype = ctypes.c_uint32
        DestroyContextRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class DestroyContextRequestCType(ctypes.Structure):
    """xf86dri DestroyContext"""
    _fields_ = [
        ("screen", ctypes.c_uint32),
        ("context", ctypes.c_uint32),
    ]


CreateDrawableRequestCookie = NewType('CreateDrawableRequestCookie', ctypes.c_uint32)


CreateDrawableRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT32)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
))


class CreateDrawableRequest:
    OPCODE = 7

    __slots__ = ('screen', 'drawable',)

    def __init__(
            self, *,
            screen: Optional[int] = None,
            drawable: Optional[int] = None,
    ) -> None:
        self.screen = screen
        self.drawable = drawable

    def as_dict(self) -> Dict[str, Any]:
        return {
            'screen': self.screen,
            'drawable': self.drawable,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateDrawableRequest':
        return CreateDrawableRequest(**CreateDrawableRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateDrawableRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], CreateDrawableRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateDrawableRequest.lib = library.xf86dri_createdrawable
        CreateDrawableRequest.lib.restype = CreateDrawableRequestCookie
        CreateDrawableRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class CreateDrawableRequestCType(ctypes.Structure):
    """xf86dri CreateDrawable"""
    _fields_ = [
        ("screen", ctypes.c_uint32),
        ("drawable", ctypes.c_uint32),
    ]


CreateDrawableReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('hw_drawable_handle', FixedDataPacketField(MARKER_UINT32)),
))


class CreateDrawableReplyReply:
    __slots__ = ('hw_drawable_handle',)

    def __init__(
            self, *,
            hw_drawable_handle: Optional[int] = None,
    ) -> None:
        self.hw_drawable_handle = hw_drawable_handle

    def as_dict(self) -> Dict[str, Any]:
        return {
            'hw_drawable_handle': self.hw_drawable_handle,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateDrawableReplyReply':
        return CreateDrawableReplyReply(**CreateDrawableReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateDrawableReplyReplyPacket.pack(**self.as_dict())


class CreateDrawableReplyReplyCType(ctypes.Structure):
    """xf86dri CreateDrawable_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("hw_drawable_handle", ctypes.c_uint32),
    ]


DestroyDrawableRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT32)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
))


class DestroyDrawableRequest:
    OPCODE = 8

    __slots__ = ('screen', 'drawable',)

    def __init__(
            self, *,
            screen: Optional[int] = None,
            drawable: Optional[int] = None,
    ) -> None:
        self.screen = screen
        self.drawable = drawable

    def as_dict(self) -> Dict[str, Any]:
        return {
            'screen': self.screen,
            'drawable': self.drawable,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DestroyDrawableRequest':
        return DestroyDrawableRequest(**DestroyDrawableRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DestroyDrawableRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        DestroyDrawableRequest.lib = library.xf86dri_destroydrawable
        DestroyDrawableRequest.lib.restype = ctypes.c_uint32
        DestroyDrawableRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class DestroyDrawableRequestCType(ctypes.Structure):
    """xf86dri DestroyDrawable"""
    _fields_ = [
        ("screen", ctypes.c_uint32),
        ("drawable", ctypes.c_uint32),
    ]


GetDrawableInfoRequestCookie = NewType('GetDrawableInfoRequestCookie', ctypes.c_uint32)


GetDrawableInfoRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT32)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
))


class GetDrawableInfoRequest:
    OPCODE = 9

    __slots__ = ('screen', 'drawable',)

    def __init__(
            self, *,
            screen: Optional[int] = None,
            drawable: Optional[int] = None,
    ) -> None:
        self.screen = screen
        self.drawable = drawable

    def as_dict(self) -> Dict[str, Any]:
        return {
            'screen': self.screen,
            'drawable': self.drawable,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetDrawableInfoRequest':
        return GetDrawableInfoRequest(**GetDrawableInfoRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetDrawableInfoRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], GetDrawableInfoRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetDrawableInfoRequest.lib = library.xf86dri_getdrawableinfo
        GetDrawableInfoRequest.lib.restype = GetDrawableInfoRequestCookie
        GetDrawableInfoRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class GetDrawableInfoRequestCType(ctypes.Structure):
    """xf86dri GetDrawableInfo"""
    _fields_ = [
        ("screen", ctypes.c_uint32),
        ("drawable", ctypes.c_uint32),
    ]


GetDrawableInfoReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('drawable_table_index', FixedDataPacketField(MARKER_UINT32)),
    ('drawable_table_stamp', FixedDataPacketField(MARKER_UINT32)),
    ('drawable_origin_X', FixedDataPacketField(MARKER_INT16)),
    ('drawable_origin_Y', FixedDataPacketField(MARKER_INT16)),
    ('drawable_size_W', FixedDataPacketField(MARKER_INT16)),
    ('drawable_size_H', FixedDataPacketField(MARKER_INT16)),
    ('num_clip_rects', FixedDataPacketField(MARKER_UINT32)),
    ('back_x', FixedDataPacketField(MARKER_INT16)),
    ('back_y', FixedDataPacketField(MARKER_INT16)),
    ('num_back_clip_rects', FixedDataPacketField(MARKER_UINT32)),
    ('clip_rects', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_clip_rects'], 0)),
    ('back_clip_rects', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_back_clip_rects'], 0)),
))


class GetDrawableInfoReplyReply:
    __slots__ = ('drawable_table_index', 'drawable_table_stamp', 'drawable_origin_x', 'drawable_origin_y', 'drawable_size_w', 'drawable_size_h', 'num_clip_rects', 'back_x', 'back_y', 'num_back_clip_rects', 'clip_rects', 'back_clip_rects',)

    def __init__(
            self, *,
            drawable_table_index: Optional[int] = None,
            drawable_table_stamp: Optional[int] = None,
            drawable_origin_x: Optional[int] = None,
            drawable_origin_y: Optional[int] = None,
            drawable_size_w: Optional[int] = None,
            drawable_size_h: Optional[int] = None,
            num_clip_rects: Optional[int] = None,
            back_x: Optional[int] = None,
            back_y: Optional[int] = None,
            num_back_clip_rects: Optional[int] = None,
            clip_rects: Optional[Sequence[int]] = None,
            back_clip_rects: Optional[Sequence[int]] = None,
    ) -> None:
        self.drawable_table_index = drawable_table_index
        self.drawable_table_stamp = drawable_table_stamp
        self.drawable_origin_x = drawable_origin_x
        self.drawable_origin_y = drawable_origin_y
        self.drawable_size_w = drawable_size_w
        self.drawable_size_h = drawable_size_h
        self.num_clip_rects = num_clip_rects
        self.back_x = back_x
        self.back_y = back_y
        self.num_back_clip_rects = num_back_clip_rects
        self.clip_rects = clip_rects
        self.back_clip_rects = back_clip_rects

    def as_dict(self) -> Dict[str, Any]:
        return {
            'drawable_table_index': self.drawable_table_index,
            'drawable_table_stamp': self.drawable_table_stamp,
            'drawable_origin_X': self.drawable_origin_x,
            'drawable_origin_Y': self.drawable_origin_y,
            'drawable_size_W': self.drawable_size_w,
            'drawable_size_H': self.drawable_size_h,
            'num_clip_rects': self.num_clip_rects,
            'back_x': self.back_x,
            'back_y': self.back_y,
            'num_back_clip_rects': self.num_back_clip_rects,
            'clip_rects': self.clip_rects,
            'back_clip_rects': self.back_clip_rects,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetDrawableInfoReplyReply':
        return GetDrawableInfoReplyReply(**GetDrawableInfoReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetDrawableInfoReplyReplyPacket.pack(**self.as_dict())


class GetDrawableInfoReplyReplyCType(ctypes.Structure):
    """xf86dri GetDrawableInfo_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("drawable_table_index", ctypes.c_uint32),
        ("drawable_table_stamp", ctypes.c_uint32),
        ("drawable_origin_X", ctypes.c_int16),
        ("drawable_origin_Y", ctypes.c_int16),
        ("drawable_size_W", ctypes.c_int16),
        ("drawable_size_H", ctypes.c_int16),
        ("num_clip_rects", ctypes.c_uint32),
        ("back_x", ctypes.c_int16),
        ("back_y", ctypes.c_int16),
        ("num_back_clip_rects", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


GetDeviceInfoRequestCookie = NewType('GetDeviceInfoRequestCookie', ctypes.c_uint32)


GetDeviceInfoRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT32)),
))


class GetDeviceInfoRequest:
    OPCODE = 10

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
    def from_data(inp: BinaryIO) -> 'GetDeviceInfoRequest':
        return GetDeviceInfoRequest(**GetDeviceInfoRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetDeviceInfoRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetDeviceInfoRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetDeviceInfoRequest.lib = library.xf86dri_getdeviceinfo
        GetDeviceInfoRequest.lib.restype = GetDeviceInfoRequestCookie
        GetDeviceInfoRequest.lib.argstype = (ctypes.c_uint32,)


class GetDeviceInfoRequestCType(ctypes.Structure):
    """xf86dri GetDeviceInfo"""
    _fields_ = [
        ("screen", ctypes.c_uint32),
    ]


GetDeviceInfoReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('framebuffer_handle_low', FixedDataPacketField(MARKER_UINT32)),
    ('framebuffer_handle_high', FixedDataPacketField(MARKER_UINT32)),
    ('framebuffer_origin_offset', FixedDataPacketField(MARKER_UINT32)),
    ('framebuffer_size', FixedDataPacketField(MARKER_UINT32)),
    ('framebuffer_stride', FixedDataPacketField(MARKER_UINT32)),
    ('device_private_size', FixedDataPacketField(MARKER_UINT32)),
    ('device_private', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['device_private_size'], 0)),
))


class GetDeviceInfoReplyReply:
    __slots__ = ('framebuffer_handle_low', 'framebuffer_handle_high', 'framebuffer_origin_offset', 'framebuffer_size', 'framebuffer_stride', 'device_private_size', 'device_private',)

    def __init__(
            self, *,
            framebuffer_handle_low: Optional[int] = None,
            framebuffer_handle_high: Optional[int] = None,
            framebuffer_origin_offset: Optional[int] = None,
            framebuffer_size: Optional[int] = None,
            framebuffer_stride: Optional[int] = None,
            device_private_size: Optional[int] = None,
            device_private: Optional[Sequence[int]] = None,
    ) -> None:
        self.framebuffer_handle_low = framebuffer_handle_low
        self.framebuffer_handle_high = framebuffer_handle_high
        self.framebuffer_origin_offset = framebuffer_origin_offset
        self.framebuffer_size = framebuffer_size
        self.framebuffer_stride = framebuffer_stride
        self.device_private_size = device_private_size
        self.device_private = device_private

    def as_dict(self) -> Dict[str, Any]:
        return {
            'framebuffer_handle_low': self.framebuffer_handle_low,
            'framebuffer_handle_high': self.framebuffer_handle_high,
            'framebuffer_origin_offset': self.framebuffer_origin_offset,
            'framebuffer_size': self.framebuffer_size,
            'framebuffer_stride': self.framebuffer_stride,
            'device_private_size': self.device_private_size,
            'device_private': self.device_private,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetDeviceInfoReplyReply':
        return GetDeviceInfoReplyReply(**GetDeviceInfoReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetDeviceInfoReplyReplyPacket.pack(**self.as_dict())


class GetDeviceInfoReplyReplyCType(ctypes.Structure):
    """xf86dri GetDeviceInfo_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("framebuffer_handle_low", ctypes.c_uint32),
        ("framebuffer_handle_high", ctypes.c_uint32),
        ("framebuffer_origin_offset", ctypes.c_uint32),
        ("framebuffer_size", ctypes.c_uint32),
        ("framebuffer_stride", ctypes.c_uint32),
        ("device_private_size", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


AuthConnectionRequestCookie = NewType('AuthConnectionRequestCookie', ctypes.c_uint32)


AuthConnectionRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT32)),
    ('magic', FixedDataPacketField(MARKER_UINT32)),
))


class AuthConnectionRequest:
    OPCODE = 11

    __slots__ = ('screen', 'magic',)

    def __init__(
            self, *,
            screen: Optional[int] = None,
            magic: Optional[int] = None,
    ) -> None:
        self.screen = screen
        self.magic = magic

    def as_dict(self) -> Dict[str, Any]:
        return {
            'screen': self.screen,
            'magic': self.magic,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'AuthConnectionRequest':
        return AuthConnectionRequest(**AuthConnectionRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return AuthConnectionRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], AuthConnectionRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        AuthConnectionRequest.lib = library.xf86dri_authconnection
        AuthConnectionRequest.lib.restype = AuthConnectionRequestCookie
        AuthConnectionRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class AuthConnectionRequestCType(ctypes.Structure):
    """xf86dri AuthConnection"""
    _fields_ = [
        ("screen", ctypes.c_uint32),
        ("magic", ctypes.c_uint32),
    ]


AuthConnectionReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('authenticated', FixedDataPacketField(MARKER_UINT32)),
))


class AuthConnectionReplyReply:
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
    def from_data(inp: BinaryIO) -> 'AuthConnectionReplyReply':
        return AuthConnectionReplyReply(**AuthConnectionReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return AuthConnectionReplyReplyPacket.pack(**self.as_dict())


class AuthConnectionReplyReplyCType(ctypes.Structure):
    """xf86dri AuthConnection_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("authenticated", ctypes.c_uint32),
    ]


# ------------------------------------------------------------------
# Unions

