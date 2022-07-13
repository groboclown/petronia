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

PbcetType = NewType('PbcetType', int)


class PbcetValues:
    DAMAGED = PbcetType(32791)
    SAVED = PbcetType(32792)


PbcdtType = NewType('PbcdtType', int)


class PbcdtValues:
    WINDOW = PbcdtType(32793)
    PBUFFER = PbcdtType(32794)


GcType = NewType('GcType', int)


class GcValues:
    GL_CURRENT_BIT = GcType(1)
    GL_POINT_BIT = GcType(2)
    GL_LINE_BIT = GcType(4)
    GL_POLYGON_BIT = GcType(8)
    GL_POLYGON_STIPPLE_BIT = GcType(16)
    GL_PIXEL_MODE_BIT = GcType(32)
    GL_LIGHTING_BIT = GcType(64)
    GL_FOG_BIT = GcType(128)
    GL_DEPTH_BUFFER_BIT = GcType(256)
    GL_ACCUM_BUFFER_BIT = GcType(512)
    GL_STENCIL_BUFFER_BIT = GcType(1024)
    GL_VIEWPORT_BIT = GcType(2048)
    GL_TRANSFORM_BIT = GcType(4096)
    GL_ENABLE_BIT = GcType(8192)
    GL_COLOR_BUFFER_BIT = GcType(16384)
    GL_HINT_BIT = GcType(32768)
    GL_EVAL_BIT = GcType(65536)
    GL_LIST_BIT = GcType(131072)
    GL_TEXTURE_BIT = GcType(262144)
    GL_SCISSOR_BIT = GcType(524288)
    GL_ALL_ATTRIB_BITS = GcType(16777215)


RmType = NewType('RmType', int)


class RmValues:
    GL_RENDER = RmType(7168)
    GL_FEEDBACK = RmType(7169)
    GL_SELECT = RmType(7170)


# ------------------------------------------------------------------
# Aliases

Pixmap = NewType('Pixmap', ctypes.c_uint32)
Fbconfig = NewType('Fbconfig', ctypes.c_uint32)
Context = NewType('Context', ctypes.c_uint32)
Pbuffer = NewType('Pbuffer', ctypes.c_uint32)
Window = NewType('Window', ctypes.c_uint32)


# ------------------------------------------------------------------
# Structures, Events, Requests, Replies


PbufferClobberEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(1)),
    ('event_type', FixedDataPacketField(MARKER_UINT16)),
    ('draw_type', FixedDataPacketField(MARKER_UINT16)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('b_mask', FixedDataPacketField(MARKER_UINT32)),
    ('aux_buffer', FixedDataPacketField(MARKER_UINT16)),
    ('x', FixedDataPacketField(MARKER_UINT16)),
    ('y', FixedDataPacketField(MARKER_UINT16)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('count', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(4)),
))


class PbufferClobberEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'event_type', 'draw_type', 'drawable', 'b_mask', 'aux_buffer', 'x', 'y', 'width', 'height', 'count',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            event_type: Optional[int] = None,
            draw_type: Optional[int] = None,
            drawable: Optional[int] = None,
            b_mask: Optional[int] = None,
            aux_buffer: Optional[int] = None,
            x: Optional[int] = None,
            y: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            count: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.event_type = event_type
        self.draw_type = draw_type
        self.drawable = drawable
        self.b_mask = b_mask
        self.aux_buffer = aux_buffer
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.count = count

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'event_type': self.event_type,
            'draw_type': self.draw_type,
            'drawable': self.drawable,
            'b_mask': self.b_mask,
            'aux_buffer': self.aux_buffer,
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height,
            'count': self.count,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PbufferClobberEvent':
        return PbufferClobberEvent(**PbufferClobberEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PbufferClobberEventPacket.pack(**self.as_dict())


class PbufferClobberEventCType(ctypes.Structure):
    """glx PbufferClobber"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8),
        ("event_type", ctypes.c_uint16),
        ("draw_type", ctypes.c_uint16),
        ("drawable", ctypes.c_uint32),
        ("b_mask", ctypes.c_uint32),
        ("aux_buffer", ctypes.c_uint16),
        ("x", ctypes.c_uint16),
        ("y", ctypes.c_uint16),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("count", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 4),
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
    """glx BufferSwapComplete"""
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


RenderRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('data', SimpleListDataPacketField(MARKER_INT8, lambda d, c: 1, 0)),
))


class RenderRequest:
    OPCODE = 1

    __slots__ = ('context_tag', 'data',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.context_tag = context_tag
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'RenderRequest':
        return RenderRequest(**RenderRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return RenderRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        RenderRequest.lib = library.glx_render
        RenderRequest.lib.restype = ctypes.c_uint32
        RenderRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_void_p)


class RenderRequestCType(ctypes.Structure):
    """glx Render"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


RenderLargeRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('request_num', FixedDataPacketField(MARKER_UINT16)),
    ('request_total', FixedDataPacketField(MARKER_UINT16)),
    ('data_len', FixedDataPacketField(MARKER_UINT32)),
    ('data', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['data_len'], 0)),
))


class RenderLargeRequest:
    OPCODE = 2

    __slots__ = ('context_tag', 'request_num', 'request_total', 'data_len', 'data',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            request_num: Optional[int] = None,
            request_total: Optional[int] = None,
            data_len: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.context_tag = context_tag
        self.request_num = request_num
        self.request_total = request_total
        self.data_len = data_len
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'request_num': self.request_num,
            'request_total': self.request_total,
            'data_len': self.data_len,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'RenderLargeRequest':
        return RenderLargeRequest(**RenderLargeRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return RenderLargeRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        RenderLargeRequest.lib = library.glx_renderlarge
        RenderLargeRequest.lib.restype = ctypes.c_uint32
        RenderLargeRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint32, ctypes.c_void_p)


class RenderLargeRequestCType(ctypes.Structure):
    """glx RenderLarge"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("request_num", ctypes.c_uint16),
        ("request_total", ctypes.c_uint16),
        ("data_len", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


CreateContextRequestPacket = DataPacket((
    ('context', FixedDataPacketField(MARKER_UINT32)),
    ('visual', FixedDataPacketField(MARKER_UINT32)),
    ('screen', FixedDataPacketField(MARKER_UINT32)),
    ('share_list', FixedDataPacketField(MARKER_UINT32)),
    ('is_direct', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class CreateContextRequest:
    OPCODE = 3

    __slots__ = ('context', 'visual', 'screen', 'share_list', 'is_direct',)

    def __init__(
            self, *,
            context: Optional[int] = None,
            visual: Optional[int] = None,
            screen: Optional[int] = None,
            share_list: Optional[int] = None,
            is_direct: Optional[bool] = None,
    ) -> None:
        self.context = context
        self.visual = visual
        self.screen = screen
        self.share_list = share_list
        self.is_direct = is_direct

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context': self.context,
            'visual': self.visual,
            'screen': self.screen,
            'share_list': self.share_list,
            'is_direct': self.is_direct,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateContextRequest':
        return CreateContextRequest(**CreateContextRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateContextRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, bool], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateContextRequest.lib = library.glx_createcontext
        CreateContextRequest.lib.restype = ctypes.c_uint32
        CreateContextRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int8, ctypes.c_uint8 * 3)


class CreateContextRequestCType(ctypes.Structure):
    """glx CreateContext"""
    _fields_ = [
        ("context", ctypes.c_uint32),
        ("visual", ctypes.c_uint32),
        ("screen", ctypes.c_uint32),
        ("share_list", ctypes.c_uint32),
        ("is_direct", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


DestroyContextRequestPacket = DataPacket((
    ('context', FixedDataPacketField(MARKER_UINT32)),
))


class DestroyContextRequest:
    OPCODE = 4

    __slots__ = ('context',)

    def __init__(
            self, *,
            context: Optional[int] = None,
    ) -> None:
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DestroyContextRequest':
        return DestroyContextRequest(**DestroyContextRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DestroyContextRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        DestroyContextRequest.lib = library.glx_destroycontext
        DestroyContextRequest.lib.restype = ctypes.c_uint32
        DestroyContextRequest.lib.argstype = (ctypes.c_uint32,)


class DestroyContextRequestCType(ctypes.Structure):
    """glx DestroyContext"""
    _fields_ = [
        ("context", ctypes.c_uint32),
    ]


MakeCurrentRequestCookie = NewType('MakeCurrentRequestCookie', ctypes.c_uint32)


MakeCurrentRequestPacket = DataPacket((
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('context', FixedDataPacketField(MARKER_UINT32)),
    ('old_context_tag', FixedDataPacketField(MARKER_UINT32)),
))


class MakeCurrentRequest:
    OPCODE = 5

    __slots__ = ('drawable', 'context', 'old_context_tag',)

    def __init__(
            self, *,
            drawable: Optional[int] = None,
            context: Optional[int] = None,
            old_context_tag: Optional[int] = None,
    ) -> None:
        self.drawable = drawable
        self.context = context
        self.old_context_tag = old_context_tag

    def as_dict(self) -> Dict[str, Any]:
        return {
            'drawable': self.drawable,
            'context': self.context,
            'old_context_tag': self.old_context_tag,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'MakeCurrentRequest':
        return MakeCurrentRequest(**MakeCurrentRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return MakeCurrentRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], MakeCurrentRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        MakeCurrentRequest.lib = library.glx_makecurrent
        MakeCurrentRequest.lib.restype = MakeCurrentRequestCookie
        MakeCurrentRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class MakeCurrentRequestCType(ctypes.Structure):
    """glx MakeCurrent"""
    _fields_ = [
        ("drawable", ctypes.c_uint32),
        ("context", ctypes.c_uint32),
        ("old_context_tag", ctypes.c_uint32),
    ]


MakeCurrentReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
))


class MakeCurrentReplyReply:
    __slots__ = ('context_tag',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'MakeCurrentReplyReply':
        return MakeCurrentReplyReply(**MakeCurrentReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return MakeCurrentReplyReplyPacket.pack(**self.as_dict())


class MakeCurrentReplyReplyCType(ctypes.Structure):
    """glx MakeCurrent_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("context_tag", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
    ]


IsDirectRequestCookie = NewType('IsDirectRequestCookie', ctypes.c_uint32)


IsDirectRequestPacket = DataPacket((
    ('context', FixedDataPacketField(MARKER_UINT32)),
))


class IsDirectRequest:
    OPCODE = 6

    __slots__ = ('context',)

    def __init__(
            self, *,
            context: Optional[int] = None,
    ) -> None:
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'IsDirectRequest':
        return IsDirectRequest(**IsDirectRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return IsDirectRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], IsDirectRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        IsDirectRequest.lib = library.glx_isdirect
        IsDirectRequest.lib.restype = IsDirectRequestCookie
        IsDirectRequest.lib.argstype = (ctypes.c_uint32,)


class IsDirectRequestCType(ctypes.Structure):
    """glx IsDirect"""
    _fields_ = [
        ("context", ctypes.c_uint32),
    ]


IsDirectReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('is_direct', FixedDataPacketField(MARKER_UINT8)),
    ('pad1', FixedPadDataPacketField(23)),
))


class IsDirectReplyReply:
    __slots__ = ('is_direct',)

    def __init__(
            self, *,
            is_direct: Optional[bool] = None,
    ) -> None:
        self.is_direct = is_direct

    def as_dict(self) -> Dict[str, Any]:
        return {
            'is_direct': self.is_direct,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'IsDirectReplyReply':
        return IsDirectReplyReply(**IsDirectReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return IsDirectReplyReplyPacket.pack(**self.as_dict())


class IsDirectReplyReplyCType(ctypes.Structure):
    """glx IsDirect_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("is_direct", ctypes.c_int8),
        ("pad1", ctypes.c_uint8 * 23),
    ]


QueryVersionRequestCookie = NewType('QueryVersionRequestCookie', ctypes.c_uint32)


QueryVersionRequestPacket = DataPacket((
    ('major_version', FixedDataPacketField(MARKER_UINT32)),
    ('minor_version', FixedDataPacketField(MARKER_UINT32)),
))


class QueryVersionRequest:
    OPCODE = 7

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
        QueryVersionRequest.lib = library.glx_queryversion
        QueryVersionRequest.lib.restype = QueryVersionRequestCookie
        QueryVersionRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class QueryVersionRequestCType(ctypes.Structure):
    """glx QueryVersion"""
    _fields_ = [
        ("major_version", ctypes.c_uint32),
        ("minor_version", ctypes.c_uint32),
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
    """glx QueryVersion_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("major_version", ctypes.c_uint32),
        ("minor_version", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 16),
    ]


WaitGlRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
))


class WaitGlRequest:
    OPCODE = 8

    __slots__ = ('context_tag',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'WaitGlRequest':
        return WaitGlRequest(**WaitGlRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return WaitGlRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        WaitGlRequest.lib = library.glx_waitgl
        WaitGlRequest.lib.restype = ctypes.c_uint32
        WaitGlRequest.lib.argstype = (ctypes.c_uint32,)


class WaitGlRequestCType(ctypes.Structure):
    """glx WaitGL"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
    ]


WaitXRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
))


class WaitXRequest:
    OPCODE = 9

    __slots__ = ('context_tag',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'WaitXRequest':
        return WaitXRequest(**WaitXRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return WaitXRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        WaitXRequest.lib = library.glx_waitx
        WaitXRequest.lib.restype = ctypes.c_uint32
        WaitXRequest.lib.argstype = (ctypes.c_uint32,)


class WaitXRequestCType(ctypes.Structure):
    """glx WaitX"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
    ]


CopyContextRequestPacket = DataPacket((
    ('src', FixedDataPacketField(MARKER_UINT32)),
    ('dest', FixedDataPacketField(MARKER_UINT32)),
    ('mask', FixedDataPacketField(MARKER_UINT32)),
    ('src_context_tag', FixedDataPacketField(MARKER_UINT32)),
))


class CopyContextRequest:
    OPCODE = 10

    __slots__ = ('src', 'dest', 'mask', 'src_context_tag',)

    def __init__(
            self, *,
            src: Optional[int] = None,
            dest: Optional[int] = None,
            mask: Optional[int] = None,
            src_context_tag: Optional[int] = None,
    ) -> None:
        self.src = src
        self.dest = dest
        self.mask = mask
        self.src_context_tag = src_context_tag

    def as_dict(self) -> Dict[str, Any]:
        return {
            'src': self.src,
            'dest': self.dest,
            'mask': self.mask,
            'src_context_tag': self.src_context_tag,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CopyContextRequest':
        return CopyContextRequest(**CopyContextRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CopyContextRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CopyContextRequest.lib = library.glx_copycontext
        CopyContextRequest.lib.restype = ctypes.c_uint32
        CopyContextRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class CopyContextRequestCType(ctypes.Structure):
    """glx CopyContext"""
    _fields_ = [
        ("src", ctypes.c_uint32),
        ("dest", ctypes.c_uint32),
        ("mask", ctypes.c_uint32),
        ("src_context_tag", ctypes.c_uint32),
    ]


SwapBuffersRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
))


class SwapBuffersRequest:
    OPCODE = 11

    __slots__ = ('context_tag', 'drawable',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            drawable: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.drawable = drawable

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'drawable': self.drawable,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SwapBuffersRequest':
        return SwapBuffersRequest(**SwapBuffersRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SwapBuffersRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SwapBuffersRequest.lib = library.glx_swapbuffers
        SwapBuffersRequest.lib.restype = ctypes.c_uint32
        SwapBuffersRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class SwapBuffersRequestCType(ctypes.Structure):
    """glx SwapBuffers"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("drawable", ctypes.c_uint32),
    ]


UseXfontRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('font', FixedDataPacketField(MARKER_UINT32)),
    ('first', FixedDataPacketField(MARKER_UINT32)),
    ('count', FixedDataPacketField(MARKER_UINT32)),
    ('list_base', FixedDataPacketField(MARKER_UINT32)),
))


class UseXfontRequest:
    OPCODE = 12

    __slots__ = ('context_tag', 'font', 'first', 'count', 'list_base',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            font: Optional[int] = None,
            first: Optional[int] = None,
            count: Optional[int] = None,
            list_base: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.font = font
        self.first = first
        self.count = count
        self.list_base = list_base

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'font': self.font,
            'first': self.first,
            'count': self.count,
            'list_base': self.list_base,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'UseXfontRequest':
        return UseXfontRequest(**UseXfontRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return UseXfontRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        UseXfontRequest.lib = library.glx_usexfont
        UseXfontRequest.lib.restype = ctypes.c_uint32
        UseXfontRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class UseXfontRequestCType(ctypes.Structure):
    """glx UseXFont"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("font", ctypes.c_uint32),
        ("first", ctypes.c_uint32),
        ("count", ctypes.c_uint32),
        ("list_base", ctypes.c_uint32),
    ]


CreateGlxpixmapRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT32)),
    ('visual', FixedDataPacketField(MARKER_UINT32)),
    ('pixmap', FixedDataPacketField(MARKER_UINT32)),
    ('glx_pixmap', FixedDataPacketField(MARKER_UINT32)),
))


class CreateGlxpixmapRequest:
    OPCODE = 13

    __slots__ = ('screen', 'visual', 'pixmap', 'glx_pixmap',)

    def __init__(
            self, *,
            screen: Optional[int] = None,
            visual: Optional[int] = None,
            pixmap: Optional[int] = None,
            glx_pixmap: Optional[int] = None,
    ) -> None:
        self.screen = screen
        self.visual = visual
        self.pixmap = pixmap
        self.glx_pixmap = glx_pixmap

    def as_dict(self) -> Dict[str, Any]:
        return {
            'screen': self.screen,
            'visual': self.visual,
            'pixmap': self.pixmap,
            'glx_pixmap': self.glx_pixmap,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateGlxpixmapRequest':
        return CreateGlxpixmapRequest(**CreateGlxpixmapRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateGlxpixmapRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateGlxpixmapRequest.lib = library.glx_createglxpixmap
        CreateGlxpixmapRequest.lib.restype = ctypes.c_uint32
        CreateGlxpixmapRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class CreateGlxpixmapRequestCType(ctypes.Structure):
    """glx CreateGLXPixmap"""
    _fields_ = [
        ("screen", ctypes.c_uint32),
        ("visual", ctypes.c_uint32),
        ("pixmap", ctypes.c_uint32),
        ("glx_pixmap", ctypes.c_uint32),
    ]


GetVisualConfigsRequestCookie = NewType('GetVisualConfigsRequestCookie', ctypes.c_uint32)


GetVisualConfigsRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT32)),
))


class GetVisualConfigsRequest:
    OPCODE = 14

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
    def from_data(inp: BinaryIO) -> 'GetVisualConfigsRequest':
        return GetVisualConfigsRequest(**GetVisualConfigsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetVisualConfigsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetVisualConfigsRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetVisualConfigsRequest.lib = library.glx_getvisualconfigs
        GetVisualConfigsRequest.lib.restype = GetVisualConfigsRequestCookie
        GetVisualConfigsRequest.lib.argstype = (ctypes.c_uint32,)


class GetVisualConfigsRequestCType(ctypes.Structure):
    """glx GetVisualConfigs"""
    _fields_ = [
        ("screen", ctypes.c_uint32),
    ]


GetVisualConfigsReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('num_visuals', FixedDataPacketField(MARKER_UINT32)),
    ('num_properties', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(16)),
    ('property_list', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['length'], 0)),
))


class GetVisualConfigsReplyReply:
    __slots__ = ('num_visuals', 'num_properties', 'property_list',)

    def __init__(
            self, *,
            num_visuals: Optional[int] = None,
            num_properties: Optional[int] = None,
            property_list: Optional[Sequence[int]] = None,
    ) -> None:
        self.num_visuals = num_visuals
        self.num_properties = num_properties
        self.property_list = property_list

    def as_dict(self) -> Dict[str, Any]:
        return {
            'num_visuals': self.num_visuals,
            'num_properties': self.num_properties,
            'property_list': self.property_list,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetVisualConfigsReplyReply':
        return GetVisualConfigsReplyReply(**GetVisualConfigsReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetVisualConfigsReplyReplyPacket.pack(**self.as_dict())


class GetVisualConfigsReplyReplyCType(ctypes.Structure):
    """glx GetVisualConfigs_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("num_visuals", ctypes.c_uint32),
        ("num_properties", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 16),
        ("var_data", ctypes.c_void_p),
    ]


DestroyGlxpixmapRequestPacket = DataPacket((
    ('glx_pixmap', FixedDataPacketField(MARKER_UINT32)),
))


class DestroyGlxpixmapRequest:
    OPCODE = 15

    __slots__ = ('glx_pixmap',)

    def __init__(
            self, *,
            glx_pixmap: Optional[int] = None,
    ) -> None:
        self.glx_pixmap = glx_pixmap

    def as_dict(self) -> Dict[str, Any]:
        return {
            'glx_pixmap': self.glx_pixmap,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DestroyGlxpixmapRequest':
        return DestroyGlxpixmapRequest(**DestroyGlxpixmapRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DestroyGlxpixmapRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        DestroyGlxpixmapRequest.lib = library.glx_destroyglxpixmap
        DestroyGlxpixmapRequest.lib.restype = ctypes.c_uint32
        DestroyGlxpixmapRequest.lib.argstype = (ctypes.c_uint32,)


class DestroyGlxpixmapRequestCType(ctypes.Structure):
    """glx DestroyGLXPixmap"""
    _fields_ = [
        ("glx_pixmap", ctypes.c_uint32),
    ]


VendorPrivateRequestPacket = DataPacket((
    ('vendor_code', FixedDataPacketField(MARKER_UINT32)),
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('data', SimpleListDataPacketField(MARKER_INT8, lambda d, c: 1, 0)),
))


class VendorPrivateRequest:
    OPCODE = 16

    __slots__ = ('vendor_code', 'context_tag', 'data',)

    def __init__(
            self, *,
            vendor_code: Optional[int] = None,
            context_tag: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.vendor_code = vendor_code
        self.context_tag = context_tag
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'vendor_code': self.vendor_code,
            'context_tag': self.context_tag,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'VendorPrivateRequest':
        return VendorPrivateRequest(**VendorPrivateRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return VendorPrivateRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        VendorPrivateRequest.lib = library.glx_vendorprivate
        VendorPrivateRequest.lib.restype = ctypes.c_uint32
        VendorPrivateRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)


class VendorPrivateRequestCType(ctypes.Structure):
    """glx VendorPrivate"""
    _fields_ = [
        ("vendor_code", ctypes.c_uint32),
        ("context_tag", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


VendorPrivateWithReplyRequestCookie = NewType('VendorPrivateWithReplyRequestCookie', ctypes.c_uint32)


VendorPrivateWithReplyRequestPacket = DataPacket((
    ('vendor_code', FixedDataPacketField(MARKER_UINT32)),
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('data', SimpleListDataPacketField(MARKER_INT8, lambda d, c: 1, 0)),
))


class VendorPrivateWithReplyRequest:
    OPCODE = 17

    __slots__ = ('vendor_code', 'context_tag', 'data',)

    def __init__(
            self, *,
            vendor_code: Optional[int] = None,
            context_tag: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.vendor_code = vendor_code
        self.context_tag = context_tag
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'vendor_code': self.vendor_code,
            'context_tag': self.context_tag,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'VendorPrivateWithReplyRequest':
        return VendorPrivateWithReplyRequest(**VendorPrivateWithReplyRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return VendorPrivateWithReplyRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int]], VendorPrivateWithReplyRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        VendorPrivateWithReplyRequest.lib = library.glx_vendorprivatewithreply
        VendorPrivateWithReplyRequest.lib.restype = VendorPrivateWithReplyRequestCookie
        VendorPrivateWithReplyRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)


class VendorPrivateWithReplyRequestCType(ctypes.Structure):
    """glx VendorPrivateWithReply"""
    _fields_ = [
        ("vendor_code", ctypes.c_uint32),
        ("context_tag", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


VendorPrivateWithReplyReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('retval', FixedDataPacketField(MARKER_UINT32)),
    ('data1', SimpleListDataPacketField(MARKER_INT8, lambda d, c: 24, 0)),
    ('data2', SimpleListDataPacketField(MARKER_INT8, lambda d, c: (d['length']) * (4), 0)),
))


class VendorPrivateWithReplyReplyReply:
    __slots__ = ('retval', 'data1', 'data2',)

    def __init__(
            self, *,
            retval: Optional[int] = None,
            data1: Optional[Sequence[int]] = None,
            data2: Optional[Sequence[int]] = None,
    ) -> None:
        self.retval = retval
        self.data1 = data1
        self.data2 = data2

    def as_dict(self) -> Dict[str, Any]:
        return {
            'retval': self.retval,
            'data1': self.data1,
            'data2': self.data2,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'VendorPrivateWithReplyReplyReply':
        return VendorPrivateWithReplyReplyReply(**VendorPrivateWithReplyReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return VendorPrivateWithReplyReplyReplyPacket.pack(**self.as_dict())


class VendorPrivateWithReplyReplyReplyCType(ctypes.Structure):
    """glx VendorPrivateWithReply_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("retval", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


QueryExtensionsStringRequestCookie = NewType('QueryExtensionsStringRequestCookie', ctypes.c_uint32)


QueryExtensionsStringRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT32)),
))


class QueryExtensionsStringRequest:
    OPCODE = 18

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
    def from_data(inp: BinaryIO) -> 'QueryExtensionsStringRequest':
        return QueryExtensionsStringRequest(**QueryExtensionsStringRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryExtensionsStringRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], QueryExtensionsStringRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryExtensionsStringRequest.lib = library.glx_queryextensionsstring
        QueryExtensionsStringRequest.lib.restype = QueryExtensionsStringRequestCookie
        QueryExtensionsStringRequest.lib.argstype = (ctypes.c_uint32,)


class QueryExtensionsStringRequestCType(ctypes.Structure):
    """glx QueryExtensionsString"""
    _fields_ = [
        ("screen", ctypes.c_uint32),
    ]


QueryExtensionsStringReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('pad2', FixedPadDataPacketField(16)),
))


class QueryExtensionsStringReplyReply:
    __slots__ = ('n',)

    def __init__(
            self, *,
            n: Optional[int] = None,
    ) -> None:
        self.n = n

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryExtensionsStringReplyReply':
        return QueryExtensionsStringReplyReply(**QueryExtensionsStringReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryExtensionsStringReplyReplyPacket.pack(**self.as_dict())


class QueryExtensionsStringReplyReplyCType(ctypes.Structure):
    """glx QueryExtensionsString_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("pad2", ctypes.c_uint8 * 16),
    ]


QueryServerStringRequestCookie = NewType('QueryServerStringRequestCookie', ctypes.c_uint32)


QueryServerStringRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT32)),
    ('name', FixedDataPacketField(MARKER_UINT32)),
))


class QueryServerStringRequest:
    OPCODE = 19

    __slots__ = ('screen', 'name',)

    def __init__(
            self, *,
            screen: Optional[int] = None,
            name: Optional[int] = None,
    ) -> None:
        self.screen = screen
        self.name = name

    def as_dict(self) -> Dict[str, Any]:
        return {
            'screen': self.screen,
            'name': self.name,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryServerStringRequest':
        return QueryServerStringRequest(**QueryServerStringRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryServerStringRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], QueryServerStringRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryServerStringRequest.lib = library.glx_queryserverstring
        QueryServerStringRequest.lib.restype = QueryServerStringRequestCookie
        QueryServerStringRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class QueryServerStringRequestCType(ctypes.Structure):
    """glx QueryServerString"""
    _fields_ = [
        ("screen", ctypes.c_uint32),
        ("name", ctypes.c_uint32),
    ]


QueryServerStringReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('str_len', FixedDataPacketField(MARKER_UINT32)),
    ('pad2', FixedPadDataPacketField(16)),
    ('string', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['str_len'], 0)),
))


class QueryServerStringReplyReply:
    __slots__ = ('str_len', 'string',)

    def __init__(
            self, *,
            str_len: Optional[int] = None,
            string: Optional[Sequence[int]] = None,
    ) -> None:
        self.str_len = str_len
        self.string = string

    def as_dict(self) -> Dict[str, Any]:
        return {
            'str_len': self.str_len,
            'string': self.string,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryServerStringReplyReply':
        return QueryServerStringReplyReply(**QueryServerStringReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryServerStringReplyReplyPacket.pack(**self.as_dict())


class QueryServerStringReplyReplyCType(ctypes.Structure):
    """glx QueryServerString_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("str_len", ctypes.c_uint32),
        ("pad2", ctypes.c_uint8 * 16),
        ("var_data", ctypes.c_void_p),
    ]


ClientInfoRequestPacket = DataPacket((
    ('major_version', FixedDataPacketField(MARKER_UINT32)),
    ('minor_version', FixedDataPacketField(MARKER_UINT32)),
    ('str_len', FixedDataPacketField(MARKER_UINT32)),
    ('string', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['str_len'], 0)),
))


class ClientInfoRequest:
    OPCODE = 20

    __slots__ = ('major_version', 'minor_version', 'str_len', 'string',)

    def __init__(
            self, *,
            major_version: Optional[int] = None,
            minor_version: Optional[int] = None,
            str_len: Optional[int] = None,
            string: Optional[Sequence[int]] = None,
    ) -> None:
        self.major_version = major_version
        self.minor_version = minor_version
        self.str_len = str_len
        self.string = string

    def as_dict(self) -> Dict[str, Any]:
        return {
            'major_version': self.major_version,
            'minor_version': self.minor_version,
            'str_len': self.str_len,
            'string': self.string,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ClientInfoRequest':
        return ClientInfoRequest(**ClientInfoRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ClientInfoRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ClientInfoRequest.lib = library.glx_clientinfo
        ClientInfoRequest.lib.restype = ctypes.c_uint32
        ClientInfoRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)


class ClientInfoRequestCType(ctypes.Structure):
    """glx ClientInfo"""
    _fields_ = [
        ("major_version", ctypes.c_uint32),
        ("minor_version", ctypes.c_uint32),
        ("str_len", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


GetFbconfigsRequestCookie = NewType('GetFbconfigsRequestCookie', ctypes.c_uint32)


GetFbconfigsRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT32)),
))


class GetFbconfigsRequest:
    OPCODE = 21

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
    def from_data(inp: BinaryIO) -> 'GetFbconfigsRequest':
        return GetFbconfigsRequest(**GetFbconfigsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetFbconfigsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetFbconfigsRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetFbconfigsRequest.lib = library.glx_getfbconfigs
        GetFbconfigsRequest.lib.restype = GetFbconfigsRequestCookie
        GetFbconfigsRequest.lib.argstype = (ctypes.c_uint32,)


class GetFbconfigsRequestCType(ctypes.Structure):
    """glx GetFBConfigs"""
    _fields_ = [
        ("screen", ctypes.c_uint32),
    ]


GetFbconfigsReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('num_FB_configs', FixedDataPacketField(MARKER_UINT32)),
    ('num_properties', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(16)),
    ('property_list', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['length'], 0)),
))


class GetFbconfigsReplyReply:
    __slots__ = ('num_fb_configs', 'num_properties', 'property_list',)

    def __init__(
            self, *,
            num_fb_configs: Optional[int] = None,
            num_properties: Optional[int] = None,
            property_list: Optional[Sequence[int]] = None,
    ) -> None:
        self.num_fb_configs = num_fb_configs
        self.num_properties = num_properties
        self.property_list = property_list

    def as_dict(self) -> Dict[str, Any]:
        return {
            'num_FB_configs': self.num_fb_configs,
            'num_properties': self.num_properties,
            'property_list': self.property_list,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetFbconfigsReplyReply':
        return GetFbconfigsReplyReply(**GetFbconfigsReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetFbconfigsReplyReplyPacket.pack(**self.as_dict())


class GetFbconfigsReplyReplyCType(ctypes.Structure):
    """glx GetFBConfigs_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("num_FB_configs", ctypes.c_uint32),
        ("num_properties", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 16),
        ("var_data", ctypes.c_void_p),
    ]


CreatePixmapRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT32)),
    ('fbconfig', FixedDataPacketField(MARKER_UINT32)),
    ('pixmap', FixedDataPacketField(MARKER_UINT32)),
    ('glx_pixmap', FixedDataPacketField(MARKER_UINT32)),
    ('num_attribs', FixedDataPacketField(MARKER_UINT32)),
    ('attribs', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: (d['num_attribs']) * (2), 0)),
))


class CreatePixmapRequest:
    OPCODE = 22

    __slots__ = ('screen', 'fbconfig', 'pixmap', 'glx_pixmap', 'num_attribs', 'attribs',)

    def __init__(
            self, *,
            screen: Optional[int] = None,
            fbconfig: Optional[int] = None,
            pixmap: Optional[int] = None,
            glx_pixmap: Optional[int] = None,
            num_attribs: Optional[int] = None,
            attribs: Optional[Sequence[int]] = None,
    ) -> None:
        self.screen = screen
        self.fbconfig = fbconfig
        self.pixmap = pixmap
        self.glx_pixmap = glx_pixmap
        self.num_attribs = num_attribs
        self.attribs = attribs

    def as_dict(self) -> Dict[str, Any]:
        return {
            'screen': self.screen,
            'fbconfig': self.fbconfig,
            'pixmap': self.pixmap,
            'glx_pixmap': self.glx_pixmap,
            'num_attribs': self.num_attribs,
            'attribs': self.attribs,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreatePixmapRequest':
        return CreatePixmapRequest(**CreatePixmapRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreatePixmapRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreatePixmapRequest.lib = library.glx_createpixmap
        CreatePixmapRequest.lib.restype = ctypes.c_uint32
        CreatePixmapRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)


class CreatePixmapRequestCType(ctypes.Structure):
    """glx CreatePixmap"""
    _fields_ = [
        ("screen", ctypes.c_uint32),
        ("fbconfig", ctypes.c_uint32),
        ("pixmap", ctypes.c_uint32),
        ("glx_pixmap", ctypes.c_uint32),
        ("num_attribs", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


DestroyPixmapRequestPacket = DataPacket((
    ('glx_pixmap', FixedDataPacketField(MARKER_UINT32)),
))


class DestroyPixmapRequest:
    OPCODE = 23

    __slots__ = ('glx_pixmap',)

    def __init__(
            self, *,
            glx_pixmap: Optional[int] = None,
    ) -> None:
        self.glx_pixmap = glx_pixmap

    def as_dict(self) -> Dict[str, Any]:
        return {
            'glx_pixmap': self.glx_pixmap,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DestroyPixmapRequest':
        return DestroyPixmapRequest(**DestroyPixmapRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DestroyPixmapRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        DestroyPixmapRequest.lib = library.glx_destroypixmap
        DestroyPixmapRequest.lib.restype = ctypes.c_uint32
        DestroyPixmapRequest.lib.argstype = (ctypes.c_uint32,)


class DestroyPixmapRequestCType(ctypes.Structure):
    """glx DestroyPixmap"""
    _fields_ = [
        ("glx_pixmap", ctypes.c_uint32),
    ]


CreateNewContextRequestPacket = DataPacket((
    ('context', FixedDataPacketField(MARKER_UINT32)),
    ('fbconfig', FixedDataPacketField(MARKER_UINT32)),
    ('screen', FixedDataPacketField(MARKER_UINT32)),
    ('render_type', FixedDataPacketField(MARKER_UINT32)),
    ('share_list', FixedDataPacketField(MARKER_UINT32)),
    ('is_direct', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class CreateNewContextRequest:
    OPCODE = 24

    __slots__ = ('context', 'fbconfig', 'screen', 'render_type', 'share_list', 'is_direct',)

    def __init__(
            self, *,
            context: Optional[int] = None,
            fbconfig: Optional[int] = None,
            screen: Optional[int] = None,
            render_type: Optional[int] = None,
            share_list: Optional[int] = None,
            is_direct: Optional[bool] = None,
    ) -> None:
        self.context = context
        self.fbconfig = fbconfig
        self.screen = screen
        self.render_type = render_type
        self.share_list = share_list
        self.is_direct = is_direct

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context': self.context,
            'fbconfig': self.fbconfig,
            'screen': self.screen,
            'render_type': self.render_type,
            'share_list': self.share_list,
            'is_direct': self.is_direct,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateNewContextRequest':
        return CreateNewContextRequest(**CreateNewContextRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateNewContextRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, bool], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateNewContextRequest.lib = library.glx_createnewcontext
        CreateNewContextRequest.lib.restype = ctypes.c_uint32
        CreateNewContextRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int8, ctypes.c_uint8 * 3)


class CreateNewContextRequestCType(ctypes.Structure):
    """glx CreateNewContext"""
    _fields_ = [
        ("context", ctypes.c_uint32),
        ("fbconfig", ctypes.c_uint32),
        ("screen", ctypes.c_uint32),
        ("render_type", ctypes.c_uint32),
        ("share_list", ctypes.c_uint32),
        ("is_direct", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


QueryContextRequestCookie = NewType('QueryContextRequestCookie', ctypes.c_uint32)


QueryContextRequestPacket = DataPacket((
    ('context', FixedDataPacketField(MARKER_UINT32)),
))


class QueryContextRequest:
    OPCODE = 25

    __slots__ = ('context',)

    def __init__(
            self, *,
            context: Optional[int] = None,
    ) -> None:
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryContextRequest':
        return QueryContextRequest(**QueryContextRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryContextRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], QueryContextRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryContextRequest.lib = library.glx_querycontext
        QueryContextRequest.lib.restype = QueryContextRequestCookie
        QueryContextRequest.lib.argstype = (ctypes.c_uint32,)


class QueryContextRequestCType(ctypes.Structure):
    """glx QueryContext"""
    _fields_ = [
        ("context", ctypes.c_uint32),
    ]


QueryContextReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('num_attribs', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('attribs', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: (d['num_attribs']) * (2), 0)),
))


class QueryContextReplyReply:
    __slots__ = ('num_attribs', 'attribs',)

    def __init__(
            self, *,
            num_attribs: Optional[int] = None,
            attribs: Optional[Sequence[int]] = None,
    ) -> None:
        self.num_attribs = num_attribs
        self.attribs = attribs

    def as_dict(self) -> Dict[str, Any]:
        return {
            'num_attribs': self.num_attribs,
            'attribs': self.attribs,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryContextReplyReply':
        return QueryContextReplyReply(**QueryContextReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryContextReplyReplyPacket.pack(**self.as_dict())


class QueryContextReplyReplyCType(ctypes.Structure):
    """glx QueryContext_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("num_attribs", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


MakeContextCurrentRequestCookie = NewType('MakeContextCurrentRequestCookie', ctypes.c_uint32)


MakeContextCurrentRequestPacket = DataPacket((
    ('old_context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('read_drawable', FixedDataPacketField(MARKER_UINT32)),
    ('context', FixedDataPacketField(MARKER_UINT32)),
))


class MakeContextCurrentRequest:
    OPCODE = 26

    __slots__ = ('old_context_tag', 'drawable', 'read_drawable', 'context',)

    def __init__(
            self, *,
            old_context_tag: Optional[int] = None,
            drawable: Optional[int] = None,
            read_drawable: Optional[int] = None,
            context: Optional[int] = None,
    ) -> None:
        self.old_context_tag = old_context_tag
        self.drawable = drawable
        self.read_drawable = read_drawable
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'old_context_tag': self.old_context_tag,
            'drawable': self.drawable,
            'read_drawable': self.read_drawable,
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'MakeContextCurrentRequest':
        return MakeContextCurrentRequest(**MakeContextCurrentRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return MakeContextCurrentRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int], MakeContextCurrentRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        MakeContextCurrentRequest.lib = library.glx_makecontextcurrent
        MakeContextCurrentRequest.lib.restype = MakeContextCurrentRequestCookie
        MakeContextCurrentRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class MakeContextCurrentRequestCType(ctypes.Structure):
    """glx MakeContextCurrent"""
    _fields_ = [
        ("old_context_tag", ctypes.c_uint32),
        ("drawable", ctypes.c_uint32),
        ("read_drawable", ctypes.c_uint32),
        ("context", ctypes.c_uint32),
    ]


MakeContextCurrentReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
))


class MakeContextCurrentReplyReply:
    __slots__ = ('context_tag',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'MakeContextCurrentReplyReply':
        return MakeContextCurrentReplyReply(**MakeContextCurrentReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return MakeContextCurrentReplyReplyPacket.pack(**self.as_dict())


class MakeContextCurrentReplyReplyCType(ctypes.Structure):
    """glx MakeContextCurrent_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("context_tag", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
    ]


CreatePbufferRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT32)),
    ('fbconfig', FixedDataPacketField(MARKER_UINT32)),
    ('pbuffer', FixedDataPacketField(MARKER_UINT32)),
    ('num_attribs', FixedDataPacketField(MARKER_UINT32)),
    ('attribs', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: (d['num_attribs']) * (2), 0)),
))


class CreatePbufferRequest:
    OPCODE = 27

    __slots__ = ('screen', 'fbconfig', 'pbuffer', 'num_attribs', 'attribs',)

    def __init__(
            self, *,
            screen: Optional[int] = None,
            fbconfig: Optional[int] = None,
            pbuffer: Optional[int] = None,
            num_attribs: Optional[int] = None,
            attribs: Optional[Sequence[int]] = None,
    ) -> None:
        self.screen = screen
        self.fbconfig = fbconfig
        self.pbuffer = pbuffer
        self.num_attribs = num_attribs
        self.attribs = attribs

    def as_dict(self) -> Dict[str, Any]:
        return {
            'screen': self.screen,
            'fbconfig': self.fbconfig,
            'pbuffer': self.pbuffer,
            'num_attribs': self.num_attribs,
            'attribs': self.attribs,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreatePbufferRequest':
        return CreatePbufferRequest(**CreatePbufferRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreatePbufferRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreatePbufferRequest.lib = library.glx_createpbuffer
        CreatePbufferRequest.lib.restype = ctypes.c_uint32
        CreatePbufferRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)


class CreatePbufferRequestCType(ctypes.Structure):
    """glx CreatePbuffer"""
    _fields_ = [
        ("screen", ctypes.c_uint32),
        ("fbconfig", ctypes.c_uint32),
        ("pbuffer", ctypes.c_uint32),
        ("num_attribs", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


DestroyPbufferRequestPacket = DataPacket((
    ('pbuffer', FixedDataPacketField(MARKER_UINT32)),
))


class DestroyPbufferRequest:
    OPCODE = 28

    __slots__ = ('pbuffer',)

    def __init__(
            self, *,
            pbuffer: Optional[int] = None,
    ) -> None:
        self.pbuffer = pbuffer

    def as_dict(self) -> Dict[str, Any]:
        return {
            'pbuffer': self.pbuffer,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DestroyPbufferRequest':
        return DestroyPbufferRequest(**DestroyPbufferRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DestroyPbufferRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        DestroyPbufferRequest.lib = library.glx_destroypbuffer
        DestroyPbufferRequest.lib.restype = ctypes.c_uint32
        DestroyPbufferRequest.lib.argstype = (ctypes.c_uint32,)


class DestroyPbufferRequestCType(ctypes.Structure):
    """glx DestroyPbuffer"""
    _fields_ = [
        ("pbuffer", ctypes.c_uint32),
    ]


GetDrawableAttributesRequestCookie = NewType('GetDrawableAttributesRequestCookie', ctypes.c_uint32)


GetDrawableAttributesRequestPacket = DataPacket((
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
))


class GetDrawableAttributesRequest:
    OPCODE = 29

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
    def from_data(inp: BinaryIO) -> 'GetDrawableAttributesRequest':
        return GetDrawableAttributesRequest(**GetDrawableAttributesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetDrawableAttributesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetDrawableAttributesRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetDrawableAttributesRequest.lib = library.glx_getdrawableattributes
        GetDrawableAttributesRequest.lib.restype = GetDrawableAttributesRequestCookie
        GetDrawableAttributesRequest.lib.argstype = (ctypes.c_uint32,)


class GetDrawableAttributesRequestCType(ctypes.Structure):
    """glx GetDrawableAttributes"""
    _fields_ = [
        ("drawable", ctypes.c_uint32),
    ]


GetDrawableAttributesReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('num_attribs', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('attribs', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: (d['num_attribs']) * (2), 0)),
))


class GetDrawableAttributesReplyReply:
    __slots__ = ('num_attribs', 'attribs',)

    def __init__(
            self, *,
            num_attribs: Optional[int] = None,
            attribs: Optional[Sequence[int]] = None,
    ) -> None:
        self.num_attribs = num_attribs
        self.attribs = attribs

    def as_dict(self) -> Dict[str, Any]:
        return {
            'num_attribs': self.num_attribs,
            'attribs': self.attribs,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetDrawableAttributesReplyReply':
        return GetDrawableAttributesReplyReply(**GetDrawableAttributesReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetDrawableAttributesReplyReplyPacket.pack(**self.as_dict())


class GetDrawableAttributesReplyReplyCType(ctypes.Structure):
    """glx GetDrawableAttributes_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("num_attribs", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


ChangeDrawableAttributesRequestPacket = DataPacket((
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('num_attribs', FixedDataPacketField(MARKER_UINT32)),
    ('attribs', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: (d['num_attribs']) * (2), 0)),
))


class ChangeDrawableAttributesRequest:
    OPCODE = 30

    __slots__ = ('drawable', 'num_attribs', 'attribs',)

    def __init__(
            self, *,
            drawable: Optional[int] = None,
            num_attribs: Optional[int] = None,
            attribs: Optional[Sequence[int]] = None,
    ) -> None:
        self.drawable = drawable
        self.num_attribs = num_attribs
        self.attribs = attribs

    def as_dict(self) -> Dict[str, Any]:
        return {
            'drawable': self.drawable,
            'num_attribs': self.num_attribs,
            'attribs': self.attribs,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ChangeDrawableAttributesRequest':
        return ChangeDrawableAttributesRequest(**ChangeDrawableAttributesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ChangeDrawableAttributesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ChangeDrawableAttributesRequest.lib = library.glx_changedrawableattributes
        ChangeDrawableAttributesRequest.lib.restype = ctypes.c_uint32
        ChangeDrawableAttributesRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)


class ChangeDrawableAttributesRequestCType(ctypes.Structure):
    """glx ChangeDrawableAttributes"""
    _fields_ = [
        ("drawable", ctypes.c_uint32),
        ("num_attribs", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


CreateWindowRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT32)),
    ('fbconfig', FixedDataPacketField(MARKER_UINT32)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('glx_window', FixedDataPacketField(MARKER_UINT32)),
    ('num_attribs', FixedDataPacketField(MARKER_UINT32)),
    ('attribs', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: (d['num_attribs']) * (2), 0)),
))


class CreateWindowRequest:
    OPCODE = 31

    __slots__ = ('screen', 'fbconfig', 'window', 'glx_window', 'num_attribs', 'attribs',)

    def __init__(
            self, *,
            screen: Optional[int] = None,
            fbconfig: Optional[int] = None,
            window: Optional[int] = None,
            glx_window: Optional[int] = None,
            num_attribs: Optional[int] = None,
            attribs: Optional[Sequence[int]] = None,
    ) -> None:
        self.screen = screen
        self.fbconfig = fbconfig
        self.window = window
        self.glx_window = glx_window
        self.num_attribs = num_attribs
        self.attribs = attribs

    def as_dict(self) -> Dict[str, Any]:
        return {
            'screen': self.screen,
            'fbconfig': self.fbconfig,
            'window': self.window,
            'glx_window': self.glx_window,
            'num_attribs': self.num_attribs,
            'attribs': self.attribs,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateWindowRequest':
        return CreateWindowRequest(**CreateWindowRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateWindowRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateWindowRequest.lib = library.glx_createwindow
        CreateWindowRequest.lib.restype = ctypes.c_uint32
        CreateWindowRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)


class CreateWindowRequestCType(ctypes.Structure):
    """glx CreateWindow"""
    _fields_ = [
        ("screen", ctypes.c_uint32),
        ("fbconfig", ctypes.c_uint32),
        ("window", ctypes.c_uint32),
        ("glx_window", ctypes.c_uint32),
        ("num_attribs", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


DeleteWindowRequestPacket = DataPacket((
    ('glxwindow', FixedDataPacketField(MARKER_UINT32)),
))


class DeleteWindowRequest:
    OPCODE = 32

    __slots__ = ('glxwindow',)

    def __init__(
            self, *,
            glxwindow: Optional[int] = None,
    ) -> None:
        self.glxwindow = glxwindow

    def as_dict(self) -> Dict[str, Any]:
        return {
            'glxwindow': self.glxwindow,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeleteWindowRequest':
        return DeleteWindowRequest(**DeleteWindowRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeleteWindowRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        DeleteWindowRequest.lib = library.glx_deletewindow
        DeleteWindowRequest.lib.restype = ctypes.c_uint32
        DeleteWindowRequest.lib.argstype = (ctypes.c_uint32,)


class DeleteWindowRequestCType(ctypes.Structure):
    """glx DeleteWindow"""
    _fields_ = [
        ("glxwindow", ctypes.c_uint32),
    ]


SetClientInfoArbRequestPacket = DataPacket((
    ('major_version', FixedDataPacketField(MARKER_UINT32)),
    ('minor_version', FixedDataPacketField(MARKER_UINT32)),
    ('num_versions', FixedDataPacketField(MARKER_UINT32)),
    ('gl_str_len', FixedDataPacketField(MARKER_UINT32)),
    ('glx_str_len', FixedDataPacketField(MARKER_UINT32)),
    ('gl_versions', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: (d['num_versions']) * (2), 0)),
    ('gl_extension_string', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['gl_str_len'], 0)),
    ('pad0', AlignedPadDataPacketField(4)),
    ('glx_extension_string', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['glx_str_len'], 0)),
))


class SetClientInfoArbRequest:
    OPCODE = 33

    __slots__ = ('major_version', 'minor_version', 'num_versions', 'gl_str_len', 'glx_str_len', 'gl_versions', 'gl_extension_string', 'glx_extension_string',)

    def __init__(
            self, *,
            major_version: Optional[int] = None,
            minor_version: Optional[int] = None,
            num_versions: Optional[int] = None,
            gl_str_len: Optional[int] = None,
            glx_str_len: Optional[int] = None,
            gl_versions: Optional[Sequence[int]] = None,
            gl_extension_string: Optional[Sequence[int]] = None,
            glx_extension_string: Optional[Sequence[int]] = None,
    ) -> None:
        self.major_version = major_version
        self.minor_version = minor_version
        self.num_versions = num_versions
        self.gl_str_len = gl_str_len
        self.glx_str_len = glx_str_len
        self.gl_versions = gl_versions
        self.gl_extension_string = gl_extension_string
        self.glx_extension_string = glx_extension_string

    def as_dict(self) -> Dict[str, Any]:
        return {
            'major_version': self.major_version,
            'minor_version': self.minor_version,
            'num_versions': self.num_versions,
            'gl_str_len': self.gl_str_len,
            'glx_str_len': self.glx_str_len,
            'gl_versions': self.gl_versions,
            'gl_extension_string': self.gl_extension_string,
            'glx_extension_string': self.glx_extension_string,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetClientInfoArbRequest':
        return SetClientInfoArbRequest(**SetClientInfoArbRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetClientInfoArbRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, Sequence[int], Sequence[int], Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetClientInfoArbRequest.lib = library.glx_setclientinfoarb
        SetClientInfoArbRequest.lib.restype = ctypes.c_uint32
        SetClientInfoArbRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)


class SetClientInfoArbRequestCType(ctypes.Structure):
    """glx SetClientInfoARB"""
    _fields_ = [
        ("major_version", ctypes.c_uint32),
        ("minor_version", ctypes.c_uint32),
        ("num_versions", ctypes.c_uint32),
        ("gl_str_len", ctypes.c_uint32),
        ("glx_str_len", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


CreateContextAttribsArbRequestPacket = DataPacket((
    ('context', FixedDataPacketField(MARKER_UINT32)),
    ('fbconfig', FixedDataPacketField(MARKER_UINT32)),
    ('screen', FixedDataPacketField(MARKER_UINT32)),
    ('share_list', FixedDataPacketField(MARKER_UINT32)),
    ('is_direct', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
    ('num_attribs', FixedDataPacketField(MARKER_UINT32)),
    ('attribs', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: (d['num_attribs']) * (2), 0)),
))


class CreateContextAttribsArbRequest:
    OPCODE = 34

    __slots__ = ('context', 'fbconfig', 'screen', 'share_list', 'is_direct', 'num_attribs', 'attribs',)

    def __init__(
            self, *,
            context: Optional[int] = None,
            fbconfig: Optional[int] = None,
            screen: Optional[int] = None,
            share_list: Optional[int] = None,
            is_direct: Optional[bool] = None,
            num_attribs: Optional[int] = None,
            attribs: Optional[Sequence[int]] = None,
    ) -> None:
        self.context = context
        self.fbconfig = fbconfig
        self.screen = screen
        self.share_list = share_list
        self.is_direct = is_direct
        self.num_attribs = num_attribs
        self.attribs = attribs

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context': self.context,
            'fbconfig': self.fbconfig,
            'screen': self.screen,
            'share_list': self.share_list,
            'is_direct': self.is_direct,
            'num_attribs': self.num_attribs,
            'attribs': self.attribs,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateContextAttribsArbRequest':
        return CreateContextAttribsArbRequest(**CreateContextAttribsArbRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateContextAttribsArbRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, bool, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateContextAttribsArbRequest.lib = library.glx_createcontextattribsarb
        CreateContextAttribsArbRequest.lib.restype = ctypes.c_uint32
        CreateContextAttribsArbRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int8, ctypes.c_uint8 * 3, ctypes.c_uint32, ctypes.c_void_p)


class CreateContextAttribsArbRequestCType(ctypes.Structure):
    """glx CreateContextAttribsARB"""
    _fields_ = [
        ("context", ctypes.c_uint32),
        ("fbconfig", ctypes.c_uint32),
        ("screen", ctypes.c_uint32),
        ("share_list", ctypes.c_uint32),
        ("is_direct", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 3),
        ("num_attribs", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


SetClientInfo2ArbRequestPacket = DataPacket((
    ('major_version', FixedDataPacketField(MARKER_UINT32)),
    ('minor_version', FixedDataPacketField(MARKER_UINT32)),
    ('num_versions', FixedDataPacketField(MARKER_UINT32)),
    ('gl_str_len', FixedDataPacketField(MARKER_UINT32)),
    ('glx_str_len', FixedDataPacketField(MARKER_UINT32)),
    ('gl_versions', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: (d['num_versions']) * (3), 0)),
    ('gl_extension_string', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['gl_str_len'], 0)),
    ('pad0', AlignedPadDataPacketField(4)),
    ('glx_extension_string', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['glx_str_len'], 0)),
))


class SetClientInfo2ArbRequest:
    OPCODE = 35

    __slots__ = ('major_version', 'minor_version', 'num_versions', 'gl_str_len', 'glx_str_len', 'gl_versions', 'gl_extension_string', 'glx_extension_string',)

    def __init__(
            self, *,
            major_version: Optional[int] = None,
            minor_version: Optional[int] = None,
            num_versions: Optional[int] = None,
            gl_str_len: Optional[int] = None,
            glx_str_len: Optional[int] = None,
            gl_versions: Optional[Sequence[int]] = None,
            gl_extension_string: Optional[Sequence[int]] = None,
            glx_extension_string: Optional[Sequence[int]] = None,
    ) -> None:
        self.major_version = major_version
        self.minor_version = minor_version
        self.num_versions = num_versions
        self.gl_str_len = gl_str_len
        self.glx_str_len = glx_str_len
        self.gl_versions = gl_versions
        self.gl_extension_string = gl_extension_string
        self.glx_extension_string = glx_extension_string

    def as_dict(self) -> Dict[str, Any]:
        return {
            'major_version': self.major_version,
            'minor_version': self.minor_version,
            'num_versions': self.num_versions,
            'gl_str_len': self.gl_str_len,
            'glx_str_len': self.glx_str_len,
            'gl_versions': self.gl_versions,
            'gl_extension_string': self.gl_extension_string,
            'glx_extension_string': self.glx_extension_string,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetClientInfo2ArbRequest':
        return SetClientInfo2ArbRequest(**SetClientInfo2ArbRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetClientInfo2ArbRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, Sequence[int], Sequence[int], Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetClientInfo2ArbRequest.lib = library.glx_setclientinfo2arb
        SetClientInfo2ArbRequest.lib.restype = ctypes.c_uint32
        SetClientInfo2ArbRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)


class SetClientInfo2ArbRequestCType(ctypes.Structure):
    """glx SetClientInfo2ARB"""
    _fields_ = [
        ("major_version", ctypes.c_uint32),
        ("minor_version", ctypes.c_uint32),
        ("num_versions", ctypes.c_uint32),
        ("gl_str_len", ctypes.c_uint32),
        ("glx_str_len", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


NewListRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('list', FixedDataPacketField(MARKER_UINT32)),
    ('mode', FixedDataPacketField(MARKER_UINT32)),
))


class NewListRequest:
    OPCODE = 101

    __slots__ = ('context_tag', 'list', 'mode',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            list: Optional[int] = None,
            mode: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.list = list
        self.mode = mode

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'list': self.list,
            'mode': self.mode,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'NewListRequest':
        return NewListRequest(**NewListRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return NewListRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        NewListRequest.lib = library.glx_newlist
        NewListRequest.lib.restype = ctypes.c_uint32
        NewListRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class NewListRequestCType(ctypes.Structure):
    """glx NewList"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("list", ctypes.c_uint32),
        ("mode", ctypes.c_uint32),
    ]


EndListRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
))


class EndListRequest:
    OPCODE = 102

    __slots__ = ('context_tag',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'EndListRequest':
        return EndListRequest(**EndListRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return EndListRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        EndListRequest.lib = library.glx_endlist
        EndListRequest.lib.restype = ctypes.c_uint32
        EndListRequest.lib.argstype = (ctypes.c_uint32,)


class EndListRequestCType(ctypes.Structure):
    """glx EndList"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
    ]


DeleteListsRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('list', FixedDataPacketField(MARKER_UINT32)),
    ('range', FixedDataPacketField(MARKER_INT32)),
))


class DeleteListsRequest:
    OPCODE = 103

    __slots__ = ('context_tag', 'list', 'range',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            list: Optional[int] = None,
            range: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.list = list
        self.range = range

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'list': self.list,
            'range': self.range,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeleteListsRequest':
        return DeleteListsRequest(**DeleteListsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeleteListsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        DeleteListsRequest.lib = library.glx_deletelists
        DeleteListsRequest.lib.restype = ctypes.c_uint32
        DeleteListsRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int32)


class DeleteListsRequestCType(ctypes.Structure):
    """glx DeleteLists"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("list", ctypes.c_uint32),
        ("range", ctypes.c_int32),
    ]


GenListsRequestCookie = NewType('GenListsRequestCookie', ctypes.c_uint32)


GenListsRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('range', FixedDataPacketField(MARKER_INT32)),
))


class GenListsRequest:
    OPCODE = 104

    __slots__ = ('context_tag', 'range',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            range: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.range = range

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'range': self.range,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GenListsRequest':
        return GenListsRequest(**GenListsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GenListsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], GenListsRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GenListsRequest.lib = library.glx_genlists
        GenListsRequest.lib.restype = GenListsRequestCookie
        GenListsRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_int32)


class GenListsRequestCType(ctypes.Structure):
    """glx GenLists"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("range", ctypes.c_int32),
    ]


GenListsReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('ret_val', FixedDataPacketField(MARKER_UINT32)),
))


class GenListsReplyReply:
    __slots__ = ('ret_val',)

    def __init__(
            self, *,
            ret_val: Optional[int] = None,
    ) -> None:
        self.ret_val = ret_val

    def as_dict(self) -> Dict[str, Any]:
        return {
            'ret_val': self.ret_val,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GenListsReplyReply':
        return GenListsReplyReply(**GenListsReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GenListsReplyReplyPacket.pack(**self.as_dict())


class GenListsReplyReplyCType(ctypes.Structure):
    """glx GenLists_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("ret_val", ctypes.c_uint32),
    ]


FeedbackBufferRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('size', FixedDataPacketField(MARKER_INT32)),
    ('type', FixedDataPacketField(MARKER_INT32)),
))


class FeedbackBufferRequest:
    OPCODE = 105

    __slots__ = ('context_tag', 'size', 'type',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            size: Optional[int] = None,
            type: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.size = size
        self.type = type

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'size': self.size,
            'type': self.type,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'FeedbackBufferRequest':
        return FeedbackBufferRequest(**FeedbackBufferRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return FeedbackBufferRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        FeedbackBufferRequest.lib = library.glx_feedbackbuffer
        FeedbackBufferRequest.lib.restype = ctypes.c_uint32
        FeedbackBufferRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_int32, ctypes.c_int32)


class FeedbackBufferRequestCType(ctypes.Structure):
    """glx FeedbackBuffer"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("size", ctypes.c_int32),
        ("type", ctypes.c_int32),
    ]


SelectBufferRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('size', FixedDataPacketField(MARKER_INT32)),
))


class SelectBufferRequest:
    OPCODE = 106

    __slots__ = ('context_tag', 'size',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            size: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.size = size

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'size': self.size,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SelectBufferRequest':
        return SelectBufferRequest(**SelectBufferRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SelectBufferRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SelectBufferRequest.lib = library.glx_selectbuffer
        SelectBufferRequest.lib.restype = ctypes.c_uint32
        SelectBufferRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_int32)


class SelectBufferRequestCType(ctypes.Structure):
    """glx SelectBuffer"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("size", ctypes.c_int32),
    ]


RenderModeRequestCookie = NewType('RenderModeRequestCookie', ctypes.c_uint32)


RenderModeRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('mode', FixedDataPacketField(MARKER_UINT32)),
))


class RenderModeRequest:
    OPCODE = 107

    __slots__ = ('context_tag', 'mode',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            mode: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.mode = mode

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'mode': self.mode,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'RenderModeRequest':
        return RenderModeRequest(**RenderModeRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return RenderModeRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], RenderModeRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        RenderModeRequest.lib = library.glx_rendermode
        RenderModeRequest.lib.restype = RenderModeRequestCookie
        RenderModeRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class RenderModeRequestCType(ctypes.Structure):
    """glx RenderMode"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("mode", ctypes.c_uint32),
    ]


RenderModeReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('ret_val', FixedDataPacketField(MARKER_UINT32)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('new_mode', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['n'], 0)),
))


class RenderModeReplyReply:
    __slots__ = ('ret_val', 'n', 'new_mode', 'data',)

    def __init__(
            self, *,
            ret_val: Optional[int] = None,
            n: Optional[int] = None,
            new_mode: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.ret_val = ret_val
        self.n = n
        self.new_mode = new_mode
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'ret_val': self.ret_val,
            'n': self.n,
            'new_mode': self.new_mode,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'RenderModeReplyReply':
        return RenderModeReplyReply(**RenderModeReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return RenderModeReplyReplyPacket.pack(**self.as_dict())


class RenderModeReplyReplyCType(ctypes.Structure):
    """glx RenderMode_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("ret_val", ctypes.c_uint32),
        ("n", ctypes.c_uint32),
        ("new_mode", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


FinishRequestCookie = NewType('FinishRequestCookie', ctypes.c_uint32)


FinishRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
))


class FinishRequest:
    OPCODE = 108

    __slots__ = ('context_tag',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'FinishRequest':
        return FinishRequest(**FinishRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return FinishRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], FinishRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        FinishRequest.lib = library.glx_finish
        FinishRequest.lib.restype = FinishRequestCookie
        FinishRequest.lib.argstype = (ctypes.c_uint32,)


class FinishRequestCType(ctypes.Structure):
    """glx Finish"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
    ]


FinishReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
))


class FinishReplyReply:
    __slots__ = (,)

    def __init__(
            self, *,
    ) -> None:

    def as_dict(self) -> Dict[str, Any]:
        return {
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'FinishReplyReply':
        return FinishReplyReply(**FinishReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return FinishReplyReplyPacket.pack(**self.as_dict())


class FinishReplyReplyCType(ctypes.Structure):
    """glx Finish_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
    ]


PixelStorefRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('pname', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_UINT32)),
))


class PixelStorefRequest:
    OPCODE = 109

    __slots__ = ('context_tag', 'pname', 'datum',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            pname: Optional[int] = None,
            datum: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.pname = pname
        self.datum = datum

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'pname': self.pname,
            'datum': self.datum,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PixelStorefRequest':
        return PixelStorefRequest(**PixelStorefRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PixelStorefRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PixelStorefRequest.lib = library.glx_pixelstoref
        PixelStorefRequest.lib.restype = ctypes.c_uint32
        PixelStorefRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class PixelStorefRequestCType(ctypes.Structure):
    """glx PixelStoref"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("pname", ctypes.c_uint32),
        ("datum", ctypes.c_uint32),
    ]


PixelStoreiRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('pname', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_INT32)),
))


class PixelStoreiRequest:
    OPCODE = 110

    __slots__ = ('context_tag', 'pname', 'datum',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            pname: Optional[int] = None,
            datum: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.pname = pname
        self.datum = datum

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'pname': self.pname,
            'datum': self.datum,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PixelStoreiRequest':
        return PixelStoreiRequest(**PixelStoreiRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PixelStoreiRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PixelStoreiRequest.lib = library.glx_pixelstorei
        PixelStoreiRequest.lib.restype = ctypes.c_uint32
        PixelStoreiRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int32)


class PixelStoreiRequestCType(ctypes.Structure):
    """glx PixelStorei"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("pname", ctypes.c_uint32),
        ("datum", ctypes.c_int32),
    ]


ReadPixelsRequestCookie = NewType('ReadPixelsRequestCookie', ctypes.c_uint32)


ReadPixelsRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('x', FixedDataPacketField(MARKER_INT32)),
    ('y', FixedDataPacketField(MARKER_INT32)),
    ('width', FixedDataPacketField(MARKER_INT32)),
    ('height', FixedDataPacketField(MARKER_INT32)),
    ('format', FixedDataPacketField(MARKER_UINT32)),
    ('type', FixedDataPacketField(MARKER_UINT32)),
    ('swap_bytes', FixedDataPacketField(MARKER_UINT8)),
    ('lsb_first', FixedDataPacketField(MARKER_UINT8)),
))


class ReadPixelsRequest:
    OPCODE = 111

    __slots__ = ('context_tag', 'x', 'y', 'width', 'height', 'format', 'type', 'swap_bytes', 'lsb_first',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            x: Optional[int] = None,
            y: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            format: Optional[int] = None,
            type: Optional[int] = None,
            swap_bytes: Optional[bool] = None,
            lsb_first: Optional[bool] = None,
    ) -> None:
        self.context_tag = context_tag
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.format = format
        self.type = type
        self.swap_bytes = swap_bytes
        self.lsb_first = lsb_first

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height,
            'format': self.format,
            'type': self.type,
            'swap_bytes': self.swap_bytes,
            'lsb_first': self.lsb_first,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ReadPixelsRequest':
        return ReadPixelsRequest(**ReadPixelsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ReadPixelsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, bool, bool], ReadPixelsRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ReadPixelsRequest.lib = library.glx_readpixels
        ReadPixelsRequest.lib.restype = ReadPixelsRequestCookie
        ReadPixelsRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_int32, ctypes.c_int32, ctypes.c_int32, ctypes.c_int32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int8, ctypes.c_int8)


class ReadPixelsRequestCType(ctypes.Structure):
    """glx ReadPixels"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("x", ctypes.c_int32),
        ("y", ctypes.c_int32),
        ("width", ctypes.c_int32),
        ("height", ctypes.c_int32),
        ("format", ctypes.c_uint32),
        ("type", ctypes.c_uint32),
        ("swap_bytes", ctypes.c_int8),
        ("lsb_first", ctypes.c_int8),
    ]


ReadPixelsReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(24)),
    ('data', SimpleListDataPacketField(MARKER_INT8, lambda d, c: (d['length']) * (4), 0)),
))


class ReadPixelsReplyReply:
    __slots__ = ('data',)

    def __init__(
            self, *,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ReadPixelsReplyReply':
        return ReadPixelsReplyReply(**ReadPixelsReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ReadPixelsReplyReplyPacket.pack(**self.as_dict())


class ReadPixelsReplyReplyCType(ctypes.Structure):
    """glx ReadPixels_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 24),
        ("var_data", ctypes.c_void_p),
    ]


GetBooleanvRequestCookie = NewType('GetBooleanvRequestCookie', ctypes.c_uint32)


GetBooleanvRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('pname', FixedDataPacketField(MARKER_INT32)),
))


class GetBooleanvRequest:
    OPCODE = 112

    __slots__ = ('context_tag', 'pname',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            pname: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.pname = pname

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'pname': self.pname,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetBooleanvRequest':
        return GetBooleanvRequest(**GetBooleanvRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetBooleanvRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], GetBooleanvRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetBooleanvRequest.lib = library.glx_getbooleanv
        GetBooleanvRequest.lib.restype = GetBooleanvRequestCookie
        GetBooleanvRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_int32)


class GetBooleanvRequestCType(ctypes.Structure):
    """glx GetBooleanv"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("pname", ctypes.c_int32),
    ]


GetBooleanvReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_UINT8)),
    ('pad2', FixedPadDataPacketField(15)),
    ('data', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: d['n'], 0)),
))


class GetBooleanvReplyReply:
    __slots__ = ('n', 'datum', 'data',)

    def __init__(
            self, *,
            n: Optional[int] = None,
            datum: Optional[bool] = None,
            data: Optional[Sequence[bool]] = None,
    ) -> None:
        self.n = n
        self.datum = datum
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
            'datum': self.datum,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetBooleanvReplyReply':
        return GetBooleanvReplyReply(**GetBooleanvReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetBooleanvReplyReplyPacket.pack(**self.as_dict())


class GetBooleanvReplyReplyCType(ctypes.Structure):
    """glx GetBooleanv_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("datum", ctypes.c_int8),
        ("pad2", ctypes.c_uint8 * 15),
        ("var_data", ctypes.c_void_p),
    ]


GetClipPlaneRequestCookie = NewType('GetClipPlaneRequestCookie', ctypes.c_uint32)


GetClipPlaneRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('plane', FixedDataPacketField(MARKER_INT32)),
))


class GetClipPlaneRequest:
    OPCODE = 113

    __slots__ = ('context_tag', 'plane',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            plane: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.plane = plane

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'plane': self.plane,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetClipPlaneRequest':
        return GetClipPlaneRequest(**GetClipPlaneRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetClipPlaneRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], GetClipPlaneRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetClipPlaneRequest.lib = library.glx_getclipplane
        GetClipPlaneRequest.lib.restype = GetClipPlaneRequestCookie
        GetClipPlaneRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_int32)


class GetClipPlaneRequestCType(ctypes.Structure):
    """glx GetClipPlane"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("plane", ctypes.c_int32),
    ]


GetClipPlaneReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(24)),
    ('data', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: (d['length']) / (2), 0)),
))


class GetClipPlaneReplyReply:
    __slots__ = ('data',)

    def __init__(
            self, *,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetClipPlaneReplyReply':
        return GetClipPlaneReplyReply(**GetClipPlaneReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetClipPlaneReplyReplyPacket.pack(**self.as_dict())


class GetClipPlaneReplyReplyCType(ctypes.Structure):
    """glx GetClipPlane_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 24),
        ("var_data", ctypes.c_void_p),
    ]


GetDoublevRequestCookie = NewType('GetDoublevRequestCookie', ctypes.c_uint32)


GetDoublevRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('pname', FixedDataPacketField(MARKER_UINT32)),
))


class GetDoublevRequest:
    OPCODE = 114

    __slots__ = ('context_tag', 'pname',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            pname: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.pname = pname

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'pname': self.pname,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetDoublevRequest':
        return GetDoublevRequest(**GetDoublevRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetDoublevRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], GetDoublevRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetDoublevRequest.lib = library.glx_getdoublev
        GetDoublevRequest.lib.restype = GetDoublevRequestCookie
        GetDoublevRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class GetDoublevRequestCType(ctypes.Structure):
    """glx GetDoublev"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("pname", ctypes.c_uint32),
    ]


GetDoublevReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_UINT32)),
    ('pad2', FixedPadDataPacketField(8)),
    ('data', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['n'], 0)),
))


class GetDoublevReplyReply:
    __slots__ = ('n', 'datum', 'data',)

    def __init__(
            self, *,
            n: Optional[int] = None,
            datum: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.n = n
        self.datum = datum
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
            'datum': self.datum,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetDoublevReplyReply':
        return GetDoublevReplyReply(**GetDoublevReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetDoublevReplyReplyPacket.pack(**self.as_dict())


class GetDoublevReplyReplyCType(ctypes.Structure):
    """glx GetDoublev_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("datum", ctypes.c_uint32),
        ("pad2", ctypes.c_uint8 * 8),
        ("var_data", ctypes.c_void_p),
    ]


GetErrorRequestCookie = NewType('GetErrorRequestCookie', ctypes.c_uint32)


GetErrorRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
))


class GetErrorRequest:
    OPCODE = 115

    __slots__ = ('context_tag',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetErrorRequest':
        return GetErrorRequest(**GetErrorRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetErrorRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetErrorRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetErrorRequest.lib = library.glx_geterror
        GetErrorRequest.lib.restype = GetErrorRequestCookie
        GetErrorRequest.lib.argstype = (ctypes.c_uint32,)


class GetErrorRequestCType(ctypes.Structure):
    """glx GetError"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
    ]


GetErrorReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('error', FixedDataPacketField(MARKER_INT32)),
))


class GetErrorReplyReply:
    __slots__ = ('error',)

    def __init__(
            self, *,
            error: Optional[int] = None,
    ) -> None:
        self.error = error

    def as_dict(self) -> Dict[str, Any]:
        return {
            'error': self.error,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetErrorReplyReply':
        return GetErrorReplyReply(**GetErrorReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetErrorReplyReplyPacket.pack(**self.as_dict())


class GetErrorReplyReplyCType(ctypes.Structure):
    """glx GetError_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("error", ctypes.c_int32),
    ]


GetFloatvRequestCookie = NewType('GetFloatvRequestCookie', ctypes.c_uint32)


GetFloatvRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('pname', FixedDataPacketField(MARKER_UINT32)),
))


class GetFloatvRequest:
    OPCODE = 116

    __slots__ = ('context_tag', 'pname',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            pname: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.pname = pname

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'pname': self.pname,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetFloatvRequest':
        return GetFloatvRequest(**GetFloatvRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetFloatvRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], GetFloatvRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetFloatvRequest.lib = library.glx_getfloatv
        GetFloatvRequest.lib.restype = GetFloatvRequestCookie
        GetFloatvRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class GetFloatvRequestCType(ctypes.Structure):
    """glx GetFloatv"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("pname", ctypes.c_uint32),
    ]


GetFloatvReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_UINT32)),
    ('pad2', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['n'], 0)),
))


class GetFloatvReplyReply:
    __slots__ = ('n', 'datum', 'data',)

    def __init__(
            self, *,
            n: Optional[int] = None,
            datum: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.n = n
        self.datum = datum
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
            'datum': self.datum,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetFloatvReplyReply':
        return GetFloatvReplyReply(**GetFloatvReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetFloatvReplyReplyPacket.pack(**self.as_dict())


class GetFloatvReplyReplyCType(ctypes.Structure):
    """glx GetFloatv_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("datum", ctypes.c_uint32),
        ("pad2", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


GetIntegervRequestCookie = NewType('GetIntegervRequestCookie', ctypes.c_uint32)


GetIntegervRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('pname', FixedDataPacketField(MARKER_UINT32)),
))


class GetIntegervRequest:
    OPCODE = 117

    __slots__ = ('context_tag', 'pname',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            pname: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.pname = pname

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'pname': self.pname,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetIntegervRequest':
        return GetIntegervRequest(**GetIntegervRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetIntegervRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], GetIntegervRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetIntegervRequest.lib = library.glx_getintegerv
        GetIntegervRequest.lib.restype = GetIntegervRequestCookie
        GetIntegervRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class GetIntegervRequestCType(ctypes.Structure):
    """glx GetIntegerv"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("pname", ctypes.c_uint32),
    ]


GetIntegervReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_INT32)),
    ('pad2', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_INT32, lambda d, c: d['n'], 0)),
))


class GetIntegervReplyReply:
    __slots__ = ('n', 'datum', 'data',)

    def __init__(
            self, *,
            n: Optional[int] = None,
            datum: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.n = n
        self.datum = datum
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
            'datum': self.datum,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetIntegervReplyReply':
        return GetIntegervReplyReply(**GetIntegervReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetIntegervReplyReplyPacket.pack(**self.as_dict())


class GetIntegervReplyReplyCType(ctypes.Structure):
    """glx GetIntegerv_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("datum", ctypes.c_int32),
        ("pad2", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


GetLightfvRequestCookie = NewType('GetLightfvRequestCookie', ctypes.c_uint32)


GetLightfvRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('light', FixedDataPacketField(MARKER_UINT32)),
    ('pname', FixedDataPacketField(MARKER_UINT32)),
))


class GetLightfvRequest:
    OPCODE = 118

    __slots__ = ('context_tag', 'light', 'pname',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            light: Optional[int] = None,
            pname: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.light = light
        self.pname = pname

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'light': self.light,
            'pname': self.pname,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetLightfvRequest':
        return GetLightfvRequest(**GetLightfvRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetLightfvRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], GetLightfvRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetLightfvRequest.lib = library.glx_getlightfv
        GetLightfvRequest.lib.restype = GetLightfvRequestCookie
        GetLightfvRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class GetLightfvRequestCType(ctypes.Structure):
    """glx GetLightfv"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("light", ctypes.c_uint32),
        ("pname", ctypes.c_uint32),
    ]


GetLightfvReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_UINT32)),
    ('pad2', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['n'], 0)),
))


class GetLightfvReplyReply:
    __slots__ = ('n', 'datum', 'data',)

    def __init__(
            self, *,
            n: Optional[int] = None,
            datum: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.n = n
        self.datum = datum
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
            'datum': self.datum,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetLightfvReplyReply':
        return GetLightfvReplyReply(**GetLightfvReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetLightfvReplyReplyPacket.pack(**self.as_dict())


class GetLightfvReplyReplyCType(ctypes.Structure):
    """glx GetLightfv_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("datum", ctypes.c_uint32),
        ("pad2", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


GetLightivRequestCookie = NewType('GetLightivRequestCookie', ctypes.c_uint32)


GetLightivRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('light', FixedDataPacketField(MARKER_UINT32)),
    ('pname', FixedDataPacketField(MARKER_UINT32)),
))


class GetLightivRequest:
    OPCODE = 119

    __slots__ = ('context_tag', 'light', 'pname',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            light: Optional[int] = None,
            pname: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.light = light
        self.pname = pname

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'light': self.light,
            'pname': self.pname,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetLightivRequest':
        return GetLightivRequest(**GetLightivRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetLightivRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], GetLightivRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetLightivRequest.lib = library.glx_getlightiv
        GetLightivRequest.lib.restype = GetLightivRequestCookie
        GetLightivRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class GetLightivRequestCType(ctypes.Structure):
    """glx GetLightiv"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("light", ctypes.c_uint32),
        ("pname", ctypes.c_uint32),
    ]


GetLightivReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_INT32)),
    ('pad2', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_INT32, lambda d, c: d['n'], 0)),
))


class GetLightivReplyReply:
    __slots__ = ('n', 'datum', 'data',)

    def __init__(
            self, *,
            n: Optional[int] = None,
            datum: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.n = n
        self.datum = datum
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
            'datum': self.datum,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetLightivReplyReply':
        return GetLightivReplyReply(**GetLightivReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetLightivReplyReplyPacket.pack(**self.as_dict())


class GetLightivReplyReplyCType(ctypes.Structure):
    """glx GetLightiv_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("datum", ctypes.c_int32),
        ("pad2", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


GetMapdvRequestCookie = NewType('GetMapdvRequestCookie', ctypes.c_uint32)


GetMapdvRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('target', FixedDataPacketField(MARKER_UINT32)),
    ('query', FixedDataPacketField(MARKER_UINT32)),
))


class GetMapdvRequest:
    OPCODE = 120

    __slots__ = ('context_tag', 'target', 'query',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            target: Optional[int] = None,
            query: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.target = target
        self.query = query

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'target': self.target,
            'query': self.query,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetMapdvRequest':
        return GetMapdvRequest(**GetMapdvRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetMapdvRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], GetMapdvRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetMapdvRequest.lib = library.glx_getmapdv
        GetMapdvRequest.lib.restype = GetMapdvRequestCookie
        GetMapdvRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class GetMapdvRequestCType(ctypes.Structure):
    """glx GetMapdv"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("target", ctypes.c_uint32),
        ("query", ctypes.c_uint32),
    ]


GetMapdvReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_UINT32)),
    ('pad2', FixedPadDataPacketField(8)),
    ('data', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['n'], 0)),
))


class GetMapdvReplyReply:
    __slots__ = ('n', 'datum', 'data',)

    def __init__(
            self, *,
            n: Optional[int] = None,
            datum: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.n = n
        self.datum = datum
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
            'datum': self.datum,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetMapdvReplyReply':
        return GetMapdvReplyReply(**GetMapdvReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetMapdvReplyReplyPacket.pack(**self.as_dict())


class GetMapdvReplyReplyCType(ctypes.Structure):
    """glx GetMapdv_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("datum", ctypes.c_uint32),
        ("pad2", ctypes.c_uint8 * 8),
        ("var_data", ctypes.c_void_p),
    ]


GetMapfvRequestCookie = NewType('GetMapfvRequestCookie', ctypes.c_uint32)


GetMapfvRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('target', FixedDataPacketField(MARKER_UINT32)),
    ('query', FixedDataPacketField(MARKER_UINT32)),
))


class GetMapfvRequest:
    OPCODE = 121

    __slots__ = ('context_tag', 'target', 'query',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            target: Optional[int] = None,
            query: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.target = target
        self.query = query

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'target': self.target,
            'query': self.query,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetMapfvRequest':
        return GetMapfvRequest(**GetMapfvRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetMapfvRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], GetMapfvRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetMapfvRequest.lib = library.glx_getmapfv
        GetMapfvRequest.lib.restype = GetMapfvRequestCookie
        GetMapfvRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class GetMapfvRequestCType(ctypes.Structure):
    """glx GetMapfv"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("target", ctypes.c_uint32),
        ("query", ctypes.c_uint32),
    ]


GetMapfvReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_UINT32)),
    ('pad2', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['n'], 0)),
))


class GetMapfvReplyReply:
    __slots__ = ('n', 'datum', 'data',)

    def __init__(
            self, *,
            n: Optional[int] = None,
            datum: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.n = n
        self.datum = datum
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
            'datum': self.datum,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetMapfvReplyReply':
        return GetMapfvReplyReply(**GetMapfvReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetMapfvReplyReplyPacket.pack(**self.as_dict())


class GetMapfvReplyReplyCType(ctypes.Structure):
    """glx GetMapfv_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("datum", ctypes.c_uint32),
        ("pad2", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


GetMapivRequestCookie = NewType('GetMapivRequestCookie', ctypes.c_uint32)


GetMapivRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('target', FixedDataPacketField(MARKER_UINT32)),
    ('query', FixedDataPacketField(MARKER_UINT32)),
))


class GetMapivRequest:
    OPCODE = 122

    __slots__ = ('context_tag', 'target', 'query',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            target: Optional[int] = None,
            query: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.target = target
        self.query = query

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'target': self.target,
            'query': self.query,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetMapivRequest':
        return GetMapivRequest(**GetMapivRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetMapivRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], GetMapivRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetMapivRequest.lib = library.glx_getmapiv
        GetMapivRequest.lib.restype = GetMapivRequestCookie
        GetMapivRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class GetMapivRequestCType(ctypes.Structure):
    """glx GetMapiv"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("target", ctypes.c_uint32),
        ("query", ctypes.c_uint32),
    ]


GetMapivReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_INT32)),
    ('pad2', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_INT32, lambda d, c: d['n'], 0)),
))


class GetMapivReplyReply:
    __slots__ = ('n', 'datum', 'data',)

    def __init__(
            self, *,
            n: Optional[int] = None,
            datum: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.n = n
        self.datum = datum
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
            'datum': self.datum,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetMapivReplyReply':
        return GetMapivReplyReply(**GetMapivReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetMapivReplyReplyPacket.pack(**self.as_dict())


class GetMapivReplyReplyCType(ctypes.Structure):
    """glx GetMapiv_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("datum", ctypes.c_int32),
        ("pad2", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


GetMaterialfvRequestCookie = NewType('GetMaterialfvRequestCookie', ctypes.c_uint32)


GetMaterialfvRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('face', FixedDataPacketField(MARKER_UINT32)),
    ('pname', FixedDataPacketField(MARKER_UINT32)),
))


class GetMaterialfvRequest:
    OPCODE = 123

    __slots__ = ('context_tag', 'face', 'pname',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            face: Optional[int] = None,
            pname: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.face = face
        self.pname = pname

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'face': self.face,
            'pname': self.pname,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetMaterialfvRequest':
        return GetMaterialfvRequest(**GetMaterialfvRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetMaterialfvRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], GetMaterialfvRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetMaterialfvRequest.lib = library.glx_getmaterialfv
        GetMaterialfvRequest.lib.restype = GetMaterialfvRequestCookie
        GetMaterialfvRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class GetMaterialfvRequestCType(ctypes.Structure):
    """glx GetMaterialfv"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("face", ctypes.c_uint32),
        ("pname", ctypes.c_uint32),
    ]


GetMaterialfvReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_UINT32)),
    ('pad2', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['n'], 0)),
))


class GetMaterialfvReplyReply:
    __slots__ = ('n', 'datum', 'data',)

    def __init__(
            self, *,
            n: Optional[int] = None,
            datum: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.n = n
        self.datum = datum
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
            'datum': self.datum,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetMaterialfvReplyReply':
        return GetMaterialfvReplyReply(**GetMaterialfvReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetMaterialfvReplyReplyPacket.pack(**self.as_dict())


class GetMaterialfvReplyReplyCType(ctypes.Structure):
    """glx GetMaterialfv_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("datum", ctypes.c_uint32),
        ("pad2", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


GetMaterialivRequestCookie = NewType('GetMaterialivRequestCookie', ctypes.c_uint32)


GetMaterialivRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('face', FixedDataPacketField(MARKER_UINT32)),
    ('pname', FixedDataPacketField(MARKER_UINT32)),
))


class GetMaterialivRequest:
    OPCODE = 124

    __slots__ = ('context_tag', 'face', 'pname',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            face: Optional[int] = None,
            pname: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.face = face
        self.pname = pname

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'face': self.face,
            'pname': self.pname,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetMaterialivRequest':
        return GetMaterialivRequest(**GetMaterialivRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetMaterialivRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], GetMaterialivRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetMaterialivRequest.lib = library.glx_getmaterialiv
        GetMaterialivRequest.lib.restype = GetMaterialivRequestCookie
        GetMaterialivRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class GetMaterialivRequestCType(ctypes.Structure):
    """glx GetMaterialiv"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("face", ctypes.c_uint32),
        ("pname", ctypes.c_uint32),
    ]


GetMaterialivReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_INT32)),
    ('pad2', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_INT32, lambda d, c: d['n'], 0)),
))


class GetMaterialivReplyReply:
    __slots__ = ('n', 'datum', 'data',)

    def __init__(
            self, *,
            n: Optional[int] = None,
            datum: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.n = n
        self.datum = datum
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
            'datum': self.datum,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetMaterialivReplyReply':
        return GetMaterialivReplyReply(**GetMaterialivReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetMaterialivReplyReplyPacket.pack(**self.as_dict())


class GetMaterialivReplyReplyCType(ctypes.Structure):
    """glx GetMaterialiv_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("datum", ctypes.c_int32),
        ("pad2", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


GetPixelMapfvRequestCookie = NewType('GetPixelMapfvRequestCookie', ctypes.c_uint32)


GetPixelMapfvRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('map', FixedDataPacketField(MARKER_UINT32)),
))


class GetPixelMapfvRequest:
    OPCODE = 125

    __slots__ = ('context_tag', 'map',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            map: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.map = map

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'map': self.map,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetPixelMapfvRequest':
        return GetPixelMapfvRequest(**GetPixelMapfvRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetPixelMapfvRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], GetPixelMapfvRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetPixelMapfvRequest.lib = library.glx_getpixelmapfv
        GetPixelMapfvRequest.lib.restype = GetPixelMapfvRequestCookie
        GetPixelMapfvRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class GetPixelMapfvRequestCType(ctypes.Structure):
    """glx GetPixelMapfv"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("map", ctypes.c_uint32),
    ]


GetPixelMapfvReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_UINT32)),
    ('pad2', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['n'], 0)),
))


class GetPixelMapfvReplyReply:
    __slots__ = ('n', 'datum', 'data',)

    def __init__(
            self, *,
            n: Optional[int] = None,
            datum: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.n = n
        self.datum = datum
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
            'datum': self.datum,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetPixelMapfvReplyReply':
        return GetPixelMapfvReplyReply(**GetPixelMapfvReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetPixelMapfvReplyReplyPacket.pack(**self.as_dict())


class GetPixelMapfvReplyReplyCType(ctypes.Structure):
    """glx GetPixelMapfv_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("datum", ctypes.c_uint32),
        ("pad2", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


GetPixelMapuivRequestCookie = NewType('GetPixelMapuivRequestCookie', ctypes.c_uint32)


GetPixelMapuivRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('map', FixedDataPacketField(MARKER_UINT32)),
))


class GetPixelMapuivRequest:
    OPCODE = 126

    __slots__ = ('context_tag', 'map',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            map: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.map = map

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'map': self.map,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetPixelMapuivRequest':
        return GetPixelMapuivRequest(**GetPixelMapuivRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetPixelMapuivRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], GetPixelMapuivRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetPixelMapuivRequest.lib = library.glx_getpixelmapuiv
        GetPixelMapuivRequest.lib.restype = GetPixelMapuivRequestCookie
        GetPixelMapuivRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class GetPixelMapuivRequestCType(ctypes.Structure):
    """glx GetPixelMapuiv"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("map", ctypes.c_uint32),
    ]


GetPixelMapuivReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_UINT32)),
    ('pad2', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['n'], 0)),
))


class GetPixelMapuivReplyReply:
    __slots__ = ('n', 'datum', 'data',)

    def __init__(
            self, *,
            n: Optional[int] = None,
            datum: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.n = n
        self.datum = datum
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
            'datum': self.datum,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetPixelMapuivReplyReply':
        return GetPixelMapuivReplyReply(**GetPixelMapuivReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetPixelMapuivReplyReplyPacket.pack(**self.as_dict())


class GetPixelMapuivReplyReplyCType(ctypes.Structure):
    """glx GetPixelMapuiv_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("datum", ctypes.c_uint32),
        ("pad2", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


GetPixelMapusvRequestCookie = NewType('GetPixelMapusvRequestCookie', ctypes.c_uint32)


GetPixelMapusvRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('map', FixedDataPacketField(MARKER_UINT32)),
))


class GetPixelMapusvRequest:
    OPCODE = 127

    __slots__ = ('context_tag', 'map',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            map: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.map = map

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'map': self.map,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetPixelMapusvRequest':
        return GetPixelMapusvRequest(**GetPixelMapusvRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetPixelMapusvRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], GetPixelMapusvRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetPixelMapusvRequest.lib = library.glx_getpixelmapusv
        GetPixelMapusvRequest.lib.restype = GetPixelMapusvRequestCookie
        GetPixelMapusvRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class GetPixelMapusvRequestCType(ctypes.Structure):
    """glx GetPixelMapusv"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("map", ctypes.c_uint32),
    ]


GetPixelMapusvReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_UINT16)),
    ('pad2', FixedPadDataPacketField(16)),
    ('data', SimpleListDataPacketField(MARKER_UINT16, lambda d, c: d['n'], 0)),
))


class GetPixelMapusvReplyReply:
    __slots__ = ('n', 'datum', 'data',)

    def __init__(
            self, *,
            n: Optional[int] = None,
            datum: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.n = n
        self.datum = datum
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
            'datum': self.datum,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetPixelMapusvReplyReply':
        return GetPixelMapusvReplyReply(**GetPixelMapusvReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetPixelMapusvReplyReplyPacket.pack(**self.as_dict())


class GetPixelMapusvReplyReplyCType(ctypes.Structure):
    """glx GetPixelMapusv_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("datum", ctypes.c_uint16),
        ("pad2", ctypes.c_uint8 * 16),
        ("var_data", ctypes.c_void_p),
    ]


GetPolygonStippleRequestCookie = NewType('GetPolygonStippleRequestCookie', ctypes.c_uint32)


GetPolygonStippleRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('lsb_first', FixedDataPacketField(MARKER_UINT8)),
))


class GetPolygonStippleRequest:
    OPCODE = 128

    __slots__ = ('context_tag', 'lsb_first',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            lsb_first: Optional[bool] = None,
    ) -> None:
        self.context_tag = context_tag
        self.lsb_first = lsb_first

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'lsb_first': self.lsb_first,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetPolygonStippleRequest':
        return GetPolygonStippleRequest(**GetPolygonStippleRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetPolygonStippleRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, bool], GetPolygonStippleRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetPolygonStippleRequest.lib = library.glx_getpolygonstipple
        GetPolygonStippleRequest.lib.restype = GetPolygonStippleRequestCookie
        GetPolygonStippleRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_int8)


class GetPolygonStippleRequestCType(ctypes.Structure):
    """glx GetPolygonStipple"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("lsb_first", ctypes.c_int8),
    ]


GetPolygonStippleReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(24)),
    ('data', SimpleListDataPacketField(MARKER_INT8, lambda d, c: (d['length']) * (4), 0)),
))


class GetPolygonStippleReplyReply:
    __slots__ = ('data',)

    def __init__(
            self, *,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetPolygonStippleReplyReply':
        return GetPolygonStippleReplyReply(**GetPolygonStippleReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetPolygonStippleReplyReplyPacket.pack(**self.as_dict())


class GetPolygonStippleReplyReplyCType(ctypes.Structure):
    """glx GetPolygonStipple_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 24),
        ("var_data", ctypes.c_void_p),
    ]


GetStringRequestCookie = NewType('GetStringRequestCookie', ctypes.c_uint32)


GetStringRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('name', FixedDataPacketField(MARKER_UINT32)),
))


class GetStringRequest:
    OPCODE = 129

    __slots__ = ('context_tag', 'name',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            name: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.name = name

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'name': self.name,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetStringRequest':
        return GetStringRequest(**GetStringRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetStringRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], GetStringRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetStringRequest.lib = library.glx_getstring
        GetStringRequest.lib.restype = GetStringRequestCookie
        GetStringRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class GetStringRequestCType(ctypes.Structure):
    """glx GetString"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("name", ctypes.c_uint32),
    ]


GetStringReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('pad2', FixedPadDataPacketField(16)),
    ('string', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['n'], 0)),
))


class GetStringReplyReply:
    __slots__ = ('n', 'string',)

    def __init__(
            self, *,
            n: Optional[int] = None,
            string: Optional[Sequence[int]] = None,
    ) -> None:
        self.n = n
        self.string = string

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
            'string': self.string,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetStringReplyReply':
        return GetStringReplyReply(**GetStringReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetStringReplyReplyPacket.pack(**self.as_dict())


class GetStringReplyReplyCType(ctypes.Structure):
    """glx GetString_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("pad2", ctypes.c_uint8 * 16),
        ("var_data", ctypes.c_void_p),
    ]


GetTexEnvfvRequestCookie = NewType('GetTexEnvfvRequestCookie', ctypes.c_uint32)


GetTexEnvfvRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('target', FixedDataPacketField(MARKER_UINT32)),
    ('pname', FixedDataPacketField(MARKER_UINT32)),
))


class GetTexEnvfvRequest:
    OPCODE = 130

    __slots__ = ('context_tag', 'target', 'pname',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            target: Optional[int] = None,
            pname: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.target = target
        self.pname = pname

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'target': self.target,
            'pname': self.pname,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetTexEnvfvRequest':
        return GetTexEnvfvRequest(**GetTexEnvfvRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetTexEnvfvRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], GetTexEnvfvRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetTexEnvfvRequest.lib = library.glx_gettexenvfv
        GetTexEnvfvRequest.lib.restype = GetTexEnvfvRequestCookie
        GetTexEnvfvRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class GetTexEnvfvRequestCType(ctypes.Structure):
    """glx GetTexEnvfv"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("target", ctypes.c_uint32),
        ("pname", ctypes.c_uint32),
    ]


GetTexEnvfvReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_UINT32)),
    ('pad2', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['n'], 0)),
))


class GetTexEnvfvReplyReply:
    __slots__ = ('n', 'datum', 'data',)

    def __init__(
            self, *,
            n: Optional[int] = None,
            datum: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.n = n
        self.datum = datum
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
            'datum': self.datum,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetTexEnvfvReplyReply':
        return GetTexEnvfvReplyReply(**GetTexEnvfvReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetTexEnvfvReplyReplyPacket.pack(**self.as_dict())


class GetTexEnvfvReplyReplyCType(ctypes.Structure):
    """glx GetTexEnvfv_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("datum", ctypes.c_uint32),
        ("pad2", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


GetTexEnvivRequestCookie = NewType('GetTexEnvivRequestCookie', ctypes.c_uint32)


GetTexEnvivRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('target', FixedDataPacketField(MARKER_UINT32)),
    ('pname', FixedDataPacketField(MARKER_UINT32)),
))


class GetTexEnvivRequest:
    OPCODE = 131

    __slots__ = ('context_tag', 'target', 'pname',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            target: Optional[int] = None,
            pname: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.target = target
        self.pname = pname

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'target': self.target,
            'pname': self.pname,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetTexEnvivRequest':
        return GetTexEnvivRequest(**GetTexEnvivRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetTexEnvivRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], GetTexEnvivRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetTexEnvivRequest.lib = library.glx_gettexenviv
        GetTexEnvivRequest.lib.restype = GetTexEnvivRequestCookie
        GetTexEnvivRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class GetTexEnvivRequestCType(ctypes.Structure):
    """glx GetTexEnviv"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("target", ctypes.c_uint32),
        ("pname", ctypes.c_uint32),
    ]


GetTexEnvivReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_INT32)),
    ('pad2', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_INT32, lambda d, c: d['n'], 0)),
))


class GetTexEnvivReplyReply:
    __slots__ = ('n', 'datum', 'data',)

    def __init__(
            self, *,
            n: Optional[int] = None,
            datum: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.n = n
        self.datum = datum
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
            'datum': self.datum,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetTexEnvivReplyReply':
        return GetTexEnvivReplyReply(**GetTexEnvivReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetTexEnvivReplyReplyPacket.pack(**self.as_dict())


class GetTexEnvivReplyReplyCType(ctypes.Structure):
    """glx GetTexEnviv_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("datum", ctypes.c_int32),
        ("pad2", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


GetTexGendvRequestCookie = NewType('GetTexGendvRequestCookie', ctypes.c_uint32)


GetTexGendvRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('coord', FixedDataPacketField(MARKER_UINT32)),
    ('pname', FixedDataPacketField(MARKER_UINT32)),
))


class GetTexGendvRequest:
    OPCODE = 132

    __slots__ = ('context_tag', 'coord', 'pname',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            coord: Optional[int] = None,
            pname: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.coord = coord
        self.pname = pname

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'coord': self.coord,
            'pname': self.pname,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetTexGendvRequest':
        return GetTexGendvRequest(**GetTexGendvRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetTexGendvRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], GetTexGendvRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetTexGendvRequest.lib = library.glx_gettexgendv
        GetTexGendvRequest.lib.restype = GetTexGendvRequestCookie
        GetTexGendvRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class GetTexGendvRequestCType(ctypes.Structure):
    """glx GetTexGendv"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("coord", ctypes.c_uint32),
        ("pname", ctypes.c_uint32),
    ]


GetTexGendvReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_UINT32)),
    ('pad2', FixedPadDataPacketField(8)),
    ('data', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['n'], 0)),
))


class GetTexGendvReplyReply:
    __slots__ = ('n', 'datum', 'data',)

    def __init__(
            self, *,
            n: Optional[int] = None,
            datum: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.n = n
        self.datum = datum
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
            'datum': self.datum,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetTexGendvReplyReply':
        return GetTexGendvReplyReply(**GetTexGendvReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetTexGendvReplyReplyPacket.pack(**self.as_dict())


class GetTexGendvReplyReplyCType(ctypes.Structure):
    """glx GetTexGendv_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("datum", ctypes.c_uint32),
        ("pad2", ctypes.c_uint8 * 8),
        ("var_data", ctypes.c_void_p),
    ]


GetTexGenfvRequestCookie = NewType('GetTexGenfvRequestCookie', ctypes.c_uint32)


GetTexGenfvRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('coord', FixedDataPacketField(MARKER_UINT32)),
    ('pname', FixedDataPacketField(MARKER_UINT32)),
))


class GetTexGenfvRequest:
    OPCODE = 133

    __slots__ = ('context_tag', 'coord', 'pname',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            coord: Optional[int] = None,
            pname: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.coord = coord
        self.pname = pname

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'coord': self.coord,
            'pname': self.pname,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetTexGenfvRequest':
        return GetTexGenfvRequest(**GetTexGenfvRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetTexGenfvRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], GetTexGenfvRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetTexGenfvRequest.lib = library.glx_gettexgenfv
        GetTexGenfvRequest.lib.restype = GetTexGenfvRequestCookie
        GetTexGenfvRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class GetTexGenfvRequestCType(ctypes.Structure):
    """glx GetTexGenfv"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("coord", ctypes.c_uint32),
        ("pname", ctypes.c_uint32),
    ]


GetTexGenfvReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_UINT32)),
    ('pad2', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['n'], 0)),
))


class GetTexGenfvReplyReply:
    __slots__ = ('n', 'datum', 'data',)

    def __init__(
            self, *,
            n: Optional[int] = None,
            datum: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.n = n
        self.datum = datum
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
            'datum': self.datum,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetTexGenfvReplyReply':
        return GetTexGenfvReplyReply(**GetTexGenfvReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetTexGenfvReplyReplyPacket.pack(**self.as_dict())


class GetTexGenfvReplyReplyCType(ctypes.Structure):
    """glx GetTexGenfv_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("datum", ctypes.c_uint32),
        ("pad2", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


GetTexGenivRequestCookie = NewType('GetTexGenivRequestCookie', ctypes.c_uint32)


GetTexGenivRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('coord', FixedDataPacketField(MARKER_UINT32)),
    ('pname', FixedDataPacketField(MARKER_UINT32)),
))


class GetTexGenivRequest:
    OPCODE = 134

    __slots__ = ('context_tag', 'coord', 'pname',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            coord: Optional[int] = None,
            pname: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.coord = coord
        self.pname = pname

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'coord': self.coord,
            'pname': self.pname,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetTexGenivRequest':
        return GetTexGenivRequest(**GetTexGenivRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetTexGenivRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], GetTexGenivRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetTexGenivRequest.lib = library.glx_gettexgeniv
        GetTexGenivRequest.lib.restype = GetTexGenivRequestCookie
        GetTexGenivRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class GetTexGenivRequestCType(ctypes.Structure):
    """glx GetTexGeniv"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("coord", ctypes.c_uint32),
        ("pname", ctypes.c_uint32),
    ]


GetTexGenivReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_INT32)),
    ('pad2', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_INT32, lambda d, c: d['n'], 0)),
))


class GetTexGenivReplyReply:
    __slots__ = ('n', 'datum', 'data',)

    def __init__(
            self, *,
            n: Optional[int] = None,
            datum: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.n = n
        self.datum = datum
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
            'datum': self.datum,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetTexGenivReplyReply':
        return GetTexGenivReplyReply(**GetTexGenivReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetTexGenivReplyReplyPacket.pack(**self.as_dict())


class GetTexGenivReplyReplyCType(ctypes.Structure):
    """glx GetTexGeniv_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("datum", ctypes.c_int32),
        ("pad2", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


GetTexImageRequestCookie = NewType('GetTexImageRequestCookie', ctypes.c_uint32)


GetTexImageRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('target', FixedDataPacketField(MARKER_UINT32)),
    ('level', FixedDataPacketField(MARKER_INT32)),
    ('format', FixedDataPacketField(MARKER_UINT32)),
    ('type', FixedDataPacketField(MARKER_UINT32)),
    ('swap_bytes', FixedDataPacketField(MARKER_UINT8)),
))


class GetTexImageRequest:
    OPCODE = 135

    __slots__ = ('context_tag', 'target', 'level', 'format', 'type', 'swap_bytes',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            target: Optional[int] = None,
            level: Optional[int] = None,
            format: Optional[int] = None,
            type: Optional[int] = None,
            swap_bytes: Optional[bool] = None,
    ) -> None:
        self.context_tag = context_tag
        self.target = target
        self.level = level
        self.format = format
        self.type = type
        self.swap_bytes = swap_bytes

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'target': self.target,
            'level': self.level,
            'format': self.format,
            'type': self.type,
            'swap_bytes': self.swap_bytes,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetTexImageRequest':
        return GetTexImageRequest(**GetTexImageRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetTexImageRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, bool], GetTexImageRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetTexImageRequest.lib = library.glx_getteximage
        GetTexImageRequest.lib.restype = GetTexImageRequestCookie
        GetTexImageRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int8)


class GetTexImageRequestCType(ctypes.Structure):
    """glx GetTexImage"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("target", ctypes.c_uint32),
        ("level", ctypes.c_int32),
        ("format", ctypes.c_uint32),
        ("type", ctypes.c_uint32),
        ("swap_bytes", ctypes.c_int8),
    ]


GetTexImageReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(8)),
    ('width', FixedDataPacketField(MARKER_INT32)),
    ('height', FixedDataPacketField(MARKER_INT32)),
    ('depth', FixedDataPacketField(MARKER_INT32)),
    ('pad2', FixedPadDataPacketField(4)),
    ('data', SimpleListDataPacketField(MARKER_INT8, lambda d, c: (d['length']) * (4), 0)),
))


class GetTexImageReplyReply:
    __slots__ = ('width', 'height', 'depth', 'data',)

    def __init__(
            self, *,
            width: Optional[int] = None,
            height: Optional[int] = None,
            depth: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.width = width
        self.height = height
        self.depth = depth
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'width': self.width,
            'height': self.height,
            'depth': self.depth,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetTexImageReplyReply':
        return GetTexImageReplyReply(**GetTexImageReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetTexImageReplyReplyPacket.pack(**self.as_dict())


class GetTexImageReplyReplyCType(ctypes.Structure):
    """glx GetTexImage_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 8),
        ("width", ctypes.c_int32),
        ("height", ctypes.c_int32),
        ("depth", ctypes.c_int32),
        ("pad2", ctypes.c_uint8 * 4),
        ("var_data", ctypes.c_void_p),
    ]


GetTexParameterfvRequestCookie = NewType('GetTexParameterfvRequestCookie', ctypes.c_uint32)


GetTexParameterfvRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('target', FixedDataPacketField(MARKER_UINT32)),
    ('pname', FixedDataPacketField(MARKER_UINT32)),
))


class GetTexParameterfvRequest:
    OPCODE = 136

    __slots__ = ('context_tag', 'target', 'pname',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            target: Optional[int] = None,
            pname: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.target = target
        self.pname = pname

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'target': self.target,
            'pname': self.pname,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetTexParameterfvRequest':
        return GetTexParameterfvRequest(**GetTexParameterfvRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetTexParameterfvRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], GetTexParameterfvRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetTexParameterfvRequest.lib = library.glx_gettexparameterfv
        GetTexParameterfvRequest.lib.restype = GetTexParameterfvRequestCookie
        GetTexParameterfvRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class GetTexParameterfvRequestCType(ctypes.Structure):
    """glx GetTexParameterfv"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("target", ctypes.c_uint32),
        ("pname", ctypes.c_uint32),
    ]


GetTexParameterfvReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_UINT32)),
    ('pad2', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['n'], 0)),
))


class GetTexParameterfvReplyReply:
    __slots__ = ('n', 'datum', 'data',)

    def __init__(
            self, *,
            n: Optional[int] = None,
            datum: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.n = n
        self.datum = datum
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
            'datum': self.datum,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetTexParameterfvReplyReply':
        return GetTexParameterfvReplyReply(**GetTexParameterfvReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetTexParameterfvReplyReplyPacket.pack(**self.as_dict())


class GetTexParameterfvReplyReplyCType(ctypes.Structure):
    """glx GetTexParameterfv_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("datum", ctypes.c_uint32),
        ("pad2", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


GetTexParameterivRequestCookie = NewType('GetTexParameterivRequestCookie', ctypes.c_uint32)


GetTexParameterivRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('target', FixedDataPacketField(MARKER_UINT32)),
    ('pname', FixedDataPacketField(MARKER_UINT32)),
))


class GetTexParameterivRequest:
    OPCODE = 137

    __slots__ = ('context_tag', 'target', 'pname',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            target: Optional[int] = None,
            pname: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.target = target
        self.pname = pname

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'target': self.target,
            'pname': self.pname,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetTexParameterivRequest':
        return GetTexParameterivRequest(**GetTexParameterivRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetTexParameterivRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], GetTexParameterivRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetTexParameterivRequest.lib = library.glx_gettexparameteriv
        GetTexParameterivRequest.lib.restype = GetTexParameterivRequestCookie
        GetTexParameterivRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class GetTexParameterivRequestCType(ctypes.Structure):
    """glx GetTexParameteriv"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("target", ctypes.c_uint32),
        ("pname", ctypes.c_uint32),
    ]


GetTexParameterivReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_INT32)),
    ('pad2', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_INT32, lambda d, c: d['n'], 0)),
))


class GetTexParameterivReplyReply:
    __slots__ = ('n', 'datum', 'data',)

    def __init__(
            self, *,
            n: Optional[int] = None,
            datum: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.n = n
        self.datum = datum
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
            'datum': self.datum,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetTexParameterivReplyReply':
        return GetTexParameterivReplyReply(**GetTexParameterivReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetTexParameterivReplyReplyPacket.pack(**self.as_dict())


class GetTexParameterivReplyReplyCType(ctypes.Structure):
    """glx GetTexParameteriv_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("datum", ctypes.c_int32),
        ("pad2", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


GetTexLevelParameterfvRequestCookie = NewType('GetTexLevelParameterfvRequestCookie', ctypes.c_uint32)


GetTexLevelParameterfvRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('target', FixedDataPacketField(MARKER_UINT32)),
    ('level', FixedDataPacketField(MARKER_INT32)),
    ('pname', FixedDataPacketField(MARKER_UINT32)),
))


class GetTexLevelParameterfvRequest:
    OPCODE = 138

    __slots__ = ('context_tag', 'target', 'level', 'pname',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            target: Optional[int] = None,
            level: Optional[int] = None,
            pname: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.target = target
        self.level = level
        self.pname = pname

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'target': self.target,
            'level': self.level,
            'pname': self.pname,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetTexLevelParameterfvRequest':
        return GetTexLevelParameterfvRequest(**GetTexLevelParameterfvRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetTexLevelParameterfvRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int], GetTexLevelParameterfvRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetTexLevelParameterfvRequest.lib = library.glx_gettexlevelparameterfv
        GetTexLevelParameterfvRequest.lib.restype = GetTexLevelParameterfvRequestCookie
        GetTexLevelParameterfvRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int32, ctypes.c_uint32)


class GetTexLevelParameterfvRequestCType(ctypes.Structure):
    """glx GetTexLevelParameterfv"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("target", ctypes.c_uint32),
        ("level", ctypes.c_int32),
        ("pname", ctypes.c_uint32),
    ]


GetTexLevelParameterfvReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_UINT32)),
    ('pad2', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['n'], 0)),
))


class GetTexLevelParameterfvReplyReply:
    __slots__ = ('n', 'datum', 'data',)

    def __init__(
            self, *,
            n: Optional[int] = None,
            datum: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.n = n
        self.datum = datum
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
            'datum': self.datum,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetTexLevelParameterfvReplyReply':
        return GetTexLevelParameterfvReplyReply(**GetTexLevelParameterfvReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetTexLevelParameterfvReplyReplyPacket.pack(**self.as_dict())


class GetTexLevelParameterfvReplyReplyCType(ctypes.Structure):
    """glx GetTexLevelParameterfv_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("datum", ctypes.c_uint32),
        ("pad2", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


GetTexLevelParameterivRequestCookie = NewType('GetTexLevelParameterivRequestCookie', ctypes.c_uint32)


GetTexLevelParameterivRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('target', FixedDataPacketField(MARKER_UINT32)),
    ('level', FixedDataPacketField(MARKER_INT32)),
    ('pname', FixedDataPacketField(MARKER_UINT32)),
))


class GetTexLevelParameterivRequest:
    OPCODE = 139

    __slots__ = ('context_tag', 'target', 'level', 'pname',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            target: Optional[int] = None,
            level: Optional[int] = None,
            pname: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.target = target
        self.level = level
        self.pname = pname

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'target': self.target,
            'level': self.level,
            'pname': self.pname,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetTexLevelParameterivRequest':
        return GetTexLevelParameterivRequest(**GetTexLevelParameterivRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetTexLevelParameterivRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int], GetTexLevelParameterivRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetTexLevelParameterivRequest.lib = library.glx_gettexlevelparameteriv
        GetTexLevelParameterivRequest.lib.restype = GetTexLevelParameterivRequestCookie
        GetTexLevelParameterivRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int32, ctypes.c_uint32)


class GetTexLevelParameterivRequestCType(ctypes.Structure):
    """glx GetTexLevelParameteriv"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("target", ctypes.c_uint32),
        ("level", ctypes.c_int32),
        ("pname", ctypes.c_uint32),
    ]


GetTexLevelParameterivReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_INT32)),
    ('pad2', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_INT32, lambda d, c: d['n'], 0)),
))


class GetTexLevelParameterivReplyReply:
    __slots__ = ('n', 'datum', 'data',)

    def __init__(
            self, *,
            n: Optional[int] = None,
            datum: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.n = n
        self.datum = datum
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
            'datum': self.datum,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetTexLevelParameterivReplyReply':
        return GetTexLevelParameterivReplyReply(**GetTexLevelParameterivReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetTexLevelParameterivReplyReplyPacket.pack(**self.as_dict())


class GetTexLevelParameterivReplyReplyCType(ctypes.Structure):
    """glx GetTexLevelParameteriv_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("datum", ctypes.c_int32),
        ("pad2", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


IsEnabledRequestCookie = NewType('IsEnabledRequestCookie', ctypes.c_uint32)


IsEnabledRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('capability', FixedDataPacketField(MARKER_UINT32)),
))


class IsEnabledRequest:
    OPCODE = 140

    __slots__ = ('context_tag', 'capability',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            capability: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.capability = capability

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'capability': self.capability,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'IsEnabledRequest':
        return IsEnabledRequest(**IsEnabledRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return IsEnabledRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], IsEnabledRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        IsEnabledRequest.lib = library.glx_isenabled
        IsEnabledRequest.lib.restype = IsEnabledRequestCookie
        IsEnabledRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class IsEnabledRequestCType(ctypes.Structure):
    """glx IsEnabled"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("capability", ctypes.c_uint32),
    ]


IsEnabledReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('ret_val', FixedDataPacketField(MARKER_UINT32)),
))


class IsEnabledReplyReply:
    __slots__ = ('ret_val',)

    def __init__(
            self, *,
            ret_val: Optional[bool] = None,
    ) -> None:
        self.ret_val = ret_val

    def as_dict(self) -> Dict[str, Any]:
        return {
            'ret_val': self.ret_val,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'IsEnabledReplyReply':
        return IsEnabledReplyReply(**IsEnabledReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return IsEnabledReplyReplyPacket.pack(**self.as_dict())


class IsEnabledReplyReplyCType(ctypes.Structure):
    """glx IsEnabled_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("ret_val", ctypes.c_int32),
    ]


IsListRequestCookie = NewType('IsListRequestCookie', ctypes.c_uint32)


IsListRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('list', FixedDataPacketField(MARKER_UINT32)),
))


class IsListRequest:
    OPCODE = 141

    __slots__ = ('context_tag', 'list',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            list: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.list = list

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'list': self.list,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'IsListRequest':
        return IsListRequest(**IsListRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return IsListRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], IsListRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        IsListRequest.lib = library.glx_islist
        IsListRequest.lib.restype = IsListRequestCookie
        IsListRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class IsListRequestCType(ctypes.Structure):
    """glx IsList"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("list", ctypes.c_uint32),
    ]


IsListReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('ret_val', FixedDataPacketField(MARKER_UINT32)),
))


class IsListReplyReply:
    __slots__ = ('ret_val',)

    def __init__(
            self, *,
            ret_val: Optional[bool] = None,
    ) -> None:
        self.ret_val = ret_val

    def as_dict(self) -> Dict[str, Any]:
        return {
            'ret_val': self.ret_val,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'IsListReplyReply':
        return IsListReplyReply(**IsListReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return IsListReplyReplyPacket.pack(**self.as_dict())


class IsListReplyReplyCType(ctypes.Structure):
    """glx IsList_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("ret_val", ctypes.c_int32),
    ]


FlushRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
))


class FlushRequest:
    OPCODE = 142

    __slots__ = ('context_tag',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'FlushRequest':
        return FlushRequest(**FlushRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return FlushRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        FlushRequest.lib = library.glx_flush
        FlushRequest.lib.restype = ctypes.c_uint32
        FlushRequest.lib.argstype = (ctypes.c_uint32,)


class FlushRequestCType(ctypes.Structure):
    """glx Flush"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
    ]


AreTexturesResidentRequestCookie = NewType('AreTexturesResidentRequestCookie', ctypes.c_uint32)


AreTexturesResidentRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('n', FixedDataPacketField(MARKER_INT32)),
    ('textures', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['n'], 0)),
))


class AreTexturesResidentRequest:
    OPCODE = 143

    __slots__ = ('context_tag', 'n', 'textures',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            n: Optional[int] = None,
            textures: Optional[Sequence[int]] = None,
    ) -> None:
        self.context_tag = context_tag
        self.n = n
        self.textures = textures

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'n': self.n,
            'textures': self.textures,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'AreTexturesResidentRequest':
        return AreTexturesResidentRequest(**AreTexturesResidentRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return AreTexturesResidentRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int]], AreTexturesResidentRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        AreTexturesResidentRequest.lib = library.glx_aretexturesresident
        AreTexturesResidentRequest.lib.restype = AreTexturesResidentRequestCookie
        AreTexturesResidentRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_int32, ctypes.c_void_p)


class AreTexturesResidentRequestCType(ctypes.Structure):
    """glx AreTexturesResident"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("n", ctypes.c_int32),
        ("var_data", ctypes.c_void_p),
    ]


AreTexturesResidentReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('ret_val', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('data', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: (d['length']) * (4), 0)),
))


class AreTexturesResidentReplyReply:
    __slots__ = ('ret_val', 'data',)

    def __init__(
            self, *,
            ret_val: Optional[bool] = None,
            data: Optional[Sequence[bool]] = None,
    ) -> None:
        self.ret_val = ret_val
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'ret_val': self.ret_val,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'AreTexturesResidentReplyReply':
        return AreTexturesResidentReplyReply(**AreTexturesResidentReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return AreTexturesResidentReplyReplyPacket.pack(**self.as_dict())


class AreTexturesResidentReplyReplyCType(ctypes.Structure):
    """glx AreTexturesResident_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("ret_val", ctypes.c_int32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


DeleteTexturesRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('n', FixedDataPacketField(MARKER_INT32)),
    ('textures', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['n'], 0)),
))


class DeleteTexturesRequest:
    OPCODE = 144

    __slots__ = ('context_tag', 'n', 'textures',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            n: Optional[int] = None,
            textures: Optional[Sequence[int]] = None,
    ) -> None:
        self.context_tag = context_tag
        self.n = n
        self.textures = textures

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'n': self.n,
            'textures': self.textures,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeleteTexturesRequest':
        return DeleteTexturesRequest(**DeleteTexturesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeleteTexturesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        DeleteTexturesRequest.lib = library.glx_deletetextures
        DeleteTexturesRequest.lib.restype = ctypes.c_uint32
        DeleteTexturesRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_int32, ctypes.c_void_p)


class DeleteTexturesRequestCType(ctypes.Structure):
    """glx DeleteTextures"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("n", ctypes.c_int32),
        ("var_data", ctypes.c_void_p),
    ]


GenTexturesRequestCookie = NewType('GenTexturesRequestCookie', ctypes.c_uint32)


GenTexturesRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('n', FixedDataPacketField(MARKER_INT32)),
))


class GenTexturesRequest:
    OPCODE = 145

    __slots__ = ('context_tag', 'n',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            n: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.n = n

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'n': self.n,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GenTexturesRequest':
        return GenTexturesRequest(**GenTexturesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GenTexturesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], GenTexturesRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GenTexturesRequest.lib = library.glx_gentextures
        GenTexturesRequest.lib.restype = GenTexturesRequestCookie
        GenTexturesRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_int32)


class GenTexturesRequestCType(ctypes.Structure):
    """glx GenTextures"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("n", ctypes.c_int32),
    ]


GenTexturesReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(24)),
    ('data', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['length'], 0)),
))


class GenTexturesReplyReply:
    __slots__ = ('data',)

    def __init__(
            self, *,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GenTexturesReplyReply':
        return GenTexturesReplyReply(**GenTexturesReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GenTexturesReplyReplyPacket.pack(**self.as_dict())


class GenTexturesReplyReplyCType(ctypes.Structure):
    """glx GenTextures_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 24),
        ("var_data", ctypes.c_void_p),
    ]


IsTextureRequestCookie = NewType('IsTextureRequestCookie', ctypes.c_uint32)


IsTextureRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('texture', FixedDataPacketField(MARKER_UINT32)),
))


class IsTextureRequest:
    OPCODE = 146

    __slots__ = ('context_tag', 'texture',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            texture: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.texture = texture

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'texture': self.texture,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'IsTextureRequest':
        return IsTextureRequest(**IsTextureRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return IsTextureRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], IsTextureRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        IsTextureRequest.lib = library.glx_istexture
        IsTextureRequest.lib.restype = IsTextureRequestCookie
        IsTextureRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class IsTextureRequestCType(ctypes.Structure):
    """glx IsTexture"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("texture", ctypes.c_uint32),
    ]


IsTextureReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('ret_val', FixedDataPacketField(MARKER_UINT32)),
))


class IsTextureReplyReply:
    __slots__ = ('ret_val',)

    def __init__(
            self, *,
            ret_val: Optional[bool] = None,
    ) -> None:
        self.ret_val = ret_val

    def as_dict(self) -> Dict[str, Any]:
        return {
            'ret_val': self.ret_val,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'IsTextureReplyReply':
        return IsTextureReplyReply(**IsTextureReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return IsTextureReplyReplyPacket.pack(**self.as_dict())


class IsTextureReplyReplyCType(ctypes.Structure):
    """glx IsTexture_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("ret_val", ctypes.c_int32),
    ]


GetColorTableRequestCookie = NewType('GetColorTableRequestCookie', ctypes.c_uint32)


GetColorTableRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('target', FixedDataPacketField(MARKER_UINT32)),
    ('format', FixedDataPacketField(MARKER_UINT32)),
    ('type', FixedDataPacketField(MARKER_UINT32)),
    ('swap_bytes', FixedDataPacketField(MARKER_UINT8)),
))


class GetColorTableRequest:
    OPCODE = 147

    __slots__ = ('context_tag', 'target', 'format', 'type', 'swap_bytes',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            target: Optional[int] = None,
            format: Optional[int] = None,
            type: Optional[int] = None,
            swap_bytes: Optional[bool] = None,
    ) -> None:
        self.context_tag = context_tag
        self.target = target
        self.format = format
        self.type = type
        self.swap_bytes = swap_bytes

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'target': self.target,
            'format': self.format,
            'type': self.type,
            'swap_bytes': self.swap_bytes,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetColorTableRequest':
        return GetColorTableRequest(**GetColorTableRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetColorTableRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, bool], GetColorTableRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetColorTableRequest.lib = library.glx_getcolortable
        GetColorTableRequest.lib.restype = GetColorTableRequestCookie
        GetColorTableRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int8)


class GetColorTableRequestCType(ctypes.Structure):
    """glx GetColorTable"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("target", ctypes.c_uint32),
        ("format", ctypes.c_uint32),
        ("type", ctypes.c_uint32),
        ("swap_bytes", ctypes.c_int8),
    ]


GetColorTableReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(8)),
    ('width', FixedDataPacketField(MARKER_INT32)),
    ('pad2', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_INT8, lambda d, c: (d['length']) * (4), 0)),
))


class GetColorTableReplyReply:
    __slots__ = ('width', 'data',)

    def __init__(
            self, *,
            width: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.width = width
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'width': self.width,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetColorTableReplyReply':
        return GetColorTableReplyReply(**GetColorTableReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetColorTableReplyReplyPacket.pack(**self.as_dict())


class GetColorTableReplyReplyCType(ctypes.Structure):
    """glx GetColorTable_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 8),
        ("width", ctypes.c_int32),
        ("pad2", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


GetColorTableParameterfvRequestCookie = NewType('GetColorTableParameterfvRequestCookie', ctypes.c_uint32)


GetColorTableParameterfvRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('target', FixedDataPacketField(MARKER_UINT32)),
    ('pname', FixedDataPacketField(MARKER_UINT32)),
))


class GetColorTableParameterfvRequest:
    OPCODE = 148

    __slots__ = ('context_tag', 'target', 'pname',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            target: Optional[int] = None,
            pname: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.target = target
        self.pname = pname

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'target': self.target,
            'pname': self.pname,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetColorTableParameterfvRequest':
        return GetColorTableParameterfvRequest(**GetColorTableParameterfvRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetColorTableParameterfvRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], GetColorTableParameterfvRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetColorTableParameterfvRequest.lib = library.glx_getcolortableparameterfv
        GetColorTableParameterfvRequest.lib.restype = GetColorTableParameterfvRequestCookie
        GetColorTableParameterfvRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class GetColorTableParameterfvRequestCType(ctypes.Structure):
    """glx GetColorTableParameterfv"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("target", ctypes.c_uint32),
        ("pname", ctypes.c_uint32),
    ]


GetColorTableParameterfvReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_UINT32)),
    ('pad2', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['n'], 0)),
))


class GetColorTableParameterfvReplyReply:
    __slots__ = ('n', 'datum', 'data',)

    def __init__(
            self, *,
            n: Optional[int] = None,
            datum: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.n = n
        self.datum = datum
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
            'datum': self.datum,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetColorTableParameterfvReplyReply':
        return GetColorTableParameterfvReplyReply(**GetColorTableParameterfvReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetColorTableParameterfvReplyReplyPacket.pack(**self.as_dict())


class GetColorTableParameterfvReplyReplyCType(ctypes.Structure):
    """glx GetColorTableParameterfv_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("datum", ctypes.c_uint32),
        ("pad2", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


GetColorTableParameterivRequestCookie = NewType('GetColorTableParameterivRequestCookie', ctypes.c_uint32)


GetColorTableParameterivRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('target', FixedDataPacketField(MARKER_UINT32)),
    ('pname', FixedDataPacketField(MARKER_UINT32)),
))


class GetColorTableParameterivRequest:
    OPCODE = 149

    __slots__ = ('context_tag', 'target', 'pname',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            target: Optional[int] = None,
            pname: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.target = target
        self.pname = pname

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'target': self.target,
            'pname': self.pname,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetColorTableParameterivRequest':
        return GetColorTableParameterivRequest(**GetColorTableParameterivRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetColorTableParameterivRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], GetColorTableParameterivRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetColorTableParameterivRequest.lib = library.glx_getcolortableparameteriv
        GetColorTableParameterivRequest.lib.restype = GetColorTableParameterivRequestCookie
        GetColorTableParameterivRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class GetColorTableParameterivRequestCType(ctypes.Structure):
    """glx GetColorTableParameteriv"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("target", ctypes.c_uint32),
        ("pname", ctypes.c_uint32),
    ]


GetColorTableParameterivReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_INT32)),
    ('pad2', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_INT32, lambda d, c: d['n'], 0)),
))


class GetColorTableParameterivReplyReply:
    __slots__ = ('n', 'datum', 'data',)

    def __init__(
            self, *,
            n: Optional[int] = None,
            datum: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.n = n
        self.datum = datum
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
            'datum': self.datum,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetColorTableParameterivReplyReply':
        return GetColorTableParameterivReplyReply(**GetColorTableParameterivReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetColorTableParameterivReplyReplyPacket.pack(**self.as_dict())


class GetColorTableParameterivReplyReplyCType(ctypes.Structure):
    """glx GetColorTableParameteriv_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("datum", ctypes.c_int32),
        ("pad2", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


GetConvolutionFilterRequestCookie = NewType('GetConvolutionFilterRequestCookie', ctypes.c_uint32)


GetConvolutionFilterRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('target', FixedDataPacketField(MARKER_UINT32)),
    ('format', FixedDataPacketField(MARKER_UINT32)),
    ('type', FixedDataPacketField(MARKER_UINT32)),
    ('swap_bytes', FixedDataPacketField(MARKER_UINT8)),
))


class GetConvolutionFilterRequest:
    OPCODE = 150

    __slots__ = ('context_tag', 'target', 'format', 'type', 'swap_bytes',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            target: Optional[int] = None,
            format: Optional[int] = None,
            type: Optional[int] = None,
            swap_bytes: Optional[bool] = None,
    ) -> None:
        self.context_tag = context_tag
        self.target = target
        self.format = format
        self.type = type
        self.swap_bytes = swap_bytes

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'target': self.target,
            'format': self.format,
            'type': self.type,
            'swap_bytes': self.swap_bytes,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetConvolutionFilterRequest':
        return GetConvolutionFilterRequest(**GetConvolutionFilterRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetConvolutionFilterRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, bool], GetConvolutionFilterRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetConvolutionFilterRequest.lib = library.glx_getconvolutionfilter
        GetConvolutionFilterRequest.lib.restype = GetConvolutionFilterRequestCookie
        GetConvolutionFilterRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int8)


class GetConvolutionFilterRequestCType(ctypes.Structure):
    """glx GetConvolutionFilter"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("target", ctypes.c_uint32),
        ("format", ctypes.c_uint32),
        ("type", ctypes.c_uint32),
        ("swap_bytes", ctypes.c_int8),
    ]


GetConvolutionFilterReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(8)),
    ('width', FixedDataPacketField(MARKER_INT32)),
    ('height', FixedDataPacketField(MARKER_INT32)),
    ('pad2', FixedPadDataPacketField(8)),
    ('data', SimpleListDataPacketField(MARKER_INT8, lambda d, c: (d['length']) * (4), 0)),
))


class GetConvolutionFilterReplyReply:
    __slots__ = ('width', 'height', 'data',)

    def __init__(
            self, *,
            width: Optional[int] = None,
            height: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.width = width
        self.height = height
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'width': self.width,
            'height': self.height,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetConvolutionFilterReplyReply':
        return GetConvolutionFilterReplyReply(**GetConvolutionFilterReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetConvolutionFilterReplyReplyPacket.pack(**self.as_dict())


class GetConvolutionFilterReplyReplyCType(ctypes.Structure):
    """glx GetConvolutionFilter_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 8),
        ("width", ctypes.c_int32),
        ("height", ctypes.c_int32),
        ("pad2", ctypes.c_uint8 * 8),
        ("var_data", ctypes.c_void_p),
    ]


GetConvolutionParameterfvRequestCookie = NewType('GetConvolutionParameterfvRequestCookie', ctypes.c_uint32)


GetConvolutionParameterfvRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('target', FixedDataPacketField(MARKER_UINT32)),
    ('pname', FixedDataPacketField(MARKER_UINT32)),
))


class GetConvolutionParameterfvRequest:
    OPCODE = 151

    __slots__ = ('context_tag', 'target', 'pname',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            target: Optional[int] = None,
            pname: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.target = target
        self.pname = pname

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'target': self.target,
            'pname': self.pname,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetConvolutionParameterfvRequest':
        return GetConvolutionParameterfvRequest(**GetConvolutionParameterfvRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetConvolutionParameterfvRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], GetConvolutionParameterfvRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetConvolutionParameterfvRequest.lib = library.glx_getconvolutionparameterfv
        GetConvolutionParameterfvRequest.lib.restype = GetConvolutionParameterfvRequestCookie
        GetConvolutionParameterfvRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class GetConvolutionParameterfvRequestCType(ctypes.Structure):
    """glx GetConvolutionParameterfv"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("target", ctypes.c_uint32),
        ("pname", ctypes.c_uint32),
    ]


GetConvolutionParameterfvReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_UINT32)),
    ('pad2', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['n'], 0)),
))


class GetConvolutionParameterfvReplyReply:
    __slots__ = ('n', 'datum', 'data',)

    def __init__(
            self, *,
            n: Optional[int] = None,
            datum: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.n = n
        self.datum = datum
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
            'datum': self.datum,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetConvolutionParameterfvReplyReply':
        return GetConvolutionParameterfvReplyReply(**GetConvolutionParameterfvReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetConvolutionParameterfvReplyReplyPacket.pack(**self.as_dict())


class GetConvolutionParameterfvReplyReplyCType(ctypes.Structure):
    """glx GetConvolutionParameterfv_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("datum", ctypes.c_uint32),
        ("pad2", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


GetConvolutionParameterivRequestCookie = NewType('GetConvolutionParameterivRequestCookie', ctypes.c_uint32)


GetConvolutionParameterivRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('target', FixedDataPacketField(MARKER_UINT32)),
    ('pname', FixedDataPacketField(MARKER_UINT32)),
))


class GetConvolutionParameterivRequest:
    OPCODE = 152

    __slots__ = ('context_tag', 'target', 'pname',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            target: Optional[int] = None,
            pname: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.target = target
        self.pname = pname

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'target': self.target,
            'pname': self.pname,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetConvolutionParameterivRequest':
        return GetConvolutionParameterivRequest(**GetConvolutionParameterivRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetConvolutionParameterivRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], GetConvolutionParameterivRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetConvolutionParameterivRequest.lib = library.glx_getconvolutionparameteriv
        GetConvolutionParameterivRequest.lib.restype = GetConvolutionParameterivRequestCookie
        GetConvolutionParameterivRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class GetConvolutionParameterivRequestCType(ctypes.Structure):
    """glx GetConvolutionParameteriv"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("target", ctypes.c_uint32),
        ("pname", ctypes.c_uint32),
    ]


GetConvolutionParameterivReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_INT32)),
    ('pad2', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_INT32, lambda d, c: d['n'], 0)),
))


class GetConvolutionParameterivReplyReply:
    __slots__ = ('n', 'datum', 'data',)

    def __init__(
            self, *,
            n: Optional[int] = None,
            datum: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.n = n
        self.datum = datum
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
            'datum': self.datum,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetConvolutionParameterivReplyReply':
        return GetConvolutionParameterivReplyReply(**GetConvolutionParameterivReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetConvolutionParameterivReplyReplyPacket.pack(**self.as_dict())


class GetConvolutionParameterivReplyReplyCType(ctypes.Structure):
    """glx GetConvolutionParameteriv_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("datum", ctypes.c_int32),
        ("pad2", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


GetSeparableFilterRequestCookie = NewType('GetSeparableFilterRequestCookie', ctypes.c_uint32)


GetSeparableFilterRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('target', FixedDataPacketField(MARKER_UINT32)),
    ('format', FixedDataPacketField(MARKER_UINT32)),
    ('type', FixedDataPacketField(MARKER_UINT32)),
    ('swap_bytes', FixedDataPacketField(MARKER_UINT8)),
))


class GetSeparableFilterRequest:
    OPCODE = 153

    __slots__ = ('context_tag', 'target', 'format', 'type', 'swap_bytes',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            target: Optional[int] = None,
            format: Optional[int] = None,
            type: Optional[int] = None,
            swap_bytes: Optional[bool] = None,
    ) -> None:
        self.context_tag = context_tag
        self.target = target
        self.format = format
        self.type = type
        self.swap_bytes = swap_bytes

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'target': self.target,
            'format': self.format,
            'type': self.type,
            'swap_bytes': self.swap_bytes,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetSeparableFilterRequest':
        return GetSeparableFilterRequest(**GetSeparableFilterRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetSeparableFilterRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, bool], GetSeparableFilterRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetSeparableFilterRequest.lib = library.glx_getseparablefilter
        GetSeparableFilterRequest.lib.restype = GetSeparableFilterRequestCookie
        GetSeparableFilterRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int8)


class GetSeparableFilterRequestCType(ctypes.Structure):
    """glx GetSeparableFilter"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("target", ctypes.c_uint32),
        ("format", ctypes.c_uint32),
        ("type", ctypes.c_uint32),
        ("swap_bytes", ctypes.c_int8),
    ]


GetSeparableFilterReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(8)),
    ('row_w', FixedDataPacketField(MARKER_INT32)),
    ('col_h', FixedDataPacketField(MARKER_INT32)),
    ('pad2', FixedPadDataPacketField(8)),
    ('rows_and_cols', SimpleListDataPacketField(MARKER_INT8, lambda d, c: (d['length']) * (4), 0)),
))


class GetSeparableFilterReplyReply:
    __slots__ = ('row_w', 'col_h', 'rows_and_cols',)

    def __init__(
            self, *,
            row_w: Optional[int] = None,
            col_h: Optional[int] = None,
            rows_and_cols: Optional[Sequence[int]] = None,
    ) -> None:
        self.row_w = row_w
        self.col_h = col_h
        self.rows_and_cols = rows_and_cols

    def as_dict(self) -> Dict[str, Any]:
        return {
            'row_w': self.row_w,
            'col_h': self.col_h,
            'rows_and_cols': self.rows_and_cols,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetSeparableFilterReplyReply':
        return GetSeparableFilterReplyReply(**GetSeparableFilterReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetSeparableFilterReplyReplyPacket.pack(**self.as_dict())


class GetSeparableFilterReplyReplyCType(ctypes.Structure):
    """glx GetSeparableFilter_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 8),
        ("row_w", ctypes.c_int32),
        ("col_h", ctypes.c_int32),
        ("pad2", ctypes.c_uint8 * 8),
        ("var_data", ctypes.c_void_p),
    ]


GetHistogramRequestCookie = NewType('GetHistogramRequestCookie', ctypes.c_uint32)


GetHistogramRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('target', FixedDataPacketField(MARKER_UINT32)),
    ('format', FixedDataPacketField(MARKER_UINT32)),
    ('type', FixedDataPacketField(MARKER_UINT32)),
    ('swap_bytes', FixedDataPacketField(MARKER_UINT8)),
    ('reset', FixedDataPacketField(MARKER_UINT8)),
))


class GetHistogramRequest:
    OPCODE = 154

    __slots__ = ('context_tag', 'target', 'format', 'type', 'swap_bytes', 'reset',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            target: Optional[int] = None,
            format: Optional[int] = None,
            type: Optional[int] = None,
            swap_bytes: Optional[bool] = None,
            reset: Optional[bool] = None,
    ) -> None:
        self.context_tag = context_tag
        self.target = target
        self.format = format
        self.type = type
        self.swap_bytes = swap_bytes
        self.reset = reset

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'target': self.target,
            'format': self.format,
            'type': self.type,
            'swap_bytes': self.swap_bytes,
            'reset': self.reset,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetHistogramRequest':
        return GetHistogramRequest(**GetHistogramRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetHistogramRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, bool, bool], GetHistogramRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetHistogramRequest.lib = library.glx_gethistogram
        GetHistogramRequest.lib.restype = GetHistogramRequestCookie
        GetHistogramRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int8, ctypes.c_int8)


class GetHistogramRequestCType(ctypes.Structure):
    """glx GetHistogram"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("target", ctypes.c_uint32),
        ("format", ctypes.c_uint32),
        ("type", ctypes.c_uint32),
        ("swap_bytes", ctypes.c_int8),
        ("reset", ctypes.c_int8),
    ]


GetHistogramReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(8)),
    ('width', FixedDataPacketField(MARKER_INT32)),
    ('pad2', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_INT8, lambda d, c: (d['length']) * (4), 0)),
))


class GetHistogramReplyReply:
    __slots__ = ('width', 'data',)

    def __init__(
            self, *,
            width: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.width = width
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'width': self.width,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetHistogramReplyReply':
        return GetHistogramReplyReply(**GetHistogramReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetHistogramReplyReplyPacket.pack(**self.as_dict())


class GetHistogramReplyReplyCType(ctypes.Structure):
    """glx GetHistogram_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 8),
        ("width", ctypes.c_int32),
        ("pad2", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


GetHistogramParameterfvRequestCookie = NewType('GetHistogramParameterfvRequestCookie', ctypes.c_uint32)


GetHistogramParameterfvRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('target', FixedDataPacketField(MARKER_UINT32)),
    ('pname', FixedDataPacketField(MARKER_UINT32)),
))


class GetHistogramParameterfvRequest:
    OPCODE = 155

    __slots__ = ('context_tag', 'target', 'pname',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            target: Optional[int] = None,
            pname: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.target = target
        self.pname = pname

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'target': self.target,
            'pname': self.pname,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetHistogramParameterfvRequest':
        return GetHistogramParameterfvRequest(**GetHistogramParameterfvRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetHistogramParameterfvRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], GetHistogramParameterfvRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetHistogramParameterfvRequest.lib = library.glx_gethistogramparameterfv
        GetHistogramParameterfvRequest.lib.restype = GetHistogramParameterfvRequestCookie
        GetHistogramParameterfvRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class GetHistogramParameterfvRequestCType(ctypes.Structure):
    """glx GetHistogramParameterfv"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("target", ctypes.c_uint32),
        ("pname", ctypes.c_uint32),
    ]


GetHistogramParameterfvReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_UINT32)),
    ('pad2', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['n'], 0)),
))


class GetHistogramParameterfvReplyReply:
    __slots__ = ('n', 'datum', 'data',)

    def __init__(
            self, *,
            n: Optional[int] = None,
            datum: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.n = n
        self.datum = datum
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
            'datum': self.datum,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetHistogramParameterfvReplyReply':
        return GetHistogramParameterfvReplyReply(**GetHistogramParameterfvReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetHistogramParameterfvReplyReplyPacket.pack(**self.as_dict())


class GetHistogramParameterfvReplyReplyCType(ctypes.Structure):
    """glx GetHistogramParameterfv_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("datum", ctypes.c_uint32),
        ("pad2", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


GetHistogramParameterivRequestCookie = NewType('GetHistogramParameterivRequestCookie', ctypes.c_uint32)


GetHistogramParameterivRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('target', FixedDataPacketField(MARKER_UINT32)),
    ('pname', FixedDataPacketField(MARKER_UINT32)),
))


class GetHistogramParameterivRequest:
    OPCODE = 156

    __slots__ = ('context_tag', 'target', 'pname',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            target: Optional[int] = None,
            pname: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.target = target
        self.pname = pname

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'target': self.target,
            'pname': self.pname,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetHistogramParameterivRequest':
        return GetHistogramParameterivRequest(**GetHistogramParameterivRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetHistogramParameterivRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], GetHistogramParameterivRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetHistogramParameterivRequest.lib = library.glx_gethistogramparameteriv
        GetHistogramParameterivRequest.lib.restype = GetHistogramParameterivRequestCookie
        GetHistogramParameterivRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class GetHistogramParameterivRequestCType(ctypes.Structure):
    """glx GetHistogramParameteriv"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("target", ctypes.c_uint32),
        ("pname", ctypes.c_uint32),
    ]


GetHistogramParameterivReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_INT32)),
    ('pad2', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_INT32, lambda d, c: d['n'], 0)),
))


class GetHistogramParameterivReplyReply:
    __slots__ = ('n', 'datum', 'data',)

    def __init__(
            self, *,
            n: Optional[int] = None,
            datum: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.n = n
        self.datum = datum
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
            'datum': self.datum,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetHistogramParameterivReplyReply':
        return GetHistogramParameterivReplyReply(**GetHistogramParameterivReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetHistogramParameterivReplyReplyPacket.pack(**self.as_dict())


class GetHistogramParameterivReplyReplyCType(ctypes.Structure):
    """glx GetHistogramParameteriv_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("datum", ctypes.c_int32),
        ("pad2", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


GetMinmaxRequestCookie = NewType('GetMinmaxRequestCookie', ctypes.c_uint32)


GetMinmaxRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('target', FixedDataPacketField(MARKER_UINT32)),
    ('format', FixedDataPacketField(MARKER_UINT32)),
    ('type', FixedDataPacketField(MARKER_UINT32)),
    ('swap_bytes', FixedDataPacketField(MARKER_UINT8)),
    ('reset', FixedDataPacketField(MARKER_UINT8)),
))


class GetMinmaxRequest:
    OPCODE = 157

    __slots__ = ('context_tag', 'target', 'format', 'type', 'swap_bytes', 'reset',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            target: Optional[int] = None,
            format: Optional[int] = None,
            type: Optional[int] = None,
            swap_bytes: Optional[bool] = None,
            reset: Optional[bool] = None,
    ) -> None:
        self.context_tag = context_tag
        self.target = target
        self.format = format
        self.type = type
        self.swap_bytes = swap_bytes
        self.reset = reset

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'target': self.target,
            'format': self.format,
            'type': self.type,
            'swap_bytes': self.swap_bytes,
            'reset': self.reset,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetMinmaxRequest':
        return GetMinmaxRequest(**GetMinmaxRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetMinmaxRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, bool, bool], GetMinmaxRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetMinmaxRequest.lib = library.glx_getminmax
        GetMinmaxRequest.lib.restype = GetMinmaxRequestCookie
        GetMinmaxRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int8, ctypes.c_int8)


class GetMinmaxRequestCType(ctypes.Structure):
    """glx GetMinmax"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("target", ctypes.c_uint32),
        ("format", ctypes.c_uint32),
        ("type", ctypes.c_uint32),
        ("swap_bytes", ctypes.c_int8),
        ("reset", ctypes.c_int8),
    ]


GetMinmaxReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(24)),
    ('data', SimpleListDataPacketField(MARKER_INT8, lambda d, c: (d['length']) * (4), 0)),
))


class GetMinmaxReplyReply:
    __slots__ = ('data',)

    def __init__(
            self, *,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetMinmaxReplyReply':
        return GetMinmaxReplyReply(**GetMinmaxReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetMinmaxReplyReplyPacket.pack(**self.as_dict())


class GetMinmaxReplyReplyCType(ctypes.Structure):
    """glx GetMinmax_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 24),
        ("var_data", ctypes.c_void_p),
    ]


GetMinmaxParameterfvRequestCookie = NewType('GetMinmaxParameterfvRequestCookie', ctypes.c_uint32)


GetMinmaxParameterfvRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('target', FixedDataPacketField(MARKER_UINT32)),
    ('pname', FixedDataPacketField(MARKER_UINT32)),
))


class GetMinmaxParameterfvRequest:
    OPCODE = 158

    __slots__ = ('context_tag', 'target', 'pname',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            target: Optional[int] = None,
            pname: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.target = target
        self.pname = pname

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'target': self.target,
            'pname': self.pname,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetMinmaxParameterfvRequest':
        return GetMinmaxParameterfvRequest(**GetMinmaxParameterfvRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetMinmaxParameterfvRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], GetMinmaxParameterfvRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetMinmaxParameterfvRequest.lib = library.glx_getminmaxparameterfv
        GetMinmaxParameterfvRequest.lib.restype = GetMinmaxParameterfvRequestCookie
        GetMinmaxParameterfvRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class GetMinmaxParameterfvRequestCType(ctypes.Structure):
    """glx GetMinmaxParameterfv"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("target", ctypes.c_uint32),
        ("pname", ctypes.c_uint32),
    ]


GetMinmaxParameterfvReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_UINT32)),
    ('pad2', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['n'], 0)),
))


class GetMinmaxParameterfvReplyReply:
    __slots__ = ('n', 'datum', 'data',)

    def __init__(
            self, *,
            n: Optional[int] = None,
            datum: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.n = n
        self.datum = datum
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
            'datum': self.datum,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetMinmaxParameterfvReplyReply':
        return GetMinmaxParameterfvReplyReply(**GetMinmaxParameterfvReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetMinmaxParameterfvReplyReplyPacket.pack(**self.as_dict())


class GetMinmaxParameterfvReplyReplyCType(ctypes.Structure):
    """glx GetMinmaxParameterfv_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("datum", ctypes.c_uint32),
        ("pad2", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


GetMinmaxParameterivRequestCookie = NewType('GetMinmaxParameterivRequestCookie', ctypes.c_uint32)


GetMinmaxParameterivRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('target', FixedDataPacketField(MARKER_UINT32)),
    ('pname', FixedDataPacketField(MARKER_UINT32)),
))


class GetMinmaxParameterivRequest:
    OPCODE = 159

    __slots__ = ('context_tag', 'target', 'pname',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            target: Optional[int] = None,
            pname: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.target = target
        self.pname = pname

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'target': self.target,
            'pname': self.pname,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetMinmaxParameterivRequest':
        return GetMinmaxParameterivRequest(**GetMinmaxParameterivRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetMinmaxParameterivRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], GetMinmaxParameterivRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetMinmaxParameterivRequest.lib = library.glx_getminmaxparameteriv
        GetMinmaxParameterivRequest.lib.restype = GetMinmaxParameterivRequestCookie
        GetMinmaxParameterivRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class GetMinmaxParameterivRequestCType(ctypes.Structure):
    """glx GetMinmaxParameteriv"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("target", ctypes.c_uint32),
        ("pname", ctypes.c_uint32),
    ]


GetMinmaxParameterivReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_INT32)),
    ('pad2', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_INT32, lambda d, c: d['n'], 0)),
))


class GetMinmaxParameterivReplyReply:
    __slots__ = ('n', 'datum', 'data',)

    def __init__(
            self, *,
            n: Optional[int] = None,
            datum: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.n = n
        self.datum = datum
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
            'datum': self.datum,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetMinmaxParameterivReplyReply':
        return GetMinmaxParameterivReplyReply(**GetMinmaxParameterivReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetMinmaxParameterivReplyReplyPacket.pack(**self.as_dict())


class GetMinmaxParameterivReplyReplyCType(ctypes.Structure):
    """glx GetMinmaxParameteriv_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("datum", ctypes.c_int32),
        ("pad2", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


GetCompressedTexImageArbRequestCookie = NewType('GetCompressedTexImageArbRequestCookie', ctypes.c_uint32)


GetCompressedTexImageArbRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('target', FixedDataPacketField(MARKER_UINT32)),
    ('level', FixedDataPacketField(MARKER_INT32)),
))


class GetCompressedTexImageArbRequest:
    OPCODE = 160

    __slots__ = ('context_tag', 'target', 'level',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            target: Optional[int] = None,
            level: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.target = target
        self.level = level

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'target': self.target,
            'level': self.level,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetCompressedTexImageArbRequest':
        return GetCompressedTexImageArbRequest(**GetCompressedTexImageArbRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetCompressedTexImageArbRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], GetCompressedTexImageArbRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetCompressedTexImageArbRequest.lib = library.glx_getcompressedteximagearb
        GetCompressedTexImageArbRequest.lib.restype = GetCompressedTexImageArbRequestCookie
        GetCompressedTexImageArbRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int32)


class GetCompressedTexImageArbRequestCType(ctypes.Structure):
    """glx GetCompressedTexImageARB"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("target", ctypes.c_uint32),
        ("level", ctypes.c_int32),
    ]


GetCompressedTexImageArbReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(8)),
    ('size', FixedDataPacketField(MARKER_INT32)),
    ('pad2', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_INT8, lambda d, c: (d['length']) * (4), 0)),
))


class GetCompressedTexImageArbReplyReply:
    __slots__ = ('size', 'data',)

    def __init__(
            self, *,
            size: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.size = size
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'size': self.size,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetCompressedTexImageArbReplyReply':
        return GetCompressedTexImageArbReplyReply(**GetCompressedTexImageArbReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetCompressedTexImageArbReplyReplyPacket.pack(**self.as_dict())


class GetCompressedTexImageArbReplyReplyCType(ctypes.Structure):
    """glx GetCompressedTexImageARB_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 8),
        ("size", ctypes.c_int32),
        ("pad2", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


DeleteQueriesArbRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('n', FixedDataPacketField(MARKER_INT32)),
    ('ids', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['n'], 0)),
))


class DeleteQueriesArbRequest:
    OPCODE = 161

    __slots__ = ('context_tag', 'n', 'ids',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            n: Optional[int] = None,
            ids: Optional[Sequence[int]] = None,
    ) -> None:
        self.context_tag = context_tag
        self.n = n
        self.ids = ids

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'n': self.n,
            'ids': self.ids,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeleteQueriesArbRequest':
        return DeleteQueriesArbRequest(**DeleteQueriesArbRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeleteQueriesArbRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        DeleteQueriesArbRequest.lib = library.glx_deletequeriesarb
        DeleteQueriesArbRequest.lib.restype = ctypes.c_uint32
        DeleteQueriesArbRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_int32, ctypes.c_void_p)


class DeleteQueriesArbRequestCType(ctypes.Structure):
    """glx DeleteQueriesARB"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("n", ctypes.c_int32),
        ("var_data", ctypes.c_void_p),
    ]


GenQueriesArbRequestCookie = NewType('GenQueriesArbRequestCookie', ctypes.c_uint32)


GenQueriesArbRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('n', FixedDataPacketField(MARKER_INT32)),
))


class GenQueriesArbRequest:
    OPCODE = 162

    __slots__ = ('context_tag', 'n',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            n: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.n = n

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'n': self.n,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GenQueriesArbRequest':
        return GenQueriesArbRequest(**GenQueriesArbRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GenQueriesArbRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], GenQueriesArbRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GenQueriesArbRequest.lib = library.glx_genqueriesarb
        GenQueriesArbRequest.lib.restype = GenQueriesArbRequestCookie
        GenQueriesArbRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_int32)


class GenQueriesArbRequestCType(ctypes.Structure):
    """glx GenQueriesARB"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("n", ctypes.c_int32),
    ]


GenQueriesArbReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(24)),
    ('data', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['length'], 0)),
))


class GenQueriesArbReplyReply:
    __slots__ = ('data',)

    def __init__(
            self, *,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GenQueriesArbReplyReply':
        return GenQueriesArbReplyReply(**GenQueriesArbReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GenQueriesArbReplyReplyPacket.pack(**self.as_dict())


class GenQueriesArbReplyReplyCType(ctypes.Structure):
    """glx GenQueriesARB_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 24),
        ("var_data", ctypes.c_void_p),
    ]


IsQueryArbRequestCookie = NewType('IsQueryArbRequestCookie', ctypes.c_uint32)


IsQueryArbRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('id', FixedDataPacketField(MARKER_UINT32)),
))


class IsQueryArbRequest:
    OPCODE = 163

    __slots__ = ('context_tag', 'id',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            id: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.id = id

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'id': self.id,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'IsQueryArbRequest':
        return IsQueryArbRequest(**IsQueryArbRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return IsQueryArbRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], IsQueryArbRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        IsQueryArbRequest.lib = library.glx_isqueryarb
        IsQueryArbRequest.lib.restype = IsQueryArbRequestCookie
        IsQueryArbRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class IsQueryArbRequestCType(ctypes.Structure):
    """glx IsQueryARB"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("id", ctypes.c_uint32),
    ]


IsQueryArbReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('ret_val', FixedDataPacketField(MARKER_UINT32)),
))


class IsQueryArbReplyReply:
    __slots__ = ('ret_val',)

    def __init__(
            self, *,
            ret_val: Optional[bool] = None,
    ) -> None:
        self.ret_val = ret_val

    def as_dict(self) -> Dict[str, Any]:
        return {
            'ret_val': self.ret_val,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'IsQueryArbReplyReply':
        return IsQueryArbReplyReply(**IsQueryArbReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return IsQueryArbReplyReplyPacket.pack(**self.as_dict())


class IsQueryArbReplyReplyCType(ctypes.Structure):
    """glx IsQueryARB_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("ret_val", ctypes.c_int32),
    ]


GetQueryivArbRequestCookie = NewType('GetQueryivArbRequestCookie', ctypes.c_uint32)


GetQueryivArbRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('target', FixedDataPacketField(MARKER_UINT32)),
    ('pname', FixedDataPacketField(MARKER_UINT32)),
))


class GetQueryivArbRequest:
    OPCODE = 164

    __slots__ = ('context_tag', 'target', 'pname',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            target: Optional[int] = None,
            pname: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.target = target
        self.pname = pname

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'target': self.target,
            'pname': self.pname,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetQueryivArbRequest':
        return GetQueryivArbRequest(**GetQueryivArbRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetQueryivArbRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], GetQueryivArbRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetQueryivArbRequest.lib = library.glx_getqueryivarb
        GetQueryivArbRequest.lib.restype = GetQueryivArbRequestCookie
        GetQueryivArbRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class GetQueryivArbRequestCType(ctypes.Structure):
    """glx GetQueryivARB"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("target", ctypes.c_uint32),
        ("pname", ctypes.c_uint32),
    ]


GetQueryivArbReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_INT32)),
    ('pad2', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_INT32, lambda d, c: d['n'], 0)),
))


class GetQueryivArbReplyReply:
    __slots__ = ('n', 'datum', 'data',)

    def __init__(
            self, *,
            n: Optional[int] = None,
            datum: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.n = n
        self.datum = datum
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
            'datum': self.datum,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetQueryivArbReplyReply':
        return GetQueryivArbReplyReply(**GetQueryivArbReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetQueryivArbReplyReplyPacket.pack(**self.as_dict())


class GetQueryivArbReplyReplyCType(ctypes.Structure):
    """glx GetQueryivARB_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("datum", ctypes.c_int32),
        ("pad2", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


GetQueryObjectivArbRequestCookie = NewType('GetQueryObjectivArbRequestCookie', ctypes.c_uint32)


GetQueryObjectivArbRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('id', FixedDataPacketField(MARKER_UINT32)),
    ('pname', FixedDataPacketField(MARKER_UINT32)),
))


class GetQueryObjectivArbRequest:
    OPCODE = 165

    __slots__ = ('context_tag', 'id', 'pname',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            id: Optional[int] = None,
            pname: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.id = id
        self.pname = pname

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'id': self.id,
            'pname': self.pname,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetQueryObjectivArbRequest':
        return GetQueryObjectivArbRequest(**GetQueryObjectivArbRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetQueryObjectivArbRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], GetQueryObjectivArbRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetQueryObjectivArbRequest.lib = library.glx_getqueryobjectivarb
        GetQueryObjectivArbRequest.lib.restype = GetQueryObjectivArbRequestCookie
        GetQueryObjectivArbRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class GetQueryObjectivArbRequestCType(ctypes.Structure):
    """glx GetQueryObjectivARB"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("id", ctypes.c_uint32),
        ("pname", ctypes.c_uint32),
    ]


GetQueryObjectivArbReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_INT32)),
    ('pad2', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_INT32, lambda d, c: d['n'], 0)),
))


class GetQueryObjectivArbReplyReply:
    __slots__ = ('n', 'datum', 'data',)

    def __init__(
            self, *,
            n: Optional[int] = None,
            datum: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.n = n
        self.datum = datum
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
            'datum': self.datum,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetQueryObjectivArbReplyReply':
        return GetQueryObjectivArbReplyReply(**GetQueryObjectivArbReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetQueryObjectivArbReplyReplyPacket.pack(**self.as_dict())


class GetQueryObjectivArbReplyReplyCType(ctypes.Structure):
    """glx GetQueryObjectivARB_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("datum", ctypes.c_int32),
        ("pad2", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


GetQueryObjectuivArbRequestCookie = NewType('GetQueryObjectuivArbRequestCookie', ctypes.c_uint32)


GetQueryObjectuivArbRequestPacket = DataPacket((
    ('context_tag', FixedDataPacketField(MARKER_UINT32)),
    ('id', FixedDataPacketField(MARKER_UINT32)),
    ('pname', FixedDataPacketField(MARKER_UINT32)),
))


class GetQueryObjectuivArbRequest:
    OPCODE = 166

    __slots__ = ('context_tag', 'id', 'pname',)

    def __init__(
            self, *,
            context_tag: Optional[int] = None,
            id: Optional[int] = None,
            pname: Optional[int] = None,
    ) -> None:
        self.context_tag = context_tag
        self.id = id
        self.pname = pname

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_tag': self.context_tag,
            'id': self.id,
            'pname': self.pname,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetQueryObjectuivArbRequest':
        return GetQueryObjectuivArbRequest(**GetQueryObjectuivArbRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetQueryObjectuivArbRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], GetQueryObjectuivArbRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetQueryObjectuivArbRequest.lib = library.glx_getqueryobjectuivarb
        GetQueryObjectuivArbRequest.lib.restype = GetQueryObjectuivArbRequestCookie
        GetQueryObjectuivArbRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class GetQueryObjectuivArbRequestCType(ctypes.Structure):
    """glx GetQueryObjectuivARB"""
    _fields_ = [
        ("context_tag", ctypes.c_uint32),
        ("id", ctypes.c_uint32),
        ("pname", ctypes.c_uint32),
    ]


GetQueryObjectuivArbReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(4)),
    ('n', FixedDataPacketField(MARKER_UINT32)),
    ('datum', FixedDataPacketField(MARKER_UINT32)),
    ('pad2', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['n'], 0)),
))


class GetQueryObjectuivArbReplyReply:
    __slots__ = ('n', 'datum', 'data',)

    def __init__(
            self, *,
            n: Optional[int] = None,
            datum: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.n = n
        self.datum = datum
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'n': self.n,
            'datum': self.datum,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetQueryObjectuivArbReplyReply':
        return GetQueryObjectuivArbReplyReply(**GetQueryObjectuivArbReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetQueryObjectuivArbReplyReplyPacket.pack(**self.as_dict())


class GetQueryObjectuivArbReplyReplyCType(ctypes.Structure):
    """glx GetQueryObjectuivARB_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
        ("n", ctypes.c_uint32),
        ("datum", ctypes.c_uint32),
        ("pad2", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


# ------------------------------------------------------------------
# Unions

