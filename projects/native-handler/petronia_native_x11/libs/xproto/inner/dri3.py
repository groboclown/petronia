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
        QueryVersionRequest.lib = library.dri3_queryversion
        QueryVersionRequest.lib.restype = QueryVersionRequestCookie
        QueryVersionRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class QueryVersionRequestCType(ctypes.Structure):
    """dri3 QueryVersion"""
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
    """dri3 QueryVersion_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("major_version", ctypes.c_uint32),
        ("minor_version", ctypes.c_uint32),
    ]


OpenRequestCookie = NewType('OpenRequestCookie', ctypes.c_uint32)


OpenRequestPacket = DataPacket((
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('provider', FixedDataPacketField(MARKER_UINT32)),
))


class OpenRequest:
    OPCODE = 1

    __slots__ = ('drawable', 'provider',)

    def __init__(
            self, *,
            drawable: Optional[int] = None,
            provider: Optional[int] = None,
    ) -> None:
        self.drawable = drawable
        self.provider = provider

    def as_dict(self) -> Dict[str, Any]:
        return {
            'drawable': self.drawable,
            'provider': self.provider,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'OpenRequest':
        return OpenRequest(**OpenRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return OpenRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], OpenRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        OpenRequest.lib = library.dri3_open
        OpenRequest.lib.restype = OpenRequestCookie
        OpenRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class OpenRequestCType(ctypes.Structure):
    """dri3 Open"""
    _fields_ = [
        ("drawable", ctypes.c_uint32),
        ("provider", ctypes.c_uint32),
    ]


OpenReplyReplyPacket = DataPacket((
    ('nfd', FixedDataPacketField(MARKER_UINT8)),
    ('device_fd', FixedDataPacketField(file_descriptor)),
    ('pad0', FixedPadDataPacketField(24)),
))


class OpenReplyReply:
    __slots__ = ('nfd', 'device_fd',)

    def __init__(
            self, *,
            nfd: Optional[int] = None,
            device_fd: Optional[int] = None,
    ) -> None:
        self.nfd = nfd
        self.device_fd = device_fd

    def as_dict(self) -> Dict[str, Any]:
        return {
            'nfd': self.nfd,
            'device_fd': self.device_fd,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'OpenReplyReply':
        return OpenReplyReply(**OpenReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return OpenReplyReplyPacket.pack(**self.as_dict())


class OpenReplyReplyCType(ctypes.Structure):
    """dri3 Open_reply"""
    _fields_ = [
        ("nfd", ctypes.c_uint8),
        ("device_fd", ctypes.c_int32),
        ("pad0", ctypes.c_uint8 * 24),
    ]


PixmapFromBufferRequestPacket = DataPacket((
    ('pixmap', FixedDataPacketField(MARKER_UINT32)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('size', FixedDataPacketField(MARKER_UINT32)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('stride', FixedDataPacketField(MARKER_UINT16)),
    ('depth', FixedDataPacketField(MARKER_UINT8)),
    ('bpp', FixedDataPacketField(MARKER_UINT8)),
    ('pixmap_fd', FixedDataPacketField(file_descriptor)),
))


class PixmapFromBufferRequest:
    OPCODE = 2

    __slots__ = ('pixmap', 'drawable', 'size', 'width', 'height', 'stride', 'depth', 'bpp', 'pixmap_fd',)

    def __init__(
            self, *,
            pixmap: Optional[int] = None,
            drawable: Optional[int] = None,
            size: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            stride: Optional[int] = None,
            depth: Optional[int] = None,
            bpp: Optional[int] = None,
            pixmap_fd: Optional[int] = None,
    ) -> None:
        self.pixmap = pixmap
        self.drawable = drawable
        self.size = size
        self.width = width
        self.height = height
        self.stride = stride
        self.depth = depth
        self.bpp = bpp
        self.pixmap_fd = pixmap_fd

    def as_dict(self) -> Dict[str, Any]:
        return {
            'pixmap': self.pixmap,
            'drawable': self.drawable,
            'size': self.size,
            'width': self.width,
            'height': self.height,
            'stride': self.stride,
            'depth': self.depth,
            'bpp': self.bpp,
            'pixmap_fd': self.pixmap_fd,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PixmapFromBufferRequest':
        return PixmapFromBufferRequest(**PixmapFromBufferRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PixmapFromBufferRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PixmapFromBufferRequest.lib = library.dri3_pixmapfrombuffer
        PixmapFromBufferRequest.lib.restype = ctypes.c_uint32
        PixmapFromBufferRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_int32)


class PixmapFromBufferRequestCType(ctypes.Structure):
    """dri3 PixmapFromBuffer"""
    _fields_ = [
        ("pixmap", ctypes.c_uint32),
        ("drawable", ctypes.c_uint32),
        ("size", ctypes.c_uint32),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("stride", ctypes.c_uint16),
        ("depth", ctypes.c_uint8),
        ("bpp", ctypes.c_uint8),
        ("pixmap_fd", ctypes.c_int32),
    ]


BufferFromPixmapRequestCookie = NewType('BufferFromPixmapRequestCookie', ctypes.c_uint32)


BufferFromPixmapRequestPacket = DataPacket((
    ('pixmap', FixedDataPacketField(MARKER_UINT32)),
))


class BufferFromPixmapRequest:
    OPCODE = 3

    __slots__ = ('pixmap',)

    def __init__(
            self, *,
            pixmap: Optional[int] = None,
    ) -> None:
        self.pixmap = pixmap

    def as_dict(self) -> Dict[str, Any]:
        return {
            'pixmap': self.pixmap,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'BufferFromPixmapRequest':
        return BufferFromPixmapRequest(**BufferFromPixmapRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return BufferFromPixmapRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], BufferFromPixmapRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        BufferFromPixmapRequest.lib = library.dri3_bufferfrompixmap
        BufferFromPixmapRequest.lib.restype = BufferFromPixmapRequestCookie
        BufferFromPixmapRequest.lib.argstype = (ctypes.c_uint32,)


class BufferFromPixmapRequestCType(ctypes.Structure):
    """dri3 BufferFromPixmap"""
    _fields_ = [
        ("pixmap", ctypes.c_uint32),
    ]


BufferFromPixmapReplyReplyPacket = DataPacket((
    ('nfd', FixedDataPacketField(MARKER_UINT8)),
    ('size', FixedDataPacketField(MARKER_UINT32)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('stride', FixedDataPacketField(MARKER_UINT16)),
    ('depth', FixedDataPacketField(MARKER_UINT8)),
    ('bpp', FixedDataPacketField(MARKER_UINT8)),
    ('pixmap_fd', FixedDataPacketField(file_descriptor)),
    ('pad0', FixedPadDataPacketField(12)),
))


class BufferFromPixmapReplyReply:
    __slots__ = ('nfd', 'size', 'width', 'height', 'stride', 'depth', 'bpp', 'pixmap_fd',)

    def __init__(
            self, *,
            nfd: Optional[int] = None,
            size: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            stride: Optional[int] = None,
            depth: Optional[int] = None,
            bpp: Optional[int] = None,
            pixmap_fd: Optional[int] = None,
    ) -> None:
        self.nfd = nfd
        self.size = size
        self.width = width
        self.height = height
        self.stride = stride
        self.depth = depth
        self.bpp = bpp
        self.pixmap_fd = pixmap_fd

    def as_dict(self) -> Dict[str, Any]:
        return {
            'nfd': self.nfd,
            'size': self.size,
            'width': self.width,
            'height': self.height,
            'stride': self.stride,
            'depth': self.depth,
            'bpp': self.bpp,
            'pixmap_fd': self.pixmap_fd,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'BufferFromPixmapReplyReply':
        return BufferFromPixmapReplyReply(**BufferFromPixmapReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return BufferFromPixmapReplyReplyPacket.pack(**self.as_dict())


class BufferFromPixmapReplyReplyCType(ctypes.Structure):
    """dri3 BufferFromPixmap_reply"""
    _fields_ = [
        ("nfd", ctypes.c_uint8),
        ("size", ctypes.c_uint32),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("stride", ctypes.c_uint16),
        ("depth", ctypes.c_uint8),
        ("bpp", ctypes.c_uint8),
        ("pixmap_fd", ctypes.c_int32),
        ("pad0", ctypes.c_uint8 * 12),
    ]


FenceFromFdRequestPacket = DataPacket((
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('fence', FixedDataPacketField(MARKER_UINT32)),
    ('initially_triggered', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
    ('fence_fd', FixedDataPacketField(file_descriptor)),
))


class FenceFromFdRequest:
    OPCODE = 4

    __slots__ = ('drawable', 'fence', 'initially_triggered', 'fence_fd',)

    def __init__(
            self, *,
            drawable: Optional[int] = None,
            fence: Optional[int] = None,
            initially_triggered: Optional[bool] = None,
            fence_fd: Optional[int] = None,
    ) -> None:
        self.drawable = drawable
        self.fence = fence
        self.initially_triggered = initially_triggered
        self.fence_fd = fence_fd

    def as_dict(self) -> Dict[str, Any]:
        return {
            'drawable': self.drawable,
            'fence': self.fence,
            'initially_triggered': self.initially_triggered,
            'fence_fd': self.fence_fd,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'FenceFromFdRequest':
        return FenceFromFdRequest(**FenceFromFdRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return FenceFromFdRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, bool, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        FenceFromFdRequest.lib = library.dri3_fencefromfd
        FenceFromFdRequest.lib.restype = ctypes.c_uint32
        FenceFromFdRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int8, ctypes.c_uint8 * 3, ctypes.c_int32)


class FenceFromFdRequestCType(ctypes.Structure):
    """dri3 FenceFromFD"""
    _fields_ = [
        ("drawable", ctypes.c_uint32),
        ("fence", ctypes.c_uint32),
        ("initially_triggered", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 3),
        ("fence_fd", ctypes.c_int32),
    ]


FdfromFenceRequestCookie = NewType('FdfromFenceRequestCookie', ctypes.c_uint32)


FdfromFenceRequestPacket = DataPacket((
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('fence', FixedDataPacketField(MARKER_UINT32)),
))


class FdfromFenceRequest:
    OPCODE = 5

    __slots__ = ('drawable', 'fence',)

    def __init__(
            self, *,
            drawable: Optional[int] = None,
            fence: Optional[int] = None,
    ) -> None:
        self.drawable = drawable
        self.fence = fence

    def as_dict(self) -> Dict[str, Any]:
        return {
            'drawable': self.drawable,
            'fence': self.fence,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'FdfromFenceRequest':
        return FdfromFenceRequest(**FdfromFenceRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return FdfromFenceRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], FdfromFenceRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        FdfromFenceRequest.lib = library.dri3_fdfromfence
        FdfromFenceRequest.lib.restype = FdfromFenceRequestCookie
        FdfromFenceRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class FdfromFenceRequestCType(ctypes.Structure):
    """dri3 FDFromFence"""
    _fields_ = [
        ("drawable", ctypes.c_uint32),
        ("fence", ctypes.c_uint32),
    ]


FdfromFenceReplyReplyPacket = DataPacket((
    ('nfd', FixedDataPacketField(MARKER_UINT8)),
    ('fence_fd', FixedDataPacketField(file_descriptor)),
    ('pad0', FixedPadDataPacketField(24)),
))


class FdfromFenceReplyReply:
    __slots__ = ('nfd', 'fence_fd',)

    def __init__(
            self, *,
            nfd: Optional[int] = None,
            fence_fd: Optional[int] = None,
    ) -> None:
        self.nfd = nfd
        self.fence_fd = fence_fd

    def as_dict(self) -> Dict[str, Any]:
        return {
            'nfd': self.nfd,
            'fence_fd': self.fence_fd,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'FdfromFenceReplyReply':
        return FdfromFenceReplyReply(**FdfromFenceReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return FdfromFenceReplyReplyPacket.pack(**self.as_dict())


class FdfromFenceReplyReplyCType(ctypes.Structure):
    """dri3 FDFromFence_reply"""
    _fields_ = [
        ("nfd", ctypes.c_uint8),
        ("fence_fd", ctypes.c_int32),
        ("pad0", ctypes.c_uint8 * 24),
    ]


GetSupportedModifiersRequestCookie = NewType('GetSupportedModifiersRequestCookie', ctypes.c_uint32)


GetSupportedModifiersRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('depth', FixedDataPacketField(MARKER_UINT8)),
    ('bpp', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
))


class GetSupportedModifiersRequest:
    OPCODE = 6

    __slots__ = ('window', 'depth', 'bpp',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            depth: Optional[int] = None,
            bpp: Optional[int] = None,
    ) -> None:
        self.window = window
        self.depth = depth
        self.bpp = bpp

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'depth': self.depth,
            'bpp': self.bpp,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetSupportedModifiersRequest':
        return GetSupportedModifiersRequest(**GetSupportedModifiersRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetSupportedModifiersRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], GetSupportedModifiersRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetSupportedModifiersRequest.lib = library.dri3_getsupportedmodifiers
        GetSupportedModifiersRequest.lib.restype = GetSupportedModifiersRequestCookie
        GetSupportedModifiersRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8 * 2)


class GetSupportedModifiersRequestCType(ctypes.Structure):
    """dri3 GetSupportedModifiers"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("depth", ctypes.c_uint8),
        ("bpp", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 2),
    ]


GetSupportedModifiersReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('num_window_modifiers', FixedDataPacketField(MARKER_UINT32)),
    ('num_screen_modifiers', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(16)),
    ('window_modifiers', SimpleListDataPacketField(MARKER_UINT64, lambda d, c: d['num_window_modifiers'], 0)),
    ('screen_modifiers', SimpleListDataPacketField(MARKER_UINT64, lambda d, c: d['num_screen_modifiers'], 0)),
))


class GetSupportedModifiersReplyReply:
    __slots__ = ('num_window_modifiers', 'num_screen_modifiers', 'window_modifiers', 'screen_modifiers',)

    def __init__(
            self, *,
            num_window_modifiers: Optional[int] = None,
            num_screen_modifiers: Optional[int] = None,
            window_modifiers: Optional[Sequence[int]] = None,
            screen_modifiers: Optional[Sequence[int]] = None,
    ) -> None:
        self.num_window_modifiers = num_window_modifiers
        self.num_screen_modifiers = num_screen_modifiers
        self.window_modifiers = window_modifiers
        self.screen_modifiers = screen_modifiers

    def as_dict(self) -> Dict[str, Any]:
        return {
            'num_window_modifiers': self.num_window_modifiers,
            'num_screen_modifiers': self.num_screen_modifiers,
            'window_modifiers': self.window_modifiers,
            'screen_modifiers': self.screen_modifiers,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetSupportedModifiersReplyReply':
        return GetSupportedModifiersReplyReply(**GetSupportedModifiersReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetSupportedModifiersReplyReplyPacket.pack(**self.as_dict())


class GetSupportedModifiersReplyReplyCType(ctypes.Structure):
    """dri3 GetSupportedModifiers_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("num_window_modifiers", ctypes.c_uint32),
        ("num_screen_modifiers", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 16),
        ("var_data", ctypes.c_void_p),
    ]


PixmapFromBuffersRequestPacket = DataPacket((
    ('pixmap', FixedDataPacketField(MARKER_UINT32)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('num_buffers', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('stride0', FixedDataPacketField(MARKER_UINT32)),
    ('offset0', FixedDataPacketField(MARKER_UINT32)),
    ('stride1', FixedDataPacketField(MARKER_UINT32)),
    ('offset1', FixedDataPacketField(MARKER_UINT32)),
    ('stride2', FixedDataPacketField(MARKER_UINT32)),
    ('offset2', FixedDataPacketField(MARKER_UINT32)),
    ('stride3', FixedDataPacketField(MARKER_UINT32)),
    ('offset3', FixedDataPacketField(MARKER_UINT32)),
    ('depth', FixedDataPacketField(MARKER_UINT8)),
    ('bpp', FixedDataPacketField(MARKER_UINT8)),
    ('pad1', FixedPadDataPacketField(2)),
    ('modifier', FixedDataPacketField(MARKER_UINT64)),
    ('buffers', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_buffers'], 0)),
))


class PixmapFromBuffersRequest:
    OPCODE = 7

    __slots__ = ('pixmap', 'window', 'num_buffers', 'width', 'height', 'stride0', 'offset0', 'stride1', 'offset1', 'stride2', 'offset2', 'stride3', 'offset3', 'depth', 'bpp', 'modifier', 'buffers',)

    def __init__(
            self, *,
            pixmap: Optional[int] = None,
            window: Optional[int] = None,
            num_buffers: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            stride0: Optional[int] = None,
            offset0: Optional[int] = None,
            stride1: Optional[int] = None,
            offset1: Optional[int] = None,
            stride2: Optional[int] = None,
            offset2: Optional[int] = None,
            stride3: Optional[int] = None,
            offset3: Optional[int] = None,
            depth: Optional[int] = None,
            bpp: Optional[int] = None,
            modifier: Optional[int] = None,
            buffers: Optional[Sequence[int]] = None,
    ) -> None:
        self.pixmap = pixmap
        self.window = window
        self.num_buffers = num_buffers
        self.width = width
        self.height = height
        self.stride0 = stride0
        self.offset0 = offset0
        self.stride1 = stride1
        self.offset1 = offset1
        self.stride2 = stride2
        self.offset2 = offset2
        self.stride3 = stride3
        self.offset3 = offset3
        self.depth = depth
        self.bpp = bpp
        self.modifier = modifier
        self.buffers = buffers

    def as_dict(self) -> Dict[str, Any]:
        return {
            'pixmap': self.pixmap,
            'window': self.window,
            'num_buffers': self.num_buffers,
            'width': self.width,
            'height': self.height,
            'stride0': self.stride0,
            'offset0': self.offset0,
            'stride1': self.stride1,
            'offset1': self.offset1,
            'stride2': self.stride2,
            'offset2': self.offset2,
            'stride3': self.stride3,
            'offset3': self.offset3,
            'depth': self.depth,
            'bpp': self.bpp,
            'modifier': self.modifier,
            'buffers': self.buffers,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PixmapFromBuffersRequest':
        return PixmapFromBuffersRequest(**PixmapFromBuffersRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PixmapFromBuffersRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PixmapFromBuffersRequest.lib = library.dri3_pixmapfrombuffers
        PixmapFromBuffersRequest.lib.restype = ctypes.c_uint32
        PixmapFromBuffersRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8 * 3, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8 * 2, ctypes.c_uint64, ctypes.c_void_p)


class PixmapFromBuffersRequestCType(ctypes.Structure):
    """dri3 PixmapFromBuffers"""
    _fields_ = [
        ("pixmap", ctypes.c_uint32),
        ("window", ctypes.c_uint32),
        ("num_buffers", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("stride0", ctypes.c_uint32),
        ("offset0", ctypes.c_uint32),
        ("stride1", ctypes.c_uint32),
        ("offset1", ctypes.c_uint32),
        ("stride2", ctypes.c_uint32),
        ("offset2", ctypes.c_uint32),
        ("stride3", ctypes.c_uint32),
        ("offset3", ctypes.c_uint32),
        ("depth", ctypes.c_uint8),
        ("bpp", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 2),
        ("modifier", ctypes.c_uint64),
        ("var_data", ctypes.c_void_p),
    ]


BuffersFromPixmapRequestCookie = NewType('BuffersFromPixmapRequestCookie', ctypes.c_uint32)


BuffersFromPixmapRequestPacket = DataPacket((
    ('pixmap', FixedDataPacketField(MARKER_UINT32)),
))


class BuffersFromPixmapRequest:
    OPCODE = 8

    __slots__ = ('pixmap',)

    def __init__(
            self, *,
            pixmap: Optional[int] = None,
    ) -> None:
        self.pixmap = pixmap

    def as_dict(self) -> Dict[str, Any]:
        return {
            'pixmap': self.pixmap,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'BuffersFromPixmapRequest':
        return BuffersFromPixmapRequest(**BuffersFromPixmapRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return BuffersFromPixmapRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], BuffersFromPixmapRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        BuffersFromPixmapRequest.lib = library.dri3_buffersfrompixmap
        BuffersFromPixmapRequest.lib.restype = BuffersFromPixmapRequestCookie
        BuffersFromPixmapRequest.lib.argstype = (ctypes.c_uint32,)


class BuffersFromPixmapRequestCType(ctypes.Structure):
    """dri3 BuffersFromPixmap"""
    _fields_ = [
        ("pixmap", ctypes.c_uint32),
    ]


BuffersFromPixmapReplyReplyPacket = DataPacket((
    ('nfd', FixedDataPacketField(MARKER_UINT8)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(4)),
    ('modifier', FixedDataPacketField(MARKER_UINT64)),
    ('depth', FixedDataPacketField(MARKER_UINT8)),
    ('bpp', FixedDataPacketField(MARKER_UINT8)),
    ('pad1', FixedPadDataPacketField(6)),
    ('strides', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nfd'], 0)),
    ('offsets', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nfd'], 0)),
    ('buffers', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nfd'], 0)),
))


class BuffersFromPixmapReplyReply:
    __slots__ = ('nfd', 'width', 'height', 'modifier', 'depth', 'bpp', 'strides', 'offsets', 'buffers',)

    def __init__(
            self, *,
            nfd: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            modifier: Optional[int] = None,
            depth: Optional[int] = None,
            bpp: Optional[int] = None,
            strides: Optional[Sequence[int]] = None,
            offsets: Optional[Sequence[int]] = None,
            buffers: Optional[Sequence[int]] = None,
    ) -> None:
        self.nfd = nfd
        self.width = width
        self.height = height
        self.modifier = modifier
        self.depth = depth
        self.bpp = bpp
        self.strides = strides
        self.offsets = offsets
        self.buffers = buffers

    def as_dict(self) -> Dict[str, Any]:
        return {
            'nfd': self.nfd,
            'width': self.width,
            'height': self.height,
            'modifier': self.modifier,
            'depth': self.depth,
            'bpp': self.bpp,
            'strides': self.strides,
            'offsets': self.offsets,
            'buffers': self.buffers,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'BuffersFromPixmapReplyReply':
        return BuffersFromPixmapReplyReply(**BuffersFromPixmapReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return BuffersFromPixmapReplyReplyPacket.pack(**self.as_dict())


class BuffersFromPixmapReplyReplyCType(ctypes.Structure):
    """dri3 BuffersFromPixmap_reply"""
    _fields_ = [
        ("nfd", ctypes.c_uint8),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 4),
        ("modifier", ctypes.c_uint64),
        ("depth", ctypes.c_uint8),
        ("bpp", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 6),
        ("var_data", ctypes.c_void_p),
    ]


SetDrmdeviceInUseRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('drmMajor', FixedDataPacketField(MARKER_UINT32)),
    ('drmMinor', FixedDataPacketField(MARKER_UINT32)),
))


class SetDrmdeviceInUseRequest:
    OPCODE = 9

    __slots__ = ('window', 'drmmajor', 'drmminor',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            drmmajor: Optional[int] = None,
            drmminor: Optional[int] = None,
    ) -> None:
        self.window = window
        self.drmmajor = drmmajor
        self.drmminor = drmminor

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'drmMajor': self.drmmajor,
            'drmMinor': self.drmminor,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetDrmdeviceInUseRequest':
        return SetDrmdeviceInUseRequest(**SetDrmdeviceInUseRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetDrmdeviceInUseRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetDrmdeviceInUseRequest.lib = library.dri3_setdrmdeviceinuse
        SetDrmdeviceInUseRequest.lib.restype = ctypes.c_uint32
        SetDrmdeviceInUseRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class SetDrmdeviceInUseRequestCType(ctypes.Structure):
    """dri3 SetDRMDeviceInUse"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("drmMajor", ctypes.c_uint32),
        ("drmMinor", ctypes.c_uint32),
    ]


# ------------------------------------------------------------------
# Unions

