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

KindType = NewType('KindType', int)


class KindValues:
    BLANKED = KindType(0)
    INTERNAL = KindType(1)
    EXTERNAL = KindType(2)


EventType = NewType('EventType', int)


class EventValues:
    NOTIFY_MASK = EventType(1)
    CYCLE_MASK = EventType(2)


StateType = NewType('StateType', int)


class StateValues:
    OFF = StateType(0)
    ON = StateType(1)
    CYCLE = StateType(2)
    DISABLED = StateType(3)


# ------------------------------------------------------------------
# Aliases



# ------------------------------------------------------------------
# Structures, Events, Requests, Replies


QueryVersionRequestCookie = NewType('QueryVersionRequestCookie', ctypes.c_uint32)


QueryVersionRequestPacket = DataPacket((
    ('client_major_version', FixedDataPacketField(MARKER_UINT8)),
    ('client_minor_version', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
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
        QueryVersionRequest.lib = library.screensaver_queryversion
        QueryVersionRequest.lib.restype = QueryVersionRequestCookie
        QueryVersionRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8 * 2)


class QueryVersionRequestCType(ctypes.Structure):
    """screensaver QueryVersion"""
    _fields_ = [
        ("client_major_version", ctypes.c_uint8),
        ("client_minor_version", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 2),
    ]


QueryVersionReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('server_major_version', FixedDataPacketField(MARKER_UINT16)),
    ('server_minor_version', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(20)),
))


class QueryVersionReplyReply:
    __slots__ = ('server_major_version', 'server_minor_version',)

    def __init__(
            self, *,
            server_major_version: Optional[int] = None,
            server_minor_version: Optional[int] = None,
    ) -> None:
        self.server_major_version = server_major_version
        self.server_minor_version = server_minor_version

    def as_dict(self) -> Dict[str, Any]:
        return {
            'server_major_version': self.server_major_version,
            'server_minor_version': self.server_minor_version,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryVersionReplyReply':
        return QueryVersionReplyReply(**QueryVersionReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryVersionReplyReplyPacket.pack(**self.as_dict())


class QueryVersionReplyReplyCType(ctypes.Structure):
    """screensaver QueryVersion_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("server_major_version", ctypes.c_uint16),
        ("server_minor_version", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 20),
    ]


QueryInfoRequestCookie = NewType('QueryInfoRequestCookie', ctypes.c_uint32)


QueryInfoRequestPacket = DataPacket((
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
))


class QueryInfoRequest:
    OPCODE = 1

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
    def from_data(inp: BinaryIO) -> 'QueryInfoRequest':
        return QueryInfoRequest(**QueryInfoRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryInfoRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], QueryInfoRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryInfoRequest.lib = library.screensaver_queryinfo
        QueryInfoRequest.lib.restype = QueryInfoRequestCookie
        QueryInfoRequest.lib.argstype = (ctypes.c_uint32,)


class QueryInfoRequestCType(ctypes.Structure):
    """screensaver QueryInfo"""
    _fields_ = [
        ("drawable", ctypes.c_uint32),
    ]


QueryInfoReplyReplyPacket = DataPacket((
    ('state', FixedDataPacketField(MARKER_UINT8)),
    ('saver_window', FixedDataPacketField(MARKER_UINT32)),
    ('ms_until_server', FixedDataPacketField(MARKER_UINT32)),
    ('ms_since_user_input', FixedDataPacketField(MARKER_UINT32)),
    ('event_mask', FixedDataPacketField(MARKER_UINT32)),
    ('kind', FixedDataPacketField(MARKER_INT8)),
    ('pad0', FixedPadDataPacketField(7)),
))


class QueryInfoReplyReply:
    __slots__ = ('state', 'saver_window', 'ms_until_server', 'ms_since_user_input', 'event_mask', 'kind',)

    def __init__(
            self, *,
            state: Optional[int] = None,
            saver_window: Optional[int] = None,
            ms_until_server: Optional[int] = None,
            ms_since_user_input: Optional[int] = None,
            event_mask: Optional[int] = None,
            kind: Optional[int] = None,
    ) -> None:
        self.state = state
        self.saver_window = saver_window
        self.ms_until_server = ms_until_server
        self.ms_since_user_input = ms_since_user_input
        self.event_mask = event_mask
        self.kind = kind

    def as_dict(self) -> Dict[str, Any]:
        return {
            'state': self.state,
            'saver_window': self.saver_window,
            'ms_until_server': self.ms_until_server,
            'ms_since_user_input': self.ms_since_user_input,
            'event_mask': self.event_mask,
            'kind': self.kind,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryInfoReplyReply':
        return QueryInfoReplyReply(**QueryInfoReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryInfoReplyReplyPacket.pack(**self.as_dict())


class QueryInfoReplyReplyCType(ctypes.Structure):
    """screensaver QueryInfo_reply"""
    _fields_ = [
        ("state", ctypes.c_uint8),
        ("saver_window", ctypes.c_uint32),
        ("ms_until_server", ctypes.c_uint32),
        ("ms_since_user_input", ctypes.c_uint32),
        ("event_mask", ctypes.c_uint32),
        ("kind", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 7),
    ]


SelectInputRequestPacket = DataPacket((
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('event_mask', FixedDataPacketField(MARKER_UINT32)),
))


class SelectInputRequest:
    OPCODE = 2

    __slots__ = ('drawable', 'event_mask',)

    def __init__(
            self, *,
            drawable: Optional[int] = None,
            event_mask: Optional[int] = None,
    ) -> None:
        self.drawable = drawable
        self.event_mask = event_mask

    def as_dict(self) -> Dict[str, Any]:
        return {
            'drawable': self.drawable,
            'event_mask': self.event_mask,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SelectInputRequest':
        return SelectInputRequest(**SelectInputRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SelectInputRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SelectInputRequest.lib = library.screensaver_selectinput
        SelectInputRequest.lib.restype = ctypes.c_uint32
        SelectInputRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class SelectInputRequestCType(ctypes.Structure):
    """screensaver SelectInput"""
    _fields_ = [
        ("drawable", ctypes.c_uint32),
        ("event_mask", ctypes.c_uint32),
    ]


SetAttributesRequestPacket = DataPacket((
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('x', FixedDataPacketField(MARKER_INT16)),
    ('y', FixedDataPacketField(MARKER_INT16)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('border_width', FixedDataPacketField(MARKER_UINT16)),
    ('class', FixedDataPacketField(MARKER_INT8)),
    ('depth', FixedDataPacketField(MARKER_UINT8)),
    ('visual', FixedDataPacketField(MARKER_UINT32)),
    ('value_mask', FixedDataPacketField(MARKER_UINT32)),
    ('value_list', BitDataPacketField(lambda d, c: d['value_mask'], {
        CwValues.BACK_PIXMAP: FixedDataPacketField(MARKER_UINT32),
        CwValues.BACK_PIXEL: FixedDataPacketField(MARKER_UINT32),
        CwValues.BORDER_PIXMAP: FixedDataPacketField(MARKER_UINT32),
        CwValues.BORDER_PIXEL: FixedDataPacketField(MARKER_UINT32),
        CwValues.BIT_GRAVITY: FixedDataPacketField(MARKER_UINT32),
        CwValues.WIN_GRAVITY: FixedDataPacketField(MARKER_UINT32),
        CwValues.BACKING_STORE: FixedDataPacketField(MARKER_UINT32),
        CwValues.BACKING_PLANES: FixedDataPacketField(MARKER_UINT32),
        CwValues.BACKING_PIXEL: FixedDataPacketField(MARKER_UINT32),
        CwValues.OVERRIDE_REDIRECT: FixedDataPacketField(MARKER_UINT32),
        CwValues.SAVE_UNDER: FixedDataPacketField(MARKER_UINT32),
        CwValues.EVENT_MASK: FixedDataPacketField(MARKER_UINT32),
        CwValues.DONT_PROPAGATE: FixedDataPacketField(MARKER_UINT32),
        CwValues.COLORMAP: FixedDataPacketField(MARKER_UINT32),
        CwValues.CURSOR: FixedDataPacketField(MARKER_UINT32),
    }, 0)),
))


class SetAttributesRequest:
    OPCODE = 3

    __slots__ = ('drawable', 'x', 'y', 'width', 'height', 'border_width', 'v_class', 'depth', 'visual', 'value_mask', 'value_list',)

    def __init__(
            self, *,
            drawable: Optional[int] = None,
            x: Optional[int] = None,
            y: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            border_width: Optional[int] = None,
            v_class: Optional[int] = None,
            depth: Optional[int] = None,
            visual: Optional[int] = None,
            value_mask: Optional[int] = None,
            value_list: Optional[Mapping[str, CwValues]] = None,
    ) -> None:
        self.drawable = drawable
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border_width = border_width
        self.v_class = v_class
        self.depth = depth
        self.visual = visual
        self.value_mask = value_mask
        self.value_list = value_list

    def as_dict(self) -> Dict[str, Any]:
        return {
            'drawable': self.drawable,
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height,
            'border_width': self.border_width,
            'class': self.v_class,
            'depth': self.depth,
            'visual': self.visual,
            'value_mask': self.value_mask,
            'value_list': self.value_list,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetAttributesRequest':
        return SetAttributesRequest(**SetAttributesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetAttributesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, int, int, int, Mapping[str, CwValues]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetAttributesRequest.lib = library.screensaver_setattributes
        SetAttributesRequest.lib.restype = ctypes.c_uint32
        SetAttributesRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_int8, ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)


class SetAttributesRequestCType(ctypes.Structure):
    """screensaver SetAttributes"""
    _fields_ = [
        ("drawable", ctypes.c_uint32),
        ("x", ctypes.c_int16),
        ("y", ctypes.c_int16),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("border_width", ctypes.c_uint16),
        ("class", ctypes.c_int8),
        ("depth", ctypes.c_uint8),
        ("visual", ctypes.c_uint32),
        ("value_mask", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


UnsetAttributesRequestPacket = DataPacket((
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
))


class UnsetAttributesRequest:
    OPCODE = 4

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
    def from_data(inp: BinaryIO) -> 'UnsetAttributesRequest':
        return UnsetAttributesRequest(**UnsetAttributesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return UnsetAttributesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        UnsetAttributesRequest.lib = library.screensaver_unsetattributes
        UnsetAttributesRequest.lib.restype = ctypes.c_uint32
        UnsetAttributesRequest.lib.argstype = (ctypes.c_uint32,)


class UnsetAttributesRequestCType(ctypes.Structure):
    """screensaver UnsetAttributes"""
    _fields_ = [
        ("drawable", ctypes.c_uint32),
    ]


SuspendRequestPacket = DataPacket((
    ('suspend', FixedDataPacketField(MARKER_UINT32)),
))


class SuspendRequest:
    OPCODE = 5

    __slots__ = ('suspend',)

    def __init__(
            self, *,
            suspend: Optional[int] = None,
    ) -> None:
        self.suspend = suspend

    def as_dict(self) -> Dict[str, Any]:
        return {
            'suspend': self.suspend,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SuspendRequest':
        return SuspendRequest(**SuspendRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SuspendRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SuspendRequest.lib = library.screensaver_suspend
        SuspendRequest.lib.restype = ctypes.c_uint32
        SuspendRequest.lib.argstype = (ctypes.c_uint32,)


class SuspendRequestCType(ctypes.Structure):
    """screensaver Suspend"""
    _fields_ = [
        ("suspend", ctypes.c_uint32),
    ]


NotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('state', FixedDataPacketField(MARKER_INT8)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('root', FixedDataPacketField(MARKER_UINT32)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('kind', FixedDataPacketField(MARKER_INT8)),
    ('forced', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(14)),
))


class NotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'state', 'time', 'root', 'window', 'kind', 'forced',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            state: Optional[int] = None,
            time: Optional[int] = None,
            root: Optional[int] = None,
            window: Optional[int] = None,
            kind: Optional[int] = None,
            forced: Optional[bool] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.state = state
        self.time = time
        self.root = root
        self.window = window
        self.kind = kind
        self.forced = forced

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'state': self.state,
            'time': self.time,
            'root': self.root,
            'window': self.window,
            'kind': self.kind,
            'forced': self.forced,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'NotifyEvent':
        return NotifyEvent(**NotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return NotifyEventPacket.pack(**self.as_dict())


class NotifyEventCType(ctypes.Structure):
    """screensaver Notify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("state", ctypes.c_int8),
        ("time", ctypes.c_uint32),
        ("root", ctypes.c_uint32),
        ("window", ctypes.c_uint32),
        ("kind", ctypes.c_int8),
        ("forced", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 14),
    ]


# ------------------------------------------------------------------
# Unions

