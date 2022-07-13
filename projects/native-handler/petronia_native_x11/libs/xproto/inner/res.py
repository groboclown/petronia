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

ClientIdMaskType = NewType('ClientIdMaskType', int)


class ClientIdMaskValues:
    CLIENT_XID = ClientIdMaskType(1)
    LOCAL_CLIENT_PID = ClientIdMaskType(2)


# ------------------------------------------------------------------
# Aliases



# ------------------------------------------------------------------
# Structures, Events, Requests, Replies


ClientStructPacket = DataPacket((
    ('resource_base', FixedDataPacketField(MARKER_UINT32)),
    ('resource_mask', FixedDataPacketField(MARKER_UINT32)),
))


class ClientStruct:
    __slots__ = ('resource_base', 'resource_mask',)

    def __init__(
            self, *,
            resource_base: Optional[int] = None,
            resource_mask: Optional[int] = None,
    ) -> None:
        self.resource_base = resource_base
        self.resource_mask = resource_mask

    def as_dict(self) -> Dict[str, Any]:
        return {
            'resource_base': self.resource_base,
            'resource_mask': self.resource_mask,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ClientStruct':
        return ClientStruct(**ClientStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ClientStructPacket.pack(**self.as_dict())


class ClientStructCType(ctypes.Structure):
    """res Client"""
    _fields_ = [
        ("resource_base", ctypes.c_uint32),
        ("resource_mask", ctypes.c_uint32),
    ]


TypeStructPacket = DataPacket((
    ('resource_type', FixedDataPacketField(MARKER_UINT32)),
    ('count', FixedDataPacketField(MARKER_UINT32)),
))


class TypeStruct:
    __slots__ = ('resource_type', 'count',)

    def __init__(
            self, *,
            resource_type: Optional[int] = None,
            count: Optional[int] = None,
    ) -> None:
        self.resource_type = resource_type
        self.count = count

    def as_dict(self) -> Dict[str, Any]:
        return {
            'resource_type': self.resource_type,
            'count': self.count,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'TypeStruct':
        return TypeStruct(**TypeStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return TypeStructPacket.pack(**self.as_dict())


class TypeStructCType(ctypes.Structure):
    """res Type"""
    _fields_ = [
        ("resource_type", ctypes.c_uint32),
        ("count", ctypes.c_uint32),
    ]


ClientIdSpecStructPacket = DataPacket((
    ('client', FixedDataPacketField(MARKER_UINT32)),
    ('mask', FixedDataPacketField(MARKER_UINT32)),
))


class ClientIdSpecStruct:
    __slots__ = ('client', 'mask',)

    def __init__(
            self, *,
            client: Optional[int] = None,
            mask: Optional[int] = None,
    ) -> None:
        self.client = client
        self.mask = mask

    def as_dict(self) -> Dict[str, Any]:
        return {
            'client': self.client,
            'mask': self.mask,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ClientIdSpecStruct':
        return ClientIdSpecStruct(**ClientIdSpecStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ClientIdSpecStructPacket.pack(**self.as_dict())


class ClientIdSpecStructCType(ctypes.Structure):
    """res ClientIdSpec"""
    _fields_ = [
        ("client", ctypes.c_uint32),
        ("mask", ctypes.c_uint32),
    ]


ClientIdValueStructPacket = DataPacket((
    ('spec', FixedDataPacketField(MARKER_UINT32)),
    ('length', FixedDataPacketField(MARKER_UINT32)),
    ('value', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: (d['length']) / (4), 0)),
))


class ClientIdValueStruct:
    __slots__ = ('spec', 'length', 'value',)

    def __init__(
            self, *,
            spec: Optional[int] = None,
            length: Optional[int] = None,
            value: Optional[Sequence[int]] = None,
    ) -> None:
        self.spec = spec
        self.length = length
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {
            'spec': self.spec,
            'length': self.length,
            'value': self.value,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ClientIdValueStruct':
        return ClientIdValueStruct(**ClientIdValueStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ClientIdValueStructPacket.pack(**self.as_dict())


class ClientIdValueStructCType(ctypes.Structure):
    """res ClientIdValue"""
    _fields_ = [
        ("spec", ctypes.c_uint32),
        ("length", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


ResourceIdSpecStructPacket = DataPacket((
    ('resource', FixedDataPacketField(MARKER_UINT32)),
    ('type', FixedDataPacketField(MARKER_UINT32)),
))


class ResourceIdSpecStruct:
    __slots__ = ('resource', 'type',)

    def __init__(
            self, *,
            resource: Optional[int] = None,
            type: Optional[int] = None,
    ) -> None:
        self.resource = resource
        self.type = type

    def as_dict(self) -> Dict[str, Any]:
        return {
            'resource': self.resource,
            'type': self.type,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ResourceIdSpecStruct':
        return ResourceIdSpecStruct(**ResourceIdSpecStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ResourceIdSpecStructPacket.pack(**self.as_dict())


class ResourceIdSpecStructCType(ctypes.Structure):
    """res ResourceIdSpec"""
    _fields_ = [
        ("resource", ctypes.c_uint32),
        ("type", ctypes.c_uint32),
    ]


ResourceSizeSpecStructPacket = DataPacket((
    ('spec', FixedDataPacketField(MARKER_UINT32)),
    ('bytes', FixedDataPacketField(MARKER_UINT32)),
    ('ref_count', FixedDataPacketField(MARKER_UINT32)),
    ('use_count', FixedDataPacketField(MARKER_UINT32)),
))


class ResourceSizeSpecStruct:
    __slots__ = ('spec', 'bytes', 'ref_count', 'use_count',)

    def __init__(
            self, *,
            spec: Optional[int] = None,
            bytes: Optional[int] = None,
            ref_count: Optional[int] = None,
            use_count: Optional[int] = None,
    ) -> None:
        self.spec = spec
        self.bytes = bytes
        self.ref_count = ref_count
        self.use_count = use_count

    def as_dict(self) -> Dict[str, Any]:
        return {
            'spec': self.spec,
            'bytes': self.bytes,
            'ref_count': self.ref_count,
            'use_count': self.use_count,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ResourceSizeSpecStruct':
        return ResourceSizeSpecStruct(**ResourceSizeSpecStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ResourceSizeSpecStructPacket.pack(**self.as_dict())


class ResourceSizeSpecStructCType(ctypes.Structure):
    """res ResourceSizeSpec"""
    _fields_ = [
        ("spec", ctypes.c_uint32),
        ("bytes", ctypes.c_uint32),
        ("ref_count", ctypes.c_uint32),
        ("use_count", ctypes.c_uint32),
    ]


ResourceSizeValueStructPacket = DataPacket((
    ('size', FixedDataPacketField(MARKER_UINT32)),
    ('num_cross_references', FixedDataPacketField(MARKER_UINT32)),
    ('cross_references', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_cross_references'], 0)),
))


class ResourceSizeValueStruct:
    __slots__ = ('size', 'num_cross_references', 'cross_references',)

    def __init__(
            self, *,
            size: Optional[int] = None,
            num_cross_references: Optional[int] = None,
            cross_references: Optional[Sequence[int]] = None,
    ) -> None:
        self.size = size
        self.num_cross_references = num_cross_references
        self.cross_references = cross_references

    def as_dict(self) -> Dict[str, Any]:
        return {
            'size': self.size,
            'num_cross_references': self.num_cross_references,
            'cross_references': self.cross_references,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ResourceSizeValueStruct':
        return ResourceSizeValueStruct(**ResourceSizeValueStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ResourceSizeValueStructPacket.pack(**self.as_dict())


class ResourceSizeValueStructCType(ctypes.Structure):
    """res ResourceSizeValue"""
    _fields_ = [
        ("size", ctypes.c_uint32),
        ("num_cross_references", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


QueryVersionRequestCookie = NewType('QueryVersionRequestCookie', ctypes.c_uint32)


QueryVersionRequestPacket = DataPacket((
    ('client_major', FixedDataPacketField(MARKER_UINT8)),
    ('client_minor', FixedDataPacketField(MARKER_UINT8)),
))


class QueryVersionRequest:
    OPCODE = 0

    __slots__ = ('client_major', 'client_minor',)

    def __init__(
            self, *,
            client_major: Optional[int] = None,
            client_minor: Optional[int] = None,
    ) -> None:
        self.client_major = client_major
        self.client_minor = client_minor

    def as_dict(self) -> Dict[str, Any]:
        return {
            'client_major': self.client_major,
            'client_minor': self.client_minor,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryVersionRequest':
        return QueryVersionRequest(**QueryVersionRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryVersionRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], QueryVersionRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryVersionRequest.lib = library.res_queryversion
        QueryVersionRequest.lib.restype = QueryVersionRequestCookie
        QueryVersionRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint8)


class QueryVersionRequestCType(ctypes.Structure):
    """res QueryVersion"""
    _fields_ = [
        ("client_major", ctypes.c_uint8),
        ("client_minor", ctypes.c_uint8),
    ]


QueryVersionReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('server_major', FixedDataPacketField(MARKER_UINT16)),
    ('server_minor', FixedDataPacketField(MARKER_UINT16)),
))


class QueryVersionReplyReply:
    __slots__ = ('server_major', 'server_minor',)

    def __init__(
            self, *,
            server_major: Optional[int] = None,
            server_minor: Optional[int] = None,
    ) -> None:
        self.server_major = server_major
        self.server_minor = server_minor

    def as_dict(self) -> Dict[str, Any]:
        return {
            'server_major': self.server_major,
            'server_minor': self.server_minor,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryVersionReplyReply':
        return QueryVersionReplyReply(**QueryVersionReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryVersionReplyReplyPacket.pack(**self.as_dict())


class QueryVersionReplyReplyCType(ctypes.Structure):
    """res QueryVersion_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("server_major", ctypes.c_uint16),
        ("server_minor", ctypes.c_uint16),
    ]


QueryClientsRequestCookie = NewType('QueryClientsRequestCookie', ctypes.c_uint32)


QueryClientsRequestPacket = DataPacket((
))


class QueryClientsRequest:
    OPCODE = 1

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryClientsRequest':
        return QueryClientsRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], QueryClientsRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryClientsRequest.lib = library.res_queryclients
        QueryClientsRequest.lib.restype = QueryClientsRequestCookie
        QueryClientsRequest.lib.argstype = ()


class QueryClientsRequestCType(ctypes.Structure):
    """res QueryClients"""
    _fields_ = [
    ]


QueryClientsReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('num_clients', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('clients', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_clients'], 0)),
))


class QueryClientsReplyReply:
    __slots__ = ('num_clients', 'clients',)

    def __init__(
            self, *,
            num_clients: Optional[int] = None,
            clients: Optional[Sequence[int]] = None,
    ) -> None:
        self.num_clients = num_clients
        self.clients = clients

    def as_dict(self) -> Dict[str, Any]:
        return {
            'num_clients': self.num_clients,
            'clients': self.clients,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryClientsReplyReply':
        return QueryClientsReplyReply(**QueryClientsReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryClientsReplyReplyPacket.pack(**self.as_dict())


class QueryClientsReplyReplyCType(ctypes.Structure):
    """res QueryClients_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("num_clients", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


QueryClientResourcesRequestCookie = NewType('QueryClientResourcesRequestCookie', ctypes.c_uint32)


QueryClientResourcesRequestPacket = DataPacket((
    ('xid', FixedDataPacketField(MARKER_UINT32)),
))


class QueryClientResourcesRequest:
    OPCODE = 2

    __slots__ = ('xid',)

    def __init__(
            self, *,
            xid: Optional[int] = None,
    ) -> None:
        self.xid = xid

    def as_dict(self) -> Dict[str, Any]:
        return {
            'xid': self.xid,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryClientResourcesRequest':
        return QueryClientResourcesRequest(**QueryClientResourcesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryClientResourcesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], QueryClientResourcesRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryClientResourcesRequest.lib = library.res_queryclientresources
        QueryClientResourcesRequest.lib.restype = QueryClientResourcesRequestCookie
        QueryClientResourcesRequest.lib.argstype = (ctypes.c_uint32,)


class QueryClientResourcesRequestCType(ctypes.Structure):
    """res QueryClientResources"""
    _fields_ = [
        ("xid", ctypes.c_uint32),
    ]


QueryClientResourcesReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('num_types', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('types', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_types'], 0)),
))


class QueryClientResourcesReplyReply:
    __slots__ = ('num_types', 'types',)

    def __init__(
            self, *,
            num_types: Optional[int] = None,
            types: Optional[Sequence[int]] = None,
    ) -> None:
        self.num_types = num_types
        self.types = types

    def as_dict(self) -> Dict[str, Any]:
        return {
            'num_types': self.num_types,
            'types': self.types,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryClientResourcesReplyReply':
        return QueryClientResourcesReplyReply(**QueryClientResourcesReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryClientResourcesReplyReplyPacket.pack(**self.as_dict())


class QueryClientResourcesReplyReplyCType(ctypes.Structure):
    """res QueryClientResources_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("num_types", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


QueryClientPixmapBytesRequestCookie = NewType('QueryClientPixmapBytesRequestCookie', ctypes.c_uint32)


QueryClientPixmapBytesRequestPacket = DataPacket((
    ('xid', FixedDataPacketField(MARKER_UINT32)),
))


class QueryClientPixmapBytesRequest:
    OPCODE = 3

    __slots__ = ('xid',)

    def __init__(
            self, *,
            xid: Optional[int] = None,
    ) -> None:
        self.xid = xid

    def as_dict(self) -> Dict[str, Any]:
        return {
            'xid': self.xid,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryClientPixmapBytesRequest':
        return QueryClientPixmapBytesRequest(**QueryClientPixmapBytesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryClientPixmapBytesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], QueryClientPixmapBytesRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryClientPixmapBytesRequest.lib = library.res_queryclientpixmapbytes
        QueryClientPixmapBytesRequest.lib.restype = QueryClientPixmapBytesRequestCookie
        QueryClientPixmapBytesRequest.lib.argstype = (ctypes.c_uint32,)


class QueryClientPixmapBytesRequestCType(ctypes.Structure):
    """res QueryClientPixmapBytes"""
    _fields_ = [
        ("xid", ctypes.c_uint32),
    ]


QueryClientPixmapBytesReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('bytes', FixedDataPacketField(MARKER_UINT32)),
    ('bytes_overflow', FixedDataPacketField(MARKER_UINT32)),
))


class QueryClientPixmapBytesReplyReply:
    __slots__ = ('bytes', 'bytes_overflow',)

    def __init__(
            self, *,
            bytes: Optional[int] = None,
            bytes_overflow: Optional[int] = None,
    ) -> None:
        self.bytes = bytes
        self.bytes_overflow = bytes_overflow

    def as_dict(self) -> Dict[str, Any]:
        return {
            'bytes': self.bytes,
            'bytes_overflow': self.bytes_overflow,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryClientPixmapBytesReplyReply':
        return QueryClientPixmapBytesReplyReply(**QueryClientPixmapBytesReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryClientPixmapBytesReplyReplyPacket.pack(**self.as_dict())


class QueryClientPixmapBytesReplyReplyCType(ctypes.Structure):
    """res QueryClientPixmapBytes_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("bytes", ctypes.c_uint32),
        ("bytes_overflow", ctypes.c_uint32),
    ]


QueryClientIdsRequestCookie = NewType('QueryClientIdsRequestCookie', ctypes.c_uint32)


QueryClientIdsRequestPacket = DataPacket((
    ('num_specs', FixedDataPacketField(MARKER_UINT32)),
    ('specs', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_specs'], 0)),
))


class QueryClientIdsRequest:
    OPCODE = 4

    __slots__ = ('num_specs', 'specs',)

    def __init__(
            self, *,
            num_specs: Optional[int] = None,
            specs: Optional[Sequence[int]] = None,
    ) -> None:
        self.num_specs = num_specs
        self.specs = specs

    def as_dict(self) -> Dict[str, Any]:
        return {
            'num_specs': self.num_specs,
            'specs': self.specs,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryClientIdsRequest':
        return QueryClientIdsRequest(**QueryClientIdsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryClientIdsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, Sequence[int]], QueryClientIdsRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryClientIdsRequest.lib = library.res_queryclientids
        QueryClientIdsRequest.lib.restype = QueryClientIdsRequestCookie
        QueryClientIdsRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_void_p)


class QueryClientIdsRequestCType(ctypes.Structure):
    """res QueryClientIds"""
    _fields_ = [
        ("num_specs", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


QueryClientIdsReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('num_ids', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('ids', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_ids'], 0)),
))


class QueryClientIdsReplyReply:
    __slots__ = ('num_ids', 'ids',)

    def __init__(
            self, *,
            num_ids: Optional[int] = None,
            ids: Optional[Sequence[int]] = None,
    ) -> None:
        self.num_ids = num_ids
        self.ids = ids

    def as_dict(self) -> Dict[str, Any]:
        return {
            'num_ids': self.num_ids,
            'ids': self.ids,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryClientIdsReplyReply':
        return QueryClientIdsReplyReply(**QueryClientIdsReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryClientIdsReplyReplyPacket.pack(**self.as_dict())


class QueryClientIdsReplyReplyCType(ctypes.Structure):
    """res QueryClientIds_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("num_ids", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


QueryResourceBytesRequestCookie = NewType('QueryResourceBytesRequestCookie', ctypes.c_uint32)


QueryResourceBytesRequestPacket = DataPacket((
    ('client', FixedDataPacketField(MARKER_UINT32)),
    ('num_specs', FixedDataPacketField(MARKER_UINT32)),
    ('specs', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_specs'], 0)),
))


class QueryResourceBytesRequest:
    OPCODE = 5

    __slots__ = ('client', 'num_specs', 'specs',)

    def __init__(
            self, *,
            client: Optional[int] = None,
            num_specs: Optional[int] = None,
            specs: Optional[Sequence[int]] = None,
    ) -> None:
        self.client = client
        self.num_specs = num_specs
        self.specs = specs

    def as_dict(self) -> Dict[str, Any]:
        return {
            'client': self.client,
            'num_specs': self.num_specs,
            'specs': self.specs,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryResourceBytesRequest':
        return QueryResourceBytesRequest(**QueryResourceBytesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryResourceBytesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int]], QueryResourceBytesRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryResourceBytesRequest.lib = library.res_queryresourcebytes
        QueryResourceBytesRequest.lib.restype = QueryResourceBytesRequestCookie
        QueryResourceBytesRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)


class QueryResourceBytesRequestCType(ctypes.Structure):
    """res QueryResourceBytes"""
    _fields_ = [
        ("client", ctypes.c_uint32),
        ("num_specs", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


QueryResourceBytesReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('num_sizes', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('sizes', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_sizes'], 0)),
))


class QueryResourceBytesReplyReply:
    __slots__ = ('num_sizes', 'sizes',)

    def __init__(
            self, *,
            num_sizes: Optional[int] = None,
            sizes: Optional[Sequence[int]] = None,
    ) -> None:
        self.num_sizes = num_sizes
        self.sizes = sizes

    def as_dict(self) -> Dict[str, Any]:
        return {
            'num_sizes': self.num_sizes,
            'sizes': self.sizes,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryResourceBytesReplyReply':
        return QueryResourceBytesReplyReply(**QueryResourceBytesReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryResourceBytesReplyReplyPacket.pack(**self.as_dict())


class QueryResourceBytesReplyReplyCType(ctypes.Structure):
    """res QueryResourceBytes_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("num_sizes", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


# ------------------------------------------------------------------
# Unions

