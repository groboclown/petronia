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

Seg = NewType('Seg', ctypes.c_uint32)


# ------------------------------------------------------------------
# Structures, Events, Requests, Replies


CompletionEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(1)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('minor_event', FixedDataPacketField(MARKER_UINT16)),
    ('major_event', FixedDataPacketField(MARKER_INT8)),
    ('pad1', FixedPadDataPacketField(1)),
    ('shmseg', FixedDataPacketField(MARKER_UINT32)),
    ('offset', FixedDataPacketField(MARKER_UINT32)),
))


class CompletionEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'drawable', 'minor_event', 'major_event', 'shmseg', 'offset',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            drawable: Optional[int] = None,
            minor_event: Optional[int] = None,
            major_event: Optional[int] = None,
            shmseg: Optional[int] = None,
            offset: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.drawable = drawable
        self.minor_event = minor_event
        self.major_event = major_event
        self.shmseg = shmseg
        self.offset = offset

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'drawable': self.drawable,
            'minor_event': self.minor_event,
            'major_event': self.major_event,
            'shmseg': self.shmseg,
            'offset': self.offset,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CompletionEvent':
        return CompletionEvent(**CompletionEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CompletionEventPacket.pack(**self.as_dict())


class CompletionEventCType(ctypes.Structure):
    """shm Completion"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8),
        ("drawable", ctypes.c_uint32),
        ("minor_event", ctypes.c_uint16),
        ("major_event", ctypes.c_int8),
        ("pad1", ctypes.c_uint8),
        ("shmseg", ctypes.c_uint32),
        ("offset", ctypes.c_uint32),
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
        QueryVersionRequest.lib = library.shm_queryversion
        QueryVersionRequest.lib.restype = QueryVersionRequestCookie
        QueryVersionRequest.lib.argstype = ()


class QueryVersionRequestCType(ctypes.Structure):
    """shm QueryVersion"""
    _fields_ = [
    ]


QueryVersionReplyReplyPacket = DataPacket((
    ('shared_pixmaps', FixedDataPacketField(MARKER_UINT8)),
    ('major_version', FixedDataPacketField(MARKER_UINT16)),
    ('minor_version', FixedDataPacketField(MARKER_UINT16)),
    ('uid', FixedDataPacketField(MARKER_UINT16)),
    ('gid', FixedDataPacketField(MARKER_UINT16)),
    ('pixmap_format', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(15)),
))


class QueryVersionReplyReply:
    __slots__ = ('shared_pixmaps', 'major_version', 'minor_version', 'uid', 'gid', 'pixmap_format',)

    def __init__(
            self, *,
            shared_pixmaps: Optional[bool] = None,
            major_version: Optional[int] = None,
            minor_version: Optional[int] = None,
            uid: Optional[int] = None,
            gid: Optional[int] = None,
            pixmap_format: Optional[int] = None,
    ) -> None:
        self.shared_pixmaps = shared_pixmaps
        self.major_version = major_version
        self.minor_version = minor_version
        self.uid = uid
        self.gid = gid
        self.pixmap_format = pixmap_format

    def as_dict(self) -> Dict[str, Any]:
        return {
            'shared_pixmaps': self.shared_pixmaps,
            'major_version': self.major_version,
            'minor_version': self.minor_version,
            'uid': self.uid,
            'gid': self.gid,
            'pixmap_format': self.pixmap_format,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryVersionReplyReply':
        return QueryVersionReplyReply(**QueryVersionReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryVersionReplyReplyPacket.pack(**self.as_dict())


class QueryVersionReplyReplyCType(ctypes.Structure):
    """shm QueryVersion_reply"""
    _fields_ = [
        ("shared_pixmaps", ctypes.c_int8),
        ("major_version", ctypes.c_uint16),
        ("minor_version", ctypes.c_uint16),
        ("uid", ctypes.c_uint16),
        ("gid", ctypes.c_uint16),
        ("pixmap_format", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 15),
    ]


AttachRequestPacket = DataPacket((
    ('shmseg', FixedDataPacketField(MARKER_UINT32)),
    ('shmid', FixedDataPacketField(MARKER_UINT32)),
    ('read_only', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class AttachRequest:
    OPCODE = 1

    __slots__ = ('shmseg', 'shmid', 'read_only',)

    def __init__(
            self, *,
            shmseg: Optional[int] = None,
            shmid: Optional[int] = None,
            read_only: Optional[bool] = None,
    ) -> None:
        self.shmseg = shmseg
        self.shmid = shmid
        self.read_only = read_only

    def as_dict(self) -> Dict[str, Any]:
        return {
            'shmseg': self.shmseg,
            'shmid': self.shmid,
            'read_only': self.read_only,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'AttachRequest':
        return AttachRequest(**AttachRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return AttachRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, bool], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        AttachRequest.lib = library.shm_attach
        AttachRequest.lib.restype = ctypes.c_uint32
        AttachRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int8, ctypes.c_uint8 * 3)


class AttachRequestCType(ctypes.Structure):
    """shm Attach"""
    _fields_ = [
        ("shmseg", ctypes.c_uint32),
        ("shmid", ctypes.c_uint32),
        ("read_only", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


DetachRequestPacket = DataPacket((
    ('shmseg', FixedDataPacketField(MARKER_UINT32)),
))


class DetachRequest:
    OPCODE = 2

    __slots__ = ('shmseg',)

    def __init__(
            self, *,
            shmseg: Optional[int] = None,
    ) -> None:
        self.shmseg = shmseg

    def as_dict(self) -> Dict[str, Any]:
        return {
            'shmseg': self.shmseg,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DetachRequest':
        return DetachRequest(**DetachRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DetachRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        DetachRequest.lib = library.shm_detach
        DetachRequest.lib.restype = ctypes.c_uint32
        DetachRequest.lib.argstype = (ctypes.c_uint32,)


class DetachRequestCType(ctypes.Structure):
    """shm Detach"""
    _fields_ = [
        ("shmseg", ctypes.c_uint32),
    ]


PutImageRequestPacket = DataPacket((
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('gc', FixedDataPacketField(MARKER_UINT32)),
    ('total_width', FixedDataPacketField(MARKER_UINT16)),
    ('total_height', FixedDataPacketField(MARKER_UINT16)),
    ('src_x', FixedDataPacketField(MARKER_UINT16)),
    ('src_y', FixedDataPacketField(MARKER_UINT16)),
    ('src_width', FixedDataPacketField(MARKER_UINT16)),
    ('src_height', FixedDataPacketField(MARKER_UINT16)),
    ('dst_x', FixedDataPacketField(MARKER_INT16)),
    ('dst_y', FixedDataPacketField(MARKER_INT16)),
    ('depth', FixedDataPacketField(MARKER_UINT8)),
    ('format', FixedDataPacketField(MARKER_UINT8)),
    ('send_event', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('shmseg', FixedDataPacketField(MARKER_UINT32)),
    ('offset', FixedDataPacketField(MARKER_UINT32)),
))


class PutImageRequest:
    OPCODE = 3

    __slots__ = ('drawable', 'gc', 'total_width', 'total_height', 'src_x', 'src_y', 'src_width', 'src_height', 'dst_x', 'dst_y', 'depth', 'format', 'send_event', 'shmseg', 'offset',)

    def __init__(
            self, *,
            drawable: Optional[int] = None,
            gc: Optional[int] = None,
            total_width: Optional[int] = None,
            total_height: Optional[int] = None,
            src_x: Optional[int] = None,
            src_y: Optional[int] = None,
            src_width: Optional[int] = None,
            src_height: Optional[int] = None,
            dst_x: Optional[int] = None,
            dst_y: Optional[int] = None,
            depth: Optional[int] = None,
            format: Optional[int] = None,
            send_event: Optional[bool] = None,
            shmseg: Optional[int] = None,
            offset: Optional[int] = None,
    ) -> None:
        self.drawable = drawable
        self.gc = gc
        self.total_width = total_width
        self.total_height = total_height
        self.src_x = src_x
        self.src_y = src_y
        self.src_width = src_width
        self.src_height = src_height
        self.dst_x = dst_x
        self.dst_y = dst_y
        self.depth = depth
        self.format = format
        self.send_event = send_event
        self.shmseg = shmseg
        self.offset = offset

    def as_dict(self) -> Dict[str, Any]:
        return {
            'drawable': self.drawable,
            'gc': self.gc,
            'total_width': self.total_width,
            'total_height': self.total_height,
            'src_x': self.src_x,
            'src_y': self.src_y,
            'src_width': self.src_width,
            'src_height': self.src_height,
            'dst_x': self.dst_x,
            'dst_y': self.dst_y,
            'depth': self.depth,
            'format': self.format,
            'send_event': self.send_event,
            'shmseg': self.shmseg,
            'offset': self.offset,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PutImageRequest':
        return PutImageRequest(**PutImageRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PutImageRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, int, int, int, int, int, bool, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PutImageRequest.lib = library.shm_putimage
        PutImageRequest.lib.restype = ctypes.c_uint32
        PutImageRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_int16, ctypes.c_int16, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_int8, ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32)


class PutImageRequestCType(ctypes.Structure):
    """shm PutImage"""
    _fields_ = [
        ("drawable", ctypes.c_uint32),
        ("gc", ctypes.c_uint32),
        ("total_width", ctypes.c_uint16),
        ("total_height", ctypes.c_uint16),
        ("src_x", ctypes.c_uint16),
        ("src_y", ctypes.c_uint16),
        ("src_width", ctypes.c_uint16),
        ("src_height", ctypes.c_uint16),
        ("dst_x", ctypes.c_int16),
        ("dst_y", ctypes.c_int16),
        ("depth", ctypes.c_uint8),
        ("format", ctypes.c_uint8),
        ("send_event", ctypes.c_int8),
        ("pad0", ctypes.c_uint8),
        ("shmseg", ctypes.c_uint32),
        ("offset", ctypes.c_uint32),
    ]


GetImageRequestCookie = NewType('GetImageRequestCookie', ctypes.c_uint32)


GetImageRequestPacket = DataPacket((
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('x', FixedDataPacketField(MARKER_INT16)),
    ('y', FixedDataPacketField(MARKER_INT16)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('plane_mask', FixedDataPacketField(MARKER_UINT32)),
    ('format', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
    ('shmseg', FixedDataPacketField(MARKER_UINT32)),
    ('offset', FixedDataPacketField(MARKER_UINT32)),
))


class GetImageRequest:
    OPCODE = 4

    __slots__ = ('drawable', 'x', 'y', 'width', 'height', 'plane_mask', 'format', 'shmseg', 'offset',)

    def __init__(
            self, *,
            drawable: Optional[int] = None,
            x: Optional[int] = None,
            y: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            plane_mask: Optional[int] = None,
            format: Optional[int] = None,
            shmseg: Optional[int] = None,
            offset: Optional[int] = None,
    ) -> None:
        self.drawable = drawable
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.plane_mask = plane_mask
        self.format = format
        self.shmseg = shmseg
        self.offset = offset

    def as_dict(self) -> Dict[str, Any]:
        return {
            'drawable': self.drawable,
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height,
            'plane_mask': self.plane_mask,
            'format': self.format,
            'shmseg': self.shmseg,
            'offset': self.offset,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetImageRequest':
        return GetImageRequest(**GetImageRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetImageRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, int, int], GetImageRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetImageRequest.lib = library.shm_getimage
        GetImageRequest.lib.restype = GetImageRequestCookie
        GetImageRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8 * 3, ctypes.c_uint32, ctypes.c_uint32)


class GetImageRequestCType(ctypes.Structure):
    """shm GetImage"""
    _fields_ = [
        ("drawable", ctypes.c_uint32),
        ("x", ctypes.c_int16),
        ("y", ctypes.c_int16),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("plane_mask", ctypes.c_uint32),
        ("format", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
        ("shmseg", ctypes.c_uint32),
        ("offset", ctypes.c_uint32),
    ]


GetImageReplyReplyPacket = DataPacket((
    ('depth', FixedDataPacketField(MARKER_UINT8)),
    ('visual', FixedDataPacketField(MARKER_UINT32)),
    ('size', FixedDataPacketField(MARKER_UINT32)),
))


class GetImageReplyReply:
    __slots__ = ('depth', 'visual', 'size',)

    def __init__(
            self, *,
            depth: Optional[int] = None,
            visual: Optional[int] = None,
            size: Optional[int] = None,
    ) -> None:
        self.depth = depth
        self.visual = visual
        self.size = size

    def as_dict(self) -> Dict[str, Any]:
        return {
            'depth': self.depth,
            'visual': self.visual,
            'size': self.size,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetImageReplyReply':
        return GetImageReplyReply(**GetImageReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetImageReplyReplyPacket.pack(**self.as_dict())


class GetImageReplyReplyCType(ctypes.Structure):
    """shm GetImage_reply"""
    _fields_ = [
        ("depth", ctypes.c_uint8),
        ("visual", ctypes.c_uint32),
        ("size", ctypes.c_uint32),
    ]


CreatePixmapRequestPacket = DataPacket((
    ('pid', FixedDataPacketField(MARKER_UINT32)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('depth', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
    ('shmseg', FixedDataPacketField(MARKER_UINT32)),
    ('offset', FixedDataPacketField(MARKER_UINT32)),
))


class CreatePixmapRequest:
    OPCODE = 5

    __slots__ = ('pid', 'drawable', 'width', 'height', 'depth', 'shmseg', 'offset',)

    def __init__(
            self, *,
            pid: Optional[int] = None,
            drawable: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            depth: Optional[int] = None,
            shmseg: Optional[int] = None,
            offset: Optional[int] = None,
    ) -> None:
        self.pid = pid
        self.drawable = drawable
        self.width = width
        self.height = height
        self.depth = depth
        self.shmseg = shmseg
        self.offset = offset

    def as_dict(self) -> Dict[str, Any]:
        return {
            'pid': self.pid,
            'drawable': self.drawable,
            'width': self.width,
            'height': self.height,
            'depth': self.depth,
            'shmseg': self.shmseg,
            'offset': self.offset,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreatePixmapRequest':
        return CreatePixmapRequest(**CreatePixmapRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreatePixmapRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreatePixmapRequest.lib = library.shm_createpixmap
        CreatePixmapRequest.lib.restype = ctypes.c_uint32
        CreatePixmapRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint8, ctypes.c_uint8 * 3, ctypes.c_uint32, ctypes.c_uint32)


class CreatePixmapRequestCType(ctypes.Structure):
    """shm CreatePixmap"""
    _fields_ = [
        ("pid", ctypes.c_uint32),
        ("drawable", ctypes.c_uint32),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("depth", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
        ("shmseg", ctypes.c_uint32),
        ("offset", ctypes.c_uint32),
    ]


AttachFdRequestPacket = DataPacket((
    ('shmseg', FixedDataPacketField(MARKER_UINT32)),
    ('shm_fd', FixedDataPacketField(file_descriptor)),
    ('read_only', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class AttachFdRequest:
    OPCODE = 6

    __slots__ = ('shmseg', 'shm_fd', 'read_only',)

    def __init__(
            self, *,
            shmseg: Optional[int] = None,
            shm_fd: Optional[int] = None,
            read_only: Optional[bool] = None,
    ) -> None:
        self.shmseg = shmseg
        self.shm_fd = shm_fd
        self.read_only = read_only

    def as_dict(self) -> Dict[str, Any]:
        return {
            'shmseg': self.shmseg,
            'shm_fd': self.shm_fd,
            'read_only': self.read_only,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'AttachFdRequest':
        return AttachFdRequest(**AttachFdRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return AttachFdRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, bool], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        AttachFdRequest.lib = library.shm_attachfd
        AttachFdRequest.lib.restype = ctypes.c_uint32
        AttachFdRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_int32, ctypes.c_int8, ctypes.c_uint8 * 3)


class AttachFdRequestCType(ctypes.Structure):
    """shm AttachFd"""
    _fields_ = [
        ("shmseg", ctypes.c_uint32),
        ("shm_fd", ctypes.c_int32),
        ("read_only", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


CreateSegmentRequestCookie = NewType('CreateSegmentRequestCookie', ctypes.c_uint32)


CreateSegmentRequestPacket = DataPacket((
    ('shmseg', FixedDataPacketField(MARKER_UINT32)),
    ('size', FixedDataPacketField(MARKER_UINT32)),
    ('read_only', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class CreateSegmentRequest:
    OPCODE = 7

    __slots__ = ('shmseg', 'size', 'read_only',)

    def __init__(
            self, *,
            shmseg: Optional[int] = None,
            size: Optional[int] = None,
            read_only: Optional[bool] = None,
    ) -> None:
        self.shmseg = shmseg
        self.size = size
        self.read_only = read_only

    def as_dict(self) -> Dict[str, Any]:
        return {
            'shmseg': self.shmseg,
            'size': self.size,
            'read_only': self.read_only,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateSegmentRequest':
        return CreateSegmentRequest(**CreateSegmentRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateSegmentRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, bool], CreateSegmentRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateSegmentRequest.lib = library.shm_createsegment
        CreateSegmentRequest.lib.restype = CreateSegmentRequestCookie
        CreateSegmentRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int8, ctypes.c_uint8 * 3)


class CreateSegmentRequestCType(ctypes.Structure):
    """shm CreateSegment"""
    _fields_ = [
        ("shmseg", ctypes.c_uint32),
        ("size", ctypes.c_uint32),
        ("read_only", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


CreateSegmentReplyReplyPacket = DataPacket((
    ('nfd', FixedDataPacketField(MARKER_UINT8)),
    ('shm_fd', FixedDataPacketField(file_descriptor)),
    ('pad0', FixedPadDataPacketField(24)),
))


class CreateSegmentReplyReply:
    __slots__ = ('nfd', 'shm_fd',)

    def __init__(
            self, *,
            nfd: Optional[int] = None,
            shm_fd: Optional[int] = None,
    ) -> None:
        self.nfd = nfd
        self.shm_fd = shm_fd

    def as_dict(self) -> Dict[str, Any]:
        return {
            'nfd': self.nfd,
            'shm_fd': self.shm_fd,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateSegmentReplyReply':
        return CreateSegmentReplyReply(**CreateSegmentReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateSegmentReplyReplyPacket.pack(**self.as_dict())


class CreateSegmentReplyReplyCType(ctypes.Structure):
    """shm CreateSegment_reply"""
    _fields_ = [
        ("nfd", ctypes.c_uint8),
        ("shm_fd", ctypes.c_int32),
        ("pad0", ctypes.c_uint8 * 24),
    ]


# ------------------------------------------------------------------
# Unions

