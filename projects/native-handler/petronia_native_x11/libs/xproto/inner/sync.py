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

AlarmstateType = NewType('AlarmstateType', int)


class AlarmstateValues:
    ACTIVE = AlarmstateType(0)
    INACTIVE = AlarmstateType(1)
    DESTROYED = AlarmstateType(2)


TesttypeType = NewType('TesttypeType', int)


class TesttypeValues:
    POSITIVE_TRANSITION = TesttypeType(0)
    NEGATIVE_TRANSITION = TesttypeType(1)
    POSITIVE_COMPARISON = TesttypeType(2)
    NEGATIVE_COMPARISON = TesttypeType(3)


ValuetypeType = NewType('ValuetypeType', int)


class ValuetypeValues:
    ABSOLUTE = ValuetypeType(0)
    RELATIVE = ValuetypeType(1)


CaType = NewType('CaType', int)


class CaValues:
    COUNTER = CaType(1)
    VALUE_TYPE = CaType(2)
    VALUE = CaType(4)
    TEST_TYPE = CaType(8)
    DELTA = CaType(16)
    EVENTS = CaType(32)


# ------------------------------------------------------------------
# Aliases

Counter = NewType('Counter', ctypes.c_uint32)
Alarm = NewType('Alarm', ctypes.c_uint32)
Fence = NewType('Fence', ctypes.c_uint32)


# ------------------------------------------------------------------
# Structures, Events, Requests, Replies


Int64StructPacket = DataPacket((
    ('hi', FixedDataPacketField(MARKER_INT32)),
    ('lo', FixedDataPacketField(MARKER_UINT32)),
))


class Int64Struct:
    __slots__ = ('hi', 'lo',)

    def __init__(
            self, *,
            hi: Optional[int] = None,
            lo: Optional[int] = None,
    ) -> None:
        self.hi = hi
        self.lo = lo

    def as_dict(self) -> Dict[str, Any]:
        return {
            'hi': self.hi,
            'lo': self.lo,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'Int64Struct':
        return Int64Struct(**Int64StructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return Int64StructPacket.pack(**self.as_dict())


class Int64StructCType(ctypes.Structure):
    """sync INT64"""
    _fields_ = [
        ("hi", ctypes.c_int32),
        ("lo", ctypes.c_uint32),
    ]


SystemcounterStructPacket = DataPacket((
    ('counter', FixedDataPacketField(MARKER_UINT32)),
    ('resolution', FixedDataPacketField(MARKER_UINT32)),
    ('name_len', FixedDataPacketField(MARKER_UINT16)),
    ('name', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['name_len'], 0)),
    ('pad0', AlignedPadDataPacketField(4)),
))


class SystemcounterStruct:
    __slots__ = ('counter', 'resolution', 'name_len', 'name',)

    def __init__(
            self, *,
            counter: Optional[int] = None,
            resolution: Optional[int] = None,
            name_len: Optional[int] = None,
            name: Optional[Sequence[int]] = None,
    ) -> None:
        self.counter = counter
        self.resolution = resolution
        self.name_len = name_len
        self.name = name

    def as_dict(self) -> Dict[str, Any]:
        return {
            'counter': self.counter,
            'resolution': self.resolution,
            'name_len': self.name_len,
            'name': self.name,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SystemcounterStruct':
        return SystemcounterStruct(**SystemcounterStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SystemcounterStructPacket.pack(**self.as_dict())


class SystemcounterStructCType(ctypes.Structure):
    """sync SYSTEMCOUNTER"""
    _fields_ = [
        ("counter", ctypes.c_uint32),
        ("resolution", ctypes.c_uint32),
        ("name_len", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


TriggerStructPacket = DataPacket((
    ('counter', FixedDataPacketField(MARKER_UINT32)),
    ('wait_type', FixedDataPacketField(MARKER_UINT32)),
    ('wait_value', FixedDataPacketField(MARKER_UINT32)),
    ('test_type', FixedDataPacketField(MARKER_UINT32)),
))


class TriggerStruct:
    __slots__ = ('counter', 'wait_type', 'wait_value', 'test_type',)

    def __init__(
            self, *,
            counter: Optional[int] = None,
            wait_type: Optional[int] = None,
            wait_value: Optional[int] = None,
            test_type: Optional[int] = None,
    ) -> None:
        self.counter = counter
        self.wait_type = wait_type
        self.wait_value = wait_value
        self.test_type = test_type

    def as_dict(self) -> Dict[str, Any]:
        return {
            'counter': self.counter,
            'wait_type': self.wait_type,
            'wait_value': self.wait_value,
            'test_type': self.test_type,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'TriggerStruct':
        return TriggerStruct(**TriggerStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return TriggerStructPacket.pack(**self.as_dict())


class TriggerStructCType(ctypes.Structure):
    """sync TRIGGER"""
    _fields_ = [
        ("counter", ctypes.c_uint32),
        ("wait_type", ctypes.c_uint32),
        ("wait_value", ctypes.c_uint32),
        ("test_type", ctypes.c_uint32),
    ]


WaitconditionStructPacket = DataPacket((
    ('trigger', FixedDataPacketField(MARKER_UINT32)),
    ('event_threshold', FixedDataPacketField(MARKER_UINT32)),
))


class WaitconditionStruct:
    __slots__ = ('trigger', 'event_threshold',)

    def __init__(
            self, *,
            trigger: Optional[int] = None,
            event_threshold: Optional[int] = None,
    ) -> None:
        self.trigger = trigger
        self.event_threshold = event_threshold

    def as_dict(self) -> Dict[str, Any]:
        return {
            'trigger': self.trigger,
            'event_threshold': self.event_threshold,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'WaitconditionStruct':
        return WaitconditionStruct(**WaitconditionStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return WaitconditionStructPacket.pack(**self.as_dict())


class WaitconditionStructCType(ctypes.Structure):
    """sync WAITCONDITION"""
    _fields_ = [
        ("trigger", ctypes.c_uint32),
        ("event_threshold", ctypes.c_uint32),
    ]


InitializeRequestCookie = NewType('InitializeRequestCookie', ctypes.c_uint32)


InitializeRequestPacket = DataPacket((
    ('desired_major_version', FixedDataPacketField(MARKER_UINT8)),
    ('desired_minor_version', FixedDataPacketField(MARKER_UINT8)),
))


class InitializeRequest:
    OPCODE = 0

    __slots__ = ('desired_major_version', 'desired_minor_version',)

    def __init__(
            self, *,
            desired_major_version: Optional[int] = None,
            desired_minor_version: Optional[int] = None,
    ) -> None:
        self.desired_major_version = desired_major_version
        self.desired_minor_version = desired_minor_version

    def as_dict(self) -> Dict[str, Any]:
        return {
            'desired_major_version': self.desired_major_version,
            'desired_minor_version': self.desired_minor_version,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'InitializeRequest':
        return InitializeRequest(**InitializeRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return InitializeRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], InitializeRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        InitializeRequest.lib = library.sync_initialize
        InitializeRequest.lib.restype = InitializeRequestCookie
        InitializeRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint8)


class InitializeRequestCType(ctypes.Structure):
    """sync Initialize"""
    _fields_ = [
        ("desired_major_version", ctypes.c_uint8),
        ("desired_minor_version", ctypes.c_uint8),
    ]


InitializeReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('major_version', FixedDataPacketField(MARKER_UINT8)),
    ('minor_version', FixedDataPacketField(MARKER_UINT8)),
    ('pad1', FixedPadDataPacketField(22)),
))


class InitializeReplyReply:
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
    def from_data(inp: BinaryIO) -> 'InitializeReplyReply':
        return InitializeReplyReply(**InitializeReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return InitializeReplyReplyPacket.pack(**self.as_dict())


class InitializeReplyReplyCType(ctypes.Structure):
    """sync Initialize_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("major_version", ctypes.c_uint8),
        ("minor_version", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 22),
    ]


ListSystemCountersRequestCookie = NewType('ListSystemCountersRequestCookie', ctypes.c_uint32)


ListSystemCountersRequestPacket = DataPacket((
))


class ListSystemCountersRequest:
    OPCODE = 1

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ListSystemCountersRequest':
        return ListSystemCountersRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], ListSystemCountersRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ListSystemCountersRequest.lib = library.sync_listsystemcounters
        ListSystemCountersRequest.lib.restype = ListSystemCountersRequestCookie
        ListSystemCountersRequest.lib.argstype = ()


class ListSystemCountersRequestCType(ctypes.Structure):
    """sync ListSystemCounters"""
    _fields_ = [
    ]


ListSystemCountersReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('counters_len', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('counters', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['counters_len'], 0)),
))


class ListSystemCountersReplyReply:
    __slots__ = ('counters_len', 'counters',)

    def __init__(
            self, *,
            counters_len: Optional[int] = None,
            counters: Optional[Sequence[int]] = None,
    ) -> None:
        self.counters_len = counters_len
        self.counters = counters

    def as_dict(self) -> Dict[str, Any]:
        return {
            'counters_len': self.counters_len,
            'counters': self.counters,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ListSystemCountersReplyReply':
        return ListSystemCountersReplyReply(**ListSystemCountersReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ListSystemCountersReplyReplyPacket.pack(**self.as_dict())


class ListSystemCountersReplyReplyCType(ctypes.Structure):
    """sync ListSystemCounters_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("counters_len", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


CreateCounterRequestPacket = DataPacket((
    ('id', FixedDataPacketField(MARKER_UINT32)),
    ('initial_value', FixedDataPacketField(MARKER_UINT32)),
))


class CreateCounterRequest:
    OPCODE = 2

    __slots__ = ('id', 'initial_value',)

    def __init__(
            self, *,
            id: Optional[int] = None,
            initial_value: Optional[int] = None,
    ) -> None:
        self.id = id
        self.initial_value = initial_value

    def as_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'initial_value': self.initial_value,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateCounterRequest':
        return CreateCounterRequest(**CreateCounterRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateCounterRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateCounterRequest.lib = library.sync_createcounter
        CreateCounterRequest.lib.restype = ctypes.c_uint32
        CreateCounterRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class CreateCounterRequestCType(ctypes.Structure):
    """sync CreateCounter"""
    _fields_ = [
        ("id", ctypes.c_uint32),
        ("initial_value", ctypes.c_uint32),
    ]


DestroyCounterRequestPacket = DataPacket((
    ('counter', FixedDataPacketField(MARKER_UINT32)),
))


class DestroyCounterRequest:
    OPCODE = 6

    __slots__ = ('counter',)

    def __init__(
            self, *,
            counter: Optional[int] = None,
    ) -> None:
        self.counter = counter

    def as_dict(self) -> Dict[str, Any]:
        return {
            'counter': self.counter,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DestroyCounterRequest':
        return DestroyCounterRequest(**DestroyCounterRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DestroyCounterRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        DestroyCounterRequest.lib = library.sync_destroycounter
        DestroyCounterRequest.lib.restype = ctypes.c_uint32
        DestroyCounterRequest.lib.argstype = (ctypes.c_uint32,)


class DestroyCounterRequestCType(ctypes.Structure):
    """sync DestroyCounter"""
    _fields_ = [
        ("counter", ctypes.c_uint32),
    ]


QueryCounterRequestCookie = NewType('QueryCounterRequestCookie', ctypes.c_uint32)


QueryCounterRequestPacket = DataPacket((
    ('counter', FixedDataPacketField(MARKER_UINT32)),
))


class QueryCounterRequest:
    OPCODE = 5

    __slots__ = ('counter',)

    def __init__(
            self, *,
            counter: Optional[int] = None,
    ) -> None:
        self.counter = counter

    def as_dict(self) -> Dict[str, Any]:
        return {
            'counter': self.counter,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryCounterRequest':
        return QueryCounterRequest(**QueryCounterRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryCounterRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], QueryCounterRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryCounterRequest.lib = library.sync_querycounter
        QueryCounterRequest.lib.restype = QueryCounterRequestCookie
        QueryCounterRequest.lib.argstype = (ctypes.c_uint32,)


class QueryCounterRequestCType(ctypes.Structure):
    """sync QueryCounter"""
    _fields_ = [
        ("counter", ctypes.c_uint32),
    ]


QueryCounterReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('counter_value', FixedDataPacketField(MARKER_UINT32)),
))


class QueryCounterReplyReply:
    __slots__ = ('counter_value',)

    def __init__(
            self, *,
            counter_value: Optional[int] = None,
    ) -> None:
        self.counter_value = counter_value

    def as_dict(self) -> Dict[str, Any]:
        return {
            'counter_value': self.counter_value,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryCounterReplyReply':
        return QueryCounterReplyReply(**QueryCounterReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryCounterReplyReplyPacket.pack(**self.as_dict())


class QueryCounterReplyReplyCType(ctypes.Structure):
    """sync QueryCounter_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("counter_value", ctypes.c_uint32),
    ]


AwaitRequestPacket = DataPacket((
    ('wait_list', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 1, 0)),
))


class AwaitRequest:
    OPCODE = 7

    __slots__ = ('wait_list',)

    def __init__(
            self, *,
            wait_list: Optional[Sequence[int]] = None,
    ) -> None:
        self.wait_list = wait_list

    def as_dict(self) -> Dict[str, Any]:
        return {
            'wait_list': self.wait_list,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'AwaitRequest':
        return AwaitRequest(**AwaitRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return AwaitRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        AwaitRequest.lib = library.sync_await
        AwaitRequest.lib.restype = ctypes.c_uint32
        AwaitRequest.lib.argstype = (ctypes.c_void_p,)


class AwaitRequestCType(ctypes.Structure):
    """sync Await"""
    _fields_ = [
        ("var_data", ctypes.c_void_p),
    ]


ChangeCounterRequestPacket = DataPacket((
    ('counter', FixedDataPacketField(MARKER_UINT32)),
    ('amount', FixedDataPacketField(MARKER_UINT32)),
))


class ChangeCounterRequest:
    OPCODE = 4

    __slots__ = ('counter', 'amount',)

    def __init__(
            self, *,
            counter: Optional[int] = None,
            amount: Optional[int] = None,
    ) -> None:
        self.counter = counter
        self.amount = amount

    def as_dict(self) -> Dict[str, Any]:
        return {
            'counter': self.counter,
            'amount': self.amount,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ChangeCounterRequest':
        return ChangeCounterRequest(**ChangeCounterRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ChangeCounterRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ChangeCounterRequest.lib = library.sync_changecounter
        ChangeCounterRequest.lib.restype = ctypes.c_uint32
        ChangeCounterRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class ChangeCounterRequestCType(ctypes.Structure):
    """sync ChangeCounter"""
    _fields_ = [
        ("counter", ctypes.c_uint32),
        ("amount", ctypes.c_uint32),
    ]


SetCounterRequestPacket = DataPacket((
    ('counter', FixedDataPacketField(MARKER_UINT32)),
    ('value', FixedDataPacketField(MARKER_UINT32)),
))


class SetCounterRequest:
    OPCODE = 3

    __slots__ = ('counter', 'value',)

    def __init__(
            self, *,
            counter: Optional[int] = None,
            value: Optional[int] = None,
    ) -> None:
        self.counter = counter
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {
            'counter': self.counter,
            'value': self.value,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetCounterRequest':
        return SetCounterRequest(**SetCounterRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetCounterRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetCounterRequest.lib = library.sync_setcounter
        SetCounterRequest.lib.restype = ctypes.c_uint32
        SetCounterRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class SetCounterRequestCType(ctypes.Structure):
    """sync SetCounter"""
    _fields_ = [
        ("counter", ctypes.c_uint32),
        ("value", ctypes.c_uint32),
    ]


CreateAlarmRequestPacket = DataPacket((
    ('id', FixedDataPacketField(MARKER_UINT32)),
    ('value_mask', FixedDataPacketField(MARKER_UINT32)),
    ('value_list', BitDataPacketField(lambda d, c: d['value_mask'], {
        CaValues.COUNTER: FixedDataPacketField(MARKER_UINT32),
        CaValues.VALUE_TYPE: FixedDataPacketField(MARKER_UINT32),
        CaValues.VALUE: FixedDataPacketField(MARKER_UINT32),
        CaValues.TEST_TYPE: FixedDataPacketField(MARKER_UINT32),
        CaValues.DELTA: FixedDataPacketField(MARKER_UINT32),
        CaValues.EVENTS: FixedDataPacketField(MARKER_UINT32),
    }, 0)),
))


class CreateAlarmRequest:
    OPCODE = 8

    __slots__ = ('id', 'value_mask', 'value_list',)

    def __init__(
            self, *,
            id: Optional[int] = None,
            value_mask: Optional[int] = None,
            value_list: Optional[Mapping[str, CaValues]] = None,
    ) -> None:
        self.id = id
        self.value_mask = value_mask
        self.value_list = value_list

    def as_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'value_mask': self.value_mask,
            'value_list': self.value_list,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateAlarmRequest':
        return CreateAlarmRequest(**CreateAlarmRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateAlarmRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Mapping[str, CaValues]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateAlarmRequest.lib = library.sync_createalarm
        CreateAlarmRequest.lib.restype = ctypes.c_uint32
        CreateAlarmRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)


class CreateAlarmRequestCType(ctypes.Structure):
    """sync CreateAlarm"""
    _fields_ = [
        ("id", ctypes.c_uint32),
        ("value_mask", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


ChangeAlarmRequestPacket = DataPacket((
    ('id', FixedDataPacketField(MARKER_UINT32)),
    ('value_mask', FixedDataPacketField(MARKER_UINT32)),
    ('value_list', BitDataPacketField(lambda d, c: d['value_mask'], {
        CaValues.COUNTER: FixedDataPacketField(MARKER_UINT32),
        CaValues.VALUE_TYPE: FixedDataPacketField(MARKER_UINT32),
        CaValues.VALUE: FixedDataPacketField(MARKER_UINT32),
        CaValues.TEST_TYPE: FixedDataPacketField(MARKER_UINT32),
        CaValues.DELTA: FixedDataPacketField(MARKER_UINT32),
        CaValues.EVENTS: FixedDataPacketField(MARKER_UINT32),
    }, 0)),
))


class ChangeAlarmRequest:
    OPCODE = 9

    __slots__ = ('id', 'value_mask', 'value_list',)

    def __init__(
            self, *,
            id: Optional[int] = None,
            value_mask: Optional[int] = None,
            value_list: Optional[Mapping[str, CaValues]] = None,
    ) -> None:
        self.id = id
        self.value_mask = value_mask
        self.value_list = value_list

    def as_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'value_mask': self.value_mask,
            'value_list': self.value_list,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ChangeAlarmRequest':
        return ChangeAlarmRequest(**ChangeAlarmRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ChangeAlarmRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Mapping[str, CaValues]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ChangeAlarmRequest.lib = library.sync_changealarm
        ChangeAlarmRequest.lib.restype = ctypes.c_uint32
        ChangeAlarmRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)


class ChangeAlarmRequestCType(ctypes.Structure):
    """sync ChangeAlarm"""
    _fields_ = [
        ("id", ctypes.c_uint32),
        ("value_mask", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


DestroyAlarmRequestPacket = DataPacket((
    ('alarm', FixedDataPacketField(MARKER_UINT32)),
))


class DestroyAlarmRequest:
    OPCODE = 11

    __slots__ = ('alarm',)

    def __init__(
            self, *,
            alarm: Optional[int] = None,
    ) -> None:
        self.alarm = alarm

    def as_dict(self) -> Dict[str, Any]:
        return {
            'alarm': self.alarm,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DestroyAlarmRequest':
        return DestroyAlarmRequest(**DestroyAlarmRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DestroyAlarmRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        DestroyAlarmRequest.lib = library.sync_destroyalarm
        DestroyAlarmRequest.lib.restype = ctypes.c_uint32
        DestroyAlarmRequest.lib.argstype = (ctypes.c_uint32,)


class DestroyAlarmRequestCType(ctypes.Structure):
    """sync DestroyAlarm"""
    _fields_ = [
        ("alarm", ctypes.c_uint32),
    ]


QueryAlarmRequestCookie = NewType('QueryAlarmRequestCookie', ctypes.c_uint32)


QueryAlarmRequestPacket = DataPacket((
    ('alarm', FixedDataPacketField(MARKER_UINT32)),
))


class QueryAlarmRequest:
    OPCODE = 10

    __slots__ = ('alarm',)

    def __init__(
            self, *,
            alarm: Optional[int] = None,
    ) -> None:
        self.alarm = alarm

    def as_dict(self) -> Dict[str, Any]:
        return {
            'alarm': self.alarm,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryAlarmRequest':
        return QueryAlarmRequest(**QueryAlarmRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryAlarmRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], QueryAlarmRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryAlarmRequest.lib = library.sync_queryalarm
        QueryAlarmRequest.lib.restype = QueryAlarmRequestCookie
        QueryAlarmRequest.lib.argstype = (ctypes.c_uint32,)


class QueryAlarmRequestCType(ctypes.Structure):
    """sync QueryAlarm"""
    _fields_ = [
        ("alarm", ctypes.c_uint32),
    ]


QueryAlarmReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('trigger', FixedDataPacketField(MARKER_UINT32)),
    ('delta', FixedDataPacketField(MARKER_UINT32)),
    ('events', FixedDataPacketField(MARKER_UINT8)),
    ('state', FixedDataPacketField(MARKER_UINT8)),
    ('pad1', FixedPadDataPacketField(2)),
))


class QueryAlarmReplyReply:
    __slots__ = ('trigger', 'delta', 'events', 'state',)

    def __init__(
            self, *,
            trigger: Optional[int] = None,
            delta: Optional[int] = None,
            events: Optional[bool] = None,
            state: Optional[int] = None,
    ) -> None:
        self.trigger = trigger
        self.delta = delta
        self.events = events
        self.state = state

    def as_dict(self) -> Dict[str, Any]:
        return {
            'trigger': self.trigger,
            'delta': self.delta,
            'events': self.events,
            'state': self.state,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryAlarmReplyReply':
        return QueryAlarmReplyReply(**QueryAlarmReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryAlarmReplyReplyPacket.pack(**self.as_dict())


class QueryAlarmReplyReplyCType(ctypes.Structure):
    """sync QueryAlarm_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("trigger", ctypes.c_uint32),
        ("delta", ctypes.c_uint32),
        ("events", ctypes.c_int8),
        ("state", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 2),
    ]


SetPriorityRequestPacket = DataPacket((
    ('id', FixedDataPacketField(MARKER_UINT32)),
    ('priority', FixedDataPacketField(MARKER_INT32)),
))


class SetPriorityRequest:
    OPCODE = 12

    __slots__ = ('id', 'priority',)

    def __init__(
            self, *,
            id: Optional[int] = None,
            priority: Optional[int] = None,
    ) -> None:
        self.id = id
        self.priority = priority

    def as_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'priority': self.priority,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetPriorityRequest':
        return SetPriorityRequest(**SetPriorityRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetPriorityRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetPriorityRequest.lib = library.sync_setpriority
        SetPriorityRequest.lib.restype = ctypes.c_uint32
        SetPriorityRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_int32)


class SetPriorityRequestCType(ctypes.Structure):
    """sync SetPriority"""
    _fields_ = [
        ("id", ctypes.c_uint32),
        ("priority", ctypes.c_int32),
    ]


GetPriorityRequestCookie = NewType('GetPriorityRequestCookie', ctypes.c_uint32)


GetPriorityRequestPacket = DataPacket((
    ('id', FixedDataPacketField(MARKER_UINT32)),
))


class GetPriorityRequest:
    OPCODE = 13

    __slots__ = ('id',)

    def __init__(
            self, *,
            id: Optional[int] = None,
    ) -> None:
        self.id = id

    def as_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetPriorityRequest':
        return GetPriorityRequest(**GetPriorityRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetPriorityRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetPriorityRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetPriorityRequest.lib = library.sync_getpriority
        GetPriorityRequest.lib.restype = GetPriorityRequestCookie
        GetPriorityRequest.lib.argstype = (ctypes.c_uint32,)


class GetPriorityRequestCType(ctypes.Structure):
    """sync GetPriority"""
    _fields_ = [
        ("id", ctypes.c_uint32),
    ]


GetPriorityReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('priority', FixedDataPacketField(MARKER_INT32)),
))


class GetPriorityReplyReply:
    __slots__ = ('priority',)

    def __init__(
            self, *,
            priority: Optional[int] = None,
    ) -> None:
        self.priority = priority

    def as_dict(self) -> Dict[str, Any]:
        return {
            'priority': self.priority,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetPriorityReplyReply':
        return GetPriorityReplyReply(**GetPriorityReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetPriorityReplyReplyPacket.pack(**self.as_dict())


class GetPriorityReplyReplyCType(ctypes.Structure):
    """sync GetPriority_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("priority", ctypes.c_int32),
    ]


CreateFenceRequestPacket = DataPacket((
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('fence', FixedDataPacketField(MARKER_UINT32)),
    ('initially_triggered', FixedDataPacketField(MARKER_UINT8)),
))


class CreateFenceRequest:
    OPCODE = 14

    __slots__ = ('drawable', 'fence', 'initially_triggered',)

    def __init__(
            self, *,
            drawable: Optional[int] = None,
            fence: Optional[int] = None,
            initially_triggered: Optional[bool] = None,
    ) -> None:
        self.drawable = drawable
        self.fence = fence
        self.initially_triggered = initially_triggered

    def as_dict(self) -> Dict[str, Any]:
        return {
            'drawable': self.drawable,
            'fence': self.fence,
            'initially_triggered': self.initially_triggered,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateFenceRequest':
        return CreateFenceRequest(**CreateFenceRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateFenceRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, bool], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateFenceRequest.lib = library.sync_createfence
        CreateFenceRequest.lib.restype = ctypes.c_uint32
        CreateFenceRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int8)


class CreateFenceRequestCType(ctypes.Structure):
    """sync CreateFence"""
    _fields_ = [
        ("drawable", ctypes.c_uint32),
        ("fence", ctypes.c_uint32),
        ("initially_triggered", ctypes.c_int8),
    ]


TriggerFenceRequestPacket = DataPacket((
    ('fence', FixedDataPacketField(MARKER_UINT32)),
))


class TriggerFenceRequest:
    OPCODE = 15

    __slots__ = ('fence',)

    def __init__(
            self, *,
            fence: Optional[int] = None,
    ) -> None:
        self.fence = fence

    def as_dict(self) -> Dict[str, Any]:
        return {
            'fence': self.fence,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'TriggerFenceRequest':
        return TriggerFenceRequest(**TriggerFenceRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return TriggerFenceRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        TriggerFenceRequest.lib = library.sync_triggerfence
        TriggerFenceRequest.lib.restype = ctypes.c_uint32
        TriggerFenceRequest.lib.argstype = (ctypes.c_uint32,)


class TriggerFenceRequestCType(ctypes.Structure):
    """sync TriggerFence"""
    _fields_ = [
        ("fence", ctypes.c_uint32),
    ]


ResetFenceRequestPacket = DataPacket((
    ('fence', FixedDataPacketField(MARKER_UINT32)),
))


class ResetFenceRequest:
    OPCODE = 16

    __slots__ = ('fence',)

    def __init__(
            self, *,
            fence: Optional[int] = None,
    ) -> None:
        self.fence = fence

    def as_dict(self) -> Dict[str, Any]:
        return {
            'fence': self.fence,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ResetFenceRequest':
        return ResetFenceRequest(**ResetFenceRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ResetFenceRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ResetFenceRequest.lib = library.sync_resetfence
        ResetFenceRequest.lib.restype = ctypes.c_uint32
        ResetFenceRequest.lib.argstype = (ctypes.c_uint32,)


class ResetFenceRequestCType(ctypes.Structure):
    """sync ResetFence"""
    _fields_ = [
        ("fence", ctypes.c_uint32),
    ]


DestroyFenceRequestPacket = DataPacket((
    ('fence', FixedDataPacketField(MARKER_UINT32)),
))


class DestroyFenceRequest:
    OPCODE = 17

    __slots__ = ('fence',)

    def __init__(
            self, *,
            fence: Optional[int] = None,
    ) -> None:
        self.fence = fence

    def as_dict(self) -> Dict[str, Any]:
        return {
            'fence': self.fence,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DestroyFenceRequest':
        return DestroyFenceRequest(**DestroyFenceRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DestroyFenceRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        DestroyFenceRequest.lib = library.sync_destroyfence
        DestroyFenceRequest.lib.restype = ctypes.c_uint32
        DestroyFenceRequest.lib.argstype = (ctypes.c_uint32,)


class DestroyFenceRequestCType(ctypes.Structure):
    """sync DestroyFence"""
    _fields_ = [
        ("fence", ctypes.c_uint32),
    ]


QueryFenceRequestCookie = NewType('QueryFenceRequestCookie', ctypes.c_uint32)


QueryFenceRequestPacket = DataPacket((
    ('fence', FixedDataPacketField(MARKER_UINT32)),
))


class QueryFenceRequest:
    OPCODE = 18

    __slots__ = ('fence',)

    def __init__(
            self, *,
            fence: Optional[int] = None,
    ) -> None:
        self.fence = fence

    def as_dict(self) -> Dict[str, Any]:
        return {
            'fence': self.fence,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryFenceRequest':
        return QueryFenceRequest(**QueryFenceRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryFenceRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], QueryFenceRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryFenceRequest.lib = library.sync_queryfence
        QueryFenceRequest.lib.restype = QueryFenceRequestCookie
        QueryFenceRequest.lib.argstype = (ctypes.c_uint32,)


class QueryFenceRequestCType(ctypes.Structure):
    """sync QueryFence"""
    _fields_ = [
        ("fence", ctypes.c_uint32),
    ]


QueryFenceReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('triggered', FixedDataPacketField(MARKER_UINT8)),
    ('pad1', FixedPadDataPacketField(23)),
))


class QueryFenceReplyReply:
    __slots__ = ('triggered',)

    def __init__(
            self, *,
            triggered: Optional[bool] = None,
    ) -> None:
        self.triggered = triggered

    def as_dict(self) -> Dict[str, Any]:
        return {
            'triggered': self.triggered,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryFenceReplyReply':
        return QueryFenceReplyReply(**QueryFenceReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryFenceReplyReplyPacket.pack(**self.as_dict())


class QueryFenceReplyReplyCType(ctypes.Structure):
    """sync QueryFence_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("triggered", ctypes.c_int8),
        ("pad1", ctypes.c_uint8 * 23),
    ]


AwaitFenceRequestPacket = DataPacket((
    ('fence_list', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 1, 0)),
))


class AwaitFenceRequest:
    OPCODE = 19

    __slots__ = ('fence_list',)

    def __init__(
            self, *,
            fence_list: Optional[Sequence[int]] = None,
    ) -> None:
        self.fence_list = fence_list

    def as_dict(self) -> Dict[str, Any]:
        return {
            'fence_list': self.fence_list,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'AwaitFenceRequest':
        return AwaitFenceRequest(**AwaitFenceRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return AwaitFenceRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        AwaitFenceRequest.lib = library.sync_awaitfence
        AwaitFenceRequest.lib.restype = ctypes.c_uint32
        AwaitFenceRequest.lib.argstype = (ctypes.c_void_p,)


class AwaitFenceRequestCType(ctypes.Structure):
    """sync AwaitFence"""
    _fields_ = [
        ("var_data", ctypes.c_void_p),
    ]


CounterNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('kind', FixedDataPacketField(MARKER_UINT8)),
    ('counter', FixedDataPacketField(MARKER_UINT32)),
    ('wait_value', FixedDataPacketField(MARKER_UINT32)),
    ('counter_value', FixedDataPacketField(MARKER_UINT32)),
    ('timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('count', FixedDataPacketField(MARKER_UINT16)),
    ('destroyed', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
))


class CounterNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'kind', 'counter', 'wait_value', 'counter_value', 'timestamp', 'count', 'destroyed',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            kind: Optional[int] = None,
            counter: Optional[int] = None,
            wait_value: Optional[int] = None,
            counter_value: Optional[int] = None,
            timestamp: Optional[int] = None,
            count: Optional[int] = None,
            destroyed: Optional[bool] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.kind = kind
        self.counter = counter
        self.wait_value = wait_value
        self.counter_value = counter_value
        self.timestamp = timestamp
        self.count = count
        self.destroyed = destroyed

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'kind': self.kind,
            'counter': self.counter,
            'wait_value': self.wait_value,
            'counter_value': self.counter_value,
            'timestamp': self.timestamp,
            'count': self.count,
            'destroyed': self.destroyed,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CounterNotifyEvent':
        return CounterNotifyEvent(**CounterNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CounterNotifyEventPacket.pack(**self.as_dict())


class CounterNotifyEventCType(ctypes.Structure):
    """sync CounterNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("kind", ctypes.c_uint8),
        ("counter", ctypes.c_uint32),
        ("wait_value", ctypes.c_uint32),
        ("counter_value", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint32),
        ("count", ctypes.c_uint16),
        ("destroyed", ctypes.c_int8),
        ("pad0", ctypes.c_uint8),
    ]


AlarmNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('kind', FixedDataPacketField(MARKER_UINT8)),
    ('alarm', FixedDataPacketField(MARKER_UINT32)),
    ('counter_value', FixedDataPacketField(MARKER_UINT32)),
    ('alarm_value', FixedDataPacketField(MARKER_UINT32)),
    ('timestamp', FixedDataPacketField(MARKER_UINT32)),
    ('state', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class AlarmNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'kind', 'alarm', 'counter_value', 'alarm_value', 'timestamp', 'state',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            kind: Optional[int] = None,
            alarm: Optional[int] = None,
            counter_value: Optional[int] = None,
            alarm_value: Optional[int] = None,
            timestamp: Optional[int] = None,
            state: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.kind = kind
        self.alarm = alarm
        self.counter_value = counter_value
        self.alarm_value = alarm_value
        self.timestamp = timestamp
        self.state = state

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'kind': self.kind,
            'alarm': self.alarm,
            'counter_value': self.counter_value,
            'alarm_value': self.alarm_value,
            'timestamp': self.timestamp,
            'state': self.state,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'AlarmNotifyEvent':
        return AlarmNotifyEvent(**AlarmNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return AlarmNotifyEventPacket.pack(**self.as_dict())


class AlarmNotifyEventCType(ctypes.Structure):
    """sync AlarmNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("kind", ctypes.c_uint8),
        ("alarm", ctypes.c_uint32),
        ("counter_value", ctypes.c_uint32),
        ("alarm_value", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint32),
        ("state", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


# ------------------------------------------------------------------
# Unions

