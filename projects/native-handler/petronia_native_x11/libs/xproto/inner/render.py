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

PictTypeType = NewType('PictTypeType', int)


class PictTypeValues:
    INDEXED = PictTypeType(0)
    DIRECT = PictTypeType(1)


PictureType = NewType('PictureType', int)


class PictureValues:
    NONE = PictureType(0)


PictOpType = NewType('PictOpType', int)


class PictOpValues:
    CLEAR = PictOpType(0)
    SRC = PictOpType(1)
    DST = PictOpType(2)
    OVER = PictOpType(3)
    OVER_REVERSE = PictOpType(4)
    IN = PictOpType(5)
    IN_REVERSE = PictOpType(6)
    OUT = PictOpType(7)
    OUT_REVERSE = PictOpType(8)
    ATOP = PictOpType(9)
    ATOP_REVERSE = PictOpType(10)
    XOR = PictOpType(11)
    ADD = PictOpType(12)
    SATURATE = PictOpType(13)
    DISJOINT_CLEAR = PictOpType(16)
    DISJOINT_SRC = PictOpType(17)
    DISJOINT_DST = PictOpType(18)
    DISJOINT_OVER = PictOpType(19)
    DISJOINT_OVER_REVERSE = PictOpType(20)
    DISJOINT_IN = PictOpType(21)
    DISJOINT_IN_REVERSE = PictOpType(22)
    DISJOINT_OUT = PictOpType(23)
    DISJOINT_OUT_REVERSE = PictOpType(24)
    DISJOINT_ATOP = PictOpType(25)
    DISJOINT_ATOP_REVERSE = PictOpType(26)
    DISJOINT_XOR = PictOpType(27)
    CONJOINT_CLEAR = PictOpType(32)
    CONJOINT_SRC = PictOpType(33)
    CONJOINT_DST = PictOpType(34)
    CONJOINT_OVER = PictOpType(35)
    CONJOINT_OVER_REVERSE = PictOpType(36)
    CONJOINT_IN = PictOpType(37)
    CONJOINT_IN_REVERSE = PictOpType(38)
    CONJOINT_OUT = PictOpType(39)
    CONJOINT_OUT_REVERSE = PictOpType(40)
    CONJOINT_ATOP = PictOpType(41)
    CONJOINT_ATOP_REVERSE = PictOpType(42)
    CONJOINT_XOR = PictOpType(43)
    MULTIPLY = PictOpType(48)
    SCREEN = PictOpType(49)
    OVERLAY = PictOpType(50)
    DARKEN = PictOpType(51)
    LIGHTEN = PictOpType(52)
    COLOR_DODGE = PictOpType(53)
    COLOR_BURN = PictOpType(54)
    HARD_LIGHT = PictOpType(55)
    SOFT_LIGHT = PictOpType(56)
    DIFFERENCE = PictOpType(57)
    EXCLUSION = PictOpType(58)
    HSLHUE = PictOpType(59)
    HSLSATURATION = PictOpType(60)
    HSLCOLOR = PictOpType(61)
    HSLLUMINOSITY = PictOpType(62)


PolyEdgeType = NewType('PolyEdgeType', int)


class PolyEdgeValues:
    SHARP = PolyEdgeType(0)
    SMOOTH = PolyEdgeType(1)


PolyModeType = NewType('PolyModeType', int)


class PolyModeValues:
    PRECISE = PolyModeType(0)
    IMPRECISE = PolyModeType(1)


CpType = NewType('CpType', int)


class CpValues:
    REPEAT = CpType(1)
    ALPHA_MAP = CpType(2)
    ALPHA_XORIGIN = CpType(4)
    ALPHA_YORIGIN = CpType(8)
    CLIP_XORIGIN = CpType(16)
    CLIP_YORIGIN = CpType(32)
    CLIP_MASK = CpType(64)
    GRAPHICS_EXPOSURE = CpType(128)
    SUBWINDOW_MODE = CpType(256)
    POLY_EDGE = CpType(512)
    POLY_MODE = CpType(1024)
    DITHER = CpType(2048)
    COMPONENT_ALPHA = CpType(4096)


SubPixelType = NewType('SubPixelType', int)


class SubPixelValues:
    UNKNOWN = SubPixelType(0)
    HORIZONTAL_RGB = SubPixelType(1)
    HORIZONTAL_BGR = SubPixelType(2)
    VERTICAL_RGB = SubPixelType(3)
    VERTICAL_BGR = SubPixelType(4)
    NONE = SubPixelType(5)


RepeatType = NewType('RepeatType', int)


class RepeatValues:
    NONE = RepeatType(0)
    NORMAL = RepeatType(1)
    PAD = RepeatType(2)
    REFLECT = RepeatType(3)


# ------------------------------------------------------------------
# Aliases

Picture = NewType('Picture', ctypes.c_uint32)
Glyphset = NewType('Glyphset', ctypes.c_uint32)
Pictformat = NewType('Pictformat', ctypes.c_uint32)


# ------------------------------------------------------------------
# Structures, Events, Requests, Replies


DirectformatStructPacket = DataPacket((
    ('red_shift', FixedDataPacketField(MARKER_UINT16)),
    ('red_mask', FixedDataPacketField(MARKER_UINT16)),
    ('green_shift', FixedDataPacketField(MARKER_UINT16)),
    ('green_mask', FixedDataPacketField(MARKER_UINT16)),
    ('blue_shift', FixedDataPacketField(MARKER_UINT16)),
    ('blue_mask', FixedDataPacketField(MARKER_UINT16)),
    ('alpha_shift', FixedDataPacketField(MARKER_UINT16)),
    ('alpha_mask', FixedDataPacketField(MARKER_UINT16)),
))


class DirectformatStruct:
    __slots__ = ('red_shift', 'red_mask', 'green_shift', 'green_mask', 'blue_shift', 'blue_mask', 'alpha_shift', 'alpha_mask',)

    def __init__(
            self, *,
            red_shift: Optional[int] = None,
            red_mask: Optional[int] = None,
            green_shift: Optional[int] = None,
            green_mask: Optional[int] = None,
            blue_shift: Optional[int] = None,
            blue_mask: Optional[int] = None,
            alpha_shift: Optional[int] = None,
            alpha_mask: Optional[int] = None,
    ) -> None:
        self.red_shift = red_shift
        self.red_mask = red_mask
        self.green_shift = green_shift
        self.green_mask = green_mask
        self.blue_shift = blue_shift
        self.blue_mask = blue_mask
        self.alpha_shift = alpha_shift
        self.alpha_mask = alpha_mask

    def as_dict(self) -> Dict[str, Any]:
        return {
            'red_shift': self.red_shift,
            'red_mask': self.red_mask,
            'green_shift': self.green_shift,
            'green_mask': self.green_mask,
            'blue_shift': self.blue_shift,
            'blue_mask': self.blue_mask,
            'alpha_shift': self.alpha_shift,
            'alpha_mask': self.alpha_mask,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DirectformatStruct':
        return DirectformatStruct(**DirectformatStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DirectformatStructPacket.pack(**self.as_dict())


class DirectformatStructCType(ctypes.Structure):
    """render DIRECTFORMAT"""
    _fields_ = [
        ("red_shift", ctypes.c_uint16),
        ("red_mask", ctypes.c_uint16),
        ("green_shift", ctypes.c_uint16),
        ("green_mask", ctypes.c_uint16),
        ("blue_shift", ctypes.c_uint16),
        ("blue_mask", ctypes.c_uint16),
        ("alpha_shift", ctypes.c_uint16),
        ("alpha_mask", ctypes.c_uint16),
    ]


PictforminfoStructPacket = DataPacket((
    ('id', FixedDataPacketField(MARKER_UINT32)),
    ('type', FixedDataPacketField(MARKER_UINT8)),
    ('depth', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
    ('direct', FixedDataPacketField(MARKER_UINT32)),
    ('colormap', FixedDataPacketField(MARKER_UINT32)),
))


class PictforminfoStruct:
    __slots__ = ('id', 'type', 'depth', 'direct', 'colormap',)

    def __init__(
            self, *,
            id: Optional[int] = None,
            type: Optional[int] = None,
            depth: Optional[int] = None,
            direct: Optional[int] = None,
            colormap: Optional[int] = None,
    ) -> None:
        self.id = id
        self.type = type
        self.depth = depth
        self.direct = direct
        self.colormap = colormap

    def as_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'type': self.type,
            'depth': self.depth,
            'direct': self.direct,
            'colormap': self.colormap,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PictforminfoStruct':
        return PictforminfoStruct(**PictforminfoStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PictforminfoStructPacket.pack(**self.as_dict())


class PictforminfoStructCType(ctypes.Structure):
    """render PICTFORMINFO"""
    _fields_ = [
        ("id", ctypes.c_uint32),
        ("type", ctypes.c_uint8),
        ("depth", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 2),
        ("direct", ctypes.c_uint32),
        ("colormap", ctypes.c_uint32),
    ]


PictvisualStructPacket = DataPacket((
    ('visual', FixedDataPacketField(MARKER_UINT32)),
    ('format', FixedDataPacketField(MARKER_UINT32)),
))


class PictvisualStruct:
    __slots__ = ('visual', 'format',)

    def __init__(
            self, *,
            visual: Optional[int] = None,
            format: Optional[int] = None,
    ) -> None:
        self.visual = visual
        self.format = format

    def as_dict(self) -> Dict[str, Any]:
        return {
            'visual': self.visual,
            'format': self.format,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PictvisualStruct':
        return PictvisualStruct(**PictvisualStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PictvisualStructPacket.pack(**self.as_dict())


class PictvisualStructCType(ctypes.Structure):
    """render PICTVISUAL"""
    _fields_ = [
        ("visual", ctypes.c_uint32),
        ("format", ctypes.c_uint32),
    ]


PictdepthStructPacket = DataPacket((
    ('depth', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('num_visuals', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(4)),
    ('visuals', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_visuals'], 0)),
))


class PictdepthStruct:
    __slots__ = ('depth', 'num_visuals', 'visuals',)

    def __init__(
            self, *,
            depth: Optional[int] = None,
            num_visuals: Optional[int] = None,
            visuals: Optional[Sequence[int]] = None,
    ) -> None:
        self.depth = depth
        self.num_visuals = num_visuals
        self.visuals = visuals

    def as_dict(self) -> Dict[str, Any]:
        return {
            'depth': self.depth,
            'num_visuals': self.num_visuals,
            'visuals': self.visuals,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PictdepthStruct':
        return PictdepthStruct(**PictdepthStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PictdepthStructPacket.pack(**self.as_dict())


class PictdepthStructCType(ctypes.Structure):
    """render PICTDEPTH"""
    _fields_ = [
        ("depth", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
        ("num_visuals", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 4),
        ("var_data", ctypes.c_void_p),
    ]


PictscreenStructPacket = DataPacket((
    ('num_depths', FixedDataPacketField(MARKER_UINT32)),
    ('fallback', FixedDataPacketField(MARKER_UINT32)),
    ('depths', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_depths'], 0)),
))


class PictscreenStruct:
    __slots__ = ('num_depths', 'fallback', 'depths',)

    def __init__(
            self, *,
            num_depths: Optional[int] = None,
            fallback: Optional[int] = None,
            depths: Optional[Sequence[int]] = None,
    ) -> None:
        self.num_depths = num_depths
        self.fallback = fallback
        self.depths = depths

    def as_dict(self) -> Dict[str, Any]:
        return {
            'num_depths': self.num_depths,
            'fallback': self.fallback,
            'depths': self.depths,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PictscreenStruct':
        return PictscreenStruct(**PictscreenStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PictscreenStructPacket.pack(**self.as_dict())


class PictscreenStructCType(ctypes.Structure):
    """render PICTSCREEN"""
    _fields_ = [
        ("num_depths", ctypes.c_uint32),
        ("fallback", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


IndexvalueStructPacket = DataPacket((
    ('pixel', FixedDataPacketField(MARKER_UINT32)),
    ('red', FixedDataPacketField(MARKER_UINT16)),
    ('green', FixedDataPacketField(MARKER_UINT16)),
    ('blue', FixedDataPacketField(MARKER_UINT16)),
    ('alpha', FixedDataPacketField(MARKER_UINT16)),
))


class IndexvalueStruct:
    __slots__ = ('pixel', 'red', 'green', 'blue', 'alpha',)

    def __init__(
            self, *,
            pixel: Optional[int] = None,
            red: Optional[int] = None,
            green: Optional[int] = None,
            blue: Optional[int] = None,
            alpha: Optional[int] = None,
    ) -> None:
        self.pixel = pixel
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def as_dict(self) -> Dict[str, Any]:
        return {
            'pixel': self.pixel,
            'red': self.red,
            'green': self.green,
            'blue': self.blue,
            'alpha': self.alpha,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'IndexvalueStruct':
        return IndexvalueStruct(**IndexvalueStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return IndexvalueStructPacket.pack(**self.as_dict())


class IndexvalueStructCType(ctypes.Structure):
    """render INDEXVALUE"""
    _fields_ = [
        ("pixel", ctypes.c_uint32),
        ("red", ctypes.c_uint16),
        ("green", ctypes.c_uint16),
        ("blue", ctypes.c_uint16),
        ("alpha", ctypes.c_uint16),
    ]


ColorStructPacket = DataPacket((
    ('red', FixedDataPacketField(MARKER_UINT16)),
    ('green', FixedDataPacketField(MARKER_UINT16)),
    ('blue', FixedDataPacketField(MARKER_UINT16)),
    ('alpha', FixedDataPacketField(MARKER_UINT16)),
))


class ColorStruct:
    __slots__ = ('red', 'green', 'blue', 'alpha',)

    def __init__(
            self, *,
            red: Optional[int] = None,
            green: Optional[int] = None,
            blue: Optional[int] = None,
            alpha: Optional[int] = None,
    ) -> None:
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def as_dict(self) -> Dict[str, Any]:
        return {
            'red': self.red,
            'green': self.green,
            'blue': self.blue,
            'alpha': self.alpha,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ColorStruct':
        return ColorStruct(**ColorStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ColorStructPacket.pack(**self.as_dict())


class ColorStructCType(ctypes.Structure):
    """render COLOR"""
    _fields_ = [
        ("red", ctypes.c_uint16),
        ("green", ctypes.c_uint16),
        ("blue", ctypes.c_uint16),
        ("alpha", ctypes.c_uint16),
    ]


PointfixStructPacket = DataPacket((
    ('x', FixedDataPacketField(MARKER_UINT32)),
    ('y', FixedDataPacketField(MARKER_UINT32)),
))


class PointfixStruct:
    __slots__ = ('x', 'y',)

    def __init__(
            self, *,
            x: Optional[int] = None,
            y: Optional[int] = None,
    ) -> None:
        self.x = x
        self.y = y

    def as_dict(self) -> Dict[str, Any]:
        return {
            'x': self.x,
            'y': self.y,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PointfixStruct':
        return PointfixStruct(**PointfixStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PointfixStructPacket.pack(**self.as_dict())


class PointfixStructCType(ctypes.Structure):
    """render POINTFIX"""
    _fields_ = [
        ("x", ctypes.c_uint32),
        ("y", ctypes.c_uint32),
    ]


LinefixStructPacket = DataPacket((
    ('p1', FixedDataPacketField(MARKER_UINT32)),
    ('p2', FixedDataPacketField(MARKER_UINT32)),
))


class LinefixStruct:
    __slots__ = ('p1', 'p2',)

    def __init__(
            self, *,
            p1: Optional[int] = None,
            p2: Optional[int] = None,
    ) -> None:
        self.p1 = p1
        self.p2 = p2

    def as_dict(self) -> Dict[str, Any]:
        return {
            'p1': self.p1,
            'p2': self.p2,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'LinefixStruct':
        return LinefixStruct(**LinefixStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return LinefixStructPacket.pack(**self.as_dict())


class LinefixStructCType(ctypes.Structure):
    """render LINEFIX"""
    _fields_ = [
        ("p1", ctypes.c_uint32),
        ("p2", ctypes.c_uint32),
    ]


TriangleStructPacket = DataPacket((
    ('p1', FixedDataPacketField(MARKER_UINT32)),
    ('p2', FixedDataPacketField(MARKER_UINT32)),
    ('p3', FixedDataPacketField(MARKER_UINT32)),
))


class TriangleStruct:
    __slots__ = ('p1', 'p2', 'p3',)

    def __init__(
            self, *,
            p1: Optional[int] = None,
            p2: Optional[int] = None,
            p3: Optional[int] = None,
    ) -> None:
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def as_dict(self) -> Dict[str, Any]:
        return {
            'p1': self.p1,
            'p2': self.p2,
            'p3': self.p3,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'TriangleStruct':
        return TriangleStruct(**TriangleStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return TriangleStructPacket.pack(**self.as_dict())


class TriangleStructCType(ctypes.Structure):
    """render TRIANGLE"""
    _fields_ = [
        ("p1", ctypes.c_uint32),
        ("p2", ctypes.c_uint32),
        ("p3", ctypes.c_uint32),
    ]


TrapezoidStructPacket = DataPacket((
    ('top', FixedDataPacketField(MARKER_UINT32)),
    ('bottom', FixedDataPacketField(MARKER_UINT32)),
    ('left', FixedDataPacketField(MARKER_UINT32)),
    ('right', FixedDataPacketField(MARKER_UINT32)),
))


class TrapezoidStruct:
    __slots__ = ('top', 'bottom', 'left', 'right',)

    def __init__(
            self, *,
            top: Optional[int] = None,
            bottom: Optional[int] = None,
            left: Optional[int] = None,
            right: Optional[int] = None,
    ) -> None:
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right

    def as_dict(self) -> Dict[str, Any]:
        return {
            'top': self.top,
            'bottom': self.bottom,
            'left': self.left,
            'right': self.right,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'TrapezoidStruct':
        return TrapezoidStruct(**TrapezoidStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return TrapezoidStructPacket.pack(**self.as_dict())


class TrapezoidStructCType(ctypes.Structure):
    """render TRAPEZOID"""
    _fields_ = [
        ("top", ctypes.c_uint32),
        ("bottom", ctypes.c_uint32),
        ("left", ctypes.c_uint32),
        ("right", ctypes.c_uint32),
    ]


GlyphinfoStructPacket = DataPacket((
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('x', FixedDataPacketField(MARKER_INT16)),
    ('y', FixedDataPacketField(MARKER_INT16)),
    ('x_off', FixedDataPacketField(MARKER_INT16)),
    ('y_off', FixedDataPacketField(MARKER_INT16)),
))


class GlyphinfoStruct:
    __slots__ = ('width', 'height', 'x', 'y', 'x_off', 'y_off',)

    def __init__(
            self, *,
            width: Optional[int] = None,
            height: Optional[int] = None,
            x: Optional[int] = None,
            y: Optional[int] = None,
            x_off: Optional[int] = None,
            y_off: Optional[int] = None,
    ) -> None:
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.x_off = x_off
        self.y_off = y_off

    def as_dict(self) -> Dict[str, Any]:
        return {
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y,
            'x_off': self.x_off,
            'y_off': self.y_off,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GlyphinfoStruct':
        return GlyphinfoStruct(**GlyphinfoStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GlyphinfoStructPacket.pack(**self.as_dict())


class GlyphinfoStructCType(ctypes.Structure):
    """render GLYPHINFO"""
    _fields_ = [
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("x", ctypes.c_int16),
        ("y", ctypes.c_int16),
        ("x_off", ctypes.c_int16),
        ("y_off", ctypes.c_int16),
    ]


QueryVersionRequestCookie = NewType('QueryVersionRequestCookie', ctypes.c_uint32)


QueryVersionRequestPacket = DataPacket((
    ('client_major_version', FixedDataPacketField(MARKER_UINT32)),
    ('client_minor_version', FixedDataPacketField(MARKER_UINT32)),
))


class QueryVersionRequest:
    OPCODE = 0

    __slots__ = ('client_major_version', 'client_minor_version',)

    def __init__(
            self, *,
            client_major_version: Optional[int] = None,
            client_minor_version: Optional[int] = None,
    ) -> None:
        self.client_major_version = client_major_version
        self.client_minor_version = client_minor_version

    def as_dict(self) -> Dict[str, Any]:
        return {
            'client_major_version': self.client_major_version,
            'client_minor_version': self.client_minor_version,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryVersionRequest':
        return QueryVersionRequest(**QueryVersionRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryVersionRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], QueryVersionRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryVersionRequest.lib = library.render_queryversion
        QueryVersionRequest.lib.restype = QueryVersionRequestCookie
        QueryVersionRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class QueryVersionRequestCType(ctypes.Structure):
    """render QueryVersion"""
    _fields_ = [
        ("client_major_version", ctypes.c_uint32),
        ("client_minor_version", ctypes.c_uint32),
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
    """render QueryVersion_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("major_version", ctypes.c_uint32),
        ("minor_version", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 16),
    ]


QueryPictFormatsRequestCookie = NewType('QueryPictFormatsRequestCookie', ctypes.c_uint32)


QueryPictFormatsRequestPacket = DataPacket((
))


class QueryPictFormatsRequest:
    OPCODE = 1

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryPictFormatsRequest':
        return QueryPictFormatsRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], QueryPictFormatsRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryPictFormatsRequest.lib = library.render_querypictformats
        QueryPictFormatsRequest.lib.restype = QueryPictFormatsRequestCookie
        QueryPictFormatsRequest.lib.argstype = ()


class QueryPictFormatsRequestCType(ctypes.Structure):
    """render QueryPictFormats"""
    _fields_ = [
    ]


QueryPictFormatsReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('num_formats', FixedDataPacketField(MARKER_UINT32)),
    ('num_screens', FixedDataPacketField(MARKER_UINT32)),
    ('num_depths', FixedDataPacketField(MARKER_UINT32)),
    ('num_visuals', FixedDataPacketField(MARKER_UINT32)),
    ('num_subpixel', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(4)),
    ('formats', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_formats'], 0)),
    ('screens', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_screens'], 0)),
    ('subpixels', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_subpixel'], 0)),
))


class QueryPictFormatsReplyReply:
    __slots__ = ('num_formats', 'num_screens', 'num_depths', 'num_visuals', 'num_subpixel', 'formats', 'screens', 'subpixels',)

    def __init__(
            self, *,
            num_formats: Optional[int] = None,
            num_screens: Optional[int] = None,
            num_depths: Optional[int] = None,
            num_visuals: Optional[int] = None,
            num_subpixel: Optional[int] = None,
            formats: Optional[Sequence[int]] = None,
            screens: Optional[Sequence[int]] = None,
            subpixels: Optional[Sequence[int]] = None,
    ) -> None:
        self.num_formats = num_formats
        self.num_screens = num_screens
        self.num_depths = num_depths
        self.num_visuals = num_visuals
        self.num_subpixel = num_subpixel
        self.formats = formats
        self.screens = screens
        self.subpixels = subpixels

    def as_dict(self) -> Dict[str, Any]:
        return {
            'num_formats': self.num_formats,
            'num_screens': self.num_screens,
            'num_depths': self.num_depths,
            'num_visuals': self.num_visuals,
            'num_subpixel': self.num_subpixel,
            'formats': self.formats,
            'screens': self.screens,
            'subpixels': self.subpixels,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryPictFormatsReplyReply':
        return QueryPictFormatsReplyReply(**QueryPictFormatsReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryPictFormatsReplyReplyPacket.pack(**self.as_dict())


class QueryPictFormatsReplyReplyCType(ctypes.Structure):
    """render QueryPictFormats_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("num_formats", ctypes.c_uint32),
        ("num_screens", ctypes.c_uint32),
        ("num_depths", ctypes.c_uint32),
        ("num_visuals", ctypes.c_uint32),
        ("num_subpixel", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 4),
        ("var_data", ctypes.c_void_p),
    ]


QueryPictIndexValuesRequestCookie = NewType('QueryPictIndexValuesRequestCookie', ctypes.c_uint32)


QueryPictIndexValuesRequestPacket = DataPacket((
    ('format', FixedDataPacketField(MARKER_UINT32)),
))


class QueryPictIndexValuesRequest:
    OPCODE = 2

    __slots__ = ('format',)

    def __init__(
            self, *,
            format: Optional[int] = None,
    ) -> None:
        self.format = format

    def as_dict(self) -> Dict[str, Any]:
        return {
            'format': self.format,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryPictIndexValuesRequest':
        return QueryPictIndexValuesRequest(**QueryPictIndexValuesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryPictIndexValuesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], QueryPictIndexValuesRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryPictIndexValuesRequest.lib = library.render_querypictindexvalues
        QueryPictIndexValuesRequest.lib.restype = QueryPictIndexValuesRequestCookie
        QueryPictIndexValuesRequest.lib.argstype = (ctypes.c_uint32,)


class QueryPictIndexValuesRequestCType(ctypes.Structure):
    """render QueryPictIndexValues"""
    _fields_ = [
        ("format", ctypes.c_uint32),
    ]


QueryPictIndexValuesReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('num_values', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('values', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_values'], 0)),
))


class QueryPictIndexValuesReplyReply:
    __slots__ = ('num_values', 'values',)

    def __init__(
            self, *,
            num_values: Optional[int] = None,
            values: Optional[Sequence[int]] = None,
    ) -> None:
        self.num_values = num_values
        self.values = values

    def as_dict(self) -> Dict[str, Any]:
        return {
            'num_values': self.num_values,
            'values': self.values,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryPictIndexValuesReplyReply':
        return QueryPictIndexValuesReplyReply(**QueryPictIndexValuesReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryPictIndexValuesReplyReplyPacket.pack(**self.as_dict())


class QueryPictIndexValuesReplyReplyCType(ctypes.Structure):
    """render QueryPictIndexValues_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("num_values", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


CreatePictureRequestPacket = DataPacket((
    ('pid', FixedDataPacketField(MARKER_UINT32)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('format', FixedDataPacketField(MARKER_UINT32)),
    ('value_mask', FixedDataPacketField(MARKER_UINT32)),
    ('value_list', BitDataPacketField(lambda d, c: d['value_mask'], {
        CpValues.REPEAT: FixedDataPacketField(MARKER_UINT32),
        CpValues.ALPHA_MAP: FixedDataPacketField(MARKER_UINT32),
        CpValues.ALPHA_XORIGIN: FixedDataPacketField(MARKER_INT32),
        CpValues.ALPHA_YORIGIN: FixedDataPacketField(MARKER_INT32),
        CpValues.CLIP_XORIGIN: FixedDataPacketField(MARKER_INT32),
        CpValues.CLIP_YORIGIN: FixedDataPacketField(MARKER_INT32),
        CpValues.CLIP_MASK: FixedDataPacketField(MARKER_UINT32),
        CpValues.GRAPHICS_EXPOSURE: FixedDataPacketField(MARKER_UINT32),
        CpValues.SUBWINDOW_MODE: FixedDataPacketField(MARKER_UINT32),
        CpValues.POLY_EDGE: FixedDataPacketField(MARKER_UINT32),
        CpValues.POLY_MODE: FixedDataPacketField(MARKER_UINT32),
        CpValues.DITHER: FixedDataPacketField(MARKER_UINT32),
        CpValues.COMPONENT_ALPHA: FixedDataPacketField(MARKER_UINT32),
    }, 0)),
))


class CreatePictureRequest:
    OPCODE = 4

    __slots__ = ('pid', 'drawable', 'format', 'value_mask', 'value_list',)

    def __init__(
            self, *,
            pid: Optional[int] = None,
            drawable: Optional[int] = None,
            format: Optional[int] = None,
            value_mask: Optional[int] = None,
            value_list: Optional[Mapping[str, CpValues]] = None,
    ) -> None:
        self.pid = pid
        self.drawable = drawable
        self.format = format
        self.value_mask = value_mask
        self.value_list = value_list

    def as_dict(self) -> Dict[str, Any]:
        return {
            'pid': self.pid,
            'drawable': self.drawable,
            'format': self.format,
            'value_mask': self.value_mask,
            'value_list': self.value_list,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreatePictureRequest':
        return CreatePictureRequest(**CreatePictureRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreatePictureRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, Mapping[str, CpValues]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreatePictureRequest.lib = library.render_createpicture
        CreatePictureRequest.lib.restype = ctypes.c_uint32
        CreatePictureRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)


class CreatePictureRequestCType(ctypes.Structure):
    """render CreatePicture"""
    _fields_ = [
        ("pid", ctypes.c_uint32),
        ("drawable", ctypes.c_uint32),
        ("format", ctypes.c_uint32),
        ("value_mask", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


ChangePictureRequestPacket = DataPacket((
    ('picture', FixedDataPacketField(MARKER_UINT32)),
    ('value_mask', FixedDataPacketField(MARKER_UINT32)),
    ('value_list', BitDataPacketField(lambda d, c: d['value_mask'], {
        CpValues.REPEAT: FixedDataPacketField(MARKER_UINT32),
        CpValues.ALPHA_MAP: FixedDataPacketField(MARKER_UINT32),
        CpValues.ALPHA_XORIGIN: FixedDataPacketField(MARKER_INT32),
        CpValues.ALPHA_YORIGIN: FixedDataPacketField(MARKER_INT32),
        CpValues.CLIP_XORIGIN: FixedDataPacketField(MARKER_INT32),
        CpValues.CLIP_YORIGIN: FixedDataPacketField(MARKER_INT32),
        CpValues.CLIP_MASK: FixedDataPacketField(MARKER_UINT32),
        CpValues.GRAPHICS_EXPOSURE: FixedDataPacketField(MARKER_UINT32),
        CpValues.SUBWINDOW_MODE: FixedDataPacketField(MARKER_UINT32),
        CpValues.POLY_EDGE: FixedDataPacketField(MARKER_UINT32),
        CpValues.POLY_MODE: FixedDataPacketField(MARKER_UINT32),
        CpValues.DITHER: FixedDataPacketField(MARKER_UINT32),
        CpValues.COMPONENT_ALPHA: FixedDataPacketField(MARKER_UINT32),
    }, 0)),
))


class ChangePictureRequest:
    OPCODE = 5

    __slots__ = ('picture', 'value_mask', 'value_list',)

    def __init__(
            self, *,
            picture: Optional[int] = None,
            value_mask: Optional[int] = None,
            value_list: Optional[Mapping[str, CpValues]] = None,
    ) -> None:
        self.picture = picture
        self.value_mask = value_mask
        self.value_list = value_list

    def as_dict(self) -> Dict[str, Any]:
        return {
            'picture': self.picture,
            'value_mask': self.value_mask,
            'value_list': self.value_list,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ChangePictureRequest':
        return ChangePictureRequest(**ChangePictureRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ChangePictureRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Mapping[str, CpValues]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ChangePictureRequest.lib = library.render_changepicture
        ChangePictureRequest.lib.restype = ctypes.c_uint32
        ChangePictureRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)


class ChangePictureRequestCType(ctypes.Structure):
    """render ChangePicture"""
    _fields_ = [
        ("picture", ctypes.c_uint32),
        ("value_mask", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


SetPictureClipRectanglesRequestPacket = DataPacket((
    ('picture', FixedDataPacketField(MARKER_UINT32)),
    ('clip_x_origin', FixedDataPacketField(MARKER_INT16)),
    ('clip_y_origin', FixedDataPacketField(MARKER_INT16)),
    ('rectangles', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 1, 0)),
))


class SetPictureClipRectanglesRequest:
    OPCODE = 6

    __slots__ = ('picture', 'clip_x_origin', 'clip_y_origin', 'rectangles',)

    def __init__(
            self, *,
            picture: Optional[int] = None,
            clip_x_origin: Optional[int] = None,
            clip_y_origin: Optional[int] = None,
            rectangles: Optional[Sequence[int]] = None,
    ) -> None:
        self.picture = picture
        self.clip_x_origin = clip_x_origin
        self.clip_y_origin = clip_y_origin
        self.rectangles = rectangles

    def as_dict(self) -> Dict[str, Any]:
        return {
            'picture': self.picture,
            'clip_x_origin': self.clip_x_origin,
            'clip_y_origin': self.clip_y_origin,
            'rectangles': self.rectangles,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetPictureClipRectanglesRequest':
        return SetPictureClipRectanglesRequest(**SetPictureClipRectanglesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetPictureClipRectanglesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetPictureClipRectanglesRequest.lib = library.render_setpicturecliprectangles
        SetPictureClipRectanglesRequest.lib.restype = ctypes.c_uint32
        SetPictureClipRectanglesRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16, ctypes.c_void_p)


class SetPictureClipRectanglesRequestCType(ctypes.Structure):
    """render SetPictureClipRectangles"""
    _fields_ = [
        ("picture", ctypes.c_uint32),
        ("clip_x_origin", ctypes.c_int16),
        ("clip_y_origin", ctypes.c_int16),
        ("var_data", ctypes.c_void_p),
    ]


FreePictureRequestPacket = DataPacket((
    ('picture', FixedDataPacketField(MARKER_UINT32)),
))


class FreePictureRequest:
    OPCODE = 7

    __slots__ = ('picture',)

    def __init__(
            self, *,
            picture: Optional[int] = None,
    ) -> None:
        self.picture = picture

    def as_dict(self) -> Dict[str, Any]:
        return {
            'picture': self.picture,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'FreePictureRequest':
        return FreePictureRequest(**FreePictureRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return FreePictureRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        FreePictureRequest.lib = library.render_freepicture
        FreePictureRequest.lib.restype = ctypes.c_uint32
        FreePictureRequest.lib.argstype = (ctypes.c_uint32,)


class FreePictureRequestCType(ctypes.Structure):
    """render FreePicture"""
    _fields_ = [
        ("picture", ctypes.c_uint32),
    ]


CompositeRequestPacket = DataPacket((
    ('op', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
    ('src', FixedDataPacketField(MARKER_UINT32)),
    ('mask', FixedDataPacketField(MARKER_UINT32)),
    ('dst', FixedDataPacketField(MARKER_UINT32)),
    ('src_x', FixedDataPacketField(MARKER_INT16)),
    ('src_y', FixedDataPacketField(MARKER_INT16)),
    ('mask_x', FixedDataPacketField(MARKER_INT16)),
    ('mask_y', FixedDataPacketField(MARKER_INT16)),
    ('dst_x', FixedDataPacketField(MARKER_INT16)),
    ('dst_y', FixedDataPacketField(MARKER_INT16)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
))


class CompositeRequest:
    OPCODE = 8

    __slots__ = ('op', 'src', 'mask', 'dst', 'src_x', 'src_y', 'mask_x', 'mask_y', 'dst_x', 'dst_y', 'width', 'height',)

    def __init__(
            self, *,
            op: Optional[int] = None,
            src: Optional[int] = None,
            mask: Optional[int] = None,
            dst: Optional[int] = None,
            src_x: Optional[int] = None,
            src_y: Optional[int] = None,
            mask_x: Optional[int] = None,
            mask_y: Optional[int] = None,
            dst_x: Optional[int] = None,
            dst_y: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
    ) -> None:
        self.op = op
        self.src = src
        self.mask = mask
        self.dst = dst
        self.src_x = src_x
        self.src_y = src_y
        self.mask_x = mask_x
        self.mask_y = mask_y
        self.dst_x = dst_x
        self.dst_y = dst_y
        self.width = width
        self.height = height

    def as_dict(self) -> Dict[str, Any]:
        return {
            'op': self.op,
            'src': self.src,
            'mask': self.mask,
            'dst': self.dst,
            'src_x': self.src_x,
            'src_y': self.src_y,
            'mask_x': self.mask_x,
            'mask_y': self.mask_y,
            'dst_x': self.dst_x,
            'dst_y': self.dst_y,
            'width': self.width,
            'height': self.height,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CompositeRequest':
        return CompositeRequest(**CompositeRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CompositeRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, int, int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CompositeRequest.lib = library.render_composite
        CompositeRequest.lib.restype = ctypes.c_uint32
        CompositeRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint8 * 3, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16, ctypes.c_int16, ctypes.c_int16, ctypes.c_int16, ctypes.c_int16, ctypes.c_uint16, ctypes.c_uint16)


class CompositeRequestCType(ctypes.Structure):
    """render Composite"""
    _fields_ = [
        ("op", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
        ("src", ctypes.c_uint32),
        ("mask", ctypes.c_uint32),
        ("dst", ctypes.c_uint32),
        ("src_x", ctypes.c_int16),
        ("src_y", ctypes.c_int16),
        ("mask_x", ctypes.c_int16),
        ("mask_y", ctypes.c_int16),
        ("dst_x", ctypes.c_int16),
        ("dst_y", ctypes.c_int16),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
    ]


TrapezoidsRequestPacket = DataPacket((
    ('op', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
    ('src', FixedDataPacketField(MARKER_UINT32)),
    ('dst', FixedDataPacketField(MARKER_UINT32)),
    ('mask_format', FixedDataPacketField(MARKER_UINT32)),
    ('src_x', FixedDataPacketField(MARKER_INT16)),
    ('src_y', FixedDataPacketField(MARKER_INT16)),
    ('traps', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 1, 0)),
))


class TrapezoidsRequest:
    OPCODE = 10

    __slots__ = ('op', 'src', 'dst', 'mask_format', 'src_x', 'src_y', 'traps',)

    def __init__(
            self, *,
            op: Optional[int] = None,
            src: Optional[int] = None,
            dst: Optional[int] = None,
            mask_format: Optional[int] = None,
            src_x: Optional[int] = None,
            src_y: Optional[int] = None,
            traps: Optional[Sequence[int]] = None,
    ) -> None:
        self.op = op
        self.src = src
        self.dst = dst
        self.mask_format = mask_format
        self.src_x = src_x
        self.src_y = src_y
        self.traps = traps

    def as_dict(self) -> Dict[str, Any]:
        return {
            'op': self.op,
            'src': self.src,
            'dst': self.dst,
            'mask_format': self.mask_format,
            'src_x': self.src_x,
            'src_y': self.src_y,
            'traps': self.traps,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'TrapezoidsRequest':
        return TrapezoidsRequest(**TrapezoidsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return TrapezoidsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        TrapezoidsRequest.lib = library.render_trapezoids
        TrapezoidsRequest.lib.restype = ctypes.c_uint32
        TrapezoidsRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint8 * 3, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16, ctypes.c_void_p)


class TrapezoidsRequestCType(ctypes.Structure):
    """render Trapezoids"""
    _fields_ = [
        ("op", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
        ("src", ctypes.c_uint32),
        ("dst", ctypes.c_uint32),
        ("mask_format", ctypes.c_uint32),
        ("src_x", ctypes.c_int16),
        ("src_y", ctypes.c_int16),
        ("var_data", ctypes.c_void_p),
    ]


TrianglesRequestPacket = DataPacket((
    ('op', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
    ('src', FixedDataPacketField(MARKER_UINT32)),
    ('dst', FixedDataPacketField(MARKER_UINT32)),
    ('mask_format', FixedDataPacketField(MARKER_UINT32)),
    ('src_x', FixedDataPacketField(MARKER_INT16)),
    ('src_y', FixedDataPacketField(MARKER_INT16)),
    ('triangles', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 1, 0)),
))


class TrianglesRequest:
    OPCODE = 11

    __slots__ = ('op', 'src', 'dst', 'mask_format', 'src_x', 'src_y', 'triangles',)

    def __init__(
            self, *,
            op: Optional[int] = None,
            src: Optional[int] = None,
            dst: Optional[int] = None,
            mask_format: Optional[int] = None,
            src_x: Optional[int] = None,
            src_y: Optional[int] = None,
            triangles: Optional[Sequence[int]] = None,
    ) -> None:
        self.op = op
        self.src = src
        self.dst = dst
        self.mask_format = mask_format
        self.src_x = src_x
        self.src_y = src_y
        self.triangles = triangles

    def as_dict(self) -> Dict[str, Any]:
        return {
            'op': self.op,
            'src': self.src,
            'dst': self.dst,
            'mask_format': self.mask_format,
            'src_x': self.src_x,
            'src_y': self.src_y,
            'triangles': self.triangles,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'TrianglesRequest':
        return TrianglesRequest(**TrianglesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return TrianglesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        TrianglesRequest.lib = library.render_triangles
        TrianglesRequest.lib.restype = ctypes.c_uint32
        TrianglesRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint8 * 3, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16, ctypes.c_void_p)


class TrianglesRequestCType(ctypes.Structure):
    """render Triangles"""
    _fields_ = [
        ("op", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
        ("src", ctypes.c_uint32),
        ("dst", ctypes.c_uint32),
        ("mask_format", ctypes.c_uint32),
        ("src_x", ctypes.c_int16),
        ("src_y", ctypes.c_int16),
        ("var_data", ctypes.c_void_p),
    ]


TriStripRequestPacket = DataPacket((
    ('op', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
    ('src', FixedDataPacketField(MARKER_UINT32)),
    ('dst', FixedDataPacketField(MARKER_UINT32)),
    ('mask_format', FixedDataPacketField(MARKER_UINT32)),
    ('src_x', FixedDataPacketField(MARKER_INT16)),
    ('src_y', FixedDataPacketField(MARKER_INT16)),
    ('points', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 1, 0)),
))


class TriStripRequest:
    OPCODE = 12

    __slots__ = ('op', 'src', 'dst', 'mask_format', 'src_x', 'src_y', 'points',)

    def __init__(
            self, *,
            op: Optional[int] = None,
            src: Optional[int] = None,
            dst: Optional[int] = None,
            mask_format: Optional[int] = None,
            src_x: Optional[int] = None,
            src_y: Optional[int] = None,
            points: Optional[Sequence[int]] = None,
    ) -> None:
        self.op = op
        self.src = src
        self.dst = dst
        self.mask_format = mask_format
        self.src_x = src_x
        self.src_y = src_y
        self.points = points

    def as_dict(self) -> Dict[str, Any]:
        return {
            'op': self.op,
            'src': self.src,
            'dst': self.dst,
            'mask_format': self.mask_format,
            'src_x': self.src_x,
            'src_y': self.src_y,
            'points': self.points,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'TriStripRequest':
        return TriStripRequest(**TriStripRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return TriStripRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        TriStripRequest.lib = library.render_tristrip
        TriStripRequest.lib.restype = ctypes.c_uint32
        TriStripRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint8 * 3, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16, ctypes.c_void_p)


class TriStripRequestCType(ctypes.Structure):
    """render TriStrip"""
    _fields_ = [
        ("op", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
        ("src", ctypes.c_uint32),
        ("dst", ctypes.c_uint32),
        ("mask_format", ctypes.c_uint32),
        ("src_x", ctypes.c_int16),
        ("src_y", ctypes.c_int16),
        ("var_data", ctypes.c_void_p),
    ]


TriFanRequestPacket = DataPacket((
    ('op', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
    ('src', FixedDataPacketField(MARKER_UINT32)),
    ('dst', FixedDataPacketField(MARKER_UINT32)),
    ('mask_format', FixedDataPacketField(MARKER_UINT32)),
    ('src_x', FixedDataPacketField(MARKER_INT16)),
    ('src_y', FixedDataPacketField(MARKER_INT16)),
    ('points', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 1, 0)),
))


class TriFanRequest:
    OPCODE = 13

    __slots__ = ('op', 'src', 'dst', 'mask_format', 'src_x', 'src_y', 'points',)

    def __init__(
            self, *,
            op: Optional[int] = None,
            src: Optional[int] = None,
            dst: Optional[int] = None,
            mask_format: Optional[int] = None,
            src_x: Optional[int] = None,
            src_y: Optional[int] = None,
            points: Optional[Sequence[int]] = None,
    ) -> None:
        self.op = op
        self.src = src
        self.dst = dst
        self.mask_format = mask_format
        self.src_x = src_x
        self.src_y = src_y
        self.points = points

    def as_dict(self) -> Dict[str, Any]:
        return {
            'op': self.op,
            'src': self.src,
            'dst': self.dst,
            'mask_format': self.mask_format,
            'src_x': self.src_x,
            'src_y': self.src_y,
            'points': self.points,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'TriFanRequest':
        return TriFanRequest(**TriFanRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return TriFanRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        TriFanRequest.lib = library.render_trifan
        TriFanRequest.lib.restype = ctypes.c_uint32
        TriFanRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint8 * 3, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16, ctypes.c_void_p)


class TriFanRequestCType(ctypes.Structure):
    """render TriFan"""
    _fields_ = [
        ("op", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
        ("src", ctypes.c_uint32),
        ("dst", ctypes.c_uint32),
        ("mask_format", ctypes.c_uint32),
        ("src_x", ctypes.c_int16),
        ("src_y", ctypes.c_int16),
        ("var_data", ctypes.c_void_p),
    ]


CreateGlyphSetRequestPacket = DataPacket((
    ('gsid', FixedDataPacketField(MARKER_UINT32)),
    ('format', FixedDataPacketField(MARKER_UINT32)),
))


class CreateGlyphSetRequest:
    OPCODE = 17

    __slots__ = ('gsid', 'format',)

    def __init__(
            self, *,
            gsid: Optional[int] = None,
            format: Optional[int] = None,
    ) -> None:
        self.gsid = gsid
        self.format = format

    def as_dict(self) -> Dict[str, Any]:
        return {
            'gsid': self.gsid,
            'format': self.format,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateGlyphSetRequest':
        return CreateGlyphSetRequest(**CreateGlyphSetRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateGlyphSetRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateGlyphSetRequest.lib = library.render_createglyphset
        CreateGlyphSetRequest.lib.restype = ctypes.c_uint32
        CreateGlyphSetRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class CreateGlyphSetRequestCType(ctypes.Structure):
    """render CreateGlyphSet"""
    _fields_ = [
        ("gsid", ctypes.c_uint32),
        ("format", ctypes.c_uint32),
    ]


ReferenceGlyphSetRequestPacket = DataPacket((
    ('gsid', FixedDataPacketField(MARKER_UINT32)),
    ('existing', FixedDataPacketField(MARKER_UINT32)),
))


class ReferenceGlyphSetRequest:
    OPCODE = 18

    __slots__ = ('gsid', 'existing',)

    def __init__(
            self, *,
            gsid: Optional[int] = None,
            existing: Optional[int] = None,
    ) -> None:
        self.gsid = gsid
        self.existing = existing

    def as_dict(self) -> Dict[str, Any]:
        return {
            'gsid': self.gsid,
            'existing': self.existing,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ReferenceGlyphSetRequest':
        return ReferenceGlyphSetRequest(**ReferenceGlyphSetRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ReferenceGlyphSetRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ReferenceGlyphSetRequest.lib = library.render_referenceglyphset
        ReferenceGlyphSetRequest.lib.restype = ctypes.c_uint32
        ReferenceGlyphSetRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class ReferenceGlyphSetRequestCType(ctypes.Structure):
    """render ReferenceGlyphSet"""
    _fields_ = [
        ("gsid", ctypes.c_uint32),
        ("existing", ctypes.c_uint32),
    ]


FreeGlyphSetRequestPacket = DataPacket((
    ('glyphset', FixedDataPacketField(MARKER_UINT32)),
))


class FreeGlyphSetRequest:
    OPCODE = 19

    __slots__ = ('glyphset',)

    def __init__(
            self, *,
            glyphset: Optional[int] = None,
    ) -> None:
        self.glyphset = glyphset

    def as_dict(self) -> Dict[str, Any]:
        return {
            'glyphset': self.glyphset,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'FreeGlyphSetRequest':
        return FreeGlyphSetRequest(**FreeGlyphSetRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return FreeGlyphSetRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        FreeGlyphSetRequest.lib = library.render_freeglyphset
        FreeGlyphSetRequest.lib.restype = ctypes.c_uint32
        FreeGlyphSetRequest.lib.argstype = (ctypes.c_uint32,)


class FreeGlyphSetRequestCType(ctypes.Structure):
    """render FreeGlyphSet"""
    _fields_ = [
        ("glyphset", ctypes.c_uint32),
    ]


AddGlyphsRequestPacket = DataPacket((
    ('glyphset', FixedDataPacketField(MARKER_UINT32)),
    ('glyphs_len', FixedDataPacketField(MARKER_UINT32)),
    ('glyphids', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['glyphs_len'], 0)),
    ('glyphs', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['glyphs_len'], 0)),
    ('data', SimpleListDataPacketField(MARKER_INT8, lambda d, c: 1, 0)),
))


class AddGlyphsRequest:
    OPCODE = 20

    __slots__ = ('glyphset', 'glyphs_len', 'glyphids', 'glyphs', 'data',)

    def __init__(
            self, *,
            glyphset: Optional[int] = None,
            glyphs_len: Optional[int] = None,
            glyphids: Optional[Sequence[int]] = None,
            glyphs: Optional[Sequence[int]] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.glyphset = glyphset
        self.glyphs_len = glyphs_len
        self.glyphids = glyphids
        self.glyphs = glyphs
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'glyphset': self.glyphset,
            'glyphs_len': self.glyphs_len,
            'glyphids': self.glyphids,
            'glyphs': self.glyphs,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'AddGlyphsRequest':
        return AddGlyphsRequest(**AddGlyphsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return AddGlyphsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int], Sequence[int], Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        AddGlyphsRequest.lib = library.render_addglyphs
        AddGlyphsRequest.lib.restype = ctypes.c_uint32
        AddGlyphsRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)


class AddGlyphsRequestCType(ctypes.Structure):
    """render AddGlyphs"""
    _fields_ = [
        ("glyphset", ctypes.c_uint32),
        ("glyphs_len", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


FreeGlyphsRequestPacket = DataPacket((
    ('glyphset', FixedDataPacketField(MARKER_UINT32)),
    ('glyphs', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 1, 0)),
))


class FreeGlyphsRequest:
    OPCODE = 22

    __slots__ = ('glyphset', 'glyphs',)

    def __init__(
            self, *,
            glyphset: Optional[int] = None,
            glyphs: Optional[Sequence[int]] = None,
    ) -> None:
        self.glyphset = glyphset
        self.glyphs = glyphs

    def as_dict(self) -> Dict[str, Any]:
        return {
            'glyphset': self.glyphset,
            'glyphs': self.glyphs,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'FreeGlyphsRequest':
        return FreeGlyphsRequest(**FreeGlyphsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return FreeGlyphsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        FreeGlyphsRequest.lib = library.render_freeglyphs
        FreeGlyphsRequest.lib.restype = ctypes.c_uint32
        FreeGlyphsRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_void_p)


class FreeGlyphsRequestCType(ctypes.Structure):
    """render FreeGlyphs"""
    _fields_ = [
        ("glyphset", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


CompositeGlyphs8RequestPacket = DataPacket((
    ('op', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
    ('src', FixedDataPacketField(MARKER_UINT32)),
    ('dst', FixedDataPacketField(MARKER_UINT32)),
    ('mask_format', FixedDataPacketField(MARKER_UINT32)),
    ('glyphset', FixedDataPacketField(MARKER_UINT32)),
    ('src_x', FixedDataPacketField(MARKER_INT16)),
    ('src_y', FixedDataPacketField(MARKER_INT16)),
    ('glyphcmds', SimpleListDataPacketField(MARKER_INT8, lambda d, c: 1, 0)),
))


class CompositeGlyphs8Request:
    OPCODE = 23

    __slots__ = ('op', 'src', 'dst', 'mask_format', 'glyphset', 'src_x', 'src_y', 'glyphcmds',)

    def __init__(
            self, *,
            op: Optional[int] = None,
            src: Optional[int] = None,
            dst: Optional[int] = None,
            mask_format: Optional[int] = None,
            glyphset: Optional[int] = None,
            src_x: Optional[int] = None,
            src_y: Optional[int] = None,
            glyphcmds: Optional[Sequence[int]] = None,
    ) -> None:
        self.op = op
        self.src = src
        self.dst = dst
        self.mask_format = mask_format
        self.glyphset = glyphset
        self.src_x = src_x
        self.src_y = src_y
        self.glyphcmds = glyphcmds

    def as_dict(self) -> Dict[str, Any]:
        return {
            'op': self.op,
            'src': self.src,
            'dst': self.dst,
            'mask_format': self.mask_format,
            'glyphset': self.glyphset,
            'src_x': self.src_x,
            'src_y': self.src_y,
            'glyphcmds': self.glyphcmds,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CompositeGlyphs8Request':
        return CompositeGlyphs8Request(**CompositeGlyphs8RequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CompositeGlyphs8RequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CompositeGlyphs8Request.lib = library.render_compositeglyphs8
        CompositeGlyphs8Request.lib.restype = ctypes.c_uint32
        CompositeGlyphs8Request.lib.argstype = (ctypes.c_uint8, ctypes.c_uint8 * 3, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16, ctypes.c_void_p)


class CompositeGlyphs8RequestCType(ctypes.Structure):
    """render CompositeGlyphs8"""
    _fields_ = [
        ("op", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
        ("src", ctypes.c_uint32),
        ("dst", ctypes.c_uint32),
        ("mask_format", ctypes.c_uint32),
        ("glyphset", ctypes.c_uint32),
        ("src_x", ctypes.c_int16),
        ("src_y", ctypes.c_int16),
        ("var_data", ctypes.c_void_p),
    ]


CompositeGlyphs16RequestPacket = DataPacket((
    ('op', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
    ('src', FixedDataPacketField(MARKER_UINT32)),
    ('dst', FixedDataPacketField(MARKER_UINT32)),
    ('mask_format', FixedDataPacketField(MARKER_UINT32)),
    ('glyphset', FixedDataPacketField(MARKER_UINT32)),
    ('src_x', FixedDataPacketField(MARKER_INT16)),
    ('src_y', FixedDataPacketField(MARKER_INT16)),
    ('glyphcmds', SimpleListDataPacketField(MARKER_INT8, lambda d, c: 1, 0)),
))


class CompositeGlyphs16Request:
    OPCODE = 24

    __slots__ = ('op', 'src', 'dst', 'mask_format', 'glyphset', 'src_x', 'src_y', 'glyphcmds',)

    def __init__(
            self, *,
            op: Optional[int] = None,
            src: Optional[int] = None,
            dst: Optional[int] = None,
            mask_format: Optional[int] = None,
            glyphset: Optional[int] = None,
            src_x: Optional[int] = None,
            src_y: Optional[int] = None,
            glyphcmds: Optional[Sequence[int]] = None,
    ) -> None:
        self.op = op
        self.src = src
        self.dst = dst
        self.mask_format = mask_format
        self.glyphset = glyphset
        self.src_x = src_x
        self.src_y = src_y
        self.glyphcmds = glyphcmds

    def as_dict(self) -> Dict[str, Any]:
        return {
            'op': self.op,
            'src': self.src,
            'dst': self.dst,
            'mask_format': self.mask_format,
            'glyphset': self.glyphset,
            'src_x': self.src_x,
            'src_y': self.src_y,
            'glyphcmds': self.glyphcmds,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CompositeGlyphs16Request':
        return CompositeGlyphs16Request(**CompositeGlyphs16RequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CompositeGlyphs16RequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CompositeGlyphs16Request.lib = library.render_compositeglyphs16
        CompositeGlyphs16Request.lib.restype = ctypes.c_uint32
        CompositeGlyphs16Request.lib.argstype = (ctypes.c_uint8, ctypes.c_uint8 * 3, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16, ctypes.c_void_p)


class CompositeGlyphs16RequestCType(ctypes.Structure):
    """render CompositeGlyphs16"""
    _fields_ = [
        ("op", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
        ("src", ctypes.c_uint32),
        ("dst", ctypes.c_uint32),
        ("mask_format", ctypes.c_uint32),
        ("glyphset", ctypes.c_uint32),
        ("src_x", ctypes.c_int16),
        ("src_y", ctypes.c_int16),
        ("var_data", ctypes.c_void_p),
    ]


CompositeGlyphs32RequestPacket = DataPacket((
    ('op', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
    ('src', FixedDataPacketField(MARKER_UINT32)),
    ('dst', FixedDataPacketField(MARKER_UINT32)),
    ('mask_format', FixedDataPacketField(MARKER_UINT32)),
    ('glyphset', FixedDataPacketField(MARKER_UINT32)),
    ('src_x', FixedDataPacketField(MARKER_INT16)),
    ('src_y', FixedDataPacketField(MARKER_INT16)),
    ('glyphcmds', SimpleListDataPacketField(MARKER_INT8, lambda d, c: 1, 0)),
))


class CompositeGlyphs32Request:
    OPCODE = 25

    __slots__ = ('op', 'src', 'dst', 'mask_format', 'glyphset', 'src_x', 'src_y', 'glyphcmds',)

    def __init__(
            self, *,
            op: Optional[int] = None,
            src: Optional[int] = None,
            dst: Optional[int] = None,
            mask_format: Optional[int] = None,
            glyphset: Optional[int] = None,
            src_x: Optional[int] = None,
            src_y: Optional[int] = None,
            glyphcmds: Optional[Sequence[int]] = None,
    ) -> None:
        self.op = op
        self.src = src
        self.dst = dst
        self.mask_format = mask_format
        self.glyphset = glyphset
        self.src_x = src_x
        self.src_y = src_y
        self.glyphcmds = glyphcmds

    def as_dict(self) -> Dict[str, Any]:
        return {
            'op': self.op,
            'src': self.src,
            'dst': self.dst,
            'mask_format': self.mask_format,
            'glyphset': self.glyphset,
            'src_x': self.src_x,
            'src_y': self.src_y,
            'glyphcmds': self.glyphcmds,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CompositeGlyphs32Request':
        return CompositeGlyphs32Request(**CompositeGlyphs32RequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CompositeGlyphs32RequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CompositeGlyphs32Request.lib = library.render_compositeglyphs32
        CompositeGlyphs32Request.lib.restype = ctypes.c_uint32
        CompositeGlyphs32Request.lib.argstype = (ctypes.c_uint8, ctypes.c_uint8 * 3, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16, ctypes.c_void_p)


class CompositeGlyphs32RequestCType(ctypes.Structure):
    """render CompositeGlyphs32"""
    _fields_ = [
        ("op", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
        ("src", ctypes.c_uint32),
        ("dst", ctypes.c_uint32),
        ("mask_format", ctypes.c_uint32),
        ("glyphset", ctypes.c_uint32),
        ("src_x", ctypes.c_int16),
        ("src_y", ctypes.c_int16),
        ("var_data", ctypes.c_void_p),
    ]


FillRectanglesRequestPacket = DataPacket((
    ('op', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
    ('dst', FixedDataPacketField(MARKER_UINT32)),
    ('color', FixedDataPacketField(MARKER_UINT32)),
    ('rects', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 1, 0)),
))


class FillRectanglesRequest:
    OPCODE = 26

    __slots__ = ('op', 'dst', 'color', 'rects',)

    def __init__(
            self, *,
            op: Optional[int] = None,
            dst: Optional[int] = None,
            color: Optional[int] = None,
            rects: Optional[Sequence[int]] = None,
    ) -> None:
        self.op = op
        self.dst = dst
        self.color = color
        self.rects = rects

    def as_dict(self) -> Dict[str, Any]:
        return {
            'op': self.op,
            'dst': self.dst,
            'color': self.color,
            'rects': self.rects,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'FillRectanglesRequest':
        return FillRectanglesRequest(**FillRectanglesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return FillRectanglesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        FillRectanglesRequest.lib = library.render_fillrectangles
        FillRectanglesRequest.lib.restype = ctypes.c_uint32
        FillRectanglesRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint8 * 3, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)


class FillRectanglesRequestCType(ctypes.Structure):
    """render FillRectangles"""
    _fields_ = [
        ("op", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
        ("dst", ctypes.c_uint32),
        ("color", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


CreateCursorRequestPacket = DataPacket((
    ('cid', FixedDataPacketField(MARKER_UINT32)),
    ('source', FixedDataPacketField(MARKER_UINT32)),
    ('x', FixedDataPacketField(MARKER_UINT16)),
    ('y', FixedDataPacketField(MARKER_UINT16)),
))


class CreateCursorRequest:
    OPCODE = 27

    __slots__ = ('cid', 'source', 'x', 'y',)

    def __init__(
            self, *,
            cid: Optional[int] = None,
            source: Optional[int] = None,
            x: Optional[int] = None,
            y: Optional[int] = None,
    ) -> None:
        self.cid = cid
        self.source = source
        self.x = x
        self.y = y

    def as_dict(self) -> Dict[str, Any]:
        return {
            'cid': self.cid,
            'source': self.source,
            'x': self.x,
            'y': self.y,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateCursorRequest':
        return CreateCursorRequest(**CreateCursorRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateCursorRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateCursorRequest.lib = library.render_createcursor
        CreateCursorRequest.lib.restype = ctypes.c_uint32
        CreateCursorRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16)


class CreateCursorRequestCType(ctypes.Structure):
    """render CreateCursor"""
    _fields_ = [
        ("cid", ctypes.c_uint32),
        ("source", ctypes.c_uint32),
        ("x", ctypes.c_uint16),
        ("y", ctypes.c_uint16),
    ]


TransformStructPacket = DataPacket((
    ('matrix11', FixedDataPacketField(MARKER_UINT32)),
    ('matrix12', FixedDataPacketField(MARKER_UINT32)),
    ('matrix13', FixedDataPacketField(MARKER_UINT32)),
    ('matrix21', FixedDataPacketField(MARKER_UINT32)),
    ('matrix22', FixedDataPacketField(MARKER_UINT32)),
    ('matrix23', FixedDataPacketField(MARKER_UINT32)),
    ('matrix31', FixedDataPacketField(MARKER_UINT32)),
    ('matrix32', FixedDataPacketField(MARKER_UINT32)),
    ('matrix33', FixedDataPacketField(MARKER_UINT32)),
))


class TransformStruct:
    __slots__ = ('matrix11', 'matrix12', 'matrix13', 'matrix21', 'matrix22', 'matrix23', 'matrix31', 'matrix32', 'matrix33',)

    def __init__(
            self, *,
            matrix11: Optional[int] = None,
            matrix12: Optional[int] = None,
            matrix13: Optional[int] = None,
            matrix21: Optional[int] = None,
            matrix22: Optional[int] = None,
            matrix23: Optional[int] = None,
            matrix31: Optional[int] = None,
            matrix32: Optional[int] = None,
            matrix33: Optional[int] = None,
    ) -> None:
        self.matrix11 = matrix11
        self.matrix12 = matrix12
        self.matrix13 = matrix13
        self.matrix21 = matrix21
        self.matrix22 = matrix22
        self.matrix23 = matrix23
        self.matrix31 = matrix31
        self.matrix32 = matrix32
        self.matrix33 = matrix33

    def as_dict(self) -> Dict[str, Any]:
        return {
            'matrix11': self.matrix11,
            'matrix12': self.matrix12,
            'matrix13': self.matrix13,
            'matrix21': self.matrix21,
            'matrix22': self.matrix22,
            'matrix23': self.matrix23,
            'matrix31': self.matrix31,
            'matrix32': self.matrix32,
            'matrix33': self.matrix33,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'TransformStruct':
        return TransformStruct(**TransformStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return TransformStructPacket.pack(**self.as_dict())


class TransformStructCType(ctypes.Structure):
    """render TRANSFORM"""
    _fields_ = [
        ("matrix11", ctypes.c_uint32),
        ("matrix12", ctypes.c_uint32),
        ("matrix13", ctypes.c_uint32),
        ("matrix21", ctypes.c_uint32),
        ("matrix22", ctypes.c_uint32),
        ("matrix23", ctypes.c_uint32),
        ("matrix31", ctypes.c_uint32),
        ("matrix32", ctypes.c_uint32),
        ("matrix33", ctypes.c_uint32),
    ]


SetPictureTransformRequestPacket = DataPacket((
    ('picture', FixedDataPacketField(MARKER_UINT32)),
    ('transform', FixedDataPacketField(MARKER_UINT32)),
))


class SetPictureTransformRequest:
    OPCODE = 28

    __slots__ = ('picture', 'transform',)

    def __init__(
            self, *,
            picture: Optional[int] = None,
            transform: Optional[int] = None,
    ) -> None:
        self.picture = picture
        self.transform = transform

    def as_dict(self) -> Dict[str, Any]:
        return {
            'picture': self.picture,
            'transform': self.transform,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetPictureTransformRequest':
        return SetPictureTransformRequest(**SetPictureTransformRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetPictureTransformRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetPictureTransformRequest.lib = library.render_setpicturetransform
        SetPictureTransformRequest.lib.restype = ctypes.c_uint32
        SetPictureTransformRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class SetPictureTransformRequestCType(ctypes.Structure):
    """render SetPictureTransform"""
    _fields_ = [
        ("picture", ctypes.c_uint32),
        ("transform", ctypes.c_uint32),
    ]


QueryFiltersRequestCookie = NewType('QueryFiltersRequestCookie', ctypes.c_uint32)


QueryFiltersRequestPacket = DataPacket((
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
))


class QueryFiltersRequest:
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
    def from_data(inp: BinaryIO) -> 'QueryFiltersRequest':
        return QueryFiltersRequest(**QueryFiltersRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryFiltersRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], QueryFiltersRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryFiltersRequest.lib = library.render_queryfilters
        QueryFiltersRequest.lib.restype = QueryFiltersRequestCookie
        QueryFiltersRequest.lib.argstype = (ctypes.c_uint32,)


class QueryFiltersRequestCType(ctypes.Structure):
    """render QueryFilters"""
    _fields_ = [
        ("drawable", ctypes.c_uint32),
    ]


QueryFiltersReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('num_aliases', FixedDataPacketField(MARKER_UINT32)),
    ('num_filters', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(16)),
    ('aliases', SimpleListDataPacketField(MARKER_UINT16, lambda d, c: d['num_aliases'], 0)),
    ('filters', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_filters'], 0)),
))


class QueryFiltersReplyReply:
    __slots__ = ('num_aliases', 'num_filters', 'aliases', 'filters',)

    def __init__(
            self, *,
            num_aliases: Optional[int] = None,
            num_filters: Optional[int] = None,
            aliases: Optional[Sequence[int]] = None,
            filters: Optional[Sequence[int]] = None,
    ) -> None:
        self.num_aliases = num_aliases
        self.num_filters = num_filters
        self.aliases = aliases
        self.filters = filters

    def as_dict(self) -> Dict[str, Any]:
        return {
            'num_aliases': self.num_aliases,
            'num_filters': self.num_filters,
            'aliases': self.aliases,
            'filters': self.filters,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryFiltersReplyReply':
        return QueryFiltersReplyReply(**QueryFiltersReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryFiltersReplyReplyPacket.pack(**self.as_dict())


class QueryFiltersReplyReplyCType(ctypes.Structure):
    """render QueryFilters_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("num_aliases", ctypes.c_uint32),
        ("num_filters", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 16),
        ("var_data", ctypes.c_void_p),
    ]


SetPictureFilterRequestPacket = DataPacket((
    ('picture', FixedDataPacketField(MARKER_UINT32)),
    ('filter_len', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
    ('filter', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['filter_len'], 0)),
    ('pad1', AlignedPadDataPacketField(4)),
    ('values', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 1, 0)),
))


class SetPictureFilterRequest:
    OPCODE = 30

    __slots__ = ('picture', 'filter_len', 'filter', 'values',)

    def __init__(
            self, *,
            picture: Optional[int] = None,
            filter_len: Optional[int] = None,
            filter: Optional[Sequence[int]] = None,
            values: Optional[Sequence[int]] = None,
    ) -> None:
        self.picture = picture
        self.filter_len = filter_len
        self.filter = filter
        self.values = values

    def as_dict(self) -> Dict[str, Any]:
        return {
            'picture': self.picture,
            'filter_len': self.filter_len,
            'filter': self.filter,
            'values': self.values,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetPictureFilterRequest':
        return SetPictureFilterRequest(**SetPictureFilterRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetPictureFilterRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int], Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetPictureFilterRequest.lib = library.render_setpicturefilter
        SetPictureFilterRequest.lib.restype = ctypes.c_uint32
        SetPictureFilterRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint8 * 2, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)


class SetPictureFilterRequestCType(ctypes.Structure):
    """render SetPictureFilter"""
    _fields_ = [
        ("picture", ctypes.c_uint32),
        ("filter_len", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


AnimcursoreltStructPacket = DataPacket((
    ('cursor', FixedDataPacketField(MARKER_UINT32)),
    ('delay', FixedDataPacketField(MARKER_UINT32)),
))


class AnimcursoreltStruct:
    __slots__ = ('cursor', 'delay',)

    def __init__(
            self, *,
            cursor: Optional[int] = None,
            delay: Optional[int] = None,
    ) -> None:
        self.cursor = cursor
        self.delay = delay

    def as_dict(self) -> Dict[str, Any]:
        return {
            'cursor': self.cursor,
            'delay': self.delay,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'AnimcursoreltStruct':
        return AnimcursoreltStruct(**AnimcursoreltStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return AnimcursoreltStructPacket.pack(**self.as_dict())


class AnimcursoreltStructCType(ctypes.Structure):
    """render ANIMCURSORELT"""
    _fields_ = [
        ("cursor", ctypes.c_uint32),
        ("delay", ctypes.c_uint32),
    ]


CreateAnimCursorRequestPacket = DataPacket((
    ('cid', FixedDataPacketField(MARKER_UINT32)),
    ('cursors', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 1, 0)),
))


class CreateAnimCursorRequest:
    OPCODE = 31

    __slots__ = ('cid', 'cursors',)

    def __init__(
            self, *,
            cid: Optional[int] = None,
            cursors: Optional[Sequence[int]] = None,
    ) -> None:
        self.cid = cid
        self.cursors = cursors

    def as_dict(self) -> Dict[str, Any]:
        return {
            'cid': self.cid,
            'cursors': self.cursors,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateAnimCursorRequest':
        return CreateAnimCursorRequest(**CreateAnimCursorRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateAnimCursorRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateAnimCursorRequest.lib = library.render_createanimcursor
        CreateAnimCursorRequest.lib.restype = ctypes.c_uint32
        CreateAnimCursorRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_void_p)


class CreateAnimCursorRequestCType(ctypes.Structure):
    """render CreateAnimCursor"""
    _fields_ = [
        ("cid", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


SpanfixStructPacket = DataPacket((
    ('l', FixedDataPacketField(MARKER_UINT32)),
    ('r', FixedDataPacketField(MARKER_UINT32)),
    ('y', FixedDataPacketField(MARKER_UINT32)),
))


class SpanfixStruct:
    __slots__ = ('l', 'r', 'y',)

    def __init__(
            self, *,
            l: Optional[int] = None,
            r: Optional[int] = None,
            y: Optional[int] = None,
    ) -> None:
        self.l = l
        self.r = r
        self.y = y

    def as_dict(self) -> Dict[str, Any]:
        return {
            'l': self.l,
            'r': self.r,
            'y': self.y,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SpanfixStruct':
        return SpanfixStruct(**SpanfixStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SpanfixStructPacket.pack(**self.as_dict())


class SpanfixStructCType(ctypes.Structure):
    """render SPANFIX"""
    _fields_ = [
        ("l", ctypes.c_uint32),
        ("r", ctypes.c_uint32),
        ("y", ctypes.c_uint32),
    ]


TrapStructPacket = DataPacket((
    ('top', FixedDataPacketField(MARKER_UINT32)),
    ('bot', FixedDataPacketField(MARKER_UINT32)),
))


class TrapStruct:
    __slots__ = ('top', 'bot',)

    def __init__(
            self, *,
            top: Optional[int] = None,
            bot: Optional[int] = None,
    ) -> None:
        self.top = top
        self.bot = bot

    def as_dict(self) -> Dict[str, Any]:
        return {
            'top': self.top,
            'bot': self.bot,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'TrapStruct':
        return TrapStruct(**TrapStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return TrapStructPacket.pack(**self.as_dict())


class TrapStructCType(ctypes.Structure):
    """render TRAP"""
    _fields_ = [
        ("top", ctypes.c_uint32),
        ("bot", ctypes.c_uint32),
    ]


AddTrapsRequestPacket = DataPacket((
    ('picture', FixedDataPacketField(MARKER_UINT32)),
    ('x_off', FixedDataPacketField(MARKER_INT16)),
    ('y_off', FixedDataPacketField(MARKER_INT16)),
    ('traps', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 1, 0)),
))


class AddTrapsRequest:
    OPCODE = 32

    __slots__ = ('picture', 'x_off', 'y_off', 'traps',)

    def __init__(
            self, *,
            picture: Optional[int] = None,
            x_off: Optional[int] = None,
            y_off: Optional[int] = None,
            traps: Optional[Sequence[int]] = None,
    ) -> None:
        self.picture = picture
        self.x_off = x_off
        self.y_off = y_off
        self.traps = traps

    def as_dict(self) -> Dict[str, Any]:
        return {
            'picture': self.picture,
            'x_off': self.x_off,
            'y_off': self.y_off,
            'traps': self.traps,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'AddTrapsRequest':
        return AddTrapsRequest(**AddTrapsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return AddTrapsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        AddTrapsRequest.lib = library.render_addtraps
        AddTrapsRequest.lib.restype = ctypes.c_uint32
        AddTrapsRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16, ctypes.c_void_p)


class AddTrapsRequestCType(ctypes.Structure):
    """render AddTraps"""
    _fields_ = [
        ("picture", ctypes.c_uint32),
        ("x_off", ctypes.c_int16),
        ("y_off", ctypes.c_int16),
        ("var_data", ctypes.c_void_p),
    ]


CreateSolidFillRequestPacket = DataPacket((
    ('picture', FixedDataPacketField(MARKER_UINT32)),
    ('color', FixedDataPacketField(MARKER_UINT32)),
))


class CreateSolidFillRequest:
    OPCODE = 33

    __slots__ = ('picture', 'color',)

    def __init__(
            self, *,
            picture: Optional[int] = None,
            color: Optional[int] = None,
    ) -> None:
        self.picture = picture
        self.color = color

    def as_dict(self) -> Dict[str, Any]:
        return {
            'picture': self.picture,
            'color': self.color,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateSolidFillRequest':
        return CreateSolidFillRequest(**CreateSolidFillRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateSolidFillRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateSolidFillRequest.lib = library.render_createsolidfill
        CreateSolidFillRequest.lib.restype = ctypes.c_uint32
        CreateSolidFillRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class CreateSolidFillRequestCType(ctypes.Structure):
    """render CreateSolidFill"""
    _fields_ = [
        ("picture", ctypes.c_uint32),
        ("color", ctypes.c_uint32),
    ]


CreateLinearGradientRequestPacket = DataPacket((
    ('picture', FixedDataPacketField(MARKER_UINT32)),
    ('p1', FixedDataPacketField(MARKER_UINT32)),
    ('p2', FixedDataPacketField(MARKER_UINT32)),
    ('num_stops', FixedDataPacketField(MARKER_UINT32)),
    ('stops', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_stops'], 0)),
    ('colors', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_stops'], 0)),
))


class CreateLinearGradientRequest:
    OPCODE = 34

    __slots__ = ('picture', 'p1', 'p2', 'num_stops', 'stops', 'colors',)

    def __init__(
            self, *,
            picture: Optional[int] = None,
            p1: Optional[int] = None,
            p2: Optional[int] = None,
            num_stops: Optional[int] = None,
            stops: Optional[Sequence[int]] = None,
            colors: Optional[Sequence[int]] = None,
    ) -> None:
        self.picture = picture
        self.p1 = p1
        self.p2 = p2
        self.num_stops = num_stops
        self.stops = stops
        self.colors = colors

    def as_dict(self) -> Dict[str, Any]:
        return {
            'picture': self.picture,
            'p1': self.p1,
            'p2': self.p2,
            'num_stops': self.num_stops,
            'stops': self.stops,
            'colors': self.colors,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateLinearGradientRequest':
        return CreateLinearGradientRequest(**CreateLinearGradientRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateLinearGradientRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, Sequence[int], Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateLinearGradientRequest.lib = library.render_createlineargradient
        CreateLinearGradientRequest.lib.restype = ctypes.c_uint32
        CreateLinearGradientRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_void_p)


class CreateLinearGradientRequestCType(ctypes.Structure):
    """render CreateLinearGradient"""
    _fields_ = [
        ("picture", ctypes.c_uint32),
        ("p1", ctypes.c_uint32),
        ("p2", ctypes.c_uint32),
        ("num_stops", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


CreateRadialGradientRequestPacket = DataPacket((
    ('picture', FixedDataPacketField(MARKER_UINT32)),
    ('inner', FixedDataPacketField(MARKER_UINT32)),
    ('outer', FixedDataPacketField(MARKER_UINT32)),
    ('inner_radius', FixedDataPacketField(MARKER_UINT32)),
    ('outer_radius', FixedDataPacketField(MARKER_UINT32)),
    ('num_stops', FixedDataPacketField(MARKER_UINT32)),
    ('stops', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_stops'], 0)),
    ('colors', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_stops'], 0)),
))


class CreateRadialGradientRequest:
    OPCODE = 35

    __slots__ = ('picture', 'inner', 'outer', 'inner_radius', 'outer_radius', 'num_stops', 'stops', 'colors',)

    def __init__(
            self, *,
            picture: Optional[int] = None,
            inner: Optional[int] = None,
            outer: Optional[int] = None,
            inner_radius: Optional[int] = None,
            outer_radius: Optional[int] = None,
            num_stops: Optional[int] = None,
            stops: Optional[Sequence[int]] = None,
            colors: Optional[Sequence[int]] = None,
    ) -> None:
        self.picture = picture
        self.inner = inner
        self.outer = outer
        self.inner_radius = inner_radius
        self.outer_radius = outer_radius
        self.num_stops = num_stops
        self.stops = stops
        self.colors = colors

    def as_dict(self) -> Dict[str, Any]:
        return {
            'picture': self.picture,
            'inner': self.inner,
            'outer': self.outer,
            'inner_radius': self.inner_radius,
            'outer_radius': self.outer_radius,
            'num_stops': self.num_stops,
            'stops': self.stops,
            'colors': self.colors,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateRadialGradientRequest':
        return CreateRadialGradientRequest(**CreateRadialGradientRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateRadialGradientRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, Sequence[int], Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateRadialGradientRequest.lib = library.render_createradialgradient
        CreateRadialGradientRequest.lib.restype = ctypes.c_uint32
        CreateRadialGradientRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_void_p)


class CreateRadialGradientRequestCType(ctypes.Structure):
    """render CreateRadialGradient"""
    _fields_ = [
        ("picture", ctypes.c_uint32),
        ("inner", ctypes.c_uint32),
        ("outer", ctypes.c_uint32),
        ("inner_radius", ctypes.c_uint32),
        ("outer_radius", ctypes.c_uint32),
        ("num_stops", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


CreateConicalGradientRequestPacket = DataPacket((
    ('picture', FixedDataPacketField(MARKER_UINT32)),
    ('center', FixedDataPacketField(MARKER_UINT32)),
    ('angle', FixedDataPacketField(MARKER_UINT32)),
    ('num_stops', FixedDataPacketField(MARKER_UINT32)),
    ('stops', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_stops'], 0)),
    ('colors', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_stops'], 0)),
))


class CreateConicalGradientRequest:
    OPCODE = 36

    __slots__ = ('picture', 'center', 'angle', 'num_stops', 'stops', 'colors',)

    def __init__(
            self, *,
            picture: Optional[int] = None,
            center: Optional[int] = None,
            angle: Optional[int] = None,
            num_stops: Optional[int] = None,
            stops: Optional[Sequence[int]] = None,
            colors: Optional[Sequence[int]] = None,
    ) -> None:
        self.picture = picture
        self.center = center
        self.angle = angle
        self.num_stops = num_stops
        self.stops = stops
        self.colors = colors

    def as_dict(self) -> Dict[str, Any]:
        return {
            'picture': self.picture,
            'center': self.center,
            'angle': self.angle,
            'num_stops': self.num_stops,
            'stops': self.stops,
            'colors': self.colors,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateConicalGradientRequest':
        return CreateConicalGradientRequest(**CreateConicalGradientRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateConicalGradientRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, Sequence[int], Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateConicalGradientRequest.lib = library.render_createconicalgradient
        CreateConicalGradientRequest.lib.restype = ctypes.c_uint32
        CreateConicalGradientRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_void_p)


class CreateConicalGradientRequestCType(ctypes.Structure):
    """render CreateConicalGradient"""
    _fields_ = [
        ("picture", ctypes.c_uint32),
        ("center", ctypes.c_uint32),
        ("angle", ctypes.c_uint32),
        ("num_stops", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


# ------------------------------------------------------------------
# Unions

