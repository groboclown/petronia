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

SoType = NewType('SoType', int)


class SoValues:
    SET = SoType(0)
    UNION = SoType(1)
    INTERSECT = SoType(2)
    SUBTRACT = SoType(3)
    INVERT = SoType(4)


SkType = NewType('SkType', int)


class SkValues:
    BOUNDING = SkType(0)
    CLIP = SkType(1)
    INPUT = SkType(2)


# ------------------------------------------------------------------
# Aliases



# ------------------------------------------------------------------
# Structures, Events, Requests, Replies


NotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('shape_kind', FixedDataPacketField(MARKER_UINT32)),
    ('affected_window', FixedDataPacketField(MARKER_UINT32)),
    ('extents_x', FixedDataPacketField(MARKER_INT16)),
    ('extents_y', FixedDataPacketField(MARKER_INT16)),
    ('extents_width', FixedDataPacketField(MARKER_UINT16)),
    ('extents_height', FixedDataPacketField(MARKER_UINT16)),
    ('server_time', FixedDataPacketField(MARKER_UINT32)),
    ('shaped', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(11)),
))


class NotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'shape_kind', 'affected_window', 'extents_x', 'extents_y', 'extents_width', 'extents_height', 'server_time', 'shaped',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            shape_kind: Optional[int] = None,
            affected_window: Optional[int] = None,
            extents_x: Optional[int] = None,
            extents_y: Optional[int] = None,
            extents_width: Optional[int] = None,
            extents_height: Optional[int] = None,
            server_time: Optional[int] = None,
            shaped: Optional[bool] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.shape_kind = shape_kind
        self.affected_window = affected_window
        self.extents_x = extents_x
        self.extents_y = extents_y
        self.extents_width = extents_width
        self.extents_height = extents_height
        self.server_time = server_time
        self.shaped = shaped

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'shape_kind': self.shape_kind,
            'affected_window': self.affected_window,
            'extents_x': self.extents_x,
            'extents_y': self.extents_y,
            'extents_width': self.extents_width,
            'extents_height': self.extents_height,
            'server_time': self.server_time,
            'shaped': self.shaped,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'NotifyEvent':
        return NotifyEvent(**NotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return NotifyEventPacket.pack(**self.as_dict())


class NotifyEventCType(ctypes.Structure):
    """shape Notify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("shape_kind", ctypes.c_uint32),
        ("affected_window", ctypes.c_uint32),
        ("extents_x", ctypes.c_int16),
        ("extents_y", ctypes.c_int16),
        ("extents_width", ctypes.c_uint16),
        ("extents_height", ctypes.c_uint16),
        ("server_time", ctypes.c_uint32),
        ("shaped", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 11),
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
        QueryVersionRequest.lib = library.shape_queryversion
        QueryVersionRequest.lib.restype = QueryVersionRequestCookie
        QueryVersionRequest.lib.argstype = ()


class QueryVersionRequestCType(ctypes.Structure):
    """shape QueryVersion"""
    _fields_ = [
    ]


QueryVersionReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('major_version', FixedDataPacketField(MARKER_UINT16)),
    ('minor_version', FixedDataPacketField(MARKER_UINT16)),
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
    """shape QueryVersion_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("major_version", ctypes.c_uint16),
        ("minor_version", ctypes.c_uint16),
    ]


RectanglesRequestPacket = DataPacket((
    ('operation', FixedDataPacketField(MARKER_UINT32)),
    ('destination_kind', FixedDataPacketField(MARKER_UINT32)),
    ('ordering', FixedDataPacketField(MARKER_INT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('destination_window', FixedDataPacketField(MARKER_UINT32)),
    ('x_offset', FixedDataPacketField(MARKER_INT16)),
    ('y_offset', FixedDataPacketField(MARKER_INT16)),
    ('rectangles', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 1, 0)),
))


class RectanglesRequest:
    OPCODE = 1

    __slots__ = ('operation', 'destination_kind', 'ordering', 'destination_window', 'x_offset', 'y_offset', 'rectangles',)

    def __init__(
            self, *,
            operation: Optional[int] = None,
            destination_kind: Optional[int] = None,
            ordering: Optional[int] = None,
            destination_window: Optional[int] = None,
            x_offset: Optional[int] = None,
            y_offset: Optional[int] = None,
            rectangles: Optional[Sequence[int]] = None,
    ) -> None:
        self.operation = operation
        self.destination_kind = destination_kind
        self.ordering = ordering
        self.destination_window = destination_window
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.rectangles = rectangles

    def as_dict(self) -> Dict[str, Any]:
        return {
            'operation': self.operation,
            'destination_kind': self.destination_kind,
            'ordering': self.ordering,
            'destination_window': self.destination_window,
            'x_offset': self.x_offset,
            'y_offset': self.y_offset,
            'rectangles': self.rectangles,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'RectanglesRequest':
        return RectanglesRequest(**RectanglesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return RectanglesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        RectanglesRequest.lib = library.shape_rectangles
        RectanglesRequest.lib.restype = ctypes.c_uint32
        RectanglesRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int8, ctypes.c_uint8, ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16, ctypes.c_void_p)


class RectanglesRequestCType(ctypes.Structure):
    """shape Rectangles"""
    _fields_ = [
        ("operation", ctypes.c_uint32),
        ("destination_kind", ctypes.c_uint32),
        ("ordering", ctypes.c_int8),
        ("pad0", ctypes.c_uint8),
        ("destination_window", ctypes.c_uint32),
        ("x_offset", ctypes.c_int16),
        ("y_offset", ctypes.c_int16),
        ("var_data", ctypes.c_void_p),
    ]


MaskRequestPacket = DataPacket((
    ('operation', FixedDataPacketField(MARKER_UINT32)),
    ('destination_kind', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(2)),
    ('destination_window', FixedDataPacketField(MARKER_UINT32)),
    ('x_offset', FixedDataPacketField(MARKER_INT16)),
    ('y_offset', FixedDataPacketField(MARKER_INT16)),
    ('source_bitmap', FixedDataPacketField(MARKER_UINT32)),
))


class MaskRequest:
    OPCODE = 2

    __slots__ = ('operation', 'destination_kind', 'destination_window', 'x_offset', 'y_offset', 'source_bitmap',)

    def __init__(
            self, *,
            operation: Optional[int] = None,
            destination_kind: Optional[int] = None,
            destination_window: Optional[int] = None,
            x_offset: Optional[int] = None,
            y_offset: Optional[int] = None,
            source_bitmap: Optional[int] = None,
    ) -> None:
        self.operation = operation
        self.destination_kind = destination_kind
        self.destination_window = destination_window
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.source_bitmap = source_bitmap

    def as_dict(self) -> Dict[str, Any]:
        return {
            'operation': self.operation,
            'destination_kind': self.destination_kind,
            'destination_window': self.destination_window,
            'x_offset': self.x_offset,
            'y_offset': self.y_offset,
            'source_bitmap': self.source_bitmap,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'MaskRequest':
        return MaskRequest(**MaskRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return MaskRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        MaskRequest.lib = library.shape_mask
        MaskRequest.lib.restype = ctypes.c_uint32
        MaskRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8 * 2, ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16, ctypes.c_uint32)


class MaskRequestCType(ctypes.Structure):
    """shape Mask"""
    _fields_ = [
        ("operation", ctypes.c_uint32),
        ("destination_kind", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 2),
        ("destination_window", ctypes.c_uint32),
        ("x_offset", ctypes.c_int16),
        ("y_offset", ctypes.c_int16),
        ("source_bitmap", ctypes.c_uint32),
    ]


CombineRequestPacket = DataPacket((
    ('operation', FixedDataPacketField(MARKER_UINT32)),
    ('destination_kind', FixedDataPacketField(MARKER_UINT32)),
    ('source_kind', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(1)),
    ('destination_window', FixedDataPacketField(MARKER_UINT32)),
    ('x_offset', FixedDataPacketField(MARKER_INT16)),
    ('y_offset', FixedDataPacketField(MARKER_INT16)),
    ('source_window', FixedDataPacketField(MARKER_UINT32)),
))


class CombineRequest:
    OPCODE = 3

    __slots__ = ('operation', 'destination_kind', 'source_kind', 'destination_window', 'x_offset', 'y_offset', 'source_window',)

    def __init__(
            self, *,
            operation: Optional[int] = None,
            destination_kind: Optional[int] = None,
            source_kind: Optional[int] = None,
            destination_window: Optional[int] = None,
            x_offset: Optional[int] = None,
            y_offset: Optional[int] = None,
            source_window: Optional[int] = None,
    ) -> None:
        self.operation = operation
        self.destination_kind = destination_kind
        self.source_kind = source_kind
        self.destination_window = destination_window
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.source_window = source_window

    def as_dict(self) -> Dict[str, Any]:
        return {
            'operation': self.operation,
            'destination_kind': self.destination_kind,
            'source_kind': self.source_kind,
            'destination_window': self.destination_window,
            'x_offset': self.x_offset,
            'y_offset': self.y_offset,
            'source_window': self.source_window,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CombineRequest':
        return CombineRequest(**CombineRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CombineRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CombineRequest.lib = library.shape_combine
        CombineRequest.lib.restype = ctypes.c_uint32
        CombineRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16, ctypes.c_uint32)


class CombineRequestCType(ctypes.Structure):
    """shape Combine"""
    _fields_ = [
        ("operation", ctypes.c_uint32),
        ("destination_kind", ctypes.c_uint32),
        ("source_kind", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8),
        ("destination_window", ctypes.c_uint32),
        ("x_offset", ctypes.c_int16),
        ("y_offset", ctypes.c_int16),
        ("source_window", ctypes.c_uint32),
    ]


OffsetRequestPacket = DataPacket((
    ('destination_kind', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(3)),
    ('destination_window', FixedDataPacketField(MARKER_UINT32)),
    ('x_offset', FixedDataPacketField(MARKER_INT16)),
    ('y_offset', FixedDataPacketField(MARKER_INT16)),
))


class OffsetRequest:
    OPCODE = 4

    __slots__ = ('destination_kind', 'destination_window', 'x_offset', 'y_offset',)

    def __init__(
            self, *,
            destination_kind: Optional[int] = None,
            destination_window: Optional[int] = None,
            x_offset: Optional[int] = None,
            y_offset: Optional[int] = None,
    ) -> None:
        self.destination_kind = destination_kind
        self.destination_window = destination_window
        self.x_offset = x_offset
        self.y_offset = y_offset

    def as_dict(self) -> Dict[str, Any]:
        return {
            'destination_kind': self.destination_kind,
            'destination_window': self.destination_window,
            'x_offset': self.x_offset,
            'y_offset': self.y_offset,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'OffsetRequest':
        return OffsetRequest(**OffsetRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return OffsetRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        OffsetRequest.lib = library.shape_offset
        OffsetRequest.lib.restype = ctypes.c_uint32
        OffsetRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint8 * 3, ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16)


class OffsetRequestCType(ctypes.Structure):
    """shape Offset"""
    _fields_ = [
        ("destination_kind", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 3),
        ("destination_window", ctypes.c_uint32),
        ("x_offset", ctypes.c_int16),
        ("y_offset", ctypes.c_int16),
    ]


QueryExtentsRequestCookie = NewType('QueryExtentsRequestCookie', ctypes.c_uint32)


QueryExtentsRequestPacket = DataPacket((
    ('destination_window', FixedDataPacketField(MARKER_UINT32)),
))


class QueryExtentsRequest:
    OPCODE = 5

    __slots__ = ('destination_window',)

    def __init__(
            self, *,
            destination_window: Optional[int] = None,
    ) -> None:
        self.destination_window = destination_window

    def as_dict(self) -> Dict[str, Any]:
        return {
            'destination_window': self.destination_window,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryExtentsRequest':
        return QueryExtentsRequest(**QueryExtentsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryExtentsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], QueryExtentsRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryExtentsRequest.lib = library.shape_queryextents
        QueryExtentsRequest.lib.restype = QueryExtentsRequestCookie
        QueryExtentsRequest.lib.argstype = (ctypes.c_uint32,)


class QueryExtentsRequestCType(ctypes.Structure):
    """shape QueryExtents"""
    _fields_ = [
        ("destination_window", ctypes.c_uint32),
    ]


QueryExtentsReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('bounding_shaped', FixedDataPacketField(MARKER_UINT8)),
    ('clip_shaped', FixedDataPacketField(MARKER_UINT8)),
    ('pad1', FixedPadDataPacketField(2)),
    ('bounding_shape_extents_x', FixedDataPacketField(MARKER_INT16)),
    ('bounding_shape_extents_y', FixedDataPacketField(MARKER_INT16)),
    ('bounding_shape_extents_width', FixedDataPacketField(MARKER_UINT16)),
    ('bounding_shape_extents_height', FixedDataPacketField(MARKER_UINT16)),
    ('clip_shape_extents_x', FixedDataPacketField(MARKER_INT16)),
    ('clip_shape_extents_y', FixedDataPacketField(MARKER_INT16)),
    ('clip_shape_extents_width', FixedDataPacketField(MARKER_UINT16)),
    ('clip_shape_extents_height', FixedDataPacketField(MARKER_UINT16)),
))


class QueryExtentsReplyReply:
    __slots__ = ('bounding_shaped', 'clip_shaped', 'bounding_shape_extents_x', 'bounding_shape_extents_y', 'bounding_shape_extents_width', 'bounding_shape_extents_height', 'clip_shape_extents_x', 'clip_shape_extents_y', 'clip_shape_extents_width', 'clip_shape_extents_height',)

    def __init__(
            self, *,
            bounding_shaped: Optional[bool] = None,
            clip_shaped: Optional[bool] = None,
            bounding_shape_extents_x: Optional[int] = None,
            bounding_shape_extents_y: Optional[int] = None,
            bounding_shape_extents_width: Optional[int] = None,
            bounding_shape_extents_height: Optional[int] = None,
            clip_shape_extents_x: Optional[int] = None,
            clip_shape_extents_y: Optional[int] = None,
            clip_shape_extents_width: Optional[int] = None,
            clip_shape_extents_height: Optional[int] = None,
    ) -> None:
        self.bounding_shaped = bounding_shaped
        self.clip_shaped = clip_shaped
        self.bounding_shape_extents_x = bounding_shape_extents_x
        self.bounding_shape_extents_y = bounding_shape_extents_y
        self.bounding_shape_extents_width = bounding_shape_extents_width
        self.bounding_shape_extents_height = bounding_shape_extents_height
        self.clip_shape_extents_x = clip_shape_extents_x
        self.clip_shape_extents_y = clip_shape_extents_y
        self.clip_shape_extents_width = clip_shape_extents_width
        self.clip_shape_extents_height = clip_shape_extents_height

    def as_dict(self) -> Dict[str, Any]:
        return {
            'bounding_shaped': self.bounding_shaped,
            'clip_shaped': self.clip_shaped,
            'bounding_shape_extents_x': self.bounding_shape_extents_x,
            'bounding_shape_extents_y': self.bounding_shape_extents_y,
            'bounding_shape_extents_width': self.bounding_shape_extents_width,
            'bounding_shape_extents_height': self.bounding_shape_extents_height,
            'clip_shape_extents_x': self.clip_shape_extents_x,
            'clip_shape_extents_y': self.clip_shape_extents_y,
            'clip_shape_extents_width': self.clip_shape_extents_width,
            'clip_shape_extents_height': self.clip_shape_extents_height,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryExtentsReplyReply':
        return QueryExtentsReplyReply(**QueryExtentsReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryExtentsReplyReplyPacket.pack(**self.as_dict())


class QueryExtentsReplyReplyCType(ctypes.Structure):
    """shape QueryExtents_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("bounding_shaped", ctypes.c_int8),
        ("clip_shaped", ctypes.c_int8),
        ("pad1", ctypes.c_uint8 * 2),
        ("bounding_shape_extents_x", ctypes.c_int16),
        ("bounding_shape_extents_y", ctypes.c_int16),
        ("bounding_shape_extents_width", ctypes.c_uint16),
        ("bounding_shape_extents_height", ctypes.c_uint16),
        ("clip_shape_extents_x", ctypes.c_int16),
        ("clip_shape_extents_y", ctypes.c_int16),
        ("clip_shape_extents_width", ctypes.c_uint16),
        ("clip_shape_extents_height", ctypes.c_uint16),
    ]


SelectInputRequestPacket = DataPacket((
    ('destination_window', FixedDataPacketField(MARKER_UINT32)),
    ('enable', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class SelectInputRequest:
    OPCODE = 6

    __slots__ = ('destination_window', 'enable',)

    def __init__(
            self, *,
            destination_window: Optional[int] = None,
            enable: Optional[bool] = None,
    ) -> None:
        self.destination_window = destination_window
        self.enable = enable

    def as_dict(self) -> Dict[str, Any]:
        return {
            'destination_window': self.destination_window,
            'enable': self.enable,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SelectInputRequest':
        return SelectInputRequest(**SelectInputRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SelectInputRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, bool], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SelectInputRequest.lib = library.shape_selectinput
        SelectInputRequest.lib.restype = ctypes.c_uint32
        SelectInputRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_int8, ctypes.c_uint8 * 3)


class SelectInputRequestCType(ctypes.Structure):
    """shape SelectInput"""
    _fields_ = [
        ("destination_window", ctypes.c_uint32),
        ("enable", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


InputSelectedRequestCookie = NewType('InputSelectedRequestCookie', ctypes.c_uint32)


InputSelectedRequestPacket = DataPacket((
    ('destination_window', FixedDataPacketField(MARKER_UINT32)),
))


class InputSelectedRequest:
    OPCODE = 7

    __slots__ = ('destination_window',)

    def __init__(
            self, *,
            destination_window: Optional[int] = None,
    ) -> None:
        self.destination_window = destination_window

    def as_dict(self) -> Dict[str, Any]:
        return {
            'destination_window': self.destination_window,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'InputSelectedRequest':
        return InputSelectedRequest(**InputSelectedRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return InputSelectedRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], InputSelectedRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        InputSelectedRequest.lib = library.shape_inputselected
        InputSelectedRequest.lib.restype = InputSelectedRequestCookie
        InputSelectedRequest.lib.argstype = (ctypes.c_uint32,)


class InputSelectedRequestCType(ctypes.Structure):
    """shape InputSelected"""
    _fields_ = [
        ("destination_window", ctypes.c_uint32),
    ]


InputSelectedReplyReplyPacket = DataPacket((
    ('enabled', FixedDataPacketField(MARKER_UINT8)),
))


class InputSelectedReplyReply:
    __slots__ = ('enabled',)

    def __init__(
            self, *,
            enabled: Optional[bool] = None,
    ) -> None:
        self.enabled = enabled

    def as_dict(self) -> Dict[str, Any]:
        return {
            'enabled': self.enabled,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'InputSelectedReplyReply':
        return InputSelectedReplyReply(**InputSelectedReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return InputSelectedReplyReplyPacket.pack(**self.as_dict())


class InputSelectedReplyReplyCType(ctypes.Structure):
    """shape InputSelected_reply"""
    _fields_ = [
        ("enabled", ctypes.c_int8),
    ]


GetRectanglesRequestCookie = NewType('GetRectanglesRequestCookie', ctypes.c_uint32)


GetRectanglesRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('source_kind', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(3)),
))


class GetRectanglesRequest:
    OPCODE = 8

    __slots__ = ('window', 'source_kind',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            source_kind: Optional[int] = None,
    ) -> None:
        self.window = window
        self.source_kind = source_kind

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'source_kind': self.source_kind,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetRectanglesRequest':
        return GetRectanglesRequest(**GetRectanglesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetRectanglesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], GetRectanglesRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetRectanglesRequest.lib = library.shape_getrectangles
        GetRectanglesRequest.lib.restype = GetRectanglesRequestCookie
        GetRectanglesRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8 * 3)


class GetRectanglesRequestCType(ctypes.Structure):
    """shape GetRectangles"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("source_kind", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 3),
    ]


GetRectanglesReplyReplyPacket = DataPacket((
    ('ordering', FixedDataPacketField(MARKER_INT8)),
    ('rectangles_len', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(20)),
    ('rectangles', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['rectangles_len'], 0)),
))


class GetRectanglesReplyReply:
    __slots__ = ('ordering', 'rectangles_len', 'rectangles',)

    def __init__(
            self, *,
            ordering: Optional[int] = None,
            rectangles_len: Optional[int] = None,
            rectangles: Optional[Sequence[int]] = None,
    ) -> None:
        self.ordering = ordering
        self.rectangles_len = rectangles_len
        self.rectangles = rectangles

    def as_dict(self) -> Dict[str, Any]:
        return {
            'ordering': self.ordering,
            'rectangles_len': self.rectangles_len,
            'rectangles': self.rectangles,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetRectanglesReplyReply':
        return GetRectanglesReplyReply(**GetRectanglesReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetRectanglesReplyReplyPacket.pack(**self.as_dict())


class GetRectanglesReplyReplyCType(ctypes.Structure):
    """shape GetRectangles_reply"""
    _fields_ = [
        ("ordering", ctypes.c_int8),
        ("rectangles_len", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


# ------------------------------------------------------------------
# Unions

