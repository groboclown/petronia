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

EventType = NewType('EventType', int)


class EventValues:
    CONFIGURE_NOTIFY = EventType(0)
    COMPLETE_NOTIFY = EventType(1)
    IDLE_NOTIFY = EventType(2)
    REDIRECT_NOTIFY = EventType(3)


EventMaskType = NewType('EventMaskType', int)


class EventMaskValues:
    NO_EVENT = EventMaskType(0)
    CONFIGURE_NOTIFY = EventMaskType(1)
    COMPLETE_NOTIFY = EventMaskType(2)
    IDLE_NOTIFY = EventMaskType(4)
    REDIRECT_NOTIFY = EventMaskType(8)


OptionType = NewType('OptionType', int)


class OptionValues:
    NONE = OptionType(0)
    ASYNC = OptionType(1)
    COPY = OptionType(2)
    UST = OptionType(4)
    SUBOPTIMAL = OptionType(8)


CapabilityType = NewType('CapabilityType', int)


class CapabilityValues:
    NONE = CapabilityType(0)
    ASYNC = CapabilityType(1)
    FENCE = CapabilityType(2)
    UST = CapabilityType(4)


CompleteKindType = NewType('CompleteKindType', int)


class CompleteKindValues:
    PIXMAP = CompleteKindType(0)
    NOTIFY_MSC = CompleteKindType(1)


CompleteModeType = NewType('CompleteModeType', int)


class CompleteModeValues:
    COPY = CompleteModeType(0)
    FLIP = CompleteModeType(1)
    SKIP = CompleteModeType(2)
    SUBOPTIMAL_COPY = CompleteModeType(3)


# ------------------------------------------------------------------
# Aliases

Event = NewType('Event', ctypes.c_uint32)


# ------------------------------------------------------------------
# Structures, Events, Requests, Replies


NotifyStructPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('serial', FixedDataPacketField(MARKER_UINT32)),
))


class NotifyStruct:
    __slots__ = ('window', 'serial',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            serial: Optional[int] = None,
    ) -> None:
        self.window = window
        self.serial = serial

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'serial': self.serial,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'NotifyStruct':
        return NotifyStruct(**NotifyStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return NotifyStructPacket.pack(**self.as_dict())


class NotifyStructCType(ctypes.Structure):
    """present Notify"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("serial", ctypes.c_uint32),
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
        QueryVersionRequest.lib = library.present_queryversion
        QueryVersionRequest.lib.restype = QueryVersionRequestCookie
        QueryVersionRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class QueryVersionRequestCType(ctypes.Structure):
    """present QueryVersion"""
    _fields_ = [
        ("major_version", ctypes.c_uint32),
        ("minor_version", ctypes.c_uint32),
    ]


QueryVersionReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('major_version', FixedDataPacketField(MARKER_UINT32)),
    ('minor_version', FixedDataPacketField(MARKER_UINT32)),
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
    """present QueryVersion_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("major_version", ctypes.c_uint32),
        ("minor_version", ctypes.c_uint32),
    ]


PixmapRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('pixmap', FixedDataPacketField(MARKER_UINT32)),
    ('serial', FixedDataPacketField(MARKER_UINT32)),
    ('valid', FixedDataPacketField(MARKER_UINT32)),
    ('update', FixedDataPacketField(MARKER_UINT32)),
    ('x_off', FixedDataPacketField(MARKER_INT16)),
    ('y_off', FixedDataPacketField(MARKER_INT16)),
    ('target_crtc', FixedDataPacketField(MARKER_UINT32)),
    ('wait_fence', FixedDataPacketField(MARKER_UINT32)),
    ('idle_fence', FixedDataPacketField(MARKER_UINT32)),
    ('options', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(4)),
    ('target_msc', FixedDataPacketField(MARKER_UINT64)),
    ('divisor', FixedDataPacketField(MARKER_UINT64)),
    ('remainder', FixedDataPacketField(MARKER_UINT64)),
    ('notifies', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 1, 0)),
))


class PixmapRequest:
    OPCODE = 1

    __slots__ = ('window', 'pixmap', 'serial', 'valid', 'update', 'x_off', 'y_off', 'target_crtc', 'wait_fence', 'idle_fence', 'options', 'target_msc', 'divisor', 'remainder', 'notifies',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            pixmap: Optional[int] = None,
            serial: Optional[int] = None,
            valid: Optional[int] = None,
            update: Optional[int] = None,
            x_off: Optional[int] = None,
            y_off: Optional[int] = None,
            target_crtc: Optional[int] = None,
            wait_fence: Optional[int] = None,
            idle_fence: Optional[int] = None,
            options: Optional[int] = None,
            target_msc: Optional[int] = None,
            divisor: Optional[int] = None,
            remainder: Optional[int] = None,
            notifies: Optional[Sequence[int]] = None,
    ) -> None:
        self.window = window
        self.pixmap = pixmap
        self.serial = serial
        self.valid = valid
        self.update = update
        self.x_off = x_off
        self.y_off = y_off
        self.target_crtc = target_crtc
        self.wait_fence = wait_fence
        self.idle_fence = idle_fence
        self.options = options
        self.target_msc = target_msc
        self.divisor = divisor
        self.remainder = remainder
        self.notifies = notifies

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'pixmap': self.pixmap,
            'serial': self.serial,
            'valid': self.valid,
            'update': self.update,
            'x_off': self.x_off,
            'y_off': self.y_off,
            'target_crtc': self.target_crtc,
            'wait_fence': self.wait_fence,
            'idle_fence': self.idle_fence,
            'options': self.options,
            'target_msc': self.target_msc,
            'divisor': self.divisor,
            'remainder': self.remainder,
            'notifies': self.notifies,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PixmapRequest':
        return PixmapRequest(**PixmapRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PixmapRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, int, int, int, int, int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PixmapRequest.lib = library.present_pixmap
        PixmapRequest.lib.restype = ctypes.c_uint32
        PixmapRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8 * 4, ctypes.c_uint64, ctypes.c_uint64, ctypes.c_uint64, ctypes.c_void_p)


class PixmapRequestCType(ctypes.Structure):
    """present Pixmap"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("pixmap", ctypes.c_uint32),
        ("serial", ctypes.c_uint32),
        ("valid", ctypes.c_uint32),
        ("update", ctypes.c_uint32),
        ("x_off", ctypes.c_int16),
        ("y_off", ctypes.c_int16),
        ("target_crtc", ctypes.c_uint32),
        ("wait_fence", ctypes.c_uint32),
        ("idle_fence", ctypes.c_uint32),
        ("options", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 4),
        ("target_msc", ctypes.c_uint64),
        ("divisor", ctypes.c_uint64),
        ("remainder", ctypes.c_uint64),
        ("var_data", ctypes.c_void_p),
    ]


NotifyMscRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('serial', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(4)),
    ('target_msc', FixedDataPacketField(MARKER_UINT64)),
    ('divisor', FixedDataPacketField(MARKER_UINT64)),
    ('remainder', FixedDataPacketField(MARKER_UINT64)),
))


class NotifyMscRequest:
    OPCODE = 2

    __slots__ = ('window', 'serial', 'target_msc', 'divisor', 'remainder',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            serial: Optional[int] = None,
            target_msc: Optional[int] = None,
            divisor: Optional[int] = None,
            remainder: Optional[int] = None,
    ) -> None:
        self.window = window
        self.serial = serial
        self.target_msc = target_msc
        self.divisor = divisor
        self.remainder = remainder

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'serial': self.serial,
            'target_msc': self.target_msc,
            'divisor': self.divisor,
            'remainder': self.remainder,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'NotifyMscRequest':
        return NotifyMscRequest(**NotifyMscRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return NotifyMscRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        NotifyMscRequest.lib = library.present_notifymsc
        NotifyMscRequest.lib.restype = ctypes.c_uint32
        NotifyMscRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8 * 4, ctypes.c_uint64, ctypes.c_uint64, ctypes.c_uint64)


class NotifyMscRequestCType(ctypes.Structure):
    """present NotifyMSC"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("serial", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 4),
        ("target_msc", ctypes.c_uint64),
        ("divisor", ctypes.c_uint64),
        ("remainder", ctypes.c_uint64),
    ]


SelectInputRequestPacket = DataPacket((
    ('eid', FixedDataPacketField(MARKER_UINT32)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('event_mask', FixedDataPacketField(MARKER_UINT32)),
))


class SelectInputRequest:
    OPCODE = 3

    __slots__ = ('eid', 'window', 'event_mask',)

    def __init__(
            self, *,
            eid: Optional[int] = None,
            window: Optional[int] = None,
            event_mask: Optional[int] = None,
    ) -> None:
        self.eid = eid
        self.window = window
        self.event_mask = event_mask

    def as_dict(self) -> Dict[str, Any]:
        return {
            'eid': self.eid,
            'window': self.window,
            'event_mask': self.event_mask,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SelectInputRequest':
        return SelectInputRequest(**SelectInputRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SelectInputRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SelectInputRequest.lib = library.present_selectinput
        SelectInputRequest.lib.restype = ctypes.c_uint32
        SelectInputRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class SelectInputRequestCType(ctypes.Structure):
    """present SelectInput"""
    _fields_ = [
        ("eid", ctypes.c_uint32),
        ("window", ctypes.c_uint32),
        ("event_mask", ctypes.c_uint32),
    ]


QueryCapabilitiesRequestCookie = NewType('QueryCapabilitiesRequestCookie', ctypes.c_uint32)


QueryCapabilitiesRequestPacket = DataPacket((
    ('target', FixedDataPacketField(MARKER_UINT32)),
))


class QueryCapabilitiesRequest:
    OPCODE = 4

    __slots__ = ('target',)

    def __init__(
            self, *,
            target: Optional[int] = None,
    ) -> None:
        self.target = target

    def as_dict(self) -> Dict[str, Any]:
        return {
            'target': self.target,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryCapabilitiesRequest':
        return QueryCapabilitiesRequest(**QueryCapabilitiesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryCapabilitiesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], QueryCapabilitiesRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryCapabilitiesRequest.lib = library.present_querycapabilities
        QueryCapabilitiesRequest.lib.restype = QueryCapabilitiesRequestCookie
        QueryCapabilitiesRequest.lib.argstype = (ctypes.c_uint32,)


class QueryCapabilitiesRequestCType(ctypes.Structure):
    """present QueryCapabilities"""
    _fields_ = [
        ("target", ctypes.c_uint32),
    ]


QueryCapabilitiesReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('capabilities', FixedDataPacketField(MARKER_UINT32)),
))


class QueryCapabilitiesReplyReply:
    __slots__ = ('capabilities',)

    def __init__(
            self, *,
            capabilities: Optional[int] = None,
    ) -> None:
        self.capabilities = capabilities

    def as_dict(self) -> Dict[str, Any]:
        return {
            'capabilities': self.capabilities,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryCapabilitiesReplyReply':
        return QueryCapabilitiesReplyReply(**QueryCapabilitiesReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryCapabilitiesReplyReplyPacket.pack(**self.as_dict())


class QueryCapabilitiesReplyReplyCType(ctypes.Structure):
    """present QueryCapabilities_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("capabilities", ctypes.c_uint32),
    ]


GenericEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('extension', FixedDataPacketField(MARKER_UINT8)),
    ('length', FixedDataPacketField(MARKER_UINT32)),
    ('evtype', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
    ('event', FixedDataPacketField(MARKER_UINT32)),
))


class GenericEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'extension', 'length', 'evtype', 'event',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            extension: Optional[int] = None,
            length: Optional[int] = None,
            evtype: Optional[int] = None,
            event: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.extension = extension
        self.length = length
        self.evtype = evtype
        self.event = event

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'extension': self.extension,
            'length': self.length,
            'evtype': self.evtype,
            'event': self.event,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GenericEvent':
        return GenericEvent(**GenericEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GenericEventPacket.pack(**self.as_dict())


class GenericEventCType(ctypes.Structure):
    """present Generic"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("extension", ctypes.c_uint8),
        ("length", ctypes.c_uint32),
        ("evtype", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
        ("event", ctypes.c_uint32),
    ]


ConfigureNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('extension', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('length', FixedDataPacketField(MARKER_UINT32)),
    ('event_type', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
    ('event', FixedDataPacketField(MARKER_UINT32)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('x', FixedDataPacketField(MARKER_INT16)),
    ('y', FixedDataPacketField(MARKER_INT16)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('off_x', FixedDataPacketField(MARKER_INT16)),
    ('off_y', FixedDataPacketField(MARKER_INT16)),
    ('pixmap_width', FixedDataPacketField(MARKER_UINT16)),
    ('pixmap_height', FixedDataPacketField(MARKER_UINT16)),
    ('pixmap_flags', FixedDataPacketField(MARKER_UINT32)),
))


class ConfigureNotifyEvent:
    __slots__ = ('response_type', 'extension', 'sequence', 'length', 'event_type', 'event', 'window', 'x', 'y', 'width', 'height', 'off_x', 'off_y', 'pixmap_width', 'pixmap_height', 'pixmap_flags',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            extension: Optional[int] = None,
            sequence: Optional[int] = None,
            length: Optional[int] = None,
            event_type: Optional[int] = None,
            event: Optional[int] = None,
            window: Optional[int] = None,
            x: Optional[int] = None,
            y: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            off_x: Optional[int] = None,
            off_y: Optional[int] = None,
            pixmap_width: Optional[int] = None,
            pixmap_height: Optional[int] = None,
            pixmap_flags: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.extension = extension
        self.sequence = sequence
        self.length = length
        self.event_type = event_type
        self.event = event
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.off_x = off_x
        self.off_y = off_y
        self.pixmap_width = pixmap_width
        self.pixmap_height = pixmap_height
        self.pixmap_flags = pixmap_flags

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'extension': self.extension,
            'sequence': self.sequence,
            'length': self.length,
            'event_type': self.event_type,
            'event': self.event,
            'window': self.window,
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height,
            'off_x': self.off_x,
            'off_y': self.off_y,
            'pixmap_width': self.pixmap_width,
            'pixmap_height': self.pixmap_height,
            'pixmap_flags': self.pixmap_flags,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ConfigureNotifyEvent':
        return ConfigureNotifyEvent(**ConfigureNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ConfigureNotifyEventPacket.pack(**self.as_dict())


class ConfigureNotifyEventCType(ctypes.Structure):
    """present ConfigureNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("extension", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("length", ctypes.c_uint32),
        ("event_type", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
        ("event", ctypes.c_uint32),
        ("window", ctypes.c_uint32),
        ("x", ctypes.c_int16),
        ("y", ctypes.c_int16),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("off_x", ctypes.c_int16),
        ("off_y", ctypes.c_int16),
        ("pixmap_width", ctypes.c_uint16),
        ("pixmap_height", ctypes.c_uint16),
        ("pixmap_flags", ctypes.c_uint32),
    ]


CompleteNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('extension', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('length', FixedDataPacketField(MARKER_UINT32)),
    ('event_type', FixedDataPacketField(MARKER_UINT16)),
    ('kind', FixedDataPacketField(MARKER_UINT8)),
    ('mode', FixedDataPacketField(MARKER_UINT8)),
    ('event', FixedDataPacketField(MARKER_UINT32)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('serial', FixedDataPacketField(MARKER_UINT32)),
    ('ust', FixedDataPacketField(MARKER_UINT64)),
    ('msc', FixedDataPacketField(MARKER_UINT64)),
))


class CompleteNotifyEvent:
    __slots__ = ('response_type', 'extension', 'sequence', 'length', 'event_type', 'kind', 'mode', 'event', 'window', 'serial', 'ust', 'msc',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            extension: Optional[int] = None,
            sequence: Optional[int] = None,
            length: Optional[int] = None,
            event_type: Optional[int] = None,
            kind: Optional[int] = None,
            mode: Optional[int] = None,
            event: Optional[int] = None,
            window: Optional[int] = None,
            serial: Optional[int] = None,
            ust: Optional[int] = None,
            msc: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.extension = extension
        self.sequence = sequence
        self.length = length
        self.event_type = event_type
        self.kind = kind
        self.mode = mode
        self.event = event
        self.window = window
        self.serial = serial
        self.ust = ust
        self.msc = msc

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'extension': self.extension,
            'sequence': self.sequence,
            'length': self.length,
            'event_type': self.event_type,
            'kind': self.kind,
            'mode': self.mode,
            'event': self.event,
            'window': self.window,
            'serial': self.serial,
            'ust': self.ust,
            'msc': self.msc,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CompleteNotifyEvent':
        return CompleteNotifyEvent(**CompleteNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CompleteNotifyEventPacket.pack(**self.as_dict())


class CompleteNotifyEventCType(ctypes.Structure):
    """present CompleteNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("extension", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("length", ctypes.c_uint32),
        ("event_type", ctypes.c_uint16),
        ("kind", ctypes.c_uint8),
        ("mode", ctypes.c_uint8),
        ("event", ctypes.c_uint32),
        ("window", ctypes.c_uint32),
        ("serial", ctypes.c_uint32),
        ("ust", ctypes.c_uint64),
        ("msc", ctypes.c_uint64),
    ]


IdleNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('extension', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('length', FixedDataPacketField(MARKER_UINT32)),
    ('event_type', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
    ('event', FixedDataPacketField(MARKER_UINT32)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('serial', FixedDataPacketField(MARKER_UINT32)),
    ('pixmap', FixedDataPacketField(MARKER_UINT32)),
    ('idle_fence', FixedDataPacketField(MARKER_UINT32)),
))


class IdleNotifyEvent:
    __slots__ = ('response_type', 'extension', 'sequence', 'length', 'event_type', 'event', 'window', 'serial', 'pixmap', 'idle_fence',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            extension: Optional[int] = None,
            sequence: Optional[int] = None,
            length: Optional[int] = None,
            event_type: Optional[int] = None,
            event: Optional[int] = None,
            window: Optional[int] = None,
            serial: Optional[int] = None,
            pixmap: Optional[int] = None,
            idle_fence: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.extension = extension
        self.sequence = sequence
        self.length = length
        self.event_type = event_type
        self.event = event
        self.window = window
        self.serial = serial
        self.pixmap = pixmap
        self.idle_fence = idle_fence

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'extension': self.extension,
            'sequence': self.sequence,
            'length': self.length,
            'event_type': self.event_type,
            'event': self.event,
            'window': self.window,
            'serial': self.serial,
            'pixmap': self.pixmap,
            'idle_fence': self.idle_fence,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'IdleNotifyEvent':
        return IdleNotifyEvent(**IdleNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return IdleNotifyEventPacket.pack(**self.as_dict())


class IdleNotifyEventCType(ctypes.Structure):
    """present IdleNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("extension", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("length", ctypes.c_uint32),
        ("event_type", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
        ("event", ctypes.c_uint32),
        ("window", ctypes.c_uint32),
        ("serial", ctypes.c_uint32),
        ("pixmap", ctypes.c_uint32),
        ("idle_fence", ctypes.c_uint32),
    ]


RedirectNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('extension', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('length', FixedDataPacketField(MARKER_UINT32)),
    ('event_type', FixedDataPacketField(MARKER_UINT16)),
    ('update_window', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('event', FixedDataPacketField(MARKER_UINT32)),
    ('event_window', FixedDataPacketField(MARKER_UINT32)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('pixmap', FixedDataPacketField(MARKER_UINT32)),
    ('serial', FixedDataPacketField(MARKER_UINT32)),
    ('valid_region', FixedDataPacketField(MARKER_UINT32)),
    ('update_region', FixedDataPacketField(MARKER_UINT32)),
    ('valid_rect', FixedDataPacketField(MARKER_UINT32)),
    ('update_rect', FixedDataPacketField(MARKER_UINT32)),
    ('x_off', FixedDataPacketField(MARKER_INT16)),
    ('y_off', FixedDataPacketField(MARKER_INT16)),
    ('target_crtc', FixedDataPacketField(MARKER_UINT32)),
    ('wait_fence', FixedDataPacketField(MARKER_UINT32)),
    ('idle_fence', FixedDataPacketField(MARKER_UINT32)),
    ('options', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(4)),
    ('target_msc', FixedDataPacketField(MARKER_UINT64)),
    ('divisor', FixedDataPacketField(MARKER_UINT64)),
    ('remainder', FixedDataPacketField(MARKER_UINT64)),
    ('notifies', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 1, 0)),
))


class RedirectNotifyEvent:
    __slots__ = ('response_type', 'extension', 'sequence', 'length', 'event_type', 'update_window', 'event', 'event_window', 'window', 'pixmap', 'serial', 'valid_region', 'update_region', 'valid_rect', 'update_rect', 'x_off', 'y_off', 'target_crtc', 'wait_fence', 'idle_fence', 'options', 'target_msc', 'divisor', 'remainder', 'notifies',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            extension: Optional[int] = None,
            sequence: Optional[int] = None,
            length: Optional[int] = None,
            event_type: Optional[int] = None,
            update_window: Optional[bool] = None,
            event: Optional[int] = None,
            event_window: Optional[int] = None,
            window: Optional[int] = None,
            pixmap: Optional[int] = None,
            serial: Optional[int] = None,
            valid_region: Optional[int] = None,
            update_region: Optional[int] = None,
            valid_rect: Optional[int] = None,
            update_rect: Optional[int] = None,
            x_off: Optional[int] = None,
            y_off: Optional[int] = None,
            target_crtc: Optional[int] = None,
            wait_fence: Optional[int] = None,
            idle_fence: Optional[int] = None,
            options: Optional[int] = None,
            target_msc: Optional[int] = None,
            divisor: Optional[int] = None,
            remainder: Optional[int] = None,
            notifies: Optional[Sequence[int]] = None,
    ) -> None:
        self.response_type = response_type
        self.extension = extension
        self.sequence = sequence
        self.length = length
        self.event_type = event_type
        self.update_window = update_window
        self.event = event
        self.event_window = event_window
        self.window = window
        self.pixmap = pixmap
        self.serial = serial
        self.valid_region = valid_region
        self.update_region = update_region
        self.valid_rect = valid_rect
        self.update_rect = update_rect
        self.x_off = x_off
        self.y_off = y_off
        self.target_crtc = target_crtc
        self.wait_fence = wait_fence
        self.idle_fence = idle_fence
        self.options = options
        self.target_msc = target_msc
        self.divisor = divisor
        self.remainder = remainder
        self.notifies = notifies

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'extension': self.extension,
            'sequence': self.sequence,
            'length': self.length,
            'event_type': self.event_type,
            'update_window': self.update_window,
            'event': self.event,
            'event_window': self.event_window,
            'window': self.window,
            'pixmap': self.pixmap,
            'serial': self.serial,
            'valid_region': self.valid_region,
            'update_region': self.update_region,
            'valid_rect': self.valid_rect,
            'update_rect': self.update_rect,
            'x_off': self.x_off,
            'y_off': self.y_off,
            'target_crtc': self.target_crtc,
            'wait_fence': self.wait_fence,
            'idle_fence': self.idle_fence,
            'options': self.options,
            'target_msc': self.target_msc,
            'divisor': self.divisor,
            'remainder': self.remainder,
            'notifies': self.notifies,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'RedirectNotifyEvent':
        return RedirectNotifyEvent(**RedirectNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return RedirectNotifyEventPacket.pack(**self.as_dict())


class RedirectNotifyEventCType(ctypes.Structure):
    """present RedirectNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("extension", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("length", ctypes.c_uint32),
        ("event_type", ctypes.c_uint16),
        ("update_window", ctypes.c_int8),
        ("pad0", ctypes.c_uint8),
        ("event", ctypes.c_uint32),
        ("event_window", ctypes.c_uint32),
        ("window", ctypes.c_uint32),
        ("pixmap", ctypes.c_uint32),
        ("serial", ctypes.c_uint32),
        ("valid_region", ctypes.c_uint32),
        ("update_region", ctypes.c_uint32),
        ("valid_rect", ctypes.c_uint32),
        ("update_rect", ctypes.c_uint32),
        ("x_off", ctypes.c_int16),
        ("y_off", ctypes.c_int16),
        ("target_crtc", ctypes.c_uint32),
        ("wait_fence", ctypes.c_uint32),
        ("idle_fence", ctypes.c_uint32),
        ("options", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 4),
        ("target_msc", ctypes.c_uint64),
        ("divisor", ctypes.c_uint64),
        ("remainder", ctypes.c_uint64),
        ("var_data", ctypes.c_void_p),
    ]


# ------------------------------------------------------------------
# Unions

