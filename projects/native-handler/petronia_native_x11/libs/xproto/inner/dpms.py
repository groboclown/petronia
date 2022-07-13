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

DpmsmodeType = NewType('DpmsmodeType', int)


class DpmsmodeValues:
    ON = DpmsmodeType(0)
    STANDBY = DpmsmodeType(1)
    SUSPEND = DpmsmodeType(2)
    OFF = DpmsmodeType(3)


# ------------------------------------------------------------------
# Aliases



# ------------------------------------------------------------------
# Structures, Events, Requests, Replies


GetVersionRequestCookie = NewType('GetVersionRequestCookie', ctypes.c_uint32)


GetVersionRequestPacket = DataPacket((
    ('client_major_version', FixedDataPacketField(MARKER_UINT16)),
    ('client_minor_version', FixedDataPacketField(MARKER_UINT16)),
))


class GetVersionRequest:
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
    def from_data(inp: BinaryIO) -> 'GetVersionRequest':
        return GetVersionRequest(**GetVersionRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetVersionRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], GetVersionRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetVersionRequest.lib = library.dpms_getversion
        GetVersionRequest.lib.restype = GetVersionRequestCookie
        GetVersionRequest.lib.argstype = (ctypes.c_uint16, ctypes.c_uint16)


class GetVersionRequestCType(ctypes.Structure):
    """dpms GetVersion"""
    _fields_ = [
        ("client_major_version", ctypes.c_uint16),
        ("client_minor_version", ctypes.c_uint16),
    ]


GetVersionReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('server_major_version', FixedDataPacketField(MARKER_UINT16)),
    ('server_minor_version', FixedDataPacketField(MARKER_UINT16)),
))


class GetVersionReplyReply:
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
    def from_data(inp: BinaryIO) -> 'GetVersionReplyReply':
        return GetVersionReplyReply(**GetVersionReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetVersionReplyReplyPacket.pack(**self.as_dict())


class GetVersionReplyReplyCType(ctypes.Structure):
    """dpms GetVersion_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("server_major_version", ctypes.c_uint16),
        ("server_minor_version", ctypes.c_uint16),
    ]


CapableRequestCookie = NewType('CapableRequestCookie', ctypes.c_uint32)


CapableRequestPacket = DataPacket((
))


class CapableRequest:
    OPCODE = 1

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CapableRequest':
        return CapableRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], CapableRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CapableRequest.lib = library.dpms_capable
        CapableRequest.lib.restype = CapableRequestCookie
        CapableRequest.lib.argstype = ()


class CapableRequestCType(ctypes.Structure):
    """dpms Capable"""
    _fields_ = [
    ]


CapableReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('capable', FixedDataPacketField(MARKER_UINT8)),
    ('pad1', FixedPadDataPacketField(23)),
))


class CapableReplyReply:
    __slots__ = ('capable',)

    def __init__(
            self, *,
            capable: Optional[bool] = None,
    ) -> None:
        self.capable = capable

    def as_dict(self) -> Dict[str, Any]:
        return {
            'capable': self.capable,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CapableReplyReply':
        return CapableReplyReply(**CapableReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CapableReplyReplyPacket.pack(**self.as_dict())


class CapableReplyReplyCType(ctypes.Structure):
    """dpms Capable_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("capable", ctypes.c_int8),
        ("pad1", ctypes.c_uint8 * 23),
    ]


GetTimeoutsRequestCookie = NewType('GetTimeoutsRequestCookie', ctypes.c_uint32)


GetTimeoutsRequestPacket = DataPacket((
))


class GetTimeoutsRequest:
    OPCODE = 2

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetTimeoutsRequest':
        return GetTimeoutsRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], GetTimeoutsRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetTimeoutsRequest.lib = library.dpms_gettimeouts
        GetTimeoutsRequest.lib.restype = GetTimeoutsRequestCookie
        GetTimeoutsRequest.lib.argstype = ()


class GetTimeoutsRequestCType(ctypes.Structure):
    """dpms GetTimeouts"""
    _fields_ = [
    ]


GetTimeoutsReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('standby_timeout', FixedDataPacketField(MARKER_UINT16)),
    ('suspend_timeout', FixedDataPacketField(MARKER_UINT16)),
    ('off_timeout', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(18)),
))


class GetTimeoutsReplyReply:
    __slots__ = ('standby_timeout', 'suspend_timeout', 'off_timeout',)

    def __init__(
            self, *,
            standby_timeout: Optional[int] = None,
            suspend_timeout: Optional[int] = None,
            off_timeout: Optional[int] = None,
    ) -> None:
        self.standby_timeout = standby_timeout
        self.suspend_timeout = suspend_timeout
        self.off_timeout = off_timeout

    def as_dict(self) -> Dict[str, Any]:
        return {
            'standby_timeout': self.standby_timeout,
            'suspend_timeout': self.suspend_timeout,
            'off_timeout': self.off_timeout,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetTimeoutsReplyReply':
        return GetTimeoutsReplyReply(**GetTimeoutsReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetTimeoutsReplyReplyPacket.pack(**self.as_dict())


class GetTimeoutsReplyReplyCType(ctypes.Structure):
    """dpms GetTimeouts_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("standby_timeout", ctypes.c_uint16),
        ("suspend_timeout", ctypes.c_uint16),
        ("off_timeout", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 18),
    ]


SetTimeoutsRequestPacket = DataPacket((
    ('standby_timeout', FixedDataPacketField(MARKER_UINT16)),
    ('suspend_timeout', FixedDataPacketField(MARKER_UINT16)),
    ('off_timeout', FixedDataPacketField(MARKER_UINT16)),
))


class SetTimeoutsRequest:
    OPCODE = 3

    __slots__ = ('standby_timeout', 'suspend_timeout', 'off_timeout',)

    def __init__(
            self, *,
            standby_timeout: Optional[int] = None,
            suspend_timeout: Optional[int] = None,
            off_timeout: Optional[int] = None,
    ) -> None:
        self.standby_timeout = standby_timeout
        self.suspend_timeout = suspend_timeout
        self.off_timeout = off_timeout

    def as_dict(self) -> Dict[str, Any]:
        return {
            'standby_timeout': self.standby_timeout,
            'suspend_timeout': self.suspend_timeout,
            'off_timeout': self.off_timeout,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetTimeoutsRequest':
        return SetTimeoutsRequest(**SetTimeoutsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetTimeoutsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetTimeoutsRequest.lib = library.dpms_settimeouts
        SetTimeoutsRequest.lib.restype = ctypes.c_uint32
        SetTimeoutsRequest.lib.argstype = (ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16)


class SetTimeoutsRequestCType(ctypes.Structure):
    """dpms SetTimeouts"""
    _fields_ = [
        ("standby_timeout", ctypes.c_uint16),
        ("suspend_timeout", ctypes.c_uint16),
        ("off_timeout", ctypes.c_uint16),
    ]


EnableRequestPacket = DataPacket((
))


class EnableRequest:
    OPCODE = 4

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'EnableRequest':
        return EnableRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        EnableRequest.lib = library.dpms_enable
        EnableRequest.lib.restype = ctypes.c_uint32
        EnableRequest.lib.argstype = ()


class EnableRequestCType(ctypes.Structure):
    """dpms Enable"""
    _fields_ = [
    ]


DisableRequestPacket = DataPacket((
))


class DisableRequest:
    OPCODE = 5

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DisableRequest':
        return DisableRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        DisableRequest.lib = library.dpms_disable
        DisableRequest.lib.restype = ctypes.c_uint32
        DisableRequest.lib.argstype = ()


class DisableRequestCType(ctypes.Structure):
    """dpms Disable"""
    _fields_ = [
    ]


ForceLevelRequestPacket = DataPacket((
    ('power_level', FixedDataPacketField(MARKER_UINT16)),
))


class ForceLevelRequest:
    OPCODE = 6

    __slots__ = ('power_level',)

    def __init__(
            self, *,
            power_level: Optional[int] = None,
    ) -> None:
        self.power_level = power_level

    def as_dict(self) -> Dict[str, Any]:
        return {
            'power_level': self.power_level,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ForceLevelRequest':
        return ForceLevelRequest(**ForceLevelRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ForceLevelRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ForceLevelRequest.lib = library.dpms_forcelevel
        ForceLevelRequest.lib.restype = ctypes.c_uint32
        ForceLevelRequest.lib.argstype = (ctypes.c_uint16,)


class ForceLevelRequestCType(ctypes.Structure):
    """dpms ForceLevel"""
    _fields_ = [
        ("power_level", ctypes.c_uint16),
    ]


InfoRequestCookie = NewType('InfoRequestCookie', ctypes.c_uint32)


InfoRequestPacket = DataPacket((
))


class InfoRequest:
    OPCODE = 7

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'InfoRequest':
        return InfoRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], InfoRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        InfoRequest.lib = library.dpms_info
        InfoRequest.lib.restype = InfoRequestCookie
        InfoRequest.lib.argstype = ()


class InfoRequestCType(ctypes.Structure):
    """dpms Info"""
    _fields_ = [
    ]


InfoReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('power_level', FixedDataPacketField(MARKER_UINT16)),
    ('state', FixedDataPacketField(MARKER_UINT8)),
    ('pad1', FixedPadDataPacketField(21)),
))


class InfoReplyReply:
    __slots__ = ('power_level', 'state',)

    def __init__(
            self, *,
            power_level: Optional[int] = None,
            state: Optional[bool] = None,
    ) -> None:
        self.power_level = power_level
        self.state = state

    def as_dict(self) -> Dict[str, Any]:
        return {
            'power_level': self.power_level,
            'state': self.state,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'InfoReplyReply':
        return InfoReplyReply(**InfoReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return InfoReplyReplyPacket.pack(**self.as_dict())


class InfoReplyReplyCType(ctypes.Structure):
    """dpms Info_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("power_level", ctypes.c_uint16),
        ("state", ctypes.c_int8),
        ("pad1", ctypes.c_uint8 * 21),
    ]


# ------------------------------------------------------------------
# Unions

