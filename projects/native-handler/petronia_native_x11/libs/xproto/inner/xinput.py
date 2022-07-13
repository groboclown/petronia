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

DeviceUseType = NewType('DeviceUseType', int)


class DeviceUseValues:
    IS_XPOINTER = DeviceUseType(0)
    IS_XKEYBOARD = DeviceUseType(1)
    IS_XEXTENSION_DEVICE = DeviceUseType(2)
    IS_XEXTENSION_KEYBOARD = DeviceUseType(3)
    IS_XEXTENSION_POINTER = DeviceUseType(4)


InputClassType = NewType('InputClassType', int)


class InputClassValues:
    KEY = InputClassType(0)
    BUTTON = InputClassType(1)
    VALUATOR = InputClassType(2)
    FEEDBACK = InputClassType(3)
    PROXIMITY = InputClassType(4)
    FOCUS = InputClassType(5)
    OTHER = InputClassType(6)


ValuatorModeType = NewType('ValuatorModeType', int)


class ValuatorModeValues:
    RELATIVE = ValuatorModeType(0)
    ABSOLUTE = ValuatorModeType(1)


PropagateModeType = NewType('PropagateModeType', int)


class PropagateModeValues:
    ADD_TO_LIST = PropagateModeType(0)
    DELETE_FROM_LIST = PropagateModeType(1)


ModifierDeviceType = NewType('ModifierDeviceType', int)


class ModifierDeviceValues:
    USE_XKEYBOARD = ModifierDeviceType(255)


DeviceInputModeType = NewType('DeviceInputModeType', int)


class DeviceInputModeValues:
    ASYNC_THIS_DEVICE = DeviceInputModeType(0)
    SYNC_THIS_DEVICE = DeviceInputModeType(1)
    REPLAY_THIS_DEVICE = DeviceInputModeType(2)
    ASYNC_OTHER_DEVICES = DeviceInputModeType(3)
    ASYNC_ALL = DeviceInputModeType(4)
    SYNC_ALL = DeviceInputModeType(5)


FeedbackClassType = NewType('FeedbackClassType', int)


class FeedbackClassValues:
    KEYBOARD = FeedbackClassType(0)
    POINTER = FeedbackClassType(1)
    STRING = FeedbackClassType(2)
    INTEGER = FeedbackClassType(3)
    LED = FeedbackClassType(4)
    BELL = FeedbackClassType(5)


ChangeFeedbackControlMaskType = NewType('ChangeFeedbackControlMaskType', int)


class ChangeFeedbackControlMaskValues:
    KEY_CLICK_PERCENT = ChangeFeedbackControlMaskType(1)
    PERCENT = ChangeFeedbackControlMaskType(2)
    PITCH = ChangeFeedbackControlMaskType(4)
    DURATION = ChangeFeedbackControlMaskType(8)
    LED = ChangeFeedbackControlMaskType(16)
    LED_MODE = ChangeFeedbackControlMaskType(32)
    KEY = ChangeFeedbackControlMaskType(64)
    AUTO_REPEAT_MODE = ChangeFeedbackControlMaskType(128)
    STRING = ChangeFeedbackControlMaskType(1)
    INTEGER = ChangeFeedbackControlMaskType(1)
    ACCEL_NUM = ChangeFeedbackControlMaskType(1)
    ACCEL_DENOM = ChangeFeedbackControlMaskType(2)
    THRESHOLD = ChangeFeedbackControlMaskType(4)


ValuatorStateModeMaskType = NewType('ValuatorStateModeMaskType', int)


class ValuatorStateModeMaskValues:
    DEVICE_MODE_ABSOLUTE = ValuatorStateModeMaskType(1)
    OUT_OF_PROXIMITY = ValuatorStateModeMaskType(2)


DeviceControlType = NewType('DeviceControlType', int)


class DeviceControlValues:
    RESOLUTION = DeviceControlType(1)
    ABS_CALIB = DeviceControlType(2)
    CORE = DeviceControlType(3)
    ENABLE = DeviceControlType(4)
    ABS_AREA = DeviceControlType(5)


PropertyFormatType = NewType('PropertyFormatType', int)


class PropertyFormatValues:
    V_8BITS = PropertyFormatType(8)
    V_16BITS = PropertyFormatType(16)
    V_32BITS = PropertyFormatType(32)


DeviceType = NewType('DeviceType', int)


class DeviceValues:
    ALL = DeviceType(0)
    ALL_MASTER = DeviceType(1)


HierarchyChangeTypeType = NewType('HierarchyChangeTypeType', int)


class HierarchyChangeTypeValues:
    ADD_MASTER = HierarchyChangeTypeType(1)
    REMOVE_MASTER = HierarchyChangeTypeType(2)
    ATTACH_SLAVE = HierarchyChangeTypeType(3)
    DETACH_SLAVE = HierarchyChangeTypeType(4)


ChangeModeType = NewType('ChangeModeType', int)


class ChangeModeValues:
    ATTACH = ChangeModeType(1)
    FLOAT = ChangeModeType(2)


XieventMaskType = NewType('XieventMaskType', int)


class XieventMaskValues:
    DEVICE_CHANGED = XieventMaskType(2)
    KEY_PRESS = XieventMaskType(4)
    KEY_RELEASE = XieventMaskType(8)
    BUTTON_PRESS = XieventMaskType(16)
    BUTTON_RELEASE = XieventMaskType(32)
    MOTION = XieventMaskType(64)
    ENTER = XieventMaskType(128)
    LEAVE = XieventMaskType(256)
    FOCUS_IN = XieventMaskType(512)
    FOCUS_OUT = XieventMaskType(1024)
    HIERARCHY = XieventMaskType(2048)
    PROPERTY = XieventMaskType(4096)
    RAW_KEY_PRESS = XieventMaskType(8192)
    RAW_KEY_RELEASE = XieventMaskType(16384)
    RAW_BUTTON_PRESS = XieventMaskType(32768)
    RAW_BUTTON_RELEASE = XieventMaskType(65536)
    RAW_MOTION = XieventMaskType(131072)
    TOUCH_BEGIN = XieventMaskType(262144)
    TOUCH_UPDATE = XieventMaskType(524288)
    TOUCH_END = XieventMaskType(1048576)
    TOUCH_OWNERSHIP = XieventMaskType(2097152)
    RAW_TOUCH_BEGIN = XieventMaskType(4194304)
    RAW_TOUCH_UPDATE = XieventMaskType(8388608)
    RAW_TOUCH_END = XieventMaskType(16777216)
    BARRIER_HIT = XieventMaskType(33554432)
    BARRIER_LEAVE = XieventMaskType(67108864)


DeviceClassTypeType = NewType('DeviceClassTypeType', int)


class DeviceClassTypeValues:
    KEY = DeviceClassTypeType(0)
    BUTTON = DeviceClassTypeType(1)
    VALUATOR = DeviceClassTypeType(2)
    SCROLL = DeviceClassTypeType(3)
    TOUCH = DeviceClassTypeType(8)
    GESTURE = DeviceClassTypeType(9)


DeviceTypeType = NewType('DeviceTypeType', int)


class DeviceTypeValues:
    MASTER_POINTER = DeviceTypeType(1)
    MASTER_KEYBOARD = DeviceTypeType(2)
    SLAVE_POINTER = DeviceTypeType(3)
    SLAVE_KEYBOARD = DeviceTypeType(4)
    FLOATING_SLAVE = DeviceTypeType(5)


ScrollFlagsType = NewType('ScrollFlagsType', int)


class ScrollFlagsValues:
    NO_EMULATION = ScrollFlagsType(1)
    PREFERRED = ScrollFlagsType(2)


ScrollTypeType = NewType('ScrollTypeType', int)


class ScrollTypeValues:
    VERTICAL = ScrollTypeType(1)
    HORIZONTAL = ScrollTypeType(2)


TouchModeType = NewType('TouchModeType', int)


class TouchModeValues:
    DIRECT = TouchModeType(1)
    DEPENDENT = TouchModeType(2)


GrabOwnerType = NewType('GrabOwnerType', int)


class GrabOwnerValues:
    NO_OWNER = GrabOwnerType(0)
    OWNER = GrabOwnerType(1)


EventModeType = NewType('EventModeType', int)


class EventModeValues:
    ASYNC_DEVICE = EventModeType(0)
    SYNC_DEVICE = EventModeType(1)
    REPLAY_DEVICE = EventModeType(2)
    ASYNC_PAIRED_DEVICE = EventModeType(3)
    ASYNC_PAIR = EventModeType(4)
    SYNC_PAIR = EventModeType(5)
    ACCEPT_TOUCH = EventModeType(6)
    REJECT_TOUCH = EventModeType(7)


GrabMode22Type = NewType('GrabMode22Type', int)


class GrabMode22Values:
    SYNC = GrabMode22Type(0)
    ASYNC = GrabMode22Type(1)
    TOUCH = GrabMode22Type(2)


GrabTypeType = NewType('GrabTypeType', int)


class GrabTypeValues:
    BUTTON = GrabTypeType(0)
    KEYCODE = GrabTypeType(1)
    ENTER = GrabTypeType(2)
    FOCUS_IN = GrabTypeType(3)
    TOUCH_BEGIN = GrabTypeType(4)
    GESTURE_PINCH_BEGIN = GrabTypeType(5)
    GESTURE_SWIPE_BEGIN = GrabTypeType(6)


ModifierMaskType = NewType('ModifierMaskType', int)


class ModifierMaskValues:
    ANY = ModifierMaskType(2147483648)


MoreEventsMaskType = NewType('MoreEventsMaskType', int)


class MoreEventsMaskValues:
    MORE_EVENTS = MoreEventsMaskType(128)


ClassesReportedMaskType = NewType('ClassesReportedMaskType', int)


class ClassesReportedMaskValues:
    OUT_OF_PROXIMITY = ClassesReportedMaskType(128)
    DEVICE_MODE_ABSOLUTE = ClassesReportedMaskType(64)
    REPORTING_VALUATORS = ClassesReportedMaskType(4)
    REPORTING_BUTTONS = ClassesReportedMaskType(2)
    REPORTING_KEYS = ClassesReportedMaskType(1)


ChangeDeviceType = NewType('ChangeDeviceType', int)


class ChangeDeviceValues:
    NEW_POINTER = ChangeDeviceType(0)
    NEW_KEYBOARD = ChangeDeviceType(1)


DeviceChangeType = NewType('DeviceChangeType', int)


class DeviceChangeValues:
    ADDED = DeviceChangeType(0)
    REMOVED = DeviceChangeType(1)
    ENABLED = DeviceChangeType(2)
    DISABLED = DeviceChangeType(3)
    UNRECOVERABLE = DeviceChangeType(4)
    CONTROL_CHANGED = DeviceChangeType(5)


ChangeReasonType = NewType('ChangeReasonType', int)


class ChangeReasonValues:
    SLAVE_SWITCH = ChangeReasonType(1)
    DEVICE_CHANGE = ChangeReasonType(2)


KeyEventFlagsType = NewType('KeyEventFlagsType', int)


class KeyEventFlagsValues:
    KEY_REPEAT = KeyEventFlagsType(65536)


PointerEventFlagsType = NewType('PointerEventFlagsType', int)


class PointerEventFlagsValues:
    POINTER_EMULATED = PointerEventFlagsType(65536)


NotifyModeType = NewType('NotifyModeType', int)


class NotifyModeValues:
    NORMAL = NotifyModeType(0)
    GRAB = NotifyModeType(1)
    UNGRAB = NotifyModeType(2)
    WHILE_GRABBED = NotifyModeType(3)
    PASSIVE_GRAB = NotifyModeType(4)
    PASSIVE_UNGRAB = NotifyModeType(5)


NotifyDetailType = NewType('NotifyDetailType', int)


class NotifyDetailValues:
    ANCESTOR = NotifyDetailType(0)
    VIRTUAL = NotifyDetailType(1)
    INFERIOR = NotifyDetailType(2)
    NONLINEAR = NotifyDetailType(3)
    NONLINEAR_VIRTUAL = NotifyDetailType(4)
    POINTER = NotifyDetailType(5)
    POINTER_ROOT = NotifyDetailType(6)
    NONE = NotifyDetailType(7)


HierarchyMaskType = NewType('HierarchyMaskType', int)


class HierarchyMaskValues:
    MASTER_ADDED = HierarchyMaskType(1)
    MASTER_REMOVED = HierarchyMaskType(2)
    SLAVE_ADDED = HierarchyMaskType(4)
    SLAVE_REMOVED = HierarchyMaskType(8)
    SLAVE_ATTACHED = HierarchyMaskType(16)
    SLAVE_DETACHED = HierarchyMaskType(32)
    DEVICE_ENABLED = HierarchyMaskType(64)
    DEVICE_DISABLED = HierarchyMaskType(128)


PropertyFlagType = NewType('PropertyFlagType', int)


class PropertyFlagValues:
    DELETED = PropertyFlagType(0)
    CREATED = PropertyFlagType(1)
    MODIFIED = PropertyFlagType(2)


TouchEventFlagsType = NewType('TouchEventFlagsType', int)


class TouchEventFlagsValues:
    TOUCH_PENDING_END = TouchEventFlagsType(65536)
    TOUCH_EMULATING_POINTER = TouchEventFlagsType(131072)


TouchOwnershipFlagsType = NewType('TouchOwnershipFlagsType', int)


class TouchOwnershipFlagsValues:
    NONE = TouchOwnershipFlagsType(0)


BarrierFlagsType = NewType('BarrierFlagsType', int)


class BarrierFlagsValues:
    POINTER_RELEASED = BarrierFlagsType(1)
    DEVICE_IS_GRABBED = BarrierFlagsType(2)


GesturePinchEventFlagsType = NewType('GesturePinchEventFlagsType', int)


class GesturePinchEventFlagsValues:
    GESTURE_PINCH_CANCELLED = GesturePinchEventFlagsType(1)


GestureSwipeEventFlagsType = NewType('GestureSwipeEventFlagsType', int)


class GestureSwipeEventFlagsValues:
    GESTURE_SWIPE_CANCELLED = GestureSwipeEventFlagsType(1)


# ------------------------------------------------------------------
# Aliases



# ------------------------------------------------------------------
# Structures, Events, Requests, Replies


Fp3232StructPacket = DataPacket((
    ('integral', FixedDataPacketField(MARKER_INT32)),
    ('frac', FixedDataPacketField(MARKER_UINT32)),
))


class Fp3232Struct:
    __slots__ = ('integral', 'frac',)

    def __init__(
            self, *,
            integral: Optional[int] = None,
            frac: Optional[int] = None,
    ) -> None:
        self.integral = integral
        self.frac = frac

    def as_dict(self) -> Dict[str, Any]:
        return {
            'integral': self.integral,
            'frac': self.frac,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'Fp3232Struct':
        return Fp3232Struct(**Fp3232StructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return Fp3232StructPacket.pack(**self.as_dict())


class Fp3232StructCType(ctypes.Structure):
    """xinput FP3232"""
    _fields_ = [
        ("integral", ctypes.c_int32),
        ("frac", ctypes.c_uint32),
    ]


GetExtensionVersionRequestCookie = NewType('GetExtensionVersionRequestCookie', ctypes.c_uint32)


GetExtensionVersionRequestPacket = DataPacket((
    ('name_len', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
    ('name', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['name_len'], 0)),
))


class GetExtensionVersionRequest:
    OPCODE = 1

    __slots__ = ('name_len', 'name',)

    def __init__(
            self, *,
            name_len: Optional[int] = None,
            name: Optional[Sequence[int]] = None,
    ) -> None:
        self.name_len = name_len
        self.name = name

    def as_dict(self) -> Dict[str, Any]:
        return {
            'name_len': self.name_len,
            'name': self.name,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetExtensionVersionRequest':
        return GetExtensionVersionRequest(**GetExtensionVersionRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetExtensionVersionRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, Sequence[int]], GetExtensionVersionRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetExtensionVersionRequest.lib = library.xinput_getextensionversion
        GetExtensionVersionRequest.lib.restype = GetExtensionVersionRequestCookie
        GetExtensionVersionRequest.lib.argstype = (ctypes.c_uint16, ctypes.c_uint8 * 2, ctypes.c_void_p)


class GetExtensionVersionRequestCType(ctypes.Structure):
    """xinput GetExtensionVersion"""
    _fields_ = [
        ("name_len", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


GetExtensionVersionReplyReplyPacket = DataPacket((
    ('xi_reply_type', FixedDataPacketField(MARKER_UINT8)),
    ('server_major', FixedDataPacketField(MARKER_UINT16)),
    ('server_minor', FixedDataPacketField(MARKER_UINT16)),
    ('present', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(19)),
))


class GetExtensionVersionReplyReply:
    __slots__ = ('xi_reply_type', 'server_major', 'server_minor', 'present',)

    def __init__(
            self, *,
            xi_reply_type: Optional[int] = None,
            server_major: Optional[int] = None,
            server_minor: Optional[int] = None,
            present: Optional[bool] = None,
    ) -> None:
        self.xi_reply_type = xi_reply_type
        self.server_major = server_major
        self.server_minor = server_minor
        self.present = present

    def as_dict(self) -> Dict[str, Any]:
        return {
            'xi_reply_type': self.xi_reply_type,
            'server_major': self.server_major,
            'server_minor': self.server_minor,
            'present': self.present,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetExtensionVersionReplyReply':
        return GetExtensionVersionReplyReply(**GetExtensionVersionReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetExtensionVersionReplyReplyPacket.pack(**self.as_dict())


class GetExtensionVersionReplyReplyCType(ctypes.Structure):
    """xinput GetExtensionVersion_reply"""
    _fields_ = [
        ("xi_reply_type", ctypes.c_uint8),
        ("server_major", ctypes.c_uint16),
        ("server_minor", ctypes.c_uint16),
        ("present", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 19),
    ]


DeviceInfoStructPacket = DataPacket((
    ('device_type', FixedDataPacketField(MARKER_UINT32)),
    ('device_id', FixedDataPacketField(MARKER_UINT8)),
    ('num_class_info', FixedDataPacketField(MARKER_UINT8)),
    ('device_use', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
))


class DeviceInfoStruct:
    __slots__ = ('device_type', 'device_id', 'num_class_info', 'device_use',)

    def __init__(
            self, *,
            device_type: Optional[int] = None,
            device_id: Optional[int] = None,
            num_class_info: Optional[int] = None,
            device_use: Optional[int] = None,
    ) -> None:
        self.device_type = device_type
        self.device_id = device_id
        self.num_class_info = num_class_info
        self.device_use = device_use

    def as_dict(self) -> Dict[str, Any]:
        return {
            'device_type': self.device_type,
            'device_id': self.device_id,
            'num_class_info': self.num_class_info,
            'device_use': self.device_use,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeviceInfoStruct':
        return DeviceInfoStruct(**DeviceInfoStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeviceInfoStructPacket.pack(**self.as_dict())


class DeviceInfoStructCType(ctypes.Structure):
    """xinput DeviceInfo"""
    _fields_ = [
        ("device_type", ctypes.c_uint32),
        ("device_id", ctypes.c_uint8),
        ("num_class_info", ctypes.c_uint8),
        ("device_use", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
    ]


KeyInfoStructPacket = DataPacket((
    ('class_id', FixedDataPacketField(MARKER_UINT8)),
    ('len', FixedDataPacketField(MARKER_UINT8)),
    ('min_keycode', FixedDataPacketField(MARKER_UINT32)),
    ('max_keycode', FixedDataPacketField(MARKER_UINT32)),
    ('num_keys', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
))


class KeyInfoStruct:
    __slots__ = ('class_id', 'len', 'min_keycode', 'max_keycode', 'num_keys',)

    def __init__(
            self, *,
            class_id: Optional[int] = None,
            len: Optional[int] = None,
            min_keycode: Optional[int] = None,
            max_keycode: Optional[int] = None,
            num_keys: Optional[int] = None,
    ) -> None:
        self.class_id = class_id
        self.len = len
        self.min_keycode = min_keycode
        self.max_keycode = max_keycode
        self.num_keys = num_keys

    def as_dict(self) -> Dict[str, Any]:
        return {
            'class_id': self.class_id,
            'len': self.len,
            'min_keycode': self.min_keycode,
            'max_keycode': self.max_keycode,
            'num_keys': self.num_keys,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'KeyInfoStruct':
        return KeyInfoStruct(**KeyInfoStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return KeyInfoStructPacket.pack(**self.as_dict())


class KeyInfoStructCType(ctypes.Structure):
    """xinput KeyInfo"""
    _fields_ = [
        ("class_id", ctypes.c_uint8),
        ("len", ctypes.c_uint8),
        ("min_keycode", ctypes.c_uint32),
        ("max_keycode", ctypes.c_uint32),
        ("num_keys", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
    ]


ButtonInfoStructPacket = DataPacket((
    ('class_id', FixedDataPacketField(MARKER_UINT8)),
    ('len', FixedDataPacketField(MARKER_UINT8)),
    ('num_buttons', FixedDataPacketField(MARKER_UINT16)),
))


class ButtonInfoStruct:
    __slots__ = ('class_id', 'len', 'num_buttons',)

    def __init__(
            self, *,
            class_id: Optional[int] = None,
            len: Optional[int] = None,
            num_buttons: Optional[int] = None,
    ) -> None:
        self.class_id = class_id
        self.len = len
        self.num_buttons = num_buttons

    def as_dict(self) -> Dict[str, Any]:
        return {
            'class_id': self.class_id,
            'len': self.len,
            'num_buttons': self.num_buttons,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ButtonInfoStruct':
        return ButtonInfoStruct(**ButtonInfoStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ButtonInfoStructPacket.pack(**self.as_dict())


class ButtonInfoStructCType(ctypes.Structure):
    """xinput ButtonInfo"""
    _fields_ = [
        ("class_id", ctypes.c_uint8),
        ("len", ctypes.c_uint8),
        ("num_buttons", ctypes.c_uint16),
    ]


AxisInfoStructPacket = DataPacket((
    ('resolution', FixedDataPacketField(MARKER_UINT32)),
    ('minimum', FixedDataPacketField(MARKER_INT32)),
    ('maximum', FixedDataPacketField(MARKER_INT32)),
))


class AxisInfoStruct:
    __slots__ = ('resolution', 'minimum', 'maximum',)

    def __init__(
            self, *,
            resolution: Optional[int] = None,
            minimum: Optional[int] = None,
            maximum: Optional[int] = None,
    ) -> None:
        self.resolution = resolution
        self.minimum = minimum
        self.maximum = maximum

    def as_dict(self) -> Dict[str, Any]:
        return {
            'resolution': self.resolution,
            'minimum': self.minimum,
            'maximum': self.maximum,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'AxisInfoStruct':
        return AxisInfoStruct(**AxisInfoStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return AxisInfoStructPacket.pack(**self.as_dict())


class AxisInfoStructCType(ctypes.Structure):
    """xinput AxisInfo"""
    _fields_ = [
        ("resolution", ctypes.c_uint32),
        ("minimum", ctypes.c_int32),
        ("maximum", ctypes.c_int32),
    ]


ValuatorInfoStructPacket = DataPacket((
    ('class_id', FixedDataPacketField(MARKER_UINT8)),
    ('len', FixedDataPacketField(MARKER_UINT8)),
    ('axes_len', FixedDataPacketField(MARKER_UINT8)),
    ('mode', FixedDataPacketField(MARKER_UINT8)),
    ('motion_size', FixedDataPacketField(MARKER_UINT32)),
    ('axes', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['axes_len'], 0)),
))


class ValuatorInfoStruct:
    __slots__ = ('class_id', 'len', 'axes_len', 'mode', 'motion_size', 'axes',)

    def __init__(
            self, *,
            class_id: Optional[int] = None,
            len: Optional[int] = None,
            axes_len: Optional[int] = None,
            mode: Optional[int] = None,
            motion_size: Optional[int] = None,
            axes: Optional[Sequence[int]] = None,
    ) -> None:
        self.class_id = class_id
        self.len = len
        self.axes_len = axes_len
        self.mode = mode
        self.motion_size = motion_size
        self.axes = axes

    def as_dict(self) -> Dict[str, Any]:
        return {
            'class_id': self.class_id,
            'len': self.len,
            'axes_len': self.axes_len,
            'mode': self.mode,
            'motion_size': self.motion_size,
            'axes': self.axes,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ValuatorInfoStruct':
        return ValuatorInfoStruct(**ValuatorInfoStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ValuatorInfoStructPacket.pack(**self.as_dict())


class ValuatorInfoStructCType(ctypes.Structure):
    """xinput ValuatorInfo"""
    _fields_ = [
        ("class_id", ctypes.c_uint8),
        ("len", ctypes.c_uint8),
        ("axes_len", ctypes.c_uint8),
        ("mode", ctypes.c_uint8),
        ("motion_size", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


InputInfoStructPacket = DataPacket((
    ('class_id', FixedDataPacketField(MARKER_UINT8)),
    ('len', FixedDataPacketField(MARKER_UINT8)),
    ('info', UnionDataPacketField(lambda d, c: d['class_id'], {
        InputClassValues.KEY: StructureDataPacketField((
            ('min_keycode', FixedDataPacketField(MARKER_UINT32)),
            ('max_keycode', FixedDataPacketField(MARKER_UINT32)),
            ('num_keys', FixedDataPacketField(MARKER_UINT16)),
            ('pad0', FixedPadDataPacketField(2)),
        )),
        InputClassValues.BUTTON: FixedDataPacketField(MARKER_UINT16),
        InputClassValues.VALUATOR: StructureDataPacketField((
            ('axes_len', FixedDataPacketField(MARKER_UINT8)),
            ('mode', FixedDataPacketField(MARKER_UINT8)),
            ('motion_size', FixedDataPacketField(MARKER_UINT32)),
            ('axes', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['axes_len'], 0)),
        )),
    }, 0)),
))


class InputInfoStruct:
    __slots__ = ('class_id', 'len', 'info',)

    def __init__(
            self, *,
            class_id: Optional[int] = None,
            len: Optional[int] = None,
            info: Optional[Mapping[str, InputClassValues]] = None,
    ) -> None:
        self.class_id = class_id
        self.len = len
        self.info = info

    def as_dict(self) -> Dict[str, Any]:
        return {
            'class_id': self.class_id,
            'len': self.len,
            'info': self.info,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'InputInfoStruct':
        return InputInfoStruct(**InputInfoStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return InputInfoStructPacket.pack(**self.as_dict())


class InputInfoStructCType(ctypes.Structure):
    """xinput InputInfo"""
    _fields_ = [
        ("class_id", ctypes.c_uint8),
        ("len", ctypes.c_uint8),
        ("var_data", ctypes.c_void_p),
    ]


DeviceNameStructPacket = DataPacket((
    ('len', FixedDataPacketField(MARKER_UINT8)),
    ('string', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['len'], 0)),
))


class DeviceNameStruct:
    __slots__ = ('len', 'string',)

    def __init__(
            self, *,
            len: Optional[int] = None,
            string: Optional[Sequence[int]] = None,
    ) -> None:
        self.len = len
        self.string = string

    def as_dict(self) -> Dict[str, Any]:
        return {
            'len': self.len,
            'string': self.string,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeviceNameStruct':
        return DeviceNameStruct(**DeviceNameStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeviceNameStructPacket.pack(**self.as_dict())


class DeviceNameStructCType(ctypes.Structure):
    """xinput DeviceName"""
    _fields_ = [
        ("len", ctypes.c_uint8),
        ("var_data", ctypes.c_void_p),
    ]


ListInputDevicesRequestCookie = NewType('ListInputDevicesRequestCookie', ctypes.c_uint32)


ListInputDevicesRequestPacket = DataPacket((
))


class ListInputDevicesRequest:
    OPCODE = 2

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ListInputDevicesRequest':
        return ListInputDevicesRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], ListInputDevicesRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ListInputDevicesRequest.lib = library.xinput_listinputdevices
        ListInputDevicesRequest.lib.restype = ListInputDevicesRequestCookie
        ListInputDevicesRequest.lib.argstype = ()


class ListInputDevicesRequestCType(ctypes.Structure):
    """xinput ListInputDevices"""
    _fields_ = [
    ]


ListInputDevicesReplyReplyPacket = DataPacket((
    ('xi_reply_type', FixedDataPacketField(MARKER_UINT8)),
    ('devices_len', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(23)),
    ('devices', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['devices_len'], 0)),
    ('infos', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: sum([(d1['num_class_info']) for d1 in d['devices']]), 0)),
    ('names', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['devices_len'], 0)),
    ('pad1', AlignedPadDataPacketField(4)),
))


class ListInputDevicesReplyReply:
    __slots__ = ('xi_reply_type', 'devices_len', 'devices', 'infos', 'names',)

    def __init__(
            self, *,
            xi_reply_type: Optional[int] = None,
            devices_len: Optional[int] = None,
            devices: Optional[Sequence[int]] = None,
            infos: Optional[Sequence[int]] = None,
            names: Optional[Sequence[int]] = None,
    ) -> None:
        self.xi_reply_type = xi_reply_type
        self.devices_len = devices_len
        self.devices = devices
        self.infos = infos
        self.names = names

    def as_dict(self) -> Dict[str, Any]:
        return {
            'xi_reply_type': self.xi_reply_type,
            'devices_len': self.devices_len,
            'devices': self.devices,
            'infos': self.infos,
            'names': self.names,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ListInputDevicesReplyReply':
        return ListInputDevicesReplyReply(**ListInputDevicesReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ListInputDevicesReplyReplyPacket.pack(**self.as_dict())


class ListInputDevicesReplyReplyCType(ctypes.Structure):
    """xinput ListInputDevices_reply"""
    _fields_ = [
        ("xi_reply_type", ctypes.c_uint8),
        ("devices_len", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 23),
        ("var_data", ctypes.c_void_p),
    ]


InputClassInfoStructPacket = DataPacket((
    ('class_id', FixedDataPacketField(MARKER_UINT8)),
    ('event_type_base', FixedDataPacketField(MARKER_UINT32)),
))


class InputClassInfoStruct:
    __slots__ = ('class_id', 'event_type_base',)

    def __init__(
            self, *,
            class_id: Optional[int] = None,
            event_type_base: Optional[int] = None,
    ) -> None:
        self.class_id = class_id
        self.event_type_base = event_type_base

    def as_dict(self) -> Dict[str, Any]:
        return {
            'class_id': self.class_id,
            'event_type_base': self.event_type_base,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'InputClassInfoStruct':
        return InputClassInfoStruct(**InputClassInfoStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return InputClassInfoStructPacket.pack(**self.as_dict())


class InputClassInfoStructCType(ctypes.Structure):
    """xinput InputClassInfo"""
    _fields_ = [
        ("class_id", ctypes.c_uint8),
        ("event_type_base", ctypes.c_uint32),
    ]


OpenDeviceRequestCookie = NewType('OpenDeviceRequestCookie', ctypes.c_uint32)


OpenDeviceRequestPacket = DataPacket((
    ('device_id', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class OpenDeviceRequest:
    OPCODE = 3

    __slots__ = ('device_id',)

    def __init__(
            self, *,
            device_id: Optional[int] = None,
    ) -> None:
        self.device_id = device_id

    def as_dict(self) -> Dict[str, Any]:
        return {
            'device_id': self.device_id,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'OpenDeviceRequest':
        return OpenDeviceRequest(**OpenDeviceRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return OpenDeviceRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], OpenDeviceRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        OpenDeviceRequest.lib = library.xinput_opendevice
        OpenDeviceRequest.lib.restype = OpenDeviceRequestCookie
        OpenDeviceRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint8 * 3)


class OpenDeviceRequestCType(ctypes.Structure):
    """xinput OpenDevice"""
    _fields_ = [
        ("device_id", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


OpenDeviceReplyReplyPacket = DataPacket((
    ('xi_reply_type', FixedDataPacketField(MARKER_UINT8)),
    ('num_classes', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(23)),
    ('class_info', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_classes'], 0)),
    ('pad1', AlignedPadDataPacketField(4)),
))


class OpenDeviceReplyReply:
    __slots__ = ('xi_reply_type', 'num_classes', 'class_info',)

    def __init__(
            self, *,
            xi_reply_type: Optional[int] = None,
            num_classes: Optional[int] = None,
            class_info: Optional[Sequence[int]] = None,
    ) -> None:
        self.xi_reply_type = xi_reply_type
        self.num_classes = num_classes
        self.class_info = class_info

    def as_dict(self) -> Dict[str, Any]:
        return {
            'xi_reply_type': self.xi_reply_type,
            'num_classes': self.num_classes,
            'class_info': self.class_info,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'OpenDeviceReplyReply':
        return OpenDeviceReplyReply(**OpenDeviceReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return OpenDeviceReplyReplyPacket.pack(**self.as_dict())


class OpenDeviceReplyReplyCType(ctypes.Structure):
    """xinput OpenDevice_reply"""
    _fields_ = [
        ("xi_reply_type", ctypes.c_uint8),
        ("num_classes", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 23),
        ("var_data", ctypes.c_void_p),
    ]


CloseDeviceRequestPacket = DataPacket((
    ('device_id', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class CloseDeviceRequest:
    OPCODE = 4

    __slots__ = ('device_id',)

    def __init__(
            self, *,
            device_id: Optional[int] = None,
    ) -> None:
        self.device_id = device_id

    def as_dict(self) -> Dict[str, Any]:
        return {
            'device_id': self.device_id,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CloseDeviceRequest':
        return CloseDeviceRequest(**CloseDeviceRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CloseDeviceRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CloseDeviceRequest.lib = library.xinput_closedevice
        CloseDeviceRequest.lib.restype = ctypes.c_uint32
        CloseDeviceRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint8 * 3)


class CloseDeviceRequestCType(ctypes.Structure):
    """xinput CloseDevice"""
    _fields_ = [
        ("device_id", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


SetDeviceModeRequestCookie = NewType('SetDeviceModeRequestCookie', ctypes.c_uint32)


SetDeviceModeRequestPacket = DataPacket((
    ('device_id', FixedDataPacketField(MARKER_UINT8)),
    ('mode', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
))


class SetDeviceModeRequest:
    OPCODE = 5

    __slots__ = ('device_id', 'mode',)

    def __init__(
            self, *,
            device_id: Optional[int] = None,
            mode: Optional[int] = None,
    ) -> None:
        self.device_id = device_id
        self.mode = mode

    def as_dict(self) -> Dict[str, Any]:
        return {
            'device_id': self.device_id,
            'mode': self.mode,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetDeviceModeRequest':
        return SetDeviceModeRequest(**SetDeviceModeRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetDeviceModeRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], SetDeviceModeRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetDeviceModeRequest.lib = library.xinput_setdevicemode
        SetDeviceModeRequest.lib.restype = SetDeviceModeRequestCookie
        SetDeviceModeRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8 * 2)


class SetDeviceModeRequestCType(ctypes.Structure):
    """xinput SetDeviceMode"""
    _fields_ = [
        ("device_id", ctypes.c_uint8),
        ("mode", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 2),
    ]


SetDeviceModeReplyReplyPacket = DataPacket((
    ('xi_reply_type', FixedDataPacketField(MARKER_UINT8)),
    ('status', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(23)),
))


class SetDeviceModeReplyReply:
    __slots__ = ('xi_reply_type', 'status',)

    def __init__(
            self, *,
            xi_reply_type: Optional[int] = None,
            status: Optional[int] = None,
    ) -> None:
        self.xi_reply_type = xi_reply_type
        self.status = status

    def as_dict(self) -> Dict[str, Any]:
        return {
            'xi_reply_type': self.xi_reply_type,
            'status': self.status,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetDeviceModeReplyReply':
        return SetDeviceModeReplyReply(**SetDeviceModeReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetDeviceModeReplyReplyPacket.pack(**self.as_dict())


class SetDeviceModeReplyReplyCType(ctypes.Structure):
    """xinput SetDeviceMode_reply"""
    _fields_ = [
        ("xi_reply_type", ctypes.c_uint8),
        ("status", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 23),
    ]


SelectExtensionEventRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('num_classes', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
    ('classes', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_classes'], 0)),
))


class SelectExtensionEventRequest:
    OPCODE = 6

    __slots__ = ('window', 'num_classes', 'classes',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            num_classes: Optional[int] = None,
            classes: Optional[Sequence[int]] = None,
    ) -> None:
        self.window = window
        self.num_classes = num_classes
        self.classes = classes

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'num_classes': self.num_classes,
            'classes': self.classes,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SelectExtensionEventRequest':
        return SelectExtensionEventRequest(**SelectExtensionEventRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SelectExtensionEventRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SelectExtensionEventRequest.lib = library.xinput_selectextensionevent
        SelectExtensionEventRequest.lib.restype = ctypes.c_uint32
        SelectExtensionEventRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint8 * 2, ctypes.c_void_p)


class SelectExtensionEventRequestCType(ctypes.Structure):
    """xinput SelectExtensionEvent"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("num_classes", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


GetSelectedExtensionEventsRequestCookie = NewType('GetSelectedExtensionEventsRequestCookie', ctypes.c_uint32)


GetSelectedExtensionEventsRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class GetSelectedExtensionEventsRequest:
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
    def from_data(inp: BinaryIO) -> 'GetSelectedExtensionEventsRequest':
        return GetSelectedExtensionEventsRequest(**GetSelectedExtensionEventsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetSelectedExtensionEventsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetSelectedExtensionEventsRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetSelectedExtensionEventsRequest.lib = library.xinput_getselectedextensionevents
        GetSelectedExtensionEventsRequest.lib.restype = GetSelectedExtensionEventsRequestCookie
        GetSelectedExtensionEventsRequest.lib.argstype = (ctypes.c_uint32,)


class GetSelectedExtensionEventsRequestCType(ctypes.Structure):
    """xinput GetSelectedExtensionEvents"""
    _fields_ = [
        ("window", ctypes.c_uint32),
    ]


GetSelectedExtensionEventsReplyReplyPacket = DataPacket((
    ('xi_reply_type', FixedDataPacketField(MARKER_UINT8)),
    ('num_this_classes', FixedDataPacketField(MARKER_UINT16)),
    ('num_all_classes', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(20)),
    ('this_classes', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_this_classes'], 0)),
    ('all_classes', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_all_classes'], 0)),
))


class GetSelectedExtensionEventsReplyReply:
    __slots__ = ('xi_reply_type', 'num_this_classes', 'num_all_classes', 'this_classes', 'all_classes',)

    def __init__(
            self, *,
            xi_reply_type: Optional[int] = None,
            num_this_classes: Optional[int] = None,
            num_all_classes: Optional[int] = None,
            this_classes: Optional[Sequence[int]] = None,
            all_classes: Optional[Sequence[int]] = None,
    ) -> None:
        self.xi_reply_type = xi_reply_type
        self.num_this_classes = num_this_classes
        self.num_all_classes = num_all_classes
        self.this_classes = this_classes
        self.all_classes = all_classes

    def as_dict(self) -> Dict[str, Any]:
        return {
            'xi_reply_type': self.xi_reply_type,
            'num_this_classes': self.num_this_classes,
            'num_all_classes': self.num_all_classes,
            'this_classes': self.this_classes,
            'all_classes': self.all_classes,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetSelectedExtensionEventsReplyReply':
        return GetSelectedExtensionEventsReplyReply(**GetSelectedExtensionEventsReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetSelectedExtensionEventsReplyReplyPacket.pack(**self.as_dict())


class GetSelectedExtensionEventsReplyReplyCType(ctypes.Structure):
    """xinput GetSelectedExtensionEvents_reply"""
    _fields_ = [
        ("xi_reply_type", ctypes.c_uint8),
        ("num_this_classes", ctypes.c_uint16),
        ("num_all_classes", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


ChangeDeviceDontPropagateListRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('num_classes', FixedDataPacketField(MARKER_UINT16)),
    ('mode', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('classes', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_classes'], 0)),
))


class ChangeDeviceDontPropagateListRequest:
    OPCODE = 8

    __slots__ = ('window', 'num_classes', 'mode', 'classes',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            num_classes: Optional[int] = None,
            mode: Optional[int] = None,
            classes: Optional[Sequence[int]] = None,
    ) -> None:
        self.window = window
        self.num_classes = num_classes
        self.mode = mode
        self.classes = classes

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'num_classes': self.num_classes,
            'mode': self.mode,
            'classes': self.classes,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ChangeDeviceDontPropagateListRequest':
        return ChangeDeviceDontPropagateListRequest(**ChangeDeviceDontPropagateListRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ChangeDeviceDontPropagateListRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ChangeDeviceDontPropagateListRequest.lib = library.xinput_changedevicedontpropagatelist
        ChangeDeviceDontPropagateListRequest.lib.restype = ctypes.c_uint32
        ChangeDeviceDontPropagateListRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_void_p)


class ChangeDeviceDontPropagateListRequestCType(ctypes.Structure):
    """xinput ChangeDeviceDontPropagateList"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("num_classes", ctypes.c_uint16),
        ("mode", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
        ("var_data", ctypes.c_void_p),
    ]


GetDeviceDontPropagateListRequestCookie = NewType('GetDeviceDontPropagateListRequestCookie', ctypes.c_uint32)


GetDeviceDontPropagateListRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class GetDeviceDontPropagateListRequest:
    OPCODE = 9

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
    def from_data(inp: BinaryIO) -> 'GetDeviceDontPropagateListRequest':
        return GetDeviceDontPropagateListRequest(**GetDeviceDontPropagateListRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetDeviceDontPropagateListRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetDeviceDontPropagateListRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetDeviceDontPropagateListRequest.lib = library.xinput_getdevicedontpropagatelist
        GetDeviceDontPropagateListRequest.lib.restype = GetDeviceDontPropagateListRequestCookie
        GetDeviceDontPropagateListRequest.lib.argstype = (ctypes.c_uint32,)


class GetDeviceDontPropagateListRequestCType(ctypes.Structure):
    """xinput GetDeviceDontPropagateList"""
    _fields_ = [
        ("window", ctypes.c_uint32),
    ]


GetDeviceDontPropagateListReplyReplyPacket = DataPacket((
    ('xi_reply_type', FixedDataPacketField(MARKER_UINT8)),
    ('num_classes', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(22)),
    ('classes', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_classes'], 0)),
))


class GetDeviceDontPropagateListReplyReply:
    __slots__ = ('xi_reply_type', 'num_classes', 'classes',)

    def __init__(
            self, *,
            xi_reply_type: Optional[int] = None,
            num_classes: Optional[int] = None,
            classes: Optional[Sequence[int]] = None,
    ) -> None:
        self.xi_reply_type = xi_reply_type
        self.num_classes = num_classes
        self.classes = classes

    def as_dict(self) -> Dict[str, Any]:
        return {
            'xi_reply_type': self.xi_reply_type,
            'num_classes': self.num_classes,
            'classes': self.classes,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetDeviceDontPropagateListReplyReply':
        return GetDeviceDontPropagateListReplyReply(**GetDeviceDontPropagateListReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetDeviceDontPropagateListReplyReplyPacket.pack(**self.as_dict())


class GetDeviceDontPropagateListReplyReplyCType(ctypes.Structure):
    """xinput GetDeviceDontPropagateList_reply"""
    _fields_ = [
        ("xi_reply_type", ctypes.c_uint8),
        ("num_classes", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 22),
        ("var_data", ctypes.c_void_p),
    ]


DeviceTimeCoordStructPacket = DataPacket((
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('axisvalues', SimpleListDataPacketField(MARKER_INT32, lambda d, c: d['num_axes'], 0)),
))


class DeviceTimeCoordStruct:
    __slots__ = ('time', 'axisvalues',)

    def __init__(
            self, *,
            time: Optional[int] = None,
            axisvalues: Optional[Sequence[int]] = None,
    ) -> None:
        self.time = time
        self.axisvalues = axisvalues

    def as_dict(self) -> Dict[str, Any]:
        return {
            'time': self.time,
            'axisvalues': self.axisvalues,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeviceTimeCoordStruct':
        return DeviceTimeCoordStruct(**DeviceTimeCoordStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeviceTimeCoordStructPacket.pack(**self.as_dict())


class DeviceTimeCoordStructCType(ctypes.Structure):
    """xinput DeviceTimeCoord"""
    _fields_ = [
        ("time", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


GetDeviceMotionEventsRequestCookie = NewType('GetDeviceMotionEventsRequestCookie', ctypes.c_uint32)


GetDeviceMotionEventsRequestPacket = DataPacket((
    ('start', FixedDataPacketField(MARKER_UINT32)),
    ('stop', FixedDataPacketField(MARKER_UINT32)),
    ('device_id', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class GetDeviceMotionEventsRequest:
    OPCODE = 10

    __slots__ = ('start', 'stop', 'device_id',)

    def __init__(
            self, *,
            start: Optional[int] = None,
            stop: Optional[int] = None,
            device_id: Optional[int] = None,
    ) -> None:
        self.start = start
        self.stop = stop
        self.device_id = device_id

    def as_dict(self) -> Dict[str, Any]:
        return {
            'start': self.start,
            'stop': self.stop,
            'device_id': self.device_id,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetDeviceMotionEventsRequest':
        return GetDeviceMotionEventsRequest(**GetDeviceMotionEventsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetDeviceMotionEventsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], GetDeviceMotionEventsRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetDeviceMotionEventsRequest.lib = library.xinput_getdevicemotionevents
        GetDeviceMotionEventsRequest.lib.restype = GetDeviceMotionEventsRequestCookie
        GetDeviceMotionEventsRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8 * 3)


class GetDeviceMotionEventsRequestCType(ctypes.Structure):
    """xinput GetDeviceMotionEvents"""
    _fields_ = [
        ("start", ctypes.c_uint32),
        ("stop", ctypes.c_uint32),
        ("device_id", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


GetDeviceMotionEventsReplyReplyPacket = DataPacket((
    ('xi_reply_type', FixedDataPacketField(MARKER_UINT8)),
    ('num_events', FixedDataPacketField(MARKER_UINT32)),
    ('num_axes', FixedDataPacketField(MARKER_UINT8)),
    ('device_mode', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(18)),
    ('events', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_events'], 0)),
))


class GetDeviceMotionEventsReplyReply:
    __slots__ = ('xi_reply_type', 'num_events', 'num_axes', 'device_mode', 'events',)

    def __init__(
            self, *,
            xi_reply_type: Optional[int] = None,
            num_events: Optional[int] = None,
            num_axes: Optional[int] = None,
            device_mode: Optional[int] = None,
            events: Optional[Sequence[int]] = None,
    ) -> None:
        self.xi_reply_type = xi_reply_type
        self.num_events = num_events
        self.num_axes = num_axes
        self.device_mode = device_mode
        self.events = events

    def as_dict(self) -> Dict[str, Any]:
        return {
            'xi_reply_type': self.xi_reply_type,
            'num_events': self.num_events,
            'num_axes': self.num_axes,
            'device_mode': self.device_mode,
            'events': self.events,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetDeviceMotionEventsReplyReply':
        return GetDeviceMotionEventsReplyReply(**GetDeviceMotionEventsReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetDeviceMotionEventsReplyReplyPacket.pack(**self.as_dict())


class GetDeviceMotionEventsReplyReplyCType(ctypes.Structure):
    """xinput GetDeviceMotionEvents_reply"""
    _fields_ = [
        ("xi_reply_type", ctypes.c_uint8),
        ("num_events", ctypes.c_uint32),
        ("num_axes", ctypes.c_uint8),
        ("device_mode", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 18),
        ("var_data", ctypes.c_void_p),
    ]


ChangeKeyboardDeviceRequestCookie = NewType('ChangeKeyboardDeviceRequestCookie', ctypes.c_uint32)


ChangeKeyboardDeviceRequestPacket = DataPacket((
    ('device_id', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class ChangeKeyboardDeviceRequest:
    OPCODE = 11

    __slots__ = ('device_id',)

    def __init__(
            self, *,
            device_id: Optional[int] = None,
    ) -> None:
        self.device_id = device_id

    def as_dict(self) -> Dict[str, Any]:
        return {
            'device_id': self.device_id,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ChangeKeyboardDeviceRequest':
        return ChangeKeyboardDeviceRequest(**ChangeKeyboardDeviceRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ChangeKeyboardDeviceRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ChangeKeyboardDeviceRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ChangeKeyboardDeviceRequest.lib = library.xinput_changekeyboarddevice
        ChangeKeyboardDeviceRequest.lib.restype = ChangeKeyboardDeviceRequestCookie
        ChangeKeyboardDeviceRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint8 * 3)


class ChangeKeyboardDeviceRequestCType(ctypes.Structure):
    """xinput ChangeKeyboardDevice"""
    _fields_ = [
        ("device_id", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


ChangeKeyboardDeviceReplyReplyPacket = DataPacket((
    ('xi_reply_type', FixedDataPacketField(MARKER_UINT8)),
    ('status', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(23)),
))


class ChangeKeyboardDeviceReplyReply:
    __slots__ = ('xi_reply_type', 'status',)

    def __init__(
            self, *,
            xi_reply_type: Optional[int] = None,
            status: Optional[int] = None,
    ) -> None:
        self.xi_reply_type = xi_reply_type
        self.status = status

    def as_dict(self) -> Dict[str, Any]:
        return {
            'xi_reply_type': self.xi_reply_type,
            'status': self.status,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ChangeKeyboardDeviceReplyReply':
        return ChangeKeyboardDeviceReplyReply(**ChangeKeyboardDeviceReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ChangeKeyboardDeviceReplyReplyPacket.pack(**self.as_dict())


class ChangeKeyboardDeviceReplyReplyCType(ctypes.Structure):
    """xinput ChangeKeyboardDevice_reply"""
    _fields_ = [
        ("xi_reply_type", ctypes.c_uint8),
        ("status", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 23),
    ]


ChangePointerDeviceRequestCookie = NewType('ChangePointerDeviceRequestCookie', ctypes.c_uint32)


ChangePointerDeviceRequestPacket = DataPacket((
    ('x_axis', FixedDataPacketField(MARKER_UINT8)),
    ('y_axis', FixedDataPacketField(MARKER_UINT8)),
    ('device_id', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
))


class ChangePointerDeviceRequest:
    OPCODE = 12

    __slots__ = ('x_axis', 'y_axis', 'device_id',)

    def __init__(
            self, *,
            x_axis: Optional[int] = None,
            y_axis: Optional[int] = None,
            device_id: Optional[int] = None,
    ) -> None:
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.device_id = device_id

    def as_dict(self) -> Dict[str, Any]:
        return {
            'x_axis': self.x_axis,
            'y_axis': self.y_axis,
            'device_id': self.device_id,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ChangePointerDeviceRequest':
        return ChangePointerDeviceRequest(**ChangePointerDeviceRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ChangePointerDeviceRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], ChangePointerDeviceRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ChangePointerDeviceRequest.lib = library.xinput_changepointerdevice
        ChangePointerDeviceRequest.lib.restype = ChangePointerDeviceRequestCookie
        ChangePointerDeviceRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8)


class ChangePointerDeviceRequestCType(ctypes.Structure):
    """xinput ChangePointerDevice"""
    _fields_ = [
        ("x_axis", ctypes.c_uint8),
        ("y_axis", ctypes.c_uint8),
        ("device_id", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
    ]


ChangePointerDeviceReplyReplyPacket = DataPacket((
    ('xi_reply_type', FixedDataPacketField(MARKER_UINT8)),
    ('status', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(23)),
))


class ChangePointerDeviceReplyReply:
    __slots__ = ('xi_reply_type', 'status',)

    def __init__(
            self, *,
            xi_reply_type: Optional[int] = None,
            status: Optional[int] = None,
    ) -> None:
        self.xi_reply_type = xi_reply_type
        self.status = status

    def as_dict(self) -> Dict[str, Any]:
        return {
            'xi_reply_type': self.xi_reply_type,
            'status': self.status,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ChangePointerDeviceReplyReply':
        return ChangePointerDeviceReplyReply(**ChangePointerDeviceReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ChangePointerDeviceReplyReplyPacket.pack(**self.as_dict())


class ChangePointerDeviceReplyReplyCType(ctypes.Structure):
    """xinput ChangePointerDevice_reply"""
    _fields_ = [
        ("xi_reply_type", ctypes.c_uint8),
        ("status", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 23),
    ]


GrabDeviceRequestCookie = NewType('GrabDeviceRequestCookie', ctypes.c_uint32)


GrabDeviceRequestPacket = DataPacket((
    ('grab_window', FixedDataPacketField(MARKER_UINT32)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('num_classes', FixedDataPacketField(MARKER_UINT16)),
    ('this_device_mode', FixedDataPacketField(MARKER_UINT8)),
    ('other_device_mode', FixedDataPacketField(MARKER_UINT8)),
    ('owner_events', FixedDataPacketField(MARKER_UINT8)),
    ('device_id', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
    ('classes', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_classes'], 0)),
))


class GrabDeviceRequest:
    OPCODE = 13

    __slots__ = ('grab_window', 'time', 'num_classes', 'this_device_mode', 'other_device_mode', 'owner_events', 'device_id', 'classes',)

    def __init__(
            self, *,
            grab_window: Optional[int] = None,
            time: Optional[int] = None,
            num_classes: Optional[int] = None,
            this_device_mode: Optional[int] = None,
            other_device_mode: Optional[int] = None,
            owner_events: Optional[bool] = None,
            device_id: Optional[int] = None,
            classes: Optional[Sequence[int]] = None,
    ) -> None:
        self.grab_window = grab_window
        self.time = time
        self.num_classes = num_classes
        self.this_device_mode = this_device_mode
        self.other_device_mode = other_device_mode
        self.owner_events = owner_events
        self.device_id = device_id
        self.classes = classes

    def as_dict(self) -> Dict[str, Any]:
        return {
            'grab_window': self.grab_window,
            'time': self.time,
            'num_classes': self.num_classes,
            'this_device_mode': self.this_device_mode,
            'other_device_mode': self.other_device_mode,
            'owner_events': self.owner_events,
            'device_id': self.device_id,
            'classes': self.classes,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GrabDeviceRequest':
        return GrabDeviceRequest(**GrabDeviceRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GrabDeviceRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, bool, int, Sequence[int]], GrabDeviceRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GrabDeviceRequest.lib = library.xinput_grabdevice
        GrabDeviceRequest.lib.restype = GrabDeviceRequestCookie
        GrabDeviceRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_int8, ctypes.c_uint8, ctypes.c_uint8 * 2, ctypes.c_void_p)


class GrabDeviceRequestCType(ctypes.Structure):
    """xinput GrabDevice"""
    _fields_ = [
        ("grab_window", ctypes.c_uint32),
        ("time", ctypes.c_uint32),
        ("num_classes", ctypes.c_uint16),
        ("this_device_mode", ctypes.c_uint8),
        ("other_device_mode", ctypes.c_uint8),
        ("owner_events", ctypes.c_int8),
        ("device_id", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


GrabDeviceReplyReplyPacket = DataPacket((
    ('xi_reply_type', FixedDataPacketField(MARKER_UINT8)),
    ('status', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(23)),
))


class GrabDeviceReplyReply:
    __slots__ = ('xi_reply_type', 'status',)

    def __init__(
            self, *,
            xi_reply_type: Optional[int] = None,
            status: Optional[int] = None,
    ) -> None:
        self.xi_reply_type = xi_reply_type
        self.status = status

    def as_dict(self) -> Dict[str, Any]:
        return {
            'xi_reply_type': self.xi_reply_type,
            'status': self.status,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GrabDeviceReplyReply':
        return GrabDeviceReplyReply(**GrabDeviceReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GrabDeviceReplyReplyPacket.pack(**self.as_dict())


class GrabDeviceReplyReplyCType(ctypes.Structure):
    """xinput GrabDevice_reply"""
    _fields_ = [
        ("xi_reply_type", ctypes.c_uint8),
        ("status", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 23),
    ]


UngrabDeviceRequestPacket = DataPacket((
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('device_id', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class UngrabDeviceRequest:
    OPCODE = 14

    __slots__ = ('time', 'device_id',)

    def __init__(
            self, *,
            time: Optional[int] = None,
            device_id: Optional[int] = None,
    ) -> None:
        self.time = time
        self.device_id = device_id

    def as_dict(self) -> Dict[str, Any]:
        return {
            'time': self.time,
            'device_id': self.device_id,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'UngrabDeviceRequest':
        return UngrabDeviceRequest(**UngrabDeviceRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return UngrabDeviceRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        UngrabDeviceRequest.lib = library.xinput_ungrabdevice
        UngrabDeviceRequest.lib.restype = ctypes.c_uint32
        UngrabDeviceRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8 * 3)


class UngrabDeviceRequestCType(ctypes.Structure):
    """xinput UngrabDevice"""
    _fields_ = [
        ("time", ctypes.c_uint32),
        ("device_id", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


GrabDeviceKeyRequestPacket = DataPacket((
    ('grab_window', FixedDataPacketField(MARKER_UINT32)),
    ('num_classes', FixedDataPacketField(MARKER_UINT16)),
    ('modifiers', FixedDataPacketField(MARKER_UINT16)),
    ('modifier_device', FixedDataPacketField(MARKER_UINT8)),
    ('grabbed_device', FixedDataPacketField(MARKER_UINT8)),
    ('key', FixedDataPacketField(MARKER_UINT8)),
    ('this_device_mode', FixedDataPacketField(MARKER_UINT8)),
    ('other_device_mode', FixedDataPacketField(MARKER_UINT8)),
    ('owner_events', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
    ('classes', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_classes'], 0)),
))


class GrabDeviceKeyRequest:
    OPCODE = 15

    __slots__ = ('grab_window', 'num_classes', 'modifiers', 'modifier_device', 'grabbed_device', 'key', 'this_device_mode', 'other_device_mode', 'owner_events', 'classes',)

    def __init__(
            self, *,
            grab_window: Optional[int] = None,
            num_classes: Optional[int] = None,
            modifiers: Optional[int] = None,
            modifier_device: Optional[int] = None,
            grabbed_device: Optional[int] = None,
            key: Optional[int] = None,
            this_device_mode: Optional[int] = None,
            other_device_mode: Optional[int] = None,
            owner_events: Optional[bool] = None,
            classes: Optional[Sequence[int]] = None,
    ) -> None:
        self.grab_window = grab_window
        self.num_classes = num_classes
        self.modifiers = modifiers
        self.modifier_device = modifier_device
        self.grabbed_device = grabbed_device
        self.key = key
        self.this_device_mode = this_device_mode
        self.other_device_mode = other_device_mode
        self.owner_events = owner_events
        self.classes = classes

    def as_dict(self) -> Dict[str, Any]:
        return {
            'grab_window': self.grab_window,
            'num_classes': self.num_classes,
            'modifiers': self.modifiers,
            'modifier_device': self.modifier_device,
            'grabbed_device': self.grabbed_device,
            'key': self.key,
            'this_device_mode': self.this_device_mode,
            'other_device_mode': self.other_device_mode,
            'owner_events': self.owner_events,
            'classes': self.classes,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GrabDeviceKeyRequest':
        return GrabDeviceKeyRequest(**GrabDeviceKeyRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GrabDeviceKeyRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, int, bool, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GrabDeviceKeyRequest.lib = library.xinput_grabdevicekey
        GrabDeviceKeyRequest.lib.restype = ctypes.c_uint32
        GrabDeviceKeyRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_int8, ctypes.c_uint8 * 2, ctypes.c_void_p)


class GrabDeviceKeyRequestCType(ctypes.Structure):
    """xinput GrabDeviceKey"""
    _fields_ = [
        ("grab_window", ctypes.c_uint32),
        ("num_classes", ctypes.c_uint16),
        ("modifiers", ctypes.c_uint16),
        ("modifier_device", ctypes.c_uint8),
        ("grabbed_device", ctypes.c_uint8),
        ("key", ctypes.c_uint8),
        ("this_device_mode", ctypes.c_uint8),
        ("other_device_mode", ctypes.c_uint8),
        ("owner_events", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


UngrabDeviceKeyRequestPacket = DataPacket((
    ('grabWindow', FixedDataPacketField(MARKER_UINT32)),
    ('modifiers', FixedDataPacketField(MARKER_UINT16)),
    ('modifier_device', FixedDataPacketField(MARKER_UINT8)),
    ('key', FixedDataPacketField(MARKER_UINT8)),
    ('grabbed_device', FixedDataPacketField(MARKER_UINT8)),
))


class UngrabDeviceKeyRequest:
    OPCODE = 16

    __slots__ = ('grabwindow', 'modifiers', 'modifier_device', 'key', 'grabbed_device',)

    def __init__(
            self, *,
            grabwindow: Optional[int] = None,
            modifiers: Optional[int] = None,
            modifier_device: Optional[int] = None,
            key: Optional[int] = None,
            grabbed_device: Optional[int] = None,
    ) -> None:
        self.grabwindow = grabwindow
        self.modifiers = modifiers
        self.modifier_device = modifier_device
        self.key = key
        self.grabbed_device = grabbed_device

    def as_dict(self) -> Dict[str, Any]:
        return {
            'grabWindow': self.grabwindow,
            'modifiers': self.modifiers,
            'modifier_device': self.modifier_device,
            'key': self.key,
            'grabbed_device': self.grabbed_device,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'UngrabDeviceKeyRequest':
        return UngrabDeviceKeyRequest(**UngrabDeviceKeyRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return UngrabDeviceKeyRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        UngrabDeviceKeyRequest.lib = library.xinput_ungrabdevicekey
        UngrabDeviceKeyRequest.lib.restype = ctypes.c_uint32
        UngrabDeviceKeyRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8)


class UngrabDeviceKeyRequestCType(ctypes.Structure):
    """xinput UngrabDeviceKey"""
    _fields_ = [
        ("grabWindow", ctypes.c_uint32),
        ("modifiers", ctypes.c_uint16),
        ("modifier_device", ctypes.c_uint8),
        ("key", ctypes.c_uint8),
        ("grabbed_device", ctypes.c_uint8),
    ]


GrabDeviceButtonRequestPacket = DataPacket((
    ('grab_window', FixedDataPacketField(MARKER_UINT32)),
    ('grabbed_device', FixedDataPacketField(MARKER_UINT8)),
    ('modifier_device', FixedDataPacketField(MARKER_UINT8)),
    ('num_classes', FixedDataPacketField(MARKER_UINT16)),
    ('modifiers', FixedDataPacketField(MARKER_UINT16)),
    ('this_device_mode', FixedDataPacketField(MARKER_UINT8)),
    ('other_device_mode', FixedDataPacketField(MARKER_UINT8)),
    ('button', FixedDataPacketField(MARKER_UINT8)),
    ('owner_events', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
    ('classes', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_classes'], 0)),
))


class GrabDeviceButtonRequest:
    OPCODE = 17

    __slots__ = ('grab_window', 'grabbed_device', 'modifier_device', 'num_classes', 'modifiers', 'this_device_mode', 'other_device_mode', 'button', 'owner_events', 'classes',)

    def __init__(
            self, *,
            grab_window: Optional[int] = None,
            grabbed_device: Optional[int] = None,
            modifier_device: Optional[int] = None,
            num_classes: Optional[int] = None,
            modifiers: Optional[int] = None,
            this_device_mode: Optional[int] = None,
            other_device_mode: Optional[int] = None,
            button: Optional[int] = None,
            owner_events: Optional[bool] = None,
            classes: Optional[Sequence[int]] = None,
    ) -> None:
        self.grab_window = grab_window
        self.grabbed_device = grabbed_device
        self.modifier_device = modifier_device
        self.num_classes = num_classes
        self.modifiers = modifiers
        self.this_device_mode = this_device_mode
        self.other_device_mode = other_device_mode
        self.button = button
        self.owner_events = owner_events
        self.classes = classes

    def as_dict(self) -> Dict[str, Any]:
        return {
            'grab_window': self.grab_window,
            'grabbed_device': self.grabbed_device,
            'modifier_device': self.modifier_device,
            'num_classes': self.num_classes,
            'modifiers': self.modifiers,
            'this_device_mode': self.this_device_mode,
            'other_device_mode': self.other_device_mode,
            'button': self.button,
            'owner_events': self.owner_events,
            'classes': self.classes,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GrabDeviceButtonRequest':
        return GrabDeviceButtonRequest(**GrabDeviceButtonRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GrabDeviceButtonRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, int, bool, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GrabDeviceButtonRequest.lib = library.xinput_grabdevicebutton
        GrabDeviceButtonRequest.lib.restype = ctypes.c_uint32
        GrabDeviceButtonRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_int8, ctypes.c_uint8 * 2, ctypes.c_void_p)


class GrabDeviceButtonRequestCType(ctypes.Structure):
    """xinput GrabDeviceButton"""
    _fields_ = [
        ("grab_window", ctypes.c_uint32),
        ("grabbed_device", ctypes.c_uint8),
        ("modifier_device", ctypes.c_uint8),
        ("num_classes", ctypes.c_uint16),
        ("modifiers", ctypes.c_uint16),
        ("this_device_mode", ctypes.c_uint8),
        ("other_device_mode", ctypes.c_uint8),
        ("button", ctypes.c_uint8),
        ("owner_events", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


UngrabDeviceButtonRequestPacket = DataPacket((
    ('grab_window', FixedDataPacketField(MARKER_UINT32)),
    ('modifiers', FixedDataPacketField(MARKER_UINT16)),
    ('modifier_device', FixedDataPacketField(MARKER_UINT8)),
    ('button', FixedDataPacketField(MARKER_UINT8)),
    ('grabbed_device', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class UngrabDeviceButtonRequest:
    OPCODE = 18

    __slots__ = ('grab_window', 'modifiers', 'modifier_device', 'button', 'grabbed_device',)

    def __init__(
            self, *,
            grab_window: Optional[int] = None,
            modifiers: Optional[int] = None,
            modifier_device: Optional[int] = None,
            button: Optional[int] = None,
            grabbed_device: Optional[int] = None,
    ) -> None:
        self.grab_window = grab_window
        self.modifiers = modifiers
        self.modifier_device = modifier_device
        self.button = button
        self.grabbed_device = grabbed_device

    def as_dict(self) -> Dict[str, Any]:
        return {
            'grab_window': self.grab_window,
            'modifiers': self.modifiers,
            'modifier_device': self.modifier_device,
            'button': self.button,
            'grabbed_device': self.grabbed_device,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'UngrabDeviceButtonRequest':
        return UngrabDeviceButtonRequest(**UngrabDeviceButtonRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return UngrabDeviceButtonRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        UngrabDeviceButtonRequest.lib = library.xinput_ungrabdevicebutton
        UngrabDeviceButtonRequest.lib.restype = ctypes.c_uint32
        UngrabDeviceButtonRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8 * 3)


class UngrabDeviceButtonRequestCType(ctypes.Structure):
    """xinput UngrabDeviceButton"""
    _fields_ = [
        ("grab_window", ctypes.c_uint32),
        ("modifiers", ctypes.c_uint16),
        ("modifier_device", ctypes.c_uint8),
        ("button", ctypes.c_uint8),
        ("grabbed_device", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


AllowDeviceEventsRequestPacket = DataPacket((
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('mode', FixedDataPacketField(MARKER_UINT8)),
    ('device_id', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
))


class AllowDeviceEventsRequest:
    OPCODE = 19

    __slots__ = ('time', 'mode', 'device_id',)

    def __init__(
            self, *,
            time: Optional[int] = None,
            mode: Optional[int] = None,
            device_id: Optional[int] = None,
    ) -> None:
        self.time = time
        self.mode = mode
        self.device_id = device_id

    def as_dict(self) -> Dict[str, Any]:
        return {
            'time': self.time,
            'mode': self.mode,
            'device_id': self.device_id,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'AllowDeviceEventsRequest':
        return AllowDeviceEventsRequest(**AllowDeviceEventsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return AllowDeviceEventsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        AllowDeviceEventsRequest.lib = library.xinput_allowdeviceevents
        AllowDeviceEventsRequest.lib.restype = ctypes.c_uint32
        AllowDeviceEventsRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8 * 2)


class AllowDeviceEventsRequestCType(ctypes.Structure):
    """xinput AllowDeviceEvents"""
    _fields_ = [
        ("time", ctypes.c_uint32),
        ("mode", ctypes.c_uint8),
        ("device_id", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 2),
    ]


GetDeviceFocusRequestCookie = NewType('GetDeviceFocusRequestCookie', ctypes.c_uint32)


GetDeviceFocusRequestPacket = DataPacket((
    ('device_id', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class GetDeviceFocusRequest:
    OPCODE = 20

    __slots__ = ('device_id',)

    def __init__(
            self, *,
            device_id: Optional[int] = None,
    ) -> None:
        self.device_id = device_id

    def as_dict(self) -> Dict[str, Any]:
        return {
            'device_id': self.device_id,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetDeviceFocusRequest':
        return GetDeviceFocusRequest(**GetDeviceFocusRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetDeviceFocusRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetDeviceFocusRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetDeviceFocusRequest.lib = library.xinput_getdevicefocus
        GetDeviceFocusRequest.lib.restype = GetDeviceFocusRequestCookie
        GetDeviceFocusRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint8 * 3)


class GetDeviceFocusRequestCType(ctypes.Structure):
    """xinput GetDeviceFocus"""
    _fields_ = [
        ("device_id", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


GetDeviceFocusReplyReplyPacket = DataPacket((
    ('xi_reply_type', FixedDataPacketField(MARKER_UINT8)),
    ('focus', FixedDataPacketField(MARKER_UINT32)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('revert_to', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(15)),
))


class GetDeviceFocusReplyReply:
    __slots__ = ('xi_reply_type', 'focus', 'time', 'revert_to',)

    def __init__(
            self, *,
            xi_reply_type: Optional[int] = None,
            focus: Optional[int] = None,
            time: Optional[int] = None,
            revert_to: Optional[int] = None,
    ) -> None:
        self.xi_reply_type = xi_reply_type
        self.focus = focus
        self.time = time
        self.revert_to = revert_to

    def as_dict(self) -> Dict[str, Any]:
        return {
            'xi_reply_type': self.xi_reply_type,
            'focus': self.focus,
            'time': self.time,
            'revert_to': self.revert_to,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetDeviceFocusReplyReply':
        return GetDeviceFocusReplyReply(**GetDeviceFocusReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetDeviceFocusReplyReplyPacket.pack(**self.as_dict())


class GetDeviceFocusReplyReplyCType(ctypes.Structure):
    """xinput GetDeviceFocus_reply"""
    _fields_ = [
        ("xi_reply_type", ctypes.c_uint8),
        ("focus", ctypes.c_uint32),
        ("time", ctypes.c_uint32),
        ("revert_to", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 15),
    ]


SetDeviceFocusRequestPacket = DataPacket((
    ('focus', FixedDataPacketField(MARKER_UINT32)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('revert_to', FixedDataPacketField(MARKER_UINT8)),
    ('device_id', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
))


class SetDeviceFocusRequest:
    OPCODE = 21

    __slots__ = ('focus', 'time', 'revert_to', 'device_id',)

    def __init__(
            self, *,
            focus: Optional[int] = None,
            time: Optional[int] = None,
            revert_to: Optional[int] = None,
            device_id: Optional[int] = None,
    ) -> None:
        self.focus = focus
        self.time = time
        self.revert_to = revert_to
        self.device_id = device_id

    def as_dict(self) -> Dict[str, Any]:
        return {
            'focus': self.focus,
            'time': self.time,
            'revert_to': self.revert_to,
            'device_id': self.device_id,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetDeviceFocusRequest':
        return SetDeviceFocusRequest(**SetDeviceFocusRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetDeviceFocusRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetDeviceFocusRequest.lib = library.xinput_setdevicefocus
        SetDeviceFocusRequest.lib.restype = ctypes.c_uint32
        SetDeviceFocusRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8 * 2)


class SetDeviceFocusRequestCType(ctypes.Structure):
    """xinput SetDeviceFocus"""
    _fields_ = [
        ("focus", ctypes.c_uint32),
        ("time", ctypes.c_uint32),
        ("revert_to", ctypes.c_uint8),
        ("device_id", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 2),
    ]


KbdFeedbackStateStructPacket = DataPacket((
    ('class_id', FixedDataPacketField(MARKER_UINT8)),
    ('feedback_id', FixedDataPacketField(MARKER_UINT8)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('pitch', FixedDataPacketField(MARKER_UINT16)),
    ('duration', FixedDataPacketField(MARKER_UINT16)),
    ('led_mask', FixedDataPacketField(MARKER_UINT32)),
    ('led_values', FixedDataPacketField(MARKER_UINT32)),
    ('global_auto_repeat', FixedDataPacketField(MARKER_UINT8)),
    ('click', FixedDataPacketField(MARKER_UINT8)),
    ('percent', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('auto_repeats', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: 32, 0)),
))


class KbdFeedbackStateStruct:
    __slots__ = ('class_id', 'feedback_id', 'len', 'pitch', 'duration', 'led_mask', 'led_values', 'global_auto_repeat', 'click', 'percent', 'auto_repeats',)

    def __init__(
            self, *,
            class_id: Optional[int] = None,
            feedback_id: Optional[int] = None,
            len: Optional[int] = None,
            pitch: Optional[int] = None,
            duration: Optional[int] = None,
            led_mask: Optional[int] = None,
            led_values: Optional[int] = None,
            global_auto_repeat: Optional[bool] = None,
            click: Optional[int] = None,
            percent: Optional[int] = None,
            auto_repeats: Optional[Sequence[int]] = None,
    ) -> None:
        self.class_id = class_id
        self.feedback_id = feedback_id
        self.len = len
        self.pitch = pitch
        self.duration = duration
        self.led_mask = led_mask
        self.led_values = led_values
        self.global_auto_repeat = global_auto_repeat
        self.click = click
        self.percent = percent
        self.auto_repeats = auto_repeats

    def as_dict(self) -> Dict[str, Any]:
        return {
            'class_id': self.class_id,
            'feedback_id': self.feedback_id,
            'len': self.len,
            'pitch': self.pitch,
            'duration': self.duration,
            'led_mask': self.led_mask,
            'led_values': self.led_values,
            'global_auto_repeat': self.global_auto_repeat,
            'click': self.click,
            'percent': self.percent,
            'auto_repeats': self.auto_repeats,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'KbdFeedbackStateStruct':
        return KbdFeedbackStateStruct(**KbdFeedbackStateStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return KbdFeedbackStateStructPacket.pack(**self.as_dict())


class KbdFeedbackStateStructCType(ctypes.Structure):
    """xinput KbdFeedbackState"""
    _fields_ = [
        ("class_id", ctypes.c_uint8),
        ("feedback_id", ctypes.c_uint8),
        ("len", ctypes.c_uint16),
        ("pitch", ctypes.c_uint16),
        ("duration", ctypes.c_uint16),
        ("led_mask", ctypes.c_uint32),
        ("led_values", ctypes.c_uint32),
        ("global_auto_repeat", ctypes.c_int8),
        ("click", ctypes.c_uint8),
        ("percent", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
        ("var_data", ctypes.c_void_p),
    ]


PtrFeedbackStateStructPacket = DataPacket((
    ('class_id', FixedDataPacketField(MARKER_UINT8)),
    ('feedback_id', FixedDataPacketField(MARKER_UINT8)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
    ('accel_num', FixedDataPacketField(MARKER_UINT16)),
    ('accel_denom', FixedDataPacketField(MARKER_UINT16)),
    ('threshold', FixedDataPacketField(MARKER_UINT16)),
))


class PtrFeedbackStateStruct:
    __slots__ = ('class_id', 'feedback_id', 'len', 'accel_num', 'accel_denom', 'threshold',)

    def __init__(
            self, *,
            class_id: Optional[int] = None,
            feedback_id: Optional[int] = None,
            len: Optional[int] = None,
            accel_num: Optional[int] = None,
            accel_denom: Optional[int] = None,
            threshold: Optional[int] = None,
    ) -> None:
        self.class_id = class_id
        self.feedback_id = feedback_id
        self.len = len
        self.accel_num = accel_num
        self.accel_denom = accel_denom
        self.threshold = threshold

    def as_dict(self) -> Dict[str, Any]:
        return {
            'class_id': self.class_id,
            'feedback_id': self.feedback_id,
            'len': self.len,
            'accel_num': self.accel_num,
            'accel_denom': self.accel_denom,
            'threshold': self.threshold,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PtrFeedbackStateStruct':
        return PtrFeedbackStateStruct(**PtrFeedbackStateStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PtrFeedbackStateStructPacket.pack(**self.as_dict())


class PtrFeedbackStateStructCType(ctypes.Structure):
    """xinput PtrFeedbackState"""
    _fields_ = [
        ("class_id", ctypes.c_uint8),
        ("feedback_id", ctypes.c_uint8),
        ("len", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
        ("accel_num", ctypes.c_uint16),
        ("accel_denom", ctypes.c_uint16),
        ("threshold", ctypes.c_uint16),
    ]


IntegerFeedbackStateStructPacket = DataPacket((
    ('class_id', FixedDataPacketField(MARKER_UINT8)),
    ('feedback_id', FixedDataPacketField(MARKER_UINT8)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('resolution', FixedDataPacketField(MARKER_UINT32)),
    ('min_value', FixedDataPacketField(MARKER_INT32)),
    ('max_value', FixedDataPacketField(MARKER_INT32)),
))


class IntegerFeedbackStateStruct:
    __slots__ = ('class_id', 'feedback_id', 'len', 'resolution', 'min_value', 'max_value',)

    def __init__(
            self, *,
            class_id: Optional[int] = None,
            feedback_id: Optional[int] = None,
            len: Optional[int] = None,
            resolution: Optional[int] = None,
            min_value: Optional[int] = None,
            max_value: Optional[int] = None,
    ) -> None:
        self.class_id = class_id
        self.feedback_id = feedback_id
        self.len = len
        self.resolution = resolution
        self.min_value = min_value
        self.max_value = max_value

    def as_dict(self) -> Dict[str, Any]:
        return {
            'class_id': self.class_id,
            'feedback_id': self.feedback_id,
            'len': self.len,
            'resolution': self.resolution,
            'min_value': self.min_value,
            'max_value': self.max_value,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'IntegerFeedbackStateStruct':
        return IntegerFeedbackStateStruct(**IntegerFeedbackStateStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return IntegerFeedbackStateStructPacket.pack(**self.as_dict())


class IntegerFeedbackStateStructCType(ctypes.Structure):
    """xinput IntegerFeedbackState"""
    _fields_ = [
        ("class_id", ctypes.c_uint8),
        ("feedback_id", ctypes.c_uint8),
        ("len", ctypes.c_uint16),
        ("resolution", ctypes.c_uint32),
        ("min_value", ctypes.c_int32),
        ("max_value", ctypes.c_int32),
    ]


StringFeedbackStateStructPacket = DataPacket((
    ('class_id', FixedDataPacketField(MARKER_UINT8)),
    ('feedback_id', FixedDataPacketField(MARKER_UINT8)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('max_symbols', FixedDataPacketField(MARKER_UINT16)),
    ('num_keysyms', FixedDataPacketField(MARKER_UINT16)),
    ('keysyms', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_keysyms'], 0)),
))


class StringFeedbackStateStruct:
    __slots__ = ('class_id', 'feedback_id', 'len', 'max_symbols', 'num_keysyms', 'keysyms',)

    def __init__(
            self, *,
            class_id: Optional[int] = None,
            feedback_id: Optional[int] = None,
            len: Optional[int] = None,
            max_symbols: Optional[int] = None,
            num_keysyms: Optional[int] = None,
            keysyms: Optional[Sequence[int]] = None,
    ) -> None:
        self.class_id = class_id
        self.feedback_id = feedback_id
        self.len = len
        self.max_symbols = max_symbols
        self.num_keysyms = num_keysyms
        self.keysyms = keysyms

    def as_dict(self) -> Dict[str, Any]:
        return {
            'class_id': self.class_id,
            'feedback_id': self.feedback_id,
            'len': self.len,
            'max_symbols': self.max_symbols,
            'num_keysyms': self.num_keysyms,
            'keysyms': self.keysyms,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'StringFeedbackStateStruct':
        return StringFeedbackStateStruct(**StringFeedbackStateStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return StringFeedbackStateStructPacket.pack(**self.as_dict())


class StringFeedbackStateStructCType(ctypes.Structure):
    """xinput StringFeedbackState"""
    _fields_ = [
        ("class_id", ctypes.c_uint8),
        ("feedback_id", ctypes.c_uint8),
        ("len", ctypes.c_uint16),
        ("max_symbols", ctypes.c_uint16),
        ("num_keysyms", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


BellFeedbackStateStructPacket = DataPacket((
    ('class_id', FixedDataPacketField(MARKER_UINT8)),
    ('feedback_id', FixedDataPacketField(MARKER_UINT8)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('percent', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
    ('pitch', FixedDataPacketField(MARKER_UINT16)),
    ('duration', FixedDataPacketField(MARKER_UINT16)),
))


class BellFeedbackStateStruct:
    __slots__ = ('class_id', 'feedback_id', 'len', 'percent', 'pitch', 'duration',)

    def __init__(
            self, *,
            class_id: Optional[int] = None,
            feedback_id: Optional[int] = None,
            len: Optional[int] = None,
            percent: Optional[int] = None,
            pitch: Optional[int] = None,
            duration: Optional[int] = None,
    ) -> None:
        self.class_id = class_id
        self.feedback_id = feedback_id
        self.len = len
        self.percent = percent
        self.pitch = pitch
        self.duration = duration

    def as_dict(self) -> Dict[str, Any]:
        return {
            'class_id': self.class_id,
            'feedback_id': self.feedback_id,
            'len': self.len,
            'percent': self.percent,
            'pitch': self.pitch,
            'duration': self.duration,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'BellFeedbackStateStruct':
        return BellFeedbackStateStruct(**BellFeedbackStateStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return BellFeedbackStateStructPacket.pack(**self.as_dict())


class BellFeedbackStateStructCType(ctypes.Structure):
    """xinput BellFeedbackState"""
    _fields_ = [
        ("class_id", ctypes.c_uint8),
        ("feedback_id", ctypes.c_uint8),
        ("len", ctypes.c_uint16),
        ("percent", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
        ("pitch", ctypes.c_uint16),
        ("duration", ctypes.c_uint16),
    ]


LedFeedbackStateStructPacket = DataPacket((
    ('class_id', FixedDataPacketField(MARKER_UINT8)),
    ('feedback_id', FixedDataPacketField(MARKER_UINT8)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('led_mask', FixedDataPacketField(MARKER_UINT32)),
    ('led_values', FixedDataPacketField(MARKER_UINT32)),
))


class LedFeedbackStateStruct:
    __slots__ = ('class_id', 'feedback_id', 'len', 'led_mask', 'led_values',)

    def __init__(
            self, *,
            class_id: Optional[int] = None,
            feedback_id: Optional[int] = None,
            len: Optional[int] = None,
            led_mask: Optional[int] = None,
            led_values: Optional[int] = None,
    ) -> None:
        self.class_id = class_id
        self.feedback_id = feedback_id
        self.len = len
        self.led_mask = led_mask
        self.led_values = led_values

    def as_dict(self) -> Dict[str, Any]:
        return {
            'class_id': self.class_id,
            'feedback_id': self.feedback_id,
            'len': self.len,
            'led_mask': self.led_mask,
            'led_values': self.led_values,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'LedFeedbackStateStruct':
        return LedFeedbackStateStruct(**LedFeedbackStateStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return LedFeedbackStateStructPacket.pack(**self.as_dict())


class LedFeedbackStateStructCType(ctypes.Structure):
    """xinput LedFeedbackState"""
    _fields_ = [
        ("class_id", ctypes.c_uint8),
        ("feedback_id", ctypes.c_uint8),
        ("len", ctypes.c_uint16),
        ("led_mask", ctypes.c_uint32),
        ("led_values", ctypes.c_uint32),
    ]


FeedbackStateStructPacket = DataPacket((
    ('class_id', FixedDataPacketField(MARKER_UINT8)),
    ('feedback_id', FixedDataPacketField(MARKER_UINT8)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('data', UnionDataPacketField(lambda d, c: d['class_id'], {
        FeedbackClassValues.KEYBOARD: StructureDataPacketField((
            ('pitch', FixedDataPacketField(MARKER_UINT16)),
            ('duration', FixedDataPacketField(MARKER_UINT16)),
            ('led_mask', FixedDataPacketField(MARKER_UINT32)),
            ('led_values', FixedDataPacketField(MARKER_UINT32)),
            ('global_auto_repeat', FixedDataPacketField(MARKER_UINT8)),
            ('click', FixedDataPacketField(MARKER_UINT8)),
            ('percent', FixedDataPacketField(MARKER_UINT8)),
            ('pad0', FixedPadDataPacketField(1)),
            ('auto_repeats', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: 32, 0)),
        )),
        FeedbackClassValues.POINTER: StructureDataPacketField((
            ('pad0', FixedPadDataPacketField(2)),
            ('accel_num', FixedDataPacketField(MARKER_UINT16)),
            ('accel_denom', FixedDataPacketField(MARKER_UINT16)),
            ('threshold', FixedDataPacketField(MARKER_UINT16)),
        )),
        FeedbackClassValues.STRING: StructureDataPacketField((
            ('max_symbols', FixedDataPacketField(MARKER_UINT16)),
            ('num_keysyms', FixedDataPacketField(MARKER_UINT16)),
            ('keysyms', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_keysyms'], 0)),
        )),
        FeedbackClassValues.INTEGER: StructureDataPacketField((
            ('resolution', FixedDataPacketField(MARKER_UINT32)),
            ('min_value', FixedDataPacketField(MARKER_INT32)),
            ('max_value', FixedDataPacketField(MARKER_INT32)),
        )),
        FeedbackClassValues.LED: StructureDataPacketField((
            ('led_mask', FixedDataPacketField(MARKER_UINT32)),
            ('led_values', FixedDataPacketField(MARKER_UINT32)),
        )),
        FeedbackClassValues.BELL: StructureDataPacketField((
            ('percent', FixedDataPacketField(MARKER_UINT8)),
            ('pad0', FixedPadDataPacketField(3)),
            ('pitch', FixedDataPacketField(MARKER_UINT16)),
            ('duration', FixedDataPacketField(MARKER_UINT16)),
        )),
    }, 0)),
))


class FeedbackStateStruct:
    __slots__ = ('class_id', 'feedback_id', 'len', 'data',)

    def __init__(
            self, *,
            class_id: Optional[int] = None,
            feedback_id: Optional[int] = None,
            len: Optional[int] = None,
            data: Optional[Mapping[str, FeedbackClassValues]] = None,
    ) -> None:
        self.class_id = class_id
        self.feedback_id = feedback_id
        self.len = len
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'class_id': self.class_id,
            'feedback_id': self.feedback_id,
            'len': self.len,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'FeedbackStateStruct':
        return FeedbackStateStruct(**FeedbackStateStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return FeedbackStateStructPacket.pack(**self.as_dict())


class FeedbackStateStructCType(ctypes.Structure):
    """xinput FeedbackState"""
    _fields_ = [
        ("class_id", ctypes.c_uint8),
        ("feedback_id", ctypes.c_uint8),
        ("len", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


GetFeedbackControlRequestCookie = NewType('GetFeedbackControlRequestCookie', ctypes.c_uint32)


GetFeedbackControlRequestPacket = DataPacket((
    ('device_id', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class GetFeedbackControlRequest:
    OPCODE = 22

    __slots__ = ('device_id',)

    def __init__(
            self, *,
            device_id: Optional[int] = None,
    ) -> None:
        self.device_id = device_id

    def as_dict(self) -> Dict[str, Any]:
        return {
            'device_id': self.device_id,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetFeedbackControlRequest':
        return GetFeedbackControlRequest(**GetFeedbackControlRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetFeedbackControlRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetFeedbackControlRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetFeedbackControlRequest.lib = library.xinput_getfeedbackcontrol
        GetFeedbackControlRequest.lib.restype = GetFeedbackControlRequestCookie
        GetFeedbackControlRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint8 * 3)


class GetFeedbackControlRequestCType(ctypes.Structure):
    """xinput GetFeedbackControl"""
    _fields_ = [
        ("device_id", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


GetFeedbackControlReplyReplyPacket = DataPacket((
    ('xi_reply_type', FixedDataPacketField(MARKER_UINT8)),
    ('num_feedbacks', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(22)),
    ('feedbacks', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_feedbacks'], 0)),
))


class GetFeedbackControlReplyReply:
    __slots__ = ('xi_reply_type', 'num_feedbacks', 'feedbacks',)

    def __init__(
            self, *,
            xi_reply_type: Optional[int] = None,
            num_feedbacks: Optional[int] = None,
            feedbacks: Optional[Sequence[int]] = None,
    ) -> None:
        self.xi_reply_type = xi_reply_type
        self.num_feedbacks = num_feedbacks
        self.feedbacks = feedbacks

    def as_dict(self) -> Dict[str, Any]:
        return {
            'xi_reply_type': self.xi_reply_type,
            'num_feedbacks': self.num_feedbacks,
            'feedbacks': self.feedbacks,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetFeedbackControlReplyReply':
        return GetFeedbackControlReplyReply(**GetFeedbackControlReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetFeedbackControlReplyReplyPacket.pack(**self.as_dict())


class GetFeedbackControlReplyReplyCType(ctypes.Structure):
    """xinput GetFeedbackControl_reply"""
    _fields_ = [
        ("xi_reply_type", ctypes.c_uint8),
        ("num_feedbacks", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 22),
        ("var_data", ctypes.c_void_p),
    ]


KbdFeedbackCtlStructPacket = DataPacket((
    ('class_id', FixedDataPacketField(MARKER_UINT8)),
    ('feedback_id', FixedDataPacketField(MARKER_UINT8)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('key', FixedDataPacketField(MARKER_UINT32)),
    ('auto_repeat_mode', FixedDataPacketField(MARKER_UINT8)),
    ('key_click_percent', FixedDataPacketField(MARKER_INT8)),
    ('bell_percent', FixedDataPacketField(MARKER_INT8)),
    ('bell_pitch', FixedDataPacketField(MARKER_INT16)),
    ('bell_duration', FixedDataPacketField(MARKER_INT16)),
    ('led_mask', FixedDataPacketField(MARKER_UINT32)),
    ('led_values', FixedDataPacketField(MARKER_UINT32)),
))


class KbdFeedbackCtlStruct:
    __slots__ = ('class_id', 'feedback_id', 'len', 'key', 'auto_repeat_mode', 'key_click_percent', 'bell_percent', 'bell_pitch', 'bell_duration', 'led_mask', 'led_values',)

    def __init__(
            self, *,
            class_id: Optional[int] = None,
            feedback_id: Optional[int] = None,
            len: Optional[int] = None,
            key: Optional[int] = None,
            auto_repeat_mode: Optional[int] = None,
            key_click_percent: Optional[int] = None,
            bell_percent: Optional[int] = None,
            bell_pitch: Optional[int] = None,
            bell_duration: Optional[int] = None,
            led_mask: Optional[int] = None,
            led_values: Optional[int] = None,
    ) -> None:
        self.class_id = class_id
        self.feedback_id = feedback_id
        self.len = len
        self.key = key
        self.auto_repeat_mode = auto_repeat_mode
        self.key_click_percent = key_click_percent
        self.bell_percent = bell_percent
        self.bell_pitch = bell_pitch
        self.bell_duration = bell_duration
        self.led_mask = led_mask
        self.led_values = led_values

    def as_dict(self) -> Dict[str, Any]:
        return {
            'class_id': self.class_id,
            'feedback_id': self.feedback_id,
            'len': self.len,
            'key': self.key,
            'auto_repeat_mode': self.auto_repeat_mode,
            'key_click_percent': self.key_click_percent,
            'bell_percent': self.bell_percent,
            'bell_pitch': self.bell_pitch,
            'bell_duration': self.bell_duration,
            'led_mask': self.led_mask,
            'led_values': self.led_values,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'KbdFeedbackCtlStruct':
        return KbdFeedbackCtlStruct(**KbdFeedbackCtlStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return KbdFeedbackCtlStructPacket.pack(**self.as_dict())


class KbdFeedbackCtlStructCType(ctypes.Structure):
    """xinput KbdFeedbackCtl"""
    _fields_ = [
        ("class_id", ctypes.c_uint8),
        ("feedback_id", ctypes.c_uint8),
        ("len", ctypes.c_uint16),
        ("key", ctypes.c_uint32),
        ("auto_repeat_mode", ctypes.c_uint8),
        ("key_click_percent", ctypes.c_int8),
        ("bell_percent", ctypes.c_int8),
        ("bell_pitch", ctypes.c_int16),
        ("bell_duration", ctypes.c_int16),
        ("led_mask", ctypes.c_uint32),
        ("led_values", ctypes.c_uint32),
    ]


PtrFeedbackCtlStructPacket = DataPacket((
    ('class_id', FixedDataPacketField(MARKER_UINT8)),
    ('feedback_id', FixedDataPacketField(MARKER_UINT8)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
    ('num', FixedDataPacketField(MARKER_INT16)),
    ('denom', FixedDataPacketField(MARKER_INT16)),
    ('threshold', FixedDataPacketField(MARKER_INT16)),
))


class PtrFeedbackCtlStruct:
    __slots__ = ('class_id', 'feedback_id', 'len', 'num', 'denom', 'threshold',)

    def __init__(
            self, *,
            class_id: Optional[int] = None,
            feedback_id: Optional[int] = None,
            len: Optional[int] = None,
            num: Optional[int] = None,
            denom: Optional[int] = None,
            threshold: Optional[int] = None,
    ) -> None:
        self.class_id = class_id
        self.feedback_id = feedback_id
        self.len = len
        self.num = num
        self.denom = denom
        self.threshold = threshold

    def as_dict(self) -> Dict[str, Any]:
        return {
            'class_id': self.class_id,
            'feedback_id': self.feedback_id,
            'len': self.len,
            'num': self.num,
            'denom': self.denom,
            'threshold': self.threshold,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PtrFeedbackCtlStruct':
        return PtrFeedbackCtlStruct(**PtrFeedbackCtlStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PtrFeedbackCtlStructPacket.pack(**self.as_dict())


class PtrFeedbackCtlStructCType(ctypes.Structure):
    """xinput PtrFeedbackCtl"""
    _fields_ = [
        ("class_id", ctypes.c_uint8),
        ("feedback_id", ctypes.c_uint8),
        ("len", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
        ("num", ctypes.c_int16),
        ("denom", ctypes.c_int16),
        ("threshold", ctypes.c_int16),
    ]


IntegerFeedbackCtlStructPacket = DataPacket((
    ('class_id', FixedDataPacketField(MARKER_UINT8)),
    ('feedback_id', FixedDataPacketField(MARKER_UINT8)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('int_to_display', FixedDataPacketField(MARKER_INT32)),
))


class IntegerFeedbackCtlStruct:
    __slots__ = ('class_id', 'feedback_id', 'len', 'int_to_display',)

    def __init__(
            self, *,
            class_id: Optional[int] = None,
            feedback_id: Optional[int] = None,
            len: Optional[int] = None,
            int_to_display: Optional[int] = None,
    ) -> None:
        self.class_id = class_id
        self.feedback_id = feedback_id
        self.len = len
        self.int_to_display = int_to_display

    def as_dict(self) -> Dict[str, Any]:
        return {
            'class_id': self.class_id,
            'feedback_id': self.feedback_id,
            'len': self.len,
            'int_to_display': self.int_to_display,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'IntegerFeedbackCtlStruct':
        return IntegerFeedbackCtlStruct(**IntegerFeedbackCtlStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return IntegerFeedbackCtlStructPacket.pack(**self.as_dict())


class IntegerFeedbackCtlStructCType(ctypes.Structure):
    """xinput IntegerFeedbackCtl"""
    _fields_ = [
        ("class_id", ctypes.c_uint8),
        ("feedback_id", ctypes.c_uint8),
        ("len", ctypes.c_uint16),
        ("int_to_display", ctypes.c_int32),
    ]


StringFeedbackCtlStructPacket = DataPacket((
    ('class_id', FixedDataPacketField(MARKER_UINT8)),
    ('feedback_id', FixedDataPacketField(MARKER_UINT8)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
    ('num_keysyms', FixedDataPacketField(MARKER_UINT16)),
    ('keysyms', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_keysyms'], 0)),
))


class StringFeedbackCtlStruct:
    __slots__ = ('class_id', 'feedback_id', 'len', 'num_keysyms', 'keysyms',)

    def __init__(
            self, *,
            class_id: Optional[int] = None,
            feedback_id: Optional[int] = None,
            len: Optional[int] = None,
            num_keysyms: Optional[int] = None,
            keysyms: Optional[Sequence[int]] = None,
    ) -> None:
        self.class_id = class_id
        self.feedback_id = feedback_id
        self.len = len
        self.num_keysyms = num_keysyms
        self.keysyms = keysyms

    def as_dict(self) -> Dict[str, Any]:
        return {
            'class_id': self.class_id,
            'feedback_id': self.feedback_id,
            'len': self.len,
            'num_keysyms': self.num_keysyms,
            'keysyms': self.keysyms,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'StringFeedbackCtlStruct':
        return StringFeedbackCtlStruct(**StringFeedbackCtlStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return StringFeedbackCtlStructPacket.pack(**self.as_dict())


class StringFeedbackCtlStructCType(ctypes.Structure):
    """xinput StringFeedbackCtl"""
    _fields_ = [
        ("class_id", ctypes.c_uint8),
        ("feedback_id", ctypes.c_uint8),
        ("len", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
        ("num_keysyms", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


BellFeedbackCtlStructPacket = DataPacket((
    ('class_id', FixedDataPacketField(MARKER_UINT8)),
    ('feedback_id', FixedDataPacketField(MARKER_UINT8)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('percent', FixedDataPacketField(MARKER_INT8)),
    ('pad0', FixedPadDataPacketField(3)),
    ('pitch', FixedDataPacketField(MARKER_INT16)),
    ('duration', FixedDataPacketField(MARKER_INT16)),
))


class BellFeedbackCtlStruct:
    __slots__ = ('class_id', 'feedback_id', 'len', 'percent', 'pitch', 'duration',)

    def __init__(
            self, *,
            class_id: Optional[int] = None,
            feedback_id: Optional[int] = None,
            len: Optional[int] = None,
            percent: Optional[int] = None,
            pitch: Optional[int] = None,
            duration: Optional[int] = None,
    ) -> None:
        self.class_id = class_id
        self.feedback_id = feedback_id
        self.len = len
        self.percent = percent
        self.pitch = pitch
        self.duration = duration

    def as_dict(self) -> Dict[str, Any]:
        return {
            'class_id': self.class_id,
            'feedback_id': self.feedback_id,
            'len': self.len,
            'percent': self.percent,
            'pitch': self.pitch,
            'duration': self.duration,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'BellFeedbackCtlStruct':
        return BellFeedbackCtlStruct(**BellFeedbackCtlStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return BellFeedbackCtlStructPacket.pack(**self.as_dict())


class BellFeedbackCtlStructCType(ctypes.Structure):
    """xinput BellFeedbackCtl"""
    _fields_ = [
        ("class_id", ctypes.c_uint8),
        ("feedback_id", ctypes.c_uint8),
        ("len", ctypes.c_uint16),
        ("percent", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 3),
        ("pitch", ctypes.c_int16),
        ("duration", ctypes.c_int16),
    ]


LedFeedbackCtlStructPacket = DataPacket((
    ('class_id', FixedDataPacketField(MARKER_UINT8)),
    ('feedback_id', FixedDataPacketField(MARKER_UINT8)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('led_mask', FixedDataPacketField(MARKER_UINT32)),
    ('led_values', FixedDataPacketField(MARKER_UINT32)),
))


class LedFeedbackCtlStruct:
    __slots__ = ('class_id', 'feedback_id', 'len', 'led_mask', 'led_values',)

    def __init__(
            self, *,
            class_id: Optional[int] = None,
            feedback_id: Optional[int] = None,
            len: Optional[int] = None,
            led_mask: Optional[int] = None,
            led_values: Optional[int] = None,
    ) -> None:
        self.class_id = class_id
        self.feedback_id = feedback_id
        self.len = len
        self.led_mask = led_mask
        self.led_values = led_values

    def as_dict(self) -> Dict[str, Any]:
        return {
            'class_id': self.class_id,
            'feedback_id': self.feedback_id,
            'len': self.len,
            'led_mask': self.led_mask,
            'led_values': self.led_values,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'LedFeedbackCtlStruct':
        return LedFeedbackCtlStruct(**LedFeedbackCtlStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return LedFeedbackCtlStructPacket.pack(**self.as_dict())


class LedFeedbackCtlStructCType(ctypes.Structure):
    """xinput LedFeedbackCtl"""
    _fields_ = [
        ("class_id", ctypes.c_uint8),
        ("feedback_id", ctypes.c_uint8),
        ("len", ctypes.c_uint16),
        ("led_mask", ctypes.c_uint32),
        ("led_values", ctypes.c_uint32),
    ]


FeedbackCtlStructPacket = DataPacket((
    ('class_id', FixedDataPacketField(MARKER_UINT8)),
    ('feedback_id', FixedDataPacketField(MARKER_UINT8)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('data', UnionDataPacketField(lambda d, c: d['class_id'], {
        FeedbackClassValues.KEYBOARD: StructureDataPacketField((
            ('key', FixedDataPacketField(MARKER_UINT32)),
            ('auto_repeat_mode', FixedDataPacketField(MARKER_UINT8)),
            ('key_click_percent', FixedDataPacketField(MARKER_INT8)),
            ('bell_percent', FixedDataPacketField(MARKER_INT8)),
            ('bell_pitch', FixedDataPacketField(MARKER_INT16)),
            ('bell_duration', FixedDataPacketField(MARKER_INT16)),
            ('led_mask', FixedDataPacketField(MARKER_UINT32)),
            ('led_values', FixedDataPacketField(MARKER_UINT32)),
        )),
        FeedbackClassValues.POINTER: StructureDataPacketField((
            ('pad0', FixedPadDataPacketField(2)),
            ('num', FixedDataPacketField(MARKER_INT16)),
            ('denom', FixedDataPacketField(MARKER_INT16)),
            ('threshold', FixedDataPacketField(MARKER_INT16)),
        )),
        FeedbackClassValues.STRING: StructureDataPacketField((
            ('pad0', FixedPadDataPacketField(2)),
            ('num_keysyms', FixedDataPacketField(MARKER_UINT16)),
            ('keysyms', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_keysyms'], 0)),
        )),
        FeedbackClassValues.INTEGER: FixedDataPacketField(MARKER_INT32),
        FeedbackClassValues.LED: StructureDataPacketField((
            ('led_mask', FixedDataPacketField(MARKER_UINT32)),
            ('led_values', FixedDataPacketField(MARKER_UINT32)),
        )),
        FeedbackClassValues.BELL: StructureDataPacketField((
            ('percent', FixedDataPacketField(MARKER_INT8)),
            ('pad0', FixedPadDataPacketField(3)),
            ('pitch', FixedDataPacketField(MARKER_INT16)),
            ('duration', FixedDataPacketField(MARKER_INT16)),
        )),
    }, 0)),
))


class FeedbackCtlStruct:
    __slots__ = ('class_id', 'feedback_id', 'len', 'data',)

    def __init__(
            self, *,
            class_id: Optional[int] = None,
            feedback_id: Optional[int] = None,
            len: Optional[int] = None,
            data: Optional[Mapping[str, FeedbackClassValues]] = None,
    ) -> None:
        self.class_id = class_id
        self.feedback_id = feedback_id
        self.len = len
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'class_id': self.class_id,
            'feedback_id': self.feedback_id,
            'len': self.len,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'FeedbackCtlStruct':
        return FeedbackCtlStruct(**FeedbackCtlStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return FeedbackCtlStructPacket.pack(**self.as_dict())


class FeedbackCtlStructCType(ctypes.Structure):
    """xinput FeedbackCtl"""
    _fields_ = [
        ("class_id", ctypes.c_uint8),
        ("feedback_id", ctypes.c_uint8),
        ("len", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


ChangeFeedbackControlRequestPacket = DataPacket((
    ('mask', FixedDataPacketField(MARKER_UINT32)),
    ('device_id', FixedDataPacketField(MARKER_UINT8)),
    ('feedback_id', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
    ('feedback', FixedDataPacketField(MARKER_UINT32)),
))


class ChangeFeedbackControlRequest:
    OPCODE = 23

    __slots__ = ('mask', 'device_id', 'feedback_id', 'feedback',)

    def __init__(
            self, *,
            mask: Optional[int] = None,
            device_id: Optional[int] = None,
            feedback_id: Optional[int] = None,
            feedback: Optional[int] = None,
    ) -> None:
        self.mask = mask
        self.device_id = device_id
        self.feedback_id = feedback_id
        self.feedback = feedback

    def as_dict(self) -> Dict[str, Any]:
        return {
            'mask': self.mask,
            'device_id': self.device_id,
            'feedback_id': self.feedback_id,
            'feedback': self.feedback,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ChangeFeedbackControlRequest':
        return ChangeFeedbackControlRequest(**ChangeFeedbackControlRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ChangeFeedbackControlRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ChangeFeedbackControlRequest.lib = library.xinput_changefeedbackcontrol
        ChangeFeedbackControlRequest.lib.restype = ctypes.c_uint32
        ChangeFeedbackControlRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8 * 2, ctypes.c_uint32)


class ChangeFeedbackControlRequestCType(ctypes.Structure):
    """xinput ChangeFeedbackControl"""
    _fields_ = [
        ("mask", ctypes.c_uint32),
        ("device_id", ctypes.c_uint8),
        ("feedback_id", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 2),
        ("feedback", ctypes.c_uint32),
    ]


GetDeviceKeyMappingRequestCookie = NewType('GetDeviceKeyMappingRequestCookie', ctypes.c_uint32)


GetDeviceKeyMappingRequestPacket = DataPacket((
    ('device_id', FixedDataPacketField(MARKER_UINT8)),
    ('first_keycode', FixedDataPacketField(MARKER_UINT32)),
    ('count', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
))


class GetDeviceKeyMappingRequest:
    OPCODE = 24

    __slots__ = ('device_id', 'first_keycode', 'count',)

    def __init__(
            self, *,
            device_id: Optional[int] = None,
            first_keycode: Optional[int] = None,
            count: Optional[int] = None,
    ) -> None:
        self.device_id = device_id
        self.first_keycode = first_keycode
        self.count = count

    def as_dict(self) -> Dict[str, Any]:
        return {
            'device_id': self.device_id,
            'first_keycode': self.first_keycode,
            'count': self.count,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetDeviceKeyMappingRequest':
        return GetDeviceKeyMappingRequest(**GetDeviceKeyMappingRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetDeviceKeyMappingRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], GetDeviceKeyMappingRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetDeviceKeyMappingRequest.lib = library.xinput_getdevicekeymapping
        GetDeviceKeyMappingRequest.lib.restype = GetDeviceKeyMappingRequestCookie
        GetDeviceKeyMappingRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8)


class GetDeviceKeyMappingRequestCType(ctypes.Structure):
    """xinput GetDeviceKeyMapping"""
    _fields_ = [
        ("device_id", ctypes.c_uint8),
        ("first_keycode", ctypes.c_uint32),
        ("count", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
    ]


GetDeviceKeyMappingReplyReplyPacket = DataPacket((
    ('xi_reply_type', FixedDataPacketField(MARKER_UINT8)),
    ('keysyms_per_keycode', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(23)),
    ('keysyms', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['length'], 0)),
))


class GetDeviceKeyMappingReplyReply:
    __slots__ = ('xi_reply_type', 'keysyms_per_keycode', 'keysyms',)

    def __init__(
            self, *,
            xi_reply_type: Optional[int] = None,
            keysyms_per_keycode: Optional[int] = None,
            keysyms: Optional[Sequence[int]] = None,
    ) -> None:
        self.xi_reply_type = xi_reply_type
        self.keysyms_per_keycode = keysyms_per_keycode
        self.keysyms = keysyms

    def as_dict(self) -> Dict[str, Any]:
        return {
            'xi_reply_type': self.xi_reply_type,
            'keysyms_per_keycode': self.keysyms_per_keycode,
            'keysyms': self.keysyms,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetDeviceKeyMappingReplyReply':
        return GetDeviceKeyMappingReplyReply(**GetDeviceKeyMappingReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetDeviceKeyMappingReplyReplyPacket.pack(**self.as_dict())


class GetDeviceKeyMappingReplyReplyCType(ctypes.Structure):
    """xinput GetDeviceKeyMapping_reply"""
    _fields_ = [
        ("xi_reply_type", ctypes.c_uint8),
        ("keysyms_per_keycode", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 23),
        ("var_data", ctypes.c_void_p),
    ]


ChangeDeviceKeyMappingRequestPacket = DataPacket((
    ('device_id', FixedDataPacketField(MARKER_UINT8)),
    ('first_keycode', FixedDataPacketField(MARKER_UINT32)),
    ('keysyms_per_keycode', FixedDataPacketField(MARKER_UINT8)),
    ('keycode_count', FixedDataPacketField(MARKER_UINT8)),
    ('keysyms', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: (d['keycode_count']) * (d['keysyms_per_keycode']), 0)),
))


class ChangeDeviceKeyMappingRequest:
    OPCODE = 25

    __slots__ = ('device_id', 'first_keycode', 'keysyms_per_keycode', 'keycode_count', 'keysyms',)

    def __init__(
            self, *,
            device_id: Optional[int] = None,
            first_keycode: Optional[int] = None,
            keysyms_per_keycode: Optional[int] = None,
            keycode_count: Optional[int] = None,
            keysyms: Optional[Sequence[int]] = None,
    ) -> None:
        self.device_id = device_id
        self.first_keycode = first_keycode
        self.keysyms_per_keycode = keysyms_per_keycode
        self.keycode_count = keycode_count
        self.keysyms = keysyms

    def as_dict(self) -> Dict[str, Any]:
        return {
            'device_id': self.device_id,
            'first_keycode': self.first_keycode,
            'keysyms_per_keycode': self.keysyms_per_keycode,
            'keycode_count': self.keycode_count,
            'keysyms': self.keysyms,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ChangeDeviceKeyMappingRequest':
        return ChangeDeviceKeyMappingRequest(**ChangeDeviceKeyMappingRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ChangeDeviceKeyMappingRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ChangeDeviceKeyMappingRequest.lib = library.xinput_changedevicekeymapping
        ChangeDeviceKeyMappingRequest.lib.restype = ctypes.c_uint32
        ChangeDeviceKeyMappingRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_void_p)


class ChangeDeviceKeyMappingRequestCType(ctypes.Structure):
    """xinput ChangeDeviceKeyMapping"""
    _fields_ = [
        ("device_id", ctypes.c_uint8),
        ("first_keycode", ctypes.c_uint32),
        ("keysyms_per_keycode", ctypes.c_uint8),
        ("keycode_count", ctypes.c_uint8),
        ("var_data", ctypes.c_void_p),
    ]


GetDeviceModifierMappingRequestCookie = NewType('GetDeviceModifierMappingRequestCookie', ctypes.c_uint32)


GetDeviceModifierMappingRequestPacket = DataPacket((
    ('device_id', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class GetDeviceModifierMappingRequest:
    OPCODE = 26

    __slots__ = ('device_id',)

    def __init__(
            self, *,
            device_id: Optional[int] = None,
    ) -> None:
        self.device_id = device_id

    def as_dict(self) -> Dict[str, Any]:
        return {
            'device_id': self.device_id,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetDeviceModifierMappingRequest':
        return GetDeviceModifierMappingRequest(**GetDeviceModifierMappingRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetDeviceModifierMappingRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetDeviceModifierMappingRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetDeviceModifierMappingRequest.lib = library.xinput_getdevicemodifiermapping
        GetDeviceModifierMappingRequest.lib.restype = GetDeviceModifierMappingRequestCookie
        GetDeviceModifierMappingRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint8 * 3)


class GetDeviceModifierMappingRequestCType(ctypes.Structure):
    """xinput GetDeviceModifierMapping"""
    _fields_ = [
        ("device_id", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


GetDeviceModifierMappingReplyReplyPacket = DataPacket((
    ('xi_reply_type', FixedDataPacketField(MARKER_UINT8)),
    ('keycodes_per_modifier', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(23)),
    ('keymaps', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: (d['keycodes_per_modifier']) * (8), 0)),
))


class GetDeviceModifierMappingReplyReply:
    __slots__ = ('xi_reply_type', 'keycodes_per_modifier', 'keymaps',)

    def __init__(
            self, *,
            xi_reply_type: Optional[int] = None,
            keycodes_per_modifier: Optional[int] = None,
            keymaps: Optional[Sequence[int]] = None,
    ) -> None:
        self.xi_reply_type = xi_reply_type
        self.keycodes_per_modifier = keycodes_per_modifier
        self.keymaps = keymaps

    def as_dict(self) -> Dict[str, Any]:
        return {
            'xi_reply_type': self.xi_reply_type,
            'keycodes_per_modifier': self.keycodes_per_modifier,
            'keymaps': self.keymaps,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetDeviceModifierMappingReplyReply':
        return GetDeviceModifierMappingReplyReply(**GetDeviceModifierMappingReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetDeviceModifierMappingReplyReplyPacket.pack(**self.as_dict())


class GetDeviceModifierMappingReplyReplyCType(ctypes.Structure):
    """xinput GetDeviceModifierMapping_reply"""
    _fields_ = [
        ("xi_reply_type", ctypes.c_uint8),
        ("keycodes_per_modifier", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 23),
        ("var_data", ctypes.c_void_p),
    ]


SetDeviceModifierMappingRequestCookie = NewType('SetDeviceModifierMappingRequestCookie', ctypes.c_uint32)


SetDeviceModifierMappingRequestPacket = DataPacket((
    ('device_id', FixedDataPacketField(MARKER_UINT8)),
    ('keycodes_per_modifier', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
    ('keymaps', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: (d['keycodes_per_modifier']) * (8), 0)),
))


class SetDeviceModifierMappingRequest:
    OPCODE = 27

    __slots__ = ('device_id', 'keycodes_per_modifier', 'keymaps',)

    def __init__(
            self, *,
            device_id: Optional[int] = None,
            keycodes_per_modifier: Optional[int] = None,
            keymaps: Optional[Sequence[int]] = None,
    ) -> None:
        self.device_id = device_id
        self.keycodes_per_modifier = keycodes_per_modifier
        self.keymaps = keymaps

    def as_dict(self) -> Dict[str, Any]:
        return {
            'device_id': self.device_id,
            'keycodes_per_modifier': self.keycodes_per_modifier,
            'keymaps': self.keymaps,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetDeviceModifierMappingRequest':
        return SetDeviceModifierMappingRequest(**SetDeviceModifierMappingRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetDeviceModifierMappingRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int]], SetDeviceModifierMappingRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetDeviceModifierMappingRequest.lib = library.xinput_setdevicemodifiermapping
        SetDeviceModifierMappingRequest.lib.restype = SetDeviceModifierMappingRequestCookie
        SetDeviceModifierMappingRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8 * 2, ctypes.c_void_p)


class SetDeviceModifierMappingRequestCType(ctypes.Structure):
    """xinput SetDeviceModifierMapping"""
    _fields_ = [
        ("device_id", ctypes.c_uint8),
        ("keycodes_per_modifier", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


SetDeviceModifierMappingReplyReplyPacket = DataPacket((
    ('xi_reply_type', FixedDataPacketField(MARKER_UINT8)),
    ('status', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(23)),
))


class SetDeviceModifierMappingReplyReply:
    __slots__ = ('xi_reply_type', 'status',)

    def __init__(
            self, *,
            xi_reply_type: Optional[int] = None,
            status: Optional[int] = None,
    ) -> None:
        self.xi_reply_type = xi_reply_type
        self.status = status

    def as_dict(self) -> Dict[str, Any]:
        return {
            'xi_reply_type': self.xi_reply_type,
            'status': self.status,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetDeviceModifierMappingReplyReply':
        return SetDeviceModifierMappingReplyReply(**SetDeviceModifierMappingReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetDeviceModifierMappingReplyReplyPacket.pack(**self.as_dict())


class SetDeviceModifierMappingReplyReplyCType(ctypes.Structure):
    """xinput SetDeviceModifierMapping_reply"""
    _fields_ = [
        ("xi_reply_type", ctypes.c_uint8),
        ("status", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 23),
    ]


GetDeviceButtonMappingRequestCookie = NewType('GetDeviceButtonMappingRequestCookie', ctypes.c_uint32)


GetDeviceButtonMappingRequestPacket = DataPacket((
    ('device_id', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class GetDeviceButtonMappingRequest:
    OPCODE = 28

    __slots__ = ('device_id',)

    def __init__(
            self, *,
            device_id: Optional[int] = None,
    ) -> None:
        self.device_id = device_id

    def as_dict(self) -> Dict[str, Any]:
        return {
            'device_id': self.device_id,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetDeviceButtonMappingRequest':
        return GetDeviceButtonMappingRequest(**GetDeviceButtonMappingRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetDeviceButtonMappingRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetDeviceButtonMappingRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetDeviceButtonMappingRequest.lib = library.xinput_getdevicebuttonmapping
        GetDeviceButtonMappingRequest.lib.restype = GetDeviceButtonMappingRequestCookie
        GetDeviceButtonMappingRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint8 * 3)


class GetDeviceButtonMappingRequestCType(ctypes.Structure):
    """xinput GetDeviceButtonMapping"""
    _fields_ = [
        ("device_id", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


GetDeviceButtonMappingReplyReplyPacket = DataPacket((
    ('xi_reply_type', FixedDataPacketField(MARKER_UINT8)),
    ('map_size', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(23)),
    ('map', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: d['map_size'], 0)),
    ('pad1', AlignedPadDataPacketField(4)),
))


class GetDeviceButtonMappingReplyReply:
    __slots__ = ('xi_reply_type', 'map_size', 'map',)

    def __init__(
            self, *,
            xi_reply_type: Optional[int] = None,
            map_size: Optional[int] = None,
            map: Optional[Sequence[int]] = None,
    ) -> None:
        self.xi_reply_type = xi_reply_type
        self.map_size = map_size
        self.map = map

    def as_dict(self) -> Dict[str, Any]:
        return {
            'xi_reply_type': self.xi_reply_type,
            'map_size': self.map_size,
            'map': self.map,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetDeviceButtonMappingReplyReply':
        return GetDeviceButtonMappingReplyReply(**GetDeviceButtonMappingReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetDeviceButtonMappingReplyReplyPacket.pack(**self.as_dict())


class GetDeviceButtonMappingReplyReplyCType(ctypes.Structure):
    """xinput GetDeviceButtonMapping_reply"""
    _fields_ = [
        ("xi_reply_type", ctypes.c_uint8),
        ("map_size", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 23),
        ("var_data", ctypes.c_void_p),
    ]


SetDeviceButtonMappingRequestCookie = NewType('SetDeviceButtonMappingRequestCookie', ctypes.c_uint32)


SetDeviceButtonMappingRequestPacket = DataPacket((
    ('device_id', FixedDataPacketField(MARKER_UINT8)),
    ('map_size', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
    ('map', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: d['map_size'], 0)),
))


class SetDeviceButtonMappingRequest:
    OPCODE = 29

    __slots__ = ('device_id', 'map_size', 'map',)

    def __init__(
            self, *,
            device_id: Optional[int] = None,
            map_size: Optional[int] = None,
            map: Optional[Sequence[int]] = None,
    ) -> None:
        self.device_id = device_id
        self.map_size = map_size
        self.map = map

    def as_dict(self) -> Dict[str, Any]:
        return {
            'device_id': self.device_id,
            'map_size': self.map_size,
            'map': self.map,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetDeviceButtonMappingRequest':
        return SetDeviceButtonMappingRequest(**SetDeviceButtonMappingRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetDeviceButtonMappingRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int]], SetDeviceButtonMappingRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetDeviceButtonMappingRequest.lib = library.xinput_setdevicebuttonmapping
        SetDeviceButtonMappingRequest.lib.restype = SetDeviceButtonMappingRequestCookie
        SetDeviceButtonMappingRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8 * 2, ctypes.c_void_p)


class SetDeviceButtonMappingRequestCType(ctypes.Structure):
    """xinput SetDeviceButtonMapping"""
    _fields_ = [
        ("device_id", ctypes.c_uint8),
        ("map_size", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


SetDeviceButtonMappingReplyReplyPacket = DataPacket((
    ('xi_reply_type', FixedDataPacketField(MARKER_UINT8)),
    ('status', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(23)),
))


class SetDeviceButtonMappingReplyReply:
    __slots__ = ('xi_reply_type', 'status',)

    def __init__(
            self, *,
            xi_reply_type: Optional[int] = None,
            status: Optional[int] = None,
    ) -> None:
        self.xi_reply_type = xi_reply_type
        self.status = status

    def as_dict(self) -> Dict[str, Any]:
        return {
            'xi_reply_type': self.xi_reply_type,
            'status': self.status,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetDeviceButtonMappingReplyReply':
        return SetDeviceButtonMappingReplyReply(**SetDeviceButtonMappingReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetDeviceButtonMappingReplyReplyPacket.pack(**self.as_dict())


class SetDeviceButtonMappingReplyReplyCType(ctypes.Structure):
    """xinput SetDeviceButtonMapping_reply"""
    _fields_ = [
        ("xi_reply_type", ctypes.c_uint8),
        ("status", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 23),
    ]


KeyStateStructPacket = DataPacket((
    ('class_id', FixedDataPacketField(MARKER_UINT8)),
    ('len', FixedDataPacketField(MARKER_UINT8)),
    ('num_keys', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('keys', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: 32, 0)),
))


class KeyStateStruct:
    __slots__ = ('class_id', 'len', 'num_keys', 'keys',)

    def __init__(
            self, *,
            class_id: Optional[int] = None,
            len: Optional[int] = None,
            num_keys: Optional[int] = None,
            keys: Optional[Sequence[int]] = None,
    ) -> None:
        self.class_id = class_id
        self.len = len
        self.num_keys = num_keys
        self.keys = keys

    def as_dict(self) -> Dict[str, Any]:
        return {
            'class_id': self.class_id,
            'len': self.len,
            'num_keys': self.num_keys,
            'keys': self.keys,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'KeyStateStruct':
        return KeyStateStruct(**KeyStateStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return KeyStateStructPacket.pack(**self.as_dict())


class KeyStateStructCType(ctypes.Structure):
    """xinput KeyState"""
    _fields_ = [
        ("class_id", ctypes.c_uint8),
        ("len", ctypes.c_uint8),
        ("num_keys", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
        ("var_data", ctypes.c_void_p),
    ]


ButtonStateStructPacket = DataPacket((
    ('class_id', FixedDataPacketField(MARKER_UINT8)),
    ('len', FixedDataPacketField(MARKER_UINT8)),
    ('num_buttons', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('buttons', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: 32, 0)),
))


class ButtonStateStruct:
    __slots__ = ('class_id', 'len', 'num_buttons', 'buttons',)

    def __init__(
            self, *,
            class_id: Optional[int] = None,
            len: Optional[int] = None,
            num_buttons: Optional[int] = None,
            buttons: Optional[Sequence[int]] = None,
    ) -> None:
        self.class_id = class_id
        self.len = len
        self.num_buttons = num_buttons
        self.buttons = buttons

    def as_dict(self) -> Dict[str, Any]:
        return {
            'class_id': self.class_id,
            'len': self.len,
            'num_buttons': self.num_buttons,
            'buttons': self.buttons,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ButtonStateStruct':
        return ButtonStateStruct(**ButtonStateStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ButtonStateStructPacket.pack(**self.as_dict())


class ButtonStateStructCType(ctypes.Structure):
    """xinput ButtonState"""
    _fields_ = [
        ("class_id", ctypes.c_uint8),
        ("len", ctypes.c_uint8),
        ("num_buttons", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
        ("var_data", ctypes.c_void_p),
    ]


ValuatorStateStructPacket = DataPacket((
    ('class_id', FixedDataPacketField(MARKER_UINT8)),
    ('len', FixedDataPacketField(MARKER_UINT8)),
    ('num_valuators', FixedDataPacketField(MARKER_UINT8)),
    ('mode', FixedDataPacketField(MARKER_UINT8)),
    ('valuators', SimpleListDataPacketField(MARKER_INT32, lambda d, c: d['num_valuators'], 0)),
))


class ValuatorStateStruct:
    __slots__ = ('class_id', 'len', 'num_valuators', 'mode', 'valuators',)

    def __init__(
            self, *,
            class_id: Optional[int] = None,
            len: Optional[int] = None,
            num_valuators: Optional[int] = None,
            mode: Optional[int] = None,
            valuators: Optional[Sequence[int]] = None,
    ) -> None:
        self.class_id = class_id
        self.len = len
        self.num_valuators = num_valuators
        self.mode = mode
        self.valuators = valuators

    def as_dict(self) -> Dict[str, Any]:
        return {
            'class_id': self.class_id,
            'len': self.len,
            'num_valuators': self.num_valuators,
            'mode': self.mode,
            'valuators': self.valuators,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ValuatorStateStruct':
        return ValuatorStateStruct(**ValuatorStateStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ValuatorStateStructPacket.pack(**self.as_dict())


class ValuatorStateStructCType(ctypes.Structure):
    """xinput ValuatorState"""
    _fields_ = [
        ("class_id", ctypes.c_uint8),
        ("len", ctypes.c_uint8),
        ("num_valuators", ctypes.c_uint8),
        ("mode", ctypes.c_uint8),
        ("var_data", ctypes.c_void_p),
    ]


InputStateStructPacket = DataPacket((
    ('class_id', FixedDataPacketField(MARKER_UINT8)),
    ('len', FixedDataPacketField(MARKER_UINT8)),
    ('data', UnionDataPacketField(lambda d, c: d['class_id'], {
        InputClassValues.KEY: StructureDataPacketField((
            ('num_keys', FixedDataPacketField(MARKER_UINT8)),
            ('pad0', FixedPadDataPacketField(1)),
            ('keys', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: 32, 0)),
        )),
        InputClassValues.BUTTON: StructureDataPacketField((
            ('num_buttons', FixedDataPacketField(MARKER_UINT8)),
            ('pad0', FixedPadDataPacketField(1)),
            ('buttons', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: 32, 0)),
        )),
        InputClassValues.VALUATOR: StructureDataPacketField((
            ('num_valuators', FixedDataPacketField(MARKER_UINT8)),
            ('mode', FixedDataPacketField(MARKER_UINT8)),
            ('valuators', SimpleListDataPacketField(MARKER_INT32, lambda d, c: d['num_valuators'], 0)),
        )),
    }, 0)),
))


class InputStateStruct:
    __slots__ = ('class_id', 'len', 'data',)

    def __init__(
            self, *,
            class_id: Optional[int] = None,
            len: Optional[int] = None,
            data: Optional[Mapping[str, InputClassValues]] = None,
    ) -> None:
        self.class_id = class_id
        self.len = len
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'class_id': self.class_id,
            'len': self.len,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'InputStateStruct':
        return InputStateStruct(**InputStateStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return InputStateStructPacket.pack(**self.as_dict())


class InputStateStructCType(ctypes.Structure):
    """xinput InputState"""
    _fields_ = [
        ("class_id", ctypes.c_uint8),
        ("len", ctypes.c_uint8),
        ("var_data", ctypes.c_void_p),
    ]


QueryDeviceStateRequestCookie = NewType('QueryDeviceStateRequestCookie', ctypes.c_uint32)


QueryDeviceStateRequestPacket = DataPacket((
    ('device_id', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class QueryDeviceStateRequest:
    OPCODE = 30

    __slots__ = ('device_id',)

    def __init__(
            self, *,
            device_id: Optional[int] = None,
    ) -> None:
        self.device_id = device_id

    def as_dict(self) -> Dict[str, Any]:
        return {
            'device_id': self.device_id,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryDeviceStateRequest':
        return QueryDeviceStateRequest(**QueryDeviceStateRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryDeviceStateRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], QueryDeviceStateRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryDeviceStateRequest.lib = library.xinput_querydevicestate
        QueryDeviceStateRequest.lib.restype = QueryDeviceStateRequestCookie
        QueryDeviceStateRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint8 * 3)


class QueryDeviceStateRequestCType(ctypes.Structure):
    """xinput QueryDeviceState"""
    _fields_ = [
        ("device_id", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


QueryDeviceStateReplyReplyPacket = DataPacket((
    ('xi_reply_type', FixedDataPacketField(MARKER_UINT8)),
    ('num_classes', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(23)),
    ('classes', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_classes'], 0)),
))


class QueryDeviceStateReplyReply:
    __slots__ = ('xi_reply_type', 'num_classes', 'classes',)

    def __init__(
            self, *,
            xi_reply_type: Optional[int] = None,
            num_classes: Optional[int] = None,
            classes: Optional[Sequence[int]] = None,
    ) -> None:
        self.xi_reply_type = xi_reply_type
        self.num_classes = num_classes
        self.classes = classes

    def as_dict(self) -> Dict[str, Any]:
        return {
            'xi_reply_type': self.xi_reply_type,
            'num_classes': self.num_classes,
            'classes': self.classes,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryDeviceStateReplyReply':
        return QueryDeviceStateReplyReply(**QueryDeviceStateReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryDeviceStateReplyReplyPacket.pack(**self.as_dict())


class QueryDeviceStateReplyReplyCType(ctypes.Structure):
    """xinput QueryDeviceState_reply"""
    _fields_ = [
        ("xi_reply_type", ctypes.c_uint8),
        ("num_classes", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 23),
        ("var_data", ctypes.c_void_p),
    ]


DeviceBellRequestPacket = DataPacket((
    ('device_id', FixedDataPacketField(MARKER_UINT8)),
    ('feedback_id', FixedDataPacketField(MARKER_UINT8)),
    ('feedback_class', FixedDataPacketField(MARKER_UINT8)),
    ('percent', FixedDataPacketField(MARKER_INT8)),
))


class DeviceBellRequest:
    OPCODE = 32

    __slots__ = ('device_id', 'feedback_id', 'feedback_class', 'percent',)

    def __init__(
            self, *,
            device_id: Optional[int] = None,
            feedback_id: Optional[int] = None,
            feedback_class: Optional[int] = None,
            percent: Optional[int] = None,
    ) -> None:
        self.device_id = device_id
        self.feedback_id = feedback_id
        self.feedback_class = feedback_class
        self.percent = percent

    def as_dict(self) -> Dict[str, Any]:
        return {
            'device_id': self.device_id,
            'feedback_id': self.feedback_id,
            'feedback_class': self.feedback_class,
            'percent': self.percent,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeviceBellRequest':
        return DeviceBellRequest(**DeviceBellRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeviceBellRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        DeviceBellRequest.lib = library.xinput_devicebell
        DeviceBellRequest.lib.restype = ctypes.c_uint32
        DeviceBellRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_int8)


class DeviceBellRequestCType(ctypes.Structure):
    """xinput DeviceBell"""
    _fields_ = [
        ("device_id", ctypes.c_uint8),
        ("feedback_id", ctypes.c_uint8),
        ("feedback_class", ctypes.c_uint8),
        ("percent", ctypes.c_int8),
    ]


SetDeviceValuatorsRequestCookie = NewType('SetDeviceValuatorsRequestCookie', ctypes.c_uint32)


SetDeviceValuatorsRequestPacket = DataPacket((
    ('device_id', FixedDataPacketField(MARKER_UINT8)),
    ('first_valuator', FixedDataPacketField(MARKER_UINT8)),
    ('num_valuators', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('valuators', SimpleListDataPacketField(MARKER_INT32, lambda d, c: d['num_valuators'], 0)),
))


class SetDeviceValuatorsRequest:
    OPCODE = 33

    __slots__ = ('device_id', 'first_valuator', 'num_valuators', 'valuators',)

    def __init__(
            self, *,
            device_id: Optional[int] = None,
            first_valuator: Optional[int] = None,
            num_valuators: Optional[int] = None,
            valuators: Optional[Sequence[int]] = None,
    ) -> None:
        self.device_id = device_id
        self.first_valuator = first_valuator
        self.num_valuators = num_valuators
        self.valuators = valuators

    def as_dict(self) -> Dict[str, Any]:
        return {
            'device_id': self.device_id,
            'first_valuator': self.first_valuator,
            'num_valuators': self.num_valuators,
            'valuators': self.valuators,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetDeviceValuatorsRequest':
        return SetDeviceValuatorsRequest(**SetDeviceValuatorsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetDeviceValuatorsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, Sequence[int]], SetDeviceValuatorsRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetDeviceValuatorsRequest.lib = library.xinput_setdevicevaluators
        SetDeviceValuatorsRequest.lib.restype = SetDeviceValuatorsRequestCookie
        SetDeviceValuatorsRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_void_p)


class SetDeviceValuatorsRequestCType(ctypes.Structure):
    """xinput SetDeviceValuators"""
    _fields_ = [
        ("device_id", ctypes.c_uint8),
        ("first_valuator", ctypes.c_uint8),
        ("num_valuators", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
        ("var_data", ctypes.c_void_p),
    ]


SetDeviceValuatorsReplyReplyPacket = DataPacket((
    ('xi_reply_type', FixedDataPacketField(MARKER_UINT8)),
    ('status', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(23)),
))


class SetDeviceValuatorsReplyReply:
    __slots__ = ('xi_reply_type', 'status',)

    def __init__(
            self, *,
            xi_reply_type: Optional[int] = None,
            status: Optional[int] = None,
    ) -> None:
        self.xi_reply_type = xi_reply_type
        self.status = status

    def as_dict(self) -> Dict[str, Any]:
        return {
            'xi_reply_type': self.xi_reply_type,
            'status': self.status,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetDeviceValuatorsReplyReply':
        return SetDeviceValuatorsReplyReply(**SetDeviceValuatorsReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetDeviceValuatorsReplyReplyPacket.pack(**self.as_dict())


class SetDeviceValuatorsReplyReplyCType(ctypes.Structure):
    """xinput SetDeviceValuators_reply"""
    _fields_ = [
        ("xi_reply_type", ctypes.c_uint8),
        ("status", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 23),
    ]


DeviceResolutionStateStructPacket = DataPacket((
    ('control_id', FixedDataPacketField(MARKER_UINT16)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('num_valuators', FixedDataPacketField(MARKER_UINT32)),
    ('resolution_values', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_valuators'], 0)),
    ('resolution_min', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_valuators'], 0)),
    ('resolution_max', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_valuators'], 0)),
))


class DeviceResolutionStateStruct:
    __slots__ = ('control_id', 'len', 'num_valuators', 'resolution_values', 'resolution_min', 'resolution_max',)

    def __init__(
            self, *,
            control_id: Optional[int] = None,
            len: Optional[int] = None,
            num_valuators: Optional[int] = None,
            resolution_values: Optional[Sequence[int]] = None,
            resolution_min: Optional[Sequence[int]] = None,
            resolution_max: Optional[Sequence[int]] = None,
    ) -> None:
        self.control_id = control_id
        self.len = len
        self.num_valuators = num_valuators
        self.resolution_values = resolution_values
        self.resolution_min = resolution_min
        self.resolution_max = resolution_max

    def as_dict(self) -> Dict[str, Any]:
        return {
            'control_id': self.control_id,
            'len': self.len,
            'num_valuators': self.num_valuators,
            'resolution_values': self.resolution_values,
            'resolution_min': self.resolution_min,
            'resolution_max': self.resolution_max,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeviceResolutionStateStruct':
        return DeviceResolutionStateStruct(**DeviceResolutionStateStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeviceResolutionStateStructPacket.pack(**self.as_dict())


class DeviceResolutionStateStructCType(ctypes.Structure):
    """xinput DeviceResolutionState"""
    _fields_ = [
        ("control_id", ctypes.c_uint16),
        ("len", ctypes.c_uint16),
        ("num_valuators", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


DeviceAbsCalibStateStructPacket = DataPacket((
    ('control_id', FixedDataPacketField(MARKER_UINT16)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('min_x', FixedDataPacketField(MARKER_INT32)),
    ('max_x', FixedDataPacketField(MARKER_INT32)),
    ('min_y', FixedDataPacketField(MARKER_INT32)),
    ('max_y', FixedDataPacketField(MARKER_INT32)),
    ('flip_x', FixedDataPacketField(MARKER_UINT32)),
    ('flip_y', FixedDataPacketField(MARKER_UINT32)),
    ('rotation', FixedDataPacketField(MARKER_UINT32)),
    ('button_threshold', FixedDataPacketField(MARKER_UINT32)),
))


class DeviceAbsCalibStateStruct:
    __slots__ = ('control_id', 'len', 'min_x', 'max_x', 'min_y', 'max_y', 'flip_x', 'flip_y', 'rotation', 'button_threshold',)

    def __init__(
            self, *,
            control_id: Optional[int] = None,
            len: Optional[int] = None,
            min_x: Optional[int] = None,
            max_x: Optional[int] = None,
            min_y: Optional[int] = None,
            max_y: Optional[int] = None,
            flip_x: Optional[int] = None,
            flip_y: Optional[int] = None,
            rotation: Optional[int] = None,
            button_threshold: Optional[int] = None,
    ) -> None:
        self.control_id = control_id
        self.len = len
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.flip_x = flip_x
        self.flip_y = flip_y
        self.rotation = rotation
        self.button_threshold = button_threshold

    def as_dict(self) -> Dict[str, Any]:
        return {
            'control_id': self.control_id,
            'len': self.len,
            'min_x': self.min_x,
            'max_x': self.max_x,
            'min_y': self.min_y,
            'max_y': self.max_y,
            'flip_x': self.flip_x,
            'flip_y': self.flip_y,
            'rotation': self.rotation,
            'button_threshold': self.button_threshold,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeviceAbsCalibStateStruct':
        return DeviceAbsCalibStateStruct(**DeviceAbsCalibStateStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeviceAbsCalibStateStructPacket.pack(**self.as_dict())


class DeviceAbsCalibStateStructCType(ctypes.Structure):
    """xinput DeviceAbsCalibState"""
    _fields_ = [
        ("control_id", ctypes.c_uint16),
        ("len", ctypes.c_uint16),
        ("min_x", ctypes.c_int32),
        ("max_x", ctypes.c_int32),
        ("min_y", ctypes.c_int32),
        ("max_y", ctypes.c_int32),
        ("flip_x", ctypes.c_uint32),
        ("flip_y", ctypes.c_uint32),
        ("rotation", ctypes.c_uint32),
        ("button_threshold", ctypes.c_uint32),
    ]


DeviceAbsAreaStateStructPacket = DataPacket((
    ('control_id', FixedDataPacketField(MARKER_UINT16)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('offset_x', FixedDataPacketField(MARKER_UINT32)),
    ('offset_y', FixedDataPacketField(MARKER_UINT32)),
    ('width', FixedDataPacketField(MARKER_UINT32)),
    ('height', FixedDataPacketField(MARKER_UINT32)),
    ('screen', FixedDataPacketField(MARKER_UINT32)),
    ('following', FixedDataPacketField(MARKER_UINT32)),
))


class DeviceAbsAreaStateStruct:
    __slots__ = ('control_id', 'len', 'offset_x', 'offset_y', 'width', 'height', 'screen', 'following',)

    def __init__(
            self, *,
            control_id: Optional[int] = None,
            len: Optional[int] = None,
            offset_x: Optional[int] = None,
            offset_y: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            screen: Optional[int] = None,
            following: Optional[int] = None,
    ) -> None:
        self.control_id = control_id
        self.len = len
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.width = width
        self.height = height
        self.screen = screen
        self.following = following

    def as_dict(self) -> Dict[str, Any]:
        return {
            'control_id': self.control_id,
            'len': self.len,
            'offset_x': self.offset_x,
            'offset_y': self.offset_y,
            'width': self.width,
            'height': self.height,
            'screen': self.screen,
            'following': self.following,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeviceAbsAreaStateStruct':
        return DeviceAbsAreaStateStruct(**DeviceAbsAreaStateStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeviceAbsAreaStateStructPacket.pack(**self.as_dict())


class DeviceAbsAreaStateStructCType(ctypes.Structure):
    """xinput DeviceAbsAreaState"""
    _fields_ = [
        ("control_id", ctypes.c_uint16),
        ("len", ctypes.c_uint16),
        ("offset_x", ctypes.c_uint32),
        ("offset_y", ctypes.c_uint32),
        ("width", ctypes.c_uint32),
        ("height", ctypes.c_uint32),
        ("screen", ctypes.c_uint32),
        ("following", ctypes.c_uint32),
    ]


DeviceCoreStateStructPacket = DataPacket((
    ('control_id', FixedDataPacketField(MARKER_UINT16)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('status', FixedDataPacketField(MARKER_UINT8)),
    ('iscore', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
))


class DeviceCoreStateStruct:
    __slots__ = ('control_id', 'len', 'status', 'iscore',)

    def __init__(
            self, *,
            control_id: Optional[int] = None,
            len: Optional[int] = None,
            status: Optional[int] = None,
            iscore: Optional[int] = None,
    ) -> None:
        self.control_id = control_id
        self.len = len
        self.status = status
        self.iscore = iscore

    def as_dict(self) -> Dict[str, Any]:
        return {
            'control_id': self.control_id,
            'len': self.len,
            'status': self.status,
            'iscore': self.iscore,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeviceCoreStateStruct':
        return DeviceCoreStateStruct(**DeviceCoreStateStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeviceCoreStateStructPacket.pack(**self.as_dict())


class DeviceCoreStateStructCType(ctypes.Structure):
    """xinput DeviceCoreState"""
    _fields_ = [
        ("control_id", ctypes.c_uint16),
        ("len", ctypes.c_uint16),
        ("status", ctypes.c_uint8),
        ("iscore", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 2),
    ]


DeviceEnableStateStructPacket = DataPacket((
    ('control_id', FixedDataPacketField(MARKER_UINT16)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('enable', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class DeviceEnableStateStruct:
    __slots__ = ('control_id', 'len', 'enable',)

    def __init__(
            self, *,
            control_id: Optional[int] = None,
            len: Optional[int] = None,
            enable: Optional[int] = None,
    ) -> None:
        self.control_id = control_id
        self.len = len
        self.enable = enable

    def as_dict(self) -> Dict[str, Any]:
        return {
            'control_id': self.control_id,
            'len': self.len,
            'enable': self.enable,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeviceEnableStateStruct':
        return DeviceEnableStateStruct(**DeviceEnableStateStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeviceEnableStateStructPacket.pack(**self.as_dict())


class DeviceEnableStateStructCType(ctypes.Structure):
    """xinput DeviceEnableState"""
    _fields_ = [
        ("control_id", ctypes.c_uint16),
        ("len", ctypes.c_uint16),
        ("enable", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


DeviceStateStructPacket = DataPacket((
    ('control_id', FixedDataPacketField(MARKER_UINT16)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('data', UnionDataPacketField(lambda d, c: d['control_id'], {
        DeviceControlValues.RESOLUTION: StructureDataPacketField((
            ('num_valuators', FixedDataPacketField(MARKER_UINT32)),
            ('resolution_values', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_valuators'], 0)),
            ('resolution_min', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_valuators'], 0)),
            ('resolution_max', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_valuators'], 0)),
        )),
        DeviceControlValues.ABS_CALIB: StructureDataPacketField((
            ('min_x', FixedDataPacketField(MARKER_INT32)),
            ('max_x', FixedDataPacketField(MARKER_INT32)),
            ('min_y', FixedDataPacketField(MARKER_INT32)),
            ('max_y', FixedDataPacketField(MARKER_INT32)),
            ('flip_x', FixedDataPacketField(MARKER_UINT32)),
            ('flip_y', FixedDataPacketField(MARKER_UINT32)),
            ('rotation', FixedDataPacketField(MARKER_UINT32)),
            ('button_threshold', FixedDataPacketField(MARKER_UINT32)),
        )),
        DeviceControlValues.CORE: StructureDataPacketField((
            ('status', FixedDataPacketField(MARKER_UINT8)),
            ('iscore', FixedDataPacketField(MARKER_UINT8)),
            ('pad0', FixedPadDataPacketField(2)),
        )),
        DeviceControlValues.ENABLE: StructureDataPacketField((
            ('enable', FixedDataPacketField(MARKER_UINT8)),
            ('pad0', FixedPadDataPacketField(3)),
        )),
        DeviceControlValues.ABS_AREA: StructureDataPacketField((
            ('offset_x', FixedDataPacketField(MARKER_UINT32)),
            ('offset_y', FixedDataPacketField(MARKER_UINT32)),
            ('width', FixedDataPacketField(MARKER_UINT32)),
            ('height', FixedDataPacketField(MARKER_UINT32)),
            ('screen', FixedDataPacketField(MARKER_UINT32)),
            ('following', FixedDataPacketField(MARKER_UINT32)),
        )),
    }, 0)),
))


class DeviceStateStruct:
    __slots__ = ('control_id', 'len', 'data',)

    def __init__(
            self, *,
            control_id: Optional[int] = None,
            len: Optional[int] = None,
            data: Optional[Mapping[str, DeviceControlValues]] = None,
    ) -> None:
        self.control_id = control_id
        self.len = len
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'control_id': self.control_id,
            'len': self.len,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeviceStateStruct':
        return DeviceStateStruct(**DeviceStateStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeviceStateStructPacket.pack(**self.as_dict())


class DeviceStateStructCType(ctypes.Structure):
    """xinput DeviceState"""
    _fields_ = [
        ("control_id", ctypes.c_uint16),
        ("len", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


GetDeviceControlRequestCookie = NewType('GetDeviceControlRequestCookie', ctypes.c_uint32)


GetDeviceControlRequestPacket = DataPacket((
    ('control_id', FixedDataPacketField(MARKER_UINT16)),
    ('device_id', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
))


class GetDeviceControlRequest:
    OPCODE = 34

    __slots__ = ('control_id', 'device_id',)

    def __init__(
            self, *,
            control_id: Optional[int] = None,
            device_id: Optional[int] = None,
    ) -> None:
        self.control_id = control_id
        self.device_id = device_id

    def as_dict(self) -> Dict[str, Any]:
        return {
            'control_id': self.control_id,
            'device_id': self.device_id,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetDeviceControlRequest':
        return GetDeviceControlRequest(**GetDeviceControlRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetDeviceControlRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], GetDeviceControlRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetDeviceControlRequest.lib = library.xinput_getdevicecontrol
        GetDeviceControlRequest.lib.restype = GetDeviceControlRequestCookie
        GetDeviceControlRequest.lib.argstype = (ctypes.c_uint16, ctypes.c_uint8, ctypes.c_uint8)


class GetDeviceControlRequestCType(ctypes.Structure):
    """xinput GetDeviceControl"""
    _fields_ = [
        ("control_id", ctypes.c_uint16),
        ("device_id", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
    ]


GetDeviceControlReplyReplyPacket = DataPacket((
    ('xi_reply_type', FixedDataPacketField(MARKER_UINT8)),
    ('status', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(23)),
    ('control', FixedDataPacketField(MARKER_UINT32)),
))


class GetDeviceControlReplyReply:
    __slots__ = ('xi_reply_type', 'status', 'control',)

    def __init__(
            self, *,
            xi_reply_type: Optional[int] = None,
            status: Optional[int] = None,
            control: Optional[int] = None,
    ) -> None:
        self.xi_reply_type = xi_reply_type
        self.status = status
        self.control = control

    def as_dict(self) -> Dict[str, Any]:
        return {
            'xi_reply_type': self.xi_reply_type,
            'status': self.status,
            'control': self.control,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetDeviceControlReplyReply':
        return GetDeviceControlReplyReply(**GetDeviceControlReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetDeviceControlReplyReplyPacket.pack(**self.as_dict())


class GetDeviceControlReplyReplyCType(ctypes.Structure):
    """xinput GetDeviceControl_reply"""
    _fields_ = [
        ("xi_reply_type", ctypes.c_uint8),
        ("status", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 23),
        ("control", ctypes.c_uint32),
    ]


DeviceResolutionCtlStructPacket = DataPacket((
    ('control_id', FixedDataPacketField(MARKER_UINT16)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('first_valuator', FixedDataPacketField(MARKER_UINT8)),
    ('num_valuators', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
    ('resolution_values', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_valuators'], 0)),
))


class DeviceResolutionCtlStruct:
    __slots__ = ('control_id', 'len', 'first_valuator', 'num_valuators', 'resolution_values',)

    def __init__(
            self, *,
            control_id: Optional[int] = None,
            len: Optional[int] = None,
            first_valuator: Optional[int] = None,
            num_valuators: Optional[int] = None,
            resolution_values: Optional[Sequence[int]] = None,
    ) -> None:
        self.control_id = control_id
        self.len = len
        self.first_valuator = first_valuator
        self.num_valuators = num_valuators
        self.resolution_values = resolution_values

    def as_dict(self) -> Dict[str, Any]:
        return {
            'control_id': self.control_id,
            'len': self.len,
            'first_valuator': self.first_valuator,
            'num_valuators': self.num_valuators,
            'resolution_values': self.resolution_values,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeviceResolutionCtlStruct':
        return DeviceResolutionCtlStruct(**DeviceResolutionCtlStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeviceResolutionCtlStructPacket.pack(**self.as_dict())


class DeviceResolutionCtlStructCType(ctypes.Structure):
    """xinput DeviceResolutionCtl"""
    _fields_ = [
        ("control_id", ctypes.c_uint16),
        ("len", ctypes.c_uint16),
        ("first_valuator", ctypes.c_uint8),
        ("num_valuators", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


DeviceAbsCalibCtlStructPacket = DataPacket((
    ('control_id', FixedDataPacketField(MARKER_UINT16)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('min_x', FixedDataPacketField(MARKER_INT32)),
    ('max_x', FixedDataPacketField(MARKER_INT32)),
    ('min_y', FixedDataPacketField(MARKER_INT32)),
    ('max_y', FixedDataPacketField(MARKER_INT32)),
    ('flip_x', FixedDataPacketField(MARKER_UINT32)),
    ('flip_y', FixedDataPacketField(MARKER_UINT32)),
    ('rotation', FixedDataPacketField(MARKER_UINT32)),
    ('button_threshold', FixedDataPacketField(MARKER_UINT32)),
))


class DeviceAbsCalibCtlStruct:
    __slots__ = ('control_id', 'len', 'min_x', 'max_x', 'min_y', 'max_y', 'flip_x', 'flip_y', 'rotation', 'button_threshold',)

    def __init__(
            self, *,
            control_id: Optional[int] = None,
            len: Optional[int] = None,
            min_x: Optional[int] = None,
            max_x: Optional[int] = None,
            min_y: Optional[int] = None,
            max_y: Optional[int] = None,
            flip_x: Optional[int] = None,
            flip_y: Optional[int] = None,
            rotation: Optional[int] = None,
            button_threshold: Optional[int] = None,
    ) -> None:
        self.control_id = control_id
        self.len = len
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.flip_x = flip_x
        self.flip_y = flip_y
        self.rotation = rotation
        self.button_threshold = button_threshold

    def as_dict(self) -> Dict[str, Any]:
        return {
            'control_id': self.control_id,
            'len': self.len,
            'min_x': self.min_x,
            'max_x': self.max_x,
            'min_y': self.min_y,
            'max_y': self.max_y,
            'flip_x': self.flip_x,
            'flip_y': self.flip_y,
            'rotation': self.rotation,
            'button_threshold': self.button_threshold,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeviceAbsCalibCtlStruct':
        return DeviceAbsCalibCtlStruct(**DeviceAbsCalibCtlStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeviceAbsCalibCtlStructPacket.pack(**self.as_dict())


class DeviceAbsCalibCtlStructCType(ctypes.Structure):
    """xinput DeviceAbsCalibCtl"""
    _fields_ = [
        ("control_id", ctypes.c_uint16),
        ("len", ctypes.c_uint16),
        ("min_x", ctypes.c_int32),
        ("max_x", ctypes.c_int32),
        ("min_y", ctypes.c_int32),
        ("max_y", ctypes.c_int32),
        ("flip_x", ctypes.c_uint32),
        ("flip_y", ctypes.c_uint32),
        ("rotation", ctypes.c_uint32),
        ("button_threshold", ctypes.c_uint32),
    ]


DeviceAbsAreaCtrlStructPacket = DataPacket((
    ('control_id', FixedDataPacketField(MARKER_UINT16)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('offset_x', FixedDataPacketField(MARKER_UINT32)),
    ('offset_y', FixedDataPacketField(MARKER_UINT32)),
    ('width', FixedDataPacketField(MARKER_INT32)),
    ('height', FixedDataPacketField(MARKER_INT32)),
    ('screen', FixedDataPacketField(MARKER_INT32)),
    ('following', FixedDataPacketField(MARKER_UINT32)),
))


class DeviceAbsAreaCtrlStruct:
    __slots__ = ('control_id', 'len', 'offset_x', 'offset_y', 'width', 'height', 'screen', 'following',)

    def __init__(
            self, *,
            control_id: Optional[int] = None,
            len: Optional[int] = None,
            offset_x: Optional[int] = None,
            offset_y: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            screen: Optional[int] = None,
            following: Optional[int] = None,
    ) -> None:
        self.control_id = control_id
        self.len = len
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.width = width
        self.height = height
        self.screen = screen
        self.following = following

    def as_dict(self) -> Dict[str, Any]:
        return {
            'control_id': self.control_id,
            'len': self.len,
            'offset_x': self.offset_x,
            'offset_y': self.offset_y,
            'width': self.width,
            'height': self.height,
            'screen': self.screen,
            'following': self.following,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeviceAbsAreaCtrlStruct':
        return DeviceAbsAreaCtrlStruct(**DeviceAbsAreaCtrlStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeviceAbsAreaCtrlStructPacket.pack(**self.as_dict())


class DeviceAbsAreaCtrlStructCType(ctypes.Structure):
    """xinput DeviceAbsAreaCtrl"""
    _fields_ = [
        ("control_id", ctypes.c_uint16),
        ("len", ctypes.c_uint16),
        ("offset_x", ctypes.c_uint32),
        ("offset_y", ctypes.c_uint32),
        ("width", ctypes.c_int32),
        ("height", ctypes.c_int32),
        ("screen", ctypes.c_int32),
        ("following", ctypes.c_uint32),
    ]


DeviceCoreCtrlStructPacket = DataPacket((
    ('control_id', FixedDataPacketField(MARKER_UINT16)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('status', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class DeviceCoreCtrlStruct:
    __slots__ = ('control_id', 'len', 'status',)

    def __init__(
            self, *,
            control_id: Optional[int] = None,
            len: Optional[int] = None,
            status: Optional[int] = None,
    ) -> None:
        self.control_id = control_id
        self.len = len
        self.status = status

    def as_dict(self) -> Dict[str, Any]:
        return {
            'control_id': self.control_id,
            'len': self.len,
            'status': self.status,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeviceCoreCtrlStruct':
        return DeviceCoreCtrlStruct(**DeviceCoreCtrlStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeviceCoreCtrlStructPacket.pack(**self.as_dict())


class DeviceCoreCtrlStructCType(ctypes.Structure):
    """xinput DeviceCoreCtrl"""
    _fields_ = [
        ("control_id", ctypes.c_uint16),
        ("len", ctypes.c_uint16),
        ("status", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


DeviceEnableCtrlStructPacket = DataPacket((
    ('control_id', FixedDataPacketField(MARKER_UINT16)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('enable', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class DeviceEnableCtrlStruct:
    __slots__ = ('control_id', 'len', 'enable',)

    def __init__(
            self, *,
            control_id: Optional[int] = None,
            len: Optional[int] = None,
            enable: Optional[int] = None,
    ) -> None:
        self.control_id = control_id
        self.len = len
        self.enable = enable

    def as_dict(self) -> Dict[str, Any]:
        return {
            'control_id': self.control_id,
            'len': self.len,
            'enable': self.enable,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeviceEnableCtrlStruct':
        return DeviceEnableCtrlStruct(**DeviceEnableCtrlStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeviceEnableCtrlStructPacket.pack(**self.as_dict())


class DeviceEnableCtrlStructCType(ctypes.Structure):
    """xinput DeviceEnableCtrl"""
    _fields_ = [
        ("control_id", ctypes.c_uint16),
        ("len", ctypes.c_uint16),
        ("enable", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


DeviceCtlStructPacket = DataPacket((
    ('control_id', FixedDataPacketField(MARKER_UINT16)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('data', UnionDataPacketField(lambda d, c: d['control_id'], {
        DeviceControlValues.RESOLUTION: StructureDataPacketField((
            ('first_valuator', FixedDataPacketField(MARKER_UINT8)),
            ('num_valuators', FixedDataPacketField(MARKER_UINT8)),
            ('pad0', FixedPadDataPacketField(2)),
            ('resolution_values', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_valuators'], 0)),
        )),
        DeviceControlValues.ABS_CALIB: StructureDataPacketField((
            ('min_x', FixedDataPacketField(MARKER_INT32)),
            ('max_x', FixedDataPacketField(MARKER_INT32)),
            ('min_y', FixedDataPacketField(MARKER_INT32)),
            ('max_y', FixedDataPacketField(MARKER_INT32)),
            ('flip_x', FixedDataPacketField(MARKER_UINT32)),
            ('flip_y', FixedDataPacketField(MARKER_UINT32)),
            ('rotation', FixedDataPacketField(MARKER_UINT32)),
            ('button_threshold', FixedDataPacketField(MARKER_UINT32)),
        )),
        DeviceControlValues.CORE: StructureDataPacketField((
            ('status', FixedDataPacketField(MARKER_UINT8)),
            ('pad0', FixedPadDataPacketField(3)),
        )),
        DeviceControlValues.ENABLE: StructureDataPacketField((
            ('enable', FixedDataPacketField(MARKER_UINT8)),
            ('pad0', FixedPadDataPacketField(3)),
        )),
        DeviceControlValues.ABS_AREA: StructureDataPacketField((
            ('offset_x', FixedDataPacketField(MARKER_UINT32)),
            ('offset_y', FixedDataPacketField(MARKER_UINT32)),
            ('width', FixedDataPacketField(MARKER_INT32)),
            ('height', FixedDataPacketField(MARKER_INT32)),
            ('screen', FixedDataPacketField(MARKER_INT32)),
            ('following', FixedDataPacketField(MARKER_UINT32)),
        )),
    }, 0)),
))


class DeviceCtlStruct:
    __slots__ = ('control_id', 'len', 'data',)

    def __init__(
            self, *,
            control_id: Optional[int] = None,
            len: Optional[int] = None,
            data: Optional[Mapping[str, DeviceControlValues]] = None,
    ) -> None:
        self.control_id = control_id
        self.len = len
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'control_id': self.control_id,
            'len': self.len,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeviceCtlStruct':
        return DeviceCtlStruct(**DeviceCtlStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeviceCtlStructPacket.pack(**self.as_dict())


class DeviceCtlStructCType(ctypes.Structure):
    """xinput DeviceCtl"""
    _fields_ = [
        ("control_id", ctypes.c_uint16),
        ("len", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


ChangeDeviceControlRequestCookie = NewType('ChangeDeviceControlRequestCookie', ctypes.c_uint32)


ChangeDeviceControlRequestPacket = DataPacket((
    ('control_id', FixedDataPacketField(MARKER_UINT16)),
    ('device_id', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('control', FixedDataPacketField(MARKER_UINT32)),
))


class ChangeDeviceControlRequest:
    OPCODE = 35

    __slots__ = ('control_id', 'device_id', 'control',)

    def __init__(
            self, *,
            control_id: Optional[int] = None,
            device_id: Optional[int] = None,
            control: Optional[int] = None,
    ) -> None:
        self.control_id = control_id
        self.device_id = device_id
        self.control = control

    def as_dict(self) -> Dict[str, Any]:
        return {
            'control_id': self.control_id,
            'device_id': self.device_id,
            'control': self.control,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ChangeDeviceControlRequest':
        return ChangeDeviceControlRequest(**ChangeDeviceControlRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ChangeDeviceControlRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], ChangeDeviceControlRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ChangeDeviceControlRequest.lib = library.xinput_changedevicecontrol
        ChangeDeviceControlRequest.lib.restype = ChangeDeviceControlRequestCookie
        ChangeDeviceControlRequest.lib.argstype = (ctypes.c_uint16, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint32)


class ChangeDeviceControlRequestCType(ctypes.Structure):
    """xinput ChangeDeviceControl"""
    _fields_ = [
        ("control_id", ctypes.c_uint16),
        ("device_id", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
        ("control", ctypes.c_uint32),
    ]


ChangeDeviceControlReplyReplyPacket = DataPacket((
    ('xi_reply_type', FixedDataPacketField(MARKER_UINT8)),
    ('status', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(23)),
))


class ChangeDeviceControlReplyReply:
    __slots__ = ('xi_reply_type', 'status',)

    def __init__(
            self, *,
            xi_reply_type: Optional[int] = None,
            status: Optional[int] = None,
    ) -> None:
        self.xi_reply_type = xi_reply_type
        self.status = status

    def as_dict(self) -> Dict[str, Any]:
        return {
            'xi_reply_type': self.xi_reply_type,
            'status': self.status,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ChangeDeviceControlReplyReply':
        return ChangeDeviceControlReplyReply(**ChangeDeviceControlReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ChangeDeviceControlReplyReplyPacket.pack(**self.as_dict())


class ChangeDeviceControlReplyReplyCType(ctypes.Structure):
    """xinput ChangeDeviceControl_reply"""
    _fields_ = [
        ("xi_reply_type", ctypes.c_uint8),
        ("status", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 23),
    ]


ListDevicePropertiesRequestCookie = NewType('ListDevicePropertiesRequestCookie', ctypes.c_uint32)


ListDevicePropertiesRequestPacket = DataPacket((
    ('device_id', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class ListDevicePropertiesRequest:
    OPCODE = 36

    __slots__ = ('device_id',)

    def __init__(
            self, *,
            device_id: Optional[int] = None,
    ) -> None:
        self.device_id = device_id

    def as_dict(self) -> Dict[str, Any]:
        return {
            'device_id': self.device_id,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ListDevicePropertiesRequest':
        return ListDevicePropertiesRequest(**ListDevicePropertiesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ListDevicePropertiesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ListDevicePropertiesRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ListDevicePropertiesRequest.lib = library.xinput_listdeviceproperties
        ListDevicePropertiesRequest.lib.restype = ListDevicePropertiesRequestCookie
        ListDevicePropertiesRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint8 * 3)


class ListDevicePropertiesRequestCType(ctypes.Structure):
    """xinput ListDeviceProperties"""
    _fields_ = [
        ("device_id", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


ListDevicePropertiesReplyReplyPacket = DataPacket((
    ('xi_reply_type', FixedDataPacketField(MARKER_UINT8)),
    ('num_atoms', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(22)),
    ('atoms', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_atoms'], 0)),
))


class ListDevicePropertiesReplyReply:
    __slots__ = ('xi_reply_type', 'num_atoms', 'atoms',)

    def __init__(
            self, *,
            xi_reply_type: Optional[int] = None,
            num_atoms: Optional[int] = None,
            atoms: Optional[Sequence[int]] = None,
    ) -> None:
        self.xi_reply_type = xi_reply_type
        self.num_atoms = num_atoms
        self.atoms = atoms

    def as_dict(self) -> Dict[str, Any]:
        return {
            'xi_reply_type': self.xi_reply_type,
            'num_atoms': self.num_atoms,
            'atoms': self.atoms,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ListDevicePropertiesReplyReply':
        return ListDevicePropertiesReplyReply(**ListDevicePropertiesReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ListDevicePropertiesReplyReplyPacket.pack(**self.as_dict())


class ListDevicePropertiesReplyReplyCType(ctypes.Structure):
    """xinput ListDeviceProperties_reply"""
    _fields_ = [
        ("xi_reply_type", ctypes.c_uint8),
        ("num_atoms", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 22),
        ("var_data", ctypes.c_void_p),
    ]


ChangeDevicePropertyRequestPacket = DataPacket((
    ('property', FixedDataPacketField(MARKER_UINT32)),
    ('type', FixedDataPacketField(MARKER_UINT32)),
    ('device_id', FixedDataPacketField(MARKER_UINT8)),
    ('format', FixedDataPacketField(MARKER_UINT8)),
    ('mode', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('num_items', FixedDataPacketField(MARKER_UINT32)),
    ('items', UnionDataPacketField(lambda d, c: d['format'], {
        PropertyFormatValues.V_8BITS: StructureDataPacketField((
            ('data8', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: d['num_items'], 0)),
            ('pad0', AlignedPadDataPacketField(4)),
        )),
        PropertyFormatValues.V_16BITS: StructureDataPacketField((
            ('data16', SimpleListDataPacketField(MARKER_UINT16, lambda d, c: d['num_items'], 0)),
            ('pad0', AlignedPadDataPacketField(4)),
        )),
        PropertyFormatValues.V_32BITS: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_items'], 0),
    }, 0)),
))


class ChangeDevicePropertyRequest:
    OPCODE = 37

    __slots__ = ('property', 'type', 'device_id', 'format', 'mode', 'num_items', 'items',)

    def __init__(
            self, *,
            property: Optional[int] = None,
            type: Optional[int] = None,
            device_id: Optional[int] = None,
            format: Optional[int] = None,
            mode: Optional[int] = None,
            num_items: Optional[int] = None,
            items: Optional[Mapping[str, PropertyFormatValues]] = None,
    ) -> None:
        self.property = property
        self.type = type
        self.device_id = device_id
        self.format = format
        self.mode = mode
        self.num_items = num_items
        self.items = items

    def as_dict(self) -> Dict[str, Any]:
        return {
            'property': self.property,
            'type': self.type,
            'device_id': self.device_id,
            'format': self.format,
            'mode': self.mode,
            'num_items': self.num_items,
            'items': self.items,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ChangeDevicePropertyRequest':
        return ChangeDevicePropertyRequest(**ChangeDevicePropertyRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ChangeDevicePropertyRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, Mapping[str, PropertyFormatValues]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ChangeDevicePropertyRequest.lib = library.xinput_changedeviceproperty
        ChangeDevicePropertyRequest.lib.restype = ctypes.c_uint32
        ChangeDevicePropertyRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint32, ctypes.c_void_p)


class ChangeDevicePropertyRequestCType(ctypes.Structure):
    """xinput ChangeDeviceProperty"""
    _fields_ = [
        ("property", ctypes.c_uint32),
        ("type", ctypes.c_uint32),
        ("device_id", ctypes.c_uint8),
        ("format", ctypes.c_uint8),
        ("mode", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
        ("num_items", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


DeleteDevicePropertyRequestPacket = DataPacket((
    ('property', FixedDataPacketField(MARKER_UINT32)),
    ('device_id', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class DeleteDevicePropertyRequest:
    OPCODE = 38

    __slots__ = ('property', 'device_id',)

    def __init__(
            self, *,
            property: Optional[int] = None,
            device_id: Optional[int] = None,
    ) -> None:
        self.property = property
        self.device_id = device_id

    def as_dict(self) -> Dict[str, Any]:
        return {
            'property': self.property,
            'device_id': self.device_id,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeleteDevicePropertyRequest':
        return DeleteDevicePropertyRequest(**DeleteDevicePropertyRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeleteDevicePropertyRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        DeleteDevicePropertyRequest.lib = library.xinput_deletedeviceproperty
        DeleteDevicePropertyRequest.lib.restype = ctypes.c_uint32
        DeleteDevicePropertyRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8 * 3)


class DeleteDevicePropertyRequestCType(ctypes.Structure):
    """xinput DeleteDeviceProperty"""
    _fields_ = [
        ("property", ctypes.c_uint32),
        ("device_id", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


GetDevicePropertyRequestCookie = NewType('GetDevicePropertyRequestCookie', ctypes.c_uint32)


GetDevicePropertyRequestPacket = DataPacket((
    ('property', FixedDataPacketField(MARKER_UINT32)),
    ('type', FixedDataPacketField(MARKER_UINT32)),
    ('offset', FixedDataPacketField(MARKER_UINT32)),
    ('len', FixedDataPacketField(MARKER_UINT32)),
    ('device_id', FixedDataPacketField(MARKER_UINT8)),
    ('delete', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
))


class GetDevicePropertyRequest:
    OPCODE = 39

    __slots__ = ('property', 'type', 'offset', 'len', 'device_id', 'delete',)

    def __init__(
            self, *,
            property: Optional[int] = None,
            type: Optional[int] = None,
            offset: Optional[int] = None,
            len: Optional[int] = None,
            device_id: Optional[int] = None,
            delete: Optional[bool] = None,
    ) -> None:
        self.property = property
        self.type = type
        self.offset = offset
        self.len = len
        self.device_id = device_id
        self.delete = delete

    def as_dict(self) -> Dict[str, Any]:
        return {
            'property': self.property,
            'type': self.type,
            'offset': self.offset,
            'len': self.len,
            'device_id': self.device_id,
            'delete': self.delete,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetDevicePropertyRequest':
        return GetDevicePropertyRequest(**GetDevicePropertyRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetDevicePropertyRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, bool], GetDevicePropertyRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetDevicePropertyRequest.lib = library.xinput_getdeviceproperty
        GetDevicePropertyRequest.lib.restype = GetDevicePropertyRequestCookie
        GetDevicePropertyRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_int8, ctypes.c_uint8 * 2)


class GetDevicePropertyRequestCType(ctypes.Structure):
    """xinput GetDeviceProperty"""
    _fields_ = [
        ("property", ctypes.c_uint32),
        ("type", ctypes.c_uint32),
        ("offset", ctypes.c_uint32),
        ("len", ctypes.c_uint32),
        ("device_id", ctypes.c_uint8),
        ("delete", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 2),
    ]


GetDevicePropertyReplyReplyPacket = DataPacket((
    ('xi_reply_type', FixedDataPacketField(MARKER_UINT8)),
    ('type', FixedDataPacketField(MARKER_UINT32)),
    ('bytes_after', FixedDataPacketField(MARKER_UINT32)),
    ('num_items', FixedDataPacketField(MARKER_UINT32)),
    ('format', FixedDataPacketField(MARKER_UINT8)),
    ('device_id', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(10)),
    ('items', UnionDataPacketField(lambda d, c: d['format'], {
        PropertyFormatValues.V_8BITS: StructureDataPacketField((
            ('data8', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: d['num_items'], 0)),
            ('pad0', AlignedPadDataPacketField(4)),
        )),
        PropertyFormatValues.V_16BITS: StructureDataPacketField((
            ('data16', SimpleListDataPacketField(MARKER_UINT16, lambda d, c: d['num_items'], 0)),
            ('pad0', AlignedPadDataPacketField(4)),
        )),
        PropertyFormatValues.V_32BITS: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_items'], 0),
    }, 0)),
))


class GetDevicePropertyReplyReply:
    __slots__ = ('xi_reply_type', 'type', 'bytes_after', 'num_items', 'format', 'device_id', 'items',)

    def __init__(
            self, *,
            xi_reply_type: Optional[int] = None,
            type: Optional[int] = None,
            bytes_after: Optional[int] = None,
            num_items: Optional[int] = None,
            format: Optional[int] = None,
            device_id: Optional[int] = None,
            items: Optional[Mapping[str, PropertyFormatValues]] = None,
    ) -> None:
        self.xi_reply_type = xi_reply_type
        self.type = type
        self.bytes_after = bytes_after
        self.num_items = num_items
        self.format = format
        self.device_id = device_id
        self.items = items

    def as_dict(self) -> Dict[str, Any]:
        return {
            'xi_reply_type': self.xi_reply_type,
            'type': self.type,
            'bytes_after': self.bytes_after,
            'num_items': self.num_items,
            'format': self.format,
            'device_id': self.device_id,
            'items': self.items,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetDevicePropertyReplyReply':
        return GetDevicePropertyReplyReply(**GetDevicePropertyReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetDevicePropertyReplyReplyPacket.pack(**self.as_dict())


class GetDevicePropertyReplyReplyCType(ctypes.Structure):
    """xinput GetDeviceProperty_reply"""
    _fields_ = [
        ("xi_reply_type", ctypes.c_uint8),
        ("type", ctypes.c_uint32),
        ("bytes_after", ctypes.c_uint32),
        ("num_items", ctypes.c_uint32),
        ("format", ctypes.c_uint8),
        ("device_id", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 10),
        ("var_data", ctypes.c_void_p),
    ]


GroupInfoStructPacket = DataPacket((
    ('base', FixedDataPacketField(MARKER_UINT8)),
    ('latched', FixedDataPacketField(MARKER_UINT8)),
    ('locked', FixedDataPacketField(MARKER_UINT8)),
    ('effective', FixedDataPacketField(MARKER_UINT8)),
))


class GroupInfoStruct:
    __slots__ = ('base', 'latched', 'locked', 'effective',)

    def __init__(
            self, *,
            base: Optional[int] = None,
            latched: Optional[int] = None,
            locked: Optional[int] = None,
            effective: Optional[int] = None,
    ) -> None:
        self.base = base
        self.latched = latched
        self.locked = locked
        self.effective = effective

    def as_dict(self) -> Dict[str, Any]:
        return {
            'base': self.base,
            'latched': self.latched,
            'locked': self.locked,
            'effective': self.effective,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GroupInfoStruct':
        return GroupInfoStruct(**GroupInfoStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GroupInfoStructPacket.pack(**self.as_dict())


class GroupInfoStructCType(ctypes.Structure):
    """xinput GroupInfo"""
    _fields_ = [
        ("base", ctypes.c_uint8),
        ("latched", ctypes.c_uint8),
        ("locked", ctypes.c_uint8),
        ("effective", ctypes.c_uint8),
    ]


ModifierInfoStructPacket = DataPacket((
    ('base', FixedDataPacketField(MARKER_UINT32)),
    ('latched', FixedDataPacketField(MARKER_UINT32)),
    ('locked', FixedDataPacketField(MARKER_UINT32)),
    ('effective', FixedDataPacketField(MARKER_UINT32)),
))


class ModifierInfoStruct:
    __slots__ = ('base', 'latched', 'locked', 'effective',)

    def __init__(
            self, *,
            base: Optional[int] = None,
            latched: Optional[int] = None,
            locked: Optional[int] = None,
            effective: Optional[int] = None,
    ) -> None:
        self.base = base
        self.latched = latched
        self.locked = locked
        self.effective = effective

    def as_dict(self) -> Dict[str, Any]:
        return {
            'base': self.base,
            'latched': self.latched,
            'locked': self.locked,
            'effective': self.effective,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ModifierInfoStruct':
        return ModifierInfoStruct(**ModifierInfoStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ModifierInfoStructPacket.pack(**self.as_dict())


class ModifierInfoStructCType(ctypes.Structure):
    """xinput ModifierInfo"""
    _fields_ = [
        ("base", ctypes.c_uint32),
        ("latched", ctypes.c_uint32),
        ("locked", ctypes.c_uint32),
        ("effective", ctypes.c_uint32),
    ]


XiqueryPointerRequestCookie = NewType('XiqueryPointerRequestCookie', ctypes.c_uint32)


XiqueryPointerRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(2)),
))


class XiqueryPointerRequest:
    OPCODE = 40

    __slots__ = ('window', 'deviceid',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            deviceid: Optional[int] = None,
    ) -> None:
        self.window = window
        self.deviceid = deviceid

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'deviceid': self.deviceid,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'XiqueryPointerRequest':
        return XiqueryPointerRequest(**XiqueryPointerRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return XiqueryPointerRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], XiqueryPointerRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        XiqueryPointerRequest.lib = library.xinput_xiquerypointer
        XiqueryPointerRequest.lib.restype = XiqueryPointerRequestCookie
        XiqueryPointerRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8 * 2)


class XiqueryPointerRequestCType(ctypes.Structure):
    """xinput XIQueryPointer"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("deviceid", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 2),
    ]


XiqueryPointerReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('root', FixedDataPacketField(MARKER_UINT32)),
    ('child', FixedDataPacketField(MARKER_UINT32)),
    ('root_x', FixedDataPacketField(MARKER_UINT32)),
    ('root_y', FixedDataPacketField(MARKER_UINT32)),
    ('win_x', FixedDataPacketField(MARKER_UINT32)),
    ('win_y', FixedDataPacketField(MARKER_UINT32)),
    ('same_screen', FixedDataPacketField(MARKER_UINT8)),
    ('pad1', FixedPadDataPacketField(1)),
    ('buttons_len', FixedDataPacketField(MARKER_UINT16)),
    ('mods', FixedDataPacketField(MARKER_UINT32)),
    ('group', FixedDataPacketField(MARKER_UINT32)),
    ('buttons', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['buttons_len'], 0)),
))


class XiqueryPointerReplyReply:
    __slots__ = ('root', 'child', 'root_x', 'root_y', 'win_x', 'win_y', 'same_screen', 'buttons_len', 'mods', 'group', 'buttons',)

    def __init__(
            self, *,
            root: Optional[int] = None,
            child: Optional[int] = None,
            root_x: Optional[int] = None,
            root_y: Optional[int] = None,
            win_x: Optional[int] = None,
            win_y: Optional[int] = None,
            same_screen: Optional[bool] = None,
            buttons_len: Optional[int] = None,
            mods: Optional[int] = None,
            group: Optional[int] = None,
            buttons: Optional[Sequence[int]] = None,
    ) -> None:
        self.root = root
        self.child = child
        self.root_x = root_x
        self.root_y = root_y
        self.win_x = win_x
        self.win_y = win_y
        self.same_screen = same_screen
        self.buttons_len = buttons_len
        self.mods = mods
        self.group = group
        self.buttons = buttons

    def as_dict(self) -> Dict[str, Any]:
        return {
            'root': self.root,
            'child': self.child,
            'root_x': self.root_x,
            'root_y': self.root_y,
            'win_x': self.win_x,
            'win_y': self.win_y,
            'same_screen': self.same_screen,
            'buttons_len': self.buttons_len,
            'mods': self.mods,
            'group': self.group,
            'buttons': self.buttons,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'XiqueryPointerReplyReply':
        return XiqueryPointerReplyReply(**XiqueryPointerReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return XiqueryPointerReplyReplyPacket.pack(**self.as_dict())


class XiqueryPointerReplyReplyCType(ctypes.Structure):
    """xinput XIQueryPointer_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("root", ctypes.c_uint32),
        ("child", ctypes.c_uint32),
        ("root_x", ctypes.c_uint32),
        ("root_y", ctypes.c_uint32),
        ("win_x", ctypes.c_uint32),
        ("win_y", ctypes.c_uint32),
        ("same_screen", ctypes.c_int8),
        ("pad1", ctypes.c_uint8),
        ("buttons_len", ctypes.c_uint16),
        ("mods", ctypes.c_uint32),
        ("group", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


XiwarpPointerRequestPacket = DataPacket((
    ('src_win', FixedDataPacketField(MARKER_UINT32)),
    ('dst_win', FixedDataPacketField(MARKER_UINT32)),
    ('src_x', FixedDataPacketField(MARKER_UINT32)),
    ('src_y', FixedDataPacketField(MARKER_UINT32)),
    ('src_width', FixedDataPacketField(MARKER_UINT16)),
    ('src_height', FixedDataPacketField(MARKER_UINT16)),
    ('dst_x', FixedDataPacketField(MARKER_UINT32)),
    ('dst_y', FixedDataPacketField(MARKER_UINT32)),
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(2)),
))


class XiwarpPointerRequest:
    OPCODE = 41

    __slots__ = ('src_win', 'dst_win', 'src_x', 'src_y', 'src_width', 'src_height', 'dst_x', 'dst_y', 'deviceid',)

    def __init__(
            self, *,
            src_win: Optional[int] = None,
            dst_win: Optional[int] = None,
            src_x: Optional[int] = None,
            src_y: Optional[int] = None,
            src_width: Optional[int] = None,
            src_height: Optional[int] = None,
            dst_x: Optional[int] = None,
            dst_y: Optional[int] = None,
            deviceid: Optional[int] = None,
    ) -> None:
        self.src_win = src_win
        self.dst_win = dst_win
        self.src_x = src_x
        self.src_y = src_y
        self.src_width = src_width
        self.src_height = src_height
        self.dst_x = dst_x
        self.dst_y = dst_y
        self.deviceid = deviceid

    def as_dict(self) -> Dict[str, Any]:
        return {
            'src_win': self.src_win,
            'dst_win': self.dst_win,
            'src_x': self.src_x,
            'src_y': self.src_y,
            'src_width': self.src_width,
            'src_height': self.src_height,
            'dst_x': self.dst_x,
            'dst_y': self.dst_y,
            'deviceid': self.deviceid,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'XiwarpPointerRequest':
        return XiwarpPointerRequest(**XiwarpPointerRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return XiwarpPointerRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        XiwarpPointerRequest.lib = library.xinput_xiwarppointer
        XiwarpPointerRequest.lib.restype = ctypes.c_uint32
        XiwarpPointerRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8 * 2)


class XiwarpPointerRequestCType(ctypes.Structure):
    """xinput XIWarpPointer"""
    _fields_ = [
        ("src_win", ctypes.c_uint32),
        ("dst_win", ctypes.c_uint32),
        ("src_x", ctypes.c_uint32),
        ("src_y", ctypes.c_uint32),
        ("src_width", ctypes.c_uint16),
        ("src_height", ctypes.c_uint16),
        ("dst_x", ctypes.c_uint32),
        ("dst_y", ctypes.c_uint32),
        ("deviceid", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 2),
    ]


XichangeCursorRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('cursor', FixedDataPacketField(MARKER_UINT32)),
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(2)),
))


class XichangeCursorRequest:
    OPCODE = 42

    __slots__ = ('window', 'cursor', 'deviceid',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            cursor: Optional[int] = None,
            deviceid: Optional[int] = None,
    ) -> None:
        self.window = window
        self.cursor = cursor
        self.deviceid = deviceid

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'cursor': self.cursor,
            'deviceid': self.deviceid,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'XichangeCursorRequest':
        return XichangeCursorRequest(**XichangeCursorRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return XichangeCursorRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        XichangeCursorRequest.lib = library.xinput_xichangecursor
        XichangeCursorRequest.lib.restype = ctypes.c_uint32
        XichangeCursorRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8 * 2)


class XichangeCursorRequestCType(ctypes.Structure):
    """xinput XIChangeCursor"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("cursor", ctypes.c_uint32),
        ("deviceid", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 2),
    ]


AddMasterStructPacket = DataPacket((
    ('type', FixedDataPacketField(MARKER_UINT16)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('name_len', FixedDataPacketField(MARKER_UINT16)),
    ('send_core', FixedDataPacketField(MARKER_UINT8)),
    ('enable', FixedDataPacketField(MARKER_UINT8)),
    ('name', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['name_len'], 0)),
    ('pad0', AlignedPadDataPacketField(4)),
))


class AddMasterStruct:
    __slots__ = ('type', 'len', 'name_len', 'send_core', 'enable', 'name',)

    def __init__(
            self, *,
            type: Optional[int] = None,
            len: Optional[int] = None,
            name_len: Optional[int] = None,
            send_core: Optional[bool] = None,
            enable: Optional[bool] = None,
            name: Optional[Sequence[int]] = None,
    ) -> None:
        self.type = type
        self.len = len
        self.name_len = name_len
        self.send_core = send_core
        self.enable = enable
        self.name = name

    def as_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type,
            'len': self.len,
            'name_len': self.name_len,
            'send_core': self.send_core,
            'enable': self.enable,
            'name': self.name,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'AddMasterStruct':
        return AddMasterStruct(**AddMasterStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return AddMasterStructPacket.pack(**self.as_dict())


class AddMasterStructCType(ctypes.Structure):
    """xinput AddMaster"""
    _fields_ = [
        ("type", ctypes.c_uint16),
        ("len", ctypes.c_uint16),
        ("name_len", ctypes.c_uint16),
        ("send_core", ctypes.c_int8),
        ("enable", ctypes.c_int8),
        ("var_data", ctypes.c_void_p),
    ]


RemoveMasterStructPacket = DataPacket((
    ('type', FixedDataPacketField(MARKER_UINT16)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('return_mode', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('return_pointer', FixedDataPacketField(MARKER_UINT32)),
    ('return_keyboard', FixedDataPacketField(MARKER_UINT32)),
))


class RemoveMasterStruct:
    __slots__ = ('type', 'len', 'deviceid', 'return_mode', 'return_pointer', 'return_keyboard',)

    def __init__(
            self, *,
            type: Optional[int] = None,
            len: Optional[int] = None,
            deviceid: Optional[int] = None,
            return_mode: Optional[int] = None,
            return_pointer: Optional[int] = None,
            return_keyboard: Optional[int] = None,
    ) -> None:
        self.type = type
        self.len = len
        self.deviceid = deviceid
        self.return_mode = return_mode
        self.return_pointer = return_pointer
        self.return_keyboard = return_keyboard

    def as_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type,
            'len': self.len,
            'deviceid': self.deviceid,
            'return_mode': self.return_mode,
            'return_pointer': self.return_pointer,
            'return_keyboard': self.return_keyboard,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'RemoveMasterStruct':
        return RemoveMasterStruct(**RemoveMasterStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return RemoveMasterStructPacket.pack(**self.as_dict())


class RemoveMasterStructCType(ctypes.Structure):
    """xinput RemoveMaster"""
    _fields_ = [
        ("type", ctypes.c_uint16),
        ("len", ctypes.c_uint16),
        ("deviceid", ctypes.c_uint32),
        ("return_mode", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
        ("return_pointer", ctypes.c_uint32),
        ("return_keyboard", ctypes.c_uint32),
    ]


AttachSlaveStructPacket = DataPacket((
    ('type', FixedDataPacketField(MARKER_UINT16)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('master', FixedDataPacketField(MARKER_UINT32)),
))


class AttachSlaveStruct:
    __slots__ = ('type', 'len', 'deviceid', 'master',)

    def __init__(
            self, *,
            type: Optional[int] = None,
            len: Optional[int] = None,
            deviceid: Optional[int] = None,
            master: Optional[int] = None,
    ) -> None:
        self.type = type
        self.len = len
        self.deviceid = deviceid
        self.master = master

    def as_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type,
            'len': self.len,
            'deviceid': self.deviceid,
            'master': self.master,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'AttachSlaveStruct':
        return AttachSlaveStruct(**AttachSlaveStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return AttachSlaveStructPacket.pack(**self.as_dict())


class AttachSlaveStructCType(ctypes.Structure):
    """xinput AttachSlave"""
    _fields_ = [
        ("type", ctypes.c_uint16),
        ("len", ctypes.c_uint16),
        ("deviceid", ctypes.c_uint32),
        ("master", ctypes.c_uint32),
    ]


DetachSlaveStructPacket = DataPacket((
    ('type', FixedDataPacketField(MARKER_UINT16)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(2)),
))


class DetachSlaveStruct:
    __slots__ = ('type', 'len', 'deviceid',)

    def __init__(
            self, *,
            type: Optional[int] = None,
            len: Optional[int] = None,
            deviceid: Optional[int] = None,
    ) -> None:
        self.type = type
        self.len = len
        self.deviceid = deviceid

    def as_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type,
            'len': self.len,
            'deviceid': self.deviceid,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DetachSlaveStruct':
        return DetachSlaveStruct(**DetachSlaveStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DetachSlaveStructPacket.pack(**self.as_dict())


class DetachSlaveStructCType(ctypes.Structure):
    """xinput DetachSlave"""
    _fields_ = [
        ("type", ctypes.c_uint16),
        ("len", ctypes.c_uint16),
        ("deviceid", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 2),
    ]


HierarchyChangeStructPacket = DataPacket((
    ('type', FixedDataPacketField(MARKER_UINT16)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('data', UnionDataPacketField(lambda d, c: d['type'], {
        HierarchyChangeTypeValues.ADD_MASTER: StructureDataPacketField((
            ('name_len', FixedDataPacketField(MARKER_UINT16)),
            ('send_core', FixedDataPacketField(MARKER_UINT8)),
            ('enable', FixedDataPacketField(MARKER_UINT8)),
            ('name', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['name_len'], 0)),
            ('pad0', AlignedPadDataPacketField(4)),
        )),
        HierarchyChangeTypeValues.REMOVE_MASTER: StructureDataPacketField((
            ('deviceid', FixedDataPacketField(MARKER_UINT32)),
            ('return_mode', FixedDataPacketField(MARKER_UINT8)),
            ('pad0', FixedPadDataPacketField(1)),
            ('return_pointer', FixedDataPacketField(MARKER_UINT32)),
            ('return_keyboard', FixedDataPacketField(MARKER_UINT32)),
        )),
        HierarchyChangeTypeValues.ATTACH_SLAVE: StructureDataPacketField((
            ('deviceid', FixedDataPacketField(MARKER_UINT32)),
            ('master', FixedDataPacketField(MARKER_UINT32)),
        )),
        HierarchyChangeTypeValues.DETACH_SLAVE: StructureDataPacketField((
            ('deviceid', FixedDataPacketField(MARKER_UINT32)),
            ('pad0', FixedPadDataPacketField(2)),
        )),
    }, 0)),
))


class HierarchyChangeStruct:
    __slots__ = ('type', 'len', 'data',)

    def __init__(
            self, *,
            type: Optional[int] = None,
            len: Optional[int] = None,
            data: Optional[Mapping[str, HierarchyChangeTypeValues]] = None,
    ) -> None:
        self.type = type
        self.len = len
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type,
            'len': self.len,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'HierarchyChangeStruct':
        return HierarchyChangeStruct(**HierarchyChangeStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return HierarchyChangeStructPacket.pack(**self.as_dict())


class HierarchyChangeStructCType(ctypes.Structure):
    """xinput HierarchyChange"""
    _fields_ = [
        ("type", ctypes.c_uint16),
        ("len", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


XichangeHierarchyRequestPacket = DataPacket((
    ('num_changes', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
    ('changes', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_changes'], 0)),
))


class XichangeHierarchyRequest:
    OPCODE = 43

    __slots__ = ('num_changes', 'changes',)

    def __init__(
            self, *,
            num_changes: Optional[int] = None,
            changes: Optional[Sequence[int]] = None,
    ) -> None:
        self.num_changes = num_changes
        self.changes = changes

    def as_dict(self) -> Dict[str, Any]:
        return {
            'num_changes': self.num_changes,
            'changes': self.changes,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'XichangeHierarchyRequest':
        return XichangeHierarchyRequest(**XichangeHierarchyRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return XichangeHierarchyRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        XichangeHierarchyRequest.lib = library.xinput_xichangehierarchy
        XichangeHierarchyRequest.lib.restype = ctypes.c_uint32
        XichangeHierarchyRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint8 * 3, ctypes.c_void_p)


class XichangeHierarchyRequestCType(ctypes.Structure):
    """xinput XIChangeHierarchy"""
    _fields_ = [
        ("num_changes", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
        ("var_data", ctypes.c_void_p),
    ]


XisetClientPointerRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(2)),
))


class XisetClientPointerRequest:
    OPCODE = 44

    __slots__ = ('window', 'deviceid',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            deviceid: Optional[int] = None,
    ) -> None:
        self.window = window
        self.deviceid = deviceid

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'deviceid': self.deviceid,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'XisetClientPointerRequest':
        return XisetClientPointerRequest(**XisetClientPointerRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return XisetClientPointerRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        XisetClientPointerRequest.lib = library.xinput_xisetclientpointer
        XisetClientPointerRequest.lib.restype = ctypes.c_uint32
        XisetClientPointerRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8 * 2)


class XisetClientPointerRequestCType(ctypes.Structure):
    """xinput XISetClientPointer"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("deviceid", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 2),
    ]


XigetClientPointerRequestCookie = NewType('XigetClientPointerRequestCookie', ctypes.c_uint32)


XigetClientPointerRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class XigetClientPointerRequest:
    OPCODE = 45

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
    def from_data(inp: BinaryIO) -> 'XigetClientPointerRequest':
        return XigetClientPointerRequest(**XigetClientPointerRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return XigetClientPointerRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], XigetClientPointerRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        XigetClientPointerRequest.lib = library.xinput_xigetclientpointer
        XigetClientPointerRequest.lib.restype = XigetClientPointerRequestCookie
        XigetClientPointerRequest.lib.argstype = (ctypes.c_uint32,)


class XigetClientPointerRequestCType(ctypes.Structure):
    """xinput XIGetClientPointer"""
    _fields_ = [
        ("window", ctypes.c_uint32),
    ]


XigetClientPointerReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('set', FixedDataPacketField(MARKER_UINT8)),
    ('pad1', FixedPadDataPacketField(1)),
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('pad2', FixedPadDataPacketField(20)),
))


class XigetClientPointerReplyReply:
    __slots__ = ('set', 'deviceid',)

    def __init__(
            self, *,
            set: Optional[bool] = None,
            deviceid: Optional[int] = None,
    ) -> None:
        self.set = set
        self.deviceid = deviceid

    def as_dict(self) -> Dict[str, Any]:
        return {
            'set': self.set,
            'deviceid': self.deviceid,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'XigetClientPointerReplyReply':
        return XigetClientPointerReplyReply(**XigetClientPointerReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return XigetClientPointerReplyReplyPacket.pack(**self.as_dict())


class XigetClientPointerReplyReplyCType(ctypes.Structure):
    """xinput XIGetClientPointer_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("set", ctypes.c_int8),
        ("pad1", ctypes.c_uint8),
        ("deviceid", ctypes.c_uint32),
        ("pad2", ctypes.c_uint8 * 20),
    ]


EventMaskStructPacket = DataPacket((
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('mask_len', FixedDataPacketField(MARKER_UINT16)),
    ('mask', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['mask_len'], 0)),
))


class EventMaskStruct:
    __slots__ = ('deviceid', 'mask_len', 'mask',)

    def __init__(
            self, *,
            deviceid: Optional[int] = None,
            mask_len: Optional[int] = None,
            mask: Optional[Sequence[int]] = None,
    ) -> None:
        self.deviceid = deviceid
        self.mask_len = mask_len
        self.mask = mask

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceid': self.deviceid,
            'mask_len': self.mask_len,
            'mask': self.mask,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'EventMaskStruct':
        return EventMaskStruct(**EventMaskStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return EventMaskStructPacket.pack(**self.as_dict())


class EventMaskStructCType(ctypes.Structure):
    """xinput EventMask"""
    _fields_ = [
        ("deviceid", ctypes.c_uint32),
        ("mask_len", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


XiselectEventsRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('num_mask', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
    ('masks', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_mask'], 0)),
))


class XiselectEventsRequest:
    OPCODE = 46

    __slots__ = ('window', 'num_mask', 'masks',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            num_mask: Optional[int] = None,
            masks: Optional[Sequence[int]] = None,
    ) -> None:
        self.window = window
        self.num_mask = num_mask
        self.masks = masks

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'num_mask': self.num_mask,
            'masks': self.masks,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'XiselectEventsRequest':
        return XiselectEventsRequest(**XiselectEventsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return XiselectEventsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        XiselectEventsRequest.lib = library.xinput_xiselectevents
        XiselectEventsRequest.lib.restype = ctypes.c_uint32
        XiselectEventsRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint8 * 2, ctypes.c_void_p)


class XiselectEventsRequestCType(ctypes.Structure):
    """xinput XISelectEvents"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("num_mask", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


XiqueryVersionRequestCookie = NewType('XiqueryVersionRequestCookie', ctypes.c_uint32)


XiqueryVersionRequestPacket = DataPacket((
    ('major_version', FixedDataPacketField(MARKER_UINT16)),
    ('minor_version', FixedDataPacketField(MARKER_UINT16)),
))


class XiqueryVersionRequest:
    OPCODE = 47

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
    def from_data(inp: BinaryIO) -> 'XiqueryVersionRequest':
        return XiqueryVersionRequest(**XiqueryVersionRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return XiqueryVersionRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], XiqueryVersionRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        XiqueryVersionRequest.lib = library.xinput_xiqueryversion
        XiqueryVersionRequest.lib.restype = XiqueryVersionRequestCookie
        XiqueryVersionRequest.lib.argstype = (ctypes.c_uint16, ctypes.c_uint16)


class XiqueryVersionRequestCType(ctypes.Structure):
    """xinput XIQueryVersion"""
    _fields_ = [
        ("major_version", ctypes.c_uint16),
        ("minor_version", ctypes.c_uint16),
    ]


XiqueryVersionReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('major_version', FixedDataPacketField(MARKER_UINT16)),
    ('minor_version', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(20)),
))


class XiqueryVersionReplyReply:
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
    def from_data(inp: BinaryIO) -> 'XiqueryVersionReplyReply':
        return XiqueryVersionReplyReply(**XiqueryVersionReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return XiqueryVersionReplyReplyPacket.pack(**self.as_dict())


class XiqueryVersionReplyReplyCType(ctypes.Structure):
    """xinput XIQueryVersion_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("major_version", ctypes.c_uint16),
        ("minor_version", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 20),
    ]


ButtonClassStructPacket = DataPacket((
    ('type', FixedDataPacketField(MARKER_UINT16)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('sourceid', FixedDataPacketField(MARKER_UINT32)),
    ('num_buttons', FixedDataPacketField(MARKER_UINT16)),
    ('state', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: ((d['num_buttons']) + (31)) / (32), 0)),
    ('labels', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_buttons'], 0)),
))


class ButtonClassStruct:
    __slots__ = ('type', 'len', 'sourceid', 'num_buttons', 'state', 'labels',)

    def __init__(
            self, *,
            type: Optional[int] = None,
            len: Optional[int] = None,
            sourceid: Optional[int] = None,
            num_buttons: Optional[int] = None,
            state: Optional[Sequence[int]] = None,
            labels: Optional[Sequence[int]] = None,
    ) -> None:
        self.type = type
        self.len = len
        self.sourceid = sourceid
        self.num_buttons = num_buttons
        self.state = state
        self.labels = labels

    def as_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type,
            'len': self.len,
            'sourceid': self.sourceid,
            'num_buttons': self.num_buttons,
            'state': self.state,
            'labels': self.labels,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ButtonClassStruct':
        return ButtonClassStruct(**ButtonClassStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ButtonClassStructPacket.pack(**self.as_dict())


class ButtonClassStructCType(ctypes.Structure):
    """xinput ButtonClass"""
    _fields_ = [
        ("type", ctypes.c_uint16),
        ("len", ctypes.c_uint16),
        ("sourceid", ctypes.c_uint32),
        ("num_buttons", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


KeyClassStructPacket = DataPacket((
    ('type', FixedDataPacketField(MARKER_UINT16)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('sourceid', FixedDataPacketField(MARKER_UINT32)),
    ('num_keys', FixedDataPacketField(MARKER_UINT16)),
    ('keys', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_keys'], 0)),
))


class KeyClassStruct:
    __slots__ = ('type', 'len', 'sourceid', 'num_keys', 'keys',)

    def __init__(
            self, *,
            type: Optional[int] = None,
            len: Optional[int] = None,
            sourceid: Optional[int] = None,
            num_keys: Optional[int] = None,
            keys: Optional[Sequence[int]] = None,
    ) -> None:
        self.type = type
        self.len = len
        self.sourceid = sourceid
        self.num_keys = num_keys
        self.keys = keys

    def as_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type,
            'len': self.len,
            'sourceid': self.sourceid,
            'num_keys': self.num_keys,
            'keys': self.keys,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'KeyClassStruct':
        return KeyClassStruct(**KeyClassStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return KeyClassStructPacket.pack(**self.as_dict())


class KeyClassStructCType(ctypes.Structure):
    """xinput KeyClass"""
    _fields_ = [
        ("type", ctypes.c_uint16),
        ("len", ctypes.c_uint16),
        ("sourceid", ctypes.c_uint32),
        ("num_keys", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


ScrollClassStructPacket = DataPacket((
    ('type', FixedDataPacketField(MARKER_UINT16)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('sourceid', FixedDataPacketField(MARKER_UINT32)),
    ('number', FixedDataPacketField(MARKER_UINT16)),
    ('scroll_type', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
    ('flags', FixedDataPacketField(MARKER_UINT32)),
    ('increment', FixedDataPacketField(MARKER_UINT32)),
))


class ScrollClassStruct:
    __slots__ = ('type', 'len', 'sourceid', 'number', 'scroll_type', 'flags', 'increment',)

    def __init__(
            self, *,
            type: Optional[int] = None,
            len: Optional[int] = None,
            sourceid: Optional[int] = None,
            number: Optional[int] = None,
            scroll_type: Optional[int] = None,
            flags: Optional[int] = None,
            increment: Optional[int] = None,
    ) -> None:
        self.type = type
        self.len = len
        self.sourceid = sourceid
        self.number = number
        self.scroll_type = scroll_type
        self.flags = flags
        self.increment = increment

    def as_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type,
            'len': self.len,
            'sourceid': self.sourceid,
            'number': self.number,
            'scroll_type': self.scroll_type,
            'flags': self.flags,
            'increment': self.increment,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ScrollClassStruct':
        return ScrollClassStruct(**ScrollClassStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ScrollClassStructPacket.pack(**self.as_dict())


class ScrollClassStructCType(ctypes.Structure):
    """xinput ScrollClass"""
    _fields_ = [
        ("type", ctypes.c_uint16),
        ("len", ctypes.c_uint16),
        ("sourceid", ctypes.c_uint32),
        ("number", ctypes.c_uint16),
        ("scroll_type", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
        ("flags", ctypes.c_uint32),
        ("increment", ctypes.c_uint32),
    ]


TouchClassStructPacket = DataPacket((
    ('type', FixedDataPacketField(MARKER_UINT16)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('sourceid', FixedDataPacketField(MARKER_UINT32)),
    ('mode', FixedDataPacketField(MARKER_UINT8)),
    ('num_touches', FixedDataPacketField(MARKER_UINT8)),
))


class TouchClassStruct:
    __slots__ = ('type', 'len', 'sourceid', 'mode', 'num_touches',)

    def __init__(
            self, *,
            type: Optional[int] = None,
            len: Optional[int] = None,
            sourceid: Optional[int] = None,
            mode: Optional[int] = None,
            num_touches: Optional[int] = None,
    ) -> None:
        self.type = type
        self.len = len
        self.sourceid = sourceid
        self.mode = mode
        self.num_touches = num_touches

    def as_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type,
            'len': self.len,
            'sourceid': self.sourceid,
            'mode': self.mode,
            'num_touches': self.num_touches,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'TouchClassStruct':
        return TouchClassStruct(**TouchClassStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return TouchClassStructPacket.pack(**self.as_dict())


class TouchClassStructCType(ctypes.Structure):
    """xinput TouchClass"""
    _fields_ = [
        ("type", ctypes.c_uint16),
        ("len", ctypes.c_uint16),
        ("sourceid", ctypes.c_uint32),
        ("mode", ctypes.c_uint8),
        ("num_touches", ctypes.c_uint8),
    ]


GestureClassStructPacket = DataPacket((
    ('type', FixedDataPacketField(MARKER_UINT16)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('sourceid', FixedDataPacketField(MARKER_UINT32)),
    ('num_touches', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
))


class GestureClassStruct:
    __slots__ = ('type', 'len', 'sourceid', 'num_touches',)

    def __init__(
            self, *,
            type: Optional[int] = None,
            len: Optional[int] = None,
            sourceid: Optional[int] = None,
            num_touches: Optional[int] = None,
    ) -> None:
        self.type = type
        self.len = len
        self.sourceid = sourceid
        self.num_touches = num_touches

    def as_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type,
            'len': self.len,
            'sourceid': self.sourceid,
            'num_touches': self.num_touches,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GestureClassStruct':
        return GestureClassStruct(**GestureClassStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GestureClassStructPacket.pack(**self.as_dict())


class GestureClassStructCType(ctypes.Structure):
    """xinput GestureClass"""
    _fields_ = [
        ("type", ctypes.c_uint16),
        ("len", ctypes.c_uint16),
        ("sourceid", ctypes.c_uint32),
        ("num_touches", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
    ]


ValuatorClassStructPacket = DataPacket((
    ('type', FixedDataPacketField(MARKER_UINT16)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('sourceid', FixedDataPacketField(MARKER_UINT32)),
    ('number', FixedDataPacketField(MARKER_UINT16)),
    ('label', FixedDataPacketField(MARKER_UINT32)),
    ('min', FixedDataPacketField(MARKER_UINT32)),
    ('max', FixedDataPacketField(MARKER_UINT32)),
    ('value', FixedDataPacketField(MARKER_UINT32)),
    ('resolution', FixedDataPacketField(MARKER_UINT32)),
    ('mode', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class ValuatorClassStruct:
    __slots__ = ('type', 'len', 'sourceid', 'number', 'label', 'min', 'max', 'value', 'resolution', 'mode',)

    def __init__(
            self, *,
            type: Optional[int] = None,
            len: Optional[int] = None,
            sourceid: Optional[int] = None,
            number: Optional[int] = None,
            label: Optional[int] = None,
            min: Optional[int] = None,
            max: Optional[int] = None,
            value: Optional[int] = None,
            resolution: Optional[int] = None,
            mode: Optional[int] = None,
    ) -> None:
        self.type = type
        self.len = len
        self.sourceid = sourceid
        self.number = number
        self.label = label
        self.min = min
        self.max = max
        self.value = value
        self.resolution = resolution
        self.mode = mode

    def as_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type,
            'len': self.len,
            'sourceid': self.sourceid,
            'number': self.number,
            'label': self.label,
            'min': self.min,
            'max': self.max,
            'value': self.value,
            'resolution': self.resolution,
            'mode': self.mode,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ValuatorClassStruct':
        return ValuatorClassStruct(**ValuatorClassStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ValuatorClassStructPacket.pack(**self.as_dict())


class ValuatorClassStructCType(ctypes.Structure):
    """xinput ValuatorClass"""
    _fields_ = [
        ("type", ctypes.c_uint16),
        ("len", ctypes.c_uint16),
        ("sourceid", ctypes.c_uint32),
        ("number", ctypes.c_uint16),
        ("label", ctypes.c_uint32),
        ("min", ctypes.c_uint32),
        ("max", ctypes.c_uint32),
        ("value", ctypes.c_uint32),
        ("resolution", ctypes.c_uint32),
        ("mode", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


DeviceClassStructPacket = DataPacket((
    ('type', FixedDataPacketField(MARKER_UINT16)),
    ('len', FixedDataPacketField(MARKER_UINT16)),
    ('sourceid', FixedDataPacketField(MARKER_UINT32)),
    ('data', UnionDataPacketField(lambda d, c: d['type'], {
        DeviceClassTypeValues.KEY: StructureDataPacketField((
            ('num_keys', FixedDataPacketField(MARKER_UINT16)),
            ('keys', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_keys'], 0)),
        )),
        DeviceClassTypeValues.BUTTON: StructureDataPacketField((
            ('num_buttons', FixedDataPacketField(MARKER_UINT16)),
            ('state', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: ((d['num_buttons']) + (31)) / (32), 0)),
            ('labels', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_buttons'], 0)),
        )),
        DeviceClassTypeValues.VALUATOR: StructureDataPacketField((
            ('number', FixedDataPacketField(MARKER_UINT16)),
            ('label', FixedDataPacketField(MARKER_UINT32)),
            ('min', FixedDataPacketField(MARKER_UINT32)),
            ('max', FixedDataPacketField(MARKER_UINT32)),
            ('value', FixedDataPacketField(MARKER_UINT32)),
            ('resolution', FixedDataPacketField(MARKER_UINT32)),
            ('mode', FixedDataPacketField(MARKER_UINT8)),
            ('pad0', FixedPadDataPacketField(3)),
        )),
        DeviceClassTypeValues.SCROLL: StructureDataPacketField((
            ('number', FixedDataPacketField(MARKER_UINT16)),
            ('scroll_type', FixedDataPacketField(MARKER_UINT16)),
            ('pad0', FixedPadDataPacketField(2)),
            ('flags', FixedDataPacketField(MARKER_UINT32)),
            ('increment', FixedDataPacketField(MARKER_UINT32)),
        )),
        DeviceClassTypeValues.TOUCH: StructureDataPacketField((
            ('mode', FixedDataPacketField(MARKER_UINT8)),
            ('num_touches', FixedDataPacketField(MARKER_UINT8)),
        )),
        DeviceClassTypeValues.GESTURE: StructureDataPacketField((
            ('num_touches', FixedDataPacketField(MARKER_UINT8)),
            ('pad0', FixedPadDataPacketField(1)),
        )),
    }, 0)),
))


class DeviceClassStruct:
    __slots__ = ('type', 'len', 'sourceid', 'data',)

    def __init__(
            self, *,
            type: Optional[int] = None,
            len: Optional[int] = None,
            sourceid: Optional[int] = None,
            data: Optional[Mapping[str, DeviceClassTypeValues]] = None,
    ) -> None:
        self.type = type
        self.len = len
        self.sourceid = sourceid
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type,
            'len': self.len,
            'sourceid': self.sourceid,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeviceClassStruct':
        return DeviceClassStruct(**DeviceClassStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeviceClassStructPacket.pack(**self.as_dict())


class DeviceClassStructCType(ctypes.Structure):
    """xinput DeviceClass"""
    _fields_ = [
        ("type", ctypes.c_uint16),
        ("len", ctypes.c_uint16),
        ("sourceid", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


XideviceInfoStructPacket = DataPacket((
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('type', FixedDataPacketField(MARKER_UINT16)),
    ('attachment', FixedDataPacketField(MARKER_UINT32)),
    ('num_classes', FixedDataPacketField(MARKER_UINT16)),
    ('name_len', FixedDataPacketField(MARKER_UINT16)),
    ('enabled', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('name', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['name_len'], 0)),
    ('pad1', AlignedPadDataPacketField(4)),
    ('classes', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_classes'], 0)),
))


class XideviceInfoStruct:
    __slots__ = ('deviceid', 'type', 'attachment', 'num_classes', 'name_len', 'enabled', 'name', 'classes',)

    def __init__(
            self, *,
            deviceid: Optional[int] = None,
            type: Optional[int] = None,
            attachment: Optional[int] = None,
            num_classes: Optional[int] = None,
            name_len: Optional[int] = None,
            enabled: Optional[bool] = None,
            name: Optional[Sequence[int]] = None,
            classes: Optional[Sequence[int]] = None,
    ) -> None:
        self.deviceid = deviceid
        self.type = type
        self.attachment = attachment
        self.num_classes = num_classes
        self.name_len = name_len
        self.enabled = enabled
        self.name = name
        self.classes = classes

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceid': self.deviceid,
            'type': self.type,
            'attachment': self.attachment,
            'num_classes': self.num_classes,
            'name_len': self.name_len,
            'enabled': self.enabled,
            'name': self.name,
            'classes': self.classes,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'XideviceInfoStruct':
        return XideviceInfoStruct(**XideviceInfoStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return XideviceInfoStructPacket.pack(**self.as_dict())


class XideviceInfoStructCType(ctypes.Structure):
    """xinput XIDeviceInfo"""
    _fields_ = [
        ("deviceid", ctypes.c_uint32),
        ("type", ctypes.c_uint16),
        ("attachment", ctypes.c_uint32),
        ("num_classes", ctypes.c_uint16),
        ("name_len", ctypes.c_uint16),
        ("enabled", ctypes.c_int8),
        ("pad0", ctypes.c_uint8),
        ("var_data", ctypes.c_void_p),
    ]


XiqueryDeviceRequestCookie = NewType('XiqueryDeviceRequestCookie', ctypes.c_uint32)


XiqueryDeviceRequestPacket = DataPacket((
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(2)),
))


class XiqueryDeviceRequest:
    OPCODE = 48

    __slots__ = ('deviceid',)

    def __init__(
            self, *,
            deviceid: Optional[int] = None,
    ) -> None:
        self.deviceid = deviceid

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceid': self.deviceid,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'XiqueryDeviceRequest':
        return XiqueryDeviceRequest(**XiqueryDeviceRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return XiqueryDeviceRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], XiqueryDeviceRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        XiqueryDeviceRequest.lib = library.xinput_xiquerydevice
        XiqueryDeviceRequest.lib.restype = XiqueryDeviceRequestCookie
        XiqueryDeviceRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint8 * 2)


class XiqueryDeviceRequestCType(ctypes.Structure):
    """xinput XIQueryDevice"""
    _fields_ = [
        ("deviceid", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 2),
    ]


XiqueryDeviceReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('num_infos', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(22)),
    ('infos', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_infos'], 0)),
))


class XiqueryDeviceReplyReply:
    __slots__ = ('num_infos', 'infos',)

    def __init__(
            self, *,
            num_infos: Optional[int] = None,
            infos: Optional[Sequence[int]] = None,
    ) -> None:
        self.num_infos = num_infos
        self.infos = infos

    def as_dict(self) -> Dict[str, Any]:
        return {
            'num_infos': self.num_infos,
            'infos': self.infos,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'XiqueryDeviceReplyReply':
        return XiqueryDeviceReplyReply(**XiqueryDeviceReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return XiqueryDeviceReplyReplyPacket.pack(**self.as_dict())


class XiqueryDeviceReplyReplyCType(ctypes.Structure):
    """xinput XIQueryDevice_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("num_infos", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 22),
        ("var_data", ctypes.c_void_p),
    ]


XisetFocusRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(2)),
))


class XisetFocusRequest:
    OPCODE = 49

    __slots__ = ('window', 'time', 'deviceid',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            time: Optional[int] = None,
            deviceid: Optional[int] = None,
    ) -> None:
        self.window = window
        self.time = time
        self.deviceid = deviceid

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'time': self.time,
            'deviceid': self.deviceid,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'XisetFocusRequest':
        return XisetFocusRequest(**XisetFocusRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return XisetFocusRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        XisetFocusRequest.lib = library.xinput_xisetfocus
        XisetFocusRequest.lib.restype = ctypes.c_uint32
        XisetFocusRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8 * 2)


class XisetFocusRequestCType(ctypes.Structure):
    """xinput XISetFocus"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("time", ctypes.c_uint32),
        ("deviceid", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 2),
    ]


XigetFocusRequestCookie = NewType('XigetFocusRequestCookie', ctypes.c_uint32)


XigetFocusRequestPacket = DataPacket((
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(2)),
))


class XigetFocusRequest:
    OPCODE = 50

    __slots__ = ('deviceid',)

    def __init__(
            self, *,
            deviceid: Optional[int] = None,
    ) -> None:
        self.deviceid = deviceid

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceid': self.deviceid,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'XigetFocusRequest':
        return XigetFocusRequest(**XigetFocusRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return XigetFocusRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], XigetFocusRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        XigetFocusRequest.lib = library.xinput_xigetfocus
        XigetFocusRequest.lib.restype = XigetFocusRequestCookie
        XigetFocusRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint8 * 2)


class XigetFocusRequestCType(ctypes.Structure):
    """xinput XIGetFocus"""
    _fields_ = [
        ("deviceid", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 2),
    ]


XigetFocusReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('focus', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
))


class XigetFocusReplyReply:
    __slots__ = ('focus',)

    def __init__(
            self, *,
            focus: Optional[int] = None,
    ) -> None:
        self.focus = focus

    def as_dict(self) -> Dict[str, Any]:
        return {
            'focus': self.focus,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'XigetFocusReplyReply':
        return XigetFocusReplyReply(**XigetFocusReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return XigetFocusReplyReplyPacket.pack(**self.as_dict())


class XigetFocusReplyReplyCType(ctypes.Structure):
    """xinput XIGetFocus_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("focus", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
    ]


XigrabDeviceRequestCookie = NewType('XigrabDeviceRequestCookie', ctypes.c_uint32)


XigrabDeviceRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('cursor', FixedDataPacketField(MARKER_UINT32)),
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('mode', FixedDataPacketField(MARKER_UINT8)),
    ('paired_device_mode', FixedDataPacketField(MARKER_UINT8)),
    ('owner_events', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('mask_len', FixedDataPacketField(MARKER_UINT16)),
    ('mask', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['mask_len'], 0)),
))


class XigrabDeviceRequest:
    OPCODE = 51

    __slots__ = ('window', 'time', 'cursor', 'deviceid', 'mode', 'paired_device_mode', 'owner_events', 'mask_len', 'mask',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            time: Optional[int] = None,
            cursor: Optional[int] = None,
            deviceid: Optional[int] = None,
            mode: Optional[int] = None,
            paired_device_mode: Optional[int] = None,
            owner_events: Optional[bool] = None,
            mask_len: Optional[int] = None,
            mask: Optional[Sequence[int]] = None,
    ) -> None:
        self.window = window
        self.time = time
        self.cursor = cursor
        self.deviceid = deviceid
        self.mode = mode
        self.paired_device_mode = paired_device_mode
        self.owner_events = owner_events
        self.mask_len = mask_len
        self.mask = mask

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'time': self.time,
            'cursor': self.cursor,
            'deviceid': self.deviceid,
            'mode': self.mode,
            'paired_device_mode': self.paired_device_mode,
            'owner_events': self.owner_events,
            'mask_len': self.mask_len,
            'mask': self.mask,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'XigrabDeviceRequest':
        return XigrabDeviceRequest(**XigrabDeviceRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return XigrabDeviceRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, bool, int, Sequence[int]], XigrabDeviceRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        XigrabDeviceRequest.lib = library.xinput_xigrabdevice
        XigrabDeviceRequest.lib.restype = XigrabDeviceRequestCookie
        XigrabDeviceRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_int8, ctypes.c_uint8, ctypes.c_uint16, ctypes.c_void_p)


class XigrabDeviceRequestCType(ctypes.Structure):
    """xinput XIGrabDevice"""
    _fields_ = [
        ("window", ctypes.c_uint32),
        ("time", ctypes.c_uint32),
        ("cursor", ctypes.c_uint32),
        ("deviceid", ctypes.c_uint32),
        ("mode", ctypes.c_uint8),
        ("paired_device_mode", ctypes.c_uint8),
        ("owner_events", ctypes.c_int8),
        ("pad0", ctypes.c_uint8),
        ("mask_len", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


XigrabDeviceReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('status', FixedDataPacketField(MARKER_UINT8)),
    ('pad1', FixedPadDataPacketField(23)),
))


class XigrabDeviceReplyReply:
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
    def from_data(inp: BinaryIO) -> 'XigrabDeviceReplyReply':
        return XigrabDeviceReplyReply(**XigrabDeviceReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return XigrabDeviceReplyReplyPacket.pack(**self.as_dict())


class XigrabDeviceReplyReplyCType(ctypes.Structure):
    """xinput XIGrabDevice_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("status", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 23),
    ]


XiungrabDeviceRequestPacket = DataPacket((
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(2)),
))


class XiungrabDeviceRequest:
    OPCODE = 52

    __slots__ = ('time', 'deviceid',)

    def __init__(
            self, *,
            time: Optional[int] = None,
            deviceid: Optional[int] = None,
    ) -> None:
        self.time = time
        self.deviceid = deviceid

    def as_dict(self) -> Dict[str, Any]:
        return {
            'time': self.time,
            'deviceid': self.deviceid,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'XiungrabDeviceRequest':
        return XiungrabDeviceRequest(**XiungrabDeviceRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return XiungrabDeviceRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        XiungrabDeviceRequest.lib = library.xinput_xiungrabdevice
        XiungrabDeviceRequest.lib.restype = ctypes.c_uint32
        XiungrabDeviceRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8 * 2)


class XiungrabDeviceRequestCType(ctypes.Structure):
    """xinput XIUngrabDevice"""
    _fields_ = [
        ("time", ctypes.c_uint32),
        ("deviceid", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 2),
    ]


XiallowEventsRequestPacket = DataPacket((
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('event_mode', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('touchid', FixedDataPacketField(MARKER_UINT32)),
    ('grab_window', FixedDataPacketField(MARKER_UINT32)),
))


class XiallowEventsRequest:
    OPCODE = 53

    __slots__ = ('time', 'deviceid', 'event_mode', 'touchid', 'grab_window',)

    def __init__(
            self, *,
            time: Optional[int] = None,
            deviceid: Optional[int] = None,
            event_mode: Optional[int] = None,
            touchid: Optional[int] = None,
            grab_window: Optional[int] = None,
    ) -> None:
        self.time = time
        self.deviceid = deviceid
        self.event_mode = event_mode
        self.touchid = touchid
        self.grab_window = grab_window

    def as_dict(self) -> Dict[str, Any]:
        return {
            'time': self.time,
            'deviceid': self.deviceid,
            'event_mode': self.event_mode,
            'touchid': self.touchid,
            'grab_window': self.grab_window,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'XiallowEventsRequest':
        return XiallowEventsRequest(**XiallowEventsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return XiallowEventsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        XiallowEventsRequest.lib = library.xinput_xiallowevents
        XiallowEventsRequest.lib.restype = ctypes.c_uint32
        XiallowEventsRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32)


class XiallowEventsRequestCType(ctypes.Structure):
    """xinput XIAllowEvents"""
    _fields_ = [
        ("time", ctypes.c_uint32),
        ("deviceid", ctypes.c_uint32),
        ("event_mode", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
        ("touchid", ctypes.c_uint32),
        ("grab_window", ctypes.c_uint32),
    ]


GrabModifierInfoStructPacket = DataPacket((
    ('modifiers', FixedDataPacketField(MARKER_UINT32)),
    ('status', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class GrabModifierInfoStruct:
    __slots__ = ('modifiers', 'status',)

    def __init__(
            self, *,
            modifiers: Optional[int] = None,
            status: Optional[int] = None,
    ) -> None:
        self.modifiers = modifiers
        self.status = status

    def as_dict(self) -> Dict[str, Any]:
        return {
            'modifiers': self.modifiers,
            'status': self.status,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GrabModifierInfoStruct':
        return GrabModifierInfoStruct(**GrabModifierInfoStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GrabModifierInfoStructPacket.pack(**self.as_dict())


class GrabModifierInfoStructCType(ctypes.Structure):
    """xinput GrabModifierInfo"""
    _fields_ = [
        ("modifiers", ctypes.c_uint32),
        ("status", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


XipassiveGrabDeviceRequestCookie = NewType('XipassiveGrabDeviceRequestCookie', ctypes.c_uint32)


XipassiveGrabDeviceRequestPacket = DataPacket((
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('grab_window', FixedDataPacketField(MARKER_UINT32)),
    ('cursor', FixedDataPacketField(MARKER_UINT32)),
    ('detail', FixedDataPacketField(MARKER_UINT32)),
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('num_modifiers', FixedDataPacketField(MARKER_UINT16)),
    ('mask_len', FixedDataPacketField(MARKER_UINT16)),
    ('grab_type', FixedDataPacketField(MARKER_UINT8)),
    ('grab_mode', FixedDataPacketField(MARKER_UINT8)),
    ('paired_device_mode', FixedDataPacketField(MARKER_UINT8)),
    ('owner_events', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
    ('mask', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['mask_len'], 0)),
    ('modifiers', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_modifiers'], 0)),
))


class XipassiveGrabDeviceRequest:
    OPCODE = 54

    __slots__ = ('time', 'grab_window', 'cursor', 'detail', 'deviceid', 'num_modifiers', 'mask_len', 'grab_type', 'grab_mode', 'paired_device_mode', 'owner_events', 'mask', 'modifiers',)

    def __init__(
            self, *,
            time: Optional[int] = None,
            grab_window: Optional[int] = None,
            cursor: Optional[int] = None,
            detail: Optional[int] = None,
            deviceid: Optional[int] = None,
            num_modifiers: Optional[int] = None,
            mask_len: Optional[int] = None,
            grab_type: Optional[int] = None,
            grab_mode: Optional[int] = None,
            paired_device_mode: Optional[int] = None,
            owner_events: Optional[bool] = None,
            mask: Optional[Sequence[int]] = None,
            modifiers: Optional[Sequence[int]] = None,
    ) -> None:
        self.time = time
        self.grab_window = grab_window
        self.cursor = cursor
        self.detail = detail
        self.deviceid = deviceid
        self.num_modifiers = num_modifiers
        self.mask_len = mask_len
        self.grab_type = grab_type
        self.grab_mode = grab_mode
        self.paired_device_mode = paired_device_mode
        self.owner_events = owner_events
        self.mask = mask
        self.modifiers = modifiers

    def as_dict(self) -> Dict[str, Any]:
        return {
            'time': self.time,
            'grab_window': self.grab_window,
            'cursor': self.cursor,
            'detail': self.detail,
            'deviceid': self.deviceid,
            'num_modifiers': self.num_modifiers,
            'mask_len': self.mask_len,
            'grab_type': self.grab_type,
            'grab_mode': self.grab_mode,
            'paired_device_mode': self.paired_device_mode,
            'owner_events': self.owner_events,
            'mask': self.mask,
            'modifiers': self.modifiers,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'XipassiveGrabDeviceRequest':
        return XipassiveGrabDeviceRequest(**XipassiveGrabDeviceRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return XipassiveGrabDeviceRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, int, int, int, bool, Sequence[int], Sequence[int]], XipassiveGrabDeviceRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        XipassiveGrabDeviceRequest.lib = library.xinput_xipassivegrabdevice
        XipassiveGrabDeviceRequest.lib.restype = XipassiveGrabDeviceRequestCookie
        XipassiveGrabDeviceRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_int8, ctypes.c_uint8 * 2, ctypes.c_void_p, ctypes.c_void_p)


class XipassiveGrabDeviceRequestCType(ctypes.Structure):
    """xinput XIPassiveGrabDevice"""
    _fields_ = [
        ("time", ctypes.c_uint32),
        ("grab_window", ctypes.c_uint32),
        ("cursor", ctypes.c_uint32),
        ("detail", ctypes.c_uint32),
        ("deviceid", ctypes.c_uint32),
        ("num_modifiers", ctypes.c_uint16),
        ("mask_len", ctypes.c_uint16),
        ("grab_type", ctypes.c_uint8),
        ("grab_mode", ctypes.c_uint8),
        ("paired_device_mode", ctypes.c_uint8),
        ("owner_events", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


XipassiveGrabDeviceReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('num_modifiers', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(22)),
    ('modifiers', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_modifiers'], 0)),
))


class XipassiveGrabDeviceReplyReply:
    __slots__ = ('num_modifiers', 'modifiers',)

    def __init__(
            self, *,
            num_modifiers: Optional[int] = None,
            modifiers: Optional[Sequence[int]] = None,
    ) -> None:
        self.num_modifiers = num_modifiers
        self.modifiers = modifiers

    def as_dict(self) -> Dict[str, Any]:
        return {
            'num_modifiers': self.num_modifiers,
            'modifiers': self.modifiers,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'XipassiveGrabDeviceReplyReply':
        return XipassiveGrabDeviceReplyReply(**XipassiveGrabDeviceReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return XipassiveGrabDeviceReplyReplyPacket.pack(**self.as_dict())


class XipassiveGrabDeviceReplyReplyCType(ctypes.Structure):
    """xinput XIPassiveGrabDevice_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("num_modifiers", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 22),
        ("var_data", ctypes.c_void_p),
    ]


XipassiveUngrabDeviceRequestPacket = DataPacket((
    ('grab_window', FixedDataPacketField(MARKER_UINT32)),
    ('detail', FixedDataPacketField(MARKER_UINT32)),
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('num_modifiers', FixedDataPacketField(MARKER_UINT16)),
    ('grab_type', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
    ('modifiers', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_modifiers'], 0)),
))


class XipassiveUngrabDeviceRequest:
    OPCODE = 55

    __slots__ = ('grab_window', 'detail', 'deviceid', 'num_modifiers', 'grab_type', 'modifiers',)

    def __init__(
            self, *,
            grab_window: Optional[int] = None,
            detail: Optional[int] = None,
            deviceid: Optional[int] = None,
            num_modifiers: Optional[int] = None,
            grab_type: Optional[int] = None,
            modifiers: Optional[Sequence[int]] = None,
    ) -> None:
        self.grab_window = grab_window
        self.detail = detail
        self.deviceid = deviceid
        self.num_modifiers = num_modifiers
        self.grab_type = grab_type
        self.modifiers = modifiers

    def as_dict(self) -> Dict[str, Any]:
        return {
            'grab_window': self.grab_window,
            'detail': self.detail,
            'deviceid': self.deviceid,
            'num_modifiers': self.num_modifiers,
            'grab_type': self.grab_type,
            'modifiers': self.modifiers,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'XipassiveUngrabDeviceRequest':
        return XipassiveUngrabDeviceRequest(**XipassiveUngrabDeviceRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return XipassiveUngrabDeviceRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        XipassiveUngrabDeviceRequest.lib = library.xinput_xipassiveungrabdevice
        XipassiveUngrabDeviceRequest.lib.restype = ctypes.c_uint32
        XipassiveUngrabDeviceRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint8, ctypes.c_uint8 * 3, ctypes.c_void_p)


class XipassiveUngrabDeviceRequestCType(ctypes.Structure):
    """xinput XIPassiveUngrabDevice"""
    _fields_ = [
        ("grab_window", ctypes.c_uint32),
        ("detail", ctypes.c_uint32),
        ("deviceid", ctypes.c_uint32),
        ("num_modifiers", ctypes.c_uint16),
        ("grab_type", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
        ("var_data", ctypes.c_void_p),
    ]


XilistPropertiesRequestCookie = NewType('XilistPropertiesRequestCookie', ctypes.c_uint32)


XilistPropertiesRequestPacket = DataPacket((
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(2)),
))


class XilistPropertiesRequest:
    OPCODE = 56

    __slots__ = ('deviceid',)

    def __init__(
            self, *,
            deviceid: Optional[int] = None,
    ) -> None:
        self.deviceid = deviceid

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceid': self.deviceid,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'XilistPropertiesRequest':
        return XilistPropertiesRequest(**XilistPropertiesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return XilistPropertiesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], XilistPropertiesRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        XilistPropertiesRequest.lib = library.xinput_xilistproperties
        XilistPropertiesRequest.lib.restype = XilistPropertiesRequestCookie
        XilistPropertiesRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint8 * 2)


class XilistPropertiesRequestCType(ctypes.Structure):
    """xinput XIListProperties"""
    _fields_ = [
        ("deviceid", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 2),
    ]


XilistPropertiesReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('num_properties', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(22)),
    ('properties', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_properties'], 0)),
))


class XilistPropertiesReplyReply:
    __slots__ = ('num_properties', 'properties',)

    def __init__(
            self, *,
            num_properties: Optional[int] = None,
            properties: Optional[Sequence[int]] = None,
    ) -> None:
        self.num_properties = num_properties
        self.properties = properties

    def as_dict(self) -> Dict[str, Any]:
        return {
            'num_properties': self.num_properties,
            'properties': self.properties,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'XilistPropertiesReplyReply':
        return XilistPropertiesReplyReply(**XilistPropertiesReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return XilistPropertiesReplyReplyPacket.pack(**self.as_dict())


class XilistPropertiesReplyReplyCType(ctypes.Structure):
    """xinput XIListProperties_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("num_properties", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 22),
        ("var_data", ctypes.c_void_p),
    ]


XichangePropertyRequestPacket = DataPacket((
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('mode', FixedDataPacketField(MARKER_UINT8)),
    ('format', FixedDataPacketField(MARKER_UINT8)),
    ('property', FixedDataPacketField(MARKER_UINT32)),
    ('type', FixedDataPacketField(MARKER_UINT32)),
    ('num_items', FixedDataPacketField(MARKER_UINT32)),
    ('items', UnionDataPacketField(lambda d, c: d['format'], {
        PropertyFormatValues.V_8BITS: StructureDataPacketField((
            ('data8', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: d['num_items'], 0)),
            ('pad0', AlignedPadDataPacketField(4)),
        )),
        PropertyFormatValues.V_16BITS: StructureDataPacketField((
            ('data16', SimpleListDataPacketField(MARKER_UINT16, lambda d, c: d['num_items'], 0)),
            ('pad0', AlignedPadDataPacketField(4)),
        )),
        PropertyFormatValues.V_32BITS: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_items'], 0),
    }, 0)),
))


class XichangePropertyRequest:
    OPCODE = 57

    __slots__ = ('deviceid', 'mode', 'format', 'property', 'type', 'num_items', 'items',)

    def __init__(
            self, *,
            deviceid: Optional[int] = None,
            mode: Optional[int] = None,
            format: Optional[int] = None,
            property: Optional[int] = None,
            type: Optional[int] = None,
            num_items: Optional[int] = None,
            items: Optional[Mapping[str, PropertyFormatValues]] = None,
    ) -> None:
        self.deviceid = deviceid
        self.mode = mode
        self.format = format
        self.property = property
        self.type = type
        self.num_items = num_items
        self.items = items

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceid': self.deviceid,
            'mode': self.mode,
            'format': self.format,
            'property': self.property,
            'type': self.type,
            'num_items': self.num_items,
            'items': self.items,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'XichangePropertyRequest':
        return XichangePropertyRequest(**XichangePropertyRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return XichangePropertyRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, Mapping[str, PropertyFormatValues]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        XichangePropertyRequest.lib = library.xinput_xichangeproperty
        XichangePropertyRequest.lib.restype = ctypes.c_uint32
        XichangePropertyRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)


class XichangePropertyRequestCType(ctypes.Structure):
    """xinput XIChangeProperty"""
    _fields_ = [
        ("deviceid", ctypes.c_uint32),
        ("mode", ctypes.c_uint8),
        ("format", ctypes.c_uint8),
        ("property", ctypes.c_uint32),
        ("type", ctypes.c_uint32),
        ("num_items", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


XideletePropertyRequestPacket = DataPacket((
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(2)),
    ('property', FixedDataPacketField(MARKER_UINT32)),
))


class XideletePropertyRequest:
    OPCODE = 58

    __slots__ = ('deviceid', 'property',)

    def __init__(
            self, *,
            deviceid: Optional[int] = None,
            property: Optional[int] = None,
    ) -> None:
        self.deviceid = deviceid
        self.property = property

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceid': self.deviceid,
            'property': self.property,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'XideletePropertyRequest':
        return XideletePropertyRequest(**XideletePropertyRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return XideletePropertyRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        XideletePropertyRequest.lib = library.xinput_xideleteproperty
        XideletePropertyRequest.lib.restype = ctypes.c_uint32
        XideletePropertyRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint8 * 2, ctypes.c_uint32)


class XideletePropertyRequestCType(ctypes.Structure):
    """xinput XIDeleteProperty"""
    _fields_ = [
        ("deviceid", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 2),
        ("property", ctypes.c_uint32),
    ]


XigetPropertyRequestCookie = NewType('XigetPropertyRequestCookie', ctypes.c_uint32)


XigetPropertyRequestPacket = DataPacket((
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('delete', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('property', FixedDataPacketField(MARKER_UINT32)),
    ('type', FixedDataPacketField(MARKER_UINT32)),
    ('offset', FixedDataPacketField(MARKER_UINT32)),
    ('len', FixedDataPacketField(MARKER_UINT32)),
))


class XigetPropertyRequest:
    OPCODE = 59

    __slots__ = ('deviceid', 'delete', 'property', 'type', 'offset', 'len',)

    def __init__(
            self, *,
            deviceid: Optional[int] = None,
            delete: Optional[bool] = None,
            property: Optional[int] = None,
            type: Optional[int] = None,
            offset: Optional[int] = None,
            len: Optional[int] = None,
    ) -> None:
        self.deviceid = deviceid
        self.delete = delete
        self.property = property
        self.type = type
        self.offset = offset
        self.len = len

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceid': self.deviceid,
            'delete': self.delete,
            'property': self.property,
            'type': self.type,
            'offset': self.offset,
            'len': self.len,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'XigetPropertyRequest':
        return XigetPropertyRequest(**XigetPropertyRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return XigetPropertyRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, bool, int, int, int, int], XigetPropertyRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        XigetPropertyRequest.lib = library.xinput_xigetproperty
        XigetPropertyRequest.lib.restype = XigetPropertyRequestCookie
        XigetPropertyRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_int8, ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class XigetPropertyRequestCType(ctypes.Structure):
    """xinput XIGetProperty"""
    _fields_ = [
        ("deviceid", ctypes.c_uint32),
        ("delete", ctypes.c_int8),
        ("pad0", ctypes.c_uint8),
        ("property", ctypes.c_uint32),
        ("type", ctypes.c_uint32),
        ("offset", ctypes.c_uint32),
        ("len", ctypes.c_uint32),
    ]


XigetPropertyReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('type', FixedDataPacketField(MARKER_UINT32)),
    ('bytes_after', FixedDataPacketField(MARKER_UINT32)),
    ('num_items', FixedDataPacketField(MARKER_UINT32)),
    ('format', FixedDataPacketField(MARKER_UINT8)),
    ('pad1', FixedPadDataPacketField(11)),
    ('items', UnionDataPacketField(lambda d, c: d['format'], {
        PropertyFormatValues.V_8BITS: StructureDataPacketField((
            ('data8', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: d['num_items'], 0)),
            ('pad0', AlignedPadDataPacketField(4)),
        )),
        PropertyFormatValues.V_16BITS: StructureDataPacketField((
            ('data16', SimpleListDataPacketField(MARKER_UINT16, lambda d, c: d['num_items'], 0)),
            ('pad0', AlignedPadDataPacketField(4)),
        )),
        PropertyFormatValues.V_32BITS: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_items'], 0),
    }, 0)),
))


class XigetPropertyReplyReply:
    __slots__ = ('type', 'bytes_after', 'num_items', 'format', 'items',)

    def __init__(
            self, *,
            type: Optional[int] = None,
            bytes_after: Optional[int] = None,
            num_items: Optional[int] = None,
            format: Optional[int] = None,
            items: Optional[Mapping[str, PropertyFormatValues]] = None,
    ) -> None:
        self.type = type
        self.bytes_after = bytes_after
        self.num_items = num_items
        self.format = format
        self.items = items

    def as_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type,
            'bytes_after': self.bytes_after,
            'num_items': self.num_items,
            'format': self.format,
            'items': self.items,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'XigetPropertyReplyReply':
        return XigetPropertyReplyReply(**XigetPropertyReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return XigetPropertyReplyReplyPacket.pack(**self.as_dict())


class XigetPropertyReplyReplyCType(ctypes.Structure):
    """xinput XIGetProperty_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("type", ctypes.c_uint32),
        ("bytes_after", ctypes.c_uint32),
        ("num_items", ctypes.c_uint32),
        ("format", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 11),
        ("var_data", ctypes.c_void_p),
    ]


XigetSelectedEventsRequestCookie = NewType('XigetSelectedEventsRequestCookie', ctypes.c_uint32)


XigetSelectedEventsRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class XigetSelectedEventsRequest:
    OPCODE = 60

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
    def from_data(inp: BinaryIO) -> 'XigetSelectedEventsRequest':
        return XigetSelectedEventsRequest(**XigetSelectedEventsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return XigetSelectedEventsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], XigetSelectedEventsRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        XigetSelectedEventsRequest.lib = library.xinput_xigetselectedevents
        XigetSelectedEventsRequest.lib.restype = XigetSelectedEventsRequestCookie
        XigetSelectedEventsRequest.lib.argstype = (ctypes.c_uint32,)


class XigetSelectedEventsRequestCType(ctypes.Structure):
    """xinput XIGetSelectedEvents"""
    _fields_ = [
        ("window", ctypes.c_uint32),
    ]


XigetSelectedEventsReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('num_masks', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(22)),
    ('masks', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_masks'], 0)),
))


class XigetSelectedEventsReplyReply:
    __slots__ = ('num_masks', 'masks',)

    def __init__(
            self, *,
            num_masks: Optional[int] = None,
            masks: Optional[Sequence[int]] = None,
    ) -> None:
        self.num_masks = num_masks
        self.masks = masks

    def as_dict(self) -> Dict[str, Any]:
        return {
            'num_masks': self.num_masks,
            'masks': self.masks,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'XigetSelectedEventsReplyReply':
        return XigetSelectedEventsReplyReply(**XigetSelectedEventsReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return XigetSelectedEventsReplyReplyPacket.pack(**self.as_dict())


class XigetSelectedEventsReplyReplyCType(ctypes.Structure):
    """xinput XIGetSelectedEvents_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("num_masks", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 22),
        ("var_data", ctypes.c_void_p),
    ]


BarrierReleasePointerInfoStructPacket = DataPacket((
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(2)),
    ('barrier', FixedDataPacketField(MARKER_UINT32)),
    ('eventid', FixedDataPacketField(MARKER_UINT32)),
))


class BarrierReleasePointerInfoStruct:
    __slots__ = ('deviceid', 'barrier', 'eventid',)

    def __init__(
            self, *,
            deviceid: Optional[int] = None,
            barrier: Optional[int] = None,
            eventid: Optional[int] = None,
    ) -> None:
        self.deviceid = deviceid
        self.barrier = barrier
        self.eventid = eventid

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceid': self.deviceid,
            'barrier': self.barrier,
            'eventid': self.eventid,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'BarrierReleasePointerInfoStruct':
        return BarrierReleasePointerInfoStruct(**BarrierReleasePointerInfoStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return BarrierReleasePointerInfoStructPacket.pack(**self.as_dict())


class BarrierReleasePointerInfoStructCType(ctypes.Structure):
    """xinput BarrierReleasePointerInfo"""
    _fields_ = [
        ("deviceid", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 2),
        ("barrier", ctypes.c_uint32),
        ("eventid", ctypes.c_uint32),
    ]


XibarrierReleasePointerRequestPacket = DataPacket((
    ('num_barriers', FixedDataPacketField(MARKER_UINT32)),
    ('barriers', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_barriers'], 0)),
))


class XibarrierReleasePointerRequest:
    OPCODE = 61

    __slots__ = ('num_barriers', 'barriers',)

    def __init__(
            self, *,
            num_barriers: Optional[int] = None,
            barriers: Optional[Sequence[int]] = None,
    ) -> None:
        self.num_barriers = num_barriers
        self.barriers = barriers

    def as_dict(self) -> Dict[str, Any]:
        return {
            'num_barriers': self.num_barriers,
            'barriers': self.barriers,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'XibarrierReleasePointerRequest':
        return XibarrierReleasePointerRequest(**XibarrierReleasePointerRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return XibarrierReleasePointerRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        XibarrierReleasePointerRequest.lib = library.xinput_xibarrierreleasepointer
        XibarrierReleasePointerRequest.lib.restype = ctypes.c_uint32
        XibarrierReleasePointerRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_void_p)


class XibarrierReleasePointerRequestCType(ctypes.Structure):
    """xinput XIBarrierReleasePointer"""
    _fields_ = [
        ("num_barriers", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


DeviceValuatorEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('device_id', FixedDataPacketField(MARKER_UINT8)),
    ('device_state', FixedDataPacketField(MARKER_UINT16)),
    ('num_valuators', FixedDataPacketField(MARKER_UINT8)),
    ('first_valuator', FixedDataPacketField(MARKER_UINT8)),
    ('valuators', SimpleListDataPacketField(MARKER_INT32, lambda d, c: 6, 0)),
))


class DeviceValuatorEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'device_id', 'device_state', 'num_valuators', 'first_valuator', 'valuators',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            device_id: Optional[int] = None,
            device_state: Optional[int] = None,
            num_valuators: Optional[int] = None,
            first_valuator: Optional[int] = None,
            valuators: Optional[Sequence[int]] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.device_id = device_id
        self.device_state = device_state
        self.num_valuators = num_valuators
        self.first_valuator = first_valuator
        self.valuators = valuators

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'device_id': self.device_id,
            'device_state': self.device_state,
            'num_valuators': self.num_valuators,
            'first_valuator': self.first_valuator,
            'valuators': self.valuators,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeviceValuatorEvent':
        return DeviceValuatorEvent(**DeviceValuatorEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeviceValuatorEventPacket.pack(**self.as_dict())


class DeviceValuatorEventCType(ctypes.Structure):
    """xinput DeviceValuator"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("device_id", ctypes.c_uint8),
        ("device_state", ctypes.c_uint16),
        ("num_valuators", ctypes.c_uint8),
        ("first_valuator", ctypes.c_uint8),
        ("var_data", ctypes.c_void_p),
    ]


DeviceKeyPressEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('detail', FixedDataPacketField(MARKER_INT8)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('root', FixedDataPacketField(MARKER_UINT32)),
    ('event', FixedDataPacketField(MARKER_UINT32)),
    ('child', FixedDataPacketField(MARKER_UINT32)),
    ('root_x', FixedDataPacketField(MARKER_INT16)),
    ('root_y', FixedDataPacketField(MARKER_INT16)),
    ('event_x', FixedDataPacketField(MARKER_INT16)),
    ('event_y', FixedDataPacketField(MARKER_INT16)),
    ('state', FixedDataPacketField(MARKER_UINT16)),
    ('same_screen', FixedDataPacketField(MARKER_UINT8)),
    ('device_id', FixedDataPacketField(MARKER_UINT8)),
))


class DeviceKeyPressEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'detail', 'time', 'root', 'event', 'child', 'root_x', 'root_y', 'event_x', 'event_y', 'state', 'same_screen', 'device_id',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            detail: Optional[int] = None,
            time: Optional[int] = None,
            root: Optional[int] = None,
            event: Optional[int] = None,
            child: Optional[int] = None,
            root_x: Optional[int] = None,
            root_y: Optional[int] = None,
            event_x: Optional[int] = None,
            event_y: Optional[int] = None,
            state: Optional[int] = None,
            same_screen: Optional[bool] = None,
            device_id: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.detail = detail
        self.time = time
        self.root = root
        self.event = event
        self.child = child
        self.root_x = root_x
        self.root_y = root_y
        self.event_x = event_x
        self.event_y = event_y
        self.state = state
        self.same_screen = same_screen
        self.device_id = device_id

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'detail': self.detail,
            'time': self.time,
            'root': self.root,
            'event': self.event,
            'child': self.child,
            'root_x': self.root_x,
            'root_y': self.root_y,
            'event_x': self.event_x,
            'event_y': self.event_y,
            'state': self.state,
            'same_screen': self.same_screen,
            'device_id': self.device_id,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeviceKeyPressEvent':
        return DeviceKeyPressEvent(**DeviceKeyPressEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeviceKeyPressEventPacket.pack(**self.as_dict())


class DeviceKeyPressEventCType(ctypes.Structure):
    """xinput DeviceKeyPress"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("detail", ctypes.c_int8),
        ("time", ctypes.c_uint32),
        ("root", ctypes.c_uint32),
        ("event", ctypes.c_uint32),
        ("child", ctypes.c_uint32),
        ("root_x", ctypes.c_int16),
        ("root_y", ctypes.c_int16),
        ("event_x", ctypes.c_int16),
        ("event_y", ctypes.c_int16),
        ("state", ctypes.c_uint16),
        ("same_screen", ctypes.c_int8),
        ("device_id", ctypes.c_uint8),
    ]


DeviceFocusInEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('detail', FixedDataPacketField(MARKER_INT8)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('mode', FixedDataPacketField(MARKER_INT8)),
    ('device_id', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(18)),
))


class DeviceFocusInEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'detail', 'time', 'window', 'mode', 'device_id',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            detail: Optional[int] = None,
            time: Optional[int] = None,
            window: Optional[int] = None,
            mode: Optional[int] = None,
            device_id: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.detail = detail
        self.time = time
        self.window = window
        self.mode = mode
        self.device_id = device_id

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'detail': self.detail,
            'time': self.time,
            'window': self.window,
            'mode': self.mode,
            'device_id': self.device_id,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeviceFocusInEvent':
        return DeviceFocusInEvent(**DeviceFocusInEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeviceFocusInEventPacket.pack(**self.as_dict())


class DeviceFocusInEventCType(ctypes.Structure):
    """xinput DeviceFocusIn"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("detail", ctypes.c_int8),
        ("time", ctypes.c_uint32),
        ("window", ctypes.c_uint32),
        ("mode", ctypes.c_int8),
        ("device_id", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 18),
    ]


DeviceStateNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('device_id', FixedDataPacketField(MARKER_INT8)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('num_keys', FixedDataPacketField(MARKER_UINT8)),
    ('num_buttons', FixedDataPacketField(MARKER_UINT8)),
    ('num_valuators', FixedDataPacketField(MARKER_UINT8)),
    ('classes_reported', FixedDataPacketField(MARKER_UINT8)),
    ('buttons', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: 4, 0)),
    ('keys', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: 4, 0)),
    ('valuators', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 3, 0)),
))


class DeviceStateNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'device_id', 'time', 'num_keys', 'num_buttons', 'num_valuators', 'classes_reported', 'buttons', 'keys', 'valuators',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            device_id: Optional[int] = None,
            time: Optional[int] = None,
            num_keys: Optional[int] = None,
            num_buttons: Optional[int] = None,
            num_valuators: Optional[int] = None,
            classes_reported: Optional[int] = None,
            buttons: Optional[Sequence[int]] = None,
            keys: Optional[Sequence[int]] = None,
            valuators: Optional[Sequence[int]] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.device_id = device_id
        self.time = time
        self.num_keys = num_keys
        self.num_buttons = num_buttons
        self.num_valuators = num_valuators
        self.classes_reported = classes_reported
        self.buttons = buttons
        self.keys = keys
        self.valuators = valuators

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'device_id': self.device_id,
            'time': self.time,
            'num_keys': self.num_keys,
            'num_buttons': self.num_buttons,
            'num_valuators': self.num_valuators,
            'classes_reported': self.classes_reported,
            'buttons': self.buttons,
            'keys': self.keys,
            'valuators': self.valuators,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeviceStateNotifyEvent':
        return DeviceStateNotifyEvent(**DeviceStateNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeviceStateNotifyEventPacket.pack(**self.as_dict())


class DeviceStateNotifyEventCType(ctypes.Structure):
    """xinput DeviceStateNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("device_id", ctypes.c_int8),
        ("time", ctypes.c_uint32),
        ("num_keys", ctypes.c_uint8),
        ("num_buttons", ctypes.c_uint8),
        ("num_valuators", ctypes.c_uint8),
        ("classes_reported", ctypes.c_uint8),
        ("var_data", ctypes.c_void_p),
    ]


DeviceMappingNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('device_id', FixedDataPacketField(MARKER_INT8)),
    ('request', FixedDataPacketField(MARKER_UINT8)),
    ('first_keycode', FixedDataPacketField(MARKER_UINT32)),
    ('count', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
))


class DeviceMappingNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'device_id', 'request', 'first_keycode', 'count', 'time',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            device_id: Optional[int] = None,
            request: Optional[int] = None,
            first_keycode: Optional[int] = None,
            count: Optional[int] = None,
            time: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.device_id = device_id
        self.request = request
        self.first_keycode = first_keycode
        self.count = count
        self.time = time

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'device_id': self.device_id,
            'request': self.request,
            'first_keycode': self.first_keycode,
            'count': self.count,
            'time': self.time,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeviceMappingNotifyEvent':
        return DeviceMappingNotifyEvent(**DeviceMappingNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeviceMappingNotifyEventPacket.pack(**self.as_dict())


class DeviceMappingNotifyEventCType(ctypes.Structure):
    """xinput DeviceMappingNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("device_id", ctypes.c_int8),
        ("request", ctypes.c_uint8),
        ("first_keycode", ctypes.c_uint32),
        ("count", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
        ("time", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
    ]


ChangeDeviceNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('device_id', FixedDataPacketField(MARKER_INT8)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('request', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(23)),
))


class ChangeDeviceNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'device_id', 'time', 'request',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            device_id: Optional[int] = None,
            time: Optional[int] = None,
            request: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.device_id = device_id
        self.time = time
        self.request = request

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'device_id': self.device_id,
            'time': self.time,
            'request': self.request,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ChangeDeviceNotifyEvent':
        return ChangeDeviceNotifyEvent(**ChangeDeviceNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ChangeDeviceNotifyEventPacket.pack(**self.as_dict())


class ChangeDeviceNotifyEventCType(ctypes.Structure):
    """xinput ChangeDeviceNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("device_id", ctypes.c_int8),
        ("time", ctypes.c_uint32),
        ("request", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 23),
    ]


DeviceKeyStateNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('device_id', FixedDataPacketField(MARKER_INT8)),
    ('keys', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: 28, 0)),
))


class DeviceKeyStateNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'device_id', 'keys',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            device_id: Optional[int] = None,
            keys: Optional[Sequence[int]] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.device_id = device_id
        self.keys = keys

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'device_id': self.device_id,
            'keys': self.keys,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeviceKeyStateNotifyEvent':
        return DeviceKeyStateNotifyEvent(**DeviceKeyStateNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeviceKeyStateNotifyEventPacket.pack(**self.as_dict())


class DeviceKeyStateNotifyEventCType(ctypes.Structure):
    """xinput DeviceKeyStateNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("device_id", ctypes.c_int8),
        ("var_data", ctypes.c_void_p),
    ]


DeviceButtonStateNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('device_id', FixedDataPacketField(MARKER_INT8)),
    ('buttons', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: 28, 0)),
))


class DeviceButtonStateNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'device_id', 'buttons',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            device_id: Optional[int] = None,
            buttons: Optional[Sequence[int]] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.device_id = device_id
        self.buttons = buttons

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'device_id': self.device_id,
            'buttons': self.buttons,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeviceButtonStateNotifyEvent':
        return DeviceButtonStateNotifyEvent(**DeviceButtonStateNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeviceButtonStateNotifyEventPacket.pack(**self.as_dict())


class DeviceButtonStateNotifyEventCType(ctypes.Structure):
    """xinput DeviceButtonStateNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("device_id", ctypes.c_int8),
        ("var_data", ctypes.c_void_p),
    ]


DevicePresenceNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(1)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('devchange', FixedDataPacketField(MARKER_INT8)),
    ('device_id', FixedDataPacketField(MARKER_INT8)),
    ('control', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(20)),
))


class DevicePresenceNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'time', 'devchange', 'device_id', 'control',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            time: Optional[int] = None,
            devchange: Optional[int] = None,
            device_id: Optional[int] = None,
            control: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.time = time
        self.devchange = devchange
        self.device_id = device_id
        self.control = control

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'time': self.time,
            'devchange': self.devchange,
            'device_id': self.device_id,
            'control': self.control,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DevicePresenceNotifyEvent':
        return DevicePresenceNotifyEvent(**DevicePresenceNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DevicePresenceNotifyEventPacket.pack(**self.as_dict())


class DevicePresenceNotifyEventCType(ctypes.Structure):
    """xinput DevicePresenceNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8),
        ("time", ctypes.c_uint32),
        ("devchange", ctypes.c_int8),
        ("device_id", ctypes.c_int8),
        ("control", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 20),
    ]


DevicePropertyNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('state', FixedDataPacketField(MARKER_INT8)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('property', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(19)),
    ('device_id', FixedDataPacketField(MARKER_UINT8)),
))


class DevicePropertyNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'state', 'time', 'property', 'device_id',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            state: Optional[int] = None,
            time: Optional[int] = None,
            property: Optional[int] = None,
            device_id: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.state = state
        self.time = time
        self.property = property
        self.device_id = device_id

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'state': self.state,
            'time': self.time,
            'property': self.property,
            'device_id': self.device_id,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DevicePropertyNotifyEvent':
        return DevicePropertyNotifyEvent(**DevicePropertyNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DevicePropertyNotifyEventPacket.pack(**self.as_dict())


class DevicePropertyNotifyEventCType(ctypes.Structure):
    """xinput DevicePropertyNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("state", ctypes.c_int8),
        ("time", ctypes.c_uint32),
        ("property", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 19),
        ("device_id", ctypes.c_uint8),
    ]


DeviceChangedEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('extension', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('length', FixedDataPacketField(MARKER_UINT32)),
    ('event_type', FixedDataPacketField(MARKER_UINT16)),
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('num_classes', FixedDataPacketField(MARKER_UINT16)),
    ('sourceid', FixedDataPacketField(MARKER_UINT32)),
    ('reason', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(11)),
    ('classes', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_classes'], 0)),
))


class DeviceChangedEvent:
    __slots__ = ('response_type', 'extension', 'sequence', 'length', 'event_type', 'deviceid', 'time', 'num_classes', 'sourceid', 'reason', 'classes',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            extension: Optional[int] = None,
            sequence: Optional[int] = None,
            length: Optional[int] = None,
            event_type: Optional[int] = None,
            deviceid: Optional[int] = None,
            time: Optional[int] = None,
            num_classes: Optional[int] = None,
            sourceid: Optional[int] = None,
            reason: Optional[int] = None,
            classes: Optional[Sequence[int]] = None,
    ) -> None:
        self.response_type = response_type
        self.extension = extension
        self.sequence = sequence
        self.length = length
        self.event_type = event_type
        self.deviceid = deviceid
        self.time = time
        self.num_classes = num_classes
        self.sourceid = sourceid
        self.reason = reason
        self.classes = classes

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'extension': self.extension,
            'sequence': self.sequence,
            'length': self.length,
            'event_type': self.event_type,
            'deviceid': self.deviceid,
            'time': self.time,
            'num_classes': self.num_classes,
            'sourceid': self.sourceid,
            'reason': self.reason,
            'classes': self.classes,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeviceChangedEvent':
        return DeviceChangedEvent(**DeviceChangedEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeviceChangedEventPacket.pack(**self.as_dict())


class DeviceChangedEventCType(ctypes.Structure):
    """xinput DeviceChanged"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("extension", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("length", ctypes.c_uint32),
        ("event_type", ctypes.c_uint16),
        ("deviceid", ctypes.c_uint32),
        ("time", ctypes.c_uint32),
        ("num_classes", ctypes.c_uint16),
        ("sourceid", ctypes.c_uint32),
        ("reason", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 11),
        ("var_data", ctypes.c_void_p),
    ]


KeyPressEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('extension', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('length', FixedDataPacketField(MARKER_UINT32)),
    ('event_type', FixedDataPacketField(MARKER_UINT16)),
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('detail', FixedDataPacketField(MARKER_UINT32)),
    ('root', FixedDataPacketField(MARKER_UINT32)),
    ('event', FixedDataPacketField(MARKER_UINT32)),
    ('child', FixedDataPacketField(MARKER_UINT32)),
    ('root_x', FixedDataPacketField(MARKER_UINT32)),
    ('root_y', FixedDataPacketField(MARKER_UINT32)),
    ('event_x', FixedDataPacketField(MARKER_UINT32)),
    ('event_y', FixedDataPacketField(MARKER_UINT32)),
    ('buttons_len', FixedDataPacketField(MARKER_UINT16)),
    ('valuators_len', FixedDataPacketField(MARKER_UINT16)),
    ('sourceid', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(2)),
    ('flags', FixedDataPacketField(MARKER_UINT32)),
    ('mods', FixedDataPacketField(MARKER_UINT32)),
    ('group', FixedDataPacketField(MARKER_UINT32)),
    ('button_mask', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['buttons_len'], 0)),
    ('valuator_mask', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['valuators_len'], 0)),
    ('axisvalues', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: sum([(d1) for d1 in d['valuator_mask']]), 0)),
))


class KeyPressEvent:
    __slots__ = ('response_type', 'extension', 'sequence', 'length', 'event_type', 'deviceid', 'time', 'detail', 'root', 'event', 'child', 'root_x', 'root_y', 'event_x', 'event_y', 'buttons_len', 'valuators_len', 'sourceid', 'flags', 'mods', 'group', 'button_mask', 'valuator_mask', 'axisvalues',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            extension: Optional[int] = None,
            sequence: Optional[int] = None,
            length: Optional[int] = None,
            event_type: Optional[int] = None,
            deviceid: Optional[int] = None,
            time: Optional[int] = None,
            detail: Optional[int] = None,
            root: Optional[int] = None,
            event: Optional[int] = None,
            child: Optional[int] = None,
            root_x: Optional[int] = None,
            root_y: Optional[int] = None,
            event_x: Optional[int] = None,
            event_y: Optional[int] = None,
            buttons_len: Optional[int] = None,
            valuators_len: Optional[int] = None,
            sourceid: Optional[int] = None,
            flags: Optional[int] = None,
            mods: Optional[int] = None,
            group: Optional[int] = None,
            button_mask: Optional[Sequence[int]] = None,
            valuator_mask: Optional[Sequence[int]] = None,
            axisvalues: Optional[Sequence[int]] = None,
    ) -> None:
        self.response_type = response_type
        self.extension = extension
        self.sequence = sequence
        self.length = length
        self.event_type = event_type
        self.deviceid = deviceid
        self.time = time
        self.detail = detail
        self.root = root
        self.event = event
        self.child = child
        self.root_x = root_x
        self.root_y = root_y
        self.event_x = event_x
        self.event_y = event_y
        self.buttons_len = buttons_len
        self.valuators_len = valuators_len
        self.sourceid = sourceid
        self.flags = flags
        self.mods = mods
        self.group = group
        self.button_mask = button_mask
        self.valuator_mask = valuator_mask
        self.axisvalues = axisvalues

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'extension': self.extension,
            'sequence': self.sequence,
            'length': self.length,
            'event_type': self.event_type,
            'deviceid': self.deviceid,
            'time': self.time,
            'detail': self.detail,
            'root': self.root,
            'event': self.event,
            'child': self.child,
            'root_x': self.root_x,
            'root_y': self.root_y,
            'event_x': self.event_x,
            'event_y': self.event_y,
            'buttons_len': self.buttons_len,
            'valuators_len': self.valuators_len,
            'sourceid': self.sourceid,
            'flags': self.flags,
            'mods': self.mods,
            'group': self.group,
            'button_mask': self.button_mask,
            'valuator_mask': self.valuator_mask,
            'axisvalues': self.axisvalues,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'KeyPressEvent':
        return KeyPressEvent(**KeyPressEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return KeyPressEventPacket.pack(**self.as_dict())


class KeyPressEventCType(ctypes.Structure):
    """xinput KeyPress"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("extension", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("length", ctypes.c_uint32),
        ("event_type", ctypes.c_uint16),
        ("deviceid", ctypes.c_uint32),
        ("time", ctypes.c_uint32),
        ("detail", ctypes.c_uint32),
        ("root", ctypes.c_uint32),
        ("event", ctypes.c_uint32),
        ("child", ctypes.c_uint32),
        ("root_x", ctypes.c_uint32),
        ("root_y", ctypes.c_uint32),
        ("event_x", ctypes.c_uint32),
        ("event_y", ctypes.c_uint32),
        ("buttons_len", ctypes.c_uint16),
        ("valuators_len", ctypes.c_uint16),
        ("sourceid", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 2),
        ("flags", ctypes.c_uint32),
        ("mods", ctypes.c_uint32),
        ("group", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


ButtonPressEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('extension', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('length', FixedDataPacketField(MARKER_UINT32)),
    ('event_type', FixedDataPacketField(MARKER_UINT16)),
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('detail', FixedDataPacketField(MARKER_UINT32)),
    ('root', FixedDataPacketField(MARKER_UINT32)),
    ('event', FixedDataPacketField(MARKER_UINT32)),
    ('child', FixedDataPacketField(MARKER_UINT32)),
    ('root_x', FixedDataPacketField(MARKER_UINT32)),
    ('root_y', FixedDataPacketField(MARKER_UINT32)),
    ('event_x', FixedDataPacketField(MARKER_UINT32)),
    ('event_y', FixedDataPacketField(MARKER_UINT32)),
    ('buttons_len', FixedDataPacketField(MARKER_UINT16)),
    ('valuators_len', FixedDataPacketField(MARKER_UINT16)),
    ('sourceid', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(2)),
    ('flags', FixedDataPacketField(MARKER_UINT32)),
    ('mods', FixedDataPacketField(MARKER_UINT32)),
    ('group', FixedDataPacketField(MARKER_UINT32)),
    ('button_mask', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['buttons_len'], 0)),
    ('valuator_mask', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['valuators_len'], 0)),
    ('axisvalues', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: sum([(d1) for d1 in d['valuator_mask']]), 0)),
))


class ButtonPressEvent:
    __slots__ = ('response_type', 'extension', 'sequence', 'length', 'event_type', 'deviceid', 'time', 'detail', 'root', 'event', 'child', 'root_x', 'root_y', 'event_x', 'event_y', 'buttons_len', 'valuators_len', 'sourceid', 'flags', 'mods', 'group', 'button_mask', 'valuator_mask', 'axisvalues',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            extension: Optional[int] = None,
            sequence: Optional[int] = None,
            length: Optional[int] = None,
            event_type: Optional[int] = None,
            deviceid: Optional[int] = None,
            time: Optional[int] = None,
            detail: Optional[int] = None,
            root: Optional[int] = None,
            event: Optional[int] = None,
            child: Optional[int] = None,
            root_x: Optional[int] = None,
            root_y: Optional[int] = None,
            event_x: Optional[int] = None,
            event_y: Optional[int] = None,
            buttons_len: Optional[int] = None,
            valuators_len: Optional[int] = None,
            sourceid: Optional[int] = None,
            flags: Optional[int] = None,
            mods: Optional[int] = None,
            group: Optional[int] = None,
            button_mask: Optional[Sequence[int]] = None,
            valuator_mask: Optional[Sequence[int]] = None,
            axisvalues: Optional[Sequence[int]] = None,
    ) -> None:
        self.response_type = response_type
        self.extension = extension
        self.sequence = sequence
        self.length = length
        self.event_type = event_type
        self.deviceid = deviceid
        self.time = time
        self.detail = detail
        self.root = root
        self.event = event
        self.child = child
        self.root_x = root_x
        self.root_y = root_y
        self.event_x = event_x
        self.event_y = event_y
        self.buttons_len = buttons_len
        self.valuators_len = valuators_len
        self.sourceid = sourceid
        self.flags = flags
        self.mods = mods
        self.group = group
        self.button_mask = button_mask
        self.valuator_mask = valuator_mask
        self.axisvalues = axisvalues

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'extension': self.extension,
            'sequence': self.sequence,
            'length': self.length,
            'event_type': self.event_type,
            'deviceid': self.deviceid,
            'time': self.time,
            'detail': self.detail,
            'root': self.root,
            'event': self.event,
            'child': self.child,
            'root_x': self.root_x,
            'root_y': self.root_y,
            'event_x': self.event_x,
            'event_y': self.event_y,
            'buttons_len': self.buttons_len,
            'valuators_len': self.valuators_len,
            'sourceid': self.sourceid,
            'flags': self.flags,
            'mods': self.mods,
            'group': self.group,
            'button_mask': self.button_mask,
            'valuator_mask': self.valuator_mask,
            'axisvalues': self.axisvalues,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ButtonPressEvent':
        return ButtonPressEvent(**ButtonPressEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ButtonPressEventPacket.pack(**self.as_dict())


class ButtonPressEventCType(ctypes.Structure):
    """xinput ButtonPress"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("extension", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("length", ctypes.c_uint32),
        ("event_type", ctypes.c_uint16),
        ("deviceid", ctypes.c_uint32),
        ("time", ctypes.c_uint32),
        ("detail", ctypes.c_uint32),
        ("root", ctypes.c_uint32),
        ("event", ctypes.c_uint32),
        ("child", ctypes.c_uint32),
        ("root_x", ctypes.c_uint32),
        ("root_y", ctypes.c_uint32),
        ("event_x", ctypes.c_uint32),
        ("event_y", ctypes.c_uint32),
        ("buttons_len", ctypes.c_uint16),
        ("valuators_len", ctypes.c_uint16),
        ("sourceid", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 2),
        ("flags", ctypes.c_uint32),
        ("mods", ctypes.c_uint32),
        ("group", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


EnterEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('extension', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('length', FixedDataPacketField(MARKER_UINT32)),
    ('event_type', FixedDataPacketField(MARKER_UINT16)),
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('sourceid', FixedDataPacketField(MARKER_UINT32)),
    ('mode', FixedDataPacketField(MARKER_UINT8)),
    ('detail', FixedDataPacketField(MARKER_UINT8)),
    ('root', FixedDataPacketField(MARKER_UINT32)),
    ('event', FixedDataPacketField(MARKER_UINT32)),
    ('child', FixedDataPacketField(MARKER_UINT32)),
    ('root_x', FixedDataPacketField(MARKER_UINT32)),
    ('root_y', FixedDataPacketField(MARKER_UINT32)),
    ('event_x', FixedDataPacketField(MARKER_UINT32)),
    ('event_y', FixedDataPacketField(MARKER_UINT32)),
    ('same_screen', FixedDataPacketField(MARKER_UINT8)),
    ('focus', FixedDataPacketField(MARKER_UINT8)),
    ('buttons_len', FixedDataPacketField(MARKER_UINT16)),
    ('mods', FixedDataPacketField(MARKER_UINT32)),
    ('group', FixedDataPacketField(MARKER_UINT32)),
    ('buttons', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['buttons_len'], 0)),
))


class EnterEvent:
    __slots__ = ('response_type', 'extension', 'sequence', 'length', 'event_type', 'deviceid', 'time', 'sourceid', 'mode', 'detail', 'root', 'event', 'child', 'root_x', 'root_y', 'event_x', 'event_y', 'same_screen', 'focus', 'buttons_len', 'mods', 'group', 'buttons',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            extension: Optional[int] = None,
            sequence: Optional[int] = None,
            length: Optional[int] = None,
            event_type: Optional[int] = None,
            deviceid: Optional[int] = None,
            time: Optional[int] = None,
            sourceid: Optional[int] = None,
            mode: Optional[int] = None,
            detail: Optional[int] = None,
            root: Optional[int] = None,
            event: Optional[int] = None,
            child: Optional[int] = None,
            root_x: Optional[int] = None,
            root_y: Optional[int] = None,
            event_x: Optional[int] = None,
            event_y: Optional[int] = None,
            same_screen: Optional[bool] = None,
            focus: Optional[bool] = None,
            buttons_len: Optional[int] = None,
            mods: Optional[int] = None,
            group: Optional[int] = None,
            buttons: Optional[Sequence[int]] = None,
    ) -> None:
        self.response_type = response_type
        self.extension = extension
        self.sequence = sequence
        self.length = length
        self.event_type = event_type
        self.deviceid = deviceid
        self.time = time
        self.sourceid = sourceid
        self.mode = mode
        self.detail = detail
        self.root = root
        self.event = event
        self.child = child
        self.root_x = root_x
        self.root_y = root_y
        self.event_x = event_x
        self.event_y = event_y
        self.same_screen = same_screen
        self.focus = focus
        self.buttons_len = buttons_len
        self.mods = mods
        self.group = group
        self.buttons = buttons

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'extension': self.extension,
            'sequence': self.sequence,
            'length': self.length,
            'event_type': self.event_type,
            'deviceid': self.deviceid,
            'time': self.time,
            'sourceid': self.sourceid,
            'mode': self.mode,
            'detail': self.detail,
            'root': self.root,
            'event': self.event,
            'child': self.child,
            'root_x': self.root_x,
            'root_y': self.root_y,
            'event_x': self.event_x,
            'event_y': self.event_y,
            'same_screen': self.same_screen,
            'focus': self.focus,
            'buttons_len': self.buttons_len,
            'mods': self.mods,
            'group': self.group,
            'buttons': self.buttons,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'EnterEvent':
        return EnterEvent(**EnterEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return EnterEventPacket.pack(**self.as_dict())


class EnterEventCType(ctypes.Structure):
    """xinput Enter"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("extension", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("length", ctypes.c_uint32),
        ("event_type", ctypes.c_uint16),
        ("deviceid", ctypes.c_uint32),
        ("time", ctypes.c_uint32),
        ("sourceid", ctypes.c_uint32),
        ("mode", ctypes.c_uint8),
        ("detail", ctypes.c_uint8),
        ("root", ctypes.c_uint32),
        ("event", ctypes.c_uint32),
        ("child", ctypes.c_uint32),
        ("root_x", ctypes.c_uint32),
        ("root_y", ctypes.c_uint32),
        ("event_x", ctypes.c_uint32),
        ("event_y", ctypes.c_uint32),
        ("same_screen", ctypes.c_int8),
        ("focus", ctypes.c_int8),
        ("buttons_len", ctypes.c_uint16),
        ("mods", ctypes.c_uint32),
        ("group", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


HierarchyInfoStructPacket = DataPacket((
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('attachment', FixedDataPacketField(MARKER_UINT32)),
    ('type', FixedDataPacketField(MARKER_UINT8)),
    ('enabled', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
    ('flags', FixedDataPacketField(MARKER_UINT32)),
))


class HierarchyInfoStruct:
    __slots__ = ('deviceid', 'attachment', 'type', 'enabled', 'flags',)

    def __init__(
            self, *,
            deviceid: Optional[int] = None,
            attachment: Optional[int] = None,
            type: Optional[int] = None,
            enabled: Optional[bool] = None,
            flags: Optional[int] = None,
    ) -> None:
        self.deviceid = deviceid
        self.attachment = attachment
        self.type = type
        self.enabled = enabled
        self.flags = flags

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceid': self.deviceid,
            'attachment': self.attachment,
            'type': self.type,
            'enabled': self.enabled,
            'flags': self.flags,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'HierarchyInfoStruct':
        return HierarchyInfoStruct(**HierarchyInfoStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return HierarchyInfoStructPacket.pack(**self.as_dict())


class HierarchyInfoStructCType(ctypes.Structure):
    """xinput HierarchyInfo"""
    _fields_ = [
        ("deviceid", ctypes.c_uint32),
        ("attachment", ctypes.c_uint32),
        ("type", ctypes.c_uint8),
        ("enabled", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 2),
        ("flags", ctypes.c_uint32),
    ]


HierarchyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('extension', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('length', FixedDataPacketField(MARKER_UINT32)),
    ('event_type', FixedDataPacketField(MARKER_UINT16)),
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('flags', FixedDataPacketField(MARKER_UINT32)),
    ('num_infos', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(10)),
    ('infos', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_infos'], 0)),
))


class HierarchyEvent:
    __slots__ = ('response_type', 'extension', 'sequence', 'length', 'event_type', 'deviceid', 'time', 'flags', 'num_infos', 'infos',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            extension: Optional[int] = None,
            sequence: Optional[int] = None,
            length: Optional[int] = None,
            event_type: Optional[int] = None,
            deviceid: Optional[int] = None,
            time: Optional[int] = None,
            flags: Optional[int] = None,
            num_infos: Optional[int] = None,
            infos: Optional[Sequence[int]] = None,
    ) -> None:
        self.response_type = response_type
        self.extension = extension
        self.sequence = sequence
        self.length = length
        self.event_type = event_type
        self.deviceid = deviceid
        self.time = time
        self.flags = flags
        self.num_infos = num_infos
        self.infos = infos

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'extension': self.extension,
            'sequence': self.sequence,
            'length': self.length,
            'event_type': self.event_type,
            'deviceid': self.deviceid,
            'time': self.time,
            'flags': self.flags,
            'num_infos': self.num_infos,
            'infos': self.infos,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'HierarchyEvent':
        return HierarchyEvent(**HierarchyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return HierarchyEventPacket.pack(**self.as_dict())


class HierarchyEventCType(ctypes.Structure):
    """xinput Hierarchy"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("extension", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("length", ctypes.c_uint32),
        ("event_type", ctypes.c_uint16),
        ("deviceid", ctypes.c_uint32),
        ("time", ctypes.c_uint32),
        ("flags", ctypes.c_uint32),
        ("num_infos", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 10),
        ("var_data", ctypes.c_void_p),
    ]


PropertyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('extension', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('length', FixedDataPacketField(MARKER_UINT32)),
    ('event_type', FixedDataPacketField(MARKER_UINT16)),
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('property', FixedDataPacketField(MARKER_UINT32)),
    ('what', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(11)),
))


class PropertyEvent:
    __slots__ = ('response_type', 'extension', 'sequence', 'length', 'event_type', 'deviceid', 'time', 'property', 'what',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            extension: Optional[int] = None,
            sequence: Optional[int] = None,
            length: Optional[int] = None,
            event_type: Optional[int] = None,
            deviceid: Optional[int] = None,
            time: Optional[int] = None,
            property: Optional[int] = None,
            what: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.extension = extension
        self.sequence = sequence
        self.length = length
        self.event_type = event_type
        self.deviceid = deviceid
        self.time = time
        self.property = property
        self.what = what

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'extension': self.extension,
            'sequence': self.sequence,
            'length': self.length,
            'event_type': self.event_type,
            'deviceid': self.deviceid,
            'time': self.time,
            'property': self.property,
            'what': self.what,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PropertyEvent':
        return PropertyEvent(**PropertyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PropertyEventPacket.pack(**self.as_dict())


class PropertyEventCType(ctypes.Structure):
    """xinput Property"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("extension", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("length", ctypes.c_uint32),
        ("event_type", ctypes.c_uint16),
        ("deviceid", ctypes.c_uint32),
        ("time", ctypes.c_uint32),
        ("property", ctypes.c_uint32),
        ("what", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 11),
    ]


RawKeyPressEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('extension', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('length', FixedDataPacketField(MARKER_UINT32)),
    ('event_type', FixedDataPacketField(MARKER_UINT16)),
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('detail', FixedDataPacketField(MARKER_UINT32)),
    ('sourceid', FixedDataPacketField(MARKER_UINT32)),
    ('valuators_len', FixedDataPacketField(MARKER_UINT16)),
    ('flags', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(4)),
    ('valuator_mask', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['valuators_len'], 0)),
    ('axisvalues', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: sum([(d1) for d1 in d['valuator_mask']]), 0)),
    ('axisvalues_raw', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: sum([(d1) for d1 in d['valuator_mask']]), 0)),
))


class RawKeyPressEvent:
    __slots__ = ('response_type', 'extension', 'sequence', 'length', 'event_type', 'deviceid', 'time', 'detail', 'sourceid', 'valuators_len', 'flags', 'valuator_mask', 'axisvalues', 'axisvalues_raw',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            extension: Optional[int] = None,
            sequence: Optional[int] = None,
            length: Optional[int] = None,
            event_type: Optional[int] = None,
            deviceid: Optional[int] = None,
            time: Optional[int] = None,
            detail: Optional[int] = None,
            sourceid: Optional[int] = None,
            valuators_len: Optional[int] = None,
            flags: Optional[int] = None,
            valuator_mask: Optional[Sequence[int]] = None,
            axisvalues: Optional[Sequence[int]] = None,
            axisvalues_raw: Optional[Sequence[int]] = None,
    ) -> None:
        self.response_type = response_type
        self.extension = extension
        self.sequence = sequence
        self.length = length
        self.event_type = event_type
        self.deviceid = deviceid
        self.time = time
        self.detail = detail
        self.sourceid = sourceid
        self.valuators_len = valuators_len
        self.flags = flags
        self.valuator_mask = valuator_mask
        self.axisvalues = axisvalues
        self.axisvalues_raw = axisvalues_raw

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'extension': self.extension,
            'sequence': self.sequence,
            'length': self.length,
            'event_type': self.event_type,
            'deviceid': self.deviceid,
            'time': self.time,
            'detail': self.detail,
            'sourceid': self.sourceid,
            'valuators_len': self.valuators_len,
            'flags': self.flags,
            'valuator_mask': self.valuator_mask,
            'axisvalues': self.axisvalues,
            'axisvalues_raw': self.axisvalues_raw,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'RawKeyPressEvent':
        return RawKeyPressEvent(**RawKeyPressEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return RawKeyPressEventPacket.pack(**self.as_dict())


class RawKeyPressEventCType(ctypes.Structure):
    """xinput RawKeyPress"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("extension", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("length", ctypes.c_uint32),
        ("event_type", ctypes.c_uint16),
        ("deviceid", ctypes.c_uint32),
        ("time", ctypes.c_uint32),
        ("detail", ctypes.c_uint32),
        ("sourceid", ctypes.c_uint32),
        ("valuators_len", ctypes.c_uint16),
        ("flags", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 4),
        ("var_data", ctypes.c_void_p),
    ]


RawButtonPressEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('extension', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('length', FixedDataPacketField(MARKER_UINT32)),
    ('event_type', FixedDataPacketField(MARKER_UINT16)),
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('detail', FixedDataPacketField(MARKER_UINT32)),
    ('sourceid', FixedDataPacketField(MARKER_UINT32)),
    ('valuators_len', FixedDataPacketField(MARKER_UINT16)),
    ('flags', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(4)),
    ('valuator_mask', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['valuators_len'], 0)),
    ('axisvalues', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: sum([(d1) for d1 in d['valuator_mask']]), 0)),
    ('axisvalues_raw', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: sum([(d1) for d1 in d['valuator_mask']]), 0)),
))


class RawButtonPressEvent:
    __slots__ = ('response_type', 'extension', 'sequence', 'length', 'event_type', 'deviceid', 'time', 'detail', 'sourceid', 'valuators_len', 'flags', 'valuator_mask', 'axisvalues', 'axisvalues_raw',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            extension: Optional[int] = None,
            sequence: Optional[int] = None,
            length: Optional[int] = None,
            event_type: Optional[int] = None,
            deviceid: Optional[int] = None,
            time: Optional[int] = None,
            detail: Optional[int] = None,
            sourceid: Optional[int] = None,
            valuators_len: Optional[int] = None,
            flags: Optional[int] = None,
            valuator_mask: Optional[Sequence[int]] = None,
            axisvalues: Optional[Sequence[int]] = None,
            axisvalues_raw: Optional[Sequence[int]] = None,
    ) -> None:
        self.response_type = response_type
        self.extension = extension
        self.sequence = sequence
        self.length = length
        self.event_type = event_type
        self.deviceid = deviceid
        self.time = time
        self.detail = detail
        self.sourceid = sourceid
        self.valuators_len = valuators_len
        self.flags = flags
        self.valuator_mask = valuator_mask
        self.axisvalues = axisvalues
        self.axisvalues_raw = axisvalues_raw

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'extension': self.extension,
            'sequence': self.sequence,
            'length': self.length,
            'event_type': self.event_type,
            'deviceid': self.deviceid,
            'time': self.time,
            'detail': self.detail,
            'sourceid': self.sourceid,
            'valuators_len': self.valuators_len,
            'flags': self.flags,
            'valuator_mask': self.valuator_mask,
            'axisvalues': self.axisvalues,
            'axisvalues_raw': self.axisvalues_raw,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'RawButtonPressEvent':
        return RawButtonPressEvent(**RawButtonPressEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return RawButtonPressEventPacket.pack(**self.as_dict())


class RawButtonPressEventCType(ctypes.Structure):
    """xinput RawButtonPress"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("extension", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("length", ctypes.c_uint32),
        ("event_type", ctypes.c_uint16),
        ("deviceid", ctypes.c_uint32),
        ("time", ctypes.c_uint32),
        ("detail", ctypes.c_uint32),
        ("sourceid", ctypes.c_uint32),
        ("valuators_len", ctypes.c_uint16),
        ("flags", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 4),
        ("var_data", ctypes.c_void_p),
    ]


TouchBeginEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('extension', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('length', FixedDataPacketField(MARKER_UINT32)),
    ('event_type', FixedDataPacketField(MARKER_UINT16)),
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('detail', FixedDataPacketField(MARKER_UINT32)),
    ('root', FixedDataPacketField(MARKER_UINT32)),
    ('event', FixedDataPacketField(MARKER_UINT32)),
    ('child', FixedDataPacketField(MARKER_UINT32)),
    ('root_x', FixedDataPacketField(MARKER_UINT32)),
    ('root_y', FixedDataPacketField(MARKER_UINT32)),
    ('event_x', FixedDataPacketField(MARKER_UINT32)),
    ('event_y', FixedDataPacketField(MARKER_UINT32)),
    ('buttons_len', FixedDataPacketField(MARKER_UINT16)),
    ('valuators_len', FixedDataPacketField(MARKER_UINT16)),
    ('sourceid', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(2)),
    ('flags', FixedDataPacketField(MARKER_UINT32)),
    ('mods', FixedDataPacketField(MARKER_UINT32)),
    ('group', FixedDataPacketField(MARKER_UINT32)),
    ('button_mask', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['buttons_len'], 0)),
    ('valuator_mask', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['valuators_len'], 0)),
    ('axisvalues', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: sum([(d1) for d1 in d['valuator_mask']]), 0)),
))


class TouchBeginEvent:
    __slots__ = ('response_type', 'extension', 'sequence', 'length', 'event_type', 'deviceid', 'time', 'detail', 'root', 'event', 'child', 'root_x', 'root_y', 'event_x', 'event_y', 'buttons_len', 'valuators_len', 'sourceid', 'flags', 'mods', 'group', 'button_mask', 'valuator_mask', 'axisvalues',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            extension: Optional[int] = None,
            sequence: Optional[int] = None,
            length: Optional[int] = None,
            event_type: Optional[int] = None,
            deviceid: Optional[int] = None,
            time: Optional[int] = None,
            detail: Optional[int] = None,
            root: Optional[int] = None,
            event: Optional[int] = None,
            child: Optional[int] = None,
            root_x: Optional[int] = None,
            root_y: Optional[int] = None,
            event_x: Optional[int] = None,
            event_y: Optional[int] = None,
            buttons_len: Optional[int] = None,
            valuators_len: Optional[int] = None,
            sourceid: Optional[int] = None,
            flags: Optional[int] = None,
            mods: Optional[int] = None,
            group: Optional[int] = None,
            button_mask: Optional[Sequence[int]] = None,
            valuator_mask: Optional[Sequence[int]] = None,
            axisvalues: Optional[Sequence[int]] = None,
    ) -> None:
        self.response_type = response_type
        self.extension = extension
        self.sequence = sequence
        self.length = length
        self.event_type = event_type
        self.deviceid = deviceid
        self.time = time
        self.detail = detail
        self.root = root
        self.event = event
        self.child = child
        self.root_x = root_x
        self.root_y = root_y
        self.event_x = event_x
        self.event_y = event_y
        self.buttons_len = buttons_len
        self.valuators_len = valuators_len
        self.sourceid = sourceid
        self.flags = flags
        self.mods = mods
        self.group = group
        self.button_mask = button_mask
        self.valuator_mask = valuator_mask
        self.axisvalues = axisvalues

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'extension': self.extension,
            'sequence': self.sequence,
            'length': self.length,
            'event_type': self.event_type,
            'deviceid': self.deviceid,
            'time': self.time,
            'detail': self.detail,
            'root': self.root,
            'event': self.event,
            'child': self.child,
            'root_x': self.root_x,
            'root_y': self.root_y,
            'event_x': self.event_x,
            'event_y': self.event_y,
            'buttons_len': self.buttons_len,
            'valuators_len': self.valuators_len,
            'sourceid': self.sourceid,
            'flags': self.flags,
            'mods': self.mods,
            'group': self.group,
            'button_mask': self.button_mask,
            'valuator_mask': self.valuator_mask,
            'axisvalues': self.axisvalues,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'TouchBeginEvent':
        return TouchBeginEvent(**TouchBeginEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return TouchBeginEventPacket.pack(**self.as_dict())


class TouchBeginEventCType(ctypes.Structure):
    """xinput TouchBegin"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("extension", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("length", ctypes.c_uint32),
        ("event_type", ctypes.c_uint16),
        ("deviceid", ctypes.c_uint32),
        ("time", ctypes.c_uint32),
        ("detail", ctypes.c_uint32),
        ("root", ctypes.c_uint32),
        ("event", ctypes.c_uint32),
        ("child", ctypes.c_uint32),
        ("root_x", ctypes.c_uint32),
        ("root_y", ctypes.c_uint32),
        ("event_x", ctypes.c_uint32),
        ("event_y", ctypes.c_uint32),
        ("buttons_len", ctypes.c_uint16),
        ("valuators_len", ctypes.c_uint16),
        ("sourceid", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 2),
        ("flags", ctypes.c_uint32),
        ("mods", ctypes.c_uint32),
        ("group", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


TouchOwnershipEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('extension', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('length', FixedDataPacketField(MARKER_UINT32)),
    ('event_type', FixedDataPacketField(MARKER_UINT16)),
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('touchid', FixedDataPacketField(MARKER_UINT32)),
    ('root', FixedDataPacketField(MARKER_UINT32)),
    ('event', FixedDataPacketField(MARKER_UINT32)),
    ('child', FixedDataPacketField(MARKER_UINT32)),
    ('sourceid', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(2)),
    ('flags', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(8)),
))


class TouchOwnershipEvent:
    __slots__ = ('response_type', 'extension', 'sequence', 'length', 'event_type', 'deviceid', 'time', 'touchid', 'root', 'event', 'child', 'sourceid', 'flags',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            extension: Optional[int] = None,
            sequence: Optional[int] = None,
            length: Optional[int] = None,
            event_type: Optional[int] = None,
            deviceid: Optional[int] = None,
            time: Optional[int] = None,
            touchid: Optional[int] = None,
            root: Optional[int] = None,
            event: Optional[int] = None,
            child: Optional[int] = None,
            sourceid: Optional[int] = None,
            flags: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.extension = extension
        self.sequence = sequence
        self.length = length
        self.event_type = event_type
        self.deviceid = deviceid
        self.time = time
        self.touchid = touchid
        self.root = root
        self.event = event
        self.child = child
        self.sourceid = sourceid
        self.flags = flags

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'extension': self.extension,
            'sequence': self.sequence,
            'length': self.length,
            'event_type': self.event_type,
            'deviceid': self.deviceid,
            'time': self.time,
            'touchid': self.touchid,
            'root': self.root,
            'event': self.event,
            'child': self.child,
            'sourceid': self.sourceid,
            'flags': self.flags,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'TouchOwnershipEvent':
        return TouchOwnershipEvent(**TouchOwnershipEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return TouchOwnershipEventPacket.pack(**self.as_dict())


class TouchOwnershipEventCType(ctypes.Structure):
    """xinput TouchOwnership"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("extension", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("length", ctypes.c_uint32),
        ("event_type", ctypes.c_uint16),
        ("deviceid", ctypes.c_uint32),
        ("time", ctypes.c_uint32),
        ("touchid", ctypes.c_uint32),
        ("root", ctypes.c_uint32),
        ("event", ctypes.c_uint32),
        ("child", ctypes.c_uint32),
        ("sourceid", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 2),
        ("flags", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 8),
    ]


RawTouchBeginEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('extension', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('length', FixedDataPacketField(MARKER_UINT32)),
    ('event_type', FixedDataPacketField(MARKER_UINT16)),
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('detail', FixedDataPacketField(MARKER_UINT32)),
    ('sourceid', FixedDataPacketField(MARKER_UINT32)),
    ('valuators_len', FixedDataPacketField(MARKER_UINT16)),
    ('flags', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(4)),
    ('valuator_mask', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['valuators_len'], 0)),
    ('axisvalues', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: sum([(d1) for d1 in d['valuator_mask']]), 0)),
    ('axisvalues_raw', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: sum([(d1) for d1 in d['valuator_mask']]), 0)),
))


class RawTouchBeginEvent:
    __slots__ = ('response_type', 'extension', 'sequence', 'length', 'event_type', 'deviceid', 'time', 'detail', 'sourceid', 'valuators_len', 'flags', 'valuator_mask', 'axisvalues', 'axisvalues_raw',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            extension: Optional[int] = None,
            sequence: Optional[int] = None,
            length: Optional[int] = None,
            event_type: Optional[int] = None,
            deviceid: Optional[int] = None,
            time: Optional[int] = None,
            detail: Optional[int] = None,
            sourceid: Optional[int] = None,
            valuators_len: Optional[int] = None,
            flags: Optional[int] = None,
            valuator_mask: Optional[Sequence[int]] = None,
            axisvalues: Optional[Sequence[int]] = None,
            axisvalues_raw: Optional[Sequence[int]] = None,
    ) -> None:
        self.response_type = response_type
        self.extension = extension
        self.sequence = sequence
        self.length = length
        self.event_type = event_type
        self.deviceid = deviceid
        self.time = time
        self.detail = detail
        self.sourceid = sourceid
        self.valuators_len = valuators_len
        self.flags = flags
        self.valuator_mask = valuator_mask
        self.axisvalues = axisvalues
        self.axisvalues_raw = axisvalues_raw

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'extension': self.extension,
            'sequence': self.sequence,
            'length': self.length,
            'event_type': self.event_type,
            'deviceid': self.deviceid,
            'time': self.time,
            'detail': self.detail,
            'sourceid': self.sourceid,
            'valuators_len': self.valuators_len,
            'flags': self.flags,
            'valuator_mask': self.valuator_mask,
            'axisvalues': self.axisvalues,
            'axisvalues_raw': self.axisvalues_raw,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'RawTouchBeginEvent':
        return RawTouchBeginEvent(**RawTouchBeginEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return RawTouchBeginEventPacket.pack(**self.as_dict())


class RawTouchBeginEventCType(ctypes.Structure):
    """xinput RawTouchBegin"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("extension", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("length", ctypes.c_uint32),
        ("event_type", ctypes.c_uint16),
        ("deviceid", ctypes.c_uint32),
        ("time", ctypes.c_uint32),
        ("detail", ctypes.c_uint32),
        ("sourceid", ctypes.c_uint32),
        ("valuators_len", ctypes.c_uint16),
        ("flags", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 4),
        ("var_data", ctypes.c_void_p),
    ]


BarrierHitEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('extension', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('length', FixedDataPacketField(MARKER_UINT32)),
    ('event_type', FixedDataPacketField(MARKER_UINT16)),
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('eventid', FixedDataPacketField(MARKER_UINT32)),
    ('root', FixedDataPacketField(MARKER_UINT32)),
    ('event', FixedDataPacketField(MARKER_UINT32)),
    ('barrier', FixedDataPacketField(MARKER_UINT32)),
    ('dtime', FixedDataPacketField(MARKER_UINT32)),
    ('flags', FixedDataPacketField(MARKER_UINT32)),
    ('sourceid', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(2)),
    ('root_x', FixedDataPacketField(MARKER_UINT32)),
    ('root_y', FixedDataPacketField(MARKER_UINT32)),
    ('dx', FixedDataPacketField(MARKER_UINT32)),
    ('dy', FixedDataPacketField(MARKER_UINT32)),
))


class BarrierHitEvent:
    __slots__ = ('response_type', 'extension', 'sequence', 'length', 'event_type', 'deviceid', 'time', 'eventid', 'root', 'event', 'barrier', 'dtime', 'flags', 'sourceid', 'root_x', 'root_y', 'dx', 'dy',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            extension: Optional[int] = None,
            sequence: Optional[int] = None,
            length: Optional[int] = None,
            event_type: Optional[int] = None,
            deviceid: Optional[int] = None,
            time: Optional[int] = None,
            eventid: Optional[int] = None,
            root: Optional[int] = None,
            event: Optional[int] = None,
            barrier: Optional[int] = None,
            dtime: Optional[int] = None,
            flags: Optional[int] = None,
            sourceid: Optional[int] = None,
            root_x: Optional[int] = None,
            root_y: Optional[int] = None,
            dx: Optional[int] = None,
            dy: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.extension = extension
        self.sequence = sequence
        self.length = length
        self.event_type = event_type
        self.deviceid = deviceid
        self.time = time
        self.eventid = eventid
        self.root = root
        self.event = event
        self.barrier = barrier
        self.dtime = dtime
        self.flags = flags
        self.sourceid = sourceid
        self.root_x = root_x
        self.root_y = root_y
        self.dx = dx
        self.dy = dy

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'extension': self.extension,
            'sequence': self.sequence,
            'length': self.length,
            'event_type': self.event_type,
            'deviceid': self.deviceid,
            'time': self.time,
            'eventid': self.eventid,
            'root': self.root,
            'event': self.event,
            'barrier': self.barrier,
            'dtime': self.dtime,
            'flags': self.flags,
            'sourceid': self.sourceid,
            'root_x': self.root_x,
            'root_y': self.root_y,
            'dx': self.dx,
            'dy': self.dy,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'BarrierHitEvent':
        return BarrierHitEvent(**BarrierHitEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return BarrierHitEventPacket.pack(**self.as_dict())


class BarrierHitEventCType(ctypes.Structure):
    """xinput BarrierHit"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("extension", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("length", ctypes.c_uint32),
        ("event_type", ctypes.c_uint16),
        ("deviceid", ctypes.c_uint32),
        ("time", ctypes.c_uint32),
        ("eventid", ctypes.c_uint32),
        ("root", ctypes.c_uint32),
        ("event", ctypes.c_uint32),
        ("barrier", ctypes.c_uint32),
        ("dtime", ctypes.c_uint32),
        ("flags", ctypes.c_uint32),
        ("sourceid", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 2),
        ("root_x", ctypes.c_uint32),
        ("root_y", ctypes.c_uint32),
        ("dx", ctypes.c_uint32),
        ("dy", ctypes.c_uint32),
    ]


GesturePinchBeginEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('extension', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('length', FixedDataPacketField(MARKER_UINT32)),
    ('event_type', FixedDataPacketField(MARKER_UINT16)),
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('detail', FixedDataPacketField(MARKER_UINT32)),
    ('root', FixedDataPacketField(MARKER_UINT32)),
    ('event', FixedDataPacketField(MARKER_UINT32)),
    ('child', FixedDataPacketField(MARKER_UINT32)),
    ('root_x', FixedDataPacketField(MARKER_UINT32)),
    ('root_y', FixedDataPacketField(MARKER_UINT32)),
    ('event_x', FixedDataPacketField(MARKER_UINT32)),
    ('event_y', FixedDataPacketField(MARKER_UINT32)),
    ('delta_x', FixedDataPacketField(MARKER_UINT32)),
    ('delta_y', FixedDataPacketField(MARKER_UINT32)),
    ('delta_unaccel_x', FixedDataPacketField(MARKER_UINT32)),
    ('delta_unaccel_y', FixedDataPacketField(MARKER_UINT32)),
    ('scale', FixedDataPacketField(MARKER_UINT32)),
    ('delta_angle', FixedDataPacketField(MARKER_UINT32)),
    ('sourceid', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(2)),
    ('mods', FixedDataPacketField(MARKER_UINT32)),
    ('group', FixedDataPacketField(MARKER_UINT32)),
    ('flags', FixedDataPacketField(MARKER_UINT32)),
))


class GesturePinchBeginEvent:
    __slots__ = ('response_type', 'extension', 'sequence', 'length', 'event_type', 'deviceid', 'time', 'detail', 'root', 'event', 'child', 'root_x', 'root_y', 'event_x', 'event_y', 'delta_x', 'delta_y', 'delta_unaccel_x', 'delta_unaccel_y', 'scale', 'delta_angle', 'sourceid', 'mods', 'group', 'flags',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            extension: Optional[int] = None,
            sequence: Optional[int] = None,
            length: Optional[int] = None,
            event_type: Optional[int] = None,
            deviceid: Optional[int] = None,
            time: Optional[int] = None,
            detail: Optional[int] = None,
            root: Optional[int] = None,
            event: Optional[int] = None,
            child: Optional[int] = None,
            root_x: Optional[int] = None,
            root_y: Optional[int] = None,
            event_x: Optional[int] = None,
            event_y: Optional[int] = None,
            delta_x: Optional[int] = None,
            delta_y: Optional[int] = None,
            delta_unaccel_x: Optional[int] = None,
            delta_unaccel_y: Optional[int] = None,
            scale: Optional[int] = None,
            delta_angle: Optional[int] = None,
            sourceid: Optional[int] = None,
            mods: Optional[int] = None,
            group: Optional[int] = None,
            flags: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.extension = extension
        self.sequence = sequence
        self.length = length
        self.event_type = event_type
        self.deviceid = deviceid
        self.time = time
        self.detail = detail
        self.root = root
        self.event = event
        self.child = child
        self.root_x = root_x
        self.root_y = root_y
        self.event_x = event_x
        self.event_y = event_y
        self.delta_x = delta_x
        self.delta_y = delta_y
        self.delta_unaccel_x = delta_unaccel_x
        self.delta_unaccel_y = delta_unaccel_y
        self.scale = scale
        self.delta_angle = delta_angle
        self.sourceid = sourceid
        self.mods = mods
        self.group = group
        self.flags = flags

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'extension': self.extension,
            'sequence': self.sequence,
            'length': self.length,
            'event_type': self.event_type,
            'deviceid': self.deviceid,
            'time': self.time,
            'detail': self.detail,
            'root': self.root,
            'event': self.event,
            'child': self.child,
            'root_x': self.root_x,
            'root_y': self.root_y,
            'event_x': self.event_x,
            'event_y': self.event_y,
            'delta_x': self.delta_x,
            'delta_y': self.delta_y,
            'delta_unaccel_x': self.delta_unaccel_x,
            'delta_unaccel_y': self.delta_unaccel_y,
            'scale': self.scale,
            'delta_angle': self.delta_angle,
            'sourceid': self.sourceid,
            'mods': self.mods,
            'group': self.group,
            'flags': self.flags,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GesturePinchBeginEvent':
        return GesturePinchBeginEvent(**GesturePinchBeginEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GesturePinchBeginEventPacket.pack(**self.as_dict())


class GesturePinchBeginEventCType(ctypes.Structure):
    """xinput GesturePinchBegin"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("extension", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("length", ctypes.c_uint32),
        ("event_type", ctypes.c_uint16),
        ("deviceid", ctypes.c_uint32),
        ("time", ctypes.c_uint32),
        ("detail", ctypes.c_uint32),
        ("root", ctypes.c_uint32),
        ("event", ctypes.c_uint32),
        ("child", ctypes.c_uint32),
        ("root_x", ctypes.c_uint32),
        ("root_y", ctypes.c_uint32),
        ("event_x", ctypes.c_uint32),
        ("event_y", ctypes.c_uint32),
        ("delta_x", ctypes.c_uint32),
        ("delta_y", ctypes.c_uint32),
        ("delta_unaccel_x", ctypes.c_uint32),
        ("delta_unaccel_y", ctypes.c_uint32),
        ("scale", ctypes.c_uint32),
        ("delta_angle", ctypes.c_uint32),
        ("sourceid", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 2),
        ("mods", ctypes.c_uint32),
        ("group", ctypes.c_uint32),
        ("flags", ctypes.c_uint32),
    ]


GestureSwipeBeginEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('extension', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('length', FixedDataPacketField(MARKER_UINT32)),
    ('event_type', FixedDataPacketField(MARKER_UINT16)),
    ('deviceid', FixedDataPacketField(MARKER_UINT32)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('detail', FixedDataPacketField(MARKER_UINT32)),
    ('root', FixedDataPacketField(MARKER_UINT32)),
    ('event', FixedDataPacketField(MARKER_UINT32)),
    ('child', FixedDataPacketField(MARKER_UINT32)),
    ('root_x', FixedDataPacketField(MARKER_UINT32)),
    ('root_y', FixedDataPacketField(MARKER_UINT32)),
    ('event_x', FixedDataPacketField(MARKER_UINT32)),
    ('event_y', FixedDataPacketField(MARKER_UINT32)),
    ('delta_x', FixedDataPacketField(MARKER_UINT32)),
    ('delta_y', FixedDataPacketField(MARKER_UINT32)),
    ('delta_unaccel_x', FixedDataPacketField(MARKER_UINT32)),
    ('delta_unaccel_y', FixedDataPacketField(MARKER_UINT32)),
    ('sourceid', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(2)),
    ('mods', FixedDataPacketField(MARKER_UINT32)),
    ('group', FixedDataPacketField(MARKER_UINT32)),
    ('flags', FixedDataPacketField(MARKER_UINT32)),
))


class GestureSwipeBeginEvent:
    __slots__ = ('response_type', 'extension', 'sequence', 'length', 'event_type', 'deviceid', 'time', 'detail', 'root', 'event', 'child', 'root_x', 'root_y', 'event_x', 'event_y', 'delta_x', 'delta_y', 'delta_unaccel_x', 'delta_unaccel_y', 'sourceid', 'mods', 'group', 'flags',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            extension: Optional[int] = None,
            sequence: Optional[int] = None,
            length: Optional[int] = None,
            event_type: Optional[int] = None,
            deviceid: Optional[int] = None,
            time: Optional[int] = None,
            detail: Optional[int] = None,
            root: Optional[int] = None,
            event: Optional[int] = None,
            child: Optional[int] = None,
            root_x: Optional[int] = None,
            root_y: Optional[int] = None,
            event_x: Optional[int] = None,
            event_y: Optional[int] = None,
            delta_x: Optional[int] = None,
            delta_y: Optional[int] = None,
            delta_unaccel_x: Optional[int] = None,
            delta_unaccel_y: Optional[int] = None,
            sourceid: Optional[int] = None,
            mods: Optional[int] = None,
            group: Optional[int] = None,
            flags: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.extension = extension
        self.sequence = sequence
        self.length = length
        self.event_type = event_type
        self.deviceid = deviceid
        self.time = time
        self.detail = detail
        self.root = root
        self.event = event
        self.child = child
        self.root_x = root_x
        self.root_y = root_y
        self.event_x = event_x
        self.event_y = event_y
        self.delta_x = delta_x
        self.delta_y = delta_y
        self.delta_unaccel_x = delta_unaccel_x
        self.delta_unaccel_y = delta_unaccel_y
        self.sourceid = sourceid
        self.mods = mods
        self.group = group
        self.flags = flags

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'extension': self.extension,
            'sequence': self.sequence,
            'length': self.length,
            'event_type': self.event_type,
            'deviceid': self.deviceid,
            'time': self.time,
            'detail': self.detail,
            'root': self.root,
            'event': self.event,
            'child': self.child,
            'root_x': self.root_x,
            'root_y': self.root_y,
            'event_x': self.event_x,
            'event_y': self.event_y,
            'delta_x': self.delta_x,
            'delta_y': self.delta_y,
            'delta_unaccel_x': self.delta_unaccel_x,
            'delta_unaccel_y': self.delta_unaccel_y,
            'sourceid': self.sourceid,
            'mods': self.mods,
            'group': self.group,
            'flags': self.flags,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GestureSwipeBeginEvent':
        return GestureSwipeBeginEvent(**GestureSwipeBeginEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GestureSwipeBeginEventPacket.pack(**self.as_dict())


class GestureSwipeBeginEventCType(ctypes.Structure):
    """xinput GestureSwipeBegin"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("extension", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("length", ctypes.c_uint32),
        ("event_type", ctypes.c_uint16),
        ("deviceid", ctypes.c_uint32),
        ("time", ctypes.c_uint32),
        ("detail", ctypes.c_uint32),
        ("root", ctypes.c_uint32),
        ("event", ctypes.c_uint32),
        ("child", ctypes.c_uint32),
        ("root_x", ctypes.c_uint32),
        ("root_y", ctypes.c_uint32),
        ("event_x", ctypes.c_uint32),
        ("event_y", ctypes.c_uint32),
        ("delta_x", ctypes.c_uint32),
        ("delta_y", ctypes.c_uint32),
        ("delta_unaccel_x", ctypes.c_uint32),
        ("delta_unaccel_y", ctypes.c_uint32),
        ("sourceid", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 2),
        ("mods", ctypes.c_uint32),
        ("group", ctypes.c_uint32),
        ("flags", ctypes.c_uint32),
    ]


SendExtensionEventRequestPacket = DataPacket((
    ('destination', FixedDataPacketField(MARKER_UINT32)),
    ('device_id', FixedDataPacketField(MARKER_UINT8)),
    ('propagate', FixedDataPacketField(MARKER_UINT8)),
    ('num_classes', FixedDataPacketField(MARKER_UINT16)),
    ('num_events', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
    ('events', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_events'], 0)),
    ('classes', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['num_classes'], 0)),
))


class SendExtensionEventRequest:
    OPCODE = 31

    __slots__ = ('destination', 'device_id', 'propagate', 'num_classes', 'num_events', 'events', 'classes',)

    def __init__(
            self, *,
            destination: Optional[int] = None,
            device_id: Optional[int] = None,
            propagate: Optional[bool] = None,
            num_classes: Optional[int] = None,
            num_events: Optional[int] = None,
            events: Optional[Sequence[int]] = None,
            classes: Optional[Sequence[int]] = None,
    ) -> None:
        self.destination = destination
        self.device_id = device_id
        self.propagate = propagate
        self.num_classes = num_classes
        self.num_events = num_events
        self.events = events
        self.classes = classes

    def as_dict(self) -> Dict[str, Any]:
        return {
            'destination': self.destination,
            'device_id': self.device_id,
            'propagate': self.propagate,
            'num_classes': self.num_classes,
            'num_events': self.num_events,
            'events': self.events,
            'classes': self.classes,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SendExtensionEventRequest':
        return SendExtensionEventRequest(**SendExtensionEventRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SendExtensionEventRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, bool, int, int, Sequence[int], Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SendExtensionEventRequest.lib = library.xinput_sendextensionevent
        SendExtensionEventRequest.lib.restype = ctypes.c_uint32
        SendExtensionEventRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint8, ctypes.c_int8, ctypes.c_uint16, ctypes.c_uint8, ctypes.c_uint8 * 3, ctypes.c_void_p, ctypes.c_void_p)


class SendExtensionEventRequestCType(ctypes.Structure):
    """xinput SendExtensionEvent"""
    _fields_ = [
        ("destination", ctypes.c_uint32),
        ("device_id", ctypes.c_uint8),
        ("propagate", ctypes.c_int8),
        ("num_classes", ctypes.c_uint16),
        ("num_events", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
        ("var_data", ctypes.c_void_p),
    ]


# ------------------------------------------------------------------
# Unions

