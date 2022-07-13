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

# ------------------------------------------------------------------
# Aliases

Context = NewType('Context', ctypes.c_uint32)
Subpicture = NewType('Subpicture', ctypes.c_uint32)
Surface = NewType('Surface', ctypes.c_uint32)


# ------------------------------------------------------------------
# Structures, Events, Requests, Replies


SurfaceInfoStructPacket = DataPacket((
    ('id', FixedDataPacketField(MARKER_UINT32)),
    ('chroma_format', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedDataPacketField(MARKER_UINT16)),
    ('max_width', FixedDataPacketField(MARKER_UINT16)),
    ('max_height', FixedDataPacketField(MARKER_UINT16)),
    ('subpicture_max_width', FixedDataPacketField(MARKER_UINT16)),
    ('subpicture_max_height', FixedDataPacketField(MARKER_UINT16)),
    ('mc_type', FixedDataPacketField(MARKER_UINT32)),
    ('flags', FixedDataPacketField(MARKER_UINT32)),
))


class SurfaceInfoStruct:
    __slots__ = ('id', 'chroma_format', 'pad0', 'max_width', 'max_height', 'subpicture_max_width', 'subpicture_max_height', 'mc_type', 'flags',)

    def __init__(
            self, *,
            id: Optional[int] = None,
            chroma_format: Optional[int] = None,
            pad0: Optional[int] = None,
            max_width: Optional[int] = None,
            max_height: Optional[int] = None,
            subpicture_max_width: Optional[int] = None,
            subpicture_max_height: Optional[int] = None,
            mc_type: Optional[int] = None,
            flags: Optional[int] = None,
    ) -> None:
        self.id = id
        self.chroma_format = chroma_format
        self.pad0 = pad0
        self.max_width = max_width
        self.max_height = max_height
        self.subpicture_max_width = subpicture_max_width
        self.subpicture_max_height = subpicture_max_height
        self.mc_type = mc_type
        self.flags = flags

    def as_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'chroma_format': self.chroma_format,
            'pad0': self.pad0,
            'max_width': self.max_width,
            'max_height': self.max_height,
            'subpicture_max_width': self.subpicture_max_width,
            'subpicture_max_height': self.subpicture_max_height,
            'mc_type': self.mc_type,
            'flags': self.flags,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SurfaceInfoStruct':
        return SurfaceInfoStruct(**SurfaceInfoStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SurfaceInfoStructPacket.pack(**self.as_dict())


class SurfaceInfoStructCType(ctypes.Structure):
    """xvmc SurfaceInfo"""
    _fields_ = [
        ("id", ctypes.c_uint32),
        ("chroma_format", ctypes.c_uint16),
        ("pad0", ctypes.c_uint16),
        ("max_width", ctypes.c_uint16),
        ("max_height", ctypes.c_uint16),
        ("subpicture_max_width", ctypes.c_uint16),
        ("subpicture_max_height", ctypes.c_uint16),
        ("mc_type", ctypes.c_uint32),
        ("flags", ctypes.c_uint32),
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
        QueryVersionRequest.lib = library.xvmc_queryversion
        QueryVersionRequest.lib.restype = QueryVersionRequestCookie
        QueryVersionRequest.lib.argstype = ()


class QueryVersionRequestCType(ctypes.Structure):
    """xvmc QueryVersion"""
    _fields_ = [
    ]


QueryVersionReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('major', FixedDataPacketField(MARKER_UINT32)),
    ('minor', FixedDataPacketField(MARKER_UINT32)),
))


class QueryVersionReplyReply:
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
    def from_data(inp: BinaryIO) -> 'QueryVersionReplyReply':
        return QueryVersionReplyReply(**QueryVersionReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryVersionReplyReplyPacket.pack(**self.as_dict())


class QueryVersionReplyReplyCType(ctypes.Structure):
    """xvmc QueryVersion_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("major", ctypes.c_uint32),
        ("minor", ctypes.c_uint32),
    ]


ListSurfaceTypesRequestCookie = NewType('ListSurfaceTypesRequestCookie', ctypes.c_uint32)


ListSurfaceTypesRequestPacket = DataPacket((
    ('port_id', FixedDataPacketField(MARKER_UINT32)),
))


class ListSurfaceTypesRequest:
    OPCODE = 1

    __slots__ = ('port_id',)

    def __init__(
            self, *,
            port_id: Optional[int] = None,
    ) -> None:
        self.port_id = port_id

    def as_dict(self) -> Dict[str, Any]:
        return {
            'port_id': self.port_id,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ListSurfaceTypesRequest':
        return ListSurfaceTypesRequest(**ListSurfaceTypesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ListSurfaceTypesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ListSurfaceTypesRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ListSurfaceTypesRequest.lib = library.xvmc_listsurfacetypes
        ListSurfaceTypesRequest.lib.restype = ListSurfaceTypesRequestCookie
        ListSurfaceTypesRequest.lib.argstype = (ctypes.c_uint32,)


class ListSurfaceTypesRequestCType(ctypes.Structure):
    """xvmc ListSurfaceTypes"""
    _fields_ = [
        ("port_id", ctypes.c_uint32),
    ]


ListSurfaceTypesReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('num', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('surfaces', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num'], 0)),
))


class ListSurfaceTypesReplyReply:
    __slots__ = ('num', 'surfaces',)

    def __init__(
            self, *,
            num: Optional[int] = None,
            surfaces: Optional[Sequence[int]] = None,
    ) -> None:
        self.num = num
        self.surfaces = surfaces

    def as_dict(self) -> Dict[str, Any]:
        return {
            'num': self.num,
            'surfaces': self.surfaces,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ListSurfaceTypesReplyReply':
        return ListSurfaceTypesReplyReply(**ListSurfaceTypesReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ListSurfaceTypesReplyReplyPacket.pack(**self.as_dict())


class ListSurfaceTypesReplyReplyCType(ctypes.Structure):
    """xvmc ListSurfaceTypes_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("num", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


CreateContextRequestCookie = NewType('CreateContextRequestCookie', ctypes.c_uint32)


CreateContextRequestPacket = DataPacket((
    ('context_id', FixedDataPacketField(MARKER_UINT32)),
    ('port_id', FixedDataPacketField(MARKER_UINT32)),
    ('surface_id', FixedDataPacketField(MARKER_UINT32)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('flags', FixedDataPacketField(MARKER_UINT32)),
))


class CreateContextRequest:
    OPCODE = 2

    __slots__ = ('context_id', 'port_id', 'surface_id', 'width', 'height', 'flags',)

    def __init__(
            self, *,
            context_id: Optional[int] = None,
            port_id: Optional[int] = None,
            surface_id: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            flags: Optional[int] = None,
    ) -> None:
        self.context_id = context_id
        self.port_id = port_id
        self.surface_id = surface_id
        self.width = width
        self.height = height
        self.flags = flags

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_id': self.context_id,
            'port_id': self.port_id,
            'surface_id': self.surface_id,
            'width': self.width,
            'height': self.height,
            'flags': self.flags,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateContextRequest':
        return CreateContextRequest(**CreateContextRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateContextRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int], CreateContextRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateContextRequest.lib = library.xvmc_createcontext
        CreateContextRequest.lib.restype = CreateContextRequestCookie
        CreateContextRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint32)


class CreateContextRequestCType(ctypes.Structure):
    """xvmc CreateContext"""
    _fields_ = [
        ("context_id", ctypes.c_uint32),
        ("port_id", ctypes.c_uint32),
        ("surface_id", ctypes.c_uint32),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("flags", ctypes.c_uint32),
    ]


CreateContextReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('width_actual', FixedDataPacketField(MARKER_UINT16)),
    ('height_actual', FixedDataPacketField(MARKER_UINT16)),
    ('flags_return', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('priv_data', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['length'], 0)),
))


class CreateContextReplyReply:
    __slots__ = ('width_actual', 'height_actual', 'flags_return', 'priv_data',)

    def __init__(
            self, *,
            width_actual: Optional[int] = None,
            height_actual: Optional[int] = None,
            flags_return: Optional[int] = None,
            priv_data: Optional[Sequence[int]] = None,
    ) -> None:
        self.width_actual = width_actual
        self.height_actual = height_actual
        self.flags_return = flags_return
        self.priv_data = priv_data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'width_actual': self.width_actual,
            'height_actual': self.height_actual,
            'flags_return': self.flags_return,
            'priv_data': self.priv_data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateContextReplyReply':
        return CreateContextReplyReply(**CreateContextReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateContextReplyReplyPacket.pack(**self.as_dict())


class CreateContextReplyReplyCType(ctypes.Structure):
    """xvmc CreateContext_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("width_actual", ctypes.c_uint16),
        ("height_actual", ctypes.c_uint16),
        ("flags_return", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


DestroyContextRequestPacket = DataPacket((
    ('context_id', FixedDataPacketField(MARKER_UINT32)),
))


class DestroyContextRequest:
    OPCODE = 3

    __slots__ = ('context_id',)

    def __init__(
            self, *,
            context_id: Optional[int] = None,
    ) -> None:
        self.context_id = context_id

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_id': self.context_id,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DestroyContextRequest':
        return DestroyContextRequest(**DestroyContextRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DestroyContextRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        DestroyContextRequest.lib = library.xvmc_destroycontext
        DestroyContextRequest.lib.restype = ctypes.c_uint32
        DestroyContextRequest.lib.argstype = (ctypes.c_uint32,)


class DestroyContextRequestCType(ctypes.Structure):
    """xvmc DestroyContext"""
    _fields_ = [
        ("context_id", ctypes.c_uint32),
    ]


CreateSurfaceRequestCookie = NewType('CreateSurfaceRequestCookie', ctypes.c_uint32)


CreateSurfaceRequestPacket = DataPacket((
    ('surface_id', FixedDataPacketField(MARKER_UINT32)),
    ('context_id', FixedDataPacketField(MARKER_UINT32)),
))


class CreateSurfaceRequest:
    OPCODE = 4

    __slots__ = ('surface_id', 'context_id',)

    def __init__(
            self, *,
            surface_id: Optional[int] = None,
            context_id: Optional[int] = None,
    ) -> None:
        self.surface_id = surface_id
        self.context_id = context_id

    def as_dict(self) -> Dict[str, Any]:
        return {
            'surface_id': self.surface_id,
            'context_id': self.context_id,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateSurfaceRequest':
        return CreateSurfaceRequest(**CreateSurfaceRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateSurfaceRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], CreateSurfaceRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateSurfaceRequest.lib = library.xvmc_createsurface
        CreateSurfaceRequest.lib.restype = CreateSurfaceRequestCookie
        CreateSurfaceRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class CreateSurfaceRequestCType(ctypes.Structure):
    """xvmc CreateSurface"""
    _fields_ = [
        ("surface_id", ctypes.c_uint32),
        ("context_id", ctypes.c_uint32),
    ]


CreateSurfaceReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(24)),
    ('priv_data', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['length'], 0)),
))


class CreateSurfaceReplyReply:
    __slots__ = ('priv_data',)

    def __init__(
            self, *,
            priv_data: Optional[Sequence[int]] = None,
    ) -> None:
        self.priv_data = priv_data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'priv_data': self.priv_data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateSurfaceReplyReply':
        return CreateSurfaceReplyReply(**CreateSurfaceReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateSurfaceReplyReplyPacket.pack(**self.as_dict())


class CreateSurfaceReplyReplyCType(ctypes.Structure):
    """xvmc CreateSurface_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 24),
        ("var_data", ctypes.c_void_p),
    ]


DestroySurfaceRequestPacket = DataPacket((
    ('surface_id', FixedDataPacketField(MARKER_UINT32)),
))


class DestroySurfaceRequest:
    OPCODE = 5

    __slots__ = ('surface_id',)

    def __init__(
            self, *,
            surface_id: Optional[int] = None,
    ) -> None:
        self.surface_id = surface_id

    def as_dict(self) -> Dict[str, Any]:
        return {
            'surface_id': self.surface_id,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DestroySurfaceRequest':
        return DestroySurfaceRequest(**DestroySurfaceRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DestroySurfaceRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        DestroySurfaceRequest.lib = library.xvmc_destroysurface
        DestroySurfaceRequest.lib.restype = ctypes.c_uint32
        DestroySurfaceRequest.lib.argstype = (ctypes.c_uint32,)


class DestroySurfaceRequestCType(ctypes.Structure):
    """xvmc DestroySurface"""
    _fields_ = [
        ("surface_id", ctypes.c_uint32),
    ]


CreateSubpictureRequestCookie = NewType('CreateSubpictureRequestCookie', ctypes.c_uint32)


CreateSubpictureRequestPacket = DataPacket((
    ('subpicture_id', FixedDataPacketField(MARKER_UINT32)),
    ('context', FixedDataPacketField(MARKER_UINT32)),
    ('xvimage_id', FixedDataPacketField(MARKER_UINT32)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
))


class CreateSubpictureRequest:
    OPCODE = 6

    __slots__ = ('subpicture_id', 'context', 'xvimage_id', 'width', 'height',)

    def __init__(
            self, *,
            subpicture_id: Optional[int] = None,
            context: Optional[int] = None,
            xvimage_id: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
    ) -> None:
        self.subpicture_id = subpicture_id
        self.context = context
        self.xvimage_id = xvimage_id
        self.width = width
        self.height = height

    def as_dict(self) -> Dict[str, Any]:
        return {
            'subpicture_id': self.subpicture_id,
            'context': self.context,
            'xvimage_id': self.xvimage_id,
            'width': self.width,
            'height': self.height,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateSubpictureRequest':
        return CreateSubpictureRequest(**CreateSubpictureRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateSubpictureRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int], CreateSubpictureRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateSubpictureRequest.lib = library.xvmc_createsubpicture
        CreateSubpictureRequest.lib.restype = CreateSubpictureRequestCookie
        CreateSubpictureRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16)


class CreateSubpictureRequestCType(ctypes.Structure):
    """xvmc CreateSubpicture"""
    _fields_ = [
        ("subpicture_id", ctypes.c_uint32),
        ("context", ctypes.c_uint32),
        ("xvimage_id", ctypes.c_uint32),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
    ]


CreateSubpictureReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('width_actual', FixedDataPacketField(MARKER_UINT16)),
    ('height_actual', FixedDataPacketField(MARKER_UINT16)),
    ('num_palette_entries', FixedDataPacketField(MARKER_UINT16)),
    ('entry_bytes', FixedDataPacketField(MARKER_UINT16)),
    ('component_order', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: 4, 0)),
    ('pad1', FixedPadDataPacketField(12)),
    ('priv_data', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['length'], 0)),
))


class CreateSubpictureReplyReply:
    __slots__ = ('width_actual', 'height_actual', 'num_palette_entries', 'entry_bytes', 'component_order', 'priv_data',)

    def __init__(
            self, *,
            width_actual: Optional[int] = None,
            height_actual: Optional[int] = None,
            num_palette_entries: Optional[int] = None,
            entry_bytes: Optional[int] = None,
            component_order: Optional[Sequence[int]] = None,
            priv_data: Optional[Sequence[int]] = None,
    ) -> None:
        self.width_actual = width_actual
        self.height_actual = height_actual
        self.num_palette_entries = num_palette_entries
        self.entry_bytes = entry_bytes
        self.component_order = component_order
        self.priv_data = priv_data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'width_actual': self.width_actual,
            'height_actual': self.height_actual,
            'num_palette_entries': self.num_palette_entries,
            'entry_bytes': self.entry_bytes,
            'component_order': self.component_order,
            'priv_data': self.priv_data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateSubpictureReplyReply':
        return CreateSubpictureReplyReply(**CreateSubpictureReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateSubpictureReplyReplyPacket.pack(**self.as_dict())


class CreateSubpictureReplyReplyCType(ctypes.Structure):
    """xvmc CreateSubpicture_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("width_actual", ctypes.c_uint16),
        ("height_actual", ctypes.c_uint16),
        ("num_palette_entries", ctypes.c_uint16),
        ("entry_bytes", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


DestroySubpictureRequestPacket = DataPacket((
    ('subpicture_id', FixedDataPacketField(MARKER_UINT32)),
))


class DestroySubpictureRequest:
    OPCODE = 7

    __slots__ = ('subpicture_id',)

    def __init__(
            self, *,
            subpicture_id: Optional[int] = None,
    ) -> None:
        self.subpicture_id = subpicture_id

    def as_dict(self) -> Dict[str, Any]:
        return {
            'subpicture_id': self.subpicture_id,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DestroySubpictureRequest':
        return DestroySubpictureRequest(**DestroySubpictureRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DestroySubpictureRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        DestroySubpictureRequest.lib = library.xvmc_destroysubpicture
        DestroySubpictureRequest.lib.restype = ctypes.c_uint32
        DestroySubpictureRequest.lib.argstype = (ctypes.c_uint32,)


class DestroySubpictureRequestCType(ctypes.Structure):
    """xvmc DestroySubpicture"""
    _fields_ = [
        ("subpicture_id", ctypes.c_uint32),
    ]


ListSubpictureTypesRequestCookie = NewType('ListSubpictureTypesRequestCookie', ctypes.c_uint32)


ListSubpictureTypesRequestPacket = DataPacket((
    ('port_id', FixedDataPacketField(MARKER_UINT32)),
    ('surface_id', FixedDataPacketField(MARKER_UINT32)),
))


class ListSubpictureTypesRequest:
    OPCODE = 8

    __slots__ = ('port_id', 'surface_id',)

    def __init__(
            self, *,
            port_id: Optional[int] = None,
            surface_id: Optional[int] = None,
    ) -> None:
        self.port_id = port_id
        self.surface_id = surface_id

    def as_dict(self) -> Dict[str, Any]:
        return {
            'port_id': self.port_id,
            'surface_id': self.surface_id,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ListSubpictureTypesRequest':
        return ListSubpictureTypesRequest(**ListSubpictureTypesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ListSubpictureTypesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ListSubpictureTypesRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ListSubpictureTypesRequest.lib = library.xvmc_listsubpicturetypes
        ListSubpictureTypesRequest.lib.restype = ListSubpictureTypesRequestCookie
        ListSubpictureTypesRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class ListSubpictureTypesRequestCType(ctypes.Structure):
    """xvmc ListSubpictureTypes"""
    _fields_ = [
        ("port_id", ctypes.c_uint32),
        ("surface_id", ctypes.c_uint32),
    ]


ListSubpictureTypesReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('num', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('types', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num'], 0)),
))


class ListSubpictureTypesReplyReply:
    __slots__ = ('num', 'types',)

    def __init__(
            self, *,
            num: Optional[int] = None,
            types: Optional[Sequence[int]] = None,
    ) -> None:
        self.num = num
        self.types = types

    def as_dict(self) -> Dict[str, Any]:
        return {
            'num': self.num,
            'types': self.types,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ListSubpictureTypesReplyReply':
        return ListSubpictureTypesReplyReply(**ListSubpictureTypesReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ListSubpictureTypesReplyReplyPacket.pack(**self.as_dict())


class ListSubpictureTypesReplyReplyCType(ctypes.Structure):
    """xvmc ListSubpictureTypes_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("num", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


# ------------------------------------------------------------------
# Unions

