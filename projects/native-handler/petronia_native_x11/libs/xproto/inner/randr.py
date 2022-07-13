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

RotationType = NewType('RotationType', int)


class RotationValues:
    ROTATE_0 = RotationType(1)
    ROTATE_90 = RotationType(2)
    ROTATE_180 = RotationType(4)
    ROTATE_270 = RotationType(8)
    REFLECT_X = RotationType(16)
    REFLECT_Y = RotationType(32)


SetConfigType = NewType('SetConfigType', int)


class SetConfigValues:
    SUCCESS = SetConfigType(0)
    INVALID_CONFIG_TIME = SetConfigType(1)
    INVALID_TIME = SetConfigType(2)
    FAILED = SetConfigType(3)


NotifyMaskType = NewType('NotifyMaskType', int)


class NotifyMaskValues:
    SCREEN_CHANGE = NotifyMaskType(1)
    CRTC_CHANGE = NotifyMaskType(2)
    OUTPUT_CHANGE = NotifyMaskType(4)
    OUTPUT_PROPERTY = NotifyMaskType(8)
    PROVIDER_CHANGE = NotifyMaskType(16)
    PROVIDER_PROPERTY = NotifyMaskType(32)
    RESOURCE_CHANGE = NotifyMaskType(64)
    LEASE = NotifyMaskType(128)


ModeFlagType = NewType('ModeFlagType', int)


class ModeFlagValues:
    HSYNC_POSITIVE = ModeFlagType(1)
    HSYNC_NEGATIVE = ModeFlagType(2)
    VSYNC_POSITIVE = ModeFlagType(4)
    VSYNC_NEGATIVE = ModeFlagType(8)
    INTERLACE = ModeFlagType(16)
    DOUBLE_SCAN = ModeFlagType(32)
    CSYNC = ModeFlagType(64)
    CSYNC_POSITIVE = ModeFlagType(128)
    CSYNC_NEGATIVE = ModeFlagType(256)
    HSKEW_PRESENT = ModeFlagType(512)
    BCAST = ModeFlagType(1024)
    PIXEL_MULTIPLEX = ModeFlagType(2048)
    DOUBLE_CLOCK = ModeFlagType(4096)
    HALVE_CLOCK = ModeFlagType(8192)


ConnectionType = NewType('ConnectionType', int)


class ConnectionValues:
    CONNECTED = ConnectionType(0)
    DISCONNECTED = ConnectionType(1)
    UNKNOWN = ConnectionType(2)


TransformType = NewType('TransformType', int)


class TransformValues:
    UNIT = TransformType(1)
    SCALE_UP = TransformType(2)
    SCALE_DOWN = TransformType(4)
    PROJECTIVE = TransformType(8)


ProviderCapabilityType = NewType('ProviderCapabilityType', int)


class ProviderCapabilityValues:
    SOURCE_OUTPUT = ProviderCapabilityType(1)
    SINK_OUTPUT = ProviderCapabilityType(2)
    SOURCE_OFFLOAD = ProviderCapabilityType(4)
    SINK_OFFLOAD = ProviderCapabilityType(8)


NotifyType = NewType('NotifyType', int)


class NotifyValues:
    CRTC_CHANGE = NotifyType(0)
    OUTPUT_CHANGE = NotifyType(1)
    OUTPUT_PROPERTY = NotifyType(2)
    PROVIDER_CHANGE = NotifyType(3)
    PROVIDER_PROPERTY = NotifyType(4)
    RESOURCE_CHANGE = NotifyType(5)
    LEASE = NotifyType(6)


# ------------------------------------------------------------------
# Aliases

Output = NewType('Output', ctypes.c_uint32)
Provider = NewType('Provider', ctypes.c_uint32)
Crtc = NewType('Crtc', ctypes.c_uint32)
Lease = NewType('Lease', ctypes.c_uint32)
Mode = NewType('Mode', ctypes.c_uint32)


# ------------------------------------------------------------------
# Structures, Events, Requests, Replies


ScreenSizeStructPacket = DataPacket((
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('mwidth', FixedDataPacketField(MARKER_UINT16)),
    ('mheight', FixedDataPacketField(MARKER_UINT16)),
))


class ScreenSizeStruct:
    __slots__ = ('width', 'height', 'mwidth', 'mheight',)

    def __init__(
            self, *,
            width: Optional[int] = None,
            height: Optional[int] = None,
            mwidth: Optional[int] = None,
            mheight: Optional[int] = None,
    ) -> None:
        self.width = width
        self.height = height
        self.mwidth = mwidth
        self.mheight = mheight

    def as_dict(self) -> Dict[str, Any]:
        return {
            'width': self.width,
            'height': self.height,
            'mwidth': self.mwidth,
            'mheight': self.mheight,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ScreenSizeStruct':
        return ScreenSizeStruct(**ScreenSizeStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ScreenSizeStructPacket.pack(**self.as_dict())


class ScreenSizeStructCType(ctypes.Structure):
    """randr ScreenSize"""
    _fields_ = [
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("mwidth", ctypes.c_uint16),
        ("mheight", ctypes.c_uint16),
    ]


RefreshRatesStructPacket = DataPacket((
    ('nRates', FixedDataPacketField(MARKER_UINT16)),
    ('rates', SimpleListDataPacketField(MARKER_UINT16, lambda d, c: d['nRates'], 0)),
))


class RefreshRatesStruct:
    __slots__ = ('nrates', 'rates',)

    def __init__(
            self, *,
            nrates: Optional[int] = None,
            rates: Optional[Sequence[int]] = None,
    ) -> None:
        self.nrates = nrates
        self.rates = rates

    def as_dict(self) -> Dict[str, Any]:
        return {
            'nRates': self.nrates,
            'rates': self.rates,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'RefreshRatesStruct':
        return RefreshRatesStruct(**RefreshRatesStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return RefreshRatesStructPacket.pack(**self.as_dict())


class RefreshRatesStructCType(ctypes.Structure):
    """randr RefreshRates"""
    _fields_ = [
        ("nRates", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
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
        QueryVersionRequest.lib = library.randr_queryversion
        QueryVersionRequest.lib.restype = QueryVersionRequestCookie
        QueryVersionRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class QueryVersionRequestCType(ctypes.Structure):
    """randr QueryVersion"""
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
    """randr QueryVersion_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("major_version", ctypes.c_uint32),
        ("minor_version", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 16),
    ]


SetScreenConfigRequestCookie = NewType('SetScreenConfigRequestCookie', ctypes.c_uint32)


SetScreenConfigRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('config_timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('sizeID', FixedDataPacketField(MARKER_UINT16)),
    ('rotation', FixedDataPacketField(MARKER_UINT16)),
    ('rate', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
))


class SetScreenConfigRequest:
    OPCODE = 2

    __slots__ = ('window', 'timestamp', 'config_timestamp', 'sizeid', 'rotation', 'rate',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            timestamp: Optional[int] = None,
            config_timestamp: Optional[int] = None,
            sizeid: Optional[int] = None,
            rotation: Optional[int] = None,
            rate: Optional[int] = None,
    ) -> None:
        self.window = window
        self.timestamp = timestamp
        self.config_timestamp = config_timestamp
        self.sizeid = sizeid
        self.rotation = rotation
        self.rate = rate

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'timestamp': self.timestamp,
            'config_timestamp': self.config_timestamp,
            'sizeID': self.sizeid,
            'rotation': self.rotation,
            'rate': self.rate,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetScreenConfigRequest':
        return SetScreenConfigRequest(**SetScreenConfigRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetScreenConfigRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int], SetScreenConfigRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetScreenConfigRequest.lib = library.randr_setscreenconfig
        SetScreenConfigRequest.lib.restype = SetScreenConfigRequestCookie
        SetScreenConfigRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint8 * 2)


class SetScreenConfigRequestCType(ctypes.Structure):
    """randr SetScreenConfig"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint32),
        ("config_timestamp", ctypes.c_uint32),
        ("sizeID", ctypes.c_uint16),
        ("rotation", ctypes.c_uint16),
        ("rate", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
    ]


SetScreenConfigReplyReplyPacket = DataPacket((
    ('status', FixedDataPacketField(MARKER_UINT8)),
    ('new_timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('config_timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('root', FixedDataPacketField(MARKER_UINT32)),
    ('subpixel_order', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(10)),
))


class SetScreenConfigReplyReply:
    __slots__ = ('status', 'new_timestamp', 'config_timestamp', 'root', 'subpixel_order',)

    def __init__(
            self, *,
            status: Optional[int] = None,
            new_timestamp: Optional[int] = None,
            config_timestamp: Optional[int] = None,
            root: Optional[int] = None,
            subpixel_order: Optional[int] = None,
    ) -> None:
        self.status = status
        self.new_timestamp = new_timestamp
        self.config_timestamp = config_timestamp
        self.root = root
        self.subpixel_order = subpixel_order

    def as_dict(self) -> Dict[str, Any]:
        return {
            'status': self.status,
            'new_timestamp': self.new_timestamp,
            'config_timestamp': self.config_timestamp,
            'root': self.root,
            'subpixel_order': self.subpixel_order,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetScreenConfigReplyReply':
        return SetScreenConfigReplyReply(**SetScreenConfigReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetScreenConfigReplyReplyPacket.pack(**self.as_dict())


class SetScreenConfigReplyReplyCType(ctypes.Structure):
    """randr SetScreenConfig_reply"""
    _fields_ = [
        ("status", ctypes.c_uint8),
        ("new_timestamp", ctypes.c_uint32),
        ("config_timestamp", ctypes.c_uint32),
        ("root", ctypes.c_uint32),
        ("subpixel_order", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 10),
    ]


SelectInputRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('enable', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
))


class SelectInputRequest:
    OPCODE = 4

    __slots__ = ('window', 'enable',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            enable: Optional[int] = None,
    ) -> None:
        self.window = window
        self.enable = enable

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'enable': self.enable,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SelectInputRequest':
        return SelectInputRequest(**SelectInputRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SelectInputRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SelectInputRequest.lib = library.randr_selectinput
        SelectInputRequest.lib.restype = ctypes.c_uint32
        SelectInputRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint8 * 2)


class SelectInputRequestCType(ctypes.Structure):
    """randr SelectInput"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("enable", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
    ]


GetScreenInfoRequestCookie = NewType('GetScreenInfoRequestCookie', ctypes.c_uint32)


GetScreenInfoRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class GetScreenInfoRequest:
    OPCODE = 5

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
    def from_data(inp: BinaryIO) -> 'GetScreenInfoRequest':
        return GetScreenInfoRequest(**GetScreenInfoRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetScreenInfoRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetScreenInfoRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetScreenInfoRequest.lib = library.randr_getscreeninfo
        GetScreenInfoRequest.lib.restype = GetScreenInfoRequestCookie
        GetScreenInfoRequest.lib.argstype = (ctypes.c_uint32,)


class GetScreenInfoRequestCType(ctypes.Structure):
    """randr GetScreenInfo"""
    _fields_ = [
        ("window", ctypes.c_uint32),
    ]


GetScreenInfoReplyReplyPacket = DataPacket((
    ('rotations', FixedDataPacketField(MARKER_UINT8)),
    ('root', FixedDataPacketField(MARKER_UINT32)),
    ('timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('config_timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('nSizes', FixedDataPacketField(MARKER_UINT16)),
    ('sizeID', FixedDataPacketField(MARKER_UINT16)),
    ('rotation', FixedDataPacketField(MARKER_UINT16)),
    ('rate', FixedDataPacketField(MARKER_UINT16)),
    ('nInfo', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
    ('sizes', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nSizes'], 0)),
    ('rates', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: (d['nInfo']) - (d['nSizes']), 0)),
))


class GetScreenInfoReplyReply:
    __slots__ = ('rotations', 'root', 'timestamp', 'config_timestamp', 'nsizes', 'sizeid', 'rotation', 'rate', 'ninfo', 'sizes', 'rates',)

    def __init__(
            self, *,
            rotations: Optional[int] = None,
            root: Optional[int] = None,
            timestamp: Optional[int] = None,
            config_timestamp: Optional[int] = None,
            nsizes: Optional[int] = None,
            sizeid: Optional[int] = None,
            rotation: Optional[int] = None,
            rate: Optional[int] = None,
            ninfo: Optional[int] = None,
            sizes: Optional[Sequence[int]] = None,
            rates: Optional[Sequence[int]] = None,
    ) -> None:
        self.rotations = rotations
        self.root = root
        self.timestamp = timestamp
        self.config_timestamp = config_timestamp
        self.nsizes = nsizes
        self.sizeid = sizeid
        self.rotation = rotation
        self.rate = rate
        self.ninfo = ninfo
        self.sizes = sizes
        self.rates = rates

    def as_dict(self) -> Dict[str, Any]:
        return {
            'rotations': self.rotations,
            'root': self.root,
            'timestamp': self.timestamp,
            'config_timestamp': self.config_timestamp,
            'nSizes': self.nsizes,
            'sizeID': self.sizeid,
            'rotation': self.rotation,
            'rate': self.rate,
            'nInfo': self.ninfo,
            'sizes': self.sizes,
            'rates': self.rates,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetScreenInfoReplyReply':
        return GetScreenInfoReplyReply(**GetScreenInfoReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetScreenInfoReplyReplyPacket.pack(**self.as_dict())


class GetScreenInfoReplyReplyCType(ctypes.Structure):
    """randr GetScreenInfo_reply"""
    _fields_ = [
        ("rotations", ctypes.c_uint8),
        ("root", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint32),
        ("config_timestamp", ctypes.c_uint32),
        ("nSizes", ctypes.c_uint16),
        ("sizeID", ctypes.c_uint16),
        ("rotation", ctypes.c_uint16),
        ("rate", ctypes.c_uint16),
        ("nInfo", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


GetScreenSizeRangeRequestCookie = NewType('GetScreenSizeRangeRequestCookie', ctypes.c_uint32)


GetScreenSizeRangeRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class GetScreenSizeRangeRequest:
    OPCODE = 6

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
    def from_data(inp: BinaryIO) -> 'GetScreenSizeRangeRequest':
        return GetScreenSizeRangeRequest(**GetScreenSizeRangeRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetScreenSizeRangeRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetScreenSizeRangeRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetScreenSizeRangeRequest.lib = library.randr_getscreensizerange
        GetScreenSizeRangeRequest.lib.restype = GetScreenSizeRangeRequestCookie
        GetScreenSizeRangeRequest.lib.argstype = (ctypes.c_uint32,)


class GetScreenSizeRangeRequestCType(ctypes.Structure):
    """randr GetScreenSizeRange"""
    _fields_ = [
        ("window", ctypes.c_uint32),
    ]


GetScreenSizeRangeReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('min_width', FixedDataPacketField(MARKER_UINT16)),
    ('min_height', FixedDataPacketField(MARKER_UINT16)),
    ('max_width', FixedDataPacketField(MARKER_UINT16)),
    ('max_height', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(16)),
))


class GetScreenSizeRangeReplyReply:
    __slots__ = ('min_width', 'min_height', 'max_width', 'max_height',)

    def __init__(
            self, *,
            min_width: Optional[int] = None,
            min_height: Optional[int] = None,
            max_width: Optional[int] = None,
            max_height: Optional[int] = None,
    ) -> None:
        self.min_width = min_width
        self.min_height = min_height
        self.max_width = max_width
        self.max_height = max_height

    def as_dict(self) -> Dict[str, Any]:
        return {
            'min_width': self.min_width,
            'min_height': self.min_height,
            'max_width': self.max_width,
            'max_height': self.max_height,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetScreenSizeRangeReplyReply':
        return GetScreenSizeRangeReplyReply(**GetScreenSizeRangeReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetScreenSizeRangeReplyReplyPacket.pack(**self.as_dict())


class GetScreenSizeRangeReplyReplyCType(ctypes.Structure):
    """randr GetScreenSizeRange_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("min_width", ctypes.c_uint16),
        ("min_height", ctypes.c_uint16),
        ("max_width", ctypes.c_uint16),
        ("max_height", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 16),
    ]


SetScreenSizeRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('mm_width', FixedDataPacketField(MARKER_UINT32)),
    ('mm_height', FixedDataPacketField(MARKER_UINT32)),
))


class SetScreenSizeRequest:
    OPCODE = 7

    __slots__ = ('window', 'width', 'height', 'mm_width', 'mm_height',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            mm_width: Optional[int] = None,
            mm_height: Optional[int] = None,
    ) -> None:
        self.window = window
        self.width = width
        self.height = height
        self.mm_width = mm_width
        self.mm_height = mm_height

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'width': self.width,
            'height': self.height,
            'mm_width': self.mm_width,
            'mm_height': self.mm_height,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetScreenSizeRequest':
        return SetScreenSizeRequest(**SetScreenSizeRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetScreenSizeRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetScreenSizeRequest.lib = library.randr_setscreensize
        SetScreenSizeRequest.lib.restype = ctypes.c_uint32
        SetScreenSizeRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint32, ctypes.c_uint32)


class SetScreenSizeRequestCType(ctypes.Structure):
    """randr SetScreenSize"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("mm_width", ctypes.c_uint32),
        ("mm_height", ctypes.c_uint32),
    ]


ModeInfoStructPacket = DataPacket((
    ('id', FixedDataPacketField(MARKER_UINT32)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('dot_clock', FixedDataPacketField(MARKER_UINT32)),
    ('hsync_start', FixedDataPacketField(MARKER_UINT16)),
    ('hsync_end', FixedDataPacketField(MARKER_UINT16)),
    ('htotal', FixedDataPacketField(MARKER_UINT16)),
    ('hskew', FixedDataPacketField(MARKER_UINT16)),
    ('vsync_start', FixedDataPacketField(MARKER_UINT16)),
    ('vsync_end', FixedDataPacketField(MARKER_UINT16)),
    ('vtotal', FixedDataPacketField(MARKER_UINT16)),
    ('name_len', FixedDataPacketField(MARKER_UINT16)),
    ('mode_flags', FixedDataPacketField(MARKER_UINT32)),
))


class ModeInfoStruct:
    __slots__ = ('id', 'width', 'height', 'dot_clock', 'hsync_start', 'hsync_end', 'htotal', 'hskew', 'vsync_start', 'vsync_end', 'vtotal', 'name_len', 'mode_flags',)

    def __init__(
            self, *,
            id: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            dot_clock: Optional[int] = None,
            hsync_start: Optional[int] = None,
            hsync_end: Optional[int] = None,
            htotal: Optional[int] = None,
            hskew: Optional[int] = None,
            vsync_start: Optional[int] = None,
            vsync_end: Optional[int] = None,
            vtotal: Optional[int] = None,
            name_len: Optional[int] = None,
            mode_flags: Optional[int] = None,
    ) -> None:
        self.id = id
        self.width = width
        self.height = height
        self.dot_clock = dot_clock
        self.hsync_start = hsync_start
        self.hsync_end = hsync_end
        self.htotal = htotal
        self.hskew = hskew
        self.vsync_start = vsync_start
        self.vsync_end = vsync_end
        self.vtotal = vtotal
        self.name_len = name_len
        self.mode_flags = mode_flags

    def as_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'dot_clock': self.dot_clock,
            'hsync_start': self.hsync_start,
            'hsync_end': self.hsync_end,
            'htotal': self.htotal,
            'hskew': self.hskew,
            'vsync_start': self.vsync_start,
            'vsync_end': self.vsync_end,
            'vtotal': self.vtotal,
            'name_len': self.name_len,
            'mode_flags': self.mode_flags,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ModeInfoStruct':
        return ModeInfoStruct(**ModeInfoStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ModeInfoStructPacket.pack(**self.as_dict())


class ModeInfoStructCType(ctypes.Structure):
    """randr ModeInfo"""
    _fields_ = [
        ("id", ctypes.c_uint32),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("dot_clock", ctypes.c_uint32),
        ("hsync_start", ctypes.c_uint16),
        ("hsync_end", ctypes.c_uint16),
        ("htotal", ctypes.c_uint16),
        ("hskew", ctypes.c_uint16),
        ("vsync_start", ctypes.c_uint16),
        ("vsync_end", ctypes.c_uint16),
        ("vtotal", ctypes.c_uint16),
        ("name_len", ctypes.c_uint16),
        ("mode_flags", ctypes.c_uint32),
    ]


GetScreenResourcesRequestCookie = NewType('GetScreenResourcesRequestCookie', ctypes.c_uint32)


GetScreenResourcesRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class GetScreenResourcesRequest:
    OPCODE = 8

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
    def from_data(inp: BinaryIO) -> 'GetScreenResourcesRequest':
        return GetScreenResourcesRequest(**GetScreenResourcesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetScreenResourcesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetScreenResourcesRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetScreenResourcesRequest.lib = library.randr_getscreenresources
        GetScreenResourcesRequest.lib.restype = GetScreenResourcesRequestCookie
        GetScreenResourcesRequest.lib.argstype = (ctypes.c_uint32,)


class GetScreenResourcesRequestCType(ctypes.Structure):
    """randr GetScreenResources"""
    _fields_ = [
        ("window", ctypes.c_uint32),
    ]


GetScreenResourcesReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('config_timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('num_crtcs', FixedDataPacketField(MARKER_UINT16)),
    ('num_outputs', FixedDataPacketField(MARKER_UINT16)),
    ('num_modes', FixedDataPacketField(MARKER_UINT16)),
    ('names_len', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(8)),
    ('crtcs', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_crtcs'], 0)),
    ('outputs', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_outputs'], 0)),
    ('modes', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_modes'], 0)),
    ('names', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['names_len'], 0)),
))


class GetScreenResourcesReplyReply:
    __slots__ = ('timestamp', 'config_timestamp', 'num_crtcs', 'num_outputs', 'num_modes', 'names_len', 'crtcs', 'outputs', 'modes', 'names',)

    def __init__(
            self, *,
            timestamp: Optional[int] = None,
            config_timestamp: Optional[int] = None,
            num_crtcs: Optional[int] = None,
            num_outputs: Optional[int] = None,
            num_modes: Optional[int] = None,
            names_len: Optional[int] = None,
            crtcs: Optional[Sequence[int]] = None,
            outputs: Optional[Sequence[int]] = None,
            modes: Optional[Sequence[int]] = None,
            names: Optional[Sequence[int]] = None,
    ) -> None:
        self.timestamp = timestamp
        self.config_timestamp = config_timestamp
        self.num_crtcs = num_crtcs
        self.num_outputs = num_outputs
        self.num_modes = num_modes
        self.names_len = names_len
        self.crtcs = crtcs
        self.outputs = outputs
        self.modes = modes
        self.names = names

    def as_dict(self) -> Dict[str, Any]:
        return {
            'timestamp': self.timestamp,
            'config_timestamp': self.config_timestamp,
            'num_crtcs': self.num_crtcs,
            'num_outputs': self.num_outputs,
            'num_modes': self.num_modes,
            'names_len': self.names_len,
            'crtcs': self.crtcs,
            'outputs': self.outputs,
            'modes': self.modes,
            'names': self.names,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetScreenResourcesReplyReply':
        return GetScreenResourcesReplyReply(**GetScreenResourcesReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetScreenResourcesReplyReplyPacket.pack(**self.as_dict())


class GetScreenResourcesReplyReplyCType(ctypes.Structure):
    """randr GetScreenResources_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("timestamp", ctypes.c_uint32),
        ("config_timestamp", ctypes.c_uint32),
        ("num_crtcs", ctypes.c_uint16),
        ("num_outputs", ctypes.c_uint16),
        ("num_modes", ctypes.c_uint16),
        ("names_len", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 8),
        ("var_data", ctypes.c_void_p),
    ]


GetOutputInfoRequestCookie = NewType('GetOutputInfoRequestCookie', ctypes.c_uint32)


GetOutputInfoRequestPacket = DataPacket((
    ('output', FixedDataPacketField(MARKER_UINT32)),
    ('config_timestamp', FixedDataPacketField(MARKER_UINT32)),
))


class GetOutputInfoRequest:
    OPCODE = 9

    __slots__ = ('output', 'config_timestamp',)

    def __init__(
            self, *,
            output: Optional[int] = None,
            config_timestamp: Optional[int] = None,
    ) -> None:
        self.output = output
        self.config_timestamp = config_timestamp

    def as_dict(self) -> Dict[str, Any]:
        return {
            'output': self.output,
            'config_timestamp': self.config_timestamp,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetOutputInfoRequest':
        return GetOutputInfoRequest(**GetOutputInfoRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetOutputInfoRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], GetOutputInfoRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetOutputInfoRequest.lib = library.randr_getoutputinfo
        GetOutputInfoRequest.lib.restype = GetOutputInfoRequestCookie
        GetOutputInfoRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class GetOutputInfoRequestCType(ctypes.Structure):
    """randr GetOutputInfo"""
    _fields_ = [
        ("output", ctypes.c_uint32),
        ("config_timestamp", ctypes.c_uint32),
    ]


GetOutputInfoReplyReplyPacket = DataPacket((
    ('status', FixedDataPacketField(MARKER_UINT8)),
    ('timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('crtc', FixedDataPacketField(MARKER_UINT32)),
    ('mm_width', FixedDataPacketField(MARKER_UINT32)),
    ('mm_height', FixedDataPacketField(MARKER_UINT32)),
    ('connection', FixedDataPacketField(MARKER_UINT8)),
    ('subpixel_order', FixedDataPacketField(MARKER_UINT8)),
    ('num_crtcs', FixedDataPacketField(MARKER_UINT16)),
    ('num_modes', FixedDataPacketField(MARKER_UINT16)),
    ('num_preferred', FixedDataPacketField(MARKER_UINT16)),
    ('num_clones', FixedDataPacketField(MARKER_UINT16)),
    ('name_len', FixedDataPacketField(MARKER_UINT16)),
    ('crtcs', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_crtcs'], 0)),
    ('modes', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_modes'], 0)),
    ('clones', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_clones'], 0)),
    ('name', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['name_len'], 0)),
))


class GetOutputInfoReplyReply:
    __slots__ = ('status', 'timestamp', 'crtc', 'mm_width', 'mm_height', 'connection', 'subpixel_order', 'num_crtcs', 'num_modes', 'num_preferred', 'num_clones', 'name_len', 'crtcs', 'modes', 'clones', 'name',)

    def __init__(
            self, *,
            status: Optional[int] = None,
            timestamp: Optional[int] = None,
            crtc: Optional[int] = None,
            mm_width: Optional[int] = None,
            mm_height: Optional[int] = None,
            connection: Optional[int] = None,
            subpixel_order: Optional[int] = None,
            num_crtcs: Optional[int] = None,
            num_modes: Optional[int] = None,
            num_preferred: Optional[int] = None,
            num_clones: Optional[int] = None,
            name_len: Optional[int] = None,
            crtcs: Optional[Sequence[int]] = None,
            modes: Optional[Sequence[int]] = None,
            clones: Optional[Sequence[int]] = None,
            name: Optional[Sequence[int]] = None,
    ) -> None:
        self.status = status
        self.timestamp = timestamp
        self.crtc = crtc
        self.mm_width = mm_width
        self.mm_height = mm_height
        self.connection = connection
        self.subpixel_order = subpixel_order
        self.num_crtcs = num_crtcs
        self.num_modes = num_modes
        self.num_preferred = num_preferred
        self.num_clones = num_clones
        self.name_len = name_len
        self.crtcs = crtcs
        self.modes = modes
        self.clones = clones
        self.name = name

    def as_dict(self) -> Dict[str, Any]:
        return {
            'status': self.status,
            'timestamp': self.timestamp,
            'crtc': self.crtc,
            'mm_width': self.mm_width,
            'mm_height': self.mm_height,
            'connection': self.connection,
            'subpixel_order': self.subpixel_order,
            'num_crtcs': self.num_crtcs,
            'num_modes': self.num_modes,
            'num_preferred': self.num_preferred,
            'num_clones': self.num_clones,
            'name_len': self.name_len,
            'crtcs': self.crtcs,
            'modes': self.modes,
            'clones': self.clones,
            'name': self.name,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetOutputInfoReplyReply':
        return GetOutputInfoReplyReply(**GetOutputInfoReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetOutputInfoReplyReplyPacket.pack(**self.as_dict())


class GetOutputInfoReplyReplyCType(ctypes.Structure):
    """randr GetOutputInfo_reply"""
    _fields_ = [
        ("status", ctypes.c_uint8),
        ("timestamp", ctypes.c_uint32),
        ("crtc", ctypes.c_uint32),
        ("mm_width", ctypes.c_uint32),
        ("mm_height", ctypes.c_uint32),
        ("connection", ctypes.c_uint8),
        ("subpixel_order", ctypes.c_uint8),
        ("num_crtcs", ctypes.c_uint16),
        ("num_modes", ctypes.c_uint16),
        ("num_preferred", ctypes.c_uint16),
        ("num_clones", ctypes.c_uint16),
        ("name_len", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


ListOutputPropertiesRequestCookie = NewType('ListOutputPropertiesRequestCookie', ctypes.c_uint32)


ListOutputPropertiesRequestPacket = DataPacket((
    ('output', FixedDataPacketField(MARKER_UINT32)),
))


class ListOutputPropertiesRequest:
    OPCODE = 10

    __slots__ = ('output',)

    def __init__(
            self, *,
            output: Optional[int] = None,
    ) -> None:
        self.output = output

    def as_dict(self) -> Dict[str, Any]:
        return {
            'output': self.output,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ListOutputPropertiesRequest':
        return ListOutputPropertiesRequest(**ListOutputPropertiesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ListOutputPropertiesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ListOutputPropertiesRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ListOutputPropertiesRequest.lib = library.randr_listoutputproperties
        ListOutputPropertiesRequest.lib.restype = ListOutputPropertiesRequestCookie
        ListOutputPropertiesRequest.lib.argstype = (ctypes.c_uint32,)


class ListOutputPropertiesRequestCType(ctypes.Structure):
    """randr ListOutputProperties"""
    _fields_ = [
        ("output", ctypes.c_uint32),
    ]


ListOutputPropertiesReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('num_atoms', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(22)),
    ('atoms', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_atoms'], 0)),
))


class ListOutputPropertiesReplyReply:
    __slots__ = ('num_atoms', 'atoms',)

    def __init__(
            self, *,
            num_atoms: Optional[int] = None,
            atoms: Optional[Sequence[int]] = None,
    ) -> None:
        self.num_atoms = num_atoms
        self.atoms = atoms

    def as_dict(self) -> Dict[str, Any]:
        return {
            'num_atoms': self.num_atoms,
            'atoms': self.atoms,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ListOutputPropertiesReplyReply':
        return ListOutputPropertiesReplyReply(**ListOutputPropertiesReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ListOutputPropertiesReplyReplyPacket.pack(**self.as_dict())


class ListOutputPropertiesReplyReplyCType(ctypes.Structure):
    """randr ListOutputProperties_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("num_atoms", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 22),
        ("var_data", ctypes.c_void_p),
    ]


QueryOutputPropertyRequestCookie = NewType('QueryOutputPropertyRequestCookie', ctypes.c_uint32)


QueryOutputPropertyRequestPacket = DataPacket((
    ('output', FixedDataPacketField(MARKER_UINT32)),
    ('property', FixedDataPacketField(MARKER_UINT32)),
))


class QueryOutputPropertyRequest:
    OPCODE = 11

    __slots__ = ('output', 'property',)

    def __init__(
            self, *,
            output: Optional[int] = None,
            property: Optional[int] = None,
    ) -> None:
        self.output = output
        self.property = property

    def as_dict(self) -> Dict[str, Any]:
        return {
            'output': self.output,
            'property': self.property,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryOutputPropertyRequest':
        return QueryOutputPropertyRequest(**QueryOutputPropertyRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryOutputPropertyRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], QueryOutputPropertyRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryOutputPropertyRequest.lib = library.randr_queryoutputproperty
        QueryOutputPropertyRequest.lib.restype = QueryOutputPropertyRequestCookie
        QueryOutputPropertyRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class QueryOutputPropertyRequestCType(ctypes.Structure):
    """randr QueryOutputProperty"""
    _fields_ = [
        ("output", ctypes.c_uint32),
        ("property", ctypes.c_uint32),
    ]


QueryOutputPropertyReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pending', FixedDataPacketField(MARKER_UINT8)),
    ('range', FixedDataPacketField(MARKER_UINT8)),
    ('immutable', FixedDataPacketField(MARKER_UINT8)),
    ('pad1', FixedPadDataPacketField(21)),
    ('validValues', SimpleListDataPacketField(MARKER_INT32, lambda d, c: d['length'], 0)),
))


class QueryOutputPropertyReplyReply:
    __slots__ = ('pending', 'range', 'immutable', 'validvalues',)

    def __init__(
            self, *,
            pending: Optional[bool] = None,
            range: Optional[bool] = None,
            immutable: Optional[bool] = None,
            validvalues: Optional[Sequence[int]] = None,
    ) -> None:
        self.pending = pending
        self.range = range
        self.immutable = immutable
        self.validvalues = validvalues

    def as_dict(self) -> Dict[str, Any]:
        return {
            'pending': self.pending,
            'range': self.range,
            'immutable': self.immutable,
            'validValues': self.validvalues,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryOutputPropertyReplyReply':
        return QueryOutputPropertyReplyReply(**QueryOutputPropertyReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryOutputPropertyReplyReplyPacket.pack(**self.as_dict())


class QueryOutputPropertyReplyReplyCType(ctypes.Structure):
    """randr QueryOutputProperty_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pending", ctypes.c_int8),
        ("range", ctypes.c_int8),
        ("immutable", ctypes.c_int8),
        ("pad1", ctypes.c_uint8 * 21),
        ("var_data", ctypes.c_void_p),
    ]


ConfigureOutputPropertyRequestPacket = DataPacket((
    ('output', FixedDataPacketField(MARKER_UINT32)),
    ('property', FixedDataPacketField(MARKER_UINT32)),
    ('pending', FixedDataPacketField(MARKER_UINT8)),
    ('range', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
    ('values', SimpleListDataPacketField(MARKER_INT32, lambda d, c: 1, 0)),
))


class ConfigureOutputPropertyRequest:
    OPCODE = 12

    __slots__ = ('output', 'property', 'pending', 'range', 'values',)

    def __init__(
            self, *,
            output: Optional[int] = None,
            property: Optional[int] = None,
            pending: Optional[bool] = None,
            range: Optional[bool] = None,
            values: Optional[Sequence[int]] = None,
    ) -> None:
        self.output = output
        self.property = property
        self.pending = pending
        self.range = range
        self.values = values

    def as_dict(self) -> Dict[str, Any]:
        return {
            'output': self.output,
            'property': self.property,
            'pending': self.pending,
            'range': self.range,
            'values': self.values,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ConfigureOutputPropertyRequest':
        return ConfigureOutputPropertyRequest(**ConfigureOutputPropertyRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ConfigureOutputPropertyRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, bool, bool, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ConfigureOutputPropertyRequest.lib = library.randr_configureoutputproperty
        ConfigureOutputPropertyRequest.lib.restype = ctypes.c_uint32
        ConfigureOutputPropertyRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int8, ctypes.c_int8, ctypes.c_uint8 * 2, ctypes.c_void_p)


class ConfigureOutputPropertyRequestCType(ctypes.Structure):
    """randr ConfigureOutputProperty"""
    _fields_ = [
        ("output", ctypes.c_uint32),
        ("property", ctypes.c_uint32),
        ("pending", ctypes.c_int8),
        ("range", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


ChangeOutputPropertyRequestPacket = DataPacket((
    ('output', FixedDataPacketField(MARKER_UINT32)),
    ('property', FixedDataPacketField(MARKER_UINT32)),
    ('type', FixedDataPacketField(MARKER_UINT32)),
    ('format', FixedDataPacketField(MARKER_UINT8)),
    ('mode', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
    ('num_units', FixedDataPacketField(MARKER_UINT32)),
    ('data', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: ((d['num_units']) * (d['format'])) / (8), 0)),
))


class ChangeOutputPropertyRequest:
    OPCODE = 13

    __slots__ = ('output', 'property', 'type', 'format', 'mode', 'num_units', 'data',)

    def __init__(
            self, *,
            output: Optional[int] = None,
            property: Optional[int] = None,
            type: Optional[int] = None,
            format: Optional[int] = None,
            mode: Optional[int] = None,
            num_units: Optional[int] = None,
            data: Optional[Sequence[None]] = None,
    ) -> None:
        self.output = output
        self.property = property
        self.type = type
        self.format = format
        self.mode = mode
        self.num_units = num_units
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'output': self.output,
            'property': self.property,
            'type': self.type,
            'format': self.format,
            'mode': self.mode,
            'num_units': self.num_units,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ChangeOutputPropertyRequest':
        return ChangeOutputPropertyRequest(**ChangeOutputPropertyRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ChangeOutputPropertyRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, Sequence[None]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ChangeOutputPropertyRequest.lib = library.randr_changeoutputproperty
        ChangeOutputPropertyRequest.lib.restype = ctypes.c_uint32
        ChangeOutputPropertyRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8 * 2, ctypes.c_uint32, ctypes.c_void_p)


class ChangeOutputPropertyRequestCType(ctypes.Structure):
    """randr ChangeOutputProperty"""
    _fields_ = [
        ("output", ctypes.c_uint32),
        ("property", ctypes.c_uint32),
        ("type", ctypes.c_uint32),
        ("format", ctypes.c_uint8),
        ("mode", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 2),
        ("num_units", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


DeleteOutputPropertyRequestPacket = DataPacket((
    ('output', FixedDataPacketField(MARKER_UINT32)),
    ('property', FixedDataPacketField(MARKER_UINT32)),
))


class DeleteOutputPropertyRequest:
    OPCODE = 14

    __slots__ = ('output', 'property',)

    def __init__(
            self, *,
            output: Optional[int] = None,
            property: Optional[int] = None,
    ) -> None:
        self.output = output
        self.property = property

    def as_dict(self) -> Dict[str, Any]:
        return {
            'output': self.output,
            'property': self.property,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeleteOutputPropertyRequest':
        return DeleteOutputPropertyRequest(**DeleteOutputPropertyRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeleteOutputPropertyRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        DeleteOutputPropertyRequest.lib = library.randr_deleteoutputproperty
        DeleteOutputPropertyRequest.lib.restype = ctypes.c_uint32
        DeleteOutputPropertyRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class DeleteOutputPropertyRequestCType(ctypes.Structure):
    """randr DeleteOutputProperty"""
    _fields_ = [
        ("output", ctypes.c_uint32),
        ("property", ctypes.c_uint32),
    ]


GetOutputPropertyRequestCookie = NewType('GetOutputPropertyRequestCookie', ctypes.c_uint32)


GetOutputPropertyRequestPacket = DataPacket((
    ('output', FixedDataPacketField(MARKER_UINT32)),
    ('property', FixedDataPacketField(MARKER_UINT32)),
    ('type', FixedDataPacketField(MARKER_UINT32)),
    ('long_offset', FixedDataPacketField(MARKER_UINT32)),
    ('long_length', FixedDataPacketField(MARKER_UINT32)),
    ('delete', FixedDataPacketField(MARKER_UINT8)),
    ('pending', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
))


class GetOutputPropertyRequest:
    OPCODE = 15

    __slots__ = ('output', 'property', 'type', 'long_offset', 'long_length', 'delete', 'pending',)

    def __init__(
            self, *,
            output: Optional[int] = None,
            property: Optional[int] = None,
            type: Optional[int] = None,
            long_offset: Optional[int] = None,
            long_length: Optional[int] = None,
            delete: Optional[bool] = None,
            pending: Optional[bool] = None,
    ) -> None:
        self.output = output
        self.property = property
        self.type = type
        self.long_offset = long_offset
        self.long_length = long_length
        self.delete = delete
        self.pending = pending

    def as_dict(self) -> Dict[str, Any]:
        return {
            'output': self.output,
            'property': self.property,
            'type': self.type,
            'long_offset': self.long_offset,
            'long_length': self.long_length,
            'delete': self.delete,
            'pending': self.pending,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetOutputPropertyRequest':
        return GetOutputPropertyRequest(**GetOutputPropertyRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetOutputPropertyRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, bool, bool], GetOutputPropertyRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetOutputPropertyRequest.lib = library.randr_getoutputproperty
        GetOutputPropertyRequest.lib.restype = GetOutputPropertyRequestCookie
        GetOutputPropertyRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int8, ctypes.c_int8, ctypes.c_uint8 * 2)


class GetOutputPropertyRequestCType(ctypes.Structure):
    """randr GetOutputProperty"""
    _fields_ = [
        ("output", ctypes.c_uint32),
        ("property", ctypes.c_uint32),
        ("type", ctypes.c_uint32),
        ("long_offset", ctypes.c_uint32),
        ("long_length", ctypes.c_uint32),
        ("delete", ctypes.c_int8),
        ("pending", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 2),
    ]


GetOutputPropertyReplyReplyPacket = DataPacket((
    ('format', FixedDataPacketField(MARKER_UINT8)),
    ('type', FixedDataPacketField(MARKER_UINT32)),
    ('bytes_after', FixedDataPacketField(MARKER_UINT32)),
    ('num_items', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_INT8, lambda d, c: (d['num_items']) * ((d['format']) / (8)), 0)),
))


class GetOutputPropertyReplyReply:
    __slots__ = ('format', 'type', 'bytes_after', 'num_items', 'data',)

    def __init__(
            self, *,
            format: Optional[int] = None,
            type: Optional[int] = None,
            bytes_after: Optional[int] = None,
            num_items: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.format = format
        self.type = type
        self.bytes_after = bytes_after
        self.num_items = num_items
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'format': self.format,
            'type': self.type,
            'bytes_after': self.bytes_after,
            'num_items': self.num_items,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetOutputPropertyReplyReply':
        return GetOutputPropertyReplyReply(**GetOutputPropertyReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetOutputPropertyReplyReplyPacket.pack(**self.as_dict())


class GetOutputPropertyReplyReplyCType(ctypes.Structure):
    """randr GetOutputProperty_reply"""
    _fields_ = [
        ("format", ctypes.c_uint8),
        ("type", ctypes.c_uint32),
        ("bytes_after", ctypes.c_uint32),
        ("num_items", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


CreateModeRequestCookie = NewType('CreateModeRequestCookie', ctypes.c_uint32)


CreateModeRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('mode_info', FixedDataPacketField(MARKER_UINT32)),
    ('name', SimpleListDataPacketField(MARKER_INT8, lambda d, c: 1, 0)),
))


class CreateModeRequest:
    OPCODE = 16

    __slots__ = ('window', 'mode_info', 'name',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            mode_info: Optional[int] = None,
            name: Optional[Sequence[int]] = None,
    ) -> None:
        self.window = window
        self.mode_info = mode_info
        self.name = name

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'mode_info': self.mode_info,
            'name': self.name,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateModeRequest':
        return CreateModeRequest(**CreateModeRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateModeRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int]], CreateModeRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateModeRequest.lib = library.randr_createmode
        CreateModeRequest.lib.restype = CreateModeRequestCookie
        CreateModeRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)


class CreateModeRequestCType(ctypes.Structure):
    """randr CreateMode"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("mode_info", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


CreateModeReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('mode', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
))


class CreateModeReplyReply:
    __slots__ = ('mode',)

    def __init__(
            self, *,
            mode: Optional[int] = None,
    ) -> None:
        self.mode = mode

    def as_dict(self) -> Dict[str, Any]:
        return {
            'mode': self.mode,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateModeReplyReply':
        return CreateModeReplyReply(**CreateModeReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateModeReplyReplyPacket.pack(**self.as_dict())


class CreateModeReplyReplyCType(ctypes.Structure):
    """randr CreateMode_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("mode", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
    ]


DestroyModeRequestPacket = DataPacket((
    ('mode', FixedDataPacketField(MARKER_UINT32)),
))


class DestroyModeRequest:
    OPCODE = 17

    __slots__ = ('mode',)

    def __init__(
            self, *,
            mode: Optional[int] = None,
    ) -> None:
        self.mode = mode

    def as_dict(self) -> Dict[str, Any]:
        return {
            'mode': self.mode,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DestroyModeRequest':
        return DestroyModeRequest(**DestroyModeRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DestroyModeRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        DestroyModeRequest.lib = library.randr_destroymode
        DestroyModeRequest.lib.restype = ctypes.c_uint32
        DestroyModeRequest.lib.argstype = (ctypes.c_uint32,)


class DestroyModeRequestCType(ctypes.Structure):
    """randr DestroyMode"""
    _fields_ = [
        ("mode", ctypes.c_uint32),
    ]


AddOutputModeRequestPacket = DataPacket((
    ('output', FixedDataPacketField(MARKER_UINT32)),
    ('mode', FixedDataPacketField(MARKER_UINT32)),
))


class AddOutputModeRequest:
    OPCODE = 18

    __slots__ = ('output', 'mode',)

    def __init__(
            self, *,
            output: Optional[int] = None,
            mode: Optional[int] = None,
    ) -> None:
        self.output = output
        self.mode = mode

    def as_dict(self) -> Dict[str, Any]:
        return {
            'output': self.output,
            'mode': self.mode,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'AddOutputModeRequest':
        return AddOutputModeRequest(**AddOutputModeRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return AddOutputModeRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        AddOutputModeRequest.lib = library.randr_addoutputmode
        AddOutputModeRequest.lib.restype = ctypes.c_uint32
        AddOutputModeRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class AddOutputModeRequestCType(ctypes.Structure):
    """randr AddOutputMode"""
    _fields_ = [
        ("output", ctypes.c_uint32),
        ("mode", ctypes.c_uint32),
    ]


DeleteOutputModeRequestPacket = DataPacket((
    ('output', FixedDataPacketField(MARKER_UINT32)),
    ('mode', FixedDataPacketField(MARKER_UINT32)),
))


class DeleteOutputModeRequest:
    OPCODE = 19

    __slots__ = ('output', 'mode',)

    def __init__(
            self, *,
            output: Optional[int] = None,
            mode: Optional[int] = None,
    ) -> None:
        self.output = output
        self.mode = mode

    def as_dict(self) -> Dict[str, Any]:
        return {
            'output': self.output,
            'mode': self.mode,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeleteOutputModeRequest':
        return DeleteOutputModeRequest(**DeleteOutputModeRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeleteOutputModeRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        DeleteOutputModeRequest.lib = library.randr_deleteoutputmode
        DeleteOutputModeRequest.lib.restype = ctypes.c_uint32
        DeleteOutputModeRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class DeleteOutputModeRequestCType(ctypes.Structure):
    """randr DeleteOutputMode"""
    _fields_ = [
        ("output", ctypes.c_uint32),
        ("mode", ctypes.c_uint32),
    ]


GetCrtcInfoRequestCookie = NewType('GetCrtcInfoRequestCookie', ctypes.c_uint32)


GetCrtcInfoRequestPacket = DataPacket((
    ('crtc', FixedDataPacketField(MARKER_UINT32)),
    ('config_timestamp', FixedDataPacketField(MARKER_UINT32)),
))


class GetCrtcInfoRequest:
    OPCODE = 20

    __slots__ = ('crtc', 'config_timestamp',)

    def __init__(
            self, *,
            crtc: Optional[int] = None,
            config_timestamp: Optional[int] = None,
    ) -> None:
        self.crtc = crtc
        self.config_timestamp = config_timestamp

    def as_dict(self) -> Dict[str, Any]:
        return {
            'crtc': self.crtc,
            'config_timestamp': self.config_timestamp,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetCrtcInfoRequest':
        return GetCrtcInfoRequest(**GetCrtcInfoRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetCrtcInfoRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], GetCrtcInfoRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetCrtcInfoRequest.lib = library.randr_getcrtcinfo
        GetCrtcInfoRequest.lib.restype = GetCrtcInfoRequestCookie
        GetCrtcInfoRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class GetCrtcInfoRequestCType(ctypes.Structure):
    """randr GetCrtcInfo"""
    _fields_ = [
        ("crtc", ctypes.c_uint32),
        ("config_timestamp", ctypes.c_uint32),
    ]


GetCrtcInfoReplyReplyPacket = DataPacket((
    ('status', FixedDataPacketField(MARKER_UINT8)),
    ('timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('x', FixedDataPacketField(MARKER_INT16)),
    ('y', FixedDataPacketField(MARKER_INT16)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('mode', FixedDataPacketField(MARKER_UINT32)),
    ('rotation', FixedDataPacketField(MARKER_UINT16)),
    ('rotations', FixedDataPacketField(MARKER_UINT16)),
    ('num_outputs', FixedDataPacketField(MARKER_UINT16)),
    ('num_possible_outputs', FixedDataPacketField(MARKER_UINT16)),
    ('outputs', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_outputs'], 0)),
    ('possible', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_possible_outputs'], 0)),
))


class GetCrtcInfoReplyReply:
    __slots__ = ('status', 'timestamp', 'x', 'y', 'width', 'height', 'mode', 'rotation', 'rotations', 'num_outputs', 'num_possible_outputs', 'outputs', 'possible',)

    def __init__(
            self, *,
            status: Optional[int] = None,
            timestamp: Optional[int] = None,
            x: Optional[int] = None,
            y: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            mode: Optional[int] = None,
            rotation: Optional[int] = None,
            rotations: Optional[int] = None,
            num_outputs: Optional[int] = None,
            num_possible_outputs: Optional[int] = None,
            outputs: Optional[Sequence[int]] = None,
            possible: Optional[Sequence[int]] = None,
    ) -> None:
        self.status = status
        self.timestamp = timestamp
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.mode = mode
        self.rotation = rotation
        self.rotations = rotations
        self.num_outputs = num_outputs
        self.num_possible_outputs = num_possible_outputs
        self.outputs = outputs
        self.possible = possible

    def as_dict(self) -> Dict[str, Any]:
        return {
            'status': self.status,
            'timestamp': self.timestamp,
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height,
            'mode': self.mode,
            'rotation': self.rotation,
            'rotations': self.rotations,
            'num_outputs': self.num_outputs,
            'num_possible_outputs': self.num_possible_outputs,
            'outputs': self.outputs,
            'possible': self.possible,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetCrtcInfoReplyReply':
        return GetCrtcInfoReplyReply(**GetCrtcInfoReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetCrtcInfoReplyReplyPacket.pack(**self.as_dict())


class GetCrtcInfoReplyReplyCType(ctypes.Structure):
    """randr GetCrtcInfo_reply"""
    _fields_ = [
        ("status", ctypes.c_uint8),
        ("timestamp", ctypes.c_uint32),
        ("x", ctypes.c_int16),
        ("y", ctypes.c_int16),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("mode", ctypes.c_uint32),
        ("rotation", ctypes.c_uint16),
        ("rotations", ctypes.c_uint16),
        ("num_outputs", ctypes.c_uint16),
        ("num_possible_outputs", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


SetCrtcConfigRequestCookie = NewType('SetCrtcConfigRequestCookie', ctypes.c_uint32)


SetCrtcConfigRequestPacket = DataPacket((
    ('crtc', FixedDataPacketField(MARKER_UINT32)),
    ('timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('config_timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('x', FixedDataPacketField(MARKER_INT16)),
    ('y', FixedDataPacketField(MARKER_INT16)),
    ('mode', FixedDataPacketField(MARKER_UINT32)),
    ('rotation', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
    ('outputs', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 1, 0)),
))


class SetCrtcConfigRequest:
    OPCODE = 21

    __slots__ = ('crtc', 'timestamp', 'config_timestamp', 'x', 'y', 'mode', 'rotation', 'outputs',)

    def __init__(
            self, *,
            crtc: Optional[int] = None,
            timestamp: Optional[int] = None,
            config_timestamp: Optional[int] = None,
            x: Optional[int] = None,
            y: Optional[int] = None,
            mode: Optional[int] = None,
            rotation: Optional[int] = None,
            outputs: Optional[Sequence[int]] = None,
    ) -> None:
        self.crtc = crtc
        self.timestamp = timestamp
        self.config_timestamp = config_timestamp
        self.x = x
        self.y = y
        self.mode = mode
        self.rotation = rotation
        self.outputs = outputs

    def as_dict(self) -> Dict[str, Any]:
        return {
            'crtc': self.crtc,
            'timestamp': self.timestamp,
            'config_timestamp': self.config_timestamp,
            'x': self.x,
            'y': self.y,
            'mode': self.mode,
            'rotation': self.rotation,
            'outputs': self.outputs,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetCrtcConfigRequest':
        return SetCrtcConfigRequest(**SetCrtcConfigRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetCrtcConfigRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, Sequence[int]], SetCrtcConfigRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetCrtcConfigRequest.lib = library.randr_setcrtcconfig
        SetCrtcConfigRequest.lib.restype = SetCrtcConfigRequestCookie
        SetCrtcConfigRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint8 * 2, ctypes.c_void_p)


class SetCrtcConfigRequestCType(ctypes.Structure):
    """randr SetCrtcConfig"""
    _fields_ = [
        ("crtc", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint32),
        ("config_timestamp", ctypes.c_uint32),
        ("x", ctypes.c_int16),
        ("y", ctypes.c_int16),
        ("mode", ctypes.c_uint32),
        ("rotation", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


SetCrtcConfigReplyReplyPacket = DataPacket((
    ('status', FixedDataPacketField(MARKER_UINT8)),
    ('timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(20)),
))


class SetCrtcConfigReplyReply:
    __slots__ = ('status', 'timestamp',)

    def __init__(
            self, *,
            status: Optional[int] = None,
            timestamp: Optional[int] = None,
    ) -> None:
        self.status = status
        self.timestamp = timestamp

    def as_dict(self) -> Dict[str, Any]:
        return {
            'status': self.status,
            'timestamp': self.timestamp,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetCrtcConfigReplyReply':
        return SetCrtcConfigReplyReply(**SetCrtcConfigReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetCrtcConfigReplyReplyPacket.pack(**self.as_dict())


class SetCrtcConfigReplyReplyCType(ctypes.Structure):
    """randr SetCrtcConfig_reply"""
    _fields_ = [
        ("status", ctypes.c_uint8),
        ("timestamp", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 20),
    ]


GetCrtcGammaSizeRequestCookie = NewType('GetCrtcGammaSizeRequestCookie', ctypes.c_uint32)


GetCrtcGammaSizeRequestPacket = DataPacket((
    ('crtc', FixedDataPacketField(MARKER_UINT32)),
))


class GetCrtcGammaSizeRequest:
    OPCODE = 22

    __slots__ = ('crtc',)

    def __init__(
            self, *,
            crtc: Optional[int] = None,
    ) -> None:
        self.crtc = crtc

    def as_dict(self) -> Dict[str, Any]:
        return {
            'crtc': self.crtc,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetCrtcGammaSizeRequest':
        return GetCrtcGammaSizeRequest(**GetCrtcGammaSizeRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetCrtcGammaSizeRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetCrtcGammaSizeRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetCrtcGammaSizeRequest.lib = library.randr_getcrtcgammasize
        GetCrtcGammaSizeRequest.lib.restype = GetCrtcGammaSizeRequestCookie
        GetCrtcGammaSizeRequest.lib.argstype = (ctypes.c_uint32,)


class GetCrtcGammaSizeRequestCType(ctypes.Structure):
    """randr GetCrtcGammaSize"""
    _fields_ = [
        ("crtc", ctypes.c_uint32),
    ]


GetCrtcGammaSizeReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('size', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(22)),
))


class GetCrtcGammaSizeReplyReply:
    __slots__ = ('size',)

    def __init__(
            self, *,
            size: Optional[int] = None,
    ) -> None:
        self.size = size

    def as_dict(self) -> Dict[str, Any]:
        return {
            'size': self.size,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetCrtcGammaSizeReplyReply':
        return GetCrtcGammaSizeReplyReply(**GetCrtcGammaSizeReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetCrtcGammaSizeReplyReplyPacket.pack(**self.as_dict())


class GetCrtcGammaSizeReplyReplyCType(ctypes.Structure):
    """randr GetCrtcGammaSize_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("size", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 22),
    ]


GetCrtcGammaRequestCookie = NewType('GetCrtcGammaRequestCookie', ctypes.c_uint32)


GetCrtcGammaRequestPacket = DataPacket((
    ('crtc', FixedDataPacketField(MARKER_UINT32)),
))


class GetCrtcGammaRequest:
    OPCODE = 23

    __slots__ = ('crtc',)

    def __init__(
            self, *,
            crtc: Optional[int] = None,
    ) -> None:
        self.crtc = crtc

    def as_dict(self) -> Dict[str, Any]:
        return {
            'crtc': self.crtc,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetCrtcGammaRequest':
        return GetCrtcGammaRequest(**GetCrtcGammaRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetCrtcGammaRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetCrtcGammaRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetCrtcGammaRequest.lib = library.randr_getcrtcgamma
        GetCrtcGammaRequest.lib.restype = GetCrtcGammaRequestCookie
        GetCrtcGammaRequest.lib.argstype = (ctypes.c_uint32,)


class GetCrtcGammaRequestCType(ctypes.Structure):
    """randr GetCrtcGamma"""
    _fields_ = [
        ("crtc", ctypes.c_uint32),
    ]


GetCrtcGammaReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('size', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(22)),
    ('red', SimpleListDataPacketField(MARKER_UINT16, lambda d, c: d['size'], 0)),
    ('green', SimpleListDataPacketField(MARKER_UINT16, lambda d, c: d['size'], 0)),
    ('blue', SimpleListDataPacketField(MARKER_UINT16, lambda d, c: d['size'], 0)),
))


class GetCrtcGammaReplyReply:
    __slots__ = ('size', 'red', 'green', 'blue',)

    def __init__(
            self, *,
            size: Optional[int] = None,
            red: Optional[Sequence[int]] = None,
            green: Optional[Sequence[int]] = None,
            blue: Optional[Sequence[int]] = None,
    ) -> None:
        self.size = size
        self.red = red
        self.green = green
        self.blue = blue

    def as_dict(self) -> Dict[str, Any]:
        return {
            'size': self.size,
            'red': self.red,
            'green': self.green,
            'blue': self.blue,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetCrtcGammaReplyReply':
        return GetCrtcGammaReplyReply(**GetCrtcGammaReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetCrtcGammaReplyReplyPacket.pack(**self.as_dict())


class GetCrtcGammaReplyReplyCType(ctypes.Structure):
    """randr GetCrtcGamma_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("size", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 22),
        ("var_data", ctypes.c_void_p),
    ]


SetCrtcGammaRequestPacket = DataPacket((
    ('crtc', FixedDataPacketField(MARKER_UINT32)),
    ('size', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
    ('red', SimpleListDataPacketField(MARKER_UINT16, lambda d, c: d['size'], 0)),
    ('green', SimpleListDataPacketField(MARKER_UINT16, lambda d, c: d['size'], 0)),
    ('blue', SimpleListDataPacketField(MARKER_UINT16, lambda d, c: d['size'], 0)),
))


class SetCrtcGammaRequest:
    OPCODE = 24

    __slots__ = ('crtc', 'size', 'red', 'green', 'blue',)

    def __init__(
            self, *,
            crtc: Optional[int] = None,
            size: Optional[int] = None,
            red: Optional[Sequence[int]] = None,
            green: Optional[Sequence[int]] = None,
            blue: Optional[Sequence[int]] = None,
    ) -> None:
        self.crtc = crtc
        self.size = size
        self.red = red
        self.green = green
        self.blue = blue

    def as_dict(self) -> Dict[str, Any]:
        return {
            'crtc': self.crtc,
            'size': self.size,
            'red': self.red,
            'green': self.green,
            'blue': self.blue,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetCrtcGammaRequest':
        return SetCrtcGammaRequest(**SetCrtcGammaRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetCrtcGammaRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int], Sequence[int], Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetCrtcGammaRequest.lib = library.randr_setcrtcgamma
        SetCrtcGammaRequest.lib.restype = ctypes.c_uint32
        SetCrtcGammaRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint8 * 2, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)


class SetCrtcGammaRequestCType(ctypes.Structure):
    """randr SetCrtcGamma"""
    _fields_ = [
        ("crtc", ctypes.c_uint32),
        ("size", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


GetScreenResourcesCurrentRequestCookie = NewType('GetScreenResourcesCurrentRequestCookie', ctypes.c_uint32)


GetScreenResourcesCurrentRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class GetScreenResourcesCurrentRequest:
    OPCODE = 25

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
    def from_data(inp: BinaryIO) -> 'GetScreenResourcesCurrentRequest':
        return GetScreenResourcesCurrentRequest(**GetScreenResourcesCurrentRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetScreenResourcesCurrentRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetScreenResourcesCurrentRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetScreenResourcesCurrentRequest.lib = library.randr_getscreenresourcescurrent
        GetScreenResourcesCurrentRequest.lib.restype = GetScreenResourcesCurrentRequestCookie
        GetScreenResourcesCurrentRequest.lib.argstype = (ctypes.c_uint32,)


class GetScreenResourcesCurrentRequestCType(ctypes.Structure):
    """randr GetScreenResourcesCurrent"""
    _fields_ = [
        ("window", ctypes.c_uint32),
    ]


GetScreenResourcesCurrentReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('config_timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('num_crtcs', FixedDataPacketField(MARKER_UINT16)),
    ('num_outputs', FixedDataPacketField(MARKER_UINT16)),
    ('num_modes', FixedDataPacketField(MARKER_UINT16)),
    ('names_len', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(8)),
    ('crtcs', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_crtcs'], 0)),
    ('outputs', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_outputs'], 0)),
    ('modes', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_modes'], 0)),
    ('names', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['names_len'], 0)),
))


class GetScreenResourcesCurrentReplyReply:
    __slots__ = ('timestamp', 'config_timestamp', 'num_crtcs', 'num_outputs', 'num_modes', 'names_len', 'crtcs', 'outputs', 'modes', 'names',)

    def __init__(
            self, *,
            timestamp: Optional[int] = None,
            config_timestamp: Optional[int] = None,
            num_crtcs: Optional[int] = None,
            num_outputs: Optional[int] = None,
            num_modes: Optional[int] = None,
            names_len: Optional[int] = None,
            crtcs: Optional[Sequence[int]] = None,
            outputs: Optional[Sequence[int]] = None,
            modes: Optional[Sequence[int]] = None,
            names: Optional[Sequence[int]] = None,
    ) -> None:
        self.timestamp = timestamp
        self.config_timestamp = config_timestamp
        self.num_crtcs = num_crtcs
        self.num_outputs = num_outputs
        self.num_modes = num_modes
        self.names_len = names_len
        self.crtcs = crtcs
        self.outputs = outputs
        self.modes = modes
        self.names = names

    def as_dict(self) -> Dict[str, Any]:
        return {
            'timestamp': self.timestamp,
            'config_timestamp': self.config_timestamp,
            'num_crtcs': self.num_crtcs,
            'num_outputs': self.num_outputs,
            'num_modes': self.num_modes,
            'names_len': self.names_len,
            'crtcs': self.crtcs,
            'outputs': self.outputs,
            'modes': self.modes,
            'names': self.names,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetScreenResourcesCurrentReplyReply':
        return GetScreenResourcesCurrentReplyReply(**GetScreenResourcesCurrentReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetScreenResourcesCurrentReplyReplyPacket.pack(**self.as_dict())


class GetScreenResourcesCurrentReplyReplyCType(ctypes.Structure):
    """randr GetScreenResourcesCurrent_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("timestamp", ctypes.c_uint32),
        ("config_timestamp", ctypes.c_uint32),
        ("num_crtcs", ctypes.c_uint16),
        ("num_outputs", ctypes.c_uint16),
        ("num_modes", ctypes.c_uint16),
        ("names_len", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 8),
        ("var_data", ctypes.c_void_p),
    ]


SetCrtcTransformRequestPacket = DataPacket((
    ('crtc', FixedDataPacketField(MARKER_UINT32)),
    ('transform', FixedDataPacketField(MARKER_UINT32)),
    ('filter_len', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
    ('filter_name', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['filter_len'], 0)),
    ('pad1', AlignedPadDataPacketField(4)),
    ('filter_params', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 1, 0)),
))


class SetCrtcTransformRequest:
    OPCODE = 26

    __slots__ = ('crtc', 'transform', 'filter_len', 'filter_name', 'filter_params',)

    def __init__(
            self, *,
            crtc: Optional[int] = None,
            transform: Optional[int] = None,
            filter_len: Optional[int] = None,
            filter_name: Optional[Sequence[int]] = None,
            filter_params: Optional[Sequence[int]] = None,
    ) -> None:
        self.crtc = crtc
        self.transform = transform
        self.filter_len = filter_len
        self.filter_name = filter_name
        self.filter_params = filter_params

    def as_dict(self) -> Dict[str, Any]:
        return {
            'crtc': self.crtc,
            'transform': self.transform,
            'filter_len': self.filter_len,
            'filter_name': self.filter_name,
            'filter_params': self.filter_params,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetCrtcTransformRequest':
        return SetCrtcTransformRequest(**SetCrtcTransformRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetCrtcTransformRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, Sequence[int], Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetCrtcTransformRequest.lib = library.randr_setcrtctransform
        SetCrtcTransformRequest.lib.restype = ctypes.c_uint32
        SetCrtcTransformRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint8 * 2, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)


class SetCrtcTransformRequestCType(ctypes.Structure):
    """randr SetCrtcTransform"""
    _fields_ = [
        ("crtc", ctypes.c_uint32),
        ("transform", ctypes.c_uint32),
        ("filter_len", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


GetCrtcTransformRequestCookie = NewType('GetCrtcTransformRequestCookie', ctypes.c_uint32)


GetCrtcTransformRequestPacket = DataPacket((
    ('crtc', FixedDataPacketField(MARKER_UINT32)),
))


class GetCrtcTransformRequest:
    OPCODE = 27

    __slots__ = ('crtc',)

    def __init__(
            self, *,
            crtc: Optional[int] = None,
    ) -> None:
        self.crtc = crtc

    def as_dict(self) -> Dict[str, Any]:
        return {
            'crtc': self.crtc,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetCrtcTransformRequest':
        return GetCrtcTransformRequest(**GetCrtcTransformRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetCrtcTransformRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetCrtcTransformRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetCrtcTransformRequest.lib = library.randr_getcrtctransform
        GetCrtcTransformRequest.lib.restype = GetCrtcTransformRequestCookie
        GetCrtcTransformRequest.lib.argstype = (ctypes.c_uint32,)


class GetCrtcTransformRequestCType(ctypes.Structure):
    """randr GetCrtcTransform"""
    _fields_ = [
        ("crtc", ctypes.c_uint32),
    ]


GetCrtcTransformReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pending_transform', FixedDataPacketField(MARKER_UINT32)),
    ('has_transforms', FixedDataPacketField(MARKER_UINT8)),
    ('pad1', FixedPadDataPacketField(3)),
    ('current_transform', FixedDataPacketField(MARKER_UINT32)),
    ('pad2', FixedPadDataPacketField(4)),
    ('pending_len', FixedDataPacketField(MARKER_UINT16)),
    ('pending_nparams', FixedDataPacketField(MARKER_UINT16)),
    ('current_len', FixedDataPacketField(MARKER_UINT16)),
    ('current_nparams', FixedDataPacketField(MARKER_UINT16)),
    ('pending_filter_name', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['pending_len'], 0)),
    ('pad3', AlignedPadDataPacketField(4)),
    ('pending_params', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['pending_nparams'], 0)),
    ('current_filter_name', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['current_len'], 0)),
    ('pad4', AlignedPadDataPacketField(4)),
    ('current_params', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['current_nparams'], 0)),
))


class GetCrtcTransformReplyReply:
    __slots__ = ('pending_transform', 'has_transforms', 'current_transform', 'pending_len', 'pending_nparams', 'current_len', 'current_nparams', 'pending_filter_name', 'pending_params', 'current_filter_name', 'current_params',)

    def __init__(
            self, *,
            pending_transform: Optional[int] = None,
            has_transforms: Optional[bool] = None,
            current_transform: Optional[int] = None,
            pending_len: Optional[int] = None,
            pending_nparams: Optional[int] = None,
            current_len: Optional[int] = None,
            current_nparams: Optional[int] = None,
            pending_filter_name: Optional[Sequence[int]] = None,
            pending_params: Optional[Sequence[int]] = None,
            current_filter_name: Optional[Sequence[int]] = None,
            current_params: Optional[Sequence[int]] = None,
    ) -> None:
        self.pending_transform = pending_transform
        self.has_transforms = has_transforms
        self.current_transform = current_transform
        self.pending_len = pending_len
        self.pending_nparams = pending_nparams
        self.current_len = current_len
        self.current_nparams = current_nparams
        self.pending_filter_name = pending_filter_name
        self.pending_params = pending_params
        self.current_filter_name = current_filter_name
        self.current_params = current_params

    def as_dict(self) -> Dict[str, Any]:
        return {
            'pending_transform': self.pending_transform,
            'has_transforms': self.has_transforms,
            'current_transform': self.current_transform,
            'pending_len': self.pending_len,
            'pending_nparams': self.pending_nparams,
            'current_len': self.current_len,
            'current_nparams': self.current_nparams,
            'pending_filter_name': self.pending_filter_name,
            'pending_params': self.pending_params,
            'current_filter_name': self.current_filter_name,
            'current_params': self.current_params,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetCrtcTransformReplyReply':
        return GetCrtcTransformReplyReply(**GetCrtcTransformReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetCrtcTransformReplyReplyPacket.pack(**self.as_dict())


class GetCrtcTransformReplyReplyCType(ctypes.Structure):
    """randr GetCrtcTransform_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pending_transform", ctypes.c_uint32),
        ("has_transforms", ctypes.c_int8),
        ("pad1", ctypes.c_uint8 * 3),
        ("current_transform", ctypes.c_uint32),
        ("pad2", ctypes.c_uint8 * 4),
        ("pending_len", ctypes.c_uint16),
        ("pending_nparams", ctypes.c_uint16),
        ("current_len", ctypes.c_uint16),
        ("current_nparams", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


GetPanningRequestCookie = NewType('GetPanningRequestCookie', ctypes.c_uint32)


GetPanningRequestPacket = DataPacket((
    ('crtc', FixedDataPacketField(MARKER_UINT32)),
))


class GetPanningRequest:
    OPCODE = 28

    __slots__ = ('crtc',)

    def __init__(
            self, *,
            crtc: Optional[int] = None,
    ) -> None:
        self.crtc = crtc

    def as_dict(self) -> Dict[str, Any]:
        return {
            'crtc': self.crtc,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetPanningRequest':
        return GetPanningRequest(**GetPanningRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetPanningRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetPanningRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetPanningRequest.lib = library.randr_getpanning
        GetPanningRequest.lib.restype = GetPanningRequestCookie
        GetPanningRequest.lib.argstype = (ctypes.c_uint32,)


class GetPanningRequestCType(ctypes.Structure):
    """randr GetPanning"""
    _fields_ = [
        ("crtc", ctypes.c_uint32),
    ]


GetPanningReplyReplyPacket = DataPacket((
    ('status', FixedDataPacketField(MARKER_UINT8)),
    ('timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('left', FixedDataPacketField(MARKER_UINT16)),
    ('top', FixedDataPacketField(MARKER_UINT16)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('track_left', FixedDataPacketField(MARKER_UINT16)),
    ('track_top', FixedDataPacketField(MARKER_UINT16)),
    ('track_width', FixedDataPacketField(MARKER_UINT16)),
    ('track_height', FixedDataPacketField(MARKER_UINT16)),
    ('border_left', FixedDataPacketField(MARKER_INT16)),
    ('border_top', FixedDataPacketField(MARKER_INT16)),
    ('border_right', FixedDataPacketField(MARKER_INT16)),
    ('border_bottom', FixedDataPacketField(MARKER_INT16)),
))


class GetPanningReplyReply:
    __slots__ = ('status', 'timestamp', 'left', 'top', 'width', 'height', 'track_left', 'track_top', 'track_width', 'track_height', 'border_left', 'border_top', 'border_right', 'border_bottom',)

    def __init__(
            self, *,
            status: Optional[int] = None,
            timestamp: Optional[int] = None,
            left: Optional[int] = None,
            top: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            track_left: Optional[int] = None,
            track_top: Optional[int] = None,
            track_width: Optional[int] = None,
            track_height: Optional[int] = None,
            border_left: Optional[int] = None,
            border_top: Optional[int] = None,
            border_right: Optional[int] = None,
            border_bottom: Optional[int] = None,
    ) -> None:
        self.status = status
        self.timestamp = timestamp
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.track_left = track_left
        self.track_top = track_top
        self.track_width = track_width
        self.track_height = track_height
        self.border_left = border_left
        self.border_top = border_top
        self.border_right = border_right
        self.border_bottom = border_bottom

    def as_dict(self) -> Dict[str, Any]:
        return {
            'status': self.status,
            'timestamp': self.timestamp,
            'left': self.left,
            'top': self.top,
            'width': self.width,
            'height': self.height,
            'track_left': self.track_left,
            'track_top': self.track_top,
            'track_width': self.track_width,
            'track_height': self.track_height,
            'border_left': self.border_left,
            'border_top': self.border_top,
            'border_right': self.border_right,
            'border_bottom': self.border_bottom,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetPanningReplyReply':
        return GetPanningReplyReply(**GetPanningReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetPanningReplyReplyPacket.pack(**self.as_dict())


class GetPanningReplyReplyCType(ctypes.Structure):
    """randr GetPanning_reply"""
    _fields_ = [
        ("status", ctypes.c_uint8),
        ("timestamp", ctypes.c_uint32),
        ("left", ctypes.c_uint16),
        ("top", ctypes.c_uint16),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("track_left", ctypes.c_uint16),
        ("track_top", ctypes.c_uint16),
        ("track_width", ctypes.c_uint16),
        ("track_height", ctypes.c_uint16),
        ("border_left", ctypes.c_int16),
        ("border_top", ctypes.c_int16),
        ("border_right", ctypes.c_int16),
        ("border_bottom", ctypes.c_int16),
    ]


SetPanningRequestCookie = NewType('SetPanningRequestCookie', ctypes.c_uint32)


SetPanningRequestPacket = DataPacket((
    ('crtc', FixedDataPacketField(MARKER_UINT32)),
    ('timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('left', FixedDataPacketField(MARKER_UINT16)),
    ('top', FixedDataPacketField(MARKER_UINT16)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('track_left', FixedDataPacketField(MARKER_UINT16)),
    ('track_top', FixedDataPacketField(MARKER_UINT16)),
    ('track_width', FixedDataPacketField(MARKER_UINT16)),
    ('track_height', FixedDataPacketField(MARKER_UINT16)),
    ('border_left', FixedDataPacketField(MARKER_INT16)),
    ('border_top', FixedDataPacketField(MARKER_INT16)),
    ('border_right', FixedDataPacketField(MARKER_INT16)),
    ('border_bottom', FixedDataPacketField(MARKER_INT16)),
))


class SetPanningRequest:
    OPCODE = 29

    __slots__ = ('crtc', 'timestamp', 'left', 'top', 'width', 'height', 'track_left', 'track_top', 'track_width', 'track_height', 'border_left', 'border_top', 'border_right', 'border_bottom',)

    def __init__(
            self, *,
            crtc: Optional[int] = None,
            timestamp: Optional[int] = None,
            left: Optional[int] = None,
            top: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            track_left: Optional[int] = None,
            track_top: Optional[int] = None,
            track_width: Optional[int] = None,
            track_height: Optional[int] = None,
            border_left: Optional[int] = None,
            border_top: Optional[int] = None,
            border_right: Optional[int] = None,
            border_bottom: Optional[int] = None,
    ) -> None:
        self.crtc = crtc
        self.timestamp = timestamp
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.track_left = track_left
        self.track_top = track_top
        self.track_width = track_width
        self.track_height = track_height
        self.border_left = border_left
        self.border_top = border_top
        self.border_right = border_right
        self.border_bottom = border_bottom

    def as_dict(self) -> Dict[str, Any]:
        return {
            'crtc': self.crtc,
            'timestamp': self.timestamp,
            'left': self.left,
            'top': self.top,
            'width': self.width,
            'height': self.height,
            'track_left': self.track_left,
            'track_top': self.track_top,
            'track_width': self.track_width,
            'track_height': self.track_height,
            'border_left': self.border_left,
            'border_top': self.border_top,
            'border_right': self.border_right,
            'border_bottom': self.border_bottom,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetPanningRequest':
        return SetPanningRequest(**SetPanningRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetPanningRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, int, int, int, int, int, int, int], SetPanningRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetPanningRequest.lib = library.randr_setpanning
        SetPanningRequest.lib.restype = SetPanningRequestCookie
        SetPanningRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_int16, ctypes.c_int16, ctypes.c_int16, ctypes.c_int16)


class SetPanningRequestCType(ctypes.Structure):
    """randr SetPanning"""
    _fields_ = [
        ("crtc", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint32),
        ("left", ctypes.c_uint16),
        ("top", ctypes.c_uint16),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("track_left", ctypes.c_uint16),
        ("track_top", ctypes.c_uint16),
        ("track_width", ctypes.c_uint16),
        ("track_height", ctypes.c_uint16),
        ("border_left", ctypes.c_int16),
        ("border_top", ctypes.c_int16),
        ("border_right", ctypes.c_int16),
        ("border_bottom", ctypes.c_int16),
    ]


SetPanningReplyReplyPacket = DataPacket((
    ('status', FixedDataPacketField(MARKER_UINT8)),
    ('timestamp', FixedDataPacketField(MARKER_UINT32)),
))


class SetPanningReplyReply:
    __slots__ = ('status', 'timestamp',)

    def __init__(
            self, *,
            status: Optional[int] = None,
            timestamp: Optional[int] = None,
    ) -> None:
        self.status = status
        self.timestamp = timestamp

    def as_dict(self) -> Dict[str, Any]:
        return {
            'status': self.status,
            'timestamp': self.timestamp,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetPanningReplyReply':
        return SetPanningReplyReply(**SetPanningReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetPanningReplyReplyPacket.pack(**self.as_dict())


class SetPanningReplyReplyCType(ctypes.Structure):
    """randr SetPanning_reply"""
    _fields_ = [
        ("status", ctypes.c_uint8),
        ("timestamp", ctypes.c_uint32),
    ]


SetOutputPrimaryRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('output', FixedDataPacketField(MARKER_UINT32)),
))


class SetOutputPrimaryRequest:
    OPCODE = 30

    __slots__ = ('window', 'output',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            output: Optional[int] = None,
    ) -> None:
        self.window = window
        self.output = output

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'output': self.output,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetOutputPrimaryRequest':
        return SetOutputPrimaryRequest(**SetOutputPrimaryRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetOutputPrimaryRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetOutputPrimaryRequest.lib = library.randr_setoutputprimary
        SetOutputPrimaryRequest.lib.restype = ctypes.c_uint32
        SetOutputPrimaryRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class SetOutputPrimaryRequestCType(ctypes.Structure):
    """randr SetOutputPrimary"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("output", ctypes.c_uint32),
    ]


GetOutputPrimaryRequestCookie = NewType('GetOutputPrimaryRequestCookie', ctypes.c_uint32)


GetOutputPrimaryRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class GetOutputPrimaryRequest:
    OPCODE = 31

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
    def from_data(inp: BinaryIO) -> 'GetOutputPrimaryRequest':
        return GetOutputPrimaryRequest(**GetOutputPrimaryRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetOutputPrimaryRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetOutputPrimaryRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetOutputPrimaryRequest.lib = library.randr_getoutputprimary
        GetOutputPrimaryRequest.lib.restype = GetOutputPrimaryRequestCookie
        GetOutputPrimaryRequest.lib.argstype = (ctypes.c_uint32,)


class GetOutputPrimaryRequestCType(ctypes.Structure):
    """randr GetOutputPrimary"""
    _fields_ = [
        ("window", ctypes.c_uint32),
    ]


GetOutputPrimaryReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('output', FixedDataPacketField(MARKER_UINT32)),
))


class GetOutputPrimaryReplyReply:
    __slots__ = ('output',)

    def __init__(
            self, *,
            output: Optional[int] = None,
    ) -> None:
        self.output = output

    def as_dict(self) -> Dict[str, Any]:
        return {
            'output': self.output,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetOutputPrimaryReplyReply':
        return GetOutputPrimaryReplyReply(**GetOutputPrimaryReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetOutputPrimaryReplyReplyPacket.pack(**self.as_dict())


class GetOutputPrimaryReplyReplyCType(ctypes.Structure):
    """randr GetOutputPrimary_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("output", ctypes.c_uint32),
    ]


GetProvidersRequestCookie = NewType('GetProvidersRequestCookie', ctypes.c_uint32)


GetProvidersRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class GetProvidersRequest:
    OPCODE = 32

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
    def from_data(inp: BinaryIO) -> 'GetProvidersRequest':
        return GetProvidersRequest(**GetProvidersRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetProvidersRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetProvidersRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetProvidersRequest.lib = library.randr_getproviders
        GetProvidersRequest.lib.restype = GetProvidersRequestCookie
        GetProvidersRequest.lib.argstype = (ctypes.c_uint32,)


class GetProvidersRequestCType(ctypes.Structure):
    """randr GetProviders"""
    _fields_ = [
        ("window", ctypes.c_uint32),
    ]


GetProvidersReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('num_providers', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(18)),
    ('providers', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_providers'], 0)),
))


class GetProvidersReplyReply:
    __slots__ = ('timestamp', 'num_providers', 'providers',)

    def __init__(
            self, *,
            timestamp: Optional[int] = None,
            num_providers: Optional[int] = None,
            providers: Optional[Sequence[int]] = None,
    ) -> None:
        self.timestamp = timestamp
        self.num_providers = num_providers
        self.providers = providers

    def as_dict(self) -> Dict[str, Any]:
        return {
            'timestamp': self.timestamp,
            'num_providers': self.num_providers,
            'providers': self.providers,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetProvidersReplyReply':
        return GetProvidersReplyReply(**GetProvidersReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetProvidersReplyReplyPacket.pack(**self.as_dict())


class GetProvidersReplyReplyCType(ctypes.Structure):
    """randr GetProviders_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("timestamp", ctypes.c_uint32),
        ("num_providers", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 18),
        ("var_data", ctypes.c_void_p),
    ]


GetProviderInfoRequestCookie = NewType('GetProviderInfoRequestCookie', ctypes.c_uint32)


GetProviderInfoRequestPacket = DataPacket((
    ('provider', FixedDataPacketField(MARKER_UINT32)),
    ('config_timestamp', FixedDataPacketField(MARKER_UINT32)),
))


class GetProviderInfoRequest:
    OPCODE = 33

    __slots__ = ('provider', 'config_timestamp',)

    def __init__(
            self, *,
            provider: Optional[int] = None,
            config_timestamp: Optional[int] = None,
    ) -> None:
        self.provider = provider
        self.config_timestamp = config_timestamp

    def as_dict(self) -> Dict[str, Any]:
        return {
            'provider': self.provider,
            'config_timestamp': self.config_timestamp,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetProviderInfoRequest':
        return GetProviderInfoRequest(**GetProviderInfoRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetProviderInfoRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], GetProviderInfoRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetProviderInfoRequest.lib = library.randr_getproviderinfo
        GetProviderInfoRequest.lib.restype = GetProviderInfoRequestCookie
        GetProviderInfoRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class GetProviderInfoRequestCType(ctypes.Structure):
    """randr GetProviderInfo"""
    _fields_ = [
        ("provider", ctypes.c_uint32),
        ("config_timestamp", ctypes.c_uint32),
    ]


GetProviderInfoReplyReplyPacket = DataPacket((
    ('status', FixedDataPacketField(MARKER_UINT8)),
    ('timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('capabilities', FixedDataPacketField(MARKER_UINT32)),
    ('num_crtcs', FixedDataPacketField(MARKER_UINT16)),
    ('num_outputs', FixedDataPacketField(MARKER_UINT16)),
    ('num_associated_providers', FixedDataPacketField(MARKER_UINT16)),
    ('name_len', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(8)),
    ('crtcs', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_crtcs'], 0)),
    ('outputs', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_outputs'], 0)),
    ('associated_providers', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_associated_providers'], 0)),
    ('associated_capability', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_associated_providers'], 0)),
    ('name', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['name_len'], 0)),
))


class GetProviderInfoReplyReply:
    __slots__ = ('status', 'timestamp', 'capabilities', 'num_crtcs', 'num_outputs', 'num_associated_providers', 'name_len', 'crtcs', 'outputs', 'associated_providers', 'associated_capability', 'name',)

    def __init__(
            self, *,
            status: Optional[int] = None,
            timestamp: Optional[int] = None,
            capabilities: Optional[int] = None,
            num_crtcs: Optional[int] = None,
            num_outputs: Optional[int] = None,
            num_associated_providers: Optional[int] = None,
            name_len: Optional[int] = None,
            crtcs: Optional[Sequence[int]] = None,
            outputs: Optional[Sequence[int]] = None,
            associated_providers: Optional[Sequence[int]] = None,
            associated_capability: Optional[Sequence[int]] = None,
            name: Optional[Sequence[int]] = None,
    ) -> None:
        self.status = status
        self.timestamp = timestamp
        self.capabilities = capabilities
        self.num_crtcs = num_crtcs
        self.num_outputs = num_outputs
        self.num_associated_providers = num_associated_providers
        self.name_len = name_len
        self.crtcs = crtcs
        self.outputs = outputs
        self.associated_providers = associated_providers
        self.associated_capability = associated_capability
        self.name = name

    def as_dict(self) -> Dict[str, Any]:
        return {
            'status': self.status,
            'timestamp': self.timestamp,
            'capabilities': self.capabilities,
            'num_crtcs': self.num_crtcs,
            'num_outputs': self.num_outputs,
            'num_associated_providers': self.num_associated_providers,
            'name_len': self.name_len,
            'crtcs': self.crtcs,
            'outputs': self.outputs,
            'associated_providers': self.associated_providers,
            'associated_capability': self.associated_capability,
            'name': self.name,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetProviderInfoReplyReply':
        return GetProviderInfoReplyReply(**GetProviderInfoReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetProviderInfoReplyReplyPacket.pack(**self.as_dict())


class GetProviderInfoReplyReplyCType(ctypes.Structure):
    """randr GetProviderInfo_reply"""
    _fields_ = [
        ("status", ctypes.c_uint8),
        ("timestamp", ctypes.c_uint32),
        ("capabilities", ctypes.c_uint32),
        ("num_crtcs", ctypes.c_uint16),
        ("num_outputs", ctypes.c_uint16),
        ("num_associated_providers", ctypes.c_uint16),
        ("name_len", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 8),
        ("var_data", ctypes.c_void_p),
    ]


SetProviderOffloadSinkRequestPacket = DataPacket((
    ('provider', FixedDataPacketField(MARKER_UINT32)),
    ('sink_provider', FixedDataPacketField(MARKER_UINT32)),
    ('config_timestamp', FixedDataPacketField(MARKER_UINT32)),
))


class SetProviderOffloadSinkRequest:
    OPCODE = 34

    __slots__ = ('provider', 'sink_provider', 'config_timestamp',)

    def __init__(
            self, *,
            provider: Optional[int] = None,
            sink_provider: Optional[int] = None,
            config_timestamp: Optional[int] = None,
    ) -> None:
        self.provider = provider
        self.sink_provider = sink_provider
        self.config_timestamp = config_timestamp

    def as_dict(self) -> Dict[str, Any]:
        return {
            'provider': self.provider,
            'sink_provider': self.sink_provider,
            'config_timestamp': self.config_timestamp,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetProviderOffloadSinkRequest':
        return SetProviderOffloadSinkRequest(**SetProviderOffloadSinkRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetProviderOffloadSinkRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetProviderOffloadSinkRequest.lib = library.randr_setprovideroffloadsink
        SetProviderOffloadSinkRequest.lib.restype = ctypes.c_uint32
        SetProviderOffloadSinkRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class SetProviderOffloadSinkRequestCType(ctypes.Structure):
    """randr SetProviderOffloadSink"""
    _fields_ = [
        ("provider", ctypes.c_uint32),
        ("sink_provider", ctypes.c_uint32),
        ("config_timestamp", ctypes.c_uint32),
    ]


SetProviderOutputSourceRequestPacket = DataPacket((
    ('provider', FixedDataPacketField(MARKER_UINT32)),
    ('source_provider', FixedDataPacketField(MARKER_UINT32)),
    ('config_timestamp', FixedDataPacketField(MARKER_UINT32)),
))


class SetProviderOutputSourceRequest:
    OPCODE = 35

    __slots__ = ('provider', 'source_provider', 'config_timestamp',)

    def __init__(
            self, *,
            provider: Optional[int] = None,
            source_provider: Optional[int] = None,
            config_timestamp: Optional[int] = None,
    ) -> None:
        self.provider = provider
        self.source_provider = source_provider
        self.config_timestamp = config_timestamp

    def as_dict(self) -> Dict[str, Any]:
        return {
            'provider': self.provider,
            'source_provider': self.source_provider,
            'config_timestamp': self.config_timestamp,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetProviderOutputSourceRequest':
        return SetProviderOutputSourceRequest(**SetProviderOutputSourceRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetProviderOutputSourceRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetProviderOutputSourceRequest.lib = library.randr_setprovideroutputsource
        SetProviderOutputSourceRequest.lib.restype = ctypes.c_uint32
        SetProviderOutputSourceRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class SetProviderOutputSourceRequestCType(ctypes.Structure):
    """randr SetProviderOutputSource"""
    _fields_ = [
        ("provider", ctypes.c_uint32),
        ("source_provider", ctypes.c_uint32),
        ("config_timestamp", ctypes.c_uint32),
    ]


ListProviderPropertiesRequestCookie = NewType('ListProviderPropertiesRequestCookie', ctypes.c_uint32)


ListProviderPropertiesRequestPacket = DataPacket((
    ('provider', FixedDataPacketField(MARKER_UINT32)),
))


class ListProviderPropertiesRequest:
    OPCODE = 36

    __slots__ = ('provider',)

    def __init__(
            self, *,
            provider: Optional[int] = None,
    ) -> None:
        self.provider = provider

    def as_dict(self) -> Dict[str, Any]:
        return {
            'provider': self.provider,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ListProviderPropertiesRequest':
        return ListProviderPropertiesRequest(**ListProviderPropertiesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ListProviderPropertiesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ListProviderPropertiesRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ListProviderPropertiesRequest.lib = library.randr_listproviderproperties
        ListProviderPropertiesRequest.lib.restype = ListProviderPropertiesRequestCookie
        ListProviderPropertiesRequest.lib.argstype = (ctypes.c_uint32,)


class ListProviderPropertiesRequestCType(ctypes.Structure):
    """randr ListProviderProperties"""
    _fields_ = [
        ("provider", ctypes.c_uint32),
    ]


ListProviderPropertiesReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('num_atoms', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(22)),
    ('atoms', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_atoms'], 0)),
))


class ListProviderPropertiesReplyReply:
    __slots__ = ('num_atoms', 'atoms',)

    def __init__(
            self, *,
            num_atoms: Optional[int] = None,
            atoms: Optional[Sequence[int]] = None,
    ) -> None:
        self.num_atoms = num_atoms
        self.atoms = atoms

    def as_dict(self) -> Dict[str, Any]:
        return {
            'num_atoms': self.num_atoms,
            'atoms': self.atoms,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ListProviderPropertiesReplyReply':
        return ListProviderPropertiesReplyReply(**ListProviderPropertiesReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ListProviderPropertiesReplyReplyPacket.pack(**self.as_dict())


class ListProviderPropertiesReplyReplyCType(ctypes.Structure):
    """randr ListProviderProperties_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("num_atoms", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 22),
        ("var_data", ctypes.c_void_p),
    ]


QueryProviderPropertyRequestCookie = NewType('QueryProviderPropertyRequestCookie', ctypes.c_uint32)


QueryProviderPropertyRequestPacket = DataPacket((
    ('provider', FixedDataPacketField(MARKER_UINT32)),
    ('property', FixedDataPacketField(MARKER_UINT32)),
))


class QueryProviderPropertyRequest:
    OPCODE = 37

    __slots__ = ('provider', 'property',)

    def __init__(
            self, *,
            provider: Optional[int] = None,
            property: Optional[int] = None,
    ) -> None:
        self.provider = provider
        self.property = property

    def as_dict(self) -> Dict[str, Any]:
        return {
            'provider': self.provider,
            'property': self.property,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryProviderPropertyRequest':
        return QueryProviderPropertyRequest(**QueryProviderPropertyRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryProviderPropertyRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], QueryProviderPropertyRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryProviderPropertyRequest.lib = library.randr_queryproviderproperty
        QueryProviderPropertyRequest.lib.restype = QueryProviderPropertyRequestCookie
        QueryProviderPropertyRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class QueryProviderPropertyRequestCType(ctypes.Structure):
    """randr QueryProviderProperty"""
    _fields_ = [
        ("provider", ctypes.c_uint32),
        ("property", ctypes.c_uint32),
    ]


QueryProviderPropertyReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pending', FixedDataPacketField(MARKER_UINT8)),
    ('range', FixedDataPacketField(MARKER_UINT8)),
    ('immutable', FixedDataPacketField(MARKER_UINT8)),
    ('pad1', FixedPadDataPacketField(21)),
    ('valid_values', SimpleListDataPacketField(MARKER_INT32, lambda d, c: d['length'], 0)),
))


class QueryProviderPropertyReplyReply:
    __slots__ = ('pending', 'range', 'immutable', 'valid_values',)

    def __init__(
            self, *,
            pending: Optional[bool] = None,
            range: Optional[bool] = None,
            immutable: Optional[bool] = None,
            valid_values: Optional[Sequence[int]] = None,
    ) -> None:
        self.pending = pending
        self.range = range
        self.immutable = immutable
        self.valid_values = valid_values

    def as_dict(self) -> Dict[str, Any]:
        return {
            'pending': self.pending,
            'range': self.range,
            'immutable': self.immutable,
            'valid_values': self.valid_values,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryProviderPropertyReplyReply':
        return QueryProviderPropertyReplyReply(**QueryProviderPropertyReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryProviderPropertyReplyReplyPacket.pack(**self.as_dict())


class QueryProviderPropertyReplyReplyCType(ctypes.Structure):
    """randr QueryProviderProperty_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pending", ctypes.c_int8),
        ("range", ctypes.c_int8),
        ("immutable", ctypes.c_int8),
        ("pad1", ctypes.c_uint8 * 21),
        ("var_data", ctypes.c_void_p),
    ]


ConfigureProviderPropertyRequestPacket = DataPacket((
    ('provider', FixedDataPacketField(MARKER_UINT32)),
    ('property', FixedDataPacketField(MARKER_UINT32)),
    ('pending', FixedDataPacketField(MARKER_UINT8)),
    ('range', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
    ('values', SimpleListDataPacketField(MARKER_INT32, lambda d, c: 1, 0)),
))


class ConfigureProviderPropertyRequest:
    OPCODE = 38

    __slots__ = ('provider', 'property', 'pending', 'range', 'values',)

    def __init__(
            self, *,
            provider: Optional[int] = None,
            property: Optional[int] = None,
            pending: Optional[bool] = None,
            range: Optional[bool] = None,
            values: Optional[Sequence[int]] = None,
    ) -> None:
        self.provider = provider
        self.property = property
        self.pending = pending
        self.range = range
        self.values = values

    def as_dict(self) -> Dict[str, Any]:
        return {
            'provider': self.provider,
            'property': self.property,
            'pending': self.pending,
            'range': self.range,
            'values': self.values,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ConfigureProviderPropertyRequest':
        return ConfigureProviderPropertyRequest(**ConfigureProviderPropertyRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ConfigureProviderPropertyRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, bool, bool, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ConfigureProviderPropertyRequest.lib = library.randr_configureproviderproperty
        ConfigureProviderPropertyRequest.lib.restype = ctypes.c_uint32
        ConfigureProviderPropertyRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int8, ctypes.c_int8, ctypes.c_uint8 * 2, ctypes.c_void_p)


class ConfigureProviderPropertyRequestCType(ctypes.Structure):
    """randr ConfigureProviderProperty"""
    _fields_ = [
        ("provider", ctypes.c_uint32),
        ("property", ctypes.c_uint32),
        ("pending", ctypes.c_int8),
        ("range", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


ChangeProviderPropertyRequestPacket = DataPacket((
    ('provider', FixedDataPacketField(MARKER_UINT32)),
    ('property', FixedDataPacketField(MARKER_UINT32)),
    ('type', FixedDataPacketField(MARKER_UINT32)),
    ('format', FixedDataPacketField(MARKER_UINT8)),
    ('mode', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
    ('num_items', FixedDataPacketField(MARKER_UINT32)),
    ('data', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: (d['num_items']) * ((d['format']) / (8)), 0)),
))


class ChangeProviderPropertyRequest:
    OPCODE = 39

    __slots__ = ('provider', 'property', 'type', 'format', 'mode', 'num_items', 'data',)

    def __init__(
            self, *,
            provider: Optional[int] = None,
            property: Optional[int] = None,
            type: Optional[int] = None,
            format: Optional[int] = None,
            mode: Optional[int] = None,
            num_items: Optional[int] = None,
            data: Optional[Sequence[None]] = None,
    ) -> None:
        self.provider = provider
        self.property = property
        self.type = type
        self.format = format
        self.mode = mode
        self.num_items = num_items
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'provider': self.provider,
            'property': self.property,
            'type': self.type,
            'format': self.format,
            'mode': self.mode,
            'num_items': self.num_items,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ChangeProviderPropertyRequest':
        return ChangeProviderPropertyRequest(**ChangeProviderPropertyRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ChangeProviderPropertyRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, Sequence[None]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ChangeProviderPropertyRequest.lib = library.randr_changeproviderproperty
        ChangeProviderPropertyRequest.lib.restype = ctypes.c_uint32
        ChangeProviderPropertyRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8 * 2, ctypes.c_uint32, ctypes.c_void_p)


class ChangeProviderPropertyRequestCType(ctypes.Structure):
    """randr ChangeProviderProperty"""
    _fields_ = [
        ("provider", ctypes.c_uint32),
        ("property", ctypes.c_uint32),
        ("type", ctypes.c_uint32),
        ("format", ctypes.c_uint8),
        ("mode", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 2),
        ("num_items", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


DeleteProviderPropertyRequestPacket = DataPacket((
    ('provider', FixedDataPacketField(MARKER_UINT32)),
    ('property', FixedDataPacketField(MARKER_UINT32)),
))


class DeleteProviderPropertyRequest:
    OPCODE = 40

    __slots__ = ('provider', 'property',)

    def __init__(
            self, *,
            provider: Optional[int] = None,
            property: Optional[int] = None,
    ) -> None:
        self.provider = provider
        self.property = property

    def as_dict(self) -> Dict[str, Any]:
        return {
            'provider': self.provider,
            'property': self.property,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeleteProviderPropertyRequest':
        return DeleteProviderPropertyRequest(**DeleteProviderPropertyRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeleteProviderPropertyRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        DeleteProviderPropertyRequest.lib = library.randr_deleteproviderproperty
        DeleteProviderPropertyRequest.lib.restype = ctypes.c_uint32
        DeleteProviderPropertyRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class DeleteProviderPropertyRequestCType(ctypes.Structure):
    """randr DeleteProviderProperty"""
    _fields_ = [
        ("provider", ctypes.c_uint32),
        ("property", ctypes.c_uint32),
    ]


GetProviderPropertyRequestCookie = NewType('GetProviderPropertyRequestCookie', ctypes.c_uint32)


GetProviderPropertyRequestPacket = DataPacket((
    ('provider', FixedDataPacketField(MARKER_UINT32)),
    ('property', FixedDataPacketField(MARKER_UINT32)),
    ('type', FixedDataPacketField(MARKER_UINT32)),
    ('long_offset', FixedDataPacketField(MARKER_UINT32)),
    ('long_length', FixedDataPacketField(MARKER_UINT32)),
    ('delete', FixedDataPacketField(MARKER_UINT8)),
    ('pending', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
))


class GetProviderPropertyRequest:
    OPCODE = 41

    __slots__ = ('provider', 'property', 'type', 'long_offset', 'long_length', 'delete', 'pending',)

    def __init__(
            self, *,
            provider: Optional[int] = None,
            property: Optional[int] = None,
            type: Optional[int] = None,
            long_offset: Optional[int] = None,
            long_length: Optional[int] = None,
            delete: Optional[bool] = None,
            pending: Optional[bool] = None,
    ) -> None:
        self.provider = provider
        self.property = property
        self.type = type
        self.long_offset = long_offset
        self.long_length = long_length
        self.delete = delete
        self.pending = pending

    def as_dict(self) -> Dict[str, Any]:
        return {
            'provider': self.provider,
            'property': self.property,
            'type': self.type,
            'long_offset': self.long_offset,
            'long_length': self.long_length,
            'delete': self.delete,
            'pending': self.pending,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetProviderPropertyRequest':
        return GetProviderPropertyRequest(**GetProviderPropertyRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetProviderPropertyRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, bool, bool], GetProviderPropertyRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetProviderPropertyRequest.lib = library.randr_getproviderproperty
        GetProviderPropertyRequest.lib.restype = GetProviderPropertyRequestCookie
        GetProviderPropertyRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int8, ctypes.c_int8, ctypes.c_uint8 * 2)


class GetProviderPropertyRequestCType(ctypes.Structure):
    """randr GetProviderProperty"""
    _fields_ = [
        ("provider", ctypes.c_uint32),
        ("property", ctypes.c_uint32),
        ("type", ctypes.c_uint32),
        ("long_offset", ctypes.c_uint32),
        ("long_length", ctypes.c_uint32),
        ("delete", ctypes.c_int8),
        ("pending", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 2),
    ]


GetProviderPropertyReplyReplyPacket = DataPacket((
    ('format', FixedDataPacketField(MARKER_UINT8)),
    ('type', FixedDataPacketField(MARKER_UINT32)),
    ('bytes_after', FixedDataPacketField(MARKER_UINT32)),
    ('num_items', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: (d['num_items']) * ((d['format']) / (8)), 0)),
))


class GetProviderPropertyReplyReply:
    __slots__ = ('format', 'type', 'bytes_after', 'num_items', 'data',)

    def __init__(
            self, *,
            format: Optional[int] = None,
            type: Optional[int] = None,
            bytes_after: Optional[int] = None,
            num_items: Optional[int] = None,
            data: Optional[Sequence[None]] = None,
    ) -> None:
        self.format = format
        self.type = type
        self.bytes_after = bytes_after
        self.num_items = num_items
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'format': self.format,
            'type': self.type,
            'bytes_after': self.bytes_after,
            'num_items': self.num_items,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetProviderPropertyReplyReply':
        return GetProviderPropertyReplyReply(**GetProviderPropertyReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetProviderPropertyReplyReplyPacket.pack(**self.as_dict())


class GetProviderPropertyReplyReplyCType(ctypes.Structure):
    """randr GetProviderProperty_reply"""
    _fields_ = [
        ("format", ctypes.c_uint8),
        ("type", ctypes.c_uint32),
        ("bytes_after", ctypes.c_uint32),
        ("num_items", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


ScreenChangeNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('rotation', FixedDataPacketField(MARKER_UINT8)),
    ('timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('config_timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('root', FixedDataPacketField(MARKER_UINT32)),
    ('request_window', FixedDataPacketField(MARKER_UINT32)),
    ('sizeID', FixedDataPacketField(MARKER_UINT16)),
    ('subpixel_order', FixedDataPacketField(MARKER_UINT16)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('mwidth', FixedDataPacketField(MARKER_UINT16)),
    ('mheight', FixedDataPacketField(MARKER_UINT16)),
))


class ScreenChangeNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'rotation', 'timestamp', 'config_timestamp', 'root', 'request_window', 'sizeid', 'subpixel_order', 'width', 'height', 'mwidth', 'mheight',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            rotation: Optional[int] = None,
            timestamp: Optional[int] = None,
            config_timestamp: Optional[int] = None,
            root: Optional[int] = None,
            request_window: Optional[int] = None,
            sizeid: Optional[int] = None,
            subpixel_order: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            mwidth: Optional[int] = None,
            mheight: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.rotation = rotation
        self.timestamp = timestamp
        self.config_timestamp = config_timestamp
        self.root = root
        self.request_window = request_window
        self.sizeid = sizeid
        self.subpixel_order = subpixel_order
        self.width = width
        self.height = height
        self.mwidth = mwidth
        self.mheight = mheight

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'rotation': self.rotation,
            'timestamp': self.timestamp,
            'config_timestamp': self.config_timestamp,
            'root': self.root,
            'request_window': self.request_window,
            'sizeID': self.sizeid,
            'subpixel_order': self.subpixel_order,
            'width': self.width,
            'height': self.height,
            'mwidth': self.mwidth,
            'mheight': self.mheight,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ScreenChangeNotifyEvent':
        return ScreenChangeNotifyEvent(**ScreenChangeNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ScreenChangeNotifyEventPacket.pack(**self.as_dict())


class ScreenChangeNotifyEventCType(ctypes.Structure):
    """randr ScreenChangeNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("rotation", ctypes.c_uint8),
        ("timestamp", ctypes.c_uint32),
        ("config_timestamp", ctypes.c_uint32),
        ("root", ctypes.c_uint32),
        ("request_window", ctypes.c_uint32),
        ("sizeID", ctypes.c_uint16),
        ("subpixel_order", ctypes.c_uint16),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("mwidth", ctypes.c_uint16),
        ("mheight", ctypes.c_uint16),
    ]


CrtcChangeStructPacket = DataPacket((
    ('timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('crtc', FixedDataPacketField(MARKER_UINT32)),
    ('mode', FixedDataPacketField(MARKER_UINT32)),
    ('rotation', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
    ('x', FixedDataPacketField(MARKER_INT16)),
    ('y', FixedDataPacketField(MARKER_INT16)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
))


class CrtcChangeStruct:
    __slots__ = ('timestamp', 'window', 'crtc', 'mode', 'rotation', 'x', 'y', 'width', 'height',)

    def __init__(
            self, *,
            timestamp: Optional[int] = None,
            window: Optional[int] = None,
            crtc: Optional[int] = None,
            mode: Optional[int] = None,
            rotation: Optional[int] = None,
            x: Optional[int] = None,
            y: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
    ) -> None:
        self.timestamp = timestamp
        self.window = window
        self.crtc = crtc
        self.mode = mode
        self.rotation = rotation
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def as_dict(self) -> Dict[str, Any]:
        return {
            'timestamp': self.timestamp,
            'window': self.window,
            'crtc': self.crtc,
            'mode': self.mode,
            'rotation': self.rotation,
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CrtcChangeStruct':
        return CrtcChangeStruct(**CrtcChangeStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CrtcChangeStructPacket.pack(**self.as_dict())


class CrtcChangeStructCType(ctypes.Structure):
    """randr CrtcChange"""
    _fields_ = [
        ("timestamp", ctypes.c_uint32),
        ("window", ctypes.c_uint32),
        ("crtc", ctypes.c_uint32),
        ("mode", ctypes.c_uint32),
        ("rotation", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
        ("x", ctypes.c_int16),
        ("y", ctypes.c_int16),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
    ]


OutputChangeStructPacket = DataPacket((
    ('timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('config_timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('output', FixedDataPacketField(MARKER_UINT32)),
    ('crtc', FixedDataPacketField(MARKER_UINT32)),
    ('mode', FixedDataPacketField(MARKER_UINT32)),
    ('rotation', FixedDataPacketField(MARKER_UINT16)),
    ('connection', FixedDataPacketField(MARKER_UINT8)),
    ('subpixel_order', FixedDataPacketField(MARKER_UINT8)),
))


class OutputChangeStruct:
    __slots__ = ('timestamp', 'config_timestamp', 'window', 'output', 'crtc', 'mode', 'rotation', 'connection', 'subpixel_order',)

    def __init__(
            self, *,
            timestamp: Optional[int] = None,
            config_timestamp: Optional[int] = None,
            window: Optional[int] = None,
            output: Optional[int] = None,
            crtc: Optional[int] = None,
            mode: Optional[int] = None,
            rotation: Optional[int] = None,
            connection: Optional[int] = None,
            subpixel_order: Optional[int] = None,
    ) -> None:
        self.timestamp = timestamp
        self.config_timestamp = config_timestamp
        self.window = window
        self.output = output
        self.crtc = crtc
        self.mode = mode
        self.rotation = rotation
        self.connection = connection
        self.subpixel_order = subpixel_order

    def as_dict(self) -> Dict[str, Any]:
        return {
            'timestamp': self.timestamp,
            'config_timestamp': self.config_timestamp,
            'window': self.window,
            'output': self.output,
            'crtc': self.crtc,
            'mode': self.mode,
            'rotation': self.rotation,
            'connection': self.connection,
            'subpixel_order': self.subpixel_order,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'OutputChangeStruct':
        return OutputChangeStruct(**OutputChangeStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return OutputChangeStructPacket.pack(**self.as_dict())


class OutputChangeStructCType(ctypes.Structure):
    """randr OutputChange"""
    _fields_ = [
        ("timestamp", ctypes.c_uint32),
        ("config_timestamp", ctypes.c_uint32),
        ("window", ctypes.c_uint32),
        ("output", ctypes.c_uint32),
        ("crtc", ctypes.c_uint32),
        ("mode", ctypes.c_uint32),
        ("rotation", ctypes.c_uint16),
        ("connection", ctypes.c_uint8),
        ("subpixel_order", ctypes.c_uint8),
    ]


OutputPropertyStructPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('output', FixedDataPacketField(MARKER_UINT32)),
    ('atom', FixedDataPacketField(MARKER_UINT32)),
    ('timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('status', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(11)),
))


class OutputPropertyStruct:
    __slots__ = ('window', 'output', 'atom', 'timestamp', 'status',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            output: Optional[int] = None,
            atom: Optional[int] = None,
            timestamp: Optional[int] = None,
            status: Optional[int] = None,
    ) -> None:
        self.window = window
        self.output = output
        self.atom = atom
        self.timestamp = timestamp
        self.status = status

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'output': self.output,
            'atom': self.atom,
            'timestamp': self.timestamp,
            'status': self.status,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'OutputPropertyStruct':
        return OutputPropertyStruct(**OutputPropertyStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return OutputPropertyStructPacket.pack(**self.as_dict())


class OutputPropertyStructCType(ctypes.Structure):
    """randr OutputProperty"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("output", ctypes.c_uint32),
        ("atom", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint32),
        ("status", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 11),
    ]


ProviderChangeStructPacket = DataPacket((
    ('timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('provider', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(16)),
))


class ProviderChangeStruct:
    __slots__ = ('timestamp', 'window', 'provider',)

    def __init__(
            self, *,
            timestamp: Optional[int] = None,
            window: Optional[int] = None,
            provider: Optional[int] = None,
    ) -> None:
        self.timestamp = timestamp
        self.window = window
        self.provider = provider

    def as_dict(self) -> Dict[str, Any]:
        return {
            'timestamp': self.timestamp,
            'window': self.window,
            'provider': self.provider,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ProviderChangeStruct':
        return ProviderChangeStruct(**ProviderChangeStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ProviderChangeStructPacket.pack(**self.as_dict())


class ProviderChangeStructCType(ctypes.Structure):
    """randr ProviderChange"""
    _fields_ = [
        ("timestamp", ctypes.c_uint32),
        ("window", ctypes.c_uint32),
        ("provider", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 16),
    ]


ProviderPropertyStructPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('provider', FixedDataPacketField(MARKER_UINT32)),
    ('atom', FixedDataPacketField(MARKER_UINT32)),
    ('timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('state', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(11)),
))


class ProviderPropertyStruct:
    __slots__ = ('window', 'provider', 'atom', 'timestamp', 'state',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            provider: Optional[int] = None,
            atom: Optional[int] = None,
            timestamp: Optional[int] = None,
            state: Optional[int] = None,
    ) -> None:
        self.window = window
        self.provider = provider
        self.atom = atom
        self.timestamp = timestamp
        self.state = state

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'provider': self.provider,
            'atom': self.atom,
            'timestamp': self.timestamp,
            'state': self.state,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ProviderPropertyStruct':
        return ProviderPropertyStruct(**ProviderPropertyStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ProviderPropertyStructPacket.pack(**self.as_dict())


class ProviderPropertyStructCType(ctypes.Structure):
    """randr ProviderProperty"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("provider", ctypes.c_uint32),
        ("atom", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint32),
        ("state", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 11),
    ]


ResourceChangeStructPacket = DataPacket((
    ('timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(20)),
))


class ResourceChangeStruct:
    __slots__ = ('timestamp', 'window',)

    def __init__(
            self, *,
            timestamp: Optional[int] = None,
            window: Optional[int] = None,
    ) -> None:
        self.timestamp = timestamp
        self.window = window

    def as_dict(self) -> Dict[str, Any]:
        return {
            'timestamp': self.timestamp,
            'window': self.window,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ResourceChangeStruct':
        return ResourceChangeStruct(**ResourceChangeStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ResourceChangeStructPacket.pack(**self.as_dict())


class ResourceChangeStructCType(ctypes.Structure):
    """randr ResourceChange"""
    _fields_ = [
        ("timestamp", ctypes.c_uint32),
        ("window", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 20),
    ]


MonitorInfoStructPacket = DataPacket((
    ('name', FixedDataPacketField(MARKER_UINT32)),
    ('primary', FixedDataPacketField(MARKER_UINT8)),
    ('automatic', FixedDataPacketField(MARKER_UINT8)),
    ('nOutput', FixedDataPacketField(MARKER_UINT16)),
    ('x', FixedDataPacketField(MARKER_INT16)),
    ('y', FixedDataPacketField(MARKER_INT16)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('width_in_millimeters', FixedDataPacketField(MARKER_UINT32)),
    ('height_in_millimeters', FixedDataPacketField(MARKER_UINT32)),
    ('outputs', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nOutput'], 0)),
))


class MonitorInfoStruct:
    __slots__ = ('name', 'primary', 'automatic', 'noutput', 'x', 'y', 'width', 'height', 'width_in_millimeters', 'height_in_millimeters', 'outputs',)

    def __init__(
            self, *,
            name: Optional[int] = None,
            primary: Optional[bool] = None,
            automatic: Optional[bool] = None,
            noutput: Optional[int] = None,
            x: Optional[int] = None,
            y: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            width_in_millimeters: Optional[int] = None,
            height_in_millimeters: Optional[int] = None,
            outputs: Optional[Sequence[int]] = None,
    ) -> None:
        self.name = name
        self.primary = primary
        self.automatic = automatic
        self.noutput = noutput
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.width_in_millimeters = width_in_millimeters
        self.height_in_millimeters = height_in_millimeters
        self.outputs = outputs

    def as_dict(self) -> Dict[str, Any]:
        return {
            'name': self.name,
            'primary': self.primary,
            'automatic': self.automatic,
            'nOutput': self.noutput,
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height,
            'width_in_millimeters': self.width_in_millimeters,
            'height_in_millimeters': self.height_in_millimeters,
            'outputs': self.outputs,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'MonitorInfoStruct':
        return MonitorInfoStruct(**MonitorInfoStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return MonitorInfoStructPacket.pack(**self.as_dict())


class MonitorInfoStructCType(ctypes.Structure):
    """randr MonitorInfo"""
    _fields_ = [
        ("name", ctypes.c_uint32),
        ("primary", ctypes.c_int8),
        ("automatic", ctypes.c_int8),
        ("nOutput", ctypes.c_uint16),
        ("x", ctypes.c_int16),
        ("y", ctypes.c_int16),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("width_in_millimeters", ctypes.c_uint32),
        ("height_in_millimeters", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


GetMonitorsRequestCookie = NewType('GetMonitorsRequestCookie', ctypes.c_uint32)


GetMonitorsRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('get_active', FixedDataPacketField(MARKER_UINT8)),
))


class GetMonitorsRequest:
    OPCODE = 42

    __slots__ = ('window', 'get_active',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            get_active: Optional[bool] = None,
    ) -> None:
        self.window = window
        self.get_active = get_active

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'get_active': self.get_active,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetMonitorsRequest':
        return GetMonitorsRequest(**GetMonitorsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetMonitorsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, bool], GetMonitorsRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetMonitorsRequest.lib = library.randr_getmonitors
        GetMonitorsRequest.lib.restype = GetMonitorsRequestCookie
        GetMonitorsRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_int8)


class GetMonitorsRequestCType(ctypes.Structure):
    """randr GetMonitors"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("get_active", ctypes.c_int8),
    ]


GetMonitorsReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('nMonitors', FixedDataPacketField(MARKER_UINT32)),
    ('nOutputs', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(12)),
    ('monitors', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nMonitors'], 0)),
))


class GetMonitorsReplyReply:
    __slots__ = ('timestamp', 'nmonitors', 'noutputs', 'monitors',)

    def __init__(
            self, *,
            timestamp: Optional[int] = None,
            nmonitors: Optional[int] = None,
            noutputs: Optional[int] = None,
            monitors: Optional[Sequence[int]] = None,
    ) -> None:
        self.timestamp = timestamp
        self.nmonitors = nmonitors
        self.noutputs = noutputs
        self.monitors = monitors

    def as_dict(self) -> Dict[str, Any]:
        return {
            'timestamp': self.timestamp,
            'nMonitors': self.nmonitors,
            'nOutputs': self.noutputs,
            'monitors': self.monitors,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetMonitorsReplyReply':
        return GetMonitorsReplyReply(**GetMonitorsReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetMonitorsReplyReplyPacket.pack(**self.as_dict())


class GetMonitorsReplyReplyCType(ctypes.Structure):
    """randr GetMonitors_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("timestamp", ctypes.c_uint32),
        ("nMonitors", ctypes.c_uint32),
        ("nOutputs", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


SetMonitorRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('monitorinfo', FixedDataPacketField(MARKER_UINT32)),
))


class SetMonitorRequest:
    OPCODE = 43

    __slots__ = ('window', 'monitorinfo',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            monitorinfo: Optional[int] = None,
    ) -> None:
        self.window = window
        self.monitorinfo = monitorinfo

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'monitorinfo': self.monitorinfo,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetMonitorRequest':
        return SetMonitorRequest(**SetMonitorRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetMonitorRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetMonitorRequest.lib = library.randr_setmonitor
        SetMonitorRequest.lib.restype = ctypes.c_uint32
        SetMonitorRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class SetMonitorRequestCType(ctypes.Structure):
    """randr SetMonitor"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("monitorinfo", ctypes.c_uint32),
    ]


DeleteMonitorRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('name', FixedDataPacketField(MARKER_UINT32)),
))


class DeleteMonitorRequest:
    OPCODE = 44

    __slots__ = ('window', 'name',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            name: Optional[int] = None,
    ) -> None:
        self.window = window
        self.name = name

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'name': self.name,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeleteMonitorRequest':
        return DeleteMonitorRequest(**DeleteMonitorRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeleteMonitorRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        DeleteMonitorRequest.lib = library.randr_deletemonitor
        DeleteMonitorRequest.lib.restype = ctypes.c_uint32
        DeleteMonitorRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class DeleteMonitorRequestCType(ctypes.Structure):
    """randr DeleteMonitor"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("name", ctypes.c_uint32),
    ]


CreateLeaseRequestCookie = NewType('CreateLeaseRequestCookie', ctypes.c_uint32)


CreateLeaseRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('lid', FixedDataPacketField(MARKER_UINT32)),
    ('num_crtcs', FixedDataPacketField(MARKER_UINT16)),
    ('num_outputs', FixedDataPacketField(MARKER_UINT16)),
    ('crtcs', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_crtcs'], 0)),
    ('outputs', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_outputs'], 0)),
))


class CreateLeaseRequest:
    OPCODE = 45

    __slots__ = ('window', 'lid', 'num_crtcs', 'num_outputs', 'crtcs', 'outputs',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            lid: Optional[int] = None,
            num_crtcs: Optional[int] = None,
            num_outputs: Optional[int] = None,
            crtcs: Optional[Sequence[int]] = None,
            outputs: Optional[Sequence[int]] = None,
    ) -> None:
        self.window = window
        self.lid = lid
        self.num_crtcs = num_crtcs
        self.num_outputs = num_outputs
        self.crtcs = crtcs
        self.outputs = outputs

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'lid': self.lid,
            'num_crtcs': self.num_crtcs,
            'num_outputs': self.num_outputs,
            'crtcs': self.crtcs,
            'outputs': self.outputs,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateLeaseRequest':
        return CreateLeaseRequest(**CreateLeaseRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateLeaseRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, Sequence[int], Sequence[int]], CreateLeaseRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateLeaseRequest.lib = library.randr_createlease
        CreateLeaseRequest.lib.restype = CreateLeaseRequestCookie
        CreateLeaseRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_void_p, ctypes.c_void_p)


class CreateLeaseRequestCType(ctypes.Structure):
    """randr CreateLease"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("lid", ctypes.c_uint32),
        ("num_crtcs", ctypes.c_uint16),
        ("num_outputs", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


CreateLeaseReplyReplyPacket = DataPacket((
    ('nfd', FixedDataPacketField(MARKER_UINT8)),
    ('master_fd', FixedDataPacketField(file_descriptor)),
    ('pad0', FixedPadDataPacketField(24)),
))


class CreateLeaseReplyReply:
    __slots__ = ('nfd', 'master_fd',)

    def __init__(
            self, *,
            nfd: Optional[int] = None,
            master_fd: Optional[int] = None,
    ) -> None:
        self.nfd = nfd
        self.master_fd = master_fd

    def as_dict(self) -> Dict[str, Any]:
        return {
            'nfd': self.nfd,
            'master_fd': self.master_fd,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateLeaseReplyReply':
        return CreateLeaseReplyReply(**CreateLeaseReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateLeaseReplyReplyPacket.pack(**self.as_dict())


class CreateLeaseReplyReplyCType(ctypes.Structure):
    """randr CreateLease_reply"""
    _fields_ = [
        ("nfd", ctypes.c_uint8),
        ("master_fd", ctypes.c_int32),
        ("pad0", ctypes.c_uint8 * 24),
    ]


FreeLeaseRequestPacket = DataPacket((
    ('lid', FixedDataPacketField(MARKER_UINT32)),
    ('terminate', FixedDataPacketField(MARKER_INT8)),
))


class FreeLeaseRequest:
    OPCODE = 46

    __slots__ = ('lid', 'terminate',)

    def __init__(
            self, *,
            lid: Optional[int] = None,
            terminate: Optional[int] = None,
    ) -> None:
        self.lid = lid
        self.terminate = terminate

    def as_dict(self) -> Dict[str, Any]:
        return {
            'lid': self.lid,
            'terminate': self.terminate,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'FreeLeaseRequest':
        return FreeLeaseRequest(**FreeLeaseRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return FreeLeaseRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        FreeLeaseRequest.lib = library.randr_freelease
        FreeLeaseRequest.lib.restype = ctypes.c_uint32
        FreeLeaseRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_int8)


class FreeLeaseRequestCType(ctypes.Structure):
    """randr FreeLease"""
    _fields_ = [
        ("lid", ctypes.c_uint32),
        ("terminate", ctypes.c_int8),
    ]


LeaseNotifyStructPacket = DataPacket((
    ('timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('lease', FixedDataPacketField(MARKER_UINT32)),
    ('created', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(15)),
))


class LeaseNotifyStruct:
    __slots__ = ('timestamp', 'window', 'lease', 'created',)

    def __init__(
            self, *,
            timestamp: Optional[int] = None,
            window: Optional[int] = None,
            lease: Optional[int] = None,
            created: Optional[int] = None,
    ) -> None:
        self.timestamp = timestamp
        self.window = window
        self.lease = lease
        self.created = created

    def as_dict(self) -> Dict[str, Any]:
        return {
            'timestamp': self.timestamp,
            'window': self.window,
            'lease': self.lease,
            'created': self.created,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'LeaseNotifyStruct':
        return LeaseNotifyStruct(**LeaseNotifyStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return LeaseNotifyStructPacket.pack(**self.as_dict())


class LeaseNotifyStructCType(ctypes.Structure):
    """randr LeaseNotify"""
    _fields_ = [
        ("timestamp", ctypes.c_uint32),
        ("window", ctypes.c_uint32),
        ("lease", ctypes.c_uint32),
        ("created", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 15),
    ]


NotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('subCode', FixedDataPacketField(MARKER_UINT8)),
    ('u', FixedDataPacketField(MARKER_UINT32)),
))


class NotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'subcode', 'u',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            subcode: Optional[int] = None,
            u: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.subcode = subcode
        self.u = u

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'subCode': self.subcode,
            'u': self.u,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'NotifyEvent':
        return NotifyEvent(**NotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return NotifyEventPacket.pack(**self.as_dict())


class NotifyEventCType(ctypes.Structure):
    """randr Notify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("subCode", ctypes.c_uint8),
        ("u", ctypes.c_uint32),
    ]


# ------------------------------------------------------------------
# Unions

NotifyDataUnion = {
    'cc': DataPacket((
        ('cc', FixedDataPacketField(MARKER_UINT32)),
    )),
    'oc': DataPacket((
        ('oc', FixedDataPacketField(MARKER_UINT32)),
    )),
    'op': DataPacket((
        ('op', FixedDataPacketField(MARKER_UINT32)),
    )),
    'pc': DataPacket((
        ('pc', FixedDataPacketField(MARKER_UINT32)),
    )),
    'pp': DataPacket((
        ('pp', FixedDataPacketField(MARKER_UINT32)),
    )),
    'rc': DataPacket((
        ('rc', FixedDataPacketField(MARKER_UINT32)),
    )),
    'lc': DataPacket((
        ('lc', FixedDataPacketField(MARKER_UINT32)),
    )),
}

