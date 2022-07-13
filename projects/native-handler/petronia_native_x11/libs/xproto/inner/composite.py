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

RedirectType = NewType('RedirectType', int)


class RedirectValues:
    AUTOMATIC = RedirectType(0)
    MANUAL = RedirectType(1)


# ------------------------------------------------------------------
# Aliases



# ------------------------------------------------------------------
# Structures, Events, Requests, Replies


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
        QueryVersionRequest.lib = library.composite_queryversion
        QueryVersionRequest.lib.restype = QueryVersionRequestCookie
        QueryVersionRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class QueryVersionRequestCType(ctypes.Structure):
    """composite QueryVersion"""
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
    """composite QueryVersion_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("major_version", ctypes.c_uint32),
        ("minor_version", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 16),
    ]


RedirectWindowRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('update', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class RedirectWindowRequest:
    OPCODE = 1

    __slots__ = ('window', 'update',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            update: Optional[int] = None,
    ) -> None:
        self.window = window
        self.update = update

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'update': self.update,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'RedirectWindowRequest':
        return RedirectWindowRequest(**RedirectWindowRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return RedirectWindowRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        RedirectWindowRequest.lib = library.composite_redirectwindow
        RedirectWindowRequest.lib.restype = ctypes.c_uint32
        RedirectWindowRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8 * 3)


class RedirectWindowRequestCType(ctypes.Structure):
    """composite RedirectWindow"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("update", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


RedirectSubwindowsRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('update', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class RedirectSubwindowsRequest:
    OPCODE = 2

    __slots__ = ('window', 'update',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            update: Optional[int] = None,
    ) -> None:
        self.window = window
        self.update = update

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'update': self.update,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'RedirectSubwindowsRequest':
        return RedirectSubwindowsRequest(**RedirectSubwindowsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return RedirectSubwindowsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        RedirectSubwindowsRequest.lib = library.composite_redirectsubwindows
        RedirectSubwindowsRequest.lib.restype = ctypes.c_uint32
        RedirectSubwindowsRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8 * 3)


class RedirectSubwindowsRequestCType(ctypes.Structure):
    """composite RedirectSubwindows"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("update", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


UnredirectWindowRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('update', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class UnredirectWindowRequest:
    OPCODE = 3

    __slots__ = ('window', 'update',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            update: Optional[int] = None,
    ) -> None:
        self.window = window
        self.update = update

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'update': self.update,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'UnredirectWindowRequest':
        return UnredirectWindowRequest(**UnredirectWindowRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return UnredirectWindowRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        UnredirectWindowRequest.lib = library.composite_unredirectwindow
        UnredirectWindowRequest.lib.restype = ctypes.c_uint32
        UnredirectWindowRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8 * 3)


class UnredirectWindowRequestCType(ctypes.Structure):
    """composite UnredirectWindow"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("update", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


UnredirectSubwindowsRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('update', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class UnredirectSubwindowsRequest:
    OPCODE = 4

    __slots__ = ('window', 'update',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            update: Optional[int] = None,
    ) -> None:
        self.window = window
        self.update = update

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'update': self.update,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'UnredirectSubwindowsRequest':
        return UnredirectSubwindowsRequest(**UnredirectSubwindowsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return UnredirectSubwindowsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        UnredirectSubwindowsRequest.lib = library.composite_unredirectsubwindows
        UnredirectSubwindowsRequest.lib.restype = ctypes.c_uint32
        UnredirectSubwindowsRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8 * 3)


class UnredirectSubwindowsRequestCType(ctypes.Structure):
    """composite UnredirectSubwindows"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("update", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


CreateRegionFromBorderClipRequestPacket = DataPacket((
    ('region', FixedDataPacketField(MARKER_UINT32)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class CreateRegionFromBorderClipRequest:
    OPCODE = 5

    __slots__ = ('region', 'window',)

    def __init__(
            self, *,
            region: Optional[int] = None,
            window: Optional[int] = None,
    ) -> None:
        self.region = region
        self.window = window

    def as_dict(self) -> Dict[str, Any]:
        return {
            'region': self.region,
            'window': self.window,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateRegionFromBorderClipRequest':
        return CreateRegionFromBorderClipRequest(**CreateRegionFromBorderClipRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateRegionFromBorderClipRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateRegionFromBorderClipRequest.lib = library.composite_createregionfromborderclip
        CreateRegionFromBorderClipRequest.lib.restype = ctypes.c_uint32
        CreateRegionFromBorderClipRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class CreateRegionFromBorderClipRequestCType(ctypes.Structure):
    """composite CreateRegionFromBorderClip"""
    _fields_ = [
        ("region", ctypes.c_uint32),
        ("window", ctypes.c_uint32),
    ]


NameWindowPixmapRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('pixmap', FixedDataPacketField(MARKER_UINT32)),
))


class NameWindowPixmapRequest:
    OPCODE = 6

    __slots__ = ('window', 'pixmap',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            pixmap: Optional[int] = None,
    ) -> None:
        self.window = window
        self.pixmap = pixmap

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'pixmap': self.pixmap,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'NameWindowPixmapRequest':
        return NameWindowPixmapRequest(**NameWindowPixmapRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return NameWindowPixmapRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        NameWindowPixmapRequest.lib = library.composite_namewindowpixmap
        NameWindowPixmapRequest.lib.restype = ctypes.c_uint32
        NameWindowPixmapRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class NameWindowPixmapRequestCType(ctypes.Structure):
    """composite NameWindowPixmap"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("pixmap", ctypes.c_uint32),
    ]


GetOverlayWindowRequestCookie = NewType('GetOverlayWindowRequestCookie', ctypes.c_uint32)


GetOverlayWindowRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class GetOverlayWindowRequest:
    OPCODE = 7

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
    def from_data(inp: BinaryIO) -> 'GetOverlayWindowRequest':
        return GetOverlayWindowRequest(**GetOverlayWindowRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetOverlayWindowRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetOverlayWindowRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetOverlayWindowRequest.lib = library.composite_getoverlaywindow
        GetOverlayWindowRequest.lib.restype = GetOverlayWindowRequestCookie
        GetOverlayWindowRequest.lib.argstype = (ctypes.c_uint32,)


class GetOverlayWindowRequestCType(ctypes.Structure):
    """composite GetOverlayWindow"""
    _fields_ = [
        ("window", ctypes.c_uint32),
    ]


GetOverlayWindowReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('overlay_win', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
))


class GetOverlayWindowReplyReply:
    __slots__ = ('overlay_win',)

    def __init__(
            self, *,
            overlay_win: Optional[int] = None,
    ) -> None:
        self.overlay_win = overlay_win

    def as_dict(self) -> Dict[str, Any]:
        return {
            'overlay_win': self.overlay_win,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetOverlayWindowReplyReply':
        return GetOverlayWindowReplyReply(**GetOverlayWindowReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetOverlayWindowReplyReplyPacket.pack(**self.as_dict())


class GetOverlayWindowReplyReplyCType(ctypes.Structure):
    """composite GetOverlayWindow_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("overlay_win", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
    ]


ReleaseOverlayWindowRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class ReleaseOverlayWindowRequest:
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
    def from_data(inp: BinaryIO) -> 'ReleaseOverlayWindowRequest':
        return ReleaseOverlayWindowRequest(**ReleaseOverlayWindowRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ReleaseOverlayWindowRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ReleaseOverlayWindowRequest.lib = library.composite_releaseoverlaywindow
        ReleaseOverlayWindowRequest.lib.restype = ctypes.c_uint32
        ReleaseOverlayWindowRequest.lib.argstype = (ctypes.c_uint32,)


class ReleaseOverlayWindowRequestCType(ctypes.Structure):
    """composite ReleaseOverlayWindow"""
    _fields_ = [
        ("window", ctypes.c_uint32),
    ]


# ------------------------------------------------------------------
# Unions

