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

HtypeType = NewType('HtypeType', int)


class HtypeValues:
    FROM_SERVER_TIME = HtypeType(1)
    FROM_CLIENT_TIME = HtypeType(2)
    FROM_CLIENT_SEQUENCE = HtypeType(4)


CsType = NewType('CsType', int)


class CsValues:
    CURRENT_CLIENTS = CsType(1)
    FUTURE_CLIENTS = CsType(2)
    ALL_CLIENTS = CsType(3)


# ------------------------------------------------------------------
# Aliases

Context = NewType('Context', ctypes.c_uint32)


# ------------------------------------------------------------------
# Structures, Events, Requests, Replies


Range8StructPacket = DataPacket((
    ('first', FixedDataPacketField(MARKER_UINT8)),
    ('last', FixedDataPacketField(MARKER_UINT8)),
))


class Range8Struct:
    __slots__ = ('first', 'last',)

    def __init__(
            self, *,
            first: Optional[int] = None,
            last: Optional[int] = None,
    ) -> None:
        self.first = first
        self.last = last

    def as_dict(self) -> Dict[str, Any]:
        return {
            'first': self.first,
            'last': self.last,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'Range8Struct':
        return Range8Struct(**Range8StructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return Range8StructPacket.pack(**self.as_dict())


class Range8StructCType(ctypes.Structure):
    """record Range8"""
    _fields_ = [
        ("first", ctypes.c_uint8),
        ("last", ctypes.c_uint8),
    ]


Range16StructPacket = DataPacket((
    ('first', FixedDataPacketField(MARKER_UINT16)),
    ('last', FixedDataPacketField(MARKER_UINT16)),
))


class Range16Struct:
    __slots__ = ('first', 'last',)

    def __init__(
            self, *,
            first: Optional[int] = None,
            last: Optional[int] = None,
    ) -> None:
        self.first = first
        self.last = last

    def as_dict(self) -> Dict[str, Any]:
        return {
            'first': self.first,
            'last': self.last,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'Range16Struct':
        return Range16Struct(**Range16StructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return Range16StructPacket.pack(**self.as_dict())


class Range16StructCType(ctypes.Structure):
    """record Range16"""
    _fields_ = [
        ("first", ctypes.c_uint16),
        ("last", ctypes.c_uint16),
    ]


ExtRangeStructPacket = DataPacket((
    ('major', FixedDataPacketField(MARKER_UINT32)),
    ('minor', FixedDataPacketField(MARKER_UINT32)),
))


class ExtRangeStruct:
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
    def from_data(inp: BinaryIO) -> 'ExtRangeStruct':
        return ExtRangeStruct(**ExtRangeStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ExtRangeStructPacket.pack(**self.as_dict())


class ExtRangeStructCType(ctypes.Structure):
    """record ExtRange"""
    _fields_ = [
        ("major", ctypes.c_uint32),
        ("minor", ctypes.c_uint32),
    ]


RangeStructPacket = DataPacket((
    ('core_requests', FixedDataPacketField(MARKER_UINT32)),
    ('core_replies', FixedDataPacketField(MARKER_UINT32)),
    ('ext_requests', FixedDataPacketField(MARKER_UINT32)),
    ('ext_replies', FixedDataPacketField(MARKER_UINT32)),
    ('delivered_events', FixedDataPacketField(MARKER_UINT32)),
    ('device_events', FixedDataPacketField(MARKER_UINT32)),
    ('errors', FixedDataPacketField(MARKER_UINT32)),
    ('client_started', FixedDataPacketField(MARKER_UINT8)),
    ('client_died', FixedDataPacketField(MARKER_UINT8)),
))


class RangeStruct:
    __slots__ = ('core_requests', 'core_replies', 'ext_requests', 'ext_replies', 'delivered_events', 'device_events', 'errors', 'client_started', 'client_died',)

    def __init__(
            self, *,
            core_requests: Optional[int] = None,
            core_replies: Optional[int] = None,
            ext_requests: Optional[int] = None,
            ext_replies: Optional[int] = None,
            delivered_events: Optional[int] = None,
            device_events: Optional[int] = None,
            errors: Optional[int] = None,
            client_started: Optional[bool] = None,
            client_died: Optional[bool] = None,
    ) -> None:
        self.core_requests = core_requests
        self.core_replies = core_replies
        self.ext_requests = ext_requests
        self.ext_replies = ext_replies
        self.delivered_events = delivered_events
        self.device_events = device_events
        self.errors = errors
        self.client_started = client_started
        self.client_died = client_died

    def as_dict(self) -> Dict[str, Any]:
        return {
            'core_requests': self.core_requests,
            'core_replies': self.core_replies,
            'ext_requests': self.ext_requests,
            'ext_replies': self.ext_replies,
            'delivered_events': self.delivered_events,
            'device_events': self.device_events,
            'errors': self.errors,
            'client_started': self.client_started,
            'client_died': self.client_died,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'RangeStruct':
        return RangeStruct(**RangeStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return RangeStructPacket.pack(**self.as_dict())


class RangeStructCType(ctypes.Structure):
    """record Range"""
    _fields_ = [
        ("core_requests", ctypes.c_uint32),
        ("core_replies", ctypes.c_uint32),
        ("ext_requests", ctypes.c_uint32),
        ("ext_replies", ctypes.c_uint32),
        ("delivered_events", ctypes.c_uint32),
        ("device_events", ctypes.c_uint32),
        ("errors", ctypes.c_uint32),
        ("client_started", ctypes.c_int8),
        ("client_died", ctypes.c_int8),
    ]


ClientInfoStructPacket = DataPacket((
    ('client_resource', FixedDataPacketField(MARKER_UINT32)),
    ('num_ranges', FixedDataPacketField(MARKER_UINT32)),
    ('ranges', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_ranges'], 0)),
))


class ClientInfoStruct:
    __slots__ = ('client_resource', 'num_ranges', 'ranges',)

    def __init__(
            self, *,
            client_resource: Optional[int] = None,
            num_ranges: Optional[int] = None,
            ranges: Optional[Sequence[int]] = None,
    ) -> None:
        self.client_resource = client_resource
        self.num_ranges = num_ranges
        self.ranges = ranges

    def as_dict(self) -> Dict[str, Any]:
        return {
            'client_resource': self.client_resource,
            'num_ranges': self.num_ranges,
            'ranges': self.ranges,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ClientInfoStruct':
        return ClientInfoStruct(**ClientInfoStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ClientInfoStructPacket.pack(**self.as_dict())


class ClientInfoStructCType(ctypes.Structure):
    """record ClientInfo"""
    _fields_ = [
        ("client_resource", ctypes.c_uint32),
        ("num_ranges", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


QueryVersionRequestCookie = NewType('QueryVersionRequestCookie', ctypes.c_uint32)


QueryVersionRequestPacket = DataPacket((
    ('major_version', FixedDataPacketField(MARKER_UINT16)),
    ('minor_version', FixedDataPacketField(MARKER_UINT16)),
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
        QueryVersionRequest.lib = library.record_queryversion
        QueryVersionRequest.lib.restype = QueryVersionRequestCookie
        QueryVersionRequest.lib.argstype = (ctypes.c_uint16, ctypes.c_uint16)


class QueryVersionRequestCType(ctypes.Structure):
    """record QueryVersion"""
    _fields_ = [
        ("major_version", ctypes.c_uint16),
        ("minor_version", ctypes.c_uint16),
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
    """record QueryVersion_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("major_version", ctypes.c_uint16),
        ("minor_version", ctypes.c_uint16),
    ]


CreateContextRequestPacket = DataPacket((
    ('context', FixedDataPacketField(MARKER_UINT32)),
    ('element_header', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(3)),
    ('num_client_specs', FixedDataPacketField(MARKER_UINT32)),
    ('num_ranges', FixedDataPacketField(MARKER_UINT32)),
    ('client_specs', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_client_specs'], 0)),
    ('ranges', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_ranges'], 0)),
))


class CreateContextRequest:
    OPCODE = 1

    __slots__ = ('context', 'element_header', 'num_client_specs', 'num_ranges', 'client_specs', 'ranges',)

    def __init__(
            self, *,
            context: Optional[int] = None,
            element_header: Optional[int] = None,
            num_client_specs: Optional[int] = None,
            num_ranges: Optional[int] = None,
            client_specs: Optional[Sequence[int]] = None,
            ranges: Optional[Sequence[int]] = None,
    ) -> None:
        self.context = context
        self.element_header = element_header
        self.num_client_specs = num_client_specs
        self.num_ranges = num_ranges
        self.client_specs = client_specs
        self.ranges = ranges

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context': self.context,
            'element_header': self.element_header,
            'num_client_specs': self.num_client_specs,
            'num_ranges': self.num_ranges,
            'client_specs': self.client_specs,
            'ranges': self.ranges,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateContextRequest':
        return CreateContextRequest(**CreateContextRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateContextRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, Sequence[int], Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateContextRequest.lib = library.record_createcontext
        CreateContextRequest.lib.restype = ctypes.c_uint32
        CreateContextRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8 * 3, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_void_p)


class CreateContextRequestCType(ctypes.Structure):
    """record CreateContext"""
    _fields_ = [
        ("context", ctypes.c_uint32),
        ("element_header", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 3),
        ("num_client_specs", ctypes.c_uint32),
        ("num_ranges", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


RegisterClientsRequestPacket = DataPacket((
    ('context', FixedDataPacketField(MARKER_UINT32)),
    ('element_header', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(3)),
    ('num_client_specs', FixedDataPacketField(MARKER_UINT32)),
    ('num_ranges', FixedDataPacketField(MARKER_UINT32)),
    ('client_specs', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_client_specs'], 0)),
    ('ranges', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_ranges'], 0)),
))


class RegisterClientsRequest:
    OPCODE = 2

    __slots__ = ('context', 'element_header', 'num_client_specs', 'num_ranges', 'client_specs', 'ranges',)

    def __init__(
            self, *,
            context: Optional[int] = None,
            element_header: Optional[int] = None,
            num_client_specs: Optional[int] = None,
            num_ranges: Optional[int] = None,
            client_specs: Optional[Sequence[int]] = None,
            ranges: Optional[Sequence[int]] = None,
    ) -> None:
        self.context = context
        self.element_header = element_header
        self.num_client_specs = num_client_specs
        self.num_ranges = num_ranges
        self.client_specs = client_specs
        self.ranges = ranges

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context': self.context,
            'element_header': self.element_header,
            'num_client_specs': self.num_client_specs,
            'num_ranges': self.num_ranges,
            'client_specs': self.client_specs,
            'ranges': self.ranges,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'RegisterClientsRequest':
        return RegisterClientsRequest(**RegisterClientsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return RegisterClientsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, Sequence[int], Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        RegisterClientsRequest.lib = library.record_registerclients
        RegisterClientsRequest.lib.restype = ctypes.c_uint32
        RegisterClientsRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8 * 3, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_void_p)


class RegisterClientsRequestCType(ctypes.Structure):
    """record RegisterClients"""
    _fields_ = [
        ("context", ctypes.c_uint32),
        ("element_header", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 3),
        ("num_client_specs", ctypes.c_uint32),
        ("num_ranges", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


UnregisterClientsRequestPacket = DataPacket((
    ('context', FixedDataPacketField(MARKER_UINT32)),
    ('num_client_specs', FixedDataPacketField(MARKER_UINT32)),
    ('client_specs', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_client_specs'], 0)),
))


class UnregisterClientsRequest:
    OPCODE = 3

    __slots__ = ('context', 'num_client_specs', 'client_specs',)

    def __init__(
            self, *,
            context: Optional[int] = None,
            num_client_specs: Optional[int] = None,
            client_specs: Optional[Sequence[int]] = None,
    ) -> None:
        self.context = context
        self.num_client_specs = num_client_specs
        self.client_specs = client_specs

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context': self.context,
            'num_client_specs': self.num_client_specs,
            'client_specs': self.client_specs,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'UnregisterClientsRequest':
        return UnregisterClientsRequest(**UnregisterClientsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return UnregisterClientsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        UnregisterClientsRequest.lib = library.record_unregisterclients
        UnregisterClientsRequest.lib.restype = ctypes.c_uint32
        UnregisterClientsRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)


class UnregisterClientsRequestCType(ctypes.Structure):
    """record UnregisterClients"""
    _fields_ = [
        ("context", ctypes.c_uint32),
        ("num_client_specs", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


GetContextRequestCookie = NewType('GetContextRequestCookie', ctypes.c_uint32)


GetContextRequestPacket = DataPacket((
    ('context', FixedDataPacketField(MARKER_UINT32)),
))


class GetContextRequest:
    OPCODE = 4

    __slots__ = ('context',)

    def __init__(
            self, *,
            context: Optional[int] = None,
    ) -> None:
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetContextRequest':
        return GetContextRequest(**GetContextRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetContextRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetContextRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetContextRequest.lib = library.record_getcontext
        GetContextRequest.lib.restype = GetContextRequestCookie
        GetContextRequest.lib.argstype = (ctypes.c_uint32,)


class GetContextRequestCType(ctypes.Structure):
    """record GetContext"""
    _fields_ = [
        ("context", ctypes.c_uint32),
    ]


GetContextReplyReplyPacket = DataPacket((
    ('enabled', FixedDataPacketField(MARKER_UINT8)),
    ('element_header', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(3)),
    ('num_intercepted_clients', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(16)),
    ('intercepted_clients', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_intercepted_clients'], 0)),
))


class GetContextReplyReply:
    __slots__ = ('enabled', 'element_header', 'num_intercepted_clients', 'intercepted_clients',)

    def __init__(
            self, *,
            enabled: Optional[bool] = None,
            element_header: Optional[int] = None,
            num_intercepted_clients: Optional[int] = None,
            intercepted_clients: Optional[Sequence[int]] = None,
    ) -> None:
        self.enabled = enabled
        self.element_header = element_header
        self.num_intercepted_clients = num_intercepted_clients
        self.intercepted_clients = intercepted_clients

    def as_dict(self) -> Dict[str, Any]:
        return {
            'enabled': self.enabled,
            'element_header': self.element_header,
            'num_intercepted_clients': self.num_intercepted_clients,
            'intercepted_clients': self.intercepted_clients,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetContextReplyReply':
        return GetContextReplyReply(**GetContextReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetContextReplyReplyPacket.pack(**self.as_dict())


class GetContextReplyReplyCType(ctypes.Structure):
    """record GetContext_reply"""
    _fields_ = [
        ("enabled", ctypes.c_int8),
        ("element_header", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 3),
        ("num_intercepted_clients", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 16),
        ("var_data", ctypes.c_void_p),
    ]


EnableContextRequestCookie = NewType('EnableContextRequestCookie', ctypes.c_uint32)


EnableContextRequestPacket = DataPacket((
    ('context', FixedDataPacketField(MARKER_UINT32)),
))


class EnableContextRequest:
    OPCODE = 5

    __slots__ = ('context',)

    def __init__(
            self, *,
            context: Optional[int] = None,
    ) -> None:
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'EnableContextRequest':
        return EnableContextRequest(**EnableContextRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return EnableContextRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], EnableContextRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        EnableContextRequest.lib = library.record_enablecontext
        EnableContextRequest.lib.restype = EnableContextRequestCookie
        EnableContextRequest.lib.argstype = (ctypes.c_uint32,)


class EnableContextRequestCType(ctypes.Structure):
    """record EnableContext"""
    _fields_ = [
        ("context", ctypes.c_uint32),
    ]


EnableContextReplyReplyPacket = DataPacket((
    ('category', FixedDataPacketField(MARKER_UINT8)),
    ('element_header', FixedDataPacketField(MARKER_UINT32)),
    ('client_swapped', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
    ('xid_base', FixedDataPacketField(MARKER_UINT32)),
    ('server_time', FixedDataPacketField(MARKER_UINT32)),
    ('rec_sequence_num', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(8)),
    ('data', SimpleListDataPacketField(MARKER_INT8, lambda d, c: (d['length']) * (4), 0)),
))


class EnableContextReplyReply:
    __slots__ = ('category', 'element_header', 'client_swapped', 'xid_base', 'server_time', 'rec_sequence_num', 'data',)

    def __init__(
            self, *,
            category: Optional[int] = None,
            element_header: Optional[int] = None,
            client_swapped: Optional[bool] = None,
            xid_base: Optional[int] = None,
            server_time: Optional[int] = None,
            rec_sequence_num: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.category = category
        self.element_header = element_header
        self.client_swapped = client_swapped
        self.xid_base = xid_base
        self.server_time = server_time
        self.rec_sequence_num = rec_sequence_num
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'category': self.category,
            'element_header': self.element_header,
            'client_swapped': self.client_swapped,
            'xid_base': self.xid_base,
            'server_time': self.server_time,
            'rec_sequence_num': self.rec_sequence_num,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'EnableContextReplyReply':
        return EnableContextReplyReply(**EnableContextReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return EnableContextReplyReplyPacket.pack(**self.as_dict())


class EnableContextReplyReplyCType(ctypes.Structure):
    """record EnableContext_reply"""
    _fields_ = [
        ("category", ctypes.c_uint8),
        ("element_header", ctypes.c_uint32),
        ("client_swapped", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 2),
        ("xid_base", ctypes.c_uint32),
        ("server_time", ctypes.c_uint32),
        ("rec_sequence_num", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 8),
        ("var_data", ctypes.c_void_p),
    ]


DisableContextRequestPacket = DataPacket((
    ('context', FixedDataPacketField(MARKER_UINT32)),
))


class DisableContextRequest:
    OPCODE = 6

    __slots__ = ('context',)

    def __init__(
            self, *,
            context: Optional[int] = None,
    ) -> None:
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DisableContextRequest':
        return DisableContextRequest(**DisableContextRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DisableContextRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        DisableContextRequest.lib = library.record_disablecontext
        DisableContextRequest.lib.restype = ctypes.c_uint32
        DisableContextRequest.lib.argstype = (ctypes.c_uint32,)


class DisableContextRequestCType(ctypes.Structure):
    """record DisableContext"""
    _fields_ = [
        ("context", ctypes.c_uint32),
    ]


FreeContextRequestPacket = DataPacket((
    ('context', FixedDataPacketField(MARKER_UINT32)),
))


class FreeContextRequest:
    OPCODE = 7

    __slots__ = ('context',)

    def __init__(
            self, *,
            context: Optional[int] = None,
    ) -> None:
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'FreeContextRequest':
        return FreeContextRequest(**FreeContextRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return FreeContextRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        FreeContextRequest.lib = library.record_freecontext
        FreeContextRequest.lib.restype = ctypes.c_uint32
        FreeContextRequest.lib.argstype = (ctypes.c_uint32,)


class FreeContextRequestCType(ctypes.Structure):
    """record FreeContext"""
    _fields_ = [
        ("context", ctypes.c_uint32),
    ]


# ------------------------------------------------------------------
# Unions

