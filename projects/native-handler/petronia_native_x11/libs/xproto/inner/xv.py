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

TypeType = NewType('TypeType', int)


class TypeValues:
    INPUT_MASK = TypeType(1)
    OUTPUT_MASK = TypeType(2)
    VIDEO_MASK = TypeType(4)
    STILL_MASK = TypeType(8)
    IMAGE_MASK = TypeType(16)


ImageFormatInfoTypeType = NewType('ImageFormatInfoTypeType', int)


class ImageFormatInfoTypeValues:
    RGB = ImageFormatInfoTypeType(0)
    YUV = ImageFormatInfoTypeType(1)


ImageFormatInfoFormatType = NewType('ImageFormatInfoFormatType', int)


class ImageFormatInfoFormatValues:
    PACKED = ImageFormatInfoFormatType(0)
    PLANAR = ImageFormatInfoFormatType(1)


AttributeFlagType = NewType('AttributeFlagType', int)


class AttributeFlagValues:
    GETTABLE = AttributeFlagType(1)
    SETTABLE = AttributeFlagType(2)


VideoNotifyReasonType = NewType('VideoNotifyReasonType', int)


class VideoNotifyReasonValues:
    STARTED = VideoNotifyReasonType(0)
    STOPPED = VideoNotifyReasonType(1)
    BUSY = VideoNotifyReasonType(2)
    PREEMPTED = VideoNotifyReasonType(3)
    HARD_ERROR = VideoNotifyReasonType(4)


ScanlineOrderType = NewType('ScanlineOrderType', int)


class ScanlineOrderValues:
    TOP_TO_BOTTOM = ScanlineOrderType(0)
    BOTTOM_TO_TOP = ScanlineOrderType(1)


GrabPortStatusType = NewType('GrabPortStatusType', int)


class GrabPortStatusValues:
    SUCCESS = GrabPortStatusType(0)
    BAD_EXTENSION = GrabPortStatusType(1)
    ALREADY_GRABBED = GrabPortStatusType(2)
    INVALID_TIME = GrabPortStatusType(3)
    BAD_REPLY = GrabPortStatusType(4)
    BAD_ALLOC = GrabPortStatusType(5)


# ------------------------------------------------------------------
# Aliases

Port = NewType('Port', ctypes.c_uint32)
Encoding = NewType('Encoding', ctypes.c_uint32)


# ------------------------------------------------------------------
# Structures, Events, Requests, Replies


RationalStructPacket = DataPacket((
    ('numerator', FixedDataPacketField(MARKER_INT32)),
    ('denominator', FixedDataPacketField(MARKER_INT32)),
))


class RationalStruct:
    __slots__ = ('numerator', 'denominator',)

    def __init__(
            self, *,
            numerator: Optional[int] = None,
            denominator: Optional[int] = None,
    ) -> None:
        self.numerator = numerator
        self.denominator = denominator

    def as_dict(self) -> Dict[str, Any]:
        return {
            'numerator': self.numerator,
            'denominator': self.denominator,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'RationalStruct':
        return RationalStruct(**RationalStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return RationalStructPacket.pack(**self.as_dict())


class RationalStructCType(ctypes.Structure):
    """xv Rational"""
    _fields_ = [
        ("numerator", ctypes.c_int32),
        ("denominator", ctypes.c_int32),
    ]


FormatStructPacket = DataPacket((
    ('visual', FixedDataPacketField(MARKER_UINT32)),
    ('depth', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class FormatStruct:
    __slots__ = ('visual', 'depth',)

    def __init__(
            self, *,
            visual: Optional[int] = None,
            depth: Optional[int] = None,
    ) -> None:
        self.visual = visual
        self.depth = depth

    def as_dict(self) -> Dict[str, Any]:
        return {
            'visual': self.visual,
            'depth': self.depth,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'FormatStruct':
        return FormatStruct(**FormatStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return FormatStructPacket.pack(**self.as_dict())


class FormatStructCType(ctypes.Structure):
    """xv Format"""
    _fields_ = [
        ("visual", ctypes.c_uint32),
        ("depth", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


AdaptorInfoStructPacket = DataPacket((
    ('base_id', FixedDataPacketField(MARKER_UINT32)),
    ('name_size', FixedDataPacketField(MARKER_UINT16)),
    ('num_ports', FixedDataPacketField(MARKER_UINT16)),
    ('num_formats', FixedDataPacketField(MARKER_UINT16)),
    ('type', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('name', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['name_size'], 0)),
    ('pad1', AlignedPadDataPacketField(4)),
    ('formats', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_formats'], 0)),
))


class AdaptorInfoStruct:
    __slots__ = ('base_id', 'name_size', 'num_ports', 'num_formats', 'type', 'name', 'formats',)

    def __init__(
            self, *,
            base_id: Optional[int] = None,
            name_size: Optional[int] = None,
            num_ports: Optional[int] = None,
            num_formats: Optional[int] = None,
            type: Optional[int] = None,
            name: Optional[Sequence[int]] = None,
            formats: Optional[Sequence[int]] = None,
    ) -> None:
        self.base_id = base_id
        self.name_size = name_size
        self.num_ports = num_ports
        self.num_formats = num_formats
        self.type = type
        self.name = name
        self.formats = formats

    def as_dict(self) -> Dict[str, Any]:
        return {
            'base_id': self.base_id,
            'name_size': self.name_size,
            'num_ports': self.num_ports,
            'num_formats': self.num_formats,
            'type': self.type,
            'name': self.name,
            'formats': self.formats,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'AdaptorInfoStruct':
        return AdaptorInfoStruct(**AdaptorInfoStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return AdaptorInfoStructPacket.pack(**self.as_dict())


class AdaptorInfoStructCType(ctypes.Structure):
    """xv AdaptorInfo"""
    _fields_ = [
        ("base_id", ctypes.c_uint32),
        ("name_size", ctypes.c_uint16),
        ("num_ports", ctypes.c_uint16),
        ("num_formats", ctypes.c_uint16),
        ("type", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
        ("var_data", ctypes.c_void_p),
    ]


EncodingInfoStructPacket = DataPacket((
    ('encoding', FixedDataPacketField(MARKER_UINT32)),
    ('name_size', FixedDataPacketField(MARKER_UINT16)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
    ('rate', FixedDataPacketField(MARKER_UINT32)),
    ('name', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['name_size'], 0)),
    ('pad1', AlignedPadDataPacketField(4)),
))


class EncodingInfoStruct:
    __slots__ = ('encoding', 'name_size', 'width', 'height', 'rate', 'name',)

    def __init__(
            self, *,
            encoding: Optional[int] = None,
            name_size: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            rate: Optional[int] = None,
            name: Optional[Sequence[int]] = None,
    ) -> None:
        self.encoding = encoding
        self.name_size = name_size
        self.width = width
        self.height = height
        self.rate = rate
        self.name = name

    def as_dict(self) -> Dict[str, Any]:
        return {
            'encoding': self.encoding,
            'name_size': self.name_size,
            'width': self.width,
            'height': self.height,
            'rate': self.rate,
            'name': self.name,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'EncodingInfoStruct':
        return EncodingInfoStruct(**EncodingInfoStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return EncodingInfoStructPacket.pack(**self.as_dict())


class EncodingInfoStructCType(ctypes.Structure):
    """xv EncodingInfo"""
    _fields_ = [
        ("encoding", ctypes.c_uint32),
        ("name_size", ctypes.c_uint16),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
        ("rate", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


ImageStructPacket = DataPacket((
    ('id', FixedDataPacketField(MARKER_UINT32)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('data_size', FixedDataPacketField(MARKER_UINT32)),
    ('num_planes', FixedDataPacketField(MARKER_UINT32)),
    ('pitches', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_planes'], 0)),
    ('offsets', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_planes'], 0)),
    ('data', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: d['data_size'], 0)),
))


class ImageStruct:
    __slots__ = ('id', 'width', 'height', 'data_size', 'num_planes', 'pitches', 'offsets', 'data',)

    def __init__(
            self, *,
            id: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            data_size: Optional[int] = None,
            num_planes: Optional[int] = None,
            pitches: Optional[Sequence[int]] = None,
            offsets: Optional[Sequence[int]] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.id = id
        self.width = width
        self.height = height
        self.data_size = data_size
        self.num_planes = num_planes
        self.pitches = pitches
        self.offsets = offsets
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'data_size': self.data_size,
            'num_planes': self.num_planes,
            'pitches': self.pitches,
            'offsets': self.offsets,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ImageStruct':
        return ImageStruct(**ImageStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ImageStructPacket.pack(**self.as_dict())


class ImageStructCType(ctypes.Structure):
    """xv Image"""
    _fields_ = [
        ("id", ctypes.c_uint32),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("data_size", ctypes.c_uint32),
        ("num_planes", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


AttributeInfoStructPacket = DataPacket((
    ('flags', FixedDataPacketField(MARKER_UINT32)),
    ('min', FixedDataPacketField(MARKER_INT32)),
    ('max', FixedDataPacketField(MARKER_INT32)),
    ('size', FixedDataPacketField(MARKER_UINT32)),
    ('name', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['size'], 0)),
    ('pad0', AlignedPadDataPacketField(4)),
))


class AttributeInfoStruct:
    __slots__ = ('flags', 'min', 'max', 'size', 'name',)

    def __init__(
            self, *,
            flags: Optional[int] = None,
            min: Optional[int] = None,
            max: Optional[int] = None,
            size: Optional[int] = None,
            name: Optional[Sequence[int]] = None,
    ) -> None:
        self.flags = flags
        self.min = min
        self.max = max
        self.size = size
        self.name = name

    def as_dict(self) -> Dict[str, Any]:
        return {
            'flags': self.flags,
            'min': self.min,
            'max': self.max,
            'size': self.size,
            'name': self.name,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'AttributeInfoStruct':
        return AttributeInfoStruct(**AttributeInfoStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return AttributeInfoStructPacket.pack(**self.as_dict())


class AttributeInfoStructCType(ctypes.Structure):
    """xv AttributeInfo"""
    _fields_ = [
        ("flags", ctypes.c_uint32),
        ("min", ctypes.c_int32),
        ("max", ctypes.c_int32),
        ("size", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


ImageFormatInfoStructPacket = DataPacket((
    ('id', FixedDataPacketField(MARKER_UINT32)),
    ('type', FixedDataPacketField(MARKER_UINT8)),
    ('byte_order', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
    ('guid', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: 16, 0)),
    ('bpp', FixedDataPacketField(MARKER_UINT8)),
    ('num_planes', FixedDataPacketField(MARKER_UINT8)),
    ('pad1', FixedPadDataPacketField(2)),
    ('depth', FixedDataPacketField(MARKER_UINT8)),
    ('pad2', FixedPadDataPacketField(3)),
    ('red_mask', FixedDataPacketField(MARKER_UINT32)),
    ('green_mask', FixedDataPacketField(MARKER_UINT32)),
    ('blue_mask', FixedDataPacketField(MARKER_UINT32)),
    ('format', FixedDataPacketField(MARKER_UINT8)),
    ('pad3', FixedPadDataPacketField(3)),
    ('y_sample_bits', FixedDataPacketField(MARKER_UINT32)),
    ('u_sample_bits', FixedDataPacketField(MARKER_UINT32)),
    ('v_sample_bits', FixedDataPacketField(MARKER_UINT32)),
    ('vhorz_y_period', FixedDataPacketField(MARKER_UINT32)),
    ('vhorz_u_period', FixedDataPacketField(MARKER_UINT32)),
    ('vhorz_v_period', FixedDataPacketField(MARKER_UINT32)),
    ('vvert_y_period', FixedDataPacketField(MARKER_UINT32)),
    ('vvert_u_period', FixedDataPacketField(MARKER_UINT32)),
    ('vvert_v_period', FixedDataPacketField(MARKER_UINT32)),
    ('vcomp_order', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: 32, 0)),
    ('vscanline_order', FixedDataPacketField(MARKER_UINT8)),
    ('pad4', FixedPadDataPacketField(11)),
))


class ImageFormatInfoStruct:
    __slots__ = ('id', 'type', 'byte_order', 'guid', 'bpp', 'num_planes', 'depth', 'red_mask', 'green_mask', 'blue_mask', 'format', 'y_sample_bits', 'u_sample_bits', 'v_sample_bits', 'vhorz_y_period', 'vhorz_u_period', 'vhorz_v_period', 'vvert_y_period', 'vvert_u_period', 'vvert_v_period', 'vcomp_order', 'vscanline_order',)

    def __init__(
            self, *,
            id: Optional[int] = None,
            type: Optional[int] = None,
            byte_order: Optional[int] = None,
            guid: Optional[Sequence[int]] = None,
            bpp: Optional[int] = None,
            num_planes: Optional[int] = None,
            depth: Optional[int] = None,
            red_mask: Optional[int] = None,
            green_mask: Optional[int] = None,
            blue_mask: Optional[int] = None,
            format: Optional[int] = None,
            y_sample_bits: Optional[int] = None,
            u_sample_bits: Optional[int] = None,
            v_sample_bits: Optional[int] = None,
            vhorz_y_period: Optional[int] = None,
            vhorz_u_period: Optional[int] = None,
            vhorz_v_period: Optional[int] = None,
            vvert_y_period: Optional[int] = None,
            vvert_u_period: Optional[int] = None,
            vvert_v_period: Optional[int] = None,
            vcomp_order: Optional[Sequence[int]] = None,
            vscanline_order: Optional[int] = None,
    ) -> None:
        self.id = id
        self.type = type
        self.byte_order = byte_order
        self.guid = guid
        self.bpp = bpp
        self.num_planes = num_planes
        self.depth = depth
        self.red_mask = red_mask
        self.green_mask = green_mask
        self.blue_mask = blue_mask
        self.format = format
        self.y_sample_bits = y_sample_bits
        self.u_sample_bits = u_sample_bits
        self.v_sample_bits = v_sample_bits
        self.vhorz_y_period = vhorz_y_period
        self.vhorz_u_period = vhorz_u_period
        self.vhorz_v_period = vhorz_v_period
        self.vvert_y_period = vvert_y_period
        self.vvert_u_period = vvert_u_period
        self.vvert_v_period = vvert_v_period
        self.vcomp_order = vcomp_order
        self.vscanline_order = vscanline_order

    def as_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'type': self.type,
            'byte_order': self.byte_order,
            'guid': self.guid,
            'bpp': self.bpp,
            'num_planes': self.num_planes,
            'depth': self.depth,
            'red_mask': self.red_mask,
            'green_mask': self.green_mask,
            'blue_mask': self.blue_mask,
            'format': self.format,
            'y_sample_bits': self.y_sample_bits,
            'u_sample_bits': self.u_sample_bits,
            'v_sample_bits': self.v_sample_bits,
            'vhorz_y_period': self.vhorz_y_period,
            'vhorz_u_period': self.vhorz_u_period,
            'vhorz_v_period': self.vhorz_v_period,
            'vvert_y_period': self.vvert_y_period,
            'vvert_u_period': self.vvert_u_period,
            'vvert_v_period': self.vvert_v_period,
            'vcomp_order': self.vcomp_order,
            'vscanline_order': self.vscanline_order,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ImageFormatInfoStruct':
        return ImageFormatInfoStruct(**ImageFormatInfoStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ImageFormatInfoStructPacket.pack(**self.as_dict())


class ImageFormatInfoStructCType(ctypes.Structure):
    """xv ImageFormatInfo"""
    _fields_ = [
        ("id", ctypes.c_uint32),
        ("type", ctypes.c_uint8),
        ("byte_order", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


VideoNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('reason', FixedDataPacketField(MARKER_INT8)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('port', FixedDataPacketField(MARKER_UINT32)),
))


class VideoNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'reason', 'time', 'drawable', 'port',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            reason: Optional[int] = None,
            time: Optional[int] = None,
            drawable: Optional[int] = None,
            port: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.reason = reason
        self.time = time
        self.drawable = drawable
        self.port = port

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'reason': self.reason,
            'time': self.time,
            'drawable': self.drawable,
            'port': self.port,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'VideoNotifyEvent':
        return VideoNotifyEvent(**VideoNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return VideoNotifyEventPacket.pack(**self.as_dict())


class VideoNotifyEventCType(ctypes.Structure):
    """xv VideoNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("reason", ctypes.c_int8),
        ("time", ctypes.c_uint32),
        ("drawable", ctypes.c_uint32),
        ("port", ctypes.c_uint32),
    ]


PortNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(1)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('port', FixedDataPacketField(MARKER_UINT32)),
    ('attribute', FixedDataPacketField(MARKER_UINT32)),
    ('value', FixedDataPacketField(MARKER_INT32)),
))


class PortNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'time', 'port', 'attribute', 'value',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            time: Optional[int] = None,
            port: Optional[int] = None,
            attribute: Optional[int] = None,
            value: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.time = time
        self.port = port
        self.attribute = attribute
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'time': self.time,
            'port': self.port,
            'attribute': self.attribute,
            'value': self.value,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PortNotifyEvent':
        return PortNotifyEvent(**PortNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PortNotifyEventPacket.pack(**self.as_dict())


class PortNotifyEventCType(ctypes.Structure):
    """xv PortNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8),
        ("time", ctypes.c_uint32),
        ("port", ctypes.c_uint32),
        ("attribute", ctypes.c_uint32),
        ("value", ctypes.c_int32),
    ]


QueryExtensionRequestCookie = NewType('QueryExtensionRequestCookie', ctypes.c_uint32)


QueryExtensionRequestPacket = DataPacket((
))


class QueryExtensionRequest:
    OPCODE = 0

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryExtensionRequest':
        return QueryExtensionRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], QueryExtensionRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryExtensionRequest.lib = library.xv_queryextension
        QueryExtensionRequest.lib.restype = QueryExtensionRequestCookie
        QueryExtensionRequest.lib.argstype = ()


class QueryExtensionRequestCType(ctypes.Structure):
    """xv QueryExtension"""
    _fields_ = [
    ]


QueryExtensionReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('major', FixedDataPacketField(MARKER_UINT16)),
    ('minor', FixedDataPacketField(MARKER_UINT16)),
))


class QueryExtensionReplyReply:
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
    def from_data(inp: BinaryIO) -> 'QueryExtensionReplyReply':
        return QueryExtensionReplyReply(**QueryExtensionReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryExtensionReplyReplyPacket.pack(**self.as_dict())


class QueryExtensionReplyReplyCType(ctypes.Structure):
    """xv QueryExtension_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("major", ctypes.c_uint16),
        ("minor", ctypes.c_uint16),
    ]


QueryAdaptorsRequestCookie = NewType('QueryAdaptorsRequestCookie', ctypes.c_uint32)


QueryAdaptorsRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class QueryAdaptorsRequest:
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
    def from_data(inp: BinaryIO) -> 'QueryAdaptorsRequest':
        return QueryAdaptorsRequest(**QueryAdaptorsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryAdaptorsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], QueryAdaptorsRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryAdaptorsRequest.lib = library.xv_queryadaptors
        QueryAdaptorsRequest.lib.restype = QueryAdaptorsRequestCookie
        QueryAdaptorsRequest.lib.argstype = (ctypes.c_uint32,)


class QueryAdaptorsRequestCType(ctypes.Structure):
    """xv QueryAdaptors"""
    _fields_ = [
        ("window", ctypes.c_uint32),
    ]


QueryAdaptorsReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('num_adaptors', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(22)),
    ('info', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_adaptors'], 0)),
))


class QueryAdaptorsReplyReply:
    __slots__ = ('num_adaptors', 'info',)

    def __init__(
            self, *,
            num_adaptors: Optional[int] = None,
            info: Optional[Sequence[int]] = None,
    ) -> None:
        self.num_adaptors = num_adaptors
        self.info = info

    def as_dict(self) -> Dict[str, Any]:
        return {
            'num_adaptors': self.num_adaptors,
            'info': self.info,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryAdaptorsReplyReply':
        return QueryAdaptorsReplyReply(**QueryAdaptorsReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryAdaptorsReplyReplyPacket.pack(**self.as_dict())


class QueryAdaptorsReplyReplyCType(ctypes.Structure):
    """xv QueryAdaptors_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("num_adaptors", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 22),
        ("var_data", ctypes.c_void_p),
    ]


QueryEncodingsRequestCookie = NewType('QueryEncodingsRequestCookie', ctypes.c_uint32)


QueryEncodingsRequestPacket = DataPacket((
    ('port', FixedDataPacketField(MARKER_UINT32)),
))


class QueryEncodingsRequest:
    OPCODE = 2

    __slots__ = ('port',)

    def __init__(
            self, *,
            port: Optional[int] = None,
    ) -> None:
        self.port = port

    def as_dict(self) -> Dict[str, Any]:
        return {
            'port': self.port,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryEncodingsRequest':
        return QueryEncodingsRequest(**QueryEncodingsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryEncodingsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], QueryEncodingsRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryEncodingsRequest.lib = library.xv_queryencodings
        QueryEncodingsRequest.lib.restype = QueryEncodingsRequestCookie
        QueryEncodingsRequest.lib.argstype = (ctypes.c_uint32,)


class QueryEncodingsRequestCType(ctypes.Structure):
    """xv QueryEncodings"""
    _fields_ = [
        ("port", ctypes.c_uint32),
    ]


QueryEncodingsReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('num_encodings', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(22)),
    ('info', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_encodings'], 0)),
))


class QueryEncodingsReplyReply:
    __slots__ = ('num_encodings', 'info',)

    def __init__(
            self, *,
            num_encodings: Optional[int] = None,
            info: Optional[Sequence[int]] = None,
    ) -> None:
        self.num_encodings = num_encodings
        self.info = info

    def as_dict(self) -> Dict[str, Any]:
        return {
            'num_encodings': self.num_encodings,
            'info': self.info,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryEncodingsReplyReply':
        return QueryEncodingsReplyReply(**QueryEncodingsReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryEncodingsReplyReplyPacket.pack(**self.as_dict())


class QueryEncodingsReplyReplyCType(ctypes.Structure):
    """xv QueryEncodings_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("num_encodings", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 22),
        ("var_data", ctypes.c_void_p),
    ]


GrabPortRequestCookie = NewType('GrabPortRequestCookie', ctypes.c_uint32)


GrabPortRequestPacket = DataPacket((
    ('port', FixedDataPacketField(MARKER_UINT32)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
))


class GrabPortRequest:
    OPCODE = 3

    __slots__ = ('port', 'time',)

    def __init__(
            self, *,
            port: Optional[int] = None,
            time: Optional[int] = None,
    ) -> None:
        self.port = port
        self.time = time

    def as_dict(self) -> Dict[str, Any]:
        return {
            'port': self.port,
            'time': self.time,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GrabPortRequest':
        return GrabPortRequest(**GrabPortRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GrabPortRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], GrabPortRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GrabPortRequest.lib = library.xv_grabport
        GrabPortRequest.lib.restype = GrabPortRequestCookie
        GrabPortRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class GrabPortRequestCType(ctypes.Structure):
    """xv GrabPort"""
    _fields_ = [
        ("port", ctypes.c_uint32),
        ("time", ctypes.c_uint32),
    ]


GrabPortReplyReplyPacket = DataPacket((
    ('result', FixedDataPacketField(MARKER_INT8)),
))


class GrabPortReplyReply:
    __slots__ = ('result',)

    def __init__(
            self, *,
            result: Optional[int] = None,
    ) -> None:
        self.result = result

    def as_dict(self) -> Dict[str, Any]:
        return {
            'result': self.result,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GrabPortReplyReply':
        return GrabPortReplyReply(**GrabPortReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GrabPortReplyReplyPacket.pack(**self.as_dict())


class GrabPortReplyReplyCType(ctypes.Structure):
    """xv GrabPort_reply"""
    _fields_ = [
        ("result", ctypes.c_int8),
    ]


UngrabPortRequestPacket = DataPacket((
    ('port', FixedDataPacketField(MARKER_UINT32)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
))


class UngrabPortRequest:
    OPCODE = 4

    __slots__ = ('port', 'time',)

    def __init__(
            self, *,
            port: Optional[int] = None,
            time: Optional[int] = None,
    ) -> None:
        self.port = port
        self.time = time

    def as_dict(self) -> Dict[str, Any]:
        return {
            'port': self.port,
            'time': self.time,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'UngrabPortRequest':
        return UngrabPortRequest(**UngrabPortRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return UngrabPortRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        UngrabPortRequest.lib = library.xv_ungrabport
        UngrabPortRequest.lib.restype = ctypes.c_uint32
        UngrabPortRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class UngrabPortRequestCType(ctypes.Structure):
    """xv UngrabPort"""
    _fields_ = [
        ("port", ctypes.c_uint32),
        ("time", ctypes.c_uint32),
    ]


PutVideoRequestPacket = DataPacket((
    ('port', FixedDataPacketField(MARKER_UINT32)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('gc', FixedDataPacketField(MARKER_UINT32)),
    ('vid_x', FixedDataPacketField(MARKER_INT16)),
    ('vid_y', FixedDataPacketField(MARKER_INT16)),
    ('vid_w', FixedDataPacketField(MARKER_UINT16)),
    ('vid_h', FixedDataPacketField(MARKER_UINT16)),
    ('drw_x', FixedDataPacketField(MARKER_INT16)),
    ('drw_y', FixedDataPacketField(MARKER_INT16)),
    ('drw_w', FixedDataPacketField(MARKER_UINT16)),
    ('drw_h', FixedDataPacketField(MARKER_UINT16)),
))


class PutVideoRequest:
    OPCODE = 5

    __slots__ = ('port', 'drawable', 'gc', 'vid_x', 'vid_y', 'vid_w', 'vid_h', 'drw_x', 'drw_y', 'drw_w', 'drw_h',)

    def __init__(
            self, *,
            port: Optional[int] = None,
            drawable: Optional[int] = None,
            gc: Optional[int] = None,
            vid_x: Optional[int] = None,
            vid_y: Optional[int] = None,
            vid_w: Optional[int] = None,
            vid_h: Optional[int] = None,
            drw_x: Optional[int] = None,
            drw_y: Optional[int] = None,
            drw_w: Optional[int] = None,
            drw_h: Optional[int] = None,
    ) -> None:
        self.port = port
        self.drawable = drawable
        self.gc = gc
        self.vid_x = vid_x
        self.vid_y = vid_y
        self.vid_w = vid_w
        self.vid_h = vid_h
        self.drw_x = drw_x
        self.drw_y = drw_y
        self.drw_w = drw_w
        self.drw_h = drw_h

    def as_dict(self) -> Dict[str, Any]:
        return {
            'port': self.port,
            'drawable': self.drawable,
            'gc': self.gc,
            'vid_x': self.vid_x,
            'vid_y': self.vid_y,
            'vid_w': self.vid_w,
            'vid_h': self.vid_h,
            'drw_x': self.drw_x,
            'drw_y': self.drw_y,
            'drw_w': self.drw_w,
            'drw_h': self.drw_h,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PutVideoRequest':
        return PutVideoRequest(**PutVideoRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PutVideoRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PutVideoRequest.lib = library.xv_putvideo
        PutVideoRequest.lib.restype = ctypes.c_uint32
        PutVideoRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_int16, ctypes.c_int16, ctypes.c_uint16, ctypes.c_uint16)


class PutVideoRequestCType(ctypes.Structure):
    """xv PutVideo"""
    _fields_ = [
        ("port", ctypes.c_uint32),
        ("drawable", ctypes.c_uint32),
        ("gc", ctypes.c_uint32),
        ("vid_x", ctypes.c_int16),
        ("vid_y", ctypes.c_int16),
        ("vid_w", ctypes.c_uint16),
        ("vid_h", ctypes.c_uint16),
        ("drw_x", ctypes.c_int16),
        ("drw_y", ctypes.c_int16),
        ("drw_w", ctypes.c_uint16),
        ("drw_h", ctypes.c_uint16),
    ]


PutStillRequestPacket = DataPacket((
    ('port', FixedDataPacketField(MARKER_UINT32)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('gc', FixedDataPacketField(MARKER_UINT32)),
    ('vid_x', FixedDataPacketField(MARKER_INT16)),
    ('vid_y', FixedDataPacketField(MARKER_INT16)),
    ('vid_w', FixedDataPacketField(MARKER_UINT16)),
    ('vid_h', FixedDataPacketField(MARKER_UINT16)),
    ('drw_x', FixedDataPacketField(MARKER_INT16)),
    ('drw_y', FixedDataPacketField(MARKER_INT16)),
    ('drw_w', FixedDataPacketField(MARKER_UINT16)),
    ('drw_h', FixedDataPacketField(MARKER_UINT16)),
))


class PutStillRequest:
    OPCODE = 6

    __slots__ = ('port', 'drawable', 'gc', 'vid_x', 'vid_y', 'vid_w', 'vid_h', 'drw_x', 'drw_y', 'drw_w', 'drw_h',)

    def __init__(
            self, *,
            port: Optional[int] = None,
            drawable: Optional[int] = None,
            gc: Optional[int] = None,
            vid_x: Optional[int] = None,
            vid_y: Optional[int] = None,
            vid_w: Optional[int] = None,
            vid_h: Optional[int] = None,
            drw_x: Optional[int] = None,
            drw_y: Optional[int] = None,
            drw_w: Optional[int] = None,
            drw_h: Optional[int] = None,
    ) -> None:
        self.port = port
        self.drawable = drawable
        self.gc = gc
        self.vid_x = vid_x
        self.vid_y = vid_y
        self.vid_w = vid_w
        self.vid_h = vid_h
        self.drw_x = drw_x
        self.drw_y = drw_y
        self.drw_w = drw_w
        self.drw_h = drw_h

    def as_dict(self) -> Dict[str, Any]:
        return {
            'port': self.port,
            'drawable': self.drawable,
            'gc': self.gc,
            'vid_x': self.vid_x,
            'vid_y': self.vid_y,
            'vid_w': self.vid_w,
            'vid_h': self.vid_h,
            'drw_x': self.drw_x,
            'drw_y': self.drw_y,
            'drw_w': self.drw_w,
            'drw_h': self.drw_h,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PutStillRequest':
        return PutStillRequest(**PutStillRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PutStillRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PutStillRequest.lib = library.xv_putstill
        PutStillRequest.lib.restype = ctypes.c_uint32
        PutStillRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_int16, ctypes.c_int16, ctypes.c_uint16, ctypes.c_uint16)


class PutStillRequestCType(ctypes.Structure):
    """xv PutStill"""
    _fields_ = [
        ("port", ctypes.c_uint32),
        ("drawable", ctypes.c_uint32),
        ("gc", ctypes.c_uint32),
        ("vid_x", ctypes.c_int16),
        ("vid_y", ctypes.c_int16),
        ("vid_w", ctypes.c_uint16),
        ("vid_h", ctypes.c_uint16),
        ("drw_x", ctypes.c_int16),
        ("drw_y", ctypes.c_int16),
        ("drw_w", ctypes.c_uint16),
        ("drw_h", ctypes.c_uint16),
    ]


GetVideoRequestPacket = DataPacket((
    ('port', FixedDataPacketField(MARKER_UINT32)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('gc', FixedDataPacketField(MARKER_UINT32)),
    ('vid_x', FixedDataPacketField(MARKER_INT16)),
    ('vid_y', FixedDataPacketField(MARKER_INT16)),
    ('vid_w', FixedDataPacketField(MARKER_UINT16)),
    ('vid_h', FixedDataPacketField(MARKER_UINT16)),
    ('drw_x', FixedDataPacketField(MARKER_INT16)),
    ('drw_y', FixedDataPacketField(MARKER_INT16)),
    ('drw_w', FixedDataPacketField(MARKER_UINT16)),
    ('drw_h', FixedDataPacketField(MARKER_UINT16)),
))


class GetVideoRequest:
    OPCODE = 7

    __slots__ = ('port', 'drawable', 'gc', 'vid_x', 'vid_y', 'vid_w', 'vid_h', 'drw_x', 'drw_y', 'drw_w', 'drw_h',)

    def __init__(
            self, *,
            port: Optional[int] = None,
            drawable: Optional[int] = None,
            gc: Optional[int] = None,
            vid_x: Optional[int] = None,
            vid_y: Optional[int] = None,
            vid_w: Optional[int] = None,
            vid_h: Optional[int] = None,
            drw_x: Optional[int] = None,
            drw_y: Optional[int] = None,
            drw_w: Optional[int] = None,
            drw_h: Optional[int] = None,
    ) -> None:
        self.port = port
        self.drawable = drawable
        self.gc = gc
        self.vid_x = vid_x
        self.vid_y = vid_y
        self.vid_w = vid_w
        self.vid_h = vid_h
        self.drw_x = drw_x
        self.drw_y = drw_y
        self.drw_w = drw_w
        self.drw_h = drw_h

    def as_dict(self) -> Dict[str, Any]:
        return {
            'port': self.port,
            'drawable': self.drawable,
            'gc': self.gc,
            'vid_x': self.vid_x,
            'vid_y': self.vid_y,
            'vid_w': self.vid_w,
            'vid_h': self.vid_h,
            'drw_x': self.drw_x,
            'drw_y': self.drw_y,
            'drw_w': self.drw_w,
            'drw_h': self.drw_h,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetVideoRequest':
        return GetVideoRequest(**GetVideoRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetVideoRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetVideoRequest.lib = library.xv_getvideo
        GetVideoRequest.lib.restype = ctypes.c_uint32
        GetVideoRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_int16, ctypes.c_int16, ctypes.c_uint16, ctypes.c_uint16)


class GetVideoRequestCType(ctypes.Structure):
    """xv GetVideo"""
    _fields_ = [
        ("port", ctypes.c_uint32),
        ("drawable", ctypes.c_uint32),
        ("gc", ctypes.c_uint32),
        ("vid_x", ctypes.c_int16),
        ("vid_y", ctypes.c_int16),
        ("vid_w", ctypes.c_uint16),
        ("vid_h", ctypes.c_uint16),
        ("drw_x", ctypes.c_int16),
        ("drw_y", ctypes.c_int16),
        ("drw_w", ctypes.c_uint16),
        ("drw_h", ctypes.c_uint16),
    ]


GetStillRequestPacket = DataPacket((
    ('port', FixedDataPacketField(MARKER_UINT32)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('gc', FixedDataPacketField(MARKER_UINT32)),
    ('vid_x', FixedDataPacketField(MARKER_INT16)),
    ('vid_y', FixedDataPacketField(MARKER_INT16)),
    ('vid_w', FixedDataPacketField(MARKER_UINT16)),
    ('vid_h', FixedDataPacketField(MARKER_UINT16)),
    ('drw_x', FixedDataPacketField(MARKER_INT16)),
    ('drw_y', FixedDataPacketField(MARKER_INT16)),
    ('drw_w', FixedDataPacketField(MARKER_UINT16)),
    ('drw_h', FixedDataPacketField(MARKER_UINT16)),
))


class GetStillRequest:
    OPCODE = 8

    __slots__ = ('port', 'drawable', 'gc', 'vid_x', 'vid_y', 'vid_w', 'vid_h', 'drw_x', 'drw_y', 'drw_w', 'drw_h',)

    def __init__(
            self, *,
            port: Optional[int] = None,
            drawable: Optional[int] = None,
            gc: Optional[int] = None,
            vid_x: Optional[int] = None,
            vid_y: Optional[int] = None,
            vid_w: Optional[int] = None,
            vid_h: Optional[int] = None,
            drw_x: Optional[int] = None,
            drw_y: Optional[int] = None,
            drw_w: Optional[int] = None,
            drw_h: Optional[int] = None,
    ) -> None:
        self.port = port
        self.drawable = drawable
        self.gc = gc
        self.vid_x = vid_x
        self.vid_y = vid_y
        self.vid_w = vid_w
        self.vid_h = vid_h
        self.drw_x = drw_x
        self.drw_y = drw_y
        self.drw_w = drw_w
        self.drw_h = drw_h

    def as_dict(self) -> Dict[str, Any]:
        return {
            'port': self.port,
            'drawable': self.drawable,
            'gc': self.gc,
            'vid_x': self.vid_x,
            'vid_y': self.vid_y,
            'vid_w': self.vid_w,
            'vid_h': self.vid_h,
            'drw_x': self.drw_x,
            'drw_y': self.drw_y,
            'drw_w': self.drw_w,
            'drw_h': self.drw_h,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetStillRequest':
        return GetStillRequest(**GetStillRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetStillRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetStillRequest.lib = library.xv_getstill
        GetStillRequest.lib.restype = ctypes.c_uint32
        GetStillRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_int16, ctypes.c_int16, ctypes.c_uint16, ctypes.c_uint16)


class GetStillRequestCType(ctypes.Structure):
    """xv GetStill"""
    _fields_ = [
        ("port", ctypes.c_uint32),
        ("drawable", ctypes.c_uint32),
        ("gc", ctypes.c_uint32),
        ("vid_x", ctypes.c_int16),
        ("vid_y", ctypes.c_int16),
        ("vid_w", ctypes.c_uint16),
        ("vid_h", ctypes.c_uint16),
        ("drw_x", ctypes.c_int16),
        ("drw_y", ctypes.c_int16),
        ("drw_w", ctypes.c_uint16),
        ("drw_h", ctypes.c_uint16),
    ]


StopVideoRequestPacket = DataPacket((
    ('port', FixedDataPacketField(MARKER_UINT32)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
))


class StopVideoRequest:
    OPCODE = 9

    __slots__ = ('port', 'drawable',)

    def __init__(
            self, *,
            port: Optional[int] = None,
            drawable: Optional[int] = None,
    ) -> None:
        self.port = port
        self.drawable = drawable

    def as_dict(self) -> Dict[str, Any]:
        return {
            'port': self.port,
            'drawable': self.drawable,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'StopVideoRequest':
        return StopVideoRequest(**StopVideoRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return StopVideoRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        StopVideoRequest.lib = library.xv_stopvideo
        StopVideoRequest.lib.restype = ctypes.c_uint32
        StopVideoRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class StopVideoRequestCType(ctypes.Structure):
    """xv StopVideo"""
    _fields_ = [
        ("port", ctypes.c_uint32),
        ("drawable", ctypes.c_uint32),
    ]


SelectVideoNotifyRequestPacket = DataPacket((
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('onoff', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class SelectVideoNotifyRequest:
    OPCODE = 10

    __slots__ = ('drawable', 'onoff',)

    def __init__(
            self, *,
            drawable: Optional[int] = None,
            onoff: Optional[bool] = None,
    ) -> None:
        self.drawable = drawable
        self.onoff = onoff

    def as_dict(self) -> Dict[str, Any]:
        return {
            'drawable': self.drawable,
            'onoff': self.onoff,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SelectVideoNotifyRequest':
        return SelectVideoNotifyRequest(**SelectVideoNotifyRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SelectVideoNotifyRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, bool], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SelectVideoNotifyRequest.lib = library.xv_selectvideonotify
        SelectVideoNotifyRequest.lib.restype = ctypes.c_uint32
        SelectVideoNotifyRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_int8, ctypes.c_uint8 * 3)


class SelectVideoNotifyRequestCType(ctypes.Structure):
    """xv SelectVideoNotify"""
    _fields_ = [
        ("drawable", ctypes.c_uint32),
        ("onoff", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


SelectPortNotifyRequestPacket = DataPacket((
    ('port', FixedDataPacketField(MARKER_UINT32)),
    ('onoff', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class SelectPortNotifyRequest:
    OPCODE = 11

    __slots__ = ('port', 'onoff',)

    def __init__(
            self, *,
            port: Optional[int] = None,
            onoff: Optional[bool] = None,
    ) -> None:
        self.port = port
        self.onoff = onoff

    def as_dict(self) -> Dict[str, Any]:
        return {
            'port': self.port,
            'onoff': self.onoff,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SelectPortNotifyRequest':
        return SelectPortNotifyRequest(**SelectPortNotifyRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SelectPortNotifyRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, bool], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SelectPortNotifyRequest.lib = library.xv_selectportnotify
        SelectPortNotifyRequest.lib.restype = ctypes.c_uint32
        SelectPortNotifyRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_int8, ctypes.c_uint8 * 3)


class SelectPortNotifyRequestCType(ctypes.Structure):
    """xv SelectPortNotify"""
    _fields_ = [
        ("port", ctypes.c_uint32),
        ("onoff", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


QueryBestSizeRequestCookie = NewType('QueryBestSizeRequestCookie', ctypes.c_uint32)


QueryBestSizeRequestPacket = DataPacket((
    ('port', FixedDataPacketField(MARKER_UINT32)),
    ('vid_w', FixedDataPacketField(MARKER_UINT16)),
    ('vid_h', FixedDataPacketField(MARKER_UINT16)),
    ('drw_w', FixedDataPacketField(MARKER_UINT16)),
    ('drw_h', FixedDataPacketField(MARKER_UINT16)),
    ('motion', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class QueryBestSizeRequest:
    OPCODE = 12

    __slots__ = ('port', 'vid_w', 'vid_h', 'drw_w', 'drw_h', 'motion',)

    def __init__(
            self, *,
            port: Optional[int] = None,
            vid_w: Optional[int] = None,
            vid_h: Optional[int] = None,
            drw_w: Optional[int] = None,
            drw_h: Optional[int] = None,
            motion: Optional[bool] = None,
    ) -> None:
        self.port = port
        self.vid_w = vid_w
        self.vid_h = vid_h
        self.drw_w = drw_w
        self.drw_h = drw_h
        self.motion = motion

    def as_dict(self) -> Dict[str, Any]:
        return {
            'port': self.port,
            'vid_w': self.vid_w,
            'vid_h': self.vid_h,
            'drw_w': self.drw_w,
            'drw_h': self.drw_h,
            'motion': self.motion,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryBestSizeRequest':
        return QueryBestSizeRequest(**QueryBestSizeRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryBestSizeRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, bool], QueryBestSizeRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryBestSizeRequest.lib = library.xv_querybestsize
        QueryBestSizeRequest.lib.restype = QueryBestSizeRequestCookie
        QueryBestSizeRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_int8, ctypes.c_uint8 * 3)


class QueryBestSizeRequestCType(ctypes.Structure):
    """xv QueryBestSize"""
    _fields_ = [
        ("port", ctypes.c_uint32),
        ("vid_w", ctypes.c_uint16),
        ("vid_h", ctypes.c_uint16),
        ("drw_w", ctypes.c_uint16),
        ("drw_h", ctypes.c_uint16),
        ("motion", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


QueryBestSizeReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('actual_width', FixedDataPacketField(MARKER_UINT16)),
    ('actual_height', FixedDataPacketField(MARKER_UINT16)),
))


class QueryBestSizeReplyReply:
    __slots__ = ('actual_width', 'actual_height',)

    def __init__(
            self, *,
            actual_width: Optional[int] = None,
            actual_height: Optional[int] = None,
    ) -> None:
        self.actual_width = actual_width
        self.actual_height = actual_height

    def as_dict(self) -> Dict[str, Any]:
        return {
            'actual_width': self.actual_width,
            'actual_height': self.actual_height,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryBestSizeReplyReply':
        return QueryBestSizeReplyReply(**QueryBestSizeReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryBestSizeReplyReplyPacket.pack(**self.as_dict())


class QueryBestSizeReplyReplyCType(ctypes.Structure):
    """xv QueryBestSize_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("actual_width", ctypes.c_uint16),
        ("actual_height", ctypes.c_uint16),
    ]


SetPortAttributeRequestPacket = DataPacket((
    ('port', FixedDataPacketField(MARKER_UINT32)),
    ('attribute', FixedDataPacketField(MARKER_UINT32)),
    ('value', FixedDataPacketField(MARKER_INT32)),
))


class SetPortAttributeRequest:
    OPCODE = 13

    __slots__ = ('port', 'attribute', 'value',)

    def __init__(
            self, *,
            port: Optional[int] = None,
            attribute: Optional[int] = None,
            value: Optional[int] = None,
    ) -> None:
        self.port = port
        self.attribute = attribute
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {
            'port': self.port,
            'attribute': self.attribute,
            'value': self.value,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetPortAttributeRequest':
        return SetPortAttributeRequest(**SetPortAttributeRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetPortAttributeRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetPortAttributeRequest.lib = library.xv_setportattribute
        SetPortAttributeRequest.lib.restype = ctypes.c_uint32
        SetPortAttributeRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int32)


class SetPortAttributeRequestCType(ctypes.Structure):
    """xv SetPortAttribute"""
    _fields_ = [
        ("port", ctypes.c_uint32),
        ("attribute", ctypes.c_uint32),
        ("value", ctypes.c_int32),
    ]


GetPortAttributeRequestCookie = NewType('GetPortAttributeRequestCookie', ctypes.c_uint32)


GetPortAttributeRequestPacket = DataPacket((
    ('port', FixedDataPacketField(MARKER_UINT32)),
    ('attribute', FixedDataPacketField(MARKER_UINT32)),
))


class GetPortAttributeRequest:
    OPCODE = 14

    __slots__ = ('port', 'attribute',)

    def __init__(
            self, *,
            port: Optional[int] = None,
            attribute: Optional[int] = None,
    ) -> None:
        self.port = port
        self.attribute = attribute

    def as_dict(self) -> Dict[str, Any]:
        return {
            'port': self.port,
            'attribute': self.attribute,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetPortAttributeRequest':
        return GetPortAttributeRequest(**GetPortAttributeRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetPortAttributeRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], GetPortAttributeRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetPortAttributeRequest.lib = library.xv_getportattribute
        GetPortAttributeRequest.lib.restype = GetPortAttributeRequestCookie
        GetPortAttributeRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class GetPortAttributeRequestCType(ctypes.Structure):
    """xv GetPortAttribute"""
    _fields_ = [
        ("port", ctypes.c_uint32),
        ("attribute", ctypes.c_uint32),
    ]


GetPortAttributeReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('value', FixedDataPacketField(MARKER_INT32)),
))


class GetPortAttributeReplyReply:
    __slots__ = ('value',)

    def __init__(
            self, *,
            value: Optional[int] = None,
    ) -> None:
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {
            'value': self.value,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetPortAttributeReplyReply':
        return GetPortAttributeReplyReply(**GetPortAttributeReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetPortAttributeReplyReplyPacket.pack(**self.as_dict())


class GetPortAttributeReplyReplyCType(ctypes.Structure):
    """xv GetPortAttribute_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("value", ctypes.c_int32),
    ]


QueryPortAttributesRequestCookie = NewType('QueryPortAttributesRequestCookie', ctypes.c_uint32)


QueryPortAttributesRequestPacket = DataPacket((
    ('port', FixedDataPacketField(MARKER_UINT32)),
))


class QueryPortAttributesRequest:
    OPCODE = 15

    __slots__ = ('port',)

    def __init__(
            self, *,
            port: Optional[int] = None,
    ) -> None:
        self.port = port

    def as_dict(self) -> Dict[str, Any]:
        return {
            'port': self.port,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryPortAttributesRequest':
        return QueryPortAttributesRequest(**QueryPortAttributesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryPortAttributesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], QueryPortAttributesRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryPortAttributesRequest.lib = library.xv_queryportattributes
        QueryPortAttributesRequest.lib.restype = QueryPortAttributesRequestCookie
        QueryPortAttributesRequest.lib.argstype = (ctypes.c_uint32,)


class QueryPortAttributesRequestCType(ctypes.Structure):
    """xv QueryPortAttributes"""
    _fields_ = [
        ("port", ctypes.c_uint32),
    ]


QueryPortAttributesReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('num_attributes', FixedDataPacketField(MARKER_UINT32)),
    ('text_size', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(16)),
    ('attributes', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_attributes'], 0)),
))


class QueryPortAttributesReplyReply:
    __slots__ = ('num_attributes', 'text_size', 'attributes',)

    def __init__(
            self, *,
            num_attributes: Optional[int] = None,
            text_size: Optional[int] = None,
            attributes: Optional[Sequence[int]] = None,
    ) -> None:
        self.num_attributes = num_attributes
        self.text_size = text_size
        self.attributes = attributes

    def as_dict(self) -> Dict[str, Any]:
        return {
            'num_attributes': self.num_attributes,
            'text_size': self.text_size,
            'attributes': self.attributes,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryPortAttributesReplyReply':
        return QueryPortAttributesReplyReply(**QueryPortAttributesReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryPortAttributesReplyReplyPacket.pack(**self.as_dict())


class QueryPortAttributesReplyReplyCType(ctypes.Structure):
    """xv QueryPortAttributes_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("num_attributes", ctypes.c_uint32),
        ("text_size", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 16),
        ("var_data", ctypes.c_void_p),
    ]


ListImageFormatsRequestCookie = NewType('ListImageFormatsRequestCookie', ctypes.c_uint32)


ListImageFormatsRequestPacket = DataPacket((
    ('port', FixedDataPacketField(MARKER_UINT32)),
))


class ListImageFormatsRequest:
    OPCODE = 16

    __slots__ = ('port',)

    def __init__(
            self, *,
            port: Optional[int] = None,
    ) -> None:
        self.port = port

    def as_dict(self) -> Dict[str, Any]:
        return {
            'port': self.port,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ListImageFormatsRequest':
        return ListImageFormatsRequest(**ListImageFormatsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ListImageFormatsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ListImageFormatsRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ListImageFormatsRequest.lib = library.xv_listimageformats
        ListImageFormatsRequest.lib.restype = ListImageFormatsRequestCookie
        ListImageFormatsRequest.lib.argstype = (ctypes.c_uint32,)


class ListImageFormatsRequestCType(ctypes.Structure):
    """xv ListImageFormats"""
    _fields_ = [
        ("port", ctypes.c_uint32),
    ]


ListImageFormatsReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('num_formats', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('format', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_formats'], 0)),
))


class ListImageFormatsReplyReply:
    __slots__ = ('num_formats', 'format',)

    def __init__(
            self, *,
            num_formats: Optional[int] = None,
            format: Optional[Sequence[int]] = None,
    ) -> None:
        self.num_formats = num_formats
        self.format = format

    def as_dict(self) -> Dict[str, Any]:
        return {
            'num_formats': self.num_formats,
            'format': self.format,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ListImageFormatsReplyReply':
        return ListImageFormatsReplyReply(**ListImageFormatsReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ListImageFormatsReplyReplyPacket.pack(**self.as_dict())


class ListImageFormatsReplyReplyCType(ctypes.Structure):
    """xv ListImageFormats_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("num_formats", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


QueryImageAttributesRequestCookie = NewType('QueryImageAttributesRequestCookie', ctypes.c_uint32)


QueryImageAttributesRequestPacket = DataPacket((
    ('port', FixedDataPacketField(MARKER_UINT32)),
    ('id', FixedDataPacketField(MARKER_UINT32)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
))


class QueryImageAttributesRequest:
    OPCODE = 17

    __slots__ = ('port', 'id', 'width', 'height',)

    def __init__(
            self, *,
            port: Optional[int] = None,
            id: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
    ) -> None:
        self.port = port
        self.id = id
        self.width = width
        self.height = height

    def as_dict(self) -> Dict[str, Any]:
        return {
            'port': self.port,
            'id': self.id,
            'width': self.width,
            'height': self.height,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryImageAttributesRequest':
        return QueryImageAttributesRequest(**QueryImageAttributesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryImageAttributesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int], QueryImageAttributesRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryImageAttributesRequest.lib = library.xv_queryimageattributes
        QueryImageAttributesRequest.lib.restype = QueryImageAttributesRequestCookie
        QueryImageAttributesRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16)


class QueryImageAttributesRequestCType(ctypes.Structure):
    """xv QueryImageAttributes"""
    _fields_ = [
        ("port", ctypes.c_uint32),
        ("id", ctypes.c_uint32),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
    ]


QueryImageAttributesReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('num_planes', FixedDataPacketField(MARKER_UINT32)),
    ('data_size', FixedDataPacketField(MARKER_UINT32)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(12)),
    ('pitches', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_planes'], 0)),
    ('offsets', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_planes'], 0)),
))


class QueryImageAttributesReplyReply:
    __slots__ = ('num_planes', 'data_size', 'width', 'height', 'pitches', 'offsets',)

    def __init__(
            self, *,
            num_planes: Optional[int] = None,
            data_size: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            pitches: Optional[Sequence[int]] = None,
            offsets: Optional[Sequence[int]] = None,
    ) -> None:
        self.num_planes = num_planes
        self.data_size = data_size
        self.width = width
        self.height = height
        self.pitches = pitches
        self.offsets = offsets

    def as_dict(self) -> Dict[str, Any]:
        return {
            'num_planes': self.num_planes,
            'data_size': self.data_size,
            'width': self.width,
            'height': self.height,
            'pitches': self.pitches,
            'offsets': self.offsets,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryImageAttributesReplyReply':
        return QueryImageAttributesReplyReply(**QueryImageAttributesReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryImageAttributesReplyReplyPacket.pack(**self.as_dict())


class QueryImageAttributesReplyReplyCType(ctypes.Structure):
    """xv QueryImageAttributes_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("num_planes", ctypes.c_uint32),
        ("data_size", ctypes.c_uint32),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


PutImageRequestPacket = DataPacket((
    ('port', FixedDataPacketField(MARKER_UINT32)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('gc', FixedDataPacketField(MARKER_UINT32)),
    ('id', FixedDataPacketField(MARKER_UINT32)),
    ('src_x', FixedDataPacketField(MARKER_INT16)),
    ('src_y', FixedDataPacketField(MARKER_INT16)),
    ('src_w', FixedDataPacketField(MARKER_UINT16)),
    ('src_h', FixedDataPacketField(MARKER_UINT16)),
    ('drw_x', FixedDataPacketField(MARKER_INT16)),
    ('drw_y', FixedDataPacketField(MARKER_INT16)),
    ('drw_w', FixedDataPacketField(MARKER_UINT16)),
    ('drw_h', FixedDataPacketField(MARKER_UINT16)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('data', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: 1, 0)),
))


class PutImageRequest:
    OPCODE = 18

    __slots__ = ('port', 'drawable', 'gc', 'id', 'src_x', 'src_y', 'src_w', 'src_h', 'drw_x', 'drw_y', 'drw_w', 'drw_h', 'width', 'height', 'data',)

    def __init__(
            self, *,
            port: Optional[int] = None,
            drawable: Optional[int] = None,
            gc: Optional[int] = None,
            id: Optional[int] = None,
            src_x: Optional[int] = None,
            src_y: Optional[int] = None,
            src_w: Optional[int] = None,
            src_h: Optional[int] = None,
            drw_x: Optional[int] = None,
            drw_y: Optional[int] = None,
            drw_w: Optional[int] = None,
            drw_h: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.port = port
        self.drawable = drawable
        self.gc = gc
        self.id = id
        self.src_x = src_x
        self.src_y = src_y
        self.src_w = src_w
        self.src_h = src_h
        self.drw_x = drw_x
        self.drw_y = drw_y
        self.drw_w = drw_w
        self.drw_h = drw_h
        self.width = width
        self.height = height
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'port': self.port,
            'drawable': self.drawable,
            'gc': self.gc,
            'id': self.id,
            'src_x': self.src_x,
            'src_y': self.src_y,
            'src_w': self.src_w,
            'src_h': self.src_h,
            'drw_x': self.drw_x,
            'drw_y': self.drw_y,
            'drw_w': self.drw_w,
            'drw_h': self.drw_h,
            'width': self.width,
            'height': self.height,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PutImageRequest':
        return PutImageRequest(**PutImageRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PutImageRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, int, int, int, int, int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PutImageRequest.lib = library.xv_putimage
        PutImageRequest.lib.restype = ctypes.c_uint32
        PutImageRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_int16, ctypes.c_int16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_void_p)


class PutImageRequestCType(ctypes.Structure):
    """xv PutImage"""
    _fields_ = [
        ("port", ctypes.c_uint32),
        ("drawable", ctypes.c_uint32),
        ("gc", ctypes.c_uint32),
        ("id", ctypes.c_uint32),
        ("src_x", ctypes.c_int16),
        ("src_y", ctypes.c_int16),
        ("src_w", ctypes.c_uint16),
        ("src_h", ctypes.c_uint16),
        ("drw_x", ctypes.c_int16),
        ("drw_y", ctypes.c_int16),
        ("drw_w", ctypes.c_uint16),
        ("drw_h", ctypes.c_uint16),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


ShmPutImageRequestPacket = DataPacket((
    ('port', FixedDataPacketField(MARKER_UINT32)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('gc', FixedDataPacketField(MARKER_UINT32)),
    ('shmseg', FixedDataPacketField(MARKER_UINT32)),
    ('id', FixedDataPacketField(MARKER_UINT32)),
    ('offset', FixedDataPacketField(MARKER_UINT32)),
    ('src_x', FixedDataPacketField(MARKER_INT16)),
    ('src_y', FixedDataPacketField(MARKER_INT16)),
    ('src_w', FixedDataPacketField(MARKER_UINT16)),
    ('src_h', FixedDataPacketField(MARKER_UINT16)),
    ('drw_x', FixedDataPacketField(MARKER_INT16)),
    ('drw_y', FixedDataPacketField(MARKER_INT16)),
    ('drw_w', FixedDataPacketField(MARKER_UINT16)),
    ('drw_h', FixedDataPacketField(MARKER_UINT16)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('send_event', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class ShmPutImageRequest:
    OPCODE = 19

    __slots__ = ('port', 'drawable', 'gc', 'shmseg', 'id', 'offset', 'src_x', 'src_y', 'src_w', 'src_h', 'drw_x', 'drw_y', 'drw_w', 'drw_h', 'width', 'height', 'send_event',)

    def __init__(
            self, *,
            port: Optional[int] = None,
            drawable: Optional[int] = None,
            gc: Optional[int] = None,
            shmseg: Optional[int] = None,
            id: Optional[int] = None,
            offset: Optional[int] = None,
            src_x: Optional[int] = None,
            src_y: Optional[int] = None,
            src_w: Optional[int] = None,
            src_h: Optional[int] = None,
            drw_x: Optional[int] = None,
            drw_y: Optional[int] = None,
            drw_w: Optional[int] = None,
            drw_h: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            send_event: Optional[int] = None,
    ) -> None:
        self.port = port
        self.drawable = drawable
        self.gc = gc
        self.shmseg = shmseg
        self.id = id
        self.offset = offset
        self.src_x = src_x
        self.src_y = src_y
        self.src_w = src_w
        self.src_h = src_h
        self.drw_x = drw_x
        self.drw_y = drw_y
        self.drw_w = drw_w
        self.drw_h = drw_h
        self.width = width
        self.height = height
        self.send_event = send_event

    def as_dict(self) -> Dict[str, Any]:
        return {
            'port': self.port,
            'drawable': self.drawable,
            'gc': self.gc,
            'shmseg': self.shmseg,
            'id': self.id,
            'offset': self.offset,
            'src_x': self.src_x,
            'src_y': self.src_y,
            'src_w': self.src_w,
            'src_h': self.src_h,
            'drw_x': self.drw_x,
            'drw_y': self.drw_y,
            'drw_w': self.drw_w,
            'drw_h': self.drw_h,
            'width': self.width,
            'height': self.height,
            'send_event': self.send_event,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ShmPutImageRequest':
        return ShmPutImageRequest(**ShmPutImageRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ShmPutImageRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ShmPutImageRequest.lib = library.xv_shmputimage
        ShmPutImageRequest.lib.restype = ctypes.c_uint32
        ShmPutImageRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_int16, ctypes.c_int16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint8, ctypes.c_uint8 * 3)


class ShmPutImageRequestCType(ctypes.Structure):
    """xv ShmPutImage"""
    _fields_ = [
        ("port", ctypes.c_uint32),
        ("drawable", ctypes.c_uint32),
        ("gc", ctypes.c_uint32),
        ("shmseg", ctypes.c_uint32),
        ("id", ctypes.c_uint32),
        ("offset", ctypes.c_uint32),
        ("src_x", ctypes.c_int16),
        ("src_y", ctypes.c_int16),
        ("src_w", ctypes.c_uint16),
        ("src_h", ctypes.c_uint16),
        ("drw_x", ctypes.c_int16),
        ("drw_y", ctypes.c_int16),
        ("drw_w", ctypes.c_uint16),
        ("drw_h", ctypes.c_uint16),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("send_event", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


# ------------------------------------------------------------------
# Unions

