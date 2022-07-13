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

ModeFlagType = NewType('ModeFlagType', int)


class ModeFlagValues:
    POSITIVE_HSYNC = ModeFlagType(1)
    NEGATIVE_HSYNC = ModeFlagType(2)
    POSITIVE_VSYNC = ModeFlagType(4)
    NEGATIVE_VSYNC = ModeFlagType(8)
    INTERLACE = ModeFlagType(16)
    COMPOSITE_SYNC = ModeFlagType(32)
    POSITIVE_CSYNC = ModeFlagType(64)
    NEGATIVE_CSYNC = ModeFlagType(128)
    HSKEW = ModeFlagType(256)
    BROADCAST = ModeFlagType(512)
    PIXMUX = ModeFlagType(1024)
    DOUBLE_CLOCK = ModeFlagType(2048)
    HALF_CLOCK = ModeFlagType(4096)


ClockFlagType = NewType('ClockFlagType', int)


class ClockFlagValues:
    PROGRAMABLE = ClockFlagType(1)


PermissionType = NewType('PermissionType', int)


class PermissionValues:
    READ = PermissionType(1)
    WRITE = PermissionType(2)


# ------------------------------------------------------------------
# Aliases



# ------------------------------------------------------------------
# Structures, Events, Requests, Replies


ModeInfoStructPacket = DataPacket((
    ('dotclock', FixedDataPacketField(MARKER_UINT32)),
    ('hdisplay', FixedDataPacketField(MARKER_UINT16)),
    ('hsyncstart', FixedDataPacketField(MARKER_UINT16)),
    ('hsyncend', FixedDataPacketField(MARKER_UINT16)),
    ('htotal', FixedDataPacketField(MARKER_UINT16)),
    ('hskew', FixedDataPacketField(MARKER_UINT32)),
    ('vdisplay', FixedDataPacketField(MARKER_UINT16)),
    ('vsyncstart', FixedDataPacketField(MARKER_UINT16)),
    ('vsyncend', FixedDataPacketField(MARKER_UINT16)),
    ('vtotal', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(4)),
    ('flags', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(12)),
    ('privsize', FixedDataPacketField(MARKER_UINT32)),
))


class ModeInfoStruct:
    __slots__ = ('dotclock', 'hdisplay', 'hsyncstart', 'hsyncend', 'htotal', 'hskew', 'vdisplay', 'vsyncstart', 'vsyncend', 'vtotal', 'flags', 'privsize',)

    def __init__(
            self, *,
            dotclock: Optional[int] = None,
            hdisplay: Optional[int] = None,
            hsyncstart: Optional[int] = None,
            hsyncend: Optional[int] = None,
            htotal: Optional[int] = None,
            hskew: Optional[int] = None,
            vdisplay: Optional[int] = None,
            vsyncstart: Optional[int] = None,
            vsyncend: Optional[int] = None,
            vtotal: Optional[int] = None,
            flags: Optional[int] = None,
            privsize: Optional[int] = None,
    ) -> None:
        self.dotclock = dotclock
        self.hdisplay = hdisplay
        self.hsyncstart = hsyncstart
        self.hsyncend = hsyncend
        self.htotal = htotal
        self.hskew = hskew
        self.vdisplay = vdisplay
        self.vsyncstart = vsyncstart
        self.vsyncend = vsyncend
        self.vtotal = vtotal
        self.flags = flags
        self.privsize = privsize

    def as_dict(self) -> Dict[str, Any]:
        return {
            'dotclock': self.dotclock,
            'hdisplay': self.hdisplay,
            'hsyncstart': self.hsyncstart,
            'hsyncend': self.hsyncend,
            'htotal': self.htotal,
            'hskew': self.hskew,
            'vdisplay': self.vdisplay,
            'vsyncstart': self.vsyncstart,
            'vsyncend': self.vsyncend,
            'vtotal': self.vtotal,
            'flags': self.flags,
            'privsize': self.privsize,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ModeInfoStruct':
        return ModeInfoStruct(**ModeInfoStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ModeInfoStructPacket.pack(**self.as_dict())


class ModeInfoStructCType(ctypes.Structure):
    """xf86vidmode ModeInfo"""
    _fields_ = [
        ("dotclock", ctypes.c_uint32),
        ("hdisplay", ctypes.c_uint16),
        ("hsyncstart", ctypes.c_uint16),
        ("hsyncend", ctypes.c_uint16),
        ("htotal", ctypes.c_uint16),
        ("hskew", ctypes.c_uint32),
        ("vdisplay", ctypes.c_uint16),
        ("vsyncstart", ctypes.c_uint16),
        ("vsyncend", ctypes.c_uint16),
        ("vtotal", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 4),
        ("flags", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 12),
        ("privsize", ctypes.c_uint32),
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
        QueryVersionRequest.lib = library.xf86vidmode_queryversion
        QueryVersionRequest.lib.restype = QueryVersionRequestCookie
        QueryVersionRequest.lib.argstype = ()


class QueryVersionRequestCType(ctypes.Structure):
    """xf86vidmode QueryVersion"""
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
    """xf86vidmode QueryVersion_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("major_version", ctypes.c_uint16),
        ("minor_version", ctypes.c_uint16),
    ]


GetModeLineRequestCookie = NewType('GetModeLineRequestCookie', ctypes.c_uint32)


GetModeLineRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
))


class GetModeLineRequest:
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
    def from_data(inp: BinaryIO) -> 'GetModeLineRequest':
        return GetModeLineRequest(**GetModeLineRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetModeLineRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetModeLineRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetModeLineRequest.lib = library.xf86vidmode_getmodeline
        GetModeLineRequest.lib.restype = GetModeLineRequestCookie
        GetModeLineRequest.lib.argstype = (ctypes.c_uint16, ctypes.c_uint8 * 2)


class GetModeLineRequestCType(ctypes.Structure):
    """xf86vidmode GetModeLine"""
    _fields_ = [
        ("screen", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
    ]


GetModeLineReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('dotclock', FixedDataPacketField(MARKER_UINT32)),
    ('hdisplay', FixedDataPacketField(MARKER_UINT16)),
    ('hsyncstart', FixedDataPacketField(MARKER_UINT16)),
    ('hsyncend', FixedDataPacketField(MARKER_UINT16)),
    ('htotal', FixedDataPacketField(MARKER_UINT16)),
    ('hskew', FixedDataPacketField(MARKER_UINT16)),
    ('vdisplay', FixedDataPacketField(MARKER_UINT16)),
    ('vsyncstart', FixedDataPacketField(MARKER_UINT16)),
    ('vsyncend', FixedDataPacketField(MARKER_UINT16)),
    ('vtotal', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(2)),
    ('flags', FixedDataPacketField(MARKER_UINT32)),
    ('pad2', FixedPadDataPacketField(12)),
    ('privsize', FixedDataPacketField(MARKER_UINT32)),
    ('private', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: d['privsize'], 0)),
))


class GetModeLineReplyReply:
    __slots__ = ('dotclock', 'hdisplay', 'hsyncstart', 'hsyncend', 'htotal', 'hskew', 'vdisplay', 'vsyncstart', 'vsyncend', 'vtotal', 'flags', 'privsize', 'private',)

    def __init__(
            self, *,
            dotclock: Optional[int] = None,
            hdisplay: Optional[int] = None,
            hsyncstart: Optional[int] = None,
            hsyncend: Optional[int] = None,
            htotal: Optional[int] = None,
            hskew: Optional[int] = None,
            vdisplay: Optional[int] = None,
            vsyncstart: Optional[int] = None,
            vsyncend: Optional[int] = None,
            vtotal: Optional[int] = None,
            flags: Optional[int] = None,
            privsize: Optional[int] = None,
            private: Optional[Sequence[int]] = None,
    ) -> None:
        self.dotclock = dotclock
        self.hdisplay = hdisplay
        self.hsyncstart = hsyncstart
        self.hsyncend = hsyncend
        self.htotal = htotal
        self.hskew = hskew
        self.vdisplay = vdisplay
        self.vsyncstart = vsyncstart
        self.vsyncend = vsyncend
        self.vtotal = vtotal
        self.flags = flags
        self.privsize = privsize
        self.private = private

    def as_dict(self) -> Dict[str, Any]:
        return {
            'dotclock': self.dotclock,
            'hdisplay': self.hdisplay,
            'hsyncstart': self.hsyncstart,
            'hsyncend': self.hsyncend,
            'htotal': self.htotal,
            'hskew': self.hskew,
            'vdisplay': self.vdisplay,
            'vsyncstart': self.vsyncstart,
            'vsyncend': self.vsyncend,
            'vtotal': self.vtotal,
            'flags': self.flags,
            'privsize': self.privsize,
            'private': self.private,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetModeLineReplyReply':
        return GetModeLineReplyReply(**GetModeLineReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetModeLineReplyReplyPacket.pack(**self.as_dict())


class GetModeLineReplyReplyCType(ctypes.Structure):
    """xf86vidmode GetModeLine_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("dotclock", ctypes.c_uint32),
        ("hdisplay", ctypes.c_uint16),
        ("hsyncstart", ctypes.c_uint16),
        ("hsyncend", ctypes.c_uint16),
        ("htotal", ctypes.c_uint16),
        ("hskew", ctypes.c_uint16),
        ("vdisplay", ctypes.c_uint16),
        ("vsyncstart", ctypes.c_uint16),
        ("vsyncend", ctypes.c_uint16),
        ("vtotal", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 2),
        ("flags", ctypes.c_uint32),
        ("pad2", ctypes.c_uint8 * 12),
        ("privsize", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


ModModeLineRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT32)),
    ('hdisplay', FixedDataPacketField(MARKER_UINT16)),
    ('hsyncstart', FixedDataPacketField(MARKER_UINT16)),
    ('hsyncend', FixedDataPacketField(MARKER_UINT16)),
    ('htotal', FixedDataPacketField(MARKER_UINT16)),
    ('hskew', FixedDataPacketField(MARKER_UINT16)),
    ('vdisplay', FixedDataPacketField(MARKER_UINT16)),
    ('vsyncstart', FixedDataPacketField(MARKER_UINT16)),
    ('vsyncend', FixedDataPacketField(MARKER_UINT16)),
    ('vtotal', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
    ('flags', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(12)),
    ('privsize', FixedDataPacketField(MARKER_UINT32)),
    ('private', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: d['privsize'], 0)),
))


class ModModeLineRequest:
    OPCODE = 2

    __slots__ = ('screen', 'hdisplay', 'hsyncstart', 'hsyncend', 'htotal', 'hskew', 'vdisplay', 'vsyncstart', 'vsyncend', 'vtotal', 'flags', 'privsize', 'private',)

    def __init__(
            self, *,
            screen: Optional[int] = None,
            hdisplay: Optional[int] = None,
            hsyncstart: Optional[int] = None,
            hsyncend: Optional[int] = None,
            htotal: Optional[int] = None,
            hskew: Optional[int] = None,
            vdisplay: Optional[int] = None,
            vsyncstart: Optional[int] = None,
            vsyncend: Optional[int] = None,
            vtotal: Optional[int] = None,
            flags: Optional[int] = None,
            privsize: Optional[int] = None,
            private: Optional[Sequence[int]] = None,
    ) -> None:
        self.screen = screen
        self.hdisplay = hdisplay
        self.hsyncstart = hsyncstart
        self.hsyncend = hsyncend
        self.htotal = htotal
        self.hskew = hskew
        self.vdisplay = vdisplay
        self.vsyncstart = vsyncstart
        self.vsyncend = vsyncend
        self.vtotal = vtotal
        self.flags = flags
        self.privsize = privsize
        self.private = private

    def as_dict(self) -> Dict[str, Any]:
        return {
            'screen': self.screen,
            'hdisplay': self.hdisplay,
            'hsyncstart': self.hsyncstart,
            'hsyncend': self.hsyncend,
            'htotal': self.htotal,
            'hskew': self.hskew,
            'vdisplay': self.vdisplay,
            'vsyncstart': self.vsyncstart,
            'vsyncend': self.vsyncend,
            'vtotal': self.vtotal,
            'flags': self.flags,
            'privsize': self.privsize,
            'private': self.private,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ModModeLineRequest':
        return ModModeLineRequest(**ModModeLineRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ModModeLineRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, int, int, int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ModModeLineRequest.lib = library.xf86vidmode_modmodeline
        ModModeLineRequest.lib.restype = ctypes.c_uint32
        ModModeLineRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint8 * 2, ctypes.c_uint32, ctypes.c_uint8 * 12, ctypes.c_uint32, ctypes.c_void_p)


class ModModeLineRequestCType(ctypes.Structure):
    """xf86vidmode ModModeLine"""
    _fields_ = [
        ("screen", ctypes.c_uint32),
        ("hdisplay", ctypes.c_uint16),
        ("hsyncstart", ctypes.c_uint16),
        ("hsyncend", ctypes.c_uint16),
        ("htotal", ctypes.c_uint16),
        ("hskew", ctypes.c_uint16),
        ("vdisplay", ctypes.c_uint16),
        ("vsyncstart", ctypes.c_uint16),
        ("vsyncend", ctypes.c_uint16),
        ("vtotal", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
        ("flags", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 12),
        ("privsize", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


SwitchModeRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT16)),
    ('zoom', FixedDataPacketField(MARKER_UINT16)),
))


class SwitchModeRequest:
    OPCODE = 3

    __slots__ = ('screen', 'zoom',)

    def __init__(
            self, *,
            screen: Optional[int] = None,
            zoom: Optional[int] = None,
    ) -> None:
        self.screen = screen
        self.zoom = zoom

    def as_dict(self) -> Dict[str, Any]:
        return {
            'screen': self.screen,
            'zoom': self.zoom,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SwitchModeRequest':
        return SwitchModeRequest(**SwitchModeRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SwitchModeRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SwitchModeRequest.lib = library.xf86vidmode_switchmode
        SwitchModeRequest.lib.restype = ctypes.c_uint32
        SwitchModeRequest.lib.argstype = (ctypes.c_uint16, ctypes.c_uint16)


class SwitchModeRequestCType(ctypes.Structure):
    """xf86vidmode SwitchMode"""
    _fields_ = [
        ("screen", ctypes.c_uint16),
        ("zoom", ctypes.c_uint16),
    ]


GetMonitorRequestCookie = NewType('GetMonitorRequestCookie', ctypes.c_uint32)


GetMonitorRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
))


class GetMonitorRequest:
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
    def from_data(inp: BinaryIO) -> 'GetMonitorRequest':
        return GetMonitorRequest(**GetMonitorRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetMonitorRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetMonitorRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetMonitorRequest.lib = library.xf86vidmode_getmonitor
        GetMonitorRequest.lib.restype = GetMonitorRequestCookie
        GetMonitorRequest.lib.argstype = (ctypes.c_uint16, ctypes.c_uint8 * 2)


class GetMonitorRequestCType(ctypes.Structure):
    """xf86vidmode GetMonitor"""
    _fields_ = [
        ("screen", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
    ]


GetMonitorReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('vendor_length', FixedDataPacketField(MARKER_UINT8)),
    ('model_length', FixedDataPacketField(MARKER_UINT8)),
    ('num_hsync', FixedDataPacketField(MARKER_UINT8)),
    ('num_vsync', FixedDataPacketField(MARKER_UINT8)),
    ('pad1', FixedPadDataPacketField(20)),
    ('hsync', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_hsync'], 0)),
    ('vsync', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_vsync'], 0)),
    ('vendor', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['vendor_length'], 0)),
    ('alignment_pad', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: (((d['vendor_length']) + (3)) & (~(3))) - (d['vendor_length']), 0)),
    ('model', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['model_length'], 0)),
))


class GetMonitorReplyReply:
    __slots__ = ('vendor_length', 'model_length', 'num_hsync', 'num_vsync', 'hsync', 'vsync', 'vendor', 'alignment_pad', 'model',)

    def __init__(
            self, *,
            vendor_length: Optional[int] = None,
            model_length: Optional[int] = None,
            num_hsync: Optional[int] = None,
            num_vsync: Optional[int] = None,
            hsync: Optional[Sequence[int]] = None,
            vsync: Optional[Sequence[int]] = None,
            vendor: Optional[Sequence[int]] = None,
            alignment_pad: Optional[Sequence[None]] = None,
            model: Optional[Sequence[int]] = None,
    ) -> None:
        self.vendor_length = vendor_length
        self.model_length = model_length
        self.num_hsync = num_hsync
        self.num_vsync = num_vsync
        self.hsync = hsync
        self.vsync = vsync
        self.vendor = vendor
        self.alignment_pad = alignment_pad
        self.model = model

    def as_dict(self) -> Dict[str, Any]:
        return {
            'vendor_length': self.vendor_length,
            'model_length': self.model_length,
            'num_hsync': self.num_hsync,
            'num_vsync': self.num_vsync,
            'hsync': self.hsync,
            'vsync': self.vsync,
            'vendor': self.vendor,
            'alignment_pad': self.alignment_pad,
            'model': self.model,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetMonitorReplyReply':
        return GetMonitorReplyReply(**GetMonitorReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetMonitorReplyReplyPacket.pack(**self.as_dict())


class GetMonitorReplyReplyCType(ctypes.Structure):
    """xf86vidmode GetMonitor_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("vendor_length", ctypes.c_uint8),
        ("model_length", ctypes.c_uint8),
        ("num_hsync", ctypes.c_uint8),
        ("num_vsync", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


LockModeSwitchRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT16)),
    ('lock', FixedDataPacketField(MARKER_UINT16)),
))


class LockModeSwitchRequest:
    OPCODE = 5

    __slots__ = ('screen', 'lock',)

    def __init__(
            self, *,
            screen: Optional[int] = None,
            lock: Optional[int] = None,
    ) -> None:
        self.screen = screen
        self.lock = lock

    def as_dict(self) -> Dict[str, Any]:
        return {
            'screen': self.screen,
            'lock': self.lock,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'LockModeSwitchRequest':
        return LockModeSwitchRequest(**LockModeSwitchRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return LockModeSwitchRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        LockModeSwitchRequest.lib = library.xf86vidmode_lockmodeswitch
        LockModeSwitchRequest.lib.restype = ctypes.c_uint32
        LockModeSwitchRequest.lib.argstype = (ctypes.c_uint16, ctypes.c_uint16)


class LockModeSwitchRequestCType(ctypes.Structure):
    """xf86vidmode LockModeSwitch"""
    _fields_ = [
        ("screen", ctypes.c_uint16),
        ("lock", ctypes.c_uint16),
    ]


GetAllModeLinesRequestCookie = NewType('GetAllModeLinesRequestCookie', ctypes.c_uint32)


GetAllModeLinesRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
))


class GetAllModeLinesRequest:
    OPCODE = 6

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
    def from_data(inp: BinaryIO) -> 'GetAllModeLinesRequest':
        return GetAllModeLinesRequest(**GetAllModeLinesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetAllModeLinesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetAllModeLinesRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetAllModeLinesRequest.lib = library.xf86vidmode_getallmodelines
        GetAllModeLinesRequest.lib.restype = GetAllModeLinesRequestCookie
        GetAllModeLinesRequest.lib.argstype = (ctypes.c_uint16, ctypes.c_uint8 * 2)


class GetAllModeLinesRequestCType(ctypes.Structure):
    """xf86vidmode GetAllModeLines"""
    _fields_ = [
        ("screen", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
    ]


GetAllModeLinesReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('modecount', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('modeinfo', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['modecount'], 0)),
))


class GetAllModeLinesReplyReply:
    __slots__ = ('modecount', 'modeinfo',)

    def __init__(
            self, *,
            modecount: Optional[int] = None,
            modeinfo: Optional[Sequence[int]] = None,
    ) -> None:
        self.modecount = modecount
        self.modeinfo = modeinfo

    def as_dict(self) -> Dict[str, Any]:
        return {
            'modecount': self.modecount,
            'modeinfo': self.modeinfo,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetAllModeLinesReplyReply':
        return GetAllModeLinesReplyReply(**GetAllModeLinesReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetAllModeLinesReplyReplyPacket.pack(**self.as_dict())


class GetAllModeLinesReplyReplyCType(ctypes.Structure):
    """xf86vidmode GetAllModeLines_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("modecount", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


AddModeLineRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT32)),
    ('dotclock', FixedDataPacketField(MARKER_UINT32)),
    ('hdisplay', FixedDataPacketField(MARKER_UINT16)),
    ('hsyncstart', FixedDataPacketField(MARKER_UINT16)),
    ('hsyncend', FixedDataPacketField(MARKER_UINT16)),
    ('htotal', FixedDataPacketField(MARKER_UINT16)),
    ('hskew', FixedDataPacketField(MARKER_UINT16)),
    ('vdisplay', FixedDataPacketField(MARKER_UINT16)),
    ('vsyncstart', FixedDataPacketField(MARKER_UINT16)),
    ('vsyncend', FixedDataPacketField(MARKER_UINT16)),
    ('vtotal', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
    ('flags', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(12)),
    ('privsize', FixedDataPacketField(MARKER_UINT32)),
    ('after_dotclock', FixedDataPacketField(MARKER_UINT32)),
    ('after_hdisplay', FixedDataPacketField(MARKER_UINT16)),
    ('after_hsyncstart', FixedDataPacketField(MARKER_UINT16)),
    ('after_hsyncend', FixedDataPacketField(MARKER_UINT16)),
    ('after_htotal', FixedDataPacketField(MARKER_UINT16)),
    ('after_hskew', FixedDataPacketField(MARKER_UINT16)),
    ('after_vdisplay', FixedDataPacketField(MARKER_UINT16)),
    ('after_vsyncstart', FixedDataPacketField(MARKER_UINT16)),
    ('after_vsyncend', FixedDataPacketField(MARKER_UINT16)),
    ('after_vtotal', FixedDataPacketField(MARKER_UINT16)),
    ('pad2', FixedPadDataPacketField(2)),
    ('after_flags', FixedDataPacketField(MARKER_UINT32)),
    ('pad3', FixedPadDataPacketField(12)),
    ('private', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: d['privsize'], 0)),
))


class AddModeLineRequest:
    OPCODE = 7

    __slots__ = ('screen', 'dotclock', 'hdisplay', 'hsyncstart', 'hsyncend', 'htotal', 'hskew', 'vdisplay', 'vsyncstart', 'vsyncend', 'vtotal', 'flags', 'privsize', 'after_dotclock', 'after_hdisplay', 'after_hsyncstart', 'after_hsyncend', 'after_htotal', 'after_hskew', 'after_vdisplay', 'after_vsyncstart', 'after_vsyncend', 'after_vtotal', 'after_flags', 'private',)

    def __init__(
            self, *,
            screen: Optional[int] = None,
            dotclock: Optional[int] = None,
            hdisplay: Optional[int] = None,
            hsyncstart: Optional[int] = None,
            hsyncend: Optional[int] = None,
            htotal: Optional[int] = None,
            hskew: Optional[int] = None,
            vdisplay: Optional[int] = None,
            vsyncstart: Optional[int] = None,
            vsyncend: Optional[int] = None,
            vtotal: Optional[int] = None,
            flags: Optional[int] = None,
            privsize: Optional[int] = None,
            after_dotclock: Optional[int] = None,
            after_hdisplay: Optional[int] = None,
            after_hsyncstart: Optional[int] = None,
            after_hsyncend: Optional[int] = None,
            after_htotal: Optional[int] = None,
            after_hskew: Optional[int] = None,
            after_vdisplay: Optional[int] = None,
            after_vsyncstart: Optional[int] = None,
            after_vsyncend: Optional[int] = None,
            after_vtotal: Optional[int] = None,
            after_flags: Optional[int] = None,
            private: Optional[Sequence[int]] = None,
    ) -> None:
        self.screen = screen
        self.dotclock = dotclock
        self.hdisplay = hdisplay
        self.hsyncstart = hsyncstart
        self.hsyncend = hsyncend
        self.htotal = htotal
        self.hskew = hskew
        self.vdisplay = vdisplay
        self.vsyncstart = vsyncstart
        self.vsyncend = vsyncend
        self.vtotal = vtotal
        self.flags = flags
        self.privsize = privsize
        self.after_dotclock = after_dotclock
        self.after_hdisplay = after_hdisplay
        self.after_hsyncstart = after_hsyncstart
        self.after_hsyncend = after_hsyncend
        self.after_htotal = after_htotal
        self.after_hskew = after_hskew
        self.after_vdisplay = after_vdisplay
        self.after_vsyncstart = after_vsyncstart
        self.after_vsyncend = after_vsyncend
        self.after_vtotal = after_vtotal
        self.after_flags = after_flags
        self.private = private

    def as_dict(self) -> Dict[str, Any]:
        return {
            'screen': self.screen,
            'dotclock': self.dotclock,
            'hdisplay': self.hdisplay,
            'hsyncstart': self.hsyncstart,
            'hsyncend': self.hsyncend,
            'htotal': self.htotal,
            'hskew': self.hskew,
            'vdisplay': self.vdisplay,
            'vsyncstart': self.vsyncstart,
            'vsyncend': self.vsyncend,
            'vtotal': self.vtotal,
            'flags': self.flags,
            'privsize': self.privsize,
            'after_dotclock': self.after_dotclock,
            'after_hdisplay': self.after_hdisplay,
            'after_hsyncstart': self.after_hsyncstart,
            'after_hsyncend': self.after_hsyncend,
            'after_htotal': self.after_htotal,
            'after_hskew': self.after_hskew,
            'after_vdisplay': self.after_vdisplay,
            'after_vsyncstart': self.after_vsyncstart,
            'after_vsyncend': self.after_vsyncend,
            'after_vtotal': self.after_vtotal,
            'after_flags': self.after_flags,
            'private': self.private,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'AddModeLineRequest':
        return AddModeLineRequest(**AddModeLineRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return AddModeLineRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        AddModeLineRequest.lib = library.xf86vidmode_addmodeline
        AddModeLineRequest.lib.restype = ctypes.c_uint32
        AddModeLineRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint8 * 2, ctypes.c_uint32, ctypes.c_uint8 * 12, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint8 * 2, ctypes.c_uint32, ctypes.c_uint8 * 12, ctypes.c_void_p)


class AddModeLineRequestCType(ctypes.Structure):
    """xf86vidmode AddModeLine"""
    _fields_ = [
        ("screen", ctypes.c_uint32),
        ("dotclock", ctypes.c_uint32),
        ("hdisplay", ctypes.c_uint16),
        ("hsyncstart", ctypes.c_uint16),
        ("hsyncend", ctypes.c_uint16),
        ("htotal", ctypes.c_uint16),
        ("hskew", ctypes.c_uint16),
        ("vdisplay", ctypes.c_uint16),
        ("vsyncstart", ctypes.c_uint16),
        ("vsyncend", ctypes.c_uint16),
        ("vtotal", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
        ("flags", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 12),
        ("privsize", ctypes.c_uint32),
        ("after_dotclock", ctypes.c_uint32),
        ("after_hdisplay", ctypes.c_uint16),
        ("after_hsyncstart", ctypes.c_uint16),
        ("after_hsyncend", ctypes.c_uint16),
        ("after_htotal", ctypes.c_uint16),
        ("after_hskew", ctypes.c_uint16),
        ("after_vdisplay", ctypes.c_uint16),
        ("after_vsyncstart", ctypes.c_uint16),
        ("after_vsyncend", ctypes.c_uint16),
        ("after_vtotal", ctypes.c_uint16),
        ("pad2", ctypes.c_uint8 * 2),
        ("after_flags", ctypes.c_uint32),
        ("pad3", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


DeleteModeLineRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT32)),
    ('dotclock', FixedDataPacketField(MARKER_UINT32)),
    ('hdisplay', FixedDataPacketField(MARKER_UINT16)),
    ('hsyncstart', FixedDataPacketField(MARKER_UINT16)),
    ('hsyncend', FixedDataPacketField(MARKER_UINT16)),
    ('htotal', FixedDataPacketField(MARKER_UINT16)),
    ('hskew', FixedDataPacketField(MARKER_UINT16)),
    ('vdisplay', FixedDataPacketField(MARKER_UINT16)),
    ('vsyncstart', FixedDataPacketField(MARKER_UINT16)),
    ('vsyncend', FixedDataPacketField(MARKER_UINT16)),
    ('vtotal', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
    ('flags', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(12)),
    ('privsize', FixedDataPacketField(MARKER_UINT32)),
    ('private', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: d['privsize'], 0)),
))


class DeleteModeLineRequest:
    OPCODE = 8

    __slots__ = ('screen', 'dotclock', 'hdisplay', 'hsyncstart', 'hsyncend', 'htotal', 'hskew', 'vdisplay', 'vsyncstart', 'vsyncend', 'vtotal', 'flags', 'privsize', 'private',)

    def __init__(
            self, *,
            screen: Optional[int] = None,
            dotclock: Optional[int] = None,
            hdisplay: Optional[int] = None,
            hsyncstart: Optional[int] = None,
            hsyncend: Optional[int] = None,
            htotal: Optional[int] = None,
            hskew: Optional[int] = None,
            vdisplay: Optional[int] = None,
            vsyncstart: Optional[int] = None,
            vsyncend: Optional[int] = None,
            vtotal: Optional[int] = None,
            flags: Optional[int] = None,
            privsize: Optional[int] = None,
            private: Optional[Sequence[int]] = None,
    ) -> None:
        self.screen = screen
        self.dotclock = dotclock
        self.hdisplay = hdisplay
        self.hsyncstart = hsyncstart
        self.hsyncend = hsyncend
        self.htotal = htotal
        self.hskew = hskew
        self.vdisplay = vdisplay
        self.vsyncstart = vsyncstart
        self.vsyncend = vsyncend
        self.vtotal = vtotal
        self.flags = flags
        self.privsize = privsize
        self.private = private

    def as_dict(self) -> Dict[str, Any]:
        return {
            'screen': self.screen,
            'dotclock': self.dotclock,
            'hdisplay': self.hdisplay,
            'hsyncstart': self.hsyncstart,
            'hsyncend': self.hsyncend,
            'htotal': self.htotal,
            'hskew': self.hskew,
            'vdisplay': self.vdisplay,
            'vsyncstart': self.vsyncstart,
            'vsyncend': self.vsyncend,
            'vtotal': self.vtotal,
            'flags': self.flags,
            'privsize': self.privsize,
            'private': self.private,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeleteModeLineRequest':
        return DeleteModeLineRequest(**DeleteModeLineRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeleteModeLineRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, int, int, int, int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        DeleteModeLineRequest.lib = library.xf86vidmode_deletemodeline
        DeleteModeLineRequest.lib.restype = ctypes.c_uint32
        DeleteModeLineRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint8 * 2, ctypes.c_uint32, ctypes.c_uint8 * 12, ctypes.c_uint32, ctypes.c_void_p)


class DeleteModeLineRequestCType(ctypes.Structure):
    """xf86vidmode DeleteModeLine"""
    _fields_ = [
        ("screen", ctypes.c_uint32),
        ("dotclock", ctypes.c_uint32),
        ("hdisplay", ctypes.c_uint16),
        ("hsyncstart", ctypes.c_uint16),
        ("hsyncend", ctypes.c_uint16),
        ("htotal", ctypes.c_uint16),
        ("hskew", ctypes.c_uint16),
        ("vdisplay", ctypes.c_uint16),
        ("vsyncstart", ctypes.c_uint16),
        ("vsyncend", ctypes.c_uint16),
        ("vtotal", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
        ("flags", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 12),
        ("privsize", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


ValidateModeLineRequestCookie = NewType('ValidateModeLineRequestCookie', ctypes.c_uint32)


ValidateModeLineRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT32)),
    ('dotclock', FixedDataPacketField(MARKER_UINT32)),
    ('hdisplay', FixedDataPacketField(MARKER_UINT16)),
    ('hsyncstart', FixedDataPacketField(MARKER_UINT16)),
    ('hsyncend', FixedDataPacketField(MARKER_UINT16)),
    ('htotal', FixedDataPacketField(MARKER_UINT16)),
    ('hskew', FixedDataPacketField(MARKER_UINT16)),
    ('vdisplay', FixedDataPacketField(MARKER_UINT16)),
    ('vsyncstart', FixedDataPacketField(MARKER_UINT16)),
    ('vsyncend', FixedDataPacketField(MARKER_UINT16)),
    ('vtotal', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
    ('flags', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(12)),
    ('privsize', FixedDataPacketField(MARKER_UINT32)),
    ('private', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: d['privsize'], 0)),
))


class ValidateModeLineRequest:
    OPCODE = 9

    __slots__ = ('screen', 'dotclock', 'hdisplay', 'hsyncstart', 'hsyncend', 'htotal', 'hskew', 'vdisplay', 'vsyncstart', 'vsyncend', 'vtotal', 'flags', 'privsize', 'private',)

    def __init__(
            self, *,
            screen: Optional[int] = None,
            dotclock: Optional[int] = None,
            hdisplay: Optional[int] = None,
            hsyncstart: Optional[int] = None,
            hsyncend: Optional[int] = None,
            htotal: Optional[int] = None,
            hskew: Optional[int] = None,
            vdisplay: Optional[int] = None,
            vsyncstart: Optional[int] = None,
            vsyncend: Optional[int] = None,
            vtotal: Optional[int] = None,
            flags: Optional[int] = None,
            privsize: Optional[int] = None,
            private: Optional[Sequence[int]] = None,
    ) -> None:
        self.screen = screen
        self.dotclock = dotclock
        self.hdisplay = hdisplay
        self.hsyncstart = hsyncstart
        self.hsyncend = hsyncend
        self.htotal = htotal
        self.hskew = hskew
        self.vdisplay = vdisplay
        self.vsyncstart = vsyncstart
        self.vsyncend = vsyncend
        self.vtotal = vtotal
        self.flags = flags
        self.privsize = privsize
        self.private = private

    def as_dict(self) -> Dict[str, Any]:
        return {
            'screen': self.screen,
            'dotclock': self.dotclock,
            'hdisplay': self.hdisplay,
            'hsyncstart': self.hsyncstart,
            'hsyncend': self.hsyncend,
            'htotal': self.htotal,
            'hskew': self.hskew,
            'vdisplay': self.vdisplay,
            'vsyncstart': self.vsyncstart,
            'vsyncend': self.vsyncend,
            'vtotal': self.vtotal,
            'flags': self.flags,
            'privsize': self.privsize,
            'private': self.private,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ValidateModeLineRequest':
        return ValidateModeLineRequest(**ValidateModeLineRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ValidateModeLineRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, int, int, int, int, int, int, Sequence[int]], ValidateModeLineRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ValidateModeLineRequest.lib = library.xf86vidmode_validatemodeline
        ValidateModeLineRequest.lib.restype = ValidateModeLineRequestCookie
        ValidateModeLineRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint8 * 2, ctypes.c_uint32, ctypes.c_uint8 * 12, ctypes.c_uint32, ctypes.c_void_p)


class ValidateModeLineRequestCType(ctypes.Structure):
    """xf86vidmode ValidateModeLine"""
    _fields_ = [
        ("screen", ctypes.c_uint32),
        ("dotclock", ctypes.c_uint32),
        ("hdisplay", ctypes.c_uint16),
        ("hsyncstart", ctypes.c_uint16),
        ("hsyncend", ctypes.c_uint16),
        ("htotal", ctypes.c_uint16),
        ("hskew", ctypes.c_uint16),
        ("vdisplay", ctypes.c_uint16),
        ("vsyncstart", ctypes.c_uint16),
        ("vsyncend", ctypes.c_uint16),
        ("vtotal", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
        ("flags", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 12),
        ("privsize", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


ValidateModeLineReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('status', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
))


class ValidateModeLineReplyReply:
    __slots__ = ('status',)

    def __init__(
            self, *,
            status: Optional[int] = None,
    ) -> None:
        self.status = status

    def as_dict(self) -> Dict[str, Any]:
        return {
            'status': self.status,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ValidateModeLineReplyReply':
        return ValidateModeLineReplyReply(**ValidateModeLineReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ValidateModeLineReplyReplyPacket.pack(**self.as_dict())


class ValidateModeLineReplyReplyCType(ctypes.Structure):
    """xf86vidmode ValidateModeLine_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("status", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
    ]


SwitchToModeRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT32)),
    ('dotclock', FixedDataPacketField(MARKER_UINT32)),
    ('hdisplay', FixedDataPacketField(MARKER_UINT16)),
    ('hsyncstart', FixedDataPacketField(MARKER_UINT16)),
    ('hsyncend', FixedDataPacketField(MARKER_UINT16)),
    ('htotal', FixedDataPacketField(MARKER_UINT16)),
    ('hskew', FixedDataPacketField(MARKER_UINT16)),
    ('vdisplay', FixedDataPacketField(MARKER_UINT16)),
    ('vsyncstart', FixedDataPacketField(MARKER_UINT16)),
    ('vsyncend', FixedDataPacketField(MARKER_UINT16)),
    ('vtotal', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
    ('flags', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(12)),
    ('privsize', FixedDataPacketField(MARKER_UINT32)),
    ('private', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: d['privsize'], 0)),
))


class SwitchToModeRequest:
    OPCODE = 10

    __slots__ = ('screen', 'dotclock', 'hdisplay', 'hsyncstart', 'hsyncend', 'htotal', 'hskew', 'vdisplay', 'vsyncstart', 'vsyncend', 'vtotal', 'flags', 'privsize', 'private',)

    def __init__(
            self, *,
            screen: Optional[int] = None,
            dotclock: Optional[int] = None,
            hdisplay: Optional[int] = None,
            hsyncstart: Optional[int] = None,
            hsyncend: Optional[int] = None,
            htotal: Optional[int] = None,
            hskew: Optional[int] = None,
            vdisplay: Optional[int] = None,
            vsyncstart: Optional[int] = None,
            vsyncend: Optional[int] = None,
            vtotal: Optional[int] = None,
            flags: Optional[int] = None,
            privsize: Optional[int] = None,
            private: Optional[Sequence[int]] = None,
    ) -> None:
        self.screen = screen
        self.dotclock = dotclock
        self.hdisplay = hdisplay
        self.hsyncstart = hsyncstart
        self.hsyncend = hsyncend
        self.htotal = htotal
        self.hskew = hskew
        self.vdisplay = vdisplay
        self.vsyncstart = vsyncstart
        self.vsyncend = vsyncend
        self.vtotal = vtotal
        self.flags = flags
        self.privsize = privsize
        self.private = private

    def as_dict(self) -> Dict[str, Any]:
        return {
            'screen': self.screen,
            'dotclock': self.dotclock,
            'hdisplay': self.hdisplay,
            'hsyncstart': self.hsyncstart,
            'hsyncend': self.hsyncend,
            'htotal': self.htotal,
            'hskew': self.hskew,
            'vdisplay': self.vdisplay,
            'vsyncstart': self.vsyncstart,
            'vsyncend': self.vsyncend,
            'vtotal': self.vtotal,
            'flags': self.flags,
            'privsize': self.privsize,
            'private': self.private,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SwitchToModeRequest':
        return SwitchToModeRequest(**SwitchToModeRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SwitchToModeRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, int, int, int, int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SwitchToModeRequest.lib = library.xf86vidmode_switchtomode
        SwitchToModeRequest.lib.restype = ctypes.c_uint32
        SwitchToModeRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint8 * 2, ctypes.c_uint32, ctypes.c_uint8 * 12, ctypes.c_uint32, ctypes.c_void_p)


class SwitchToModeRequestCType(ctypes.Structure):
    """xf86vidmode SwitchToMode"""
    _fields_ = [
        ("screen", ctypes.c_uint32),
        ("dotclock", ctypes.c_uint32),
        ("hdisplay", ctypes.c_uint16),
        ("hsyncstart", ctypes.c_uint16),
        ("hsyncend", ctypes.c_uint16),
        ("htotal", ctypes.c_uint16),
        ("hskew", ctypes.c_uint16),
        ("vdisplay", ctypes.c_uint16),
        ("vsyncstart", ctypes.c_uint16),
        ("vsyncend", ctypes.c_uint16),
        ("vtotal", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
        ("flags", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 12),
        ("privsize", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


GetViewPortRequestCookie = NewType('GetViewPortRequestCookie', ctypes.c_uint32)


GetViewPortRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
))


class GetViewPortRequest:
    OPCODE = 11

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
    def from_data(inp: BinaryIO) -> 'GetViewPortRequest':
        return GetViewPortRequest(**GetViewPortRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetViewPortRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetViewPortRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetViewPortRequest.lib = library.xf86vidmode_getviewport
        GetViewPortRequest.lib.restype = GetViewPortRequestCookie
        GetViewPortRequest.lib.argstype = (ctypes.c_uint16, ctypes.c_uint8 * 2)


class GetViewPortRequestCType(ctypes.Structure):
    """xf86vidmode GetViewPort"""
    _fields_ = [
        ("screen", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
    ]


GetViewPortReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('x', FixedDataPacketField(MARKER_UINT32)),
    ('y', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(16)),
))


class GetViewPortReplyReply:
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
    def from_data(inp: BinaryIO) -> 'GetViewPortReplyReply':
        return GetViewPortReplyReply(**GetViewPortReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetViewPortReplyReplyPacket.pack(**self.as_dict())


class GetViewPortReplyReplyCType(ctypes.Structure):
    """xf86vidmode GetViewPort_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("x", ctypes.c_uint32),
        ("y", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 16),
    ]


SetViewPortRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
    ('x', FixedDataPacketField(MARKER_UINT32)),
    ('y', FixedDataPacketField(MARKER_UINT32)),
))


class SetViewPortRequest:
    OPCODE = 12

    __slots__ = ('screen', 'x', 'y',)

    def __init__(
            self, *,
            screen: Optional[int] = None,
            x: Optional[int] = None,
            y: Optional[int] = None,
    ) -> None:
        self.screen = screen
        self.x = x
        self.y = y

    def as_dict(self) -> Dict[str, Any]:
        return {
            'screen': self.screen,
            'x': self.x,
            'y': self.y,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetViewPortRequest':
        return SetViewPortRequest(**SetViewPortRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetViewPortRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetViewPortRequest.lib = library.xf86vidmode_setviewport
        SetViewPortRequest.lib.restype = ctypes.c_uint32
        SetViewPortRequest.lib.argstype = (ctypes.c_uint16, ctypes.c_uint8 * 2, ctypes.c_uint32, ctypes.c_uint32)


class SetViewPortRequestCType(ctypes.Structure):
    """xf86vidmode SetViewPort"""
    _fields_ = [
        ("screen", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
        ("x", ctypes.c_uint32),
        ("y", ctypes.c_uint32),
    ]


GetDotClocksRequestCookie = NewType('GetDotClocksRequestCookie', ctypes.c_uint32)


GetDotClocksRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
))


class GetDotClocksRequest:
    OPCODE = 13

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
    def from_data(inp: BinaryIO) -> 'GetDotClocksRequest':
        return GetDotClocksRequest(**GetDotClocksRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetDotClocksRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetDotClocksRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetDotClocksRequest.lib = library.xf86vidmode_getdotclocks
        GetDotClocksRequest.lib.restype = GetDotClocksRequestCookie
        GetDotClocksRequest.lib.argstype = (ctypes.c_uint16, ctypes.c_uint8 * 2)


class GetDotClocksRequestCType(ctypes.Structure):
    """xf86vidmode GetDotClocks"""
    _fields_ = [
        ("screen", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
    ]


GetDotClocksReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('flags', FixedDataPacketField(MARKER_UINT32)),
    ('clocks', FixedDataPacketField(MARKER_UINT32)),
    ('maxclocks', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(12)),
    ('clock', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: ((1) - ((d['flags']) & (1))) * (d['clocks']), 0)),
))


class GetDotClocksReplyReply:
    __slots__ = ('flags', 'clocks', 'maxclocks', 'clock',)

    def __init__(
            self, *,
            flags: Optional[int] = None,
            clocks: Optional[int] = None,
            maxclocks: Optional[int] = None,
            clock: Optional[Sequence[int]] = None,
    ) -> None:
        self.flags = flags
        self.clocks = clocks
        self.maxclocks = maxclocks
        self.clock = clock

    def as_dict(self) -> Dict[str, Any]:
        return {
            'flags': self.flags,
            'clocks': self.clocks,
            'maxclocks': self.maxclocks,
            'clock': self.clock,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetDotClocksReplyReply':
        return GetDotClocksReplyReply(**GetDotClocksReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetDotClocksReplyReplyPacket.pack(**self.as_dict())


class GetDotClocksReplyReplyCType(ctypes.Structure):
    """xf86vidmode GetDotClocks_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("flags", ctypes.c_uint32),
        ("clocks", ctypes.c_uint32),
        ("maxclocks", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


SetClientVersionRequestPacket = DataPacket((
    ('major', FixedDataPacketField(MARKER_UINT16)),
    ('minor', FixedDataPacketField(MARKER_UINT16)),
))


class SetClientVersionRequest:
    OPCODE = 14

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
    def from_data(inp: BinaryIO) -> 'SetClientVersionRequest':
        return SetClientVersionRequest(**SetClientVersionRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetClientVersionRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetClientVersionRequest.lib = library.xf86vidmode_setclientversion
        SetClientVersionRequest.lib.restype = ctypes.c_uint32
        SetClientVersionRequest.lib.argstype = (ctypes.c_uint16, ctypes.c_uint16)


class SetClientVersionRequestCType(ctypes.Structure):
    """xf86vidmode SetClientVersion"""
    _fields_ = [
        ("major", ctypes.c_uint16),
        ("minor", ctypes.c_uint16),
    ]


SetGammaRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
    ('red', FixedDataPacketField(MARKER_UINT32)),
    ('green', FixedDataPacketField(MARKER_UINT32)),
    ('blue', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(12)),
))


class SetGammaRequest:
    OPCODE = 15

    __slots__ = ('screen', 'red', 'green', 'blue',)

    def __init__(
            self, *,
            screen: Optional[int] = None,
            red: Optional[int] = None,
            green: Optional[int] = None,
            blue: Optional[int] = None,
    ) -> None:
        self.screen = screen
        self.red = red
        self.green = green
        self.blue = blue

    def as_dict(self) -> Dict[str, Any]:
        return {
            'screen': self.screen,
            'red': self.red,
            'green': self.green,
            'blue': self.blue,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetGammaRequest':
        return SetGammaRequest(**SetGammaRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetGammaRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetGammaRequest.lib = library.xf86vidmode_setgamma
        SetGammaRequest.lib.restype = ctypes.c_uint32
        SetGammaRequest.lib.argstype = (ctypes.c_uint16, ctypes.c_uint8 * 2, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8 * 12)


class SetGammaRequestCType(ctypes.Structure):
    """xf86vidmode SetGamma"""
    _fields_ = [
        ("screen", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
        ("red", ctypes.c_uint32),
        ("green", ctypes.c_uint32),
        ("blue", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 12),
    ]


GetGammaRequestCookie = NewType('GetGammaRequestCookie', ctypes.c_uint32)


GetGammaRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(26)),
))


class GetGammaRequest:
    OPCODE = 16

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
    def from_data(inp: BinaryIO) -> 'GetGammaRequest':
        return GetGammaRequest(**GetGammaRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetGammaRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetGammaRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetGammaRequest.lib = library.xf86vidmode_getgamma
        GetGammaRequest.lib.restype = GetGammaRequestCookie
        GetGammaRequest.lib.argstype = (ctypes.c_uint16, ctypes.c_uint8 * 26)


class GetGammaRequestCType(ctypes.Structure):
    """xf86vidmode GetGamma"""
    _fields_ = [
        ("screen", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 26),
    ]


GetGammaReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('red', FixedDataPacketField(MARKER_UINT32)),
    ('green', FixedDataPacketField(MARKER_UINT32)),
    ('blue', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(12)),
))


class GetGammaReplyReply:
    __slots__ = ('red', 'green', 'blue',)

    def __init__(
            self, *,
            red: Optional[int] = None,
            green: Optional[int] = None,
            blue: Optional[int] = None,
    ) -> None:
        self.red = red
        self.green = green
        self.blue = blue

    def as_dict(self) -> Dict[str, Any]:
        return {
            'red': self.red,
            'green': self.green,
            'blue': self.blue,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetGammaReplyReply':
        return GetGammaReplyReply(**GetGammaReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetGammaReplyReplyPacket.pack(**self.as_dict())


class GetGammaReplyReplyCType(ctypes.Structure):
    """xf86vidmode GetGamma_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("red", ctypes.c_uint32),
        ("green", ctypes.c_uint32),
        ("blue", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 12),
    ]


GetGammaRampRequestCookie = NewType('GetGammaRampRequestCookie', ctypes.c_uint32)


GetGammaRampRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT16)),
    ('size', FixedDataPacketField(MARKER_UINT16)),
))


class GetGammaRampRequest:
    OPCODE = 17

    __slots__ = ('screen', 'size',)

    def __init__(
            self, *,
            screen: Optional[int] = None,
            size: Optional[int] = None,
    ) -> None:
        self.screen = screen
        self.size = size

    def as_dict(self) -> Dict[str, Any]:
        return {
            'screen': self.screen,
            'size': self.size,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetGammaRampRequest':
        return GetGammaRampRequest(**GetGammaRampRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetGammaRampRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], GetGammaRampRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetGammaRampRequest.lib = library.xf86vidmode_getgammaramp
        GetGammaRampRequest.lib.restype = GetGammaRampRequestCookie
        GetGammaRampRequest.lib.argstype = (ctypes.c_uint16, ctypes.c_uint16)


class GetGammaRampRequestCType(ctypes.Structure):
    """xf86vidmode GetGammaRamp"""
    _fields_ = [
        ("screen", ctypes.c_uint16),
        ("size", ctypes.c_uint16),
    ]


GetGammaRampReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('size', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(22)),
    ('red', SimpleListDataPacketField(MARKER_UINT16, lambda d, c: ((d['size']) + (1)) & (~(1)), 0)),
    ('green', SimpleListDataPacketField(MARKER_UINT16, lambda d, c: ((d['size']) + (1)) & (~(1)), 0)),
    ('blue', SimpleListDataPacketField(MARKER_UINT16, lambda d, c: ((d['size']) + (1)) & (~(1)), 0)),
))


class GetGammaRampReplyReply:
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
    def from_data(inp: BinaryIO) -> 'GetGammaRampReplyReply':
        return GetGammaRampReplyReply(**GetGammaRampReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetGammaRampReplyReplyPacket.pack(**self.as_dict())


class GetGammaRampReplyReplyCType(ctypes.Structure):
    """xf86vidmode GetGammaRamp_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("size", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 22),
        ("var_data", ctypes.c_void_p),
    ]


SetGammaRampRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT16)),
    ('size', FixedDataPacketField(MARKER_UINT16)),
    ('red', SimpleListDataPacketField(MARKER_UINT16, lambda d, c: ((d['size']) + (1)) & (~(1)), 0)),
    ('green', SimpleListDataPacketField(MARKER_UINT16, lambda d, c: ((d['size']) + (1)) & (~(1)), 0)),
    ('blue', SimpleListDataPacketField(MARKER_UINT16, lambda d, c: ((d['size']) + (1)) & (~(1)), 0)),
))


class SetGammaRampRequest:
    OPCODE = 18

    __slots__ = ('screen', 'size', 'red', 'green', 'blue',)

    def __init__(
            self, *,
            screen: Optional[int] = None,
            size: Optional[int] = None,
            red: Optional[Sequence[int]] = None,
            green: Optional[Sequence[int]] = None,
            blue: Optional[Sequence[int]] = None,
    ) -> None:
        self.screen = screen
        self.size = size
        self.red = red
        self.green = green
        self.blue = blue

    def as_dict(self) -> Dict[str, Any]:
        return {
            'screen': self.screen,
            'size': self.size,
            'red': self.red,
            'green': self.green,
            'blue': self.blue,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetGammaRampRequest':
        return SetGammaRampRequest(**SetGammaRampRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetGammaRampRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int], Sequence[int], Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetGammaRampRequest.lib = library.xf86vidmode_setgammaramp
        SetGammaRampRequest.lib.restype = ctypes.c_uint32
        SetGammaRampRequest.lib.argstype = (ctypes.c_uint16, ctypes.c_uint16, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)


class SetGammaRampRequestCType(ctypes.Structure):
    """xf86vidmode SetGammaRamp"""
    _fields_ = [
        ("screen", ctypes.c_uint16),
        ("size", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


GetGammaRampSizeRequestCookie = NewType('GetGammaRampSizeRequestCookie', ctypes.c_uint32)


GetGammaRampSizeRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
))


class GetGammaRampSizeRequest:
    OPCODE = 19

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
    def from_data(inp: BinaryIO) -> 'GetGammaRampSizeRequest':
        return GetGammaRampSizeRequest(**GetGammaRampSizeRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetGammaRampSizeRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetGammaRampSizeRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetGammaRampSizeRequest.lib = library.xf86vidmode_getgammarampsize
        GetGammaRampSizeRequest.lib.restype = GetGammaRampSizeRequestCookie
        GetGammaRampSizeRequest.lib.argstype = (ctypes.c_uint16, ctypes.c_uint8 * 2)


class GetGammaRampSizeRequestCType(ctypes.Structure):
    """xf86vidmode GetGammaRampSize"""
    _fields_ = [
        ("screen", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
    ]


GetGammaRampSizeReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('size', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(22)),
))


class GetGammaRampSizeReplyReply:
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
    def from_data(inp: BinaryIO) -> 'GetGammaRampSizeReplyReply':
        return GetGammaRampSizeReplyReply(**GetGammaRampSizeReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetGammaRampSizeReplyReplyPacket.pack(**self.as_dict())


class GetGammaRampSizeReplyReplyCType(ctypes.Structure):
    """xf86vidmode GetGammaRampSize_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("size", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 22),
    ]


GetPermissionsRequestCookie = NewType('GetPermissionsRequestCookie', ctypes.c_uint32)


GetPermissionsRequestPacket = DataPacket((
    ('screen', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
))


class GetPermissionsRequest:
    OPCODE = 20

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
    def from_data(inp: BinaryIO) -> 'GetPermissionsRequest':
        return GetPermissionsRequest(**GetPermissionsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetPermissionsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetPermissionsRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetPermissionsRequest.lib = library.xf86vidmode_getpermissions
        GetPermissionsRequest.lib.restype = GetPermissionsRequestCookie
        GetPermissionsRequest.lib.argstype = (ctypes.c_uint16, ctypes.c_uint8 * 2)


class GetPermissionsRequestCType(ctypes.Structure):
    """xf86vidmode GetPermissions"""
    _fields_ = [
        ("screen", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
    ]


GetPermissionsReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('permissions', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
))


class GetPermissionsReplyReply:
    __slots__ = ('permissions',)

    def __init__(
            self, *,
            permissions: Optional[int] = None,
    ) -> None:
        self.permissions = permissions

    def as_dict(self) -> Dict[str, Any]:
        return {
            'permissions': self.permissions,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetPermissionsReplyReply':
        return GetPermissionsReplyReply(**GetPermissionsReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetPermissionsReplyReplyPacket.pack(**self.as_dict())


class GetPermissionsReplyReplyCType(ctypes.Structure):
    """xf86vidmode GetPermissions_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("permissions", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
    ]


# ------------------------------------------------------------------
# Unions

