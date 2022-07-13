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

SaveSetModeType = NewType('SaveSetModeType', int)


class SaveSetModeValues:
    INSERT = SaveSetModeType(0)
    DELETE = SaveSetModeType(1)


SaveSetTargetType = NewType('SaveSetTargetType', int)


class SaveSetTargetValues:
    NEAREST = SaveSetTargetType(0)
    ROOT = SaveSetTargetType(1)


SaveSetMappingType = NewType('SaveSetMappingType', int)


class SaveSetMappingValues:
    MAP = SaveSetMappingType(0)
    UNMAP = SaveSetMappingType(1)


SelectionEventType = NewType('SelectionEventType', int)


class SelectionEventValues:
    SET_SELECTION_OWNER = SelectionEventType(0)
    SELECTION_WINDOW_DESTROY = SelectionEventType(1)
    SELECTION_CLIENT_CLOSE = SelectionEventType(2)


SelectionEventMaskType = NewType('SelectionEventMaskType', int)


class SelectionEventMaskValues:
    SET_SELECTION_OWNER = SelectionEventMaskType(1)
    SELECTION_WINDOW_DESTROY = SelectionEventMaskType(2)
    SELECTION_CLIENT_CLOSE = SelectionEventMaskType(4)


CursorNotifyType = NewType('CursorNotifyType', int)


class CursorNotifyValues:
    DISPLAY_CURSOR = CursorNotifyType(0)


CursorNotifyMaskType = NewType('CursorNotifyMaskType', int)


class CursorNotifyMaskValues:
    DISPLAY_CURSOR = CursorNotifyMaskType(1)


RegionType = NewType('RegionType', int)


class RegionValues:
    NONE = RegionType(0)


BarrierDirectionsType = NewType('BarrierDirectionsType', int)


class BarrierDirectionsValues:
    POSITIVE_X = BarrierDirectionsType(1)
    POSITIVE_Y = BarrierDirectionsType(2)
    NEGATIVE_X = BarrierDirectionsType(4)
    NEGATIVE_Y = BarrierDirectionsType(8)


ClientDisconnectFlagsType = NewType('ClientDisconnectFlagsType', int)


class ClientDisconnectFlagsValues:
    DEFAULT = ClientDisconnectFlagsType(0)
    TERMINATE = ClientDisconnectFlagsType(1)


# ------------------------------------------------------------------
# Aliases

Barrier = NewType('Barrier', ctypes.c_uint32)
Region = NewType('Region', ctypes.c_uint32)


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
        QueryVersionRequest.lib = library.xfixes_queryversion
        QueryVersionRequest.lib.restype = QueryVersionRequestCookie
        QueryVersionRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class QueryVersionRequestCType(ctypes.Structure):
    """xfixes QueryVersion"""
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
    """xfixes QueryVersion_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("major_version", ctypes.c_uint32),
        ("minor_version", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 16),
    ]


ChangeSaveSetRequestPacket = DataPacket((
    ('mode', FixedDataPacketField(MARKER_INT8)),
    ('target', FixedDataPacketField(MARKER_INT8)),
    ('map', FixedDataPacketField(MARKER_INT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class ChangeSaveSetRequest:
    OPCODE = 1

    __slots__ = ('mode', 'target', 'map', 'window',)

    def __init__(
            self, *,
            mode: Optional[int] = None,
            target: Optional[int] = None,
            map: Optional[int] = None,
            window: Optional[int] = None,
    ) -> None:
        self.mode = mode
        self.target = target
        self.map = map
        self.window = window

    def as_dict(self) -> Dict[str, Any]:
        return {
            'mode': self.mode,
            'target': self.target,
            'map': self.map,
            'window': self.window,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ChangeSaveSetRequest':
        return ChangeSaveSetRequest(**ChangeSaveSetRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ChangeSaveSetRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ChangeSaveSetRequest.lib = library.xfixes_changesaveset
        ChangeSaveSetRequest.lib.restype = ctypes.c_uint32
        ChangeSaveSetRequest.lib.argstype = (ctypes.c_int8, ctypes.c_int8, ctypes.c_int8, ctypes.c_uint8, ctypes.c_uint32)


class ChangeSaveSetRequestCType(ctypes.Structure):
    """xfixes ChangeSaveSet"""
    _fields_ = [
        ("mode", ctypes.c_int8),
        ("target", ctypes.c_int8),
        ("map", ctypes.c_int8),
        ("pad0", ctypes.c_uint8),
        ("window", ctypes.c_uint32),
    ]


SelectionNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('subtype', FixedDataPacketField(MARKER_UINT8)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('owner', FixedDataPacketField(MARKER_UINT32)),
    ('selection', FixedDataPacketField(MARKER_UINT32)),
    ('timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('selection_timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(8)),
))


class SelectionNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'subtype', 'window', 'owner', 'selection', 'timestamp', 'selection_timestamp',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            subtype: Optional[int] = None,
            window: Optional[int] = None,
            owner: Optional[int] = None,
            selection: Optional[int] = None,
            timestamp: Optional[int] = None,
            selection_timestamp: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.subtype = subtype
        self.window = window
        self.owner = owner
        self.selection = selection
        self.timestamp = timestamp
        self.selection_timestamp = selection_timestamp

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'subtype': self.subtype,
            'window': self.window,
            'owner': self.owner,
            'selection': self.selection,
            'timestamp': self.timestamp,
            'selection_timestamp': self.selection_timestamp,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SelectionNotifyEvent':
        return SelectionNotifyEvent(**SelectionNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SelectionNotifyEventPacket.pack(**self.as_dict())


class SelectionNotifyEventCType(ctypes.Structure):
    """xfixes SelectionNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("subtype", ctypes.c_uint8),
        ("window", ctypes.c_uint32),
        ("owner", ctypes.c_uint32),
        ("selection", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint32),
        ("selection_timestamp", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 8),
    ]


SelectSelectionInputRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('selection', FixedDataPacketField(MARKER_UINT32)),
    ('event_mask', FixedDataPacketField(MARKER_UINT32)),
))


class SelectSelectionInputRequest:
    OPCODE = 2

    __slots__ = ('window', 'selection', 'event_mask',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            selection: Optional[int] = None,
            event_mask: Optional[int] = None,
    ) -> None:
        self.window = window
        self.selection = selection
        self.event_mask = event_mask

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'selection': self.selection,
            'event_mask': self.event_mask,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SelectSelectionInputRequest':
        return SelectSelectionInputRequest(**SelectSelectionInputRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SelectSelectionInputRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SelectSelectionInputRequest.lib = library.xfixes_selectselectioninput
        SelectSelectionInputRequest.lib.restype = ctypes.c_uint32
        SelectSelectionInputRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class SelectSelectionInputRequestCType(ctypes.Structure):
    """xfixes SelectSelectionInput"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("selection", ctypes.c_uint32),
        ("event_mask", ctypes.c_uint32),
    ]


CursorNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('subtype', FixedDataPacketField(MARKER_UINT8)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('cursor_serial', FixedDataPacketField(MARKER_UINT32)),
    ('timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('name', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(12)),
))


class CursorNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'subtype', 'window', 'cursor_serial', 'timestamp', 'name',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            subtype: Optional[int] = None,
            window: Optional[int] = None,
            cursor_serial: Optional[int] = None,
            timestamp: Optional[int] = None,
            name: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.subtype = subtype
        self.window = window
        self.cursor_serial = cursor_serial
        self.timestamp = timestamp
        self.name = name

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'subtype': self.subtype,
            'window': self.window,
            'cursor_serial': self.cursor_serial,
            'timestamp': self.timestamp,
            'name': self.name,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CursorNotifyEvent':
        return CursorNotifyEvent(**CursorNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CursorNotifyEventPacket.pack(**self.as_dict())


class CursorNotifyEventCType(ctypes.Structure):
    """xfixes CursorNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("subtype", ctypes.c_uint8),
        ("window", ctypes.c_uint32),
        ("cursor_serial", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint32),
        ("name", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 12),
    ]


SelectCursorInputRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('event_mask', FixedDataPacketField(MARKER_UINT32)),
))


class SelectCursorInputRequest:
    OPCODE = 3

    __slots__ = ('window', 'event_mask',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            event_mask: Optional[int] = None,
    ) -> None:
        self.window = window
        self.event_mask = event_mask

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'event_mask': self.event_mask,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SelectCursorInputRequest':
        return SelectCursorInputRequest(**SelectCursorInputRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SelectCursorInputRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SelectCursorInputRequest.lib = library.xfixes_selectcursorinput
        SelectCursorInputRequest.lib.restype = ctypes.c_uint32
        SelectCursorInputRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class SelectCursorInputRequestCType(ctypes.Structure):
    """xfixes SelectCursorInput"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("event_mask", ctypes.c_uint32),
    ]


GetCursorImageRequestCookie = NewType('GetCursorImageRequestCookie', ctypes.c_uint32)


GetCursorImageRequestPacket = DataPacket((
))


class GetCursorImageRequest:
    OPCODE = 4

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetCursorImageRequest':
        return GetCursorImageRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], GetCursorImageRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetCursorImageRequest.lib = library.xfixes_getcursorimage
        GetCursorImageRequest.lib.restype = GetCursorImageRequestCookie
        GetCursorImageRequest.lib.argstype = ()


class GetCursorImageRequestCType(ctypes.Structure):
    """xfixes GetCursorImage"""
    _fields_ = [
    ]


GetCursorImageReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('x', FixedDataPacketField(MARKER_INT16)),
    ('y', FixedDataPacketField(MARKER_INT16)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('xhot', FixedDataPacketField(MARKER_UINT16)),
    ('yhot', FixedDataPacketField(MARKER_UINT16)),
    ('cursor_serial', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(8)),
    ('cursor_image', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: (d['width']) * (d['height']), 0)),
))


class GetCursorImageReplyReply:
    __slots__ = ('x', 'y', 'width', 'height', 'xhot', 'yhot', 'cursor_serial', 'cursor_image',)

    def __init__(
            self, *,
            x: Optional[int] = None,
            y: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            xhot: Optional[int] = None,
            yhot: Optional[int] = None,
            cursor_serial: Optional[int] = None,
            cursor_image: Optional[Sequence[int]] = None,
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.xhot = xhot
        self.yhot = yhot
        self.cursor_serial = cursor_serial
        self.cursor_image = cursor_image

    def as_dict(self) -> Dict[str, Any]:
        return {
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height,
            'xhot': self.xhot,
            'yhot': self.yhot,
            'cursor_serial': self.cursor_serial,
            'cursor_image': self.cursor_image,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetCursorImageReplyReply':
        return GetCursorImageReplyReply(**GetCursorImageReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetCursorImageReplyReplyPacket.pack(**self.as_dict())


class GetCursorImageReplyReplyCType(ctypes.Structure):
    """xfixes GetCursorImage_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("x", ctypes.c_int16),
        ("y", ctypes.c_int16),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("xhot", ctypes.c_uint16),
        ("yhot", ctypes.c_uint16),
        ("cursor_serial", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 8),
        ("var_data", ctypes.c_void_p),
    ]


CreateRegionRequestPacket = DataPacket((
    ('region', FixedDataPacketField(MARKER_UINT32)),
    ('rectangles', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 1, 0)),
))


class CreateRegionRequest:
    OPCODE = 5

    __slots__ = ('region', 'rectangles',)

    def __init__(
            self, *,
            region: Optional[int] = None,
            rectangles: Optional[Sequence[int]] = None,
    ) -> None:
        self.region = region
        self.rectangles = rectangles

    def as_dict(self) -> Dict[str, Any]:
        return {
            'region': self.region,
            'rectangles': self.rectangles,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateRegionRequest':
        return CreateRegionRequest(**CreateRegionRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateRegionRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateRegionRequest.lib = library.xfixes_createregion
        CreateRegionRequest.lib.restype = ctypes.c_uint32
        CreateRegionRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_void_p)


class CreateRegionRequestCType(ctypes.Structure):
    """xfixes CreateRegion"""
    _fields_ = [
        ("region", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


CreateRegionFromBitmapRequestPacket = DataPacket((
    ('region', FixedDataPacketField(MARKER_UINT32)),
    ('bitmap', FixedDataPacketField(MARKER_UINT32)),
))


class CreateRegionFromBitmapRequest:
    OPCODE = 6

    __slots__ = ('region', 'bitmap',)

    def __init__(
            self, *,
            region: Optional[int] = None,
            bitmap: Optional[int] = None,
    ) -> None:
        self.region = region
        self.bitmap = bitmap

    def as_dict(self) -> Dict[str, Any]:
        return {
            'region': self.region,
            'bitmap': self.bitmap,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateRegionFromBitmapRequest':
        return CreateRegionFromBitmapRequest(**CreateRegionFromBitmapRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateRegionFromBitmapRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateRegionFromBitmapRequest.lib = library.xfixes_createregionfrombitmap
        CreateRegionFromBitmapRequest.lib.restype = ctypes.c_uint32
        CreateRegionFromBitmapRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class CreateRegionFromBitmapRequestCType(ctypes.Structure):
    """xfixes CreateRegionFromBitmap"""
    _fields_ = [
        ("region", ctypes.c_uint32),
        ("bitmap", ctypes.c_uint32),
    ]


CreateRegionFromWindowRequestPacket = DataPacket((
    ('region', FixedDataPacketField(MARKER_UINT32)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('kind', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(3)),
))


class CreateRegionFromWindowRequest:
    OPCODE = 7

    __slots__ = ('region', 'window', 'kind',)

    def __init__(
            self, *,
            region: Optional[int] = None,
            window: Optional[int] = None,
            kind: Optional[int] = None,
    ) -> None:
        self.region = region
        self.window = window
        self.kind = kind

    def as_dict(self) -> Dict[str, Any]:
        return {
            'region': self.region,
            'window': self.window,
            'kind': self.kind,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateRegionFromWindowRequest':
        return CreateRegionFromWindowRequest(**CreateRegionFromWindowRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateRegionFromWindowRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateRegionFromWindowRequest.lib = library.xfixes_createregionfromwindow
        CreateRegionFromWindowRequest.lib.restype = ctypes.c_uint32
        CreateRegionFromWindowRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8 * 3)


class CreateRegionFromWindowRequestCType(ctypes.Structure):
    """xfixes CreateRegionFromWindow"""
    _fields_ = [
        ("region", ctypes.c_uint32),
        ("window", ctypes.c_uint32),
        ("kind", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 3),
    ]


CreateRegionFromGcRequestPacket = DataPacket((
    ('region', FixedDataPacketField(MARKER_UINT32)),
    ('gc', FixedDataPacketField(MARKER_UINT32)),
))


class CreateRegionFromGcRequest:
    OPCODE = 8

    __slots__ = ('region', 'gc',)

    def __init__(
            self, *,
            region: Optional[int] = None,
            gc: Optional[int] = None,
    ) -> None:
        self.region = region
        self.gc = gc

    def as_dict(self) -> Dict[str, Any]:
        return {
            'region': self.region,
            'gc': self.gc,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateRegionFromGcRequest':
        return CreateRegionFromGcRequest(**CreateRegionFromGcRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateRegionFromGcRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateRegionFromGcRequest.lib = library.xfixes_createregionfromgc
        CreateRegionFromGcRequest.lib.restype = ctypes.c_uint32
        CreateRegionFromGcRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class CreateRegionFromGcRequestCType(ctypes.Structure):
    """xfixes CreateRegionFromGC"""
    _fields_ = [
        ("region", ctypes.c_uint32),
        ("gc", ctypes.c_uint32),
    ]


CreateRegionFromPictureRequestPacket = DataPacket((
    ('region', FixedDataPacketField(MARKER_UINT32)),
    ('picture', FixedDataPacketField(MARKER_UINT32)),
))


class CreateRegionFromPictureRequest:
    OPCODE = 9

    __slots__ = ('region', 'picture',)

    def __init__(
            self, *,
            region: Optional[int] = None,
            picture: Optional[int] = None,
    ) -> None:
        self.region = region
        self.picture = picture

    def as_dict(self) -> Dict[str, Any]:
        return {
            'region': self.region,
            'picture': self.picture,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateRegionFromPictureRequest':
        return CreateRegionFromPictureRequest(**CreateRegionFromPictureRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateRegionFromPictureRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateRegionFromPictureRequest.lib = library.xfixes_createregionfrompicture
        CreateRegionFromPictureRequest.lib.restype = ctypes.c_uint32
        CreateRegionFromPictureRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class CreateRegionFromPictureRequestCType(ctypes.Structure):
    """xfixes CreateRegionFromPicture"""
    _fields_ = [
        ("region", ctypes.c_uint32),
        ("picture", ctypes.c_uint32),
    ]


DestroyRegionRequestPacket = DataPacket((
    ('region', FixedDataPacketField(MARKER_UINT32)),
))


class DestroyRegionRequest:
    OPCODE = 10

    __slots__ = ('region',)

    def __init__(
            self, *,
            region: Optional[int] = None,
    ) -> None:
        self.region = region

    def as_dict(self) -> Dict[str, Any]:
        return {
            'region': self.region,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DestroyRegionRequest':
        return DestroyRegionRequest(**DestroyRegionRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DestroyRegionRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        DestroyRegionRequest.lib = library.xfixes_destroyregion
        DestroyRegionRequest.lib.restype = ctypes.c_uint32
        DestroyRegionRequest.lib.argstype = (ctypes.c_uint32,)


class DestroyRegionRequestCType(ctypes.Structure):
    """xfixes DestroyRegion"""
    _fields_ = [
        ("region", ctypes.c_uint32),
    ]


SetRegionRequestPacket = DataPacket((
    ('region', FixedDataPacketField(MARKER_UINT32)),
    ('rectangles', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 1, 0)),
))


class SetRegionRequest:
    OPCODE = 11

    __slots__ = ('region', 'rectangles',)

    def __init__(
            self, *,
            region: Optional[int] = None,
            rectangles: Optional[Sequence[int]] = None,
    ) -> None:
        self.region = region
        self.rectangles = rectangles

    def as_dict(self) -> Dict[str, Any]:
        return {
            'region': self.region,
            'rectangles': self.rectangles,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetRegionRequest':
        return SetRegionRequest(**SetRegionRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetRegionRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetRegionRequest.lib = library.xfixes_setregion
        SetRegionRequest.lib.restype = ctypes.c_uint32
        SetRegionRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_void_p)


class SetRegionRequestCType(ctypes.Structure):
    """xfixes SetRegion"""
    _fields_ = [
        ("region", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


CopyRegionRequestPacket = DataPacket((
    ('source', FixedDataPacketField(MARKER_UINT32)),
    ('destination', FixedDataPacketField(MARKER_UINT32)),
))


class CopyRegionRequest:
    OPCODE = 12

    __slots__ = ('source', 'destination',)

    def __init__(
            self, *,
            source: Optional[int] = None,
            destination: Optional[int] = None,
    ) -> None:
        self.source = source
        self.destination = destination

    def as_dict(self) -> Dict[str, Any]:
        return {
            'source': self.source,
            'destination': self.destination,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CopyRegionRequest':
        return CopyRegionRequest(**CopyRegionRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CopyRegionRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CopyRegionRequest.lib = library.xfixes_copyregion
        CopyRegionRequest.lib.restype = ctypes.c_uint32
        CopyRegionRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class CopyRegionRequestCType(ctypes.Structure):
    """xfixes CopyRegion"""
    _fields_ = [
        ("source", ctypes.c_uint32),
        ("destination", ctypes.c_uint32),
    ]


UnionRegionRequestPacket = DataPacket((
    ('source1', FixedDataPacketField(MARKER_UINT32)),
    ('source2', FixedDataPacketField(MARKER_UINT32)),
    ('destination', FixedDataPacketField(MARKER_UINT32)),
))


class UnionRegionRequest:
    OPCODE = 13

    __slots__ = ('source1', 'source2', 'destination',)

    def __init__(
            self, *,
            source1: Optional[int] = None,
            source2: Optional[int] = None,
            destination: Optional[int] = None,
    ) -> None:
        self.source1 = source1
        self.source2 = source2
        self.destination = destination

    def as_dict(self) -> Dict[str, Any]:
        return {
            'source1': self.source1,
            'source2': self.source2,
            'destination': self.destination,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'UnionRegionRequest':
        return UnionRegionRequest(**UnionRegionRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return UnionRegionRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        UnionRegionRequest.lib = library.xfixes_unionregion
        UnionRegionRequest.lib.restype = ctypes.c_uint32
        UnionRegionRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class UnionRegionRequestCType(ctypes.Structure):
    """xfixes UnionRegion"""
    _fields_ = [
        ("source1", ctypes.c_uint32),
        ("source2", ctypes.c_uint32),
        ("destination", ctypes.c_uint32),
    ]


IntersectRegionRequestPacket = DataPacket((
    ('source1', FixedDataPacketField(MARKER_UINT32)),
    ('source2', FixedDataPacketField(MARKER_UINT32)),
    ('destination', FixedDataPacketField(MARKER_UINT32)),
))


class IntersectRegionRequest:
    OPCODE = 14

    __slots__ = ('source1', 'source2', 'destination',)

    def __init__(
            self, *,
            source1: Optional[int] = None,
            source2: Optional[int] = None,
            destination: Optional[int] = None,
    ) -> None:
        self.source1 = source1
        self.source2 = source2
        self.destination = destination

    def as_dict(self) -> Dict[str, Any]:
        return {
            'source1': self.source1,
            'source2': self.source2,
            'destination': self.destination,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'IntersectRegionRequest':
        return IntersectRegionRequest(**IntersectRegionRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return IntersectRegionRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        IntersectRegionRequest.lib = library.xfixes_intersectregion
        IntersectRegionRequest.lib.restype = ctypes.c_uint32
        IntersectRegionRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class IntersectRegionRequestCType(ctypes.Structure):
    """xfixes IntersectRegion"""
    _fields_ = [
        ("source1", ctypes.c_uint32),
        ("source2", ctypes.c_uint32),
        ("destination", ctypes.c_uint32),
    ]


SubtractRegionRequestPacket = DataPacket((
    ('source1', FixedDataPacketField(MARKER_UINT32)),
    ('source2', FixedDataPacketField(MARKER_UINT32)),
    ('destination', FixedDataPacketField(MARKER_UINT32)),
))


class SubtractRegionRequest:
    OPCODE = 15

    __slots__ = ('source1', 'source2', 'destination',)

    def __init__(
            self, *,
            source1: Optional[int] = None,
            source2: Optional[int] = None,
            destination: Optional[int] = None,
    ) -> None:
        self.source1 = source1
        self.source2 = source2
        self.destination = destination

    def as_dict(self) -> Dict[str, Any]:
        return {
            'source1': self.source1,
            'source2': self.source2,
            'destination': self.destination,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SubtractRegionRequest':
        return SubtractRegionRequest(**SubtractRegionRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SubtractRegionRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SubtractRegionRequest.lib = library.xfixes_subtractregion
        SubtractRegionRequest.lib.restype = ctypes.c_uint32
        SubtractRegionRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class SubtractRegionRequestCType(ctypes.Structure):
    """xfixes SubtractRegion"""
    _fields_ = [
        ("source1", ctypes.c_uint32),
        ("source2", ctypes.c_uint32),
        ("destination", ctypes.c_uint32),
    ]


InvertRegionRequestPacket = DataPacket((
    ('source', FixedDataPacketField(MARKER_UINT32)),
    ('bounds', FixedDataPacketField(MARKER_UINT32)),
    ('destination', FixedDataPacketField(MARKER_UINT32)),
))


class InvertRegionRequest:
    OPCODE = 16

    __slots__ = ('source', 'bounds', 'destination',)

    def __init__(
            self, *,
            source: Optional[int] = None,
            bounds: Optional[int] = None,
            destination: Optional[int] = None,
    ) -> None:
        self.source = source
        self.bounds = bounds
        self.destination = destination

    def as_dict(self) -> Dict[str, Any]:
        return {
            'source': self.source,
            'bounds': self.bounds,
            'destination': self.destination,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'InvertRegionRequest':
        return InvertRegionRequest(**InvertRegionRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return InvertRegionRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        InvertRegionRequest.lib = library.xfixes_invertregion
        InvertRegionRequest.lib.restype = ctypes.c_uint32
        InvertRegionRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class InvertRegionRequestCType(ctypes.Structure):
    """xfixes InvertRegion"""
    _fields_ = [
        ("source", ctypes.c_uint32),
        ("bounds", ctypes.c_uint32),
        ("destination", ctypes.c_uint32),
    ]


TranslateRegionRequestPacket = DataPacket((
    ('region', FixedDataPacketField(MARKER_UINT32)),
    ('dx', FixedDataPacketField(MARKER_INT16)),
    ('dy', FixedDataPacketField(MARKER_INT16)),
))


class TranslateRegionRequest:
    OPCODE = 17

    __slots__ = ('region', 'dx', 'dy',)

    def __init__(
            self, *,
            region: Optional[int] = None,
            dx: Optional[int] = None,
            dy: Optional[int] = None,
    ) -> None:
        self.region = region
        self.dx = dx
        self.dy = dy

    def as_dict(self) -> Dict[str, Any]:
        return {
            'region': self.region,
            'dx': self.dx,
            'dy': self.dy,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'TranslateRegionRequest':
        return TranslateRegionRequest(**TranslateRegionRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return TranslateRegionRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        TranslateRegionRequest.lib = library.xfixes_translateregion
        TranslateRegionRequest.lib.restype = ctypes.c_uint32
        TranslateRegionRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16)


class TranslateRegionRequestCType(ctypes.Structure):
    """xfixes TranslateRegion"""
    _fields_ = [
        ("region", ctypes.c_uint32),
        ("dx", ctypes.c_int16),
        ("dy", ctypes.c_int16),
    ]


RegionExtentsRequestPacket = DataPacket((
    ('source', FixedDataPacketField(MARKER_UINT32)),
    ('destination', FixedDataPacketField(MARKER_UINT32)),
))


class RegionExtentsRequest:
    OPCODE = 18

    __slots__ = ('source', 'destination',)

    def __init__(
            self, *,
            source: Optional[int] = None,
            destination: Optional[int] = None,
    ) -> None:
        self.source = source
        self.destination = destination

    def as_dict(self) -> Dict[str, Any]:
        return {
            'source': self.source,
            'destination': self.destination,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'RegionExtentsRequest':
        return RegionExtentsRequest(**RegionExtentsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return RegionExtentsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        RegionExtentsRequest.lib = library.xfixes_regionextents
        RegionExtentsRequest.lib.restype = ctypes.c_uint32
        RegionExtentsRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class RegionExtentsRequestCType(ctypes.Structure):
    """xfixes RegionExtents"""
    _fields_ = [
        ("source", ctypes.c_uint32),
        ("destination", ctypes.c_uint32),
    ]


FetchRegionRequestCookie = NewType('FetchRegionRequestCookie', ctypes.c_uint32)


FetchRegionRequestPacket = DataPacket((
    ('region', FixedDataPacketField(MARKER_UINT32)),
))


class FetchRegionRequest:
    OPCODE = 19

    __slots__ = ('region',)

    def __init__(
            self, *,
            region: Optional[int] = None,
    ) -> None:
        self.region = region

    def as_dict(self) -> Dict[str, Any]:
        return {
            'region': self.region,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'FetchRegionRequest':
        return FetchRegionRequest(**FetchRegionRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return FetchRegionRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], FetchRegionRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        FetchRegionRequest.lib = library.xfixes_fetchregion
        FetchRegionRequest.lib.restype = FetchRegionRequestCookie
        FetchRegionRequest.lib.argstype = (ctypes.c_uint32,)


class FetchRegionRequestCType(ctypes.Structure):
    """xfixes FetchRegion"""
    _fields_ = [
        ("region", ctypes.c_uint32),
    ]


FetchRegionReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('extents', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(16)),
    ('rectangles', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: (d['length']) / (2), 0)),
))


class FetchRegionReplyReply:
    __slots__ = ('extents', 'rectangles',)

    def __init__(
            self, *,
            extents: Optional[int] = None,
            rectangles: Optional[Sequence[int]] = None,
    ) -> None:
        self.extents = extents
        self.rectangles = rectangles

    def as_dict(self) -> Dict[str, Any]:
        return {
            'extents': self.extents,
            'rectangles': self.rectangles,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'FetchRegionReplyReply':
        return FetchRegionReplyReply(**FetchRegionReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return FetchRegionReplyReplyPacket.pack(**self.as_dict())


class FetchRegionReplyReplyCType(ctypes.Structure):
    """xfixes FetchRegion_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("extents", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 16),
        ("var_data", ctypes.c_void_p),
    ]


SetGcclipRegionRequestPacket = DataPacket((
    ('gc', FixedDataPacketField(MARKER_UINT32)),
    ('region', FixedDataPacketField(MARKER_UINT32)),
    ('x_origin', FixedDataPacketField(MARKER_INT16)),
    ('y_origin', FixedDataPacketField(MARKER_INT16)),
))


class SetGcclipRegionRequest:
    OPCODE = 20

    __slots__ = ('gc', 'region', 'x_origin', 'y_origin',)

    def __init__(
            self, *,
            gc: Optional[int] = None,
            region: Optional[int] = None,
            x_origin: Optional[int] = None,
            y_origin: Optional[int] = None,
    ) -> None:
        self.gc = gc
        self.region = region
        self.x_origin = x_origin
        self.y_origin = y_origin

    def as_dict(self) -> Dict[str, Any]:
        return {
            'gc': self.gc,
            'region': self.region,
            'x_origin': self.x_origin,
            'y_origin': self.y_origin,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetGcclipRegionRequest':
        return SetGcclipRegionRequest(**SetGcclipRegionRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetGcclipRegionRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetGcclipRegionRequest.lib = library.xfixes_setgcclipregion
        SetGcclipRegionRequest.lib.restype = ctypes.c_uint32
        SetGcclipRegionRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16)


class SetGcclipRegionRequestCType(ctypes.Structure):
    """xfixes SetGCClipRegion"""
    _fields_ = [
        ("gc", ctypes.c_uint32),
        ("region", ctypes.c_uint32),
        ("x_origin", ctypes.c_int16),
        ("y_origin", ctypes.c_int16),
    ]


SetWindowShapeRegionRequestPacket = DataPacket((
    ('dest', FixedDataPacketField(MARKER_UINT32)),
    ('dest_kind', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(3)),
    ('x_offset', FixedDataPacketField(MARKER_INT16)),
    ('y_offset', FixedDataPacketField(MARKER_INT16)),
    ('region', FixedDataPacketField(MARKER_UINT32)),
))


class SetWindowShapeRegionRequest:
    OPCODE = 21

    __slots__ = ('dest', 'dest_kind', 'x_offset', 'y_offset', 'region',)

    def __init__(
            self, *,
            dest: Optional[int] = None,
            dest_kind: Optional[int] = None,
            x_offset: Optional[int] = None,
            y_offset: Optional[int] = None,
            region: Optional[int] = None,
    ) -> None:
        self.dest = dest
        self.dest_kind = dest_kind
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.region = region

    def as_dict(self) -> Dict[str, Any]:
        return {
            'dest': self.dest,
            'dest_kind': self.dest_kind,
            'x_offset': self.x_offset,
            'y_offset': self.y_offset,
            'region': self.region,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetWindowShapeRegionRequest':
        return SetWindowShapeRegionRequest(**SetWindowShapeRegionRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetWindowShapeRegionRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetWindowShapeRegionRequest.lib = library.xfixes_setwindowshaperegion
        SetWindowShapeRegionRequest.lib.restype = ctypes.c_uint32
        SetWindowShapeRegionRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8 * 3, ctypes.c_int16, ctypes.c_int16, ctypes.c_uint32)


class SetWindowShapeRegionRequestCType(ctypes.Structure):
    """xfixes SetWindowShapeRegion"""
    _fields_ = [
        ("dest", ctypes.c_uint32),
        ("dest_kind", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 3),
        ("x_offset", ctypes.c_int16),
        ("y_offset", ctypes.c_int16),
        ("region", ctypes.c_uint32),
    ]


SetPictureClipRegionRequestPacket = DataPacket((
    ('picture', FixedDataPacketField(MARKER_UINT32)),
    ('region', FixedDataPacketField(MARKER_UINT32)),
    ('x_origin', FixedDataPacketField(MARKER_INT16)),
    ('y_origin', FixedDataPacketField(MARKER_INT16)),
))


class SetPictureClipRegionRequest:
    OPCODE = 22

    __slots__ = ('picture', 'region', 'x_origin', 'y_origin',)

    def __init__(
            self, *,
            picture: Optional[int] = None,
            region: Optional[int] = None,
            x_origin: Optional[int] = None,
            y_origin: Optional[int] = None,
    ) -> None:
        self.picture = picture
        self.region = region
        self.x_origin = x_origin
        self.y_origin = y_origin

    def as_dict(self) -> Dict[str, Any]:
        return {
            'picture': self.picture,
            'region': self.region,
            'x_origin': self.x_origin,
            'y_origin': self.y_origin,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetPictureClipRegionRequest':
        return SetPictureClipRegionRequest(**SetPictureClipRegionRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetPictureClipRegionRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetPictureClipRegionRequest.lib = library.xfixes_setpictureclipregion
        SetPictureClipRegionRequest.lib.restype = ctypes.c_uint32
        SetPictureClipRegionRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16)


class SetPictureClipRegionRequestCType(ctypes.Structure):
    """xfixes SetPictureClipRegion"""
    _fields_ = [
        ("picture", ctypes.c_uint32),
        ("region", ctypes.c_uint32),
        ("x_origin", ctypes.c_int16),
        ("y_origin", ctypes.c_int16),
    ]


SetCursorNameRequestPacket = DataPacket((
    ('cursor', FixedDataPacketField(MARKER_UINT32)),
    ('nbytes', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
    ('name', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['nbytes'], 0)),
))


class SetCursorNameRequest:
    OPCODE = 23

    __slots__ = ('cursor', 'nbytes', 'name',)

    def __init__(
            self, *,
            cursor: Optional[int] = None,
            nbytes: Optional[int] = None,
            name: Optional[Sequence[int]] = None,
    ) -> None:
        self.cursor = cursor
        self.nbytes = nbytes
        self.name = name

    def as_dict(self) -> Dict[str, Any]:
        return {
            'cursor': self.cursor,
            'nbytes': self.nbytes,
            'name': self.name,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetCursorNameRequest':
        return SetCursorNameRequest(**SetCursorNameRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetCursorNameRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetCursorNameRequest.lib = library.xfixes_setcursorname
        SetCursorNameRequest.lib.restype = ctypes.c_uint32
        SetCursorNameRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint8 * 2, ctypes.c_void_p)


class SetCursorNameRequestCType(ctypes.Structure):
    """xfixes SetCursorName"""
    _fields_ = [
        ("cursor", ctypes.c_uint32),
        ("nbytes", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


GetCursorNameRequestCookie = NewType('GetCursorNameRequestCookie', ctypes.c_uint32)


GetCursorNameRequestPacket = DataPacket((
    ('cursor', FixedDataPacketField(MARKER_UINT32)),
))


class GetCursorNameRequest:
    OPCODE = 24

    __slots__ = ('cursor',)

    def __init__(
            self, *,
            cursor: Optional[int] = None,
    ) -> None:
        self.cursor = cursor

    def as_dict(self) -> Dict[str, Any]:
        return {
            'cursor': self.cursor,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetCursorNameRequest':
        return GetCursorNameRequest(**GetCursorNameRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetCursorNameRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetCursorNameRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetCursorNameRequest.lib = library.xfixes_getcursorname
        GetCursorNameRequest.lib.restype = GetCursorNameRequestCookie
        GetCursorNameRequest.lib.argstype = (ctypes.c_uint32,)


class GetCursorNameRequestCType(ctypes.Structure):
    """xfixes GetCursorName"""
    _fields_ = [
        ("cursor", ctypes.c_uint32),
    ]


GetCursorNameReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('atom', FixedDataPacketField(MARKER_UINT32)),
    ('nbytes', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(18)),
    ('name', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['nbytes'], 0)),
))


class GetCursorNameReplyReply:
    __slots__ = ('atom', 'nbytes', 'name',)

    def __init__(
            self, *,
            atom: Optional[int] = None,
            nbytes: Optional[int] = None,
            name: Optional[Sequence[int]] = None,
    ) -> None:
        self.atom = atom
        self.nbytes = nbytes
        self.name = name

    def as_dict(self) -> Dict[str, Any]:
        return {
            'atom': self.atom,
            'nbytes': self.nbytes,
            'name': self.name,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetCursorNameReplyReply':
        return GetCursorNameReplyReply(**GetCursorNameReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetCursorNameReplyReplyPacket.pack(**self.as_dict())


class GetCursorNameReplyReplyCType(ctypes.Structure):
    """xfixes GetCursorName_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("atom", ctypes.c_uint32),
        ("nbytes", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 18),
        ("var_data", ctypes.c_void_p),
    ]


GetCursorImageAndNameRequestCookie = NewType('GetCursorImageAndNameRequestCookie', ctypes.c_uint32)


GetCursorImageAndNameRequestPacket = DataPacket((
))


class GetCursorImageAndNameRequest:
    OPCODE = 25

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetCursorImageAndNameRequest':
        return GetCursorImageAndNameRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], GetCursorImageAndNameRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetCursorImageAndNameRequest.lib = library.xfixes_getcursorimageandname
        GetCursorImageAndNameRequest.lib.restype = GetCursorImageAndNameRequestCookie
        GetCursorImageAndNameRequest.lib.argstype = ()


class GetCursorImageAndNameRequestCType(ctypes.Structure):
    """xfixes GetCursorImageAndName"""
    _fields_ = [
    ]


GetCursorImageAndNameReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('x', FixedDataPacketField(MARKER_INT16)),
    ('y', FixedDataPacketField(MARKER_INT16)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('xhot', FixedDataPacketField(MARKER_UINT16)),
    ('yhot', FixedDataPacketField(MARKER_UINT16)),
    ('cursor_serial', FixedDataPacketField(MARKER_UINT32)),
    ('cursor_atom', FixedDataPacketField(MARKER_UINT32)),
    ('nbytes', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(2)),
    ('cursor_image', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: (d['width']) * (d['height']), 0)),
    ('name', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['nbytes'], 0)),
))


class GetCursorImageAndNameReplyReply:
    __slots__ = ('x', 'y', 'width', 'height', 'xhot', 'yhot', 'cursor_serial', 'cursor_atom', 'nbytes', 'cursor_image', 'name',)

    def __init__(
            self, *,
            x: Optional[int] = None,
            y: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            xhot: Optional[int] = None,
            yhot: Optional[int] = None,
            cursor_serial: Optional[int] = None,
            cursor_atom: Optional[int] = None,
            nbytes: Optional[int] = None,
            cursor_image: Optional[Sequence[int]] = None,
            name: Optional[Sequence[int]] = None,
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.xhot = xhot
        self.yhot = yhot
        self.cursor_serial = cursor_serial
        self.cursor_atom = cursor_atom
        self.nbytes = nbytes
        self.cursor_image = cursor_image
        self.name = name

    def as_dict(self) -> Dict[str, Any]:
        return {
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height,
            'xhot': self.xhot,
            'yhot': self.yhot,
            'cursor_serial': self.cursor_serial,
            'cursor_atom': self.cursor_atom,
            'nbytes': self.nbytes,
            'cursor_image': self.cursor_image,
            'name': self.name,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetCursorImageAndNameReplyReply':
        return GetCursorImageAndNameReplyReply(**GetCursorImageAndNameReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetCursorImageAndNameReplyReplyPacket.pack(**self.as_dict())


class GetCursorImageAndNameReplyReplyCType(ctypes.Structure):
    """xfixes GetCursorImageAndName_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("x", ctypes.c_int16),
        ("y", ctypes.c_int16),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("xhot", ctypes.c_uint16),
        ("yhot", ctypes.c_uint16),
        ("cursor_serial", ctypes.c_uint32),
        ("cursor_atom", ctypes.c_uint32),
        ("nbytes", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


ChangeCursorRequestPacket = DataPacket((
    ('source', FixedDataPacketField(MARKER_UINT32)),
    ('destination', FixedDataPacketField(MARKER_UINT32)),
))


class ChangeCursorRequest:
    OPCODE = 26

    __slots__ = ('source', 'destination',)

    def __init__(
            self, *,
            source: Optional[int] = None,
            destination: Optional[int] = None,
    ) -> None:
        self.source = source
        self.destination = destination

    def as_dict(self) -> Dict[str, Any]:
        return {
            'source': self.source,
            'destination': self.destination,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ChangeCursorRequest':
        return ChangeCursorRequest(**ChangeCursorRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ChangeCursorRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ChangeCursorRequest.lib = library.xfixes_changecursor
        ChangeCursorRequest.lib.restype = ctypes.c_uint32
        ChangeCursorRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class ChangeCursorRequestCType(ctypes.Structure):
    """xfixes ChangeCursor"""
    _fields_ = [
        ("source", ctypes.c_uint32),
        ("destination", ctypes.c_uint32),
    ]


ChangeCursorByNameRequestPacket = DataPacket((
    ('src', FixedDataPacketField(MARKER_UINT32)),
    ('nbytes', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
    ('name', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['nbytes'], 0)),
))


class ChangeCursorByNameRequest:
    OPCODE = 27

    __slots__ = ('src', 'nbytes', 'name',)

    def __init__(
            self, *,
            src: Optional[int] = None,
            nbytes: Optional[int] = None,
            name: Optional[Sequence[int]] = None,
    ) -> None:
        self.src = src
        self.nbytes = nbytes
        self.name = name

    def as_dict(self) -> Dict[str, Any]:
        return {
            'src': self.src,
            'nbytes': self.nbytes,
            'name': self.name,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ChangeCursorByNameRequest':
        return ChangeCursorByNameRequest(**ChangeCursorByNameRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ChangeCursorByNameRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ChangeCursorByNameRequest.lib = library.xfixes_changecursorbyname
        ChangeCursorByNameRequest.lib.restype = ctypes.c_uint32
        ChangeCursorByNameRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint8 * 2, ctypes.c_void_p)


class ChangeCursorByNameRequestCType(ctypes.Structure):
    """xfixes ChangeCursorByName"""
    _fields_ = [
        ("src", ctypes.c_uint32),
        ("nbytes", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


ExpandRegionRequestPacket = DataPacket((
    ('source', FixedDataPacketField(MARKER_UINT32)),
    ('destination', FixedDataPacketField(MARKER_UINT32)),
    ('left', FixedDataPacketField(MARKER_UINT16)),
    ('right', FixedDataPacketField(MARKER_UINT16)),
    ('top', FixedDataPacketField(MARKER_UINT16)),
    ('bottom', FixedDataPacketField(MARKER_UINT16)),
))


class ExpandRegionRequest:
    OPCODE = 28

    __slots__ = ('source', 'destination', 'left', 'right', 'top', 'bottom',)

    def __init__(
            self, *,
            source: Optional[int] = None,
            destination: Optional[int] = None,
            left: Optional[int] = None,
            right: Optional[int] = None,
            top: Optional[int] = None,
            bottom: Optional[int] = None,
    ) -> None:
        self.source = source
        self.destination = destination
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    def as_dict(self) -> Dict[str, Any]:
        return {
            'source': self.source,
            'destination': self.destination,
            'left': self.left,
            'right': self.right,
            'top': self.top,
            'bottom': self.bottom,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ExpandRegionRequest':
        return ExpandRegionRequest(**ExpandRegionRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ExpandRegionRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ExpandRegionRequest.lib = library.xfixes_expandregion
        ExpandRegionRequest.lib.restype = ctypes.c_uint32
        ExpandRegionRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16)


class ExpandRegionRequestCType(ctypes.Structure):
    """xfixes ExpandRegion"""
    _fields_ = [
        ("source", ctypes.c_uint32),
        ("destination", ctypes.c_uint32),
        ("left", ctypes.c_uint16),
        ("right", ctypes.c_uint16),
        ("top", ctypes.c_uint16),
        ("bottom", ctypes.c_uint16),
    ]


HideCursorRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class HideCursorRequest:
    OPCODE = 29

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
    def from_data(inp: BinaryIO) -> 'HideCursorRequest':
        return HideCursorRequest(**HideCursorRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return HideCursorRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        HideCursorRequest.lib = library.xfixes_hidecursor
        HideCursorRequest.lib.restype = ctypes.c_uint32
        HideCursorRequest.lib.argstype = (ctypes.c_uint32,)


class HideCursorRequestCType(ctypes.Structure):
    """xfixes HideCursor"""
    _fields_ = [
        ("window", ctypes.c_uint32),
    ]


ShowCursorRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class ShowCursorRequest:
    OPCODE = 30

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
    def from_data(inp: BinaryIO) -> 'ShowCursorRequest':
        return ShowCursorRequest(**ShowCursorRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ShowCursorRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ShowCursorRequest.lib = library.xfixes_showcursor
        ShowCursorRequest.lib.restype = ctypes.c_uint32
        ShowCursorRequest.lib.argstype = (ctypes.c_uint32,)


class ShowCursorRequestCType(ctypes.Structure):
    """xfixes ShowCursor"""
    _fields_ = [
        ("window", ctypes.c_uint32),
    ]


CreatePointerBarrierRequestPacket = DataPacket((
    ('barrier', FixedDataPacketField(MARKER_UINT32)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('x1', FixedDataPacketField(MARKER_UINT16)),
    ('y1', FixedDataPacketField(MARKER_UINT16)),
    ('x2', FixedDataPacketField(MARKER_UINT16)),
    ('y2', FixedDataPacketField(MARKER_UINT16)),
    ('directions', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(2)),
    ('num_devices', FixedDataPacketField(MARKER_UINT16)),
    ('devices', SimpleListDataPacketField(MARKER_UINT16, lambda d, c: d['num_devices'], 0)),
))


class CreatePointerBarrierRequest:
    OPCODE = 31

    __slots__ = ('barrier', 'window', 'x1', 'y1', 'x2', 'y2', 'directions', 'num_devices', 'devices',)

    def __init__(
            self, *,
            barrier: Optional[int] = None,
            window: Optional[int] = None,
            x1: Optional[int] = None,
            y1: Optional[int] = None,
            x2: Optional[int] = None,
            y2: Optional[int] = None,
            directions: Optional[int] = None,
            num_devices: Optional[int] = None,
            devices: Optional[Sequence[int]] = None,
    ) -> None:
        self.barrier = barrier
        self.window = window
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.directions = directions
        self.num_devices = num_devices
        self.devices = devices

    def as_dict(self) -> Dict[str, Any]:
        return {
            'barrier': self.barrier,
            'window': self.window,
            'x1': self.x1,
            'y1': self.y1,
            'x2': self.x2,
            'y2': self.y2,
            'directions': self.directions,
            'num_devices': self.num_devices,
            'devices': self.devices,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreatePointerBarrierRequest':
        return CreatePointerBarrierRequest(**CreatePointerBarrierRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreatePointerBarrierRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreatePointerBarrierRequest.lib = library.xfixes_createpointerbarrier
        CreatePointerBarrierRequest.lib.restype = ctypes.c_uint32
        CreatePointerBarrierRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint32, ctypes.c_uint8 * 2, ctypes.c_uint16, ctypes.c_void_p)


class CreatePointerBarrierRequestCType(ctypes.Structure):
    """xfixes CreatePointerBarrier"""
    _fields_ = [
        ("barrier", ctypes.c_uint32),
        ("window", ctypes.c_uint32),
        ("x1", ctypes.c_uint16),
        ("y1", ctypes.c_uint16),
        ("x2", ctypes.c_uint16),
        ("y2", ctypes.c_uint16),
        ("directions", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 2),
        ("num_devices", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


DeletePointerBarrierRequestPacket = DataPacket((
    ('barrier', FixedDataPacketField(MARKER_UINT32)),
))


class DeletePointerBarrierRequest:
    OPCODE = 32

    __slots__ = ('barrier',)

    def __init__(
            self, *,
            barrier: Optional[int] = None,
    ) -> None:
        self.barrier = barrier

    def as_dict(self) -> Dict[str, Any]:
        return {
            'barrier': self.barrier,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeletePointerBarrierRequest':
        return DeletePointerBarrierRequest(**DeletePointerBarrierRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeletePointerBarrierRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        DeletePointerBarrierRequest.lib = library.xfixes_deletepointerbarrier
        DeletePointerBarrierRequest.lib.restype = ctypes.c_uint32
        DeletePointerBarrierRequest.lib.argstype = (ctypes.c_uint32,)


class DeletePointerBarrierRequestCType(ctypes.Structure):
    """xfixes DeletePointerBarrier"""
    _fields_ = [
        ("barrier", ctypes.c_uint32),
    ]


SetClientDisconnectModeRequestPacket = DataPacket((
    ('disconnect_mode', FixedDataPacketField(MARKER_UINT32)),
))


class SetClientDisconnectModeRequest:
    OPCODE = 33

    __slots__ = ('disconnect_mode',)

    def __init__(
            self, *,
            disconnect_mode: Optional[int] = None,
    ) -> None:
        self.disconnect_mode = disconnect_mode

    def as_dict(self) -> Dict[str, Any]:
        return {
            'disconnect_mode': self.disconnect_mode,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetClientDisconnectModeRequest':
        return SetClientDisconnectModeRequest(**SetClientDisconnectModeRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetClientDisconnectModeRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetClientDisconnectModeRequest.lib = library.xfixes_setclientdisconnectmode
        SetClientDisconnectModeRequest.lib.restype = ctypes.c_uint32
        SetClientDisconnectModeRequest.lib.argstype = (ctypes.c_uint32,)


class SetClientDisconnectModeRequestCType(ctypes.Structure):
    """xfixes SetClientDisconnectMode"""
    _fields_ = [
        ("disconnect_mode", ctypes.c_uint32),
    ]


GetClientDisconnectModeRequestCookie = NewType('GetClientDisconnectModeRequestCookie', ctypes.c_uint32)


GetClientDisconnectModeRequestPacket = DataPacket((
))


class GetClientDisconnectModeRequest:
    OPCODE = 34

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetClientDisconnectModeRequest':
        return GetClientDisconnectModeRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], GetClientDisconnectModeRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetClientDisconnectModeRequest.lib = library.xfixes_getclientdisconnectmode
        GetClientDisconnectModeRequest.lib.restype = GetClientDisconnectModeRequestCookie
        GetClientDisconnectModeRequest.lib.argstype = ()


class GetClientDisconnectModeRequestCType(ctypes.Structure):
    """xfixes GetClientDisconnectMode"""
    _fields_ = [
    ]


GetClientDisconnectModeReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('disconnect_mode', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
))


class GetClientDisconnectModeReplyReply:
    __slots__ = ('disconnect_mode',)

    def __init__(
            self, *,
            disconnect_mode: Optional[int] = None,
    ) -> None:
        self.disconnect_mode = disconnect_mode

    def as_dict(self) -> Dict[str, Any]:
        return {
            'disconnect_mode': self.disconnect_mode,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetClientDisconnectModeReplyReply':
        return GetClientDisconnectModeReplyReply(**GetClientDisconnectModeReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetClientDisconnectModeReplyReplyPacket.pack(**self.as_dict())


class GetClientDisconnectModeReplyReplyCType(ctypes.Structure):
    """xfixes GetClientDisconnectMode_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("disconnect_mode", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
    ]


# ------------------------------------------------------------------
# Unions

