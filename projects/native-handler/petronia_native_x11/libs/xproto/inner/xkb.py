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

ConstType = NewType('ConstType', int)


class ConstValues:
    MAX_LEGAL_KEY_CODE = ConstType(255)
    PER_KEY_BIT_ARRAY_SIZE = ConstType(32)
    KEY_NAME_LENGTH = ConstType(4)


EventTypeType = NewType('EventTypeType', int)


class EventTypeValues:
    NEW_KEYBOARD_NOTIFY = EventTypeType(1)
    MAP_NOTIFY = EventTypeType(2)
    STATE_NOTIFY = EventTypeType(4)
    CONTROLS_NOTIFY = EventTypeType(8)
    INDICATOR_STATE_NOTIFY = EventTypeType(16)
    INDICATOR_MAP_NOTIFY = EventTypeType(32)
    NAMES_NOTIFY = EventTypeType(64)
    COMPAT_MAP_NOTIFY = EventTypeType(128)
    BELL_NOTIFY = EventTypeType(256)
    ACTION_MESSAGE = EventTypeType(512)
    ACCESS_XNOTIFY = EventTypeType(1024)
    EXTENSION_DEVICE_NOTIFY = EventTypeType(2048)


NkndetailType = NewType('NkndetailType', int)


class NkndetailValues:
    KEYCODES = NkndetailType(1)
    GEOMETRY = NkndetailType(2)
    DEVICE_ID = NkndetailType(4)


AxndetailType = NewType('AxndetailType', int)


class AxndetailValues:
    SKPRESS = AxndetailType(1)
    SKACCEPT = AxndetailType(2)
    SKREJECT = AxndetailType(4)
    SKRELEASE = AxndetailType(8)
    BKACCEPT = AxndetailType(16)
    BKREJECT = AxndetailType(32)
    AXKWARNING = AxndetailType(64)


MapPartType = NewType('MapPartType', int)


class MapPartValues:
    KEY_TYPES = MapPartType(1)
    KEY_SYMS = MapPartType(2)
    MODIFIER_MAP = MapPartType(4)
    EXPLICIT_COMPONENTS = MapPartType(8)
    KEY_ACTIONS = MapPartType(16)
    KEY_BEHAVIORS = MapPartType(32)
    VIRTUAL_MODS = MapPartType(64)
    VIRTUAL_MOD_MAP = MapPartType(128)


SetMapFlagsType = NewType('SetMapFlagsType', int)


class SetMapFlagsValues:
    RESIZE_TYPES = SetMapFlagsType(1)
    RECOMPUTE_ACTIONS = SetMapFlagsType(2)


StatePartType = NewType('StatePartType', int)


class StatePartValues:
    MODIFIER_STATE = StatePartType(1)
    MODIFIER_BASE = StatePartType(2)
    MODIFIER_LATCH = StatePartType(4)
    MODIFIER_LOCK = StatePartType(8)
    GROUP_STATE = StatePartType(16)
    GROUP_BASE = StatePartType(32)
    GROUP_LATCH = StatePartType(64)
    GROUP_LOCK = StatePartType(128)
    COMPAT_STATE = StatePartType(256)
    GRAB_MODS = StatePartType(512)
    COMPAT_GRAB_MODS = StatePartType(1024)
    LOOKUP_MODS = StatePartType(2048)
    COMPAT_LOOKUP_MODS = StatePartType(4096)
    POINTER_BUTTONS = StatePartType(8192)


BoolCtrlType = NewType('BoolCtrlType', int)


class BoolCtrlValues:
    REPEAT_KEYS = BoolCtrlType(1)
    SLOW_KEYS = BoolCtrlType(2)
    BOUNCE_KEYS = BoolCtrlType(4)
    STICKY_KEYS = BoolCtrlType(8)
    MOUSE_KEYS = BoolCtrlType(16)
    MOUSE_KEYS_ACCEL = BoolCtrlType(32)
    ACCESS_XKEYS = BoolCtrlType(64)
    ACCESS_XTIMEOUT_MASK = BoolCtrlType(128)
    ACCESS_XFEEDBACK_MASK = BoolCtrlType(256)
    AUDIBLE_BELL_MASK = BoolCtrlType(512)
    OVERLAY1MASK = BoolCtrlType(1024)
    OVERLAY2MASK = BoolCtrlType(2048)
    IGNORE_GROUP_LOCK_MASK = BoolCtrlType(4096)


ControlType = NewType('ControlType', int)


class ControlValues:
    GROUPS_WRAP = ControlType(134217728)
    INTERNAL_MODS = ControlType(268435456)
    IGNORE_LOCK_MODS = ControlType(536870912)
    PER_KEY_REPEAT = ControlType(1073741824)
    CONTROLS_ENABLED = ControlType(2147483648)


AxoptionType = NewType('AxoptionType', int)


class AxoptionValues:
    SKPRESS_FB = AxoptionType(1)
    SKACCEPT_FB = AxoptionType(2)
    FEATURE_FB = AxoptionType(4)
    SLOW_WARN_FB = AxoptionType(8)
    INDICATOR_FB = AxoptionType(16)
    STICKY_KEYS_FB = AxoptionType(32)
    TWO_KEYS = AxoptionType(64)
    LATCH_TO_LOCK = AxoptionType(128)
    SKRELEASE_FB = AxoptionType(256)
    SKREJECT_FB = AxoptionType(512)
    BKREJECT_FB = AxoptionType(1024)
    DUMB_BELL = AxoptionType(2048)


LedClassResultType = NewType('LedClassResultType', int)


class LedClassResultValues:
    KBD_FEEDBACK_CLASS = LedClassResultType(0)
    LED_FEEDBACK_CLASS = LedClassResultType(4)


LedClassType = NewType('LedClassType', int)


class LedClassValues:
    KBD_FEEDBACK_CLASS = LedClassType(0)
    LED_FEEDBACK_CLASS = LedClassType(4)
    DFLT_XICLASS = LedClassType(768)
    ALL_XICLASSES = LedClassType(1280)


BellClassResultType = NewType('BellClassResultType', int)


class BellClassResultValues:
    KBD_FEEDBACK_CLASS = BellClassResultType(0)
    BELL_FEEDBACK_CLASS = BellClassResultType(5)


BellClassType = NewType('BellClassType', int)


class BellClassValues:
    KBD_FEEDBACK_CLASS = BellClassType(0)
    BELL_FEEDBACK_CLASS = BellClassType(5)
    DFLT_XICLASS = BellClassType(768)


IdType = NewType('IdType', int)


class IdValues:
    USE_CORE_KBD = IdType(256)
    USE_CORE_PTR = IdType(512)
    DFLT_XICLASS = IdType(768)
    DFLT_XIID = IdType(1024)
    ALL_XICLASS = IdType(1280)
    ALL_XIID = IdType(1536)
    XINONE = IdType(65280)


GroupType = NewType('GroupType', int)


class GroupValues:
    V_1 = GroupType(0)
    V_2 = GroupType(1)
    V_3 = GroupType(2)
    V_4 = GroupType(3)


GroupsType = NewType('GroupsType', int)


class GroupsValues:
    ANY = GroupsType(254)
    ALL = GroupsType(255)


SetOfGroupType = NewType('SetOfGroupType', int)


class SetOfGroupValues:
    GROUP1 = SetOfGroupType(1)
    GROUP2 = SetOfGroupType(2)
    GROUP3 = SetOfGroupType(4)
    GROUP4 = SetOfGroupType(8)


SetOfGroupsType = NewType('SetOfGroupsType', int)


class SetOfGroupsValues:
    ANY = SetOfGroupsType(128)


GroupsWrapType = NewType('GroupsWrapType', int)


class GroupsWrapValues:
    WRAP_INTO_RANGE = GroupsWrapType(0)
    CLAMP_INTO_RANGE = GroupsWrapType(64)
    REDIRECT_INTO_RANGE = GroupsWrapType(128)


VmodsHighType = NewType('VmodsHighType', int)


class VmodsHighValues:
    V_15 = VmodsHighType(128)
    V_14 = VmodsHighType(64)
    V_13 = VmodsHighType(32)
    V_12 = VmodsHighType(16)
    V_11 = VmodsHighType(8)
    V_10 = VmodsHighType(4)
    V_9 = VmodsHighType(2)
    V_8 = VmodsHighType(1)


VmodsLowType = NewType('VmodsLowType', int)


class VmodsLowValues:
    V_7 = VmodsLowType(128)
    V_6 = VmodsLowType(64)
    V_5 = VmodsLowType(32)
    V_4 = VmodsLowType(16)
    V_3 = VmodsLowType(8)
    V_2 = VmodsLowType(4)
    V_1 = VmodsLowType(2)
    V_0 = VmodsLowType(1)


VmodType = NewType('VmodType', int)


class VmodValues:
    V_15 = VmodType(32768)
    V_14 = VmodType(16384)
    V_13 = VmodType(8192)
    V_12 = VmodType(4096)
    V_11 = VmodType(2048)
    V_10 = VmodType(1024)
    V_9 = VmodType(512)
    V_8 = VmodType(256)
    V_7 = VmodType(128)
    V_6 = VmodType(64)
    V_5 = VmodType(32)
    V_4 = VmodType(16)
    V_3 = VmodType(8)
    V_2 = VmodType(4)
    V_1 = VmodType(2)
    V_0 = VmodType(1)


ExplicitType = NewType('ExplicitType', int)


class ExplicitValues:
    VMOD_MAP = ExplicitType(128)
    BEHAVIOR = ExplicitType(64)
    AUTO_REPEAT = ExplicitType(32)
    INTERPRET = ExplicitType(16)
    KEY_TYPE4 = ExplicitType(8)
    KEY_TYPE3 = ExplicitType(4)
    KEY_TYPE2 = ExplicitType(2)
    KEY_TYPE1 = ExplicitType(1)


SymInterpretMatchType = NewType('SymInterpretMatchType', int)


class SymInterpretMatchValues:
    NONE_OF = SymInterpretMatchType(0)
    ANY_OF_OR_NONE = SymInterpretMatchType(1)
    ANY_OF = SymInterpretMatchType(2)
    ALL_OF = SymInterpretMatchType(3)
    EXACTLY = SymInterpretMatchType(4)


SymInterpMatchType = NewType('SymInterpMatchType', int)


class SymInterpMatchValues:
    LEVEL_ONE_ONLY = SymInterpMatchType(128)
    OP_MASK = SymInterpMatchType(127)


ImflagType = NewType('ImflagType', int)


class ImflagValues:
    NO_EXPLICIT = ImflagType(128)
    NO_AUTOMATIC = ImflagType(64)
    LEDDRIVES_KB = ImflagType(32)


ImmodsWhichType = NewType('ImmodsWhichType', int)


class ImmodsWhichValues:
    USE_COMPAT = ImmodsWhichType(16)
    USE_EFFECTIVE = ImmodsWhichType(8)
    USE_LOCKED = ImmodsWhichType(4)
    USE_LATCHED = ImmodsWhichType(2)
    USE_BASE = ImmodsWhichType(1)


ImgroupsWhichType = NewType('ImgroupsWhichType', int)


class ImgroupsWhichValues:
    USE_COMPAT = ImgroupsWhichType(16)
    USE_EFFECTIVE = ImgroupsWhichType(8)
    USE_LOCKED = ImgroupsWhichType(4)
    USE_LATCHED = ImgroupsWhichType(2)
    USE_BASE = ImgroupsWhichType(1)


CmdetailType = NewType('CmdetailType', int)


class CmdetailValues:
    SYM_INTERP = CmdetailType(1)
    GROUP_COMPAT = CmdetailType(2)


NameDetailType = NewType('NameDetailType', int)


class NameDetailValues:
    KEYCODES = NameDetailType(1)
    GEOMETRY = NameDetailType(2)
    SYMBOLS = NameDetailType(4)
    PHYS_SYMBOLS = NameDetailType(8)
    TYPES = NameDetailType(16)
    COMPAT = NameDetailType(32)
    KEY_TYPE_NAMES = NameDetailType(64)
    KTLEVEL_NAMES = NameDetailType(128)
    INDICATOR_NAMES = NameDetailType(256)
    KEY_NAMES = NameDetailType(512)
    KEY_ALIASES = NameDetailType(1024)
    VIRTUAL_MOD_NAMES = NameDetailType(2048)
    GROUP_NAMES = NameDetailType(4096)
    RGNAMES = NameDetailType(8192)


GbndetailType = NewType('GbndetailType', int)


class GbndetailValues:
    TYPES = GbndetailType(1)
    COMPAT_MAP = GbndetailType(2)
    CLIENT_SYMBOLS = GbndetailType(4)
    SERVER_SYMBOLS = GbndetailType(8)
    INDICATOR_MAPS = GbndetailType(16)
    KEY_NAMES = GbndetailType(32)
    GEOMETRY = GbndetailType(64)
    OTHER_NAMES = GbndetailType(128)


XifeatureType = NewType('XifeatureType', int)


class XifeatureValues:
    KEYBOARDS = XifeatureType(1)
    BUTTON_ACTIONS = XifeatureType(2)
    INDICATOR_NAMES = XifeatureType(4)
    INDICATOR_MAPS = XifeatureType(8)
    INDICATOR_STATE = XifeatureType(16)


PerClientFlagType = NewType('PerClientFlagType', int)


class PerClientFlagValues:
    DETECTABLE_AUTO_REPEAT = PerClientFlagType(1)
    GRABS_USE_XKBSTATE = PerClientFlagType(2)
    AUTO_RESET_CONTROLS = PerClientFlagType(4)
    LOOKUP_STATE_WHEN_GRABBED = PerClientFlagType(8)
    SEND_EVENT_USES_XKBSTATE = PerClientFlagType(16)


BehaviorTypeType = NewType('BehaviorTypeType', int)


class BehaviorTypeValues:
    DEFAULT = BehaviorTypeType(0)
    LOCK = BehaviorTypeType(1)
    RADIO_GROUP = BehaviorTypeType(2)
    OVERLAY1 = BehaviorTypeType(3)
    OVERLAY2 = BehaviorTypeType(4)
    PERMAMENT_LOCK = BehaviorTypeType(129)
    PERMAMENT_RADIO_GROUP = BehaviorTypeType(130)
    PERMAMENT_OVERLAY1 = BehaviorTypeType(131)
    PERMAMENT_OVERLAY2 = BehaviorTypeType(132)


DoodadTypeType = NewType('DoodadTypeType', int)


class DoodadTypeValues:
    OUTLINE = DoodadTypeType(1)
    SOLID = DoodadTypeType(2)
    TEXT = DoodadTypeType(3)
    INDICATOR = DoodadTypeType(4)
    LOGO = DoodadTypeType(5)


ErrorType = NewType('ErrorType', int)


class ErrorValues:
    BAD_DEVICE = ErrorType(255)
    BAD_CLASS = ErrorType(254)
    BAD_ID = ErrorType(253)


SaType = NewType('SaType', int)


class SaValues:
    CLEAR_LOCKS = SaType(1)
    LATCH_TO_LOCK = SaType(2)
    USE_MOD_MAP_MODS = SaType(4)
    GROUP_ABSOLUTE = SaType(4)


SatypeType = NewType('SatypeType', int)


class SatypeValues:
    NO_ACTION = SatypeType(0)
    SET_MODS = SatypeType(1)
    LATCH_MODS = SatypeType(2)
    LOCK_MODS = SatypeType(3)
    SET_GROUP = SatypeType(4)
    LATCH_GROUP = SatypeType(5)
    LOCK_GROUP = SatypeType(6)
    MOVE_PTR = SatypeType(7)
    PTR_BTN = SatypeType(8)
    LOCK_PTR_BTN = SatypeType(9)
    SET_PTR_DFLT = SatypeType(10)
    ISOLOCK = SatypeType(11)
    TERMINATE = SatypeType(12)
    SWITCH_SCREEN = SatypeType(13)
    SET_CONTROLS = SatypeType(14)
    LOCK_CONTROLS = SatypeType(15)
    ACTION_MESSAGE = SatypeType(16)
    REDIRECT_KEY = SatypeType(17)
    DEVICE_BTN = SatypeType(18)
    LOCK_DEVICE_BTN = SatypeType(19)
    DEVICE_VALUATOR = SatypeType(20)


SamovePtrFlagType = NewType('SamovePtrFlagType', int)


class SamovePtrFlagValues:
    NO_ACCELERATION = SamovePtrFlagType(1)
    MOVE_ABSOLUTE_X = SamovePtrFlagType(2)
    MOVE_ABSOLUTE_Y = SamovePtrFlagType(4)


SasetPtrDfltFlagType = NewType('SasetPtrDfltFlagType', int)


class SasetPtrDfltFlagValues:
    DFLT_BTN_ABSOLUTE = SasetPtrDfltFlagType(4)
    AFFECT_DFLT_BUTTON = SasetPtrDfltFlagType(1)


SaisoLockFlagType = NewType('SaisoLockFlagType', int)


class SaisoLockFlagValues:
    NO_LOCK = SaisoLockFlagType(1)
    NO_UNLOCK = SaisoLockFlagType(2)
    USE_MOD_MAP_MODS = SaisoLockFlagType(4)
    GROUP_ABSOLUTE = SaisoLockFlagType(4)
    ISODFLT_IS_GROUP = SaisoLockFlagType(8)


SaisoLockNoAffectType = NewType('SaisoLockNoAffectType', int)


class SaisoLockNoAffectValues:
    CTRLS = SaisoLockNoAffectType(8)
    PTR = SaisoLockNoAffectType(16)
    GROUP = SaisoLockNoAffectType(32)
    MODS = SaisoLockNoAffectType(64)


SwitchScreenFlagType = NewType('SwitchScreenFlagType', int)


class SwitchScreenFlagValues:
    APPLICATION = SwitchScreenFlagType(1)
    ABSOLUTE = SwitchScreenFlagType(4)


BoolCtrlsHighType = NewType('BoolCtrlsHighType', int)


class BoolCtrlsHighValues:
    ACCESS_XFEEDBACK = BoolCtrlsHighType(1)
    AUDIBLE_BELL = BoolCtrlsHighType(2)
    OVERLAY1 = BoolCtrlsHighType(4)
    OVERLAY2 = BoolCtrlsHighType(8)
    IGNORE_GROUP_LOCK = BoolCtrlsHighType(16)


BoolCtrlsLowType = NewType('BoolCtrlsLowType', int)


class BoolCtrlsLowValues:
    REPEAT_KEYS = BoolCtrlsLowType(1)
    SLOW_KEYS = BoolCtrlsLowType(2)
    BOUNCE_KEYS = BoolCtrlsLowType(4)
    STICKY_KEYS = BoolCtrlsLowType(8)
    MOUSE_KEYS = BoolCtrlsLowType(16)
    MOUSE_KEYS_ACCEL = BoolCtrlsLowType(32)
    ACCESS_XKEYS = BoolCtrlsLowType(64)
    ACCESS_XTIMEOUT = BoolCtrlsLowType(128)


ActionMessageFlagType = NewType('ActionMessageFlagType', int)


class ActionMessageFlagValues:
    ON_PRESS = ActionMessageFlagType(1)
    ON_RELEASE = ActionMessageFlagType(2)
    GEN_KEY_EVENT = ActionMessageFlagType(4)


LockDeviceFlagsType = NewType('LockDeviceFlagsType', int)


class LockDeviceFlagsValues:
    NO_LOCK = LockDeviceFlagsType(1)
    NO_UNLOCK = LockDeviceFlagsType(2)


SavalWhatType = NewType('SavalWhatType', int)


class SavalWhatValues:
    IGNORE_VAL = SavalWhatType(0)
    SET_VAL_MIN = SavalWhatType(1)
    SET_VAL_CENTER = SavalWhatType(2)
    SET_VAL_MAX = SavalWhatType(3)
    SET_VAL_RELATIVE = SavalWhatType(4)
    SET_VAL_ABSOLUTE = SavalWhatType(5)


# ------------------------------------------------------------------
# Aliases



# ------------------------------------------------------------------
# Structures, Events, Requests, Replies


IndicatorMapStructPacket = DataPacket((
    ('flags', FixedDataPacketField(MARKER_UINT8)),
    ('whichGroups', FixedDataPacketField(MARKER_UINT8)),
    ('groups', FixedDataPacketField(MARKER_UINT8)),
    ('whichMods', FixedDataPacketField(MARKER_UINT8)),
    ('mods', FixedDataPacketField(MARKER_UINT8)),
    ('realMods', FixedDataPacketField(MARKER_UINT8)),
    ('vmods', FixedDataPacketField(MARKER_UINT16)),
    ('ctrls', FixedDataPacketField(MARKER_UINT32)),
))


class IndicatorMapStruct:
    __slots__ = ('flags', 'whichgroups', 'groups', 'whichmods', 'mods', 'realmods', 'vmods', 'ctrls',)

    def __init__(
            self, *,
            flags: Optional[int] = None,
            whichgroups: Optional[int] = None,
            groups: Optional[int] = None,
            whichmods: Optional[int] = None,
            mods: Optional[int] = None,
            realmods: Optional[int] = None,
            vmods: Optional[int] = None,
            ctrls: Optional[int] = None,
    ) -> None:
        self.flags = flags
        self.whichgroups = whichgroups
        self.groups = groups
        self.whichmods = whichmods
        self.mods = mods
        self.realmods = realmods
        self.vmods = vmods
        self.ctrls = ctrls

    def as_dict(self) -> Dict[str, Any]:
        return {
            'flags': self.flags,
            'whichGroups': self.whichgroups,
            'groups': self.groups,
            'whichMods': self.whichmods,
            'mods': self.mods,
            'realMods': self.realmods,
            'vmods': self.vmods,
            'ctrls': self.ctrls,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'IndicatorMapStruct':
        return IndicatorMapStruct(**IndicatorMapStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return IndicatorMapStructPacket.pack(**self.as_dict())


class IndicatorMapStructCType(ctypes.Structure):
    """xkb IndicatorMap"""
    _fields_ = [
        ("flags", ctypes.c_uint8),
        ("whichGroups", ctypes.c_uint8),
        ("groups", ctypes.c_uint8),
        ("whichMods", ctypes.c_uint8),
        ("mods", ctypes.c_uint8),
        ("realMods", ctypes.c_uint8),
        ("vmods", ctypes.c_uint16),
        ("ctrls", ctypes.c_uint32),
    ]


ModDefStructPacket = DataPacket((
    ('mask', FixedDataPacketField(MARKER_UINT8)),
    ('realMods', FixedDataPacketField(MARKER_UINT8)),
    ('vmods', FixedDataPacketField(MARKER_UINT16)),
))


class ModDefStruct:
    __slots__ = ('mask', 'realmods', 'vmods',)

    def __init__(
            self, *,
            mask: Optional[int] = None,
            realmods: Optional[int] = None,
            vmods: Optional[int] = None,
    ) -> None:
        self.mask = mask
        self.realmods = realmods
        self.vmods = vmods

    def as_dict(self) -> Dict[str, Any]:
        return {
            'mask': self.mask,
            'realMods': self.realmods,
            'vmods': self.vmods,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ModDefStruct':
        return ModDefStruct(**ModDefStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ModDefStructPacket.pack(**self.as_dict())


class ModDefStructCType(ctypes.Structure):
    """xkb ModDef"""
    _fields_ = [
        ("mask", ctypes.c_uint8),
        ("realMods", ctypes.c_uint8),
        ("vmods", ctypes.c_uint16),
    ]


KeyNameStructPacket = DataPacket((
    ('name', SimpleListDataPacketField(MARKER_INT8, lambda d, c: 4, 0)),
))


class KeyNameStruct:
    __slots__ = ('name',)

    def __init__(
            self, *,
            name: Optional[Sequence[int]] = None,
    ) -> None:
        self.name = name

    def as_dict(self) -> Dict[str, Any]:
        return {
            'name': self.name,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'KeyNameStruct':
        return KeyNameStruct(**KeyNameStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return KeyNameStructPacket.pack(**self.as_dict())


class KeyNameStructCType(ctypes.Structure):
    """xkb KeyName"""
    _fields_ = [
        ("var_data", ctypes.c_void_p),
    ]


KeyAliasStructPacket = DataPacket((
    ('real', SimpleListDataPacketField(MARKER_INT8, lambda d, c: 4, 0)),
    ('alias', SimpleListDataPacketField(MARKER_INT8, lambda d, c: 4, 0)),
))


class KeyAliasStruct:
    __slots__ = ('real', 'alias',)

    def __init__(
            self, *,
            real: Optional[Sequence[int]] = None,
            alias: Optional[Sequence[int]] = None,
    ) -> None:
        self.real = real
        self.alias = alias

    def as_dict(self) -> Dict[str, Any]:
        return {
            'real': self.real,
            'alias': self.alias,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'KeyAliasStruct':
        return KeyAliasStruct(**KeyAliasStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return KeyAliasStructPacket.pack(**self.as_dict())


class KeyAliasStructCType(ctypes.Structure):
    """xkb KeyAlias"""
    _fields_ = [
        ("var_data", ctypes.c_void_p),
    ]


CountedString16StructPacket = DataPacket((
    ('length', FixedDataPacketField(MARKER_UINT16)),
    ('string', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['length'], 0)),
    ('alignment_pad', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: (((d['length']) + (5)) & (~(3))) - ((d['length']) + (2)), 0)),
))


class CountedString16Struct:
    __slots__ = ('length', 'string', 'alignment_pad',)

    def __init__(
            self, *,
            length: Optional[int] = None,
            string: Optional[Sequence[int]] = None,
            alignment_pad: Optional[Sequence[None]] = None,
    ) -> None:
        self.length = length
        self.string = string
        self.alignment_pad = alignment_pad

    def as_dict(self) -> Dict[str, Any]:
        return {
            'length': self.length,
            'string': self.string,
            'alignment_pad': self.alignment_pad,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CountedString16Struct':
        return CountedString16Struct(**CountedString16StructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CountedString16StructPacket.pack(**self.as_dict())


class CountedString16StructCType(ctypes.Structure):
    """xkb CountedString16"""
    _fields_ = [
        ("length", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


KtmapEntryStructPacket = DataPacket((
    ('active', FixedDataPacketField(MARKER_UINT8)),
    ('mods_mask', FixedDataPacketField(MARKER_UINT8)),
    ('level', FixedDataPacketField(MARKER_UINT8)),
    ('mods_mods', FixedDataPacketField(MARKER_UINT8)),
    ('mods_vmods', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
))


class KtmapEntryStruct:
    __slots__ = ('active', 'mods_mask', 'level', 'mods_mods', 'mods_vmods',)

    def __init__(
            self, *,
            active: Optional[bool] = None,
            mods_mask: Optional[int] = None,
            level: Optional[int] = None,
            mods_mods: Optional[int] = None,
            mods_vmods: Optional[int] = None,
    ) -> None:
        self.active = active
        self.mods_mask = mods_mask
        self.level = level
        self.mods_mods = mods_mods
        self.mods_vmods = mods_vmods

    def as_dict(self) -> Dict[str, Any]:
        return {
            'active': self.active,
            'mods_mask': self.mods_mask,
            'level': self.level,
            'mods_mods': self.mods_mods,
            'mods_vmods': self.mods_vmods,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'KtmapEntryStruct':
        return KtmapEntryStruct(**KtmapEntryStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return KtmapEntryStructPacket.pack(**self.as_dict())


class KtmapEntryStructCType(ctypes.Structure):
    """xkb KTMapEntry"""
    _fields_ = [
        ("active", ctypes.c_int8),
        ("mods_mask", ctypes.c_uint8),
        ("level", ctypes.c_uint8),
        ("mods_mods", ctypes.c_uint8),
        ("mods_vmods", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
    ]


KeyTypeStructPacket = DataPacket((
    ('mods_mask', FixedDataPacketField(MARKER_UINT8)),
    ('mods_mods', FixedDataPacketField(MARKER_UINT8)),
    ('mods_vmods', FixedDataPacketField(MARKER_UINT16)),
    ('numLevels', FixedDataPacketField(MARKER_UINT8)),
    ('nMapEntries', FixedDataPacketField(MARKER_UINT8)),
    ('hasPreserve', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('map', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nMapEntries'], 0)),
    ('preserve', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: (d['hasPreserve']) * (d['nMapEntries']), 0)),
))


class KeyTypeStruct:
    __slots__ = ('mods_mask', 'mods_mods', 'mods_vmods', 'numlevels', 'nmapentries', 'haspreserve', 'map', 'preserve',)

    def __init__(
            self, *,
            mods_mask: Optional[int] = None,
            mods_mods: Optional[int] = None,
            mods_vmods: Optional[int] = None,
            numlevels: Optional[int] = None,
            nmapentries: Optional[int] = None,
            haspreserve: Optional[bool] = None,
            map: Optional[Sequence[int]] = None,
            preserve: Optional[Sequence[int]] = None,
    ) -> None:
        self.mods_mask = mods_mask
        self.mods_mods = mods_mods
        self.mods_vmods = mods_vmods
        self.numlevels = numlevels
        self.nmapentries = nmapentries
        self.haspreserve = haspreserve
        self.map = map
        self.preserve = preserve

    def as_dict(self) -> Dict[str, Any]:
        return {
            'mods_mask': self.mods_mask,
            'mods_mods': self.mods_mods,
            'mods_vmods': self.mods_vmods,
            'numLevels': self.numlevels,
            'nMapEntries': self.nmapentries,
            'hasPreserve': self.haspreserve,
            'map': self.map,
            'preserve': self.preserve,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'KeyTypeStruct':
        return KeyTypeStruct(**KeyTypeStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return KeyTypeStructPacket.pack(**self.as_dict())


class KeyTypeStructCType(ctypes.Structure):
    """xkb KeyType"""
    _fields_ = [
        ("mods_mask", ctypes.c_uint8),
        ("mods_mods", ctypes.c_uint8),
        ("mods_vmods", ctypes.c_uint16),
        ("numLevels", ctypes.c_uint8),
        ("nMapEntries", ctypes.c_uint8),
        ("hasPreserve", ctypes.c_int8),
        ("pad0", ctypes.c_uint8),
        ("var_data", ctypes.c_void_p),
    ]


KeySymMapStructPacket = DataPacket((
    ('kt_index', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: 4, 0)),
    ('groupInfo', FixedDataPacketField(MARKER_UINT8)),
    ('width', FixedDataPacketField(MARKER_UINT8)),
    ('nSyms', FixedDataPacketField(MARKER_UINT16)),
    ('syms', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nSyms'], 0)),
))


class KeySymMapStruct:
    __slots__ = ('kt_index', 'groupinfo', 'width', 'nsyms', 'syms',)

    def __init__(
            self, *,
            kt_index: Optional[Sequence[int]] = None,
            groupinfo: Optional[int] = None,
            width: Optional[int] = None,
            nsyms: Optional[int] = None,
            syms: Optional[Sequence[int]] = None,
    ) -> None:
        self.kt_index = kt_index
        self.groupinfo = groupinfo
        self.width = width
        self.nsyms = nsyms
        self.syms = syms

    def as_dict(self) -> Dict[str, Any]:
        return {
            'kt_index': self.kt_index,
            'groupInfo': self.groupinfo,
            'width': self.width,
            'nSyms': self.nsyms,
            'syms': self.syms,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'KeySymMapStruct':
        return KeySymMapStruct(**KeySymMapStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return KeySymMapStructPacket.pack(**self.as_dict())


class KeySymMapStructCType(ctypes.Structure):
    """xkb KeySymMap"""
    _fields_ = [
        ("var_data", ctypes.c_void_p),
    ]


CommonBehaviorStructPacket = DataPacket((
    ('type', FixedDataPacketField(MARKER_UINT8)),
    ('data', FixedDataPacketField(MARKER_UINT8)),
))


class CommonBehaviorStruct:
    __slots__ = ('type', 'data',)

    def __init__(
            self, *,
            type: Optional[int] = None,
            data: Optional[int] = None,
    ) -> None:
        self.type = type
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CommonBehaviorStruct':
        return CommonBehaviorStruct(**CommonBehaviorStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CommonBehaviorStructPacket.pack(**self.as_dict())


class CommonBehaviorStructCType(ctypes.Structure):
    """xkb CommonBehavior"""
    _fields_ = [
        ("type", ctypes.c_uint8),
        ("data", ctypes.c_uint8),
    ]


DefaultBehaviorStructPacket = DataPacket((
    ('type', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
))


class DefaultBehaviorStruct:
    __slots__ = ('type',)

    def __init__(
            self, *,
            type: Optional[int] = None,
    ) -> None:
        self.type = type

    def as_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DefaultBehaviorStruct':
        return DefaultBehaviorStruct(**DefaultBehaviorStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DefaultBehaviorStructPacket.pack(**self.as_dict())


class DefaultBehaviorStructCType(ctypes.Structure):
    """xkb DefaultBehavior"""
    _fields_ = [
        ("type", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
    ]


RadioGroupBehaviorStructPacket = DataPacket((
    ('type', FixedDataPacketField(MARKER_UINT8)),
    ('group', FixedDataPacketField(MARKER_UINT8)),
))


class RadioGroupBehaviorStruct:
    __slots__ = ('type', 'group',)

    def __init__(
            self, *,
            type: Optional[int] = None,
            group: Optional[int] = None,
    ) -> None:
        self.type = type
        self.group = group

    def as_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type,
            'group': self.group,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'RadioGroupBehaviorStruct':
        return RadioGroupBehaviorStruct(**RadioGroupBehaviorStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return RadioGroupBehaviorStructPacket.pack(**self.as_dict())


class RadioGroupBehaviorStructCType(ctypes.Structure):
    """xkb RadioGroupBehavior"""
    _fields_ = [
        ("type", ctypes.c_uint8),
        ("group", ctypes.c_uint8),
    ]


OverlayBehaviorStructPacket = DataPacket((
    ('type', FixedDataPacketField(MARKER_UINT8)),
    ('key', FixedDataPacketField(MARKER_UINT32)),
))


class OverlayBehaviorStruct:
    __slots__ = ('type', 'key',)

    def __init__(
            self, *,
            type: Optional[int] = None,
            key: Optional[int] = None,
    ) -> None:
        self.type = type
        self.key = key

    def as_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type,
            'key': self.key,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'OverlayBehaviorStruct':
        return OverlayBehaviorStruct(**OverlayBehaviorStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return OverlayBehaviorStructPacket.pack(**self.as_dict())


class OverlayBehaviorStructCType(ctypes.Structure):
    """xkb OverlayBehavior"""
    _fields_ = [
        ("type", ctypes.c_uint8),
        ("key", ctypes.c_uint32),
    ]


SetBehaviorStructPacket = DataPacket((
    ('keycode', FixedDataPacketField(MARKER_UINT32)),
    ('behavior', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(1)),
))


class SetBehaviorStruct:
    __slots__ = ('keycode', 'behavior',)

    def __init__(
            self, *,
            keycode: Optional[int] = None,
            behavior: Optional[int] = None,
    ) -> None:
        self.keycode = keycode
        self.behavior = behavior

    def as_dict(self) -> Dict[str, Any]:
        return {
            'keycode': self.keycode,
            'behavior': self.behavior,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetBehaviorStruct':
        return SetBehaviorStruct(**SetBehaviorStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetBehaviorStructPacket.pack(**self.as_dict())


class SetBehaviorStructCType(ctypes.Structure):
    """xkb SetBehavior"""
    _fields_ = [
        ("keycode", ctypes.c_uint32),
        ("behavior", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8),
    ]


SetExplicitStructPacket = DataPacket((
    ('keycode', FixedDataPacketField(MARKER_UINT32)),
    ('explicit', FixedDataPacketField(MARKER_UINT8)),
))


class SetExplicitStruct:
    __slots__ = ('keycode', 'explicit',)

    def __init__(
            self, *,
            keycode: Optional[int] = None,
            explicit: Optional[int] = None,
    ) -> None:
        self.keycode = keycode
        self.explicit = explicit

    def as_dict(self) -> Dict[str, Any]:
        return {
            'keycode': self.keycode,
            'explicit': self.explicit,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetExplicitStruct':
        return SetExplicitStruct(**SetExplicitStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetExplicitStructPacket.pack(**self.as_dict())


class SetExplicitStructCType(ctypes.Structure):
    """xkb SetExplicit"""
    _fields_ = [
        ("keycode", ctypes.c_uint32),
        ("explicit", ctypes.c_uint8),
    ]


KeyModMapStructPacket = DataPacket((
    ('keycode', FixedDataPacketField(MARKER_UINT32)),
    ('mods', FixedDataPacketField(MARKER_UINT8)),
))


class KeyModMapStruct:
    __slots__ = ('keycode', 'mods',)

    def __init__(
            self, *,
            keycode: Optional[int] = None,
            mods: Optional[int] = None,
    ) -> None:
        self.keycode = keycode
        self.mods = mods

    def as_dict(self) -> Dict[str, Any]:
        return {
            'keycode': self.keycode,
            'mods': self.mods,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'KeyModMapStruct':
        return KeyModMapStruct(**KeyModMapStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return KeyModMapStructPacket.pack(**self.as_dict())


class KeyModMapStructCType(ctypes.Structure):
    """xkb KeyModMap"""
    _fields_ = [
        ("keycode", ctypes.c_uint32),
        ("mods", ctypes.c_uint8),
    ]


KeyVmodMapStructPacket = DataPacket((
    ('keycode', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(1)),
    ('vmods', FixedDataPacketField(MARKER_UINT16)),
))


class KeyVmodMapStruct:
    __slots__ = ('keycode', 'vmods',)

    def __init__(
            self, *,
            keycode: Optional[int] = None,
            vmods: Optional[int] = None,
    ) -> None:
        self.keycode = keycode
        self.vmods = vmods

    def as_dict(self) -> Dict[str, Any]:
        return {
            'keycode': self.keycode,
            'vmods': self.vmods,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'KeyVmodMapStruct':
        return KeyVmodMapStruct(**KeyVmodMapStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return KeyVmodMapStructPacket.pack(**self.as_dict())


class KeyVmodMapStructCType(ctypes.Structure):
    """xkb KeyVModMap"""
    _fields_ = [
        ("keycode", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8),
        ("vmods", ctypes.c_uint16),
    ]


KtsetMapEntryStructPacket = DataPacket((
    ('level', FixedDataPacketField(MARKER_UINT8)),
    ('realMods', FixedDataPacketField(MARKER_UINT8)),
    ('virtualMods', FixedDataPacketField(MARKER_UINT16)),
))


class KtsetMapEntryStruct:
    __slots__ = ('level', 'realmods', 'virtualmods',)

    def __init__(
            self, *,
            level: Optional[int] = None,
            realmods: Optional[int] = None,
            virtualmods: Optional[int] = None,
    ) -> None:
        self.level = level
        self.realmods = realmods
        self.virtualmods = virtualmods

    def as_dict(self) -> Dict[str, Any]:
        return {
            'level': self.level,
            'realMods': self.realmods,
            'virtualMods': self.virtualmods,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'KtsetMapEntryStruct':
        return KtsetMapEntryStruct(**KtsetMapEntryStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return KtsetMapEntryStructPacket.pack(**self.as_dict())


class KtsetMapEntryStructCType(ctypes.Structure):
    """xkb KTSetMapEntry"""
    _fields_ = [
        ("level", ctypes.c_uint8),
        ("realMods", ctypes.c_uint8),
        ("virtualMods", ctypes.c_uint16),
    ]


SetKeyTypeStructPacket = DataPacket((
    ('mask', FixedDataPacketField(MARKER_UINT8)),
    ('realMods', FixedDataPacketField(MARKER_UINT8)),
    ('virtualMods', FixedDataPacketField(MARKER_UINT16)),
    ('numLevels', FixedDataPacketField(MARKER_UINT8)),
    ('nMapEntries', FixedDataPacketField(MARKER_UINT8)),
    ('preserve', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('entries', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nMapEntries'], 0)),
    ('preserve_entries', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: (d['preserve']) * (d['nMapEntries']), 0)),
))


class SetKeyTypeStruct:
    __slots__ = ('mask', 'realmods', 'virtualmods', 'numlevels', 'nmapentries', 'preserve', 'entries', 'preserve_entries',)

    def __init__(
            self, *,
            mask: Optional[int] = None,
            realmods: Optional[int] = None,
            virtualmods: Optional[int] = None,
            numlevels: Optional[int] = None,
            nmapentries: Optional[int] = None,
            preserve: Optional[bool] = None,
            entries: Optional[Sequence[int]] = None,
            preserve_entries: Optional[Sequence[int]] = None,
    ) -> None:
        self.mask = mask
        self.realmods = realmods
        self.virtualmods = virtualmods
        self.numlevels = numlevels
        self.nmapentries = nmapentries
        self.preserve = preserve
        self.entries = entries
        self.preserve_entries = preserve_entries

    def as_dict(self) -> Dict[str, Any]:
        return {
            'mask': self.mask,
            'realMods': self.realmods,
            'virtualMods': self.virtualmods,
            'numLevels': self.numlevels,
            'nMapEntries': self.nmapentries,
            'preserve': self.preserve,
            'entries': self.entries,
            'preserve_entries': self.preserve_entries,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetKeyTypeStruct':
        return SetKeyTypeStruct(**SetKeyTypeStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetKeyTypeStructPacket.pack(**self.as_dict())


class SetKeyTypeStructCType(ctypes.Structure):
    """xkb SetKeyType"""
    _fields_ = [
        ("mask", ctypes.c_uint8),
        ("realMods", ctypes.c_uint8),
        ("virtualMods", ctypes.c_uint16),
        ("numLevels", ctypes.c_uint8),
        ("nMapEntries", ctypes.c_uint8),
        ("preserve", ctypes.c_int8),
        ("pad0", ctypes.c_uint8),
        ("var_data", ctypes.c_void_p),
    ]


OutlineStructPacket = DataPacket((
    ('nPoints', FixedDataPacketField(MARKER_UINT8)),
    ('cornerRadius', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
    ('points', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nPoints'], 0)),
))


class OutlineStruct:
    __slots__ = ('npoints', 'cornerradius', 'points',)

    def __init__(
            self, *,
            npoints: Optional[int] = None,
            cornerradius: Optional[int] = None,
            points: Optional[Sequence[int]] = None,
    ) -> None:
        self.npoints = npoints
        self.cornerradius = cornerradius
        self.points = points

    def as_dict(self) -> Dict[str, Any]:
        return {
            'nPoints': self.npoints,
            'cornerRadius': self.cornerradius,
            'points': self.points,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'OutlineStruct':
        return OutlineStruct(**OutlineStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return OutlineStructPacket.pack(**self.as_dict())


class OutlineStructCType(ctypes.Structure):
    """xkb Outline"""
    _fields_ = [
        ("nPoints", ctypes.c_uint8),
        ("cornerRadius", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


ShapeStructPacket = DataPacket((
    ('name', FixedDataPacketField(MARKER_UINT32)),
    ('nOutlines', FixedDataPacketField(MARKER_UINT8)),
    ('primaryNdx', FixedDataPacketField(MARKER_UINT8)),
    ('approxNdx', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('outlines', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nOutlines'], 0)),
))


class ShapeStruct:
    __slots__ = ('name', 'noutlines', 'primaryndx', 'approxndx', 'outlines',)

    def __init__(
            self, *,
            name: Optional[int] = None,
            noutlines: Optional[int] = None,
            primaryndx: Optional[int] = None,
            approxndx: Optional[int] = None,
            outlines: Optional[Sequence[int]] = None,
    ) -> None:
        self.name = name
        self.noutlines = noutlines
        self.primaryndx = primaryndx
        self.approxndx = approxndx
        self.outlines = outlines

    def as_dict(self) -> Dict[str, Any]:
        return {
            'name': self.name,
            'nOutlines': self.noutlines,
            'primaryNdx': self.primaryndx,
            'approxNdx': self.approxndx,
            'outlines': self.outlines,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ShapeStruct':
        return ShapeStruct(**ShapeStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ShapeStructPacket.pack(**self.as_dict())


class ShapeStructCType(ctypes.Structure):
    """xkb Shape"""
    _fields_ = [
        ("name", ctypes.c_uint32),
        ("nOutlines", ctypes.c_uint8),
        ("primaryNdx", ctypes.c_uint8),
        ("approxNdx", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
        ("var_data", ctypes.c_void_p),
    ]


KeyStructPacket = DataPacket((
    ('name', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 4, 0)),
    ('gap', FixedDataPacketField(MARKER_INT16)),
    ('shapeNdx', FixedDataPacketField(MARKER_UINT8)),
    ('colorNdx', FixedDataPacketField(MARKER_UINT8)),
))


class KeyStruct:
    __slots__ = ('name', 'gap', 'shapendx', 'colorndx',)

    def __init__(
            self, *,
            name: Optional[Sequence[int]] = None,
            gap: Optional[int] = None,
            shapendx: Optional[int] = None,
            colorndx: Optional[int] = None,
    ) -> None:
        self.name = name
        self.gap = gap
        self.shapendx = shapendx
        self.colorndx = colorndx

    def as_dict(self) -> Dict[str, Any]:
        return {
            'name': self.name,
            'gap': self.gap,
            'shapeNdx': self.shapendx,
            'colorNdx': self.colorndx,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'KeyStruct':
        return KeyStruct(**KeyStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return KeyStructPacket.pack(**self.as_dict())


class KeyStructCType(ctypes.Structure):
    """xkb Key"""
    _fields_ = [
        ("var_data", ctypes.c_void_p),
    ]


OverlayKeyStructPacket = DataPacket((
    ('over', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 4, 0)),
    ('under', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 4, 0)),
))


class OverlayKeyStruct:
    __slots__ = ('over', 'under',)

    def __init__(
            self, *,
            over: Optional[Sequence[int]] = None,
            under: Optional[Sequence[int]] = None,
    ) -> None:
        self.over = over
        self.under = under

    def as_dict(self) -> Dict[str, Any]:
        return {
            'over': self.over,
            'under': self.under,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'OverlayKeyStruct':
        return OverlayKeyStruct(**OverlayKeyStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return OverlayKeyStructPacket.pack(**self.as_dict())


class OverlayKeyStructCType(ctypes.Structure):
    """xkb OverlayKey"""
    _fields_ = [
        ("var_data", ctypes.c_void_p),
    ]


OverlayRowStructPacket = DataPacket((
    ('rowUnder', FixedDataPacketField(MARKER_UINT8)),
    ('nKeys', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
    ('keys', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nKeys'], 0)),
))


class OverlayRowStruct:
    __slots__ = ('rowunder', 'nkeys', 'keys',)

    def __init__(
            self, *,
            rowunder: Optional[int] = None,
            nkeys: Optional[int] = None,
            keys: Optional[Sequence[int]] = None,
    ) -> None:
        self.rowunder = rowunder
        self.nkeys = nkeys
        self.keys = keys

    def as_dict(self) -> Dict[str, Any]:
        return {
            'rowUnder': self.rowunder,
            'nKeys': self.nkeys,
            'keys': self.keys,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'OverlayRowStruct':
        return OverlayRowStruct(**OverlayRowStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return OverlayRowStructPacket.pack(**self.as_dict())


class OverlayRowStructCType(ctypes.Structure):
    """xkb OverlayRow"""
    _fields_ = [
        ("rowUnder", ctypes.c_uint8),
        ("nKeys", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


OverlayStructPacket = DataPacket((
    ('name', FixedDataPacketField(MARKER_UINT32)),
    ('nRows', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
    ('rows', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nRows'], 0)),
))


class OverlayStruct:
    __slots__ = ('name', 'nrows', 'rows',)

    def __init__(
            self, *,
            name: Optional[int] = None,
            nrows: Optional[int] = None,
            rows: Optional[Sequence[int]] = None,
    ) -> None:
        self.name = name
        self.nrows = nrows
        self.rows = rows

    def as_dict(self) -> Dict[str, Any]:
        return {
            'name': self.name,
            'nRows': self.nrows,
            'rows': self.rows,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'OverlayStruct':
        return OverlayStruct(**OverlayStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return OverlayStructPacket.pack(**self.as_dict())


class OverlayStructCType(ctypes.Structure):
    """xkb Overlay"""
    _fields_ = [
        ("name", ctypes.c_uint32),
        ("nRows", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
        ("var_data", ctypes.c_void_p),
    ]


RowStructPacket = DataPacket((
    ('top', FixedDataPacketField(MARKER_INT16)),
    ('left', FixedDataPacketField(MARKER_INT16)),
    ('nKeys', FixedDataPacketField(MARKER_UINT8)),
    ('vertical', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
    ('keys', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nKeys'], 0)),
))


class RowStruct:
    __slots__ = ('top', 'left', 'nkeys', 'vertical', 'keys',)

    def __init__(
            self, *,
            top: Optional[int] = None,
            left: Optional[int] = None,
            nkeys: Optional[int] = None,
            vertical: Optional[bool] = None,
            keys: Optional[Sequence[int]] = None,
    ) -> None:
        self.top = top
        self.left = left
        self.nkeys = nkeys
        self.vertical = vertical
        self.keys = keys

    def as_dict(self) -> Dict[str, Any]:
        return {
            'top': self.top,
            'left': self.left,
            'nKeys': self.nkeys,
            'vertical': self.vertical,
            'keys': self.keys,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'RowStruct':
        return RowStruct(**RowStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return RowStructPacket.pack(**self.as_dict())


class RowStructCType(ctypes.Structure):
    """xkb Row"""
    _fields_ = [
        ("top", ctypes.c_int16),
        ("left", ctypes.c_int16),
        ("nKeys", ctypes.c_uint8),
        ("vertical", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


ListingStructPacket = DataPacket((
    ('flags', FixedDataPacketField(MARKER_UINT16)),
    ('length', FixedDataPacketField(MARKER_UINT16)),
    ('string', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['length'], 0)),
    ('pad0', AlignedPadDataPacketField(2)),
))


class ListingStruct:
    __slots__ = ('flags', 'length', 'string',)

    def __init__(
            self, *,
            flags: Optional[int] = None,
            length: Optional[int] = None,
            string: Optional[Sequence[int]] = None,
    ) -> None:
        self.flags = flags
        self.length = length
        self.string = string

    def as_dict(self) -> Dict[str, Any]:
        return {
            'flags': self.flags,
            'length': self.length,
            'string': self.string,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ListingStruct':
        return ListingStruct(**ListingStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ListingStructPacket.pack(**self.as_dict())


class ListingStructCType(ctypes.Structure):
    """xkb Listing"""
    _fields_ = [
        ("flags", ctypes.c_uint16),
        ("length", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


DeviceLedInfoStructPacket = DataPacket((
    ('ledClass', FixedDataPacketField(MARKER_UINT32)),
    ('ledID', FixedDataPacketField(MARKER_UINT32)),
    ('namesPresent', FixedDataPacketField(MARKER_UINT32)),
    ('mapsPresent', FixedDataPacketField(MARKER_UINT32)),
    ('physIndicators', FixedDataPacketField(MARKER_UINT32)),
    ('state', FixedDataPacketField(MARKER_UINT32)),
    ('names', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['namesPresent'], 0)),
    ('maps', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['mapsPresent'], 0)),
))


class DeviceLedInfoStruct:
    __slots__ = ('ledclass', 'ledid', 'namespresent', 'mapspresent', 'physindicators', 'state', 'names', 'maps',)

    def __init__(
            self, *,
            ledclass: Optional[int] = None,
            ledid: Optional[int] = None,
            namespresent: Optional[int] = None,
            mapspresent: Optional[int] = None,
            physindicators: Optional[int] = None,
            state: Optional[int] = None,
            names: Optional[Sequence[int]] = None,
            maps: Optional[Sequence[int]] = None,
    ) -> None:
        self.ledclass = ledclass
        self.ledid = ledid
        self.namespresent = namespresent
        self.mapspresent = mapspresent
        self.physindicators = physindicators
        self.state = state
        self.names = names
        self.maps = maps

    def as_dict(self) -> Dict[str, Any]:
        return {
            'ledClass': self.ledclass,
            'ledID': self.ledid,
            'namesPresent': self.namespresent,
            'mapsPresent': self.mapspresent,
            'physIndicators': self.physindicators,
            'state': self.state,
            'names': self.names,
            'maps': self.maps,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeviceLedInfoStruct':
        return DeviceLedInfoStruct(**DeviceLedInfoStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeviceLedInfoStructPacket.pack(**self.as_dict())


class DeviceLedInfoStructCType(ctypes.Structure):
    """xkb DeviceLedInfo"""
    _fields_ = [
        ("ledClass", ctypes.c_uint32),
        ("ledID", ctypes.c_uint32),
        ("namesPresent", ctypes.c_uint32),
        ("mapsPresent", ctypes.c_uint32),
        ("physIndicators", ctypes.c_uint32),
        ("state", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


SanoActionStructPacket = DataPacket((
    ('type', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(7)),
))


class SanoActionStruct:
    __slots__ = ('type',)

    def __init__(
            self, *,
            type: Optional[int] = None,
    ) -> None:
        self.type = type

    def as_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SanoActionStruct':
        return SanoActionStruct(**SanoActionStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SanoActionStructPacket.pack(**self.as_dict())


class SanoActionStructCType(ctypes.Structure):
    """xkb SANoAction"""
    _fields_ = [
        ("type", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 7),
    ]


SasetModsStructPacket = DataPacket((
    ('type', FixedDataPacketField(MARKER_UINT8)),
    ('flags', FixedDataPacketField(MARKER_UINT8)),
    ('mask', FixedDataPacketField(MARKER_UINT8)),
    ('realMods', FixedDataPacketField(MARKER_UINT8)),
    ('vmodsHigh', FixedDataPacketField(MARKER_UINT8)),
    ('vmodsLow', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
))


class SasetModsStruct:
    __slots__ = ('type', 'flags', 'mask', 'realmods', 'vmodshigh', 'vmodslow',)

    def __init__(
            self, *,
            type: Optional[int] = None,
            flags: Optional[int] = None,
            mask: Optional[int] = None,
            realmods: Optional[int] = None,
            vmodshigh: Optional[int] = None,
            vmodslow: Optional[int] = None,
    ) -> None:
        self.type = type
        self.flags = flags
        self.mask = mask
        self.realmods = realmods
        self.vmodshigh = vmodshigh
        self.vmodslow = vmodslow

    def as_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type,
            'flags': self.flags,
            'mask': self.mask,
            'realMods': self.realmods,
            'vmodsHigh': self.vmodshigh,
            'vmodsLow': self.vmodslow,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SasetModsStruct':
        return SasetModsStruct(**SasetModsStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SasetModsStructPacket.pack(**self.as_dict())


class SasetModsStructCType(ctypes.Structure):
    """xkb SASetMods"""
    _fields_ = [
        ("type", ctypes.c_uint8),
        ("flags", ctypes.c_uint8),
        ("mask", ctypes.c_uint8),
        ("realMods", ctypes.c_uint8),
        ("vmodsHigh", ctypes.c_uint8),
        ("vmodsLow", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 2),
    ]


SasetGroupStructPacket = DataPacket((
    ('type', FixedDataPacketField(MARKER_UINT8)),
    ('flags', FixedDataPacketField(MARKER_UINT8)),
    ('group', FixedDataPacketField(MARKER_INT8)),
    ('pad0', FixedPadDataPacketField(5)),
))


class SasetGroupStruct:
    __slots__ = ('type', 'flags', 'group',)

    def __init__(
            self, *,
            type: Optional[int] = None,
            flags: Optional[int] = None,
            group: Optional[int] = None,
    ) -> None:
        self.type = type
        self.flags = flags
        self.group = group

    def as_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type,
            'flags': self.flags,
            'group': self.group,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SasetGroupStruct':
        return SasetGroupStruct(**SasetGroupStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SasetGroupStructPacket.pack(**self.as_dict())


class SasetGroupStructCType(ctypes.Structure):
    """xkb SASetGroup"""
    _fields_ = [
        ("type", ctypes.c_uint8),
        ("flags", ctypes.c_uint8),
        ("group", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 5),
    ]


SamovePtrStructPacket = DataPacket((
    ('type', FixedDataPacketField(MARKER_UINT8)),
    ('flags', FixedDataPacketField(MARKER_UINT8)),
    ('xHigh', FixedDataPacketField(MARKER_INT8)),
    ('xLow', FixedDataPacketField(MARKER_UINT8)),
    ('yHigh', FixedDataPacketField(MARKER_INT8)),
    ('yLow', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
))


class SamovePtrStruct:
    __slots__ = ('type', 'flags', 'xhigh', 'xlow', 'yhigh', 'ylow',)

    def __init__(
            self, *,
            type: Optional[int] = None,
            flags: Optional[int] = None,
            xhigh: Optional[int] = None,
            xlow: Optional[int] = None,
            yhigh: Optional[int] = None,
            ylow: Optional[int] = None,
    ) -> None:
        self.type = type
        self.flags = flags
        self.xhigh = xhigh
        self.xlow = xlow
        self.yhigh = yhigh
        self.ylow = ylow

    def as_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type,
            'flags': self.flags,
            'xHigh': self.xhigh,
            'xLow': self.xlow,
            'yHigh': self.yhigh,
            'yLow': self.ylow,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SamovePtrStruct':
        return SamovePtrStruct(**SamovePtrStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SamovePtrStructPacket.pack(**self.as_dict())


class SamovePtrStructCType(ctypes.Structure):
    """xkb SAMovePtr"""
    _fields_ = [
        ("type", ctypes.c_uint8),
        ("flags", ctypes.c_uint8),
        ("xHigh", ctypes.c_int8),
        ("xLow", ctypes.c_uint8),
        ("yHigh", ctypes.c_int8),
        ("yLow", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 2),
    ]


SaptrBtnStructPacket = DataPacket((
    ('type', FixedDataPacketField(MARKER_UINT8)),
    ('flags', FixedDataPacketField(MARKER_UINT8)),
    ('count', FixedDataPacketField(MARKER_UINT8)),
    ('button', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(4)),
))


class SaptrBtnStruct:
    __slots__ = ('type', 'flags', 'count', 'button',)

    def __init__(
            self, *,
            type: Optional[int] = None,
            flags: Optional[int] = None,
            count: Optional[int] = None,
            button: Optional[int] = None,
    ) -> None:
        self.type = type
        self.flags = flags
        self.count = count
        self.button = button

    def as_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type,
            'flags': self.flags,
            'count': self.count,
            'button': self.button,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SaptrBtnStruct':
        return SaptrBtnStruct(**SaptrBtnStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SaptrBtnStructPacket.pack(**self.as_dict())


class SaptrBtnStructCType(ctypes.Structure):
    """xkb SAPtrBtn"""
    _fields_ = [
        ("type", ctypes.c_uint8),
        ("flags", ctypes.c_uint8),
        ("count", ctypes.c_uint8),
        ("button", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 4),
    ]


SalockPtrBtnStructPacket = DataPacket((
    ('type', FixedDataPacketField(MARKER_UINT8)),
    ('flags', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('button', FixedDataPacketField(MARKER_UINT8)),
    ('pad1', FixedPadDataPacketField(4)),
))


class SalockPtrBtnStruct:
    __slots__ = ('type', 'flags', 'button',)

    def __init__(
            self, *,
            type: Optional[int] = None,
            flags: Optional[int] = None,
            button: Optional[int] = None,
    ) -> None:
        self.type = type
        self.flags = flags
        self.button = button

    def as_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type,
            'flags': self.flags,
            'button': self.button,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SalockPtrBtnStruct':
        return SalockPtrBtnStruct(**SalockPtrBtnStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SalockPtrBtnStructPacket.pack(**self.as_dict())


class SalockPtrBtnStructCType(ctypes.Structure):
    """xkb SALockPtrBtn"""
    _fields_ = [
        ("type", ctypes.c_uint8),
        ("flags", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
        ("button", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
    ]


SasetPtrDfltStructPacket = DataPacket((
    ('type', FixedDataPacketField(MARKER_UINT8)),
    ('flags', FixedDataPacketField(MARKER_UINT8)),
    ('affect', FixedDataPacketField(MARKER_UINT8)),
    ('value', FixedDataPacketField(MARKER_INT8)),
    ('pad0', FixedPadDataPacketField(4)),
))


class SasetPtrDfltStruct:
    __slots__ = ('type', 'flags', 'affect', 'value',)

    def __init__(
            self, *,
            type: Optional[int] = None,
            flags: Optional[int] = None,
            affect: Optional[int] = None,
            value: Optional[int] = None,
    ) -> None:
        self.type = type
        self.flags = flags
        self.affect = affect
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type,
            'flags': self.flags,
            'affect': self.affect,
            'value': self.value,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SasetPtrDfltStruct':
        return SasetPtrDfltStruct(**SasetPtrDfltStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SasetPtrDfltStructPacket.pack(**self.as_dict())


class SasetPtrDfltStructCType(ctypes.Structure):
    """xkb SASetPtrDflt"""
    _fields_ = [
        ("type", ctypes.c_uint8),
        ("flags", ctypes.c_uint8),
        ("affect", ctypes.c_uint8),
        ("value", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 4),
    ]


SaisoLockStructPacket = DataPacket((
    ('type', FixedDataPacketField(MARKER_UINT8)),
    ('flags', FixedDataPacketField(MARKER_UINT8)),
    ('mask', FixedDataPacketField(MARKER_UINT8)),
    ('realMods', FixedDataPacketField(MARKER_UINT8)),
    ('group', FixedDataPacketField(MARKER_INT8)),
    ('affect', FixedDataPacketField(MARKER_UINT8)),
    ('vmodsHigh', FixedDataPacketField(MARKER_UINT8)),
    ('vmodsLow', FixedDataPacketField(MARKER_UINT8)),
))


class SaisoLockStruct:
    __slots__ = ('type', 'flags', 'mask', 'realmods', 'group', 'affect', 'vmodshigh', 'vmodslow',)

    def __init__(
            self, *,
            type: Optional[int] = None,
            flags: Optional[int] = None,
            mask: Optional[int] = None,
            realmods: Optional[int] = None,
            group: Optional[int] = None,
            affect: Optional[int] = None,
            vmodshigh: Optional[int] = None,
            vmodslow: Optional[int] = None,
    ) -> None:
        self.type = type
        self.flags = flags
        self.mask = mask
        self.realmods = realmods
        self.group = group
        self.affect = affect
        self.vmodshigh = vmodshigh
        self.vmodslow = vmodslow

    def as_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type,
            'flags': self.flags,
            'mask': self.mask,
            'realMods': self.realmods,
            'group': self.group,
            'affect': self.affect,
            'vmodsHigh': self.vmodshigh,
            'vmodsLow': self.vmodslow,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SaisoLockStruct':
        return SaisoLockStruct(**SaisoLockStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SaisoLockStructPacket.pack(**self.as_dict())


class SaisoLockStructCType(ctypes.Structure):
    """xkb SAIsoLock"""
    _fields_ = [
        ("type", ctypes.c_uint8),
        ("flags", ctypes.c_uint8),
        ("mask", ctypes.c_uint8),
        ("realMods", ctypes.c_uint8),
        ("group", ctypes.c_int8),
        ("affect", ctypes.c_uint8),
        ("vmodsHigh", ctypes.c_uint8),
        ("vmodsLow", ctypes.c_uint8),
    ]


SaterminateStructPacket = DataPacket((
    ('type', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(7)),
))


class SaterminateStruct:
    __slots__ = ('type',)

    def __init__(
            self, *,
            type: Optional[int] = None,
    ) -> None:
        self.type = type

    def as_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SaterminateStruct':
        return SaterminateStruct(**SaterminateStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SaterminateStructPacket.pack(**self.as_dict())


class SaterminateStructCType(ctypes.Structure):
    """xkb SATerminate"""
    _fields_ = [
        ("type", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 7),
    ]


SaswitchScreenStructPacket = DataPacket((
    ('type', FixedDataPacketField(MARKER_UINT8)),
    ('flags', FixedDataPacketField(MARKER_UINT8)),
    ('newScreen', FixedDataPacketField(MARKER_INT8)),
    ('pad0', FixedPadDataPacketField(5)),
))


class SaswitchScreenStruct:
    __slots__ = ('type', 'flags', 'newscreen',)

    def __init__(
            self, *,
            type: Optional[int] = None,
            flags: Optional[int] = None,
            newscreen: Optional[int] = None,
    ) -> None:
        self.type = type
        self.flags = flags
        self.newscreen = newscreen

    def as_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type,
            'flags': self.flags,
            'newScreen': self.newscreen,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SaswitchScreenStruct':
        return SaswitchScreenStruct(**SaswitchScreenStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SaswitchScreenStructPacket.pack(**self.as_dict())


class SaswitchScreenStructCType(ctypes.Structure):
    """xkb SASwitchScreen"""
    _fields_ = [
        ("type", ctypes.c_uint8),
        ("flags", ctypes.c_uint8),
        ("newScreen", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 5),
    ]


SasetControlsStructPacket = DataPacket((
    ('type', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
    ('boolCtrlsHigh', FixedDataPacketField(MARKER_UINT8)),
    ('boolCtrlsLow', FixedDataPacketField(MARKER_UINT8)),
    ('pad1', FixedPadDataPacketField(2)),
))


class SasetControlsStruct:
    __slots__ = ('type', 'boolctrlshigh', 'boolctrlslow',)

    def __init__(
            self, *,
            type: Optional[int] = None,
            boolctrlshigh: Optional[int] = None,
            boolctrlslow: Optional[int] = None,
    ) -> None:
        self.type = type
        self.boolctrlshigh = boolctrlshigh
        self.boolctrlslow = boolctrlslow

    def as_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type,
            'boolCtrlsHigh': self.boolctrlshigh,
            'boolCtrlsLow': self.boolctrlslow,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SasetControlsStruct':
        return SasetControlsStruct(**SasetControlsStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SasetControlsStructPacket.pack(**self.as_dict())


class SasetControlsStructCType(ctypes.Structure):
    """xkb SASetControls"""
    _fields_ = [
        ("type", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
        ("boolCtrlsHigh", ctypes.c_uint8),
        ("boolCtrlsLow", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 2),
    ]


SaactionMessageStructPacket = DataPacket((
    ('type', FixedDataPacketField(MARKER_UINT8)),
    ('flags', FixedDataPacketField(MARKER_UINT8)),
    ('message', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: 6, 0)),
))


class SaactionMessageStruct:
    __slots__ = ('type', 'flags', 'message',)

    def __init__(
            self, *,
            type: Optional[int] = None,
            flags: Optional[int] = None,
            message: Optional[Sequence[int]] = None,
    ) -> None:
        self.type = type
        self.flags = flags
        self.message = message

    def as_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type,
            'flags': self.flags,
            'message': self.message,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SaactionMessageStruct':
        return SaactionMessageStruct(**SaactionMessageStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SaactionMessageStructPacket.pack(**self.as_dict())


class SaactionMessageStructCType(ctypes.Structure):
    """xkb SAActionMessage"""
    _fields_ = [
        ("type", ctypes.c_uint8),
        ("flags", ctypes.c_uint8),
        ("var_data", ctypes.c_void_p),
    ]


SaredirectKeyStructPacket = DataPacket((
    ('type', FixedDataPacketField(MARKER_UINT8)),
    ('newkey', FixedDataPacketField(MARKER_UINT32)),
    ('mask', FixedDataPacketField(MARKER_UINT8)),
    ('realModifiers', FixedDataPacketField(MARKER_UINT8)),
    ('vmodsMaskHigh', FixedDataPacketField(MARKER_UINT8)),
    ('vmodsMaskLow', FixedDataPacketField(MARKER_UINT8)),
    ('vmodsHigh', FixedDataPacketField(MARKER_UINT8)),
    ('vmodsLow', FixedDataPacketField(MARKER_UINT8)),
))


class SaredirectKeyStruct:
    __slots__ = ('type', 'newkey', 'mask', 'realmodifiers', 'vmodsmaskhigh', 'vmodsmasklow', 'vmodshigh', 'vmodslow',)

    def __init__(
            self, *,
            type: Optional[int] = None,
            newkey: Optional[int] = None,
            mask: Optional[int] = None,
            realmodifiers: Optional[int] = None,
            vmodsmaskhigh: Optional[int] = None,
            vmodsmasklow: Optional[int] = None,
            vmodshigh: Optional[int] = None,
            vmodslow: Optional[int] = None,
    ) -> None:
        self.type = type
        self.newkey = newkey
        self.mask = mask
        self.realmodifiers = realmodifiers
        self.vmodsmaskhigh = vmodsmaskhigh
        self.vmodsmasklow = vmodsmasklow
        self.vmodshigh = vmodshigh
        self.vmodslow = vmodslow

    def as_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type,
            'newkey': self.newkey,
            'mask': self.mask,
            'realModifiers': self.realmodifiers,
            'vmodsMaskHigh': self.vmodsmaskhigh,
            'vmodsMaskLow': self.vmodsmasklow,
            'vmodsHigh': self.vmodshigh,
            'vmodsLow': self.vmodslow,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SaredirectKeyStruct':
        return SaredirectKeyStruct(**SaredirectKeyStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SaredirectKeyStructPacket.pack(**self.as_dict())


class SaredirectKeyStructCType(ctypes.Structure):
    """xkb SARedirectKey"""
    _fields_ = [
        ("type", ctypes.c_uint8),
        ("newkey", ctypes.c_uint32),
        ("mask", ctypes.c_uint8),
        ("realModifiers", ctypes.c_uint8),
        ("vmodsMaskHigh", ctypes.c_uint8),
        ("vmodsMaskLow", ctypes.c_uint8),
        ("vmodsHigh", ctypes.c_uint8),
        ("vmodsLow", ctypes.c_uint8),
    ]


SadeviceBtnStructPacket = DataPacket((
    ('type', FixedDataPacketField(MARKER_UINT8)),
    ('flags', FixedDataPacketField(MARKER_UINT8)),
    ('count', FixedDataPacketField(MARKER_UINT8)),
    ('button', FixedDataPacketField(MARKER_UINT8)),
    ('device', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class SadeviceBtnStruct:
    __slots__ = ('type', 'flags', 'count', 'button', 'device',)

    def __init__(
            self, *,
            type: Optional[int] = None,
            flags: Optional[int] = None,
            count: Optional[int] = None,
            button: Optional[int] = None,
            device: Optional[int] = None,
    ) -> None:
        self.type = type
        self.flags = flags
        self.count = count
        self.button = button
        self.device = device

    def as_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type,
            'flags': self.flags,
            'count': self.count,
            'button': self.button,
            'device': self.device,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SadeviceBtnStruct':
        return SadeviceBtnStruct(**SadeviceBtnStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SadeviceBtnStructPacket.pack(**self.as_dict())


class SadeviceBtnStructCType(ctypes.Structure):
    """xkb SADeviceBtn"""
    _fields_ = [
        ("type", ctypes.c_uint8),
        ("flags", ctypes.c_uint8),
        ("count", ctypes.c_uint8),
        ("button", ctypes.c_uint8),
        ("device", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


SalockDeviceBtnStructPacket = DataPacket((
    ('type', FixedDataPacketField(MARKER_UINT8)),
    ('flags', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('button', FixedDataPacketField(MARKER_UINT8)),
    ('device', FixedDataPacketField(MARKER_UINT8)),
    ('pad1', FixedPadDataPacketField(3)),
))


class SalockDeviceBtnStruct:
    __slots__ = ('type', 'flags', 'button', 'device',)

    def __init__(
            self, *,
            type: Optional[int] = None,
            flags: Optional[int] = None,
            button: Optional[int] = None,
            device: Optional[int] = None,
    ) -> None:
        self.type = type
        self.flags = flags
        self.button = button
        self.device = device

    def as_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type,
            'flags': self.flags,
            'button': self.button,
            'device': self.device,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SalockDeviceBtnStruct':
        return SalockDeviceBtnStruct(**SalockDeviceBtnStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SalockDeviceBtnStructPacket.pack(**self.as_dict())


class SalockDeviceBtnStructCType(ctypes.Structure):
    """xkb SALockDeviceBtn"""
    _fields_ = [
        ("type", ctypes.c_uint8),
        ("flags", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
        ("button", ctypes.c_uint8),
        ("device", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 3),
    ]


SadeviceValuatorStructPacket = DataPacket((
    ('type', FixedDataPacketField(MARKER_UINT8)),
    ('device', FixedDataPacketField(MARKER_UINT8)),
    ('val1what', FixedDataPacketField(MARKER_UINT8)),
    ('val1index', FixedDataPacketField(MARKER_UINT8)),
    ('val1value', FixedDataPacketField(MARKER_UINT8)),
    ('val2what', FixedDataPacketField(MARKER_UINT8)),
    ('val2index', FixedDataPacketField(MARKER_UINT8)),
    ('val2value', FixedDataPacketField(MARKER_UINT8)),
))


class SadeviceValuatorStruct:
    __slots__ = ('type', 'device', 'val1what', 'val1index', 'val1value', 'val2what', 'val2index', 'val2value',)

    def __init__(
            self, *,
            type: Optional[int] = None,
            device: Optional[int] = None,
            val1what: Optional[int] = None,
            val1index: Optional[int] = None,
            val1value: Optional[int] = None,
            val2what: Optional[int] = None,
            val2index: Optional[int] = None,
            val2value: Optional[int] = None,
    ) -> None:
        self.type = type
        self.device = device
        self.val1what = val1what
        self.val1index = val1index
        self.val1value = val1value
        self.val2what = val2what
        self.val2index = val2index
        self.val2value = val2value

    def as_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type,
            'device': self.device,
            'val1what': self.val1what,
            'val1index': self.val1index,
            'val1value': self.val1value,
            'val2what': self.val2what,
            'val2index': self.val2index,
            'val2value': self.val2value,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SadeviceValuatorStruct':
        return SadeviceValuatorStruct(**SadeviceValuatorStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SadeviceValuatorStructPacket.pack(**self.as_dict())


class SadeviceValuatorStructCType(ctypes.Structure):
    """xkb SADeviceValuator"""
    _fields_ = [
        ("type", ctypes.c_uint8),
        ("device", ctypes.c_uint8),
        ("val1what", ctypes.c_uint8),
        ("val1index", ctypes.c_uint8),
        ("val1value", ctypes.c_uint8),
        ("val2what", ctypes.c_uint8),
        ("val2index", ctypes.c_uint8),
        ("val2value", ctypes.c_uint8),
    ]


SiactionStructPacket = DataPacket((
    ('type', FixedDataPacketField(MARKER_UINT8)),
    ('data', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: 7, 0)),
))


class SiactionStruct:
    __slots__ = ('type', 'data',)

    def __init__(
            self, *,
            type: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.type = type
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SiactionStruct':
        return SiactionStruct(**SiactionStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SiactionStructPacket.pack(**self.as_dict())


class SiactionStructCType(ctypes.Structure):
    """xkb SIAction"""
    _fields_ = [
        ("type", ctypes.c_uint8),
        ("var_data", ctypes.c_void_p),
    ]


SymInterpretStructPacket = DataPacket((
    ('sym', FixedDataPacketField(MARKER_UINT32)),
    ('mods', FixedDataPacketField(MARKER_UINT8)),
    ('match', FixedDataPacketField(MARKER_UINT8)),
    ('virtualMod', FixedDataPacketField(MARKER_UINT8)),
    ('flags', FixedDataPacketField(MARKER_UINT8)),
    ('action', FixedDataPacketField(MARKER_UINT32)),
))


class SymInterpretStruct:
    __slots__ = ('sym', 'mods', 'match', 'virtualmod', 'flags', 'action',)

    def __init__(
            self, *,
            sym: Optional[int] = None,
            mods: Optional[int] = None,
            match: Optional[int] = None,
            virtualmod: Optional[int] = None,
            flags: Optional[int] = None,
            action: Optional[int] = None,
    ) -> None:
        self.sym = sym
        self.mods = mods
        self.match = match
        self.virtualmod = virtualmod
        self.flags = flags
        self.action = action

    def as_dict(self) -> Dict[str, Any]:
        return {
            'sym': self.sym,
            'mods': self.mods,
            'match': self.match,
            'virtualMod': self.virtualmod,
            'flags': self.flags,
            'action': self.action,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SymInterpretStruct':
        return SymInterpretStruct(**SymInterpretStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SymInterpretStructPacket.pack(**self.as_dict())


class SymInterpretStructCType(ctypes.Structure):
    """xkb SymInterpret"""
    _fields_ = [
        ("sym", ctypes.c_uint32),
        ("mods", ctypes.c_uint8),
        ("match", ctypes.c_uint8),
        ("virtualMod", ctypes.c_uint8),
        ("flags", ctypes.c_uint8),
        ("action", ctypes.c_uint32),
    ]


UseExtensionRequestCookie = NewType('UseExtensionRequestCookie', ctypes.c_uint32)


UseExtensionRequestPacket = DataPacket((
    ('wantedMajor', FixedDataPacketField(MARKER_UINT16)),
    ('wantedMinor', FixedDataPacketField(MARKER_UINT16)),
))


class UseExtensionRequest:
    OPCODE = 0

    __slots__ = ('wantedmajor', 'wantedminor',)

    def __init__(
            self, *,
            wantedmajor: Optional[int] = None,
            wantedminor: Optional[int] = None,
    ) -> None:
        self.wantedmajor = wantedmajor
        self.wantedminor = wantedminor

    def as_dict(self) -> Dict[str, Any]:
        return {
            'wantedMajor': self.wantedmajor,
            'wantedMinor': self.wantedminor,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'UseExtensionRequest':
        return UseExtensionRequest(**UseExtensionRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return UseExtensionRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], UseExtensionRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        UseExtensionRequest.lib = library.xkb_useextension
        UseExtensionRequest.lib.restype = UseExtensionRequestCookie
        UseExtensionRequest.lib.argstype = (ctypes.c_uint16, ctypes.c_uint16)


class UseExtensionRequestCType(ctypes.Structure):
    """xkb UseExtension"""
    _fields_ = [
        ("wantedMajor", ctypes.c_uint16),
        ("wantedMinor", ctypes.c_uint16),
    ]


UseExtensionReplyReplyPacket = DataPacket((
    ('supported', FixedDataPacketField(MARKER_UINT8)),
    ('serverMajor', FixedDataPacketField(MARKER_UINT16)),
    ('serverMinor', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(20)),
))


class UseExtensionReplyReply:
    __slots__ = ('supported', 'servermajor', 'serverminor',)

    def __init__(
            self, *,
            supported: Optional[bool] = None,
            servermajor: Optional[int] = None,
            serverminor: Optional[int] = None,
    ) -> None:
        self.supported = supported
        self.servermajor = servermajor
        self.serverminor = serverminor

    def as_dict(self) -> Dict[str, Any]:
        return {
            'supported': self.supported,
            'serverMajor': self.servermajor,
            'serverMinor': self.serverminor,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'UseExtensionReplyReply':
        return UseExtensionReplyReply(**UseExtensionReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return UseExtensionReplyReplyPacket.pack(**self.as_dict())


class UseExtensionReplyReplyCType(ctypes.Structure):
    """xkb UseExtension_reply"""
    _fields_ = [
        ("supported", ctypes.c_int8),
        ("serverMajor", ctypes.c_uint16),
        ("serverMinor", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 20),
    ]


SelectEventsRequestPacket = DataPacket((
    ('deviceSpec', FixedDataPacketField(MARKER_UINT32)),
    ('affectWhich', FixedDataPacketField(MARKER_UINT16)),
    ('clear', FixedDataPacketField(MARKER_UINT16)),
    ('selectAll', FixedDataPacketField(MARKER_UINT16)),
    ('affectMap', FixedDataPacketField(MARKER_UINT16)),
    ('map', FixedDataPacketField(MARKER_UINT16)),
    ('details', BitDataPacketField(lambda d, c: d[''], {
        EventTypeValues.NEW_KEYBOARD_NOTIFY: StructureDataPacketField((
            ('affectNewKeyboard', FixedDataPacketField(MARKER_UINT16)),
            ('newKeyboardDetails', FixedDataPacketField(MARKER_UINT16)),
        )),
        EventTypeValues.STATE_NOTIFY: StructureDataPacketField((
            ('affectState', FixedDataPacketField(MARKER_UINT16)),
            ('stateDetails', FixedDataPacketField(MARKER_UINT16)),
        )),
        EventTypeValues.CONTROLS_NOTIFY: StructureDataPacketField((
            ('affectCtrls', FixedDataPacketField(MARKER_UINT32)),
            ('ctrlDetails', FixedDataPacketField(MARKER_UINT32)),
        )),
        EventTypeValues.INDICATOR_STATE_NOTIFY: StructureDataPacketField((
            ('affectIndicatorState', FixedDataPacketField(MARKER_UINT32)),
            ('indicatorStateDetails', FixedDataPacketField(MARKER_UINT32)),
        )),
        EventTypeValues.INDICATOR_MAP_NOTIFY: StructureDataPacketField((
            ('affectIndicatorMap', FixedDataPacketField(MARKER_UINT32)),
            ('indicatorMapDetails', FixedDataPacketField(MARKER_UINT32)),
        )),
        EventTypeValues.NAMES_NOTIFY: StructureDataPacketField((
            ('affectNames', FixedDataPacketField(MARKER_UINT16)),
            ('namesDetails', FixedDataPacketField(MARKER_UINT16)),
        )),
        EventTypeValues.COMPAT_MAP_NOTIFY: StructureDataPacketField((
            ('affectCompat', FixedDataPacketField(MARKER_UINT8)),
            ('compatDetails', FixedDataPacketField(MARKER_UINT8)),
        )),
        EventTypeValues.BELL_NOTIFY: StructureDataPacketField((
            ('affectBell', FixedDataPacketField(MARKER_UINT8)),
            ('bellDetails', FixedDataPacketField(MARKER_UINT8)),
        )),
        EventTypeValues.ACTION_MESSAGE: StructureDataPacketField((
            ('affectMsgDetails', FixedDataPacketField(MARKER_UINT8)),
            ('msgDetails', FixedDataPacketField(MARKER_UINT8)),
        )),
        EventTypeValues.ACCESS_XNOTIFY: StructureDataPacketField((
            ('affectAccessX', FixedDataPacketField(MARKER_UINT16)),
            ('accessXDetails', FixedDataPacketField(MARKER_UINT16)),
        )),
        EventTypeValues.EXTENSION_DEVICE_NOTIFY: StructureDataPacketField((
            ('affectExtDev', FixedDataPacketField(MARKER_UINT16)),
            ('extdevDetails', FixedDataPacketField(MARKER_UINT16)),
        )),
    }, 0)),
))


class SelectEventsRequest:
    OPCODE = 1

    __slots__ = ('devicespec', 'affectwhich', 'clear', 'selectall', 'affectmap', 'map', 'details',)

    def __init__(
            self, *,
            devicespec: Optional[int] = None,
            affectwhich: Optional[int] = None,
            clear: Optional[int] = None,
            selectall: Optional[int] = None,
            affectmap: Optional[int] = None,
            map: Optional[int] = None,
            details: Optional[Mapping[str, EventTypeValues]] = None,
    ) -> None:
        self.devicespec = devicespec
        self.affectwhich = affectwhich
        self.clear = clear
        self.selectall = selectall
        self.affectmap = affectmap
        self.map = map
        self.details = details

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceSpec': self.devicespec,
            'affectWhich': self.affectwhich,
            'clear': self.clear,
            'selectAll': self.selectall,
            'affectMap': self.affectmap,
            'map': self.map,
            'details': self.details,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SelectEventsRequest':
        return SelectEventsRequest(**SelectEventsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SelectEventsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, Mapping[str, EventTypeValues]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SelectEventsRequest.lib = library.xkb_selectevents
        SelectEventsRequest.lib.restype = ctypes.c_uint32
        SelectEventsRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_void_p)


class SelectEventsRequestCType(ctypes.Structure):
    """xkb SelectEvents"""
    _fields_ = [
        ("deviceSpec", ctypes.c_uint32),
        ("affectWhich", ctypes.c_uint16),
        ("clear", ctypes.c_uint16),
        ("selectAll", ctypes.c_uint16),
        ("affectMap", ctypes.c_uint16),
        ("map", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


BellRequestPacket = DataPacket((
    ('deviceSpec', FixedDataPacketField(MARKER_UINT32)),
    ('bellClass', FixedDataPacketField(MARKER_UINT32)),
    ('bellID', FixedDataPacketField(MARKER_UINT32)),
    ('percent', FixedDataPacketField(MARKER_INT8)),
    ('forceSound', FixedDataPacketField(MARKER_UINT8)),
    ('eventOnly', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('pitch', FixedDataPacketField(MARKER_INT16)),
    ('duration', FixedDataPacketField(MARKER_INT16)),
    ('pad1', FixedPadDataPacketField(2)),
    ('name', FixedDataPacketField(MARKER_UINT32)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class BellRequest:
    OPCODE = 3

    __slots__ = ('devicespec', 'bellclass', 'bellid', 'percent', 'forcesound', 'eventonly', 'pitch', 'duration', 'name', 'window',)

    def __init__(
            self, *,
            devicespec: Optional[int] = None,
            bellclass: Optional[int] = None,
            bellid: Optional[int] = None,
            percent: Optional[int] = None,
            forcesound: Optional[bool] = None,
            eventonly: Optional[bool] = None,
            pitch: Optional[int] = None,
            duration: Optional[int] = None,
            name: Optional[int] = None,
            window: Optional[int] = None,
    ) -> None:
        self.devicespec = devicespec
        self.bellclass = bellclass
        self.bellid = bellid
        self.percent = percent
        self.forcesound = forcesound
        self.eventonly = eventonly
        self.pitch = pitch
        self.duration = duration
        self.name = name
        self.window = window

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceSpec': self.devicespec,
            'bellClass': self.bellclass,
            'bellID': self.bellid,
            'percent': self.percent,
            'forceSound': self.forcesound,
            'eventOnly': self.eventonly,
            'pitch': self.pitch,
            'duration': self.duration,
            'name': self.name,
            'window': self.window,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'BellRequest':
        return BellRequest(**BellRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return BellRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, bool, bool, int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        BellRequest.lib = library.xkb_bell
        BellRequest.lib.restype = ctypes.c_uint32
        BellRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int8, ctypes.c_int8, ctypes.c_int8, ctypes.c_uint8, ctypes.c_int16, ctypes.c_int16, ctypes.c_uint8 * 2, ctypes.c_uint32, ctypes.c_uint32)


class BellRequestCType(ctypes.Structure):
    """xkb Bell"""
    _fields_ = [
        ("deviceSpec", ctypes.c_uint32),
        ("bellClass", ctypes.c_uint32),
        ("bellID", ctypes.c_uint32),
        ("percent", ctypes.c_int8),
        ("forceSound", ctypes.c_int8),
        ("eventOnly", ctypes.c_int8),
        ("pad0", ctypes.c_uint8),
        ("pitch", ctypes.c_int16),
        ("duration", ctypes.c_int16),
        ("pad1", ctypes.c_uint8 * 2),
        ("name", ctypes.c_uint32),
        ("window", ctypes.c_uint32),
    ]


GetStateRequestCookie = NewType('GetStateRequestCookie', ctypes.c_uint32)


GetStateRequestPacket = DataPacket((
    ('deviceSpec', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(2)),
))


class GetStateRequest:
    OPCODE = 4

    __slots__ = ('devicespec',)

    def __init__(
            self, *,
            devicespec: Optional[int] = None,
    ) -> None:
        self.devicespec = devicespec

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceSpec': self.devicespec,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetStateRequest':
        return GetStateRequest(**GetStateRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetStateRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetStateRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetStateRequest.lib = library.xkb_getstate
        GetStateRequest.lib.restype = GetStateRequestCookie
        GetStateRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint8 * 2)


class GetStateRequestCType(ctypes.Structure):
    """xkb GetState"""
    _fields_ = [
        ("deviceSpec", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 2),
    ]


GetStateReplyReplyPacket = DataPacket((
    ('deviceID', FixedDataPacketField(MARKER_UINT8)),
    ('mods', FixedDataPacketField(MARKER_UINT8)),
    ('baseMods', FixedDataPacketField(MARKER_UINT8)),
    ('latchedMods', FixedDataPacketField(MARKER_UINT8)),
    ('lockedMods', FixedDataPacketField(MARKER_UINT8)),
    ('group', FixedDataPacketField(MARKER_UINT8)),
    ('lockedGroup', FixedDataPacketField(MARKER_UINT8)),
    ('baseGroup', FixedDataPacketField(MARKER_INT16)),
    ('latchedGroup', FixedDataPacketField(MARKER_INT16)),
    ('compatState', FixedDataPacketField(MARKER_UINT8)),
    ('grabMods', FixedDataPacketField(MARKER_UINT8)),
    ('compatGrabMods', FixedDataPacketField(MARKER_UINT8)),
    ('lookupMods', FixedDataPacketField(MARKER_UINT8)),
    ('compatLookupMods', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('ptrBtnState', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(6)),
))


class GetStateReplyReply:
    __slots__ = ('deviceid', 'mods', 'basemods', 'latchedmods', 'lockedmods', 'group', 'lockedgroup', 'basegroup', 'latchedgroup', 'compatstate', 'grabmods', 'compatgrabmods', 'lookupmods', 'compatlookupmods', 'ptrbtnstate',)

    def __init__(
            self, *,
            deviceid: Optional[int] = None,
            mods: Optional[int] = None,
            basemods: Optional[int] = None,
            latchedmods: Optional[int] = None,
            lockedmods: Optional[int] = None,
            group: Optional[int] = None,
            lockedgroup: Optional[int] = None,
            basegroup: Optional[int] = None,
            latchedgroup: Optional[int] = None,
            compatstate: Optional[int] = None,
            grabmods: Optional[int] = None,
            compatgrabmods: Optional[int] = None,
            lookupmods: Optional[int] = None,
            compatlookupmods: Optional[int] = None,
            ptrbtnstate: Optional[int] = None,
    ) -> None:
        self.deviceid = deviceid
        self.mods = mods
        self.basemods = basemods
        self.latchedmods = latchedmods
        self.lockedmods = lockedmods
        self.group = group
        self.lockedgroup = lockedgroup
        self.basegroup = basegroup
        self.latchedgroup = latchedgroup
        self.compatstate = compatstate
        self.grabmods = grabmods
        self.compatgrabmods = compatgrabmods
        self.lookupmods = lookupmods
        self.compatlookupmods = compatlookupmods
        self.ptrbtnstate = ptrbtnstate

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceID': self.deviceid,
            'mods': self.mods,
            'baseMods': self.basemods,
            'latchedMods': self.latchedmods,
            'lockedMods': self.lockedmods,
            'group': self.group,
            'lockedGroup': self.lockedgroup,
            'baseGroup': self.basegroup,
            'latchedGroup': self.latchedgroup,
            'compatState': self.compatstate,
            'grabMods': self.grabmods,
            'compatGrabMods': self.compatgrabmods,
            'lookupMods': self.lookupmods,
            'compatLookupMods': self.compatlookupmods,
            'ptrBtnState': self.ptrbtnstate,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetStateReplyReply':
        return GetStateReplyReply(**GetStateReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetStateReplyReplyPacket.pack(**self.as_dict())


class GetStateReplyReplyCType(ctypes.Structure):
    """xkb GetState_reply"""
    _fields_ = [
        ("deviceID", ctypes.c_uint8),
        ("mods", ctypes.c_uint8),
        ("baseMods", ctypes.c_uint8),
        ("latchedMods", ctypes.c_uint8),
        ("lockedMods", ctypes.c_uint8),
        ("group", ctypes.c_uint8),
        ("lockedGroup", ctypes.c_uint8),
        ("baseGroup", ctypes.c_int16),
        ("latchedGroup", ctypes.c_int16),
        ("compatState", ctypes.c_uint8),
        ("grabMods", ctypes.c_uint8),
        ("compatGrabMods", ctypes.c_uint8),
        ("lookupMods", ctypes.c_uint8),
        ("compatLookupMods", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
        ("ptrBtnState", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 6),
    ]


LatchLockStateRequestPacket = DataPacket((
    ('deviceSpec', FixedDataPacketField(MARKER_UINT32)),
    ('affectModLocks', FixedDataPacketField(MARKER_UINT8)),
    ('modLocks', FixedDataPacketField(MARKER_UINT8)),
    ('lockGroup', FixedDataPacketField(MARKER_UINT8)),
    ('groupLock', FixedDataPacketField(MARKER_UINT8)),
    ('affectModLatches', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('pad1', FixedPadDataPacketField(1)),
    ('latchGroup', FixedDataPacketField(MARKER_UINT8)),
    ('groupLatch', FixedDataPacketField(MARKER_UINT16)),
))


class LatchLockStateRequest:
    OPCODE = 5

    __slots__ = ('devicespec', 'affectmodlocks', 'modlocks', 'lockgroup', 'grouplock', 'affectmodlatches', 'latchgroup', 'grouplatch',)

    def __init__(
            self, *,
            devicespec: Optional[int] = None,
            affectmodlocks: Optional[int] = None,
            modlocks: Optional[int] = None,
            lockgroup: Optional[bool] = None,
            grouplock: Optional[int] = None,
            affectmodlatches: Optional[int] = None,
            latchgroup: Optional[bool] = None,
            grouplatch: Optional[int] = None,
    ) -> None:
        self.devicespec = devicespec
        self.affectmodlocks = affectmodlocks
        self.modlocks = modlocks
        self.lockgroup = lockgroup
        self.grouplock = grouplock
        self.affectmodlatches = affectmodlatches
        self.latchgroup = latchgroup
        self.grouplatch = grouplatch

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceSpec': self.devicespec,
            'affectModLocks': self.affectmodlocks,
            'modLocks': self.modlocks,
            'lockGroup': self.lockgroup,
            'groupLock': self.grouplock,
            'affectModLatches': self.affectmodlatches,
            'latchGroup': self.latchgroup,
            'groupLatch': self.grouplatch,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'LatchLockStateRequest':
        return LatchLockStateRequest(**LatchLockStateRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return LatchLockStateRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, bool, int, int, bool, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        LatchLockStateRequest.lib = library.xkb_latchlockstate
        LatchLockStateRequest.lib.restype = ctypes.c_uint32
        LatchLockStateRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_int8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_int8, ctypes.c_uint16)


class LatchLockStateRequestCType(ctypes.Structure):
    """xkb LatchLockState"""
    _fields_ = [
        ("deviceSpec", ctypes.c_uint32),
        ("affectModLocks", ctypes.c_uint8),
        ("modLocks", ctypes.c_uint8),
        ("lockGroup", ctypes.c_int8),
        ("groupLock", ctypes.c_uint8),
        ("affectModLatches", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8),
        ("latchGroup", ctypes.c_int8),
        ("groupLatch", ctypes.c_uint16),
    ]


GetControlsRequestCookie = NewType('GetControlsRequestCookie', ctypes.c_uint32)


GetControlsRequestPacket = DataPacket((
    ('deviceSpec', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(2)),
))


class GetControlsRequest:
    OPCODE = 6

    __slots__ = ('devicespec',)

    def __init__(
            self, *,
            devicespec: Optional[int] = None,
    ) -> None:
        self.devicespec = devicespec

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceSpec': self.devicespec,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetControlsRequest':
        return GetControlsRequest(**GetControlsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetControlsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetControlsRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetControlsRequest.lib = library.xkb_getcontrols
        GetControlsRequest.lib.restype = GetControlsRequestCookie
        GetControlsRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint8 * 2)


class GetControlsRequestCType(ctypes.Structure):
    """xkb GetControls"""
    _fields_ = [
        ("deviceSpec", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 2),
    ]


GetControlsReplyReplyPacket = DataPacket((
    ('deviceID', FixedDataPacketField(MARKER_UINT8)),
    ('mouseKeysDfltBtn', FixedDataPacketField(MARKER_UINT8)),
    ('numGroups', FixedDataPacketField(MARKER_UINT8)),
    ('groupsWrap', FixedDataPacketField(MARKER_UINT8)),
    ('internalModsMask', FixedDataPacketField(MARKER_UINT8)),
    ('ignoreLockModsMask', FixedDataPacketField(MARKER_UINT8)),
    ('internalModsRealMods', FixedDataPacketField(MARKER_UINT8)),
    ('ignoreLockModsRealMods', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('internalModsVmods', FixedDataPacketField(MARKER_UINT16)),
    ('ignoreLockModsVmods', FixedDataPacketField(MARKER_UINT16)),
    ('repeatDelay', FixedDataPacketField(MARKER_UINT16)),
    ('repeatInterval', FixedDataPacketField(MARKER_UINT16)),
    ('slowKeysDelay', FixedDataPacketField(MARKER_UINT16)),
    ('debounceDelay', FixedDataPacketField(MARKER_UINT16)),
    ('mouseKeysDelay', FixedDataPacketField(MARKER_UINT16)),
    ('mouseKeysInterval', FixedDataPacketField(MARKER_UINT16)),
    ('mouseKeysTimeToMax', FixedDataPacketField(MARKER_UINT16)),
    ('mouseKeysMaxSpeed', FixedDataPacketField(MARKER_UINT16)),
    ('mouseKeysCurve', FixedDataPacketField(MARKER_INT16)),
    ('accessXOption', FixedDataPacketField(MARKER_UINT16)),
    ('accessXTimeout', FixedDataPacketField(MARKER_UINT16)),
    ('accessXTimeoutOptionsMask', FixedDataPacketField(MARKER_UINT16)),
    ('accessXTimeoutOptionsValues', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(2)),
    ('accessXTimeoutMask', FixedDataPacketField(MARKER_UINT32)),
    ('accessXTimeoutValues', FixedDataPacketField(MARKER_UINT32)),
    ('enabledControls', FixedDataPacketField(MARKER_UINT32)),
    ('perKeyRepeat', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: 32, 0)),
))


class GetControlsReplyReply:
    __slots__ = ('deviceid', 'mousekeysdfltbtn', 'numgroups', 'groupswrap', 'internalmodsmask', 'ignorelockmodsmask', 'internalmodsrealmods', 'ignorelockmodsrealmods', 'internalmodsvmods', 'ignorelockmodsvmods', 'repeatdelay', 'repeatinterval', 'slowkeysdelay', 'debouncedelay', 'mousekeysdelay', 'mousekeysinterval', 'mousekeystimetomax', 'mousekeysmaxspeed', 'mousekeyscurve', 'accessxoption', 'accessxtimeout', 'accessxtimeoutoptionsmask', 'accessxtimeoutoptionsvalues', 'accessxtimeoutmask', 'accessxtimeoutvalues', 'enabledcontrols', 'perkeyrepeat',)

    def __init__(
            self, *,
            deviceid: Optional[int] = None,
            mousekeysdfltbtn: Optional[int] = None,
            numgroups: Optional[int] = None,
            groupswrap: Optional[int] = None,
            internalmodsmask: Optional[int] = None,
            ignorelockmodsmask: Optional[int] = None,
            internalmodsrealmods: Optional[int] = None,
            ignorelockmodsrealmods: Optional[int] = None,
            internalmodsvmods: Optional[int] = None,
            ignorelockmodsvmods: Optional[int] = None,
            repeatdelay: Optional[int] = None,
            repeatinterval: Optional[int] = None,
            slowkeysdelay: Optional[int] = None,
            debouncedelay: Optional[int] = None,
            mousekeysdelay: Optional[int] = None,
            mousekeysinterval: Optional[int] = None,
            mousekeystimetomax: Optional[int] = None,
            mousekeysmaxspeed: Optional[int] = None,
            mousekeyscurve: Optional[int] = None,
            accessxoption: Optional[int] = None,
            accessxtimeout: Optional[int] = None,
            accessxtimeoutoptionsmask: Optional[int] = None,
            accessxtimeoutoptionsvalues: Optional[int] = None,
            accessxtimeoutmask: Optional[int] = None,
            accessxtimeoutvalues: Optional[int] = None,
            enabledcontrols: Optional[int] = None,
            perkeyrepeat: Optional[Sequence[int]] = None,
    ) -> None:
        self.deviceid = deviceid
        self.mousekeysdfltbtn = mousekeysdfltbtn
        self.numgroups = numgroups
        self.groupswrap = groupswrap
        self.internalmodsmask = internalmodsmask
        self.ignorelockmodsmask = ignorelockmodsmask
        self.internalmodsrealmods = internalmodsrealmods
        self.ignorelockmodsrealmods = ignorelockmodsrealmods
        self.internalmodsvmods = internalmodsvmods
        self.ignorelockmodsvmods = ignorelockmodsvmods
        self.repeatdelay = repeatdelay
        self.repeatinterval = repeatinterval
        self.slowkeysdelay = slowkeysdelay
        self.debouncedelay = debouncedelay
        self.mousekeysdelay = mousekeysdelay
        self.mousekeysinterval = mousekeysinterval
        self.mousekeystimetomax = mousekeystimetomax
        self.mousekeysmaxspeed = mousekeysmaxspeed
        self.mousekeyscurve = mousekeyscurve
        self.accessxoption = accessxoption
        self.accessxtimeout = accessxtimeout
        self.accessxtimeoutoptionsmask = accessxtimeoutoptionsmask
        self.accessxtimeoutoptionsvalues = accessxtimeoutoptionsvalues
        self.accessxtimeoutmask = accessxtimeoutmask
        self.accessxtimeoutvalues = accessxtimeoutvalues
        self.enabledcontrols = enabledcontrols
        self.perkeyrepeat = perkeyrepeat

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceID': self.deviceid,
            'mouseKeysDfltBtn': self.mousekeysdfltbtn,
            'numGroups': self.numgroups,
            'groupsWrap': self.groupswrap,
            'internalModsMask': self.internalmodsmask,
            'ignoreLockModsMask': self.ignorelockmodsmask,
            'internalModsRealMods': self.internalmodsrealmods,
            'ignoreLockModsRealMods': self.ignorelockmodsrealmods,
            'internalModsVmods': self.internalmodsvmods,
            'ignoreLockModsVmods': self.ignorelockmodsvmods,
            'repeatDelay': self.repeatdelay,
            'repeatInterval': self.repeatinterval,
            'slowKeysDelay': self.slowkeysdelay,
            'debounceDelay': self.debouncedelay,
            'mouseKeysDelay': self.mousekeysdelay,
            'mouseKeysInterval': self.mousekeysinterval,
            'mouseKeysTimeToMax': self.mousekeystimetomax,
            'mouseKeysMaxSpeed': self.mousekeysmaxspeed,
            'mouseKeysCurve': self.mousekeyscurve,
            'accessXOption': self.accessxoption,
            'accessXTimeout': self.accessxtimeout,
            'accessXTimeoutOptionsMask': self.accessxtimeoutoptionsmask,
            'accessXTimeoutOptionsValues': self.accessxtimeoutoptionsvalues,
            'accessXTimeoutMask': self.accessxtimeoutmask,
            'accessXTimeoutValues': self.accessxtimeoutvalues,
            'enabledControls': self.enabledcontrols,
            'perKeyRepeat': self.perkeyrepeat,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetControlsReplyReply':
        return GetControlsReplyReply(**GetControlsReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetControlsReplyReplyPacket.pack(**self.as_dict())


class GetControlsReplyReplyCType(ctypes.Structure):
    """xkb GetControls_reply"""
    _fields_ = [
        ("deviceID", ctypes.c_uint8),
        ("mouseKeysDfltBtn", ctypes.c_uint8),
        ("numGroups", ctypes.c_uint8),
        ("groupsWrap", ctypes.c_uint8),
        ("internalModsMask", ctypes.c_uint8),
        ("ignoreLockModsMask", ctypes.c_uint8),
        ("internalModsRealMods", ctypes.c_uint8),
        ("ignoreLockModsRealMods", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
        ("internalModsVmods", ctypes.c_uint16),
        ("ignoreLockModsVmods", ctypes.c_uint16),
        ("repeatDelay", ctypes.c_uint16),
        ("repeatInterval", ctypes.c_uint16),
        ("slowKeysDelay", ctypes.c_uint16),
        ("debounceDelay", ctypes.c_uint16),
        ("mouseKeysDelay", ctypes.c_uint16),
        ("mouseKeysInterval", ctypes.c_uint16),
        ("mouseKeysTimeToMax", ctypes.c_uint16),
        ("mouseKeysMaxSpeed", ctypes.c_uint16),
        ("mouseKeysCurve", ctypes.c_int16),
        ("accessXOption", ctypes.c_uint16),
        ("accessXTimeout", ctypes.c_uint16),
        ("accessXTimeoutOptionsMask", ctypes.c_uint16),
        ("accessXTimeoutOptionsValues", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 2),
        ("accessXTimeoutMask", ctypes.c_uint32),
        ("accessXTimeoutValues", ctypes.c_uint32),
        ("enabledControls", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


SetControlsRequestPacket = DataPacket((
    ('deviceSpec', FixedDataPacketField(MARKER_UINT32)),
    ('affectInternalRealMods', FixedDataPacketField(MARKER_UINT8)),
    ('internalRealMods', FixedDataPacketField(MARKER_UINT8)),
    ('affectIgnoreLockRealMods', FixedDataPacketField(MARKER_UINT8)),
    ('ignoreLockRealMods', FixedDataPacketField(MARKER_UINT8)),
    ('affectInternalVirtualMods', FixedDataPacketField(MARKER_UINT16)),
    ('internalVirtualMods', FixedDataPacketField(MARKER_UINT16)),
    ('affectIgnoreLockVirtualMods', FixedDataPacketField(MARKER_UINT16)),
    ('ignoreLockVirtualMods', FixedDataPacketField(MARKER_UINT16)),
    ('mouseKeysDfltBtn', FixedDataPacketField(MARKER_UINT8)),
    ('groupsWrap', FixedDataPacketField(MARKER_UINT8)),
    ('accessXOptions', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
    ('affectEnabledControls', FixedDataPacketField(MARKER_UINT32)),
    ('enabledControls', FixedDataPacketField(MARKER_UINT32)),
    ('changeControls', FixedDataPacketField(MARKER_UINT32)),
    ('repeatDelay', FixedDataPacketField(MARKER_UINT16)),
    ('repeatInterval', FixedDataPacketField(MARKER_UINT16)),
    ('slowKeysDelay', FixedDataPacketField(MARKER_UINT16)),
    ('debounceDelay', FixedDataPacketField(MARKER_UINT16)),
    ('mouseKeysDelay', FixedDataPacketField(MARKER_UINT16)),
    ('mouseKeysInterval', FixedDataPacketField(MARKER_UINT16)),
    ('mouseKeysTimeToMax', FixedDataPacketField(MARKER_UINT16)),
    ('mouseKeysMaxSpeed', FixedDataPacketField(MARKER_UINT16)),
    ('mouseKeysCurve', FixedDataPacketField(MARKER_INT16)),
    ('accessXTimeout', FixedDataPacketField(MARKER_UINT16)),
    ('accessXTimeoutMask', FixedDataPacketField(MARKER_UINT32)),
    ('accessXTimeoutValues', FixedDataPacketField(MARKER_UINT32)),
    ('accessXTimeoutOptionsMask', FixedDataPacketField(MARKER_UINT16)),
    ('accessXTimeoutOptionsValues', FixedDataPacketField(MARKER_UINT16)),
    ('perKeyRepeat', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: 32, 0)),
))


class SetControlsRequest:
    OPCODE = 7

    __slots__ = ('devicespec', 'affectinternalrealmods', 'internalrealmods', 'affectignorelockrealmods', 'ignorelockrealmods', 'affectinternalvirtualmods', 'internalvirtualmods', 'affectignorelockvirtualmods', 'ignorelockvirtualmods', 'mousekeysdfltbtn', 'groupswrap', 'accessxoptions', 'affectenabledcontrols', 'enabledcontrols', 'changecontrols', 'repeatdelay', 'repeatinterval', 'slowkeysdelay', 'debouncedelay', 'mousekeysdelay', 'mousekeysinterval', 'mousekeystimetomax', 'mousekeysmaxspeed', 'mousekeyscurve', 'accessxtimeout', 'accessxtimeoutmask', 'accessxtimeoutvalues', 'accessxtimeoutoptionsmask', 'accessxtimeoutoptionsvalues', 'perkeyrepeat',)

    def __init__(
            self, *,
            devicespec: Optional[int] = None,
            affectinternalrealmods: Optional[int] = None,
            internalrealmods: Optional[int] = None,
            affectignorelockrealmods: Optional[int] = None,
            ignorelockrealmods: Optional[int] = None,
            affectinternalvirtualmods: Optional[int] = None,
            internalvirtualmods: Optional[int] = None,
            affectignorelockvirtualmods: Optional[int] = None,
            ignorelockvirtualmods: Optional[int] = None,
            mousekeysdfltbtn: Optional[int] = None,
            groupswrap: Optional[int] = None,
            accessxoptions: Optional[int] = None,
            affectenabledcontrols: Optional[int] = None,
            enabledcontrols: Optional[int] = None,
            changecontrols: Optional[int] = None,
            repeatdelay: Optional[int] = None,
            repeatinterval: Optional[int] = None,
            slowkeysdelay: Optional[int] = None,
            debouncedelay: Optional[int] = None,
            mousekeysdelay: Optional[int] = None,
            mousekeysinterval: Optional[int] = None,
            mousekeystimetomax: Optional[int] = None,
            mousekeysmaxspeed: Optional[int] = None,
            mousekeyscurve: Optional[int] = None,
            accessxtimeout: Optional[int] = None,
            accessxtimeoutmask: Optional[int] = None,
            accessxtimeoutvalues: Optional[int] = None,
            accessxtimeoutoptionsmask: Optional[int] = None,
            accessxtimeoutoptionsvalues: Optional[int] = None,
            perkeyrepeat: Optional[Sequence[int]] = None,
    ) -> None:
        self.devicespec = devicespec
        self.affectinternalrealmods = affectinternalrealmods
        self.internalrealmods = internalrealmods
        self.affectignorelockrealmods = affectignorelockrealmods
        self.ignorelockrealmods = ignorelockrealmods
        self.affectinternalvirtualmods = affectinternalvirtualmods
        self.internalvirtualmods = internalvirtualmods
        self.affectignorelockvirtualmods = affectignorelockvirtualmods
        self.ignorelockvirtualmods = ignorelockvirtualmods
        self.mousekeysdfltbtn = mousekeysdfltbtn
        self.groupswrap = groupswrap
        self.accessxoptions = accessxoptions
        self.affectenabledcontrols = affectenabledcontrols
        self.enabledcontrols = enabledcontrols
        self.changecontrols = changecontrols
        self.repeatdelay = repeatdelay
        self.repeatinterval = repeatinterval
        self.slowkeysdelay = slowkeysdelay
        self.debouncedelay = debouncedelay
        self.mousekeysdelay = mousekeysdelay
        self.mousekeysinterval = mousekeysinterval
        self.mousekeystimetomax = mousekeystimetomax
        self.mousekeysmaxspeed = mousekeysmaxspeed
        self.mousekeyscurve = mousekeyscurve
        self.accessxtimeout = accessxtimeout
        self.accessxtimeoutmask = accessxtimeoutmask
        self.accessxtimeoutvalues = accessxtimeoutvalues
        self.accessxtimeoutoptionsmask = accessxtimeoutoptionsmask
        self.accessxtimeoutoptionsvalues = accessxtimeoutoptionsvalues
        self.perkeyrepeat = perkeyrepeat

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceSpec': self.devicespec,
            'affectInternalRealMods': self.affectinternalrealmods,
            'internalRealMods': self.internalrealmods,
            'affectIgnoreLockRealMods': self.affectignorelockrealmods,
            'ignoreLockRealMods': self.ignorelockrealmods,
            'affectInternalVirtualMods': self.affectinternalvirtualmods,
            'internalVirtualMods': self.internalvirtualmods,
            'affectIgnoreLockVirtualMods': self.affectignorelockvirtualmods,
            'ignoreLockVirtualMods': self.ignorelockvirtualmods,
            'mouseKeysDfltBtn': self.mousekeysdfltbtn,
            'groupsWrap': self.groupswrap,
            'accessXOptions': self.accessxoptions,
            'affectEnabledControls': self.affectenabledcontrols,
            'enabledControls': self.enabledcontrols,
            'changeControls': self.changecontrols,
            'repeatDelay': self.repeatdelay,
            'repeatInterval': self.repeatinterval,
            'slowKeysDelay': self.slowkeysdelay,
            'debounceDelay': self.debouncedelay,
            'mouseKeysDelay': self.mousekeysdelay,
            'mouseKeysInterval': self.mousekeysinterval,
            'mouseKeysTimeToMax': self.mousekeystimetomax,
            'mouseKeysMaxSpeed': self.mousekeysmaxspeed,
            'mouseKeysCurve': self.mousekeyscurve,
            'accessXTimeout': self.accessxtimeout,
            'accessXTimeoutMask': self.accessxtimeoutmask,
            'accessXTimeoutValues': self.accessxtimeoutvalues,
            'accessXTimeoutOptionsMask': self.accessxtimeoutoptionsmask,
            'accessXTimeoutOptionsValues': self.accessxtimeoutoptionsvalues,
            'perKeyRepeat': self.perkeyrepeat,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetControlsRequest':
        return SetControlsRequest(**SetControlsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetControlsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetControlsRequest.lib = library.xkb_setcontrols
        SetControlsRequest.lib.restype = ctypes.c_uint32
        SetControlsRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint16, ctypes.c_uint8 * 2, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_int16, ctypes.c_uint16, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_void_p)


class SetControlsRequestCType(ctypes.Structure):
    """xkb SetControls"""
    _fields_ = [
        ("deviceSpec", ctypes.c_uint32),
        ("affectInternalRealMods", ctypes.c_uint8),
        ("internalRealMods", ctypes.c_uint8),
        ("affectIgnoreLockRealMods", ctypes.c_uint8),
        ("ignoreLockRealMods", ctypes.c_uint8),
        ("affectInternalVirtualMods", ctypes.c_uint16),
        ("internalVirtualMods", ctypes.c_uint16),
        ("affectIgnoreLockVirtualMods", ctypes.c_uint16),
        ("ignoreLockVirtualMods", ctypes.c_uint16),
        ("mouseKeysDfltBtn", ctypes.c_uint8),
        ("groupsWrap", ctypes.c_uint8),
        ("accessXOptions", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
        ("affectEnabledControls", ctypes.c_uint32),
        ("enabledControls", ctypes.c_uint32),
        ("changeControls", ctypes.c_uint32),
        ("repeatDelay", ctypes.c_uint16),
        ("repeatInterval", ctypes.c_uint16),
        ("slowKeysDelay", ctypes.c_uint16),
        ("debounceDelay", ctypes.c_uint16),
        ("mouseKeysDelay", ctypes.c_uint16),
        ("mouseKeysInterval", ctypes.c_uint16),
        ("mouseKeysTimeToMax", ctypes.c_uint16),
        ("mouseKeysMaxSpeed", ctypes.c_uint16),
        ("mouseKeysCurve", ctypes.c_int16),
        ("accessXTimeout", ctypes.c_uint16),
        ("accessXTimeoutMask", ctypes.c_uint32),
        ("accessXTimeoutValues", ctypes.c_uint32),
        ("accessXTimeoutOptionsMask", ctypes.c_uint16),
        ("accessXTimeoutOptionsValues", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


GetMapRequestCookie = NewType('GetMapRequestCookie', ctypes.c_uint32)


GetMapRequestPacket = DataPacket((
    ('deviceSpec', FixedDataPacketField(MARKER_UINT32)),
    ('full', FixedDataPacketField(MARKER_UINT16)),
    ('partial', FixedDataPacketField(MARKER_UINT16)),
    ('firstType', FixedDataPacketField(MARKER_UINT8)),
    ('nTypes', FixedDataPacketField(MARKER_UINT8)),
    ('firstKeySym', FixedDataPacketField(MARKER_UINT32)),
    ('nKeySyms', FixedDataPacketField(MARKER_UINT8)),
    ('firstKeyAction', FixedDataPacketField(MARKER_UINT32)),
    ('nKeyActions', FixedDataPacketField(MARKER_UINT8)),
    ('firstKeyBehavior', FixedDataPacketField(MARKER_UINT32)),
    ('nKeyBehaviors', FixedDataPacketField(MARKER_UINT8)),
    ('virtualMods', FixedDataPacketField(MARKER_UINT16)),
    ('firstKeyExplicit', FixedDataPacketField(MARKER_UINT32)),
    ('nKeyExplicit', FixedDataPacketField(MARKER_UINT8)),
    ('firstModMapKey', FixedDataPacketField(MARKER_UINT32)),
    ('nModMapKeys', FixedDataPacketField(MARKER_UINT8)),
    ('firstVModMapKey', FixedDataPacketField(MARKER_UINT32)),
    ('nVModMapKeys', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
))


class GetMapRequest:
    OPCODE = 8

    __slots__ = ('devicespec', 'full', 'partial', 'firsttype', 'ntypes', 'firstkeysym', 'nkeysyms', 'firstkeyaction', 'nkeyactions', 'firstkeybehavior', 'nkeybehaviors', 'virtualmods', 'firstkeyexplicit', 'nkeyexplicit', 'firstmodmapkey', 'nmodmapkeys', 'firstvmodmapkey', 'nvmodmapkeys',)

    def __init__(
            self, *,
            devicespec: Optional[int] = None,
            full: Optional[int] = None,
            partial: Optional[int] = None,
            firsttype: Optional[int] = None,
            ntypes: Optional[int] = None,
            firstkeysym: Optional[int] = None,
            nkeysyms: Optional[int] = None,
            firstkeyaction: Optional[int] = None,
            nkeyactions: Optional[int] = None,
            firstkeybehavior: Optional[int] = None,
            nkeybehaviors: Optional[int] = None,
            virtualmods: Optional[int] = None,
            firstkeyexplicit: Optional[int] = None,
            nkeyexplicit: Optional[int] = None,
            firstmodmapkey: Optional[int] = None,
            nmodmapkeys: Optional[int] = None,
            firstvmodmapkey: Optional[int] = None,
            nvmodmapkeys: Optional[int] = None,
    ) -> None:
        self.devicespec = devicespec
        self.full = full
        self.partial = partial
        self.firsttype = firsttype
        self.ntypes = ntypes
        self.firstkeysym = firstkeysym
        self.nkeysyms = nkeysyms
        self.firstkeyaction = firstkeyaction
        self.nkeyactions = nkeyactions
        self.firstkeybehavior = firstkeybehavior
        self.nkeybehaviors = nkeybehaviors
        self.virtualmods = virtualmods
        self.firstkeyexplicit = firstkeyexplicit
        self.nkeyexplicit = nkeyexplicit
        self.firstmodmapkey = firstmodmapkey
        self.nmodmapkeys = nmodmapkeys
        self.firstvmodmapkey = firstvmodmapkey
        self.nvmodmapkeys = nvmodmapkeys

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceSpec': self.devicespec,
            'full': self.full,
            'partial': self.partial,
            'firstType': self.firsttype,
            'nTypes': self.ntypes,
            'firstKeySym': self.firstkeysym,
            'nKeySyms': self.nkeysyms,
            'firstKeyAction': self.firstkeyaction,
            'nKeyActions': self.nkeyactions,
            'firstKeyBehavior': self.firstkeybehavior,
            'nKeyBehaviors': self.nkeybehaviors,
            'virtualMods': self.virtualmods,
            'firstKeyExplicit': self.firstkeyexplicit,
            'nKeyExplicit': self.nkeyexplicit,
            'firstModMapKey': self.firstmodmapkey,
            'nModMapKeys': self.nmodmapkeys,
            'firstVModMapKey': self.firstvmodmapkey,
            'nVModMapKeys': self.nvmodmapkeys,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetMapRequest':
        return GetMapRequest(**GetMapRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetMapRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int], GetMapRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetMapRequest.lib = library.xkb_getmap
        GetMapRequest.lib.restype = GetMapRequestCookie
        GetMapRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint16, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8 * 2)


class GetMapRequestCType(ctypes.Structure):
    """xkb GetMap"""
    _fields_ = [
        ("deviceSpec", ctypes.c_uint32),
        ("full", ctypes.c_uint16),
        ("partial", ctypes.c_uint16),
        ("firstType", ctypes.c_uint8),
        ("nTypes", ctypes.c_uint8),
        ("firstKeySym", ctypes.c_uint32),
        ("nKeySyms", ctypes.c_uint8),
        ("firstKeyAction", ctypes.c_uint32),
        ("nKeyActions", ctypes.c_uint8),
        ("firstKeyBehavior", ctypes.c_uint32),
        ("nKeyBehaviors", ctypes.c_uint8),
        ("virtualMods", ctypes.c_uint16),
        ("firstKeyExplicit", ctypes.c_uint32),
        ("nKeyExplicit", ctypes.c_uint8),
        ("firstModMapKey", ctypes.c_uint32),
        ("nModMapKeys", ctypes.c_uint8),
        ("firstVModMapKey", ctypes.c_uint32),
        ("nVModMapKeys", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 2),
    ]


GetMapReplyReplyPacket = DataPacket((
    ('deviceID', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
    ('minKeyCode', FixedDataPacketField(MARKER_UINT32)),
    ('maxKeyCode', FixedDataPacketField(MARKER_UINT32)),
    ('present', FixedDataPacketField(MARKER_UINT16)),
    ('firstType', FixedDataPacketField(MARKER_UINT8)),
    ('nTypes', FixedDataPacketField(MARKER_UINT8)),
    ('totalTypes', FixedDataPacketField(MARKER_UINT8)),
    ('firstKeySym', FixedDataPacketField(MARKER_UINT32)),
    ('totalSyms', FixedDataPacketField(MARKER_UINT16)),
    ('nKeySyms', FixedDataPacketField(MARKER_UINT8)),
    ('firstKeyAction', FixedDataPacketField(MARKER_UINT32)),
    ('totalActions', FixedDataPacketField(MARKER_UINT16)),
    ('nKeyActions', FixedDataPacketField(MARKER_UINT8)),
    ('firstKeyBehavior', FixedDataPacketField(MARKER_UINT32)),
    ('nKeyBehaviors', FixedDataPacketField(MARKER_UINT8)),
    ('totalKeyBehaviors', FixedDataPacketField(MARKER_UINT8)),
    ('firstKeyExplicit', FixedDataPacketField(MARKER_UINT32)),
    ('nKeyExplicit', FixedDataPacketField(MARKER_UINT8)),
    ('totalKeyExplicit', FixedDataPacketField(MARKER_UINT8)),
    ('firstModMapKey', FixedDataPacketField(MARKER_UINT32)),
    ('nModMapKeys', FixedDataPacketField(MARKER_UINT8)),
    ('totalModMapKeys', FixedDataPacketField(MARKER_UINT8)),
    ('firstVModMapKey', FixedDataPacketField(MARKER_UINT32)),
    ('nVModMapKeys', FixedDataPacketField(MARKER_UINT8)),
    ('totalVModMapKeys', FixedDataPacketField(MARKER_UINT8)),
    ('pad1', FixedPadDataPacketField(1)),
    ('virtualMods', FixedDataPacketField(MARKER_UINT16)),
    ('map', BitDataPacketField(lambda d, c: d['present'], {
        MapPartValues.KEY_TYPES: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nTypes'], 0),
        MapPartValues.KEY_SYMS: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nKeySyms'], 0),
        MapPartValues.KEY_ACTIONS: StructureDataPacketField((
            ('acts_rtrn_count', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: d['nKeyActions'], 0)),
            ('pad0', AlignedPadDataPacketField(4)),
            ('acts_rtrn_acts', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['totalActions'], 0)),
        )),
        MapPartValues.KEY_BEHAVIORS: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['totalKeyBehaviors'], 0),
        MapPartValues.VIRTUAL_MODS: StructureDataPacketField((
            ('vmods_rtrn', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: d['virtualMods'], 0)),
            ('pad0', AlignedPadDataPacketField(4)),
        )),
        MapPartValues.EXPLICIT_COMPONENTS: StructureDataPacketField((
            ('explicit_rtrn', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['totalKeyExplicit'], 0)),
            ('pad0', AlignedPadDataPacketField(4)),
        )),
        MapPartValues.MODIFIER_MAP: StructureDataPacketField((
            ('modmap_rtrn', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['totalModMapKeys'], 0)),
            ('pad0', AlignedPadDataPacketField(4)),
        )),
        MapPartValues.VIRTUAL_MOD_MAP: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['totalVModMapKeys'], 0),
    }, 0)),
))


class GetMapReplyReply:
    __slots__ = ('deviceid', 'minkeycode', 'maxkeycode', 'present', 'firsttype', 'ntypes', 'totaltypes', 'firstkeysym', 'totalsyms', 'nkeysyms', 'firstkeyaction', 'totalactions', 'nkeyactions', 'firstkeybehavior', 'nkeybehaviors', 'totalkeybehaviors', 'firstkeyexplicit', 'nkeyexplicit', 'totalkeyexplicit', 'firstmodmapkey', 'nmodmapkeys', 'totalmodmapkeys', 'firstvmodmapkey', 'nvmodmapkeys', 'totalvmodmapkeys', 'virtualmods', 'map',)

    def __init__(
            self, *,
            deviceid: Optional[int] = None,
            minkeycode: Optional[int] = None,
            maxkeycode: Optional[int] = None,
            present: Optional[int] = None,
            firsttype: Optional[int] = None,
            ntypes: Optional[int] = None,
            totaltypes: Optional[int] = None,
            firstkeysym: Optional[int] = None,
            totalsyms: Optional[int] = None,
            nkeysyms: Optional[int] = None,
            firstkeyaction: Optional[int] = None,
            totalactions: Optional[int] = None,
            nkeyactions: Optional[int] = None,
            firstkeybehavior: Optional[int] = None,
            nkeybehaviors: Optional[int] = None,
            totalkeybehaviors: Optional[int] = None,
            firstkeyexplicit: Optional[int] = None,
            nkeyexplicit: Optional[int] = None,
            totalkeyexplicit: Optional[int] = None,
            firstmodmapkey: Optional[int] = None,
            nmodmapkeys: Optional[int] = None,
            totalmodmapkeys: Optional[int] = None,
            firstvmodmapkey: Optional[int] = None,
            nvmodmapkeys: Optional[int] = None,
            totalvmodmapkeys: Optional[int] = None,
            virtualmods: Optional[int] = None,
            map: Optional[Mapping[str, MapPartValues]] = None,
    ) -> None:
        self.deviceid = deviceid
        self.minkeycode = minkeycode
        self.maxkeycode = maxkeycode
        self.present = present
        self.firsttype = firsttype
        self.ntypes = ntypes
        self.totaltypes = totaltypes
        self.firstkeysym = firstkeysym
        self.totalsyms = totalsyms
        self.nkeysyms = nkeysyms
        self.firstkeyaction = firstkeyaction
        self.totalactions = totalactions
        self.nkeyactions = nkeyactions
        self.firstkeybehavior = firstkeybehavior
        self.nkeybehaviors = nkeybehaviors
        self.totalkeybehaviors = totalkeybehaviors
        self.firstkeyexplicit = firstkeyexplicit
        self.nkeyexplicit = nkeyexplicit
        self.totalkeyexplicit = totalkeyexplicit
        self.firstmodmapkey = firstmodmapkey
        self.nmodmapkeys = nmodmapkeys
        self.totalmodmapkeys = totalmodmapkeys
        self.firstvmodmapkey = firstvmodmapkey
        self.nvmodmapkeys = nvmodmapkeys
        self.totalvmodmapkeys = totalvmodmapkeys
        self.virtualmods = virtualmods
        self.map = map

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceID': self.deviceid,
            'minKeyCode': self.minkeycode,
            'maxKeyCode': self.maxkeycode,
            'present': self.present,
            'firstType': self.firsttype,
            'nTypes': self.ntypes,
            'totalTypes': self.totaltypes,
            'firstKeySym': self.firstkeysym,
            'totalSyms': self.totalsyms,
            'nKeySyms': self.nkeysyms,
            'firstKeyAction': self.firstkeyaction,
            'totalActions': self.totalactions,
            'nKeyActions': self.nkeyactions,
            'firstKeyBehavior': self.firstkeybehavior,
            'nKeyBehaviors': self.nkeybehaviors,
            'totalKeyBehaviors': self.totalkeybehaviors,
            'firstKeyExplicit': self.firstkeyexplicit,
            'nKeyExplicit': self.nkeyexplicit,
            'totalKeyExplicit': self.totalkeyexplicit,
            'firstModMapKey': self.firstmodmapkey,
            'nModMapKeys': self.nmodmapkeys,
            'totalModMapKeys': self.totalmodmapkeys,
            'firstVModMapKey': self.firstvmodmapkey,
            'nVModMapKeys': self.nvmodmapkeys,
            'totalVModMapKeys': self.totalvmodmapkeys,
            'virtualMods': self.virtualmods,
            'map': self.map,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetMapReplyReply':
        return GetMapReplyReply(**GetMapReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetMapReplyReplyPacket.pack(**self.as_dict())


class GetMapReplyReplyCType(ctypes.Structure):
    """xkb GetMap_reply"""
    _fields_ = [
        ("deviceID", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 2),
        ("minKeyCode", ctypes.c_uint32),
        ("maxKeyCode", ctypes.c_uint32),
        ("present", ctypes.c_uint16),
        ("firstType", ctypes.c_uint8),
        ("nTypes", ctypes.c_uint8),
        ("totalTypes", ctypes.c_uint8),
        ("firstKeySym", ctypes.c_uint32),
        ("totalSyms", ctypes.c_uint16),
        ("nKeySyms", ctypes.c_uint8),
        ("firstKeyAction", ctypes.c_uint32),
        ("totalActions", ctypes.c_uint16),
        ("nKeyActions", ctypes.c_uint8),
        ("firstKeyBehavior", ctypes.c_uint32),
        ("nKeyBehaviors", ctypes.c_uint8),
        ("totalKeyBehaviors", ctypes.c_uint8),
        ("firstKeyExplicit", ctypes.c_uint32),
        ("nKeyExplicit", ctypes.c_uint8),
        ("totalKeyExplicit", ctypes.c_uint8),
        ("firstModMapKey", ctypes.c_uint32),
        ("nModMapKeys", ctypes.c_uint8),
        ("totalModMapKeys", ctypes.c_uint8),
        ("firstVModMapKey", ctypes.c_uint32),
        ("nVModMapKeys", ctypes.c_uint8),
        ("totalVModMapKeys", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8),
        ("virtualMods", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


SetMapRequestPacket = DataPacket((
    ('deviceSpec', FixedDataPacketField(MARKER_UINT32)),
    ('present', FixedDataPacketField(MARKER_UINT16)),
    ('flags', FixedDataPacketField(MARKER_UINT16)),
    ('minKeyCode', FixedDataPacketField(MARKER_UINT32)),
    ('maxKeyCode', FixedDataPacketField(MARKER_UINT32)),
    ('firstType', FixedDataPacketField(MARKER_UINT8)),
    ('nTypes', FixedDataPacketField(MARKER_UINT8)),
    ('firstKeySym', FixedDataPacketField(MARKER_UINT32)),
    ('nKeySyms', FixedDataPacketField(MARKER_UINT8)),
    ('totalSyms', FixedDataPacketField(MARKER_UINT16)),
    ('firstKeyAction', FixedDataPacketField(MARKER_UINT32)),
    ('nKeyActions', FixedDataPacketField(MARKER_UINT8)),
    ('totalActions', FixedDataPacketField(MARKER_UINT16)),
    ('firstKeyBehavior', FixedDataPacketField(MARKER_UINT32)),
    ('nKeyBehaviors', FixedDataPacketField(MARKER_UINT8)),
    ('totalKeyBehaviors', FixedDataPacketField(MARKER_UINT8)),
    ('firstKeyExplicit', FixedDataPacketField(MARKER_UINT32)),
    ('nKeyExplicit', FixedDataPacketField(MARKER_UINT8)),
    ('totalKeyExplicit', FixedDataPacketField(MARKER_UINT8)),
    ('firstModMapKey', FixedDataPacketField(MARKER_UINT32)),
    ('nModMapKeys', FixedDataPacketField(MARKER_UINT8)),
    ('totalModMapKeys', FixedDataPacketField(MARKER_UINT8)),
    ('firstVModMapKey', FixedDataPacketField(MARKER_UINT32)),
    ('nVModMapKeys', FixedDataPacketField(MARKER_UINT8)),
    ('totalVModMapKeys', FixedDataPacketField(MARKER_UINT8)),
    ('virtualMods', FixedDataPacketField(MARKER_UINT16)),
    ('values', BitDataPacketField(lambda d, c: d['present'], {
        MapPartValues.KEY_TYPES: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nTypes'], 0),
        MapPartValues.KEY_SYMS: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nKeySyms'], 0),
        MapPartValues.KEY_ACTIONS: StructureDataPacketField((
            ('actionsCount', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: d['nKeyActions'], 0)),
            ('pad0', AlignedPadDataPacketField(4)),
            ('actions', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['totalActions'], 0)),
        )),
        MapPartValues.KEY_BEHAVIORS: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['totalKeyBehaviors'], 0),
        MapPartValues.VIRTUAL_MODS: StructureDataPacketField((
            ('vmods', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: d['virtualMods'], 0)),
            ('pad0', AlignedPadDataPacketField(4)),
        )),
        MapPartValues.EXPLICIT_COMPONENTS: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['totalKeyExplicit'], 0),
        MapPartValues.MODIFIER_MAP: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['totalModMapKeys'], 0),
        MapPartValues.VIRTUAL_MOD_MAP: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['totalVModMapKeys'], 0),
    }, 0)),
))


class SetMapRequest:
    OPCODE = 9

    __slots__ = ('devicespec', 'present', 'flags', 'minkeycode', 'maxkeycode', 'firsttype', 'ntypes', 'firstkeysym', 'nkeysyms', 'totalsyms', 'firstkeyaction', 'nkeyactions', 'totalactions', 'firstkeybehavior', 'nkeybehaviors', 'totalkeybehaviors', 'firstkeyexplicit', 'nkeyexplicit', 'totalkeyexplicit', 'firstmodmapkey', 'nmodmapkeys', 'totalmodmapkeys', 'firstvmodmapkey', 'nvmodmapkeys', 'totalvmodmapkeys', 'virtualmods', 'values',)

    def __init__(
            self, *,
            devicespec: Optional[int] = None,
            present: Optional[int] = None,
            flags: Optional[int] = None,
            minkeycode: Optional[int] = None,
            maxkeycode: Optional[int] = None,
            firsttype: Optional[int] = None,
            ntypes: Optional[int] = None,
            firstkeysym: Optional[int] = None,
            nkeysyms: Optional[int] = None,
            totalsyms: Optional[int] = None,
            firstkeyaction: Optional[int] = None,
            nkeyactions: Optional[int] = None,
            totalactions: Optional[int] = None,
            firstkeybehavior: Optional[int] = None,
            nkeybehaviors: Optional[int] = None,
            totalkeybehaviors: Optional[int] = None,
            firstkeyexplicit: Optional[int] = None,
            nkeyexplicit: Optional[int] = None,
            totalkeyexplicit: Optional[int] = None,
            firstmodmapkey: Optional[int] = None,
            nmodmapkeys: Optional[int] = None,
            totalmodmapkeys: Optional[int] = None,
            firstvmodmapkey: Optional[int] = None,
            nvmodmapkeys: Optional[int] = None,
            totalvmodmapkeys: Optional[int] = None,
            virtualmods: Optional[int] = None,
            values: Optional[Mapping[str, MapPartValues]] = None,
    ) -> None:
        self.devicespec = devicespec
        self.present = present
        self.flags = flags
        self.minkeycode = minkeycode
        self.maxkeycode = maxkeycode
        self.firsttype = firsttype
        self.ntypes = ntypes
        self.firstkeysym = firstkeysym
        self.nkeysyms = nkeysyms
        self.totalsyms = totalsyms
        self.firstkeyaction = firstkeyaction
        self.nkeyactions = nkeyactions
        self.totalactions = totalactions
        self.firstkeybehavior = firstkeybehavior
        self.nkeybehaviors = nkeybehaviors
        self.totalkeybehaviors = totalkeybehaviors
        self.firstkeyexplicit = firstkeyexplicit
        self.nkeyexplicit = nkeyexplicit
        self.totalkeyexplicit = totalkeyexplicit
        self.firstmodmapkey = firstmodmapkey
        self.nmodmapkeys = nmodmapkeys
        self.totalmodmapkeys = totalmodmapkeys
        self.firstvmodmapkey = firstvmodmapkey
        self.nvmodmapkeys = nvmodmapkeys
        self.totalvmodmapkeys = totalvmodmapkeys
        self.virtualmods = virtualmods
        self.values = values

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceSpec': self.devicespec,
            'present': self.present,
            'flags': self.flags,
            'minKeyCode': self.minkeycode,
            'maxKeyCode': self.maxkeycode,
            'firstType': self.firsttype,
            'nTypes': self.ntypes,
            'firstKeySym': self.firstkeysym,
            'nKeySyms': self.nkeysyms,
            'totalSyms': self.totalsyms,
            'firstKeyAction': self.firstkeyaction,
            'nKeyActions': self.nkeyactions,
            'totalActions': self.totalactions,
            'firstKeyBehavior': self.firstkeybehavior,
            'nKeyBehaviors': self.nkeybehaviors,
            'totalKeyBehaviors': self.totalkeybehaviors,
            'firstKeyExplicit': self.firstkeyexplicit,
            'nKeyExplicit': self.nkeyexplicit,
            'totalKeyExplicit': self.totalkeyexplicit,
            'firstModMapKey': self.firstmodmapkey,
            'nModMapKeys': self.nmodmapkeys,
            'totalModMapKeys': self.totalmodmapkeys,
            'firstVModMapKey': self.firstvmodmapkey,
            'nVModMapKeys': self.nvmodmapkeys,
            'totalVModMapKeys': self.totalvmodmapkeys,
            'virtualMods': self.virtualmods,
            'values': self.values,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetMapRequest':
        return SetMapRequest(**SetMapRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetMapRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, Mapping[str, MapPartValues]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetMapRequest.lib = library.xkb_setmap
        SetMapRequest.lib.restype = ctypes.c_uint32
        SetMapRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint16, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint16, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint16, ctypes.c_void_p)


class SetMapRequestCType(ctypes.Structure):
    """xkb SetMap"""
    _fields_ = [
        ("deviceSpec", ctypes.c_uint32),
        ("present", ctypes.c_uint16),
        ("flags", ctypes.c_uint16),
        ("minKeyCode", ctypes.c_uint32),
        ("maxKeyCode", ctypes.c_uint32),
        ("firstType", ctypes.c_uint8),
        ("nTypes", ctypes.c_uint8),
        ("firstKeySym", ctypes.c_uint32),
        ("nKeySyms", ctypes.c_uint8),
        ("totalSyms", ctypes.c_uint16),
        ("firstKeyAction", ctypes.c_uint32),
        ("nKeyActions", ctypes.c_uint8),
        ("totalActions", ctypes.c_uint16),
        ("firstKeyBehavior", ctypes.c_uint32),
        ("nKeyBehaviors", ctypes.c_uint8),
        ("totalKeyBehaviors", ctypes.c_uint8),
        ("firstKeyExplicit", ctypes.c_uint32),
        ("nKeyExplicit", ctypes.c_uint8),
        ("totalKeyExplicit", ctypes.c_uint8),
        ("firstModMapKey", ctypes.c_uint32),
        ("nModMapKeys", ctypes.c_uint8),
        ("totalModMapKeys", ctypes.c_uint8),
        ("firstVModMapKey", ctypes.c_uint32),
        ("nVModMapKeys", ctypes.c_uint8),
        ("totalVModMapKeys", ctypes.c_uint8),
        ("virtualMods", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


GetCompatMapRequestCookie = NewType('GetCompatMapRequestCookie', ctypes.c_uint32)


GetCompatMapRequestPacket = DataPacket((
    ('deviceSpec', FixedDataPacketField(MARKER_UINT32)),
    ('groups', FixedDataPacketField(MARKER_UINT8)),
    ('getAllSI', FixedDataPacketField(MARKER_UINT8)),
    ('firstSI', FixedDataPacketField(MARKER_UINT16)),
    ('nSI', FixedDataPacketField(MARKER_UINT16)),
))


class GetCompatMapRequest:
    OPCODE = 10

    __slots__ = ('devicespec', 'groups', 'getallsi', 'firstsi', 'nsi',)

    def __init__(
            self, *,
            devicespec: Optional[int] = None,
            groups: Optional[int] = None,
            getallsi: Optional[bool] = None,
            firstsi: Optional[int] = None,
            nsi: Optional[int] = None,
    ) -> None:
        self.devicespec = devicespec
        self.groups = groups
        self.getallsi = getallsi
        self.firstsi = firstsi
        self.nsi = nsi

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceSpec': self.devicespec,
            'groups': self.groups,
            'getAllSI': self.getallsi,
            'firstSI': self.firstsi,
            'nSI': self.nsi,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetCompatMapRequest':
        return GetCompatMapRequest(**GetCompatMapRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetCompatMapRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, bool, int, int], GetCompatMapRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetCompatMapRequest.lib = library.xkb_getcompatmap
        GetCompatMapRequest.lib.restype = GetCompatMapRequestCookie
        GetCompatMapRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint8, ctypes.c_int8, ctypes.c_uint16, ctypes.c_uint16)


class GetCompatMapRequestCType(ctypes.Structure):
    """xkb GetCompatMap"""
    _fields_ = [
        ("deviceSpec", ctypes.c_uint32),
        ("groups", ctypes.c_uint8),
        ("getAllSI", ctypes.c_int8),
        ("firstSI", ctypes.c_uint16),
        ("nSI", ctypes.c_uint16),
    ]


GetCompatMapReplyReplyPacket = DataPacket((
    ('deviceID', FixedDataPacketField(MARKER_UINT8)),
    ('groupsRtrn', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('firstSIRtrn', FixedDataPacketField(MARKER_UINT16)),
    ('nSIRtrn', FixedDataPacketField(MARKER_UINT16)),
    ('nTotalSI', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(16)),
    ('si_rtrn', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nSIRtrn'], 0)),
    ('group_rtrn', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['groupsRtrn'], 0)),
))


class GetCompatMapReplyReply:
    __slots__ = ('deviceid', 'groupsrtrn', 'firstsirtrn', 'nsirtrn', 'ntotalsi', 'si_rtrn', 'group_rtrn',)

    def __init__(
            self, *,
            deviceid: Optional[int] = None,
            groupsrtrn: Optional[int] = None,
            firstsirtrn: Optional[int] = None,
            nsirtrn: Optional[int] = None,
            ntotalsi: Optional[int] = None,
            si_rtrn: Optional[Sequence[int]] = None,
            group_rtrn: Optional[Sequence[int]] = None,
    ) -> None:
        self.deviceid = deviceid
        self.groupsrtrn = groupsrtrn
        self.firstsirtrn = firstsirtrn
        self.nsirtrn = nsirtrn
        self.ntotalsi = ntotalsi
        self.si_rtrn = si_rtrn
        self.group_rtrn = group_rtrn

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceID': self.deviceid,
            'groupsRtrn': self.groupsrtrn,
            'firstSIRtrn': self.firstsirtrn,
            'nSIRtrn': self.nsirtrn,
            'nTotalSI': self.ntotalsi,
            'si_rtrn': self.si_rtrn,
            'group_rtrn': self.group_rtrn,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetCompatMapReplyReply':
        return GetCompatMapReplyReply(**GetCompatMapReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetCompatMapReplyReplyPacket.pack(**self.as_dict())


class GetCompatMapReplyReplyCType(ctypes.Structure):
    """xkb GetCompatMap_reply"""
    _fields_ = [
        ("deviceID", ctypes.c_uint8),
        ("groupsRtrn", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
        ("firstSIRtrn", ctypes.c_uint16),
        ("nSIRtrn", ctypes.c_uint16),
        ("nTotalSI", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 16),
        ("var_data", ctypes.c_void_p),
    ]


SetCompatMapRequestPacket = DataPacket((
    ('deviceSpec', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(1)),
    ('recomputeActions', FixedDataPacketField(MARKER_UINT8)),
    ('truncateSI', FixedDataPacketField(MARKER_UINT8)),
    ('groups', FixedDataPacketField(MARKER_UINT8)),
    ('firstSI', FixedDataPacketField(MARKER_UINT16)),
    ('nSI', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(2)),
    ('si', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nSI'], 0)),
    ('groupMaps', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['groups'], 0)),
))


class SetCompatMapRequest:
    OPCODE = 11

    __slots__ = ('devicespec', 'recomputeactions', 'truncatesi', 'groups', 'firstsi', 'nsi', 'si', 'groupmaps',)

    def __init__(
            self, *,
            devicespec: Optional[int] = None,
            recomputeactions: Optional[bool] = None,
            truncatesi: Optional[bool] = None,
            groups: Optional[int] = None,
            firstsi: Optional[int] = None,
            nsi: Optional[int] = None,
            si: Optional[Sequence[int]] = None,
            groupmaps: Optional[Sequence[int]] = None,
    ) -> None:
        self.devicespec = devicespec
        self.recomputeactions = recomputeactions
        self.truncatesi = truncatesi
        self.groups = groups
        self.firstsi = firstsi
        self.nsi = nsi
        self.si = si
        self.groupmaps = groupmaps

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceSpec': self.devicespec,
            'recomputeActions': self.recomputeactions,
            'truncateSI': self.truncatesi,
            'groups': self.groups,
            'firstSI': self.firstsi,
            'nSI': self.nsi,
            'si': self.si,
            'groupMaps': self.groupmaps,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetCompatMapRequest':
        return SetCompatMapRequest(**SetCompatMapRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetCompatMapRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, bool, bool, int, int, int, Sequence[int], Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetCompatMapRequest.lib = library.xkb_setcompatmap
        SetCompatMapRequest.lib.restype = ctypes.c_uint32
        SetCompatMapRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint8, ctypes.c_int8, ctypes.c_int8, ctypes.c_uint8, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint8 * 2, ctypes.c_void_p, ctypes.c_void_p)


class SetCompatMapRequestCType(ctypes.Structure):
    """xkb SetCompatMap"""
    _fields_ = [
        ("deviceSpec", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8),
        ("recomputeActions", ctypes.c_int8),
        ("truncateSI", ctypes.c_int8),
        ("groups", ctypes.c_uint8),
        ("firstSI", ctypes.c_uint16),
        ("nSI", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


GetIndicatorStateRequestCookie = NewType('GetIndicatorStateRequestCookie', ctypes.c_uint32)


GetIndicatorStateRequestPacket = DataPacket((
    ('deviceSpec', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(2)),
))


class GetIndicatorStateRequest:
    OPCODE = 12

    __slots__ = ('devicespec',)

    def __init__(
            self, *,
            devicespec: Optional[int] = None,
    ) -> None:
        self.devicespec = devicespec

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceSpec': self.devicespec,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetIndicatorStateRequest':
        return GetIndicatorStateRequest(**GetIndicatorStateRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetIndicatorStateRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetIndicatorStateRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetIndicatorStateRequest.lib = library.xkb_getindicatorstate
        GetIndicatorStateRequest.lib.restype = GetIndicatorStateRequestCookie
        GetIndicatorStateRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint8 * 2)


class GetIndicatorStateRequestCType(ctypes.Structure):
    """xkb GetIndicatorState"""
    _fields_ = [
        ("deviceSpec", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 2),
    ]


GetIndicatorStateReplyReplyPacket = DataPacket((
    ('deviceID', FixedDataPacketField(MARKER_UINT8)),
    ('state', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(20)),
))


class GetIndicatorStateReplyReply:
    __slots__ = ('deviceid', 'state',)

    def __init__(
            self, *,
            deviceid: Optional[int] = None,
            state: Optional[int] = None,
    ) -> None:
        self.deviceid = deviceid
        self.state = state

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceID': self.deviceid,
            'state': self.state,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetIndicatorStateReplyReply':
        return GetIndicatorStateReplyReply(**GetIndicatorStateReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetIndicatorStateReplyReplyPacket.pack(**self.as_dict())


class GetIndicatorStateReplyReplyCType(ctypes.Structure):
    """xkb GetIndicatorState_reply"""
    _fields_ = [
        ("deviceID", ctypes.c_uint8),
        ("state", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 20),
    ]


GetIndicatorMapRequestCookie = NewType('GetIndicatorMapRequestCookie', ctypes.c_uint32)


GetIndicatorMapRequestPacket = DataPacket((
    ('deviceSpec', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(2)),
    ('which', FixedDataPacketField(MARKER_UINT32)),
))


class GetIndicatorMapRequest:
    OPCODE = 13

    __slots__ = ('devicespec', 'which',)

    def __init__(
            self, *,
            devicespec: Optional[int] = None,
            which: Optional[int] = None,
    ) -> None:
        self.devicespec = devicespec
        self.which = which

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceSpec': self.devicespec,
            'which': self.which,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetIndicatorMapRequest':
        return GetIndicatorMapRequest(**GetIndicatorMapRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetIndicatorMapRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], GetIndicatorMapRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetIndicatorMapRequest.lib = library.xkb_getindicatormap
        GetIndicatorMapRequest.lib.restype = GetIndicatorMapRequestCookie
        GetIndicatorMapRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint8 * 2, ctypes.c_uint32)


class GetIndicatorMapRequestCType(ctypes.Structure):
    """xkb GetIndicatorMap"""
    _fields_ = [
        ("deviceSpec", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 2),
        ("which", ctypes.c_uint32),
    ]


GetIndicatorMapReplyReplyPacket = DataPacket((
    ('deviceID', FixedDataPacketField(MARKER_UINT8)),
    ('which', FixedDataPacketField(MARKER_UINT32)),
    ('realIndicators', FixedDataPacketField(MARKER_UINT32)),
    ('nIndicators', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(15)),
    ('maps', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['which'], 0)),
))


class GetIndicatorMapReplyReply:
    __slots__ = ('deviceid', 'which', 'realindicators', 'nindicators', 'maps',)

    def __init__(
            self, *,
            deviceid: Optional[int] = None,
            which: Optional[int] = None,
            realindicators: Optional[int] = None,
            nindicators: Optional[int] = None,
            maps: Optional[Sequence[int]] = None,
    ) -> None:
        self.deviceid = deviceid
        self.which = which
        self.realindicators = realindicators
        self.nindicators = nindicators
        self.maps = maps

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceID': self.deviceid,
            'which': self.which,
            'realIndicators': self.realindicators,
            'nIndicators': self.nindicators,
            'maps': self.maps,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetIndicatorMapReplyReply':
        return GetIndicatorMapReplyReply(**GetIndicatorMapReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetIndicatorMapReplyReplyPacket.pack(**self.as_dict())


class GetIndicatorMapReplyReplyCType(ctypes.Structure):
    """xkb GetIndicatorMap_reply"""
    _fields_ = [
        ("deviceID", ctypes.c_uint8),
        ("which", ctypes.c_uint32),
        ("realIndicators", ctypes.c_uint32),
        ("nIndicators", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 15),
        ("var_data", ctypes.c_void_p),
    ]


SetIndicatorMapRequestPacket = DataPacket((
    ('deviceSpec', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(2)),
    ('which', FixedDataPacketField(MARKER_UINT32)),
    ('maps', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['which'], 0)),
))


class SetIndicatorMapRequest:
    OPCODE = 14

    __slots__ = ('devicespec', 'which', 'maps',)

    def __init__(
            self, *,
            devicespec: Optional[int] = None,
            which: Optional[int] = None,
            maps: Optional[Sequence[int]] = None,
    ) -> None:
        self.devicespec = devicespec
        self.which = which
        self.maps = maps

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceSpec': self.devicespec,
            'which': self.which,
            'maps': self.maps,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetIndicatorMapRequest':
        return SetIndicatorMapRequest(**SetIndicatorMapRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetIndicatorMapRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetIndicatorMapRequest.lib = library.xkb_setindicatormap
        SetIndicatorMapRequest.lib.restype = ctypes.c_uint32
        SetIndicatorMapRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint8 * 2, ctypes.c_uint32, ctypes.c_void_p)


class SetIndicatorMapRequestCType(ctypes.Structure):
    """xkb SetIndicatorMap"""
    _fields_ = [
        ("deviceSpec", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 2),
        ("which", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


GetNamedIndicatorRequestCookie = NewType('GetNamedIndicatorRequestCookie', ctypes.c_uint32)


GetNamedIndicatorRequestPacket = DataPacket((
    ('deviceSpec', FixedDataPacketField(MARKER_UINT32)),
    ('ledClass', FixedDataPacketField(MARKER_UINT32)),
    ('ledID', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(2)),
    ('indicator', FixedDataPacketField(MARKER_UINT32)),
))


class GetNamedIndicatorRequest:
    OPCODE = 15

    __slots__ = ('devicespec', 'ledclass', 'ledid', 'indicator',)

    def __init__(
            self, *,
            devicespec: Optional[int] = None,
            ledclass: Optional[int] = None,
            ledid: Optional[int] = None,
            indicator: Optional[int] = None,
    ) -> None:
        self.devicespec = devicespec
        self.ledclass = ledclass
        self.ledid = ledid
        self.indicator = indicator

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceSpec': self.devicespec,
            'ledClass': self.ledclass,
            'ledID': self.ledid,
            'indicator': self.indicator,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetNamedIndicatorRequest':
        return GetNamedIndicatorRequest(**GetNamedIndicatorRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetNamedIndicatorRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int], GetNamedIndicatorRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetNamedIndicatorRequest.lib = library.xkb_getnamedindicator
        GetNamedIndicatorRequest.lib.restype = GetNamedIndicatorRequestCookie
        GetNamedIndicatorRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8 * 2, ctypes.c_uint32)


class GetNamedIndicatorRequestCType(ctypes.Structure):
    """xkb GetNamedIndicator"""
    _fields_ = [
        ("deviceSpec", ctypes.c_uint32),
        ("ledClass", ctypes.c_uint32),
        ("ledID", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 2),
        ("indicator", ctypes.c_uint32),
    ]


GetNamedIndicatorReplyReplyPacket = DataPacket((
    ('deviceID', FixedDataPacketField(MARKER_UINT8)),
    ('indicator', FixedDataPacketField(MARKER_UINT32)),
    ('found', FixedDataPacketField(MARKER_UINT8)),
    ('on', FixedDataPacketField(MARKER_UINT8)),
    ('realIndicator', FixedDataPacketField(MARKER_UINT8)),
    ('ndx', FixedDataPacketField(MARKER_UINT8)),
    ('map_flags', FixedDataPacketField(MARKER_UINT8)),
    ('map_whichGroups', FixedDataPacketField(MARKER_UINT8)),
    ('map_groups', FixedDataPacketField(MARKER_UINT8)),
    ('map_whichMods', FixedDataPacketField(MARKER_UINT8)),
    ('map_mods', FixedDataPacketField(MARKER_UINT8)),
    ('map_realMods', FixedDataPacketField(MARKER_UINT8)),
    ('map_vmod', FixedDataPacketField(MARKER_UINT16)),
    ('map_ctrls', FixedDataPacketField(MARKER_UINT32)),
    ('supported', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class GetNamedIndicatorReplyReply:
    __slots__ = ('deviceid', 'indicator', 'found', 'on', 'realindicator', 'ndx', 'map_flags', 'map_whichgroups', 'map_groups', 'map_whichmods', 'map_mods', 'map_realmods', 'map_vmod', 'map_ctrls', 'supported',)

    def __init__(
            self, *,
            deviceid: Optional[int] = None,
            indicator: Optional[int] = None,
            found: Optional[bool] = None,
            on: Optional[bool] = None,
            realindicator: Optional[bool] = None,
            ndx: Optional[int] = None,
            map_flags: Optional[int] = None,
            map_whichgroups: Optional[int] = None,
            map_groups: Optional[int] = None,
            map_whichmods: Optional[int] = None,
            map_mods: Optional[int] = None,
            map_realmods: Optional[int] = None,
            map_vmod: Optional[int] = None,
            map_ctrls: Optional[int] = None,
            supported: Optional[bool] = None,
    ) -> None:
        self.deviceid = deviceid
        self.indicator = indicator
        self.found = found
        self.on = on
        self.realindicator = realindicator
        self.ndx = ndx
        self.map_flags = map_flags
        self.map_whichgroups = map_whichgroups
        self.map_groups = map_groups
        self.map_whichmods = map_whichmods
        self.map_mods = map_mods
        self.map_realmods = map_realmods
        self.map_vmod = map_vmod
        self.map_ctrls = map_ctrls
        self.supported = supported

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceID': self.deviceid,
            'indicator': self.indicator,
            'found': self.found,
            'on': self.on,
            'realIndicator': self.realindicator,
            'ndx': self.ndx,
            'map_flags': self.map_flags,
            'map_whichGroups': self.map_whichgroups,
            'map_groups': self.map_groups,
            'map_whichMods': self.map_whichmods,
            'map_mods': self.map_mods,
            'map_realMods': self.map_realmods,
            'map_vmod': self.map_vmod,
            'map_ctrls': self.map_ctrls,
            'supported': self.supported,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetNamedIndicatorReplyReply':
        return GetNamedIndicatorReplyReply(**GetNamedIndicatorReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetNamedIndicatorReplyReplyPacket.pack(**self.as_dict())


class GetNamedIndicatorReplyReplyCType(ctypes.Structure):
    """xkb GetNamedIndicator_reply"""
    _fields_ = [
        ("deviceID", ctypes.c_uint8),
        ("indicator", ctypes.c_uint32),
        ("found", ctypes.c_int8),
        ("on", ctypes.c_int8),
        ("realIndicator", ctypes.c_int8),
        ("ndx", ctypes.c_uint8),
        ("map_flags", ctypes.c_uint8),
        ("map_whichGroups", ctypes.c_uint8),
        ("map_groups", ctypes.c_uint8),
        ("map_whichMods", ctypes.c_uint8),
        ("map_mods", ctypes.c_uint8),
        ("map_realMods", ctypes.c_uint8),
        ("map_vmod", ctypes.c_uint16),
        ("map_ctrls", ctypes.c_uint32),
        ("supported", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


SetNamedIndicatorRequestPacket = DataPacket((
    ('deviceSpec', FixedDataPacketField(MARKER_UINT32)),
    ('ledClass', FixedDataPacketField(MARKER_UINT32)),
    ('ledID', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(2)),
    ('indicator', FixedDataPacketField(MARKER_UINT32)),
    ('setState', FixedDataPacketField(MARKER_UINT8)),
    ('on', FixedDataPacketField(MARKER_UINT8)),
    ('setMap', FixedDataPacketField(MARKER_UINT8)),
    ('createMap', FixedDataPacketField(MARKER_UINT8)),
    ('pad1', FixedPadDataPacketField(1)),
    ('map_flags', FixedDataPacketField(MARKER_UINT8)),
    ('map_whichGroups', FixedDataPacketField(MARKER_UINT8)),
    ('map_groups', FixedDataPacketField(MARKER_UINT8)),
    ('map_whichMods', FixedDataPacketField(MARKER_UINT8)),
    ('map_realMods', FixedDataPacketField(MARKER_UINT8)),
    ('map_vmods', FixedDataPacketField(MARKER_UINT16)),
    ('map_ctrls', FixedDataPacketField(MARKER_UINT32)),
))


class SetNamedIndicatorRequest:
    OPCODE = 16

    __slots__ = ('devicespec', 'ledclass', 'ledid', 'indicator', 'setstate', 'on', 'setmap', 'createmap', 'map_flags', 'map_whichgroups', 'map_groups', 'map_whichmods', 'map_realmods', 'map_vmods', 'map_ctrls',)

    def __init__(
            self, *,
            devicespec: Optional[int] = None,
            ledclass: Optional[int] = None,
            ledid: Optional[int] = None,
            indicator: Optional[int] = None,
            setstate: Optional[bool] = None,
            on: Optional[bool] = None,
            setmap: Optional[bool] = None,
            createmap: Optional[bool] = None,
            map_flags: Optional[int] = None,
            map_whichgroups: Optional[int] = None,
            map_groups: Optional[int] = None,
            map_whichmods: Optional[int] = None,
            map_realmods: Optional[int] = None,
            map_vmods: Optional[int] = None,
            map_ctrls: Optional[int] = None,
    ) -> None:
        self.devicespec = devicespec
        self.ledclass = ledclass
        self.ledid = ledid
        self.indicator = indicator
        self.setstate = setstate
        self.on = on
        self.setmap = setmap
        self.createmap = createmap
        self.map_flags = map_flags
        self.map_whichgroups = map_whichgroups
        self.map_groups = map_groups
        self.map_whichmods = map_whichmods
        self.map_realmods = map_realmods
        self.map_vmods = map_vmods
        self.map_ctrls = map_ctrls

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceSpec': self.devicespec,
            'ledClass': self.ledclass,
            'ledID': self.ledid,
            'indicator': self.indicator,
            'setState': self.setstate,
            'on': self.on,
            'setMap': self.setmap,
            'createMap': self.createmap,
            'map_flags': self.map_flags,
            'map_whichGroups': self.map_whichgroups,
            'map_groups': self.map_groups,
            'map_whichMods': self.map_whichmods,
            'map_realMods': self.map_realmods,
            'map_vmods': self.map_vmods,
            'map_ctrls': self.map_ctrls,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetNamedIndicatorRequest':
        return SetNamedIndicatorRequest(**SetNamedIndicatorRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetNamedIndicatorRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, bool, bool, bool, bool, int, int, int, int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetNamedIndicatorRequest.lib = library.xkb_setnamedindicator
        SetNamedIndicatorRequest.lib.restype = ctypes.c_uint32
        SetNamedIndicatorRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8 * 2, ctypes.c_uint32, ctypes.c_int8, ctypes.c_int8, ctypes.c_int8, ctypes.c_int8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint16, ctypes.c_uint32)


class SetNamedIndicatorRequestCType(ctypes.Structure):
    """xkb SetNamedIndicator"""
    _fields_ = [
        ("deviceSpec", ctypes.c_uint32),
        ("ledClass", ctypes.c_uint32),
        ("ledID", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 2),
        ("indicator", ctypes.c_uint32),
        ("setState", ctypes.c_int8),
        ("on", ctypes.c_int8),
        ("setMap", ctypes.c_int8),
        ("createMap", ctypes.c_int8),
        ("pad1", ctypes.c_uint8),
        ("map_flags", ctypes.c_uint8),
        ("map_whichGroups", ctypes.c_uint8),
        ("map_groups", ctypes.c_uint8),
        ("map_whichMods", ctypes.c_uint8),
        ("map_realMods", ctypes.c_uint8),
        ("map_vmods", ctypes.c_uint16),
        ("map_ctrls", ctypes.c_uint32),
    ]


GetNamesRequestCookie = NewType('GetNamesRequestCookie', ctypes.c_uint32)


GetNamesRequestPacket = DataPacket((
    ('deviceSpec', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(2)),
    ('which', FixedDataPacketField(MARKER_UINT32)),
))


class GetNamesRequest:
    OPCODE = 17

    __slots__ = ('devicespec', 'which',)

    def __init__(
            self, *,
            devicespec: Optional[int] = None,
            which: Optional[int] = None,
    ) -> None:
        self.devicespec = devicespec
        self.which = which

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceSpec': self.devicespec,
            'which': self.which,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetNamesRequest':
        return GetNamesRequest(**GetNamesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetNamesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], GetNamesRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetNamesRequest.lib = library.xkb_getnames
        GetNamesRequest.lib.restype = GetNamesRequestCookie
        GetNamesRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint8 * 2, ctypes.c_uint32)


class GetNamesRequestCType(ctypes.Structure):
    """xkb GetNames"""
    _fields_ = [
        ("deviceSpec", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 2),
        ("which", ctypes.c_uint32),
    ]


GetNamesReplyReplyPacket = DataPacket((
    ('deviceID', FixedDataPacketField(MARKER_UINT8)),
    ('which', FixedDataPacketField(MARKER_UINT32)),
    ('minKeyCode', FixedDataPacketField(MARKER_UINT32)),
    ('maxKeyCode', FixedDataPacketField(MARKER_UINT32)),
    ('nTypes', FixedDataPacketField(MARKER_UINT8)),
    ('groupNames', FixedDataPacketField(MARKER_UINT8)),
    ('virtualMods', FixedDataPacketField(MARKER_UINT16)),
    ('firstKey', FixedDataPacketField(MARKER_UINT32)),
    ('nKeys', FixedDataPacketField(MARKER_UINT8)),
    ('indicators', FixedDataPacketField(MARKER_UINT32)),
    ('nRadioGroups', FixedDataPacketField(MARKER_UINT8)),
    ('nKeyAliases', FixedDataPacketField(MARKER_UINT8)),
    ('nKTLevels', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(4)),
    ('valueList', BitDataPacketField(lambda d, c: d['which'], {
        NameDetailValues.KEYCODES: FixedDataPacketField(MARKER_UINT32),
        NameDetailValues.GEOMETRY: FixedDataPacketField(MARKER_UINT32),
        NameDetailValues.SYMBOLS: FixedDataPacketField(MARKER_UINT32),
        NameDetailValues.PHYS_SYMBOLS: FixedDataPacketField(MARKER_UINT32),
        NameDetailValues.TYPES: FixedDataPacketField(MARKER_UINT32),
        NameDetailValues.COMPAT: FixedDataPacketField(MARKER_UINT32),
        NameDetailValues.KEY_TYPE_NAMES: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nTypes'], 0),
        NameDetailValues.KTLEVEL_NAMES: StructureDataPacketField((
            ('nLevelsPerType', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: d['nTypes'], 0)),
            ('pad0', AlignedPadDataPacketField(4)),
            ('ktLevelNames', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: sum([None for d1 in d['nLevelsPerType']]), 0)),
        )),
        NameDetailValues.INDICATOR_NAMES: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['indicators'], 0),
        NameDetailValues.VIRTUAL_MOD_NAMES: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['virtualMods'], 0),
        NameDetailValues.GROUP_NAMES: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['groupNames'], 0),
        NameDetailValues.KEY_NAMES: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nKeys'], 0),
        NameDetailValues.KEY_ALIASES: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nKeyAliases'], 0),
        NameDetailValues.RGNAMES: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nRadioGroups'], 0),
    }, 0)),
))


class GetNamesReplyReply:
    __slots__ = ('deviceid', 'which', 'minkeycode', 'maxkeycode', 'ntypes', 'groupnames', 'virtualmods', 'firstkey', 'nkeys', 'indicators', 'nradiogroups', 'nkeyaliases', 'nktlevels', 'valuelist',)

    def __init__(
            self, *,
            deviceid: Optional[int] = None,
            which: Optional[int] = None,
            minkeycode: Optional[int] = None,
            maxkeycode: Optional[int] = None,
            ntypes: Optional[int] = None,
            groupnames: Optional[int] = None,
            virtualmods: Optional[int] = None,
            firstkey: Optional[int] = None,
            nkeys: Optional[int] = None,
            indicators: Optional[int] = None,
            nradiogroups: Optional[int] = None,
            nkeyaliases: Optional[int] = None,
            nktlevels: Optional[int] = None,
            valuelist: Optional[Mapping[str, NameDetailValues]] = None,
    ) -> None:
        self.deviceid = deviceid
        self.which = which
        self.minkeycode = minkeycode
        self.maxkeycode = maxkeycode
        self.ntypes = ntypes
        self.groupnames = groupnames
        self.virtualmods = virtualmods
        self.firstkey = firstkey
        self.nkeys = nkeys
        self.indicators = indicators
        self.nradiogroups = nradiogroups
        self.nkeyaliases = nkeyaliases
        self.nktlevels = nktlevels
        self.valuelist = valuelist

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceID': self.deviceid,
            'which': self.which,
            'minKeyCode': self.minkeycode,
            'maxKeyCode': self.maxkeycode,
            'nTypes': self.ntypes,
            'groupNames': self.groupnames,
            'virtualMods': self.virtualmods,
            'firstKey': self.firstkey,
            'nKeys': self.nkeys,
            'indicators': self.indicators,
            'nRadioGroups': self.nradiogroups,
            'nKeyAliases': self.nkeyaliases,
            'nKTLevels': self.nktlevels,
            'valueList': self.valuelist,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetNamesReplyReply':
        return GetNamesReplyReply(**GetNamesReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetNamesReplyReplyPacket.pack(**self.as_dict())


class GetNamesReplyReplyCType(ctypes.Structure):
    """xkb GetNames_reply"""
    _fields_ = [
        ("deviceID", ctypes.c_uint8),
        ("which", ctypes.c_uint32),
        ("minKeyCode", ctypes.c_uint32),
        ("maxKeyCode", ctypes.c_uint32),
        ("nTypes", ctypes.c_uint8),
        ("groupNames", ctypes.c_uint8),
        ("virtualMods", ctypes.c_uint16),
        ("firstKey", ctypes.c_uint32),
        ("nKeys", ctypes.c_uint8),
        ("indicators", ctypes.c_uint32),
        ("nRadioGroups", ctypes.c_uint8),
        ("nKeyAliases", ctypes.c_uint8),
        ("nKTLevels", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 4),
        ("var_data", ctypes.c_void_p),
    ]


SetNamesRequestPacket = DataPacket((
    ('deviceSpec', FixedDataPacketField(MARKER_UINT32)),
    ('virtualMods', FixedDataPacketField(MARKER_UINT16)),
    ('which', FixedDataPacketField(MARKER_UINT32)),
    ('firstType', FixedDataPacketField(MARKER_UINT8)),
    ('nTypes', FixedDataPacketField(MARKER_UINT8)),
    ('firstKTLevelt', FixedDataPacketField(MARKER_UINT8)),
    ('nKTLevels', FixedDataPacketField(MARKER_UINT8)),
    ('indicators', FixedDataPacketField(MARKER_UINT32)),
    ('groupNames', FixedDataPacketField(MARKER_UINT8)),
    ('nRadioGroups', FixedDataPacketField(MARKER_UINT8)),
    ('firstKey', FixedDataPacketField(MARKER_UINT32)),
    ('nKeys', FixedDataPacketField(MARKER_UINT8)),
    ('nKeyAliases', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('totalKTLevelNames', FixedDataPacketField(MARKER_UINT16)),
    ('values', BitDataPacketField(lambda d, c: d['which'], {
        NameDetailValues.KEYCODES: FixedDataPacketField(MARKER_UINT32),
        NameDetailValues.GEOMETRY: FixedDataPacketField(MARKER_UINT32),
        NameDetailValues.SYMBOLS: FixedDataPacketField(MARKER_UINT32),
        NameDetailValues.PHYS_SYMBOLS: FixedDataPacketField(MARKER_UINT32),
        NameDetailValues.TYPES: FixedDataPacketField(MARKER_UINT32),
        NameDetailValues.COMPAT: FixedDataPacketField(MARKER_UINT32),
        NameDetailValues.KEY_TYPE_NAMES: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nTypes'], 0),
        NameDetailValues.KTLEVEL_NAMES: StructureDataPacketField((
            ('nLevelsPerType', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: d['nTypes'], 0)),
            ('pad0', AlignedPadDataPacketField(4)),
            ('ktLevelNames', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: sum([None for d1 in d['nLevelsPerType']]), 0)),
        )),
        NameDetailValues.INDICATOR_NAMES: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['indicators'], 0),
        NameDetailValues.VIRTUAL_MOD_NAMES: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['virtualMods'], 0),
        NameDetailValues.GROUP_NAMES: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['groupNames'], 0),
        NameDetailValues.KEY_NAMES: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nKeys'], 0),
        NameDetailValues.KEY_ALIASES: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nKeyAliases'], 0),
        NameDetailValues.RGNAMES: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nRadioGroups'], 0),
    }, 0)),
))


class SetNamesRequest:
    OPCODE = 18

    __slots__ = ('devicespec', 'virtualmods', 'which', 'firsttype', 'ntypes', 'firstktlevelt', 'nktlevels', 'indicators', 'groupnames', 'nradiogroups', 'firstkey', 'nkeys', 'nkeyaliases', 'totalktlevelnames', 'values',)

    def __init__(
            self, *,
            devicespec: Optional[int] = None,
            virtualmods: Optional[int] = None,
            which: Optional[int] = None,
            firsttype: Optional[int] = None,
            ntypes: Optional[int] = None,
            firstktlevelt: Optional[int] = None,
            nktlevels: Optional[int] = None,
            indicators: Optional[int] = None,
            groupnames: Optional[int] = None,
            nradiogroups: Optional[int] = None,
            firstkey: Optional[int] = None,
            nkeys: Optional[int] = None,
            nkeyaliases: Optional[int] = None,
            totalktlevelnames: Optional[int] = None,
            values: Optional[Mapping[str, NameDetailValues]] = None,
    ) -> None:
        self.devicespec = devicespec
        self.virtualmods = virtualmods
        self.which = which
        self.firsttype = firsttype
        self.ntypes = ntypes
        self.firstktlevelt = firstktlevelt
        self.nktlevels = nktlevels
        self.indicators = indicators
        self.groupnames = groupnames
        self.nradiogroups = nradiogroups
        self.firstkey = firstkey
        self.nkeys = nkeys
        self.nkeyaliases = nkeyaliases
        self.totalktlevelnames = totalktlevelnames
        self.values = values

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceSpec': self.devicespec,
            'virtualMods': self.virtualmods,
            'which': self.which,
            'firstType': self.firsttype,
            'nTypes': self.ntypes,
            'firstKTLevelt': self.firstktlevelt,
            'nKTLevels': self.nktlevels,
            'indicators': self.indicators,
            'groupNames': self.groupnames,
            'nRadioGroups': self.nradiogroups,
            'firstKey': self.firstkey,
            'nKeys': self.nkeys,
            'nKeyAliases': self.nkeyaliases,
            'totalKTLevelNames': self.totalktlevelnames,
            'values': self.values,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetNamesRequest':
        return SetNamesRequest(**SetNamesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetNamesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, int, int, int, int, int, int, int, Mapping[str, NameDetailValues]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetNamesRequest.lib = library.xkb_setnames
        SetNamesRequest.lib.restype = ctypes.c_uint32
        SetNamesRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint16, ctypes.c_void_p)


class SetNamesRequestCType(ctypes.Structure):
    """xkb SetNames"""
    _fields_ = [
        ("deviceSpec", ctypes.c_uint32),
        ("virtualMods", ctypes.c_uint16),
        ("which", ctypes.c_uint32),
        ("firstType", ctypes.c_uint8),
        ("nTypes", ctypes.c_uint8),
        ("firstKTLevelt", ctypes.c_uint8),
        ("nKTLevels", ctypes.c_uint8),
        ("indicators", ctypes.c_uint32),
        ("groupNames", ctypes.c_uint8),
        ("nRadioGroups", ctypes.c_uint8),
        ("firstKey", ctypes.c_uint32),
        ("nKeys", ctypes.c_uint8),
        ("nKeyAliases", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
        ("totalKTLevelNames", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


PerClientFlagsRequestCookie = NewType('PerClientFlagsRequestCookie', ctypes.c_uint32)


PerClientFlagsRequestPacket = DataPacket((
    ('deviceSpec', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(2)),
    ('change', FixedDataPacketField(MARKER_UINT32)),
    ('value', FixedDataPacketField(MARKER_UINT32)),
    ('ctrlsToChange', FixedDataPacketField(MARKER_UINT32)),
    ('autoCtrls', FixedDataPacketField(MARKER_UINT32)),
    ('autoCtrlsValues', FixedDataPacketField(MARKER_UINT32)),
))


class PerClientFlagsRequest:
    OPCODE = 21

    __slots__ = ('devicespec', 'change', 'value', 'ctrlstochange', 'autoctrls', 'autoctrlsvalues',)

    def __init__(
            self, *,
            devicespec: Optional[int] = None,
            change: Optional[int] = None,
            value: Optional[int] = None,
            ctrlstochange: Optional[int] = None,
            autoctrls: Optional[int] = None,
            autoctrlsvalues: Optional[int] = None,
    ) -> None:
        self.devicespec = devicespec
        self.change = change
        self.value = value
        self.ctrlstochange = ctrlstochange
        self.autoctrls = autoctrls
        self.autoctrlsvalues = autoctrlsvalues

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceSpec': self.devicespec,
            'change': self.change,
            'value': self.value,
            'ctrlsToChange': self.ctrlstochange,
            'autoCtrls': self.autoctrls,
            'autoCtrlsValues': self.autoctrlsvalues,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PerClientFlagsRequest':
        return PerClientFlagsRequest(**PerClientFlagsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PerClientFlagsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int], PerClientFlagsRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PerClientFlagsRequest.lib = library.xkb_perclientflags
        PerClientFlagsRequest.lib.restype = PerClientFlagsRequestCookie
        PerClientFlagsRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint8 * 2, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class PerClientFlagsRequestCType(ctypes.Structure):
    """xkb PerClientFlags"""
    _fields_ = [
        ("deviceSpec", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 2),
        ("change", ctypes.c_uint32),
        ("value", ctypes.c_uint32),
        ("ctrlsToChange", ctypes.c_uint32),
        ("autoCtrls", ctypes.c_uint32),
        ("autoCtrlsValues", ctypes.c_uint32),
    ]


PerClientFlagsReplyReplyPacket = DataPacket((
    ('deviceID', FixedDataPacketField(MARKER_UINT8)),
    ('supported', FixedDataPacketField(MARKER_UINT32)),
    ('value', FixedDataPacketField(MARKER_UINT32)),
    ('autoCtrls', FixedDataPacketField(MARKER_UINT32)),
    ('autoCtrlsValues', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(8)),
))


class PerClientFlagsReplyReply:
    __slots__ = ('deviceid', 'supported', 'value', 'autoctrls', 'autoctrlsvalues',)

    def __init__(
            self, *,
            deviceid: Optional[int] = None,
            supported: Optional[int] = None,
            value: Optional[int] = None,
            autoctrls: Optional[int] = None,
            autoctrlsvalues: Optional[int] = None,
    ) -> None:
        self.deviceid = deviceid
        self.supported = supported
        self.value = value
        self.autoctrls = autoctrls
        self.autoctrlsvalues = autoctrlsvalues

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceID': self.deviceid,
            'supported': self.supported,
            'value': self.value,
            'autoCtrls': self.autoctrls,
            'autoCtrlsValues': self.autoctrlsvalues,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PerClientFlagsReplyReply':
        return PerClientFlagsReplyReply(**PerClientFlagsReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PerClientFlagsReplyReplyPacket.pack(**self.as_dict())


class PerClientFlagsReplyReplyCType(ctypes.Structure):
    """xkb PerClientFlags_reply"""
    _fields_ = [
        ("deviceID", ctypes.c_uint8),
        ("supported", ctypes.c_uint32),
        ("value", ctypes.c_uint32),
        ("autoCtrls", ctypes.c_uint32),
        ("autoCtrlsValues", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 8),
    ]


ListComponentsRequestCookie = NewType('ListComponentsRequestCookie', ctypes.c_uint32)


ListComponentsRequestPacket = DataPacket((
    ('deviceSpec', FixedDataPacketField(MARKER_UINT32)),
    ('maxNames', FixedDataPacketField(MARKER_UINT16)),
))


class ListComponentsRequest:
    OPCODE = 22

    __slots__ = ('devicespec', 'maxnames',)

    def __init__(
            self, *,
            devicespec: Optional[int] = None,
            maxnames: Optional[int] = None,
    ) -> None:
        self.devicespec = devicespec
        self.maxnames = maxnames

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceSpec': self.devicespec,
            'maxNames': self.maxnames,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ListComponentsRequest':
        return ListComponentsRequest(**ListComponentsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ListComponentsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ListComponentsRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ListComponentsRequest.lib = library.xkb_listcomponents
        ListComponentsRequest.lib.restype = ListComponentsRequestCookie
        ListComponentsRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint16)


class ListComponentsRequestCType(ctypes.Structure):
    """xkb ListComponents"""
    _fields_ = [
        ("deviceSpec", ctypes.c_uint32),
        ("maxNames", ctypes.c_uint16),
    ]


ListComponentsReplyReplyPacket = DataPacket((
    ('deviceID', FixedDataPacketField(MARKER_UINT8)),
    ('nKeymaps', FixedDataPacketField(MARKER_UINT16)),
    ('nKeycodes', FixedDataPacketField(MARKER_UINT16)),
    ('nTypes', FixedDataPacketField(MARKER_UINT16)),
    ('nCompatMaps', FixedDataPacketField(MARKER_UINT16)),
    ('nSymbols', FixedDataPacketField(MARKER_UINT16)),
    ('nGeometries', FixedDataPacketField(MARKER_UINT16)),
    ('extra', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(10)),
    ('keymaps', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nKeymaps'], 0)),
    ('keycodes', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nKeycodes'], 0)),
    ('types', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nTypes'], 0)),
    ('compatMaps', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nCompatMaps'], 0)),
    ('symbols', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nSymbols'], 0)),
    ('geometries', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nGeometries'], 0)),
))


class ListComponentsReplyReply:
    __slots__ = ('deviceid', 'nkeymaps', 'nkeycodes', 'ntypes', 'ncompatmaps', 'nsymbols', 'ngeometries', 'extra', 'keymaps', 'keycodes', 'types', 'compatmaps', 'symbols', 'geometries',)

    def __init__(
            self, *,
            deviceid: Optional[int] = None,
            nkeymaps: Optional[int] = None,
            nkeycodes: Optional[int] = None,
            ntypes: Optional[int] = None,
            ncompatmaps: Optional[int] = None,
            nsymbols: Optional[int] = None,
            ngeometries: Optional[int] = None,
            extra: Optional[int] = None,
            keymaps: Optional[Sequence[int]] = None,
            keycodes: Optional[Sequence[int]] = None,
            types: Optional[Sequence[int]] = None,
            compatmaps: Optional[Sequence[int]] = None,
            symbols: Optional[Sequence[int]] = None,
            geometries: Optional[Sequence[int]] = None,
    ) -> None:
        self.deviceid = deviceid
        self.nkeymaps = nkeymaps
        self.nkeycodes = nkeycodes
        self.ntypes = ntypes
        self.ncompatmaps = ncompatmaps
        self.nsymbols = nsymbols
        self.ngeometries = ngeometries
        self.extra = extra
        self.keymaps = keymaps
        self.keycodes = keycodes
        self.types = types
        self.compatmaps = compatmaps
        self.symbols = symbols
        self.geometries = geometries

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceID': self.deviceid,
            'nKeymaps': self.nkeymaps,
            'nKeycodes': self.nkeycodes,
            'nTypes': self.ntypes,
            'nCompatMaps': self.ncompatmaps,
            'nSymbols': self.nsymbols,
            'nGeometries': self.ngeometries,
            'extra': self.extra,
            'keymaps': self.keymaps,
            'keycodes': self.keycodes,
            'types': self.types,
            'compatMaps': self.compatmaps,
            'symbols': self.symbols,
            'geometries': self.geometries,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ListComponentsReplyReply':
        return ListComponentsReplyReply(**ListComponentsReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ListComponentsReplyReplyPacket.pack(**self.as_dict())


class ListComponentsReplyReplyCType(ctypes.Structure):
    """xkb ListComponents_reply"""
    _fields_ = [
        ("deviceID", ctypes.c_uint8),
        ("nKeymaps", ctypes.c_uint16),
        ("nKeycodes", ctypes.c_uint16),
        ("nTypes", ctypes.c_uint16),
        ("nCompatMaps", ctypes.c_uint16),
        ("nSymbols", ctypes.c_uint16),
        ("nGeometries", ctypes.c_uint16),
        ("extra", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 10),
        ("var_data", ctypes.c_void_p),
    ]


GetKbdByNameRequestCookie = NewType('GetKbdByNameRequestCookie', ctypes.c_uint32)


GetKbdByNameRequestPacket = DataPacket((
    ('deviceSpec', FixedDataPacketField(MARKER_UINT32)),
    ('need', FixedDataPacketField(MARKER_UINT16)),
    ('want', FixedDataPacketField(MARKER_UINT16)),
    ('load', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
))


class GetKbdByNameRequest:
    OPCODE = 23

    __slots__ = ('devicespec', 'need', 'want', 'load',)

    def __init__(
            self, *,
            devicespec: Optional[int] = None,
            need: Optional[int] = None,
            want: Optional[int] = None,
            load: Optional[bool] = None,
    ) -> None:
        self.devicespec = devicespec
        self.need = need
        self.want = want
        self.load = load

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceSpec': self.devicespec,
            'need': self.need,
            'want': self.want,
            'load': self.load,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetKbdByNameRequest':
        return GetKbdByNameRequest(**GetKbdByNameRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetKbdByNameRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, bool], GetKbdByNameRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetKbdByNameRequest.lib = library.xkb_getkbdbyname
        GetKbdByNameRequest.lib.restype = GetKbdByNameRequestCookie
        GetKbdByNameRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_int8, ctypes.c_uint8)


class GetKbdByNameRequestCType(ctypes.Structure):
    """xkb GetKbdByName"""
    _fields_ = [
        ("deviceSpec", ctypes.c_uint32),
        ("need", ctypes.c_uint16),
        ("want", ctypes.c_uint16),
        ("load", ctypes.c_int8),
        ("pad0", ctypes.c_uint8),
    ]


GetKbdByNameReplyReplyPacket = DataPacket((
    ('deviceID', FixedDataPacketField(MARKER_UINT8)),
    ('minKeyCode', FixedDataPacketField(MARKER_UINT32)),
    ('maxKeyCode', FixedDataPacketField(MARKER_UINT32)),
    ('loaded', FixedDataPacketField(MARKER_UINT8)),
    ('newKeyboard', FixedDataPacketField(MARKER_UINT8)),
    ('found', FixedDataPacketField(MARKER_UINT16)),
    ('reported', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(16)),
    ('replies', BitDataPacketField(lambda d, c: d['reported'], {
        GbndetailValues.TYPES: StructureDataPacketField((
            ('getmap_type', FixedDataPacketField(MARKER_UINT8)),
            ('typeDeviceID', FixedDataPacketField(MARKER_UINT8)),
            ('getmap_sequence', FixedDataPacketField(MARKER_UINT16)),
            ('getmap_length', FixedDataPacketField(MARKER_UINT32)),
            ('pad0', FixedPadDataPacketField(2)),
            ('typeMinKeyCode', FixedDataPacketField(MARKER_UINT32)),
            ('typeMaxKeyCode', FixedDataPacketField(MARKER_UINT32)),
            ('present', FixedDataPacketField(MARKER_UINT16)),
            ('firstType', FixedDataPacketField(MARKER_UINT8)),
            ('nTypes', FixedDataPacketField(MARKER_UINT8)),
            ('totalTypes', FixedDataPacketField(MARKER_UINT8)),
            ('firstKeySym', FixedDataPacketField(MARKER_UINT32)),
            ('totalSyms', FixedDataPacketField(MARKER_UINT16)),
            ('nKeySyms', FixedDataPacketField(MARKER_UINT8)),
            ('firstKeyAction', FixedDataPacketField(MARKER_UINT32)),
            ('totalActions', FixedDataPacketField(MARKER_UINT16)),
            ('nKeyActions', FixedDataPacketField(MARKER_UINT8)),
            ('firstKeyBehavior', FixedDataPacketField(MARKER_UINT32)),
            ('nKeyBehaviors', FixedDataPacketField(MARKER_UINT8)),
            ('totalKeyBehaviors', FixedDataPacketField(MARKER_UINT8)),
            ('firstKeyExplicit', FixedDataPacketField(MARKER_UINT32)),
            ('nKeyExplicit', FixedDataPacketField(MARKER_UINT8)),
            ('totalKeyExplicit', FixedDataPacketField(MARKER_UINT8)),
            ('firstModMapKey', FixedDataPacketField(MARKER_UINT32)),
            ('nModMapKeys', FixedDataPacketField(MARKER_UINT8)),
            ('totalModMapKeys', FixedDataPacketField(MARKER_UINT8)),
            ('firstVModMapKey', FixedDataPacketField(MARKER_UINT32)),
            ('nVModMapKeys', FixedDataPacketField(MARKER_UINT8)),
            ('totalVModMapKeys', FixedDataPacketField(MARKER_UINT8)),
            ('pad1', FixedPadDataPacketField(1)),
            ('virtualMods', FixedDataPacketField(MARKER_UINT16)),
            ('map', BitDataPacketField(lambda d, c: d['present'], {
                MapPartValues.KEY_TYPES: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nTypes'], 0),
                MapPartValues.KEY_SYMS: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nKeySyms'], 0),
                MapPartValues.KEY_ACTIONS: StructureDataPacketField((
                    ('acts_rtrn_count', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: d['nKeyActions'], 0)),
                    ('pad0', AlignedPadDataPacketField(4)),
                    ('acts_rtrn_acts', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['totalActions'], 0)),
                )),
                MapPartValues.KEY_BEHAVIORS: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['totalKeyBehaviors'], 0),
                MapPartValues.VIRTUAL_MODS: StructureDataPacketField((
                    ('vmods_rtrn', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: d['virtualMods'], 0)),
                    ('pad0', AlignedPadDataPacketField(4)),
                )),
                MapPartValues.EXPLICIT_COMPONENTS: StructureDataPacketField((
                    ('explicit_rtrn', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['totalKeyExplicit'], 0)),
                    ('pad0', AlignedPadDataPacketField(4)),
                )),
                MapPartValues.MODIFIER_MAP: StructureDataPacketField((
                    ('modmap_rtrn', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['totalModMapKeys'], 0)),
                    ('pad0', AlignedPadDataPacketField(4)),
                )),
                MapPartValues.VIRTUAL_MOD_MAP: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['totalVModMapKeys'], 0),
            }, 0)),
        )),
        GbndetailValues.COMPAT_MAP: StructureDataPacketField((
            ('compatmap_type', FixedDataPacketField(MARKER_UINT8)),
            ('compatDeviceID', FixedDataPacketField(MARKER_UINT8)),
            ('compatmap_sequence', FixedDataPacketField(MARKER_UINT16)),
            ('compatmap_length', FixedDataPacketField(MARKER_UINT32)),
            ('groupsRtrn', FixedDataPacketField(MARKER_UINT8)),
            ('pad0', FixedPadDataPacketField(1)),
            ('firstSIRtrn', FixedDataPacketField(MARKER_UINT16)),
            ('nSIRtrn', FixedDataPacketField(MARKER_UINT16)),
            ('nTotalSI', FixedDataPacketField(MARKER_UINT16)),
            ('pad1', FixedPadDataPacketField(16)),
            ('si_rtrn', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nSIRtrn'], 0)),
            ('group_rtrn', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['groupsRtrn'], 0)),
        )),
        GbndetailValues.INDICATOR_MAPS: StructureDataPacketField((
            ('indicatormap_type', FixedDataPacketField(MARKER_UINT8)),
            ('indicatorDeviceID', FixedDataPacketField(MARKER_UINT8)),
            ('indicatormap_sequence', FixedDataPacketField(MARKER_UINT16)),
            ('indicatormap_length', FixedDataPacketField(MARKER_UINT32)),
            ('which', FixedDataPacketField(MARKER_UINT32)),
            ('realIndicators', FixedDataPacketField(MARKER_UINT32)),
            ('nIndicators', FixedDataPacketField(MARKER_UINT8)),
            ('pad0', FixedPadDataPacketField(15)),
            ('maps', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nIndicators'], 0)),
        )),
        GbndetailValues.KEY_NAMES: StructureDataPacketField((
            ('keyname_type', FixedDataPacketField(MARKER_UINT8)),
            ('keyDeviceID', FixedDataPacketField(MARKER_UINT8)),
            ('keyname_sequence', FixedDataPacketField(MARKER_UINT16)),
            ('keyname_length', FixedDataPacketField(MARKER_UINT32)),
            ('which', FixedDataPacketField(MARKER_UINT32)),
            ('keyMinKeyCode', FixedDataPacketField(MARKER_UINT32)),
            ('keyMaxKeyCode', FixedDataPacketField(MARKER_UINT32)),
            ('nTypes', FixedDataPacketField(MARKER_UINT8)),
            ('groupNames', FixedDataPacketField(MARKER_UINT8)),
            ('virtualMods', FixedDataPacketField(MARKER_UINT16)),
            ('firstKey', FixedDataPacketField(MARKER_UINT32)),
            ('nKeys', FixedDataPacketField(MARKER_UINT8)),
            ('indicators', FixedDataPacketField(MARKER_UINT32)),
            ('nRadioGroups', FixedDataPacketField(MARKER_UINT8)),
            ('nKeyAliases', FixedDataPacketField(MARKER_UINT8)),
            ('nKTLevels', FixedDataPacketField(MARKER_UINT16)),
            ('pad0', FixedPadDataPacketField(4)),
            ('valueList', BitDataPacketField(lambda d, c: d['which'], {
                NameDetailValues.KEYCODES: FixedDataPacketField(MARKER_UINT32),
                NameDetailValues.GEOMETRY: FixedDataPacketField(MARKER_UINT32),
                NameDetailValues.SYMBOLS: FixedDataPacketField(MARKER_UINT32),
                NameDetailValues.PHYS_SYMBOLS: FixedDataPacketField(MARKER_UINT32),
                NameDetailValues.TYPES: FixedDataPacketField(MARKER_UINT32),
                NameDetailValues.COMPAT: FixedDataPacketField(MARKER_UINT32),
                NameDetailValues.KEY_TYPE_NAMES: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nTypes'], 0),
                NameDetailValues.KTLEVEL_NAMES: StructureDataPacketField((
                    ('nLevelsPerType', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: d['nTypes'], 0)),
                    ('pad0', AlignedPadDataPacketField(4)),
                    ('ktLevelNames', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: sum([None for d1 in d['nLevelsPerType']]), 0)),
                )),
                NameDetailValues.INDICATOR_NAMES: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['indicators'], 0),
                NameDetailValues.VIRTUAL_MOD_NAMES: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['virtualMods'], 0),
                NameDetailValues.GROUP_NAMES: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['groupNames'], 0),
                NameDetailValues.KEY_NAMES: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nKeys'], 0),
                NameDetailValues.KEY_ALIASES: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nKeyAliases'], 0),
                NameDetailValues.RGNAMES: SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nRadioGroups'], 0),
            }, 0)),
        )),
        GbndetailValues.GEOMETRY: StructureDataPacketField((
            ('geometry_type', FixedDataPacketField(MARKER_UINT8)),
            ('geometryDeviceID', FixedDataPacketField(MARKER_UINT8)),
            ('geometry_sequence', FixedDataPacketField(MARKER_UINT16)),
            ('geometry_length', FixedDataPacketField(MARKER_UINT32)),
            ('name', FixedDataPacketField(MARKER_UINT32)),
            ('geometryFound', FixedDataPacketField(MARKER_UINT8)),
            ('pad0', FixedPadDataPacketField(1)),
            ('widthMM', FixedDataPacketField(MARKER_UINT16)),
            ('heightMM', FixedDataPacketField(MARKER_UINT16)),
            ('nProperties', FixedDataPacketField(MARKER_UINT16)),
            ('nColors', FixedDataPacketField(MARKER_UINT16)),
            ('nShapes', FixedDataPacketField(MARKER_UINT16)),
            ('nSections', FixedDataPacketField(MARKER_UINT16)),
            ('nDoodads', FixedDataPacketField(MARKER_UINT16)),
            ('nKeyAliases', FixedDataPacketField(MARKER_UINT16)),
            ('baseColorNdx', FixedDataPacketField(MARKER_UINT8)),
            ('labelColorNdx', FixedDataPacketField(MARKER_UINT8)),
            ('labelFont', FixedDataPacketField(MARKER_UINT32)),
        )),
    }, 0)),
))


class GetKbdByNameReplyReply:
    __slots__ = ('deviceid', 'minkeycode', 'maxkeycode', 'loaded', 'newkeyboard', 'found', 'reported', 'replies',)

    def __init__(
            self, *,
            deviceid: Optional[int] = None,
            minkeycode: Optional[int] = None,
            maxkeycode: Optional[int] = None,
            loaded: Optional[bool] = None,
            newkeyboard: Optional[bool] = None,
            found: Optional[int] = None,
            reported: Optional[int] = None,
            replies: Optional[Mapping[str, GbndetailValues]] = None,
    ) -> None:
        self.deviceid = deviceid
        self.minkeycode = minkeycode
        self.maxkeycode = maxkeycode
        self.loaded = loaded
        self.newkeyboard = newkeyboard
        self.found = found
        self.reported = reported
        self.replies = replies

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceID': self.deviceid,
            'minKeyCode': self.minkeycode,
            'maxKeyCode': self.maxkeycode,
            'loaded': self.loaded,
            'newKeyboard': self.newkeyboard,
            'found': self.found,
            'reported': self.reported,
            'replies': self.replies,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetKbdByNameReplyReply':
        return GetKbdByNameReplyReply(**GetKbdByNameReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetKbdByNameReplyReplyPacket.pack(**self.as_dict())


class GetKbdByNameReplyReplyCType(ctypes.Structure):
    """xkb GetKbdByName_reply"""
    _fields_ = [
        ("deviceID", ctypes.c_uint8),
        ("minKeyCode", ctypes.c_uint32),
        ("maxKeyCode", ctypes.c_uint32),
        ("loaded", ctypes.c_int8),
        ("newKeyboard", ctypes.c_int8),
        ("found", ctypes.c_uint16),
        ("reported", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 16),
        ("var_data", ctypes.c_void_p),
    ]


GetDeviceInfoRequestCookie = NewType('GetDeviceInfoRequestCookie', ctypes.c_uint32)


GetDeviceInfoRequestPacket = DataPacket((
    ('deviceSpec', FixedDataPacketField(MARKER_UINT32)),
    ('wanted', FixedDataPacketField(MARKER_UINT16)),
    ('allButtons', FixedDataPacketField(MARKER_UINT8)),
    ('firstButton', FixedDataPacketField(MARKER_UINT8)),
    ('nButtons', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('ledClass', FixedDataPacketField(MARKER_UINT32)),
    ('ledID', FixedDataPacketField(MARKER_UINT32)),
))


class GetDeviceInfoRequest:
    OPCODE = 24

    __slots__ = ('devicespec', 'wanted', 'allbuttons', 'firstbutton', 'nbuttons', 'ledclass', 'ledid',)

    def __init__(
            self, *,
            devicespec: Optional[int] = None,
            wanted: Optional[int] = None,
            allbuttons: Optional[bool] = None,
            firstbutton: Optional[int] = None,
            nbuttons: Optional[int] = None,
            ledclass: Optional[int] = None,
            ledid: Optional[int] = None,
    ) -> None:
        self.devicespec = devicespec
        self.wanted = wanted
        self.allbuttons = allbuttons
        self.firstbutton = firstbutton
        self.nbuttons = nbuttons
        self.ledclass = ledclass
        self.ledid = ledid

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceSpec': self.devicespec,
            'wanted': self.wanted,
            'allButtons': self.allbuttons,
            'firstButton': self.firstbutton,
            'nButtons': self.nbuttons,
            'ledClass': self.ledclass,
            'ledID': self.ledid,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetDeviceInfoRequest':
        return GetDeviceInfoRequest(**GetDeviceInfoRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetDeviceInfoRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, bool, int, int, int, int], GetDeviceInfoRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetDeviceInfoRequest.lib = library.xkb_getdeviceinfo
        GetDeviceInfoRequest.lib.restype = GetDeviceInfoRequestCookie
        GetDeviceInfoRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint16, ctypes.c_int8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32)


class GetDeviceInfoRequestCType(ctypes.Structure):
    """xkb GetDeviceInfo"""
    _fields_ = [
        ("deviceSpec", ctypes.c_uint32),
        ("wanted", ctypes.c_uint16),
        ("allButtons", ctypes.c_int8),
        ("firstButton", ctypes.c_uint8),
        ("nButtons", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
        ("ledClass", ctypes.c_uint32),
        ("ledID", ctypes.c_uint32),
    ]


GetDeviceInfoReplyReplyPacket = DataPacket((
    ('deviceID', FixedDataPacketField(MARKER_UINT8)),
    ('present', FixedDataPacketField(MARKER_UINT16)),
    ('supported', FixedDataPacketField(MARKER_UINT16)),
    ('unsupported', FixedDataPacketField(MARKER_UINT16)),
    ('nDeviceLedFBs', FixedDataPacketField(MARKER_UINT16)),
    ('firstBtnWanted', FixedDataPacketField(MARKER_UINT8)),
    ('nBtnsWanted', FixedDataPacketField(MARKER_UINT8)),
    ('firstBtnRtrn', FixedDataPacketField(MARKER_UINT8)),
    ('nBtnsRtrn', FixedDataPacketField(MARKER_UINT8)),
    ('totalBtns', FixedDataPacketField(MARKER_UINT8)),
    ('hasOwnState', FixedDataPacketField(MARKER_UINT8)),
    ('dfltKbdFB', FixedDataPacketField(MARKER_UINT16)),
    ('dfltLedFB', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
    ('devType', FixedDataPacketField(MARKER_UINT32)),
    ('nameLen', FixedDataPacketField(MARKER_UINT16)),
    ('name', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nameLen'], 0)),
    ('pad1', AlignedPadDataPacketField(4)),
    ('btnActions', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nBtnsRtrn'], 0)),
    ('leds', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nDeviceLedFBs'], 0)),
))


class GetDeviceInfoReplyReply:
    __slots__ = ('deviceid', 'present', 'supported', 'unsupported', 'ndeviceledfbs', 'firstbtnwanted', 'nbtnswanted', 'firstbtnrtrn', 'nbtnsrtrn', 'totalbtns', 'hasownstate', 'dfltkbdfb', 'dfltledfb', 'devtype', 'namelen', 'name', 'btnactions', 'leds',)

    def __init__(
            self, *,
            deviceid: Optional[int] = None,
            present: Optional[int] = None,
            supported: Optional[int] = None,
            unsupported: Optional[int] = None,
            ndeviceledfbs: Optional[int] = None,
            firstbtnwanted: Optional[int] = None,
            nbtnswanted: Optional[int] = None,
            firstbtnrtrn: Optional[int] = None,
            nbtnsrtrn: Optional[int] = None,
            totalbtns: Optional[int] = None,
            hasownstate: Optional[bool] = None,
            dfltkbdfb: Optional[int] = None,
            dfltledfb: Optional[int] = None,
            devtype: Optional[int] = None,
            namelen: Optional[int] = None,
            name: Optional[Sequence[int]] = None,
            btnactions: Optional[Sequence[int]] = None,
            leds: Optional[Sequence[int]] = None,
    ) -> None:
        self.deviceid = deviceid
        self.present = present
        self.supported = supported
        self.unsupported = unsupported
        self.ndeviceledfbs = ndeviceledfbs
        self.firstbtnwanted = firstbtnwanted
        self.nbtnswanted = nbtnswanted
        self.firstbtnrtrn = firstbtnrtrn
        self.nbtnsrtrn = nbtnsrtrn
        self.totalbtns = totalbtns
        self.hasownstate = hasownstate
        self.dfltkbdfb = dfltkbdfb
        self.dfltledfb = dfltledfb
        self.devtype = devtype
        self.namelen = namelen
        self.name = name
        self.btnactions = btnactions
        self.leds = leds

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceID': self.deviceid,
            'present': self.present,
            'supported': self.supported,
            'unsupported': self.unsupported,
            'nDeviceLedFBs': self.ndeviceledfbs,
            'firstBtnWanted': self.firstbtnwanted,
            'nBtnsWanted': self.nbtnswanted,
            'firstBtnRtrn': self.firstbtnrtrn,
            'nBtnsRtrn': self.nbtnsrtrn,
            'totalBtns': self.totalbtns,
            'hasOwnState': self.hasownstate,
            'dfltKbdFB': self.dfltkbdfb,
            'dfltLedFB': self.dfltledfb,
            'devType': self.devtype,
            'nameLen': self.namelen,
            'name': self.name,
            'btnActions': self.btnactions,
            'leds': self.leds,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetDeviceInfoReplyReply':
        return GetDeviceInfoReplyReply(**GetDeviceInfoReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetDeviceInfoReplyReplyPacket.pack(**self.as_dict())


class GetDeviceInfoReplyReplyCType(ctypes.Structure):
    """xkb GetDeviceInfo_reply"""
    _fields_ = [
        ("deviceID", ctypes.c_uint8),
        ("present", ctypes.c_uint16),
        ("supported", ctypes.c_uint16),
        ("unsupported", ctypes.c_uint16),
        ("nDeviceLedFBs", ctypes.c_uint16),
        ("firstBtnWanted", ctypes.c_uint8),
        ("nBtnsWanted", ctypes.c_uint8),
        ("firstBtnRtrn", ctypes.c_uint8),
        ("nBtnsRtrn", ctypes.c_uint8),
        ("totalBtns", ctypes.c_uint8),
        ("hasOwnState", ctypes.c_int8),
        ("dfltKbdFB", ctypes.c_uint16),
        ("dfltLedFB", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
        ("devType", ctypes.c_uint32),
        ("nameLen", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


SetDeviceInfoRequestPacket = DataPacket((
    ('deviceSpec', FixedDataPacketField(MARKER_UINT32)),
    ('firstBtn', FixedDataPacketField(MARKER_UINT8)),
    ('nBtns', FixedDataPacketField(MARKER_UINT8)),
    ('change', FixedDataPacketField(MARKER_UINT16)),
    ('nDeviceLedFBs', FixedDataPacketField(MARKER_UINT16)),
    ('btnActions', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nBtns'], 0)),
    ('leds', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nDeviceLedFBs'], 0)),
))


class SetDeviceInfoRequest:
    OPCODE = 25

    __slots__ = ('devicespec', 'firstbtn', 'nbtns', 'change', 'ndeviceledfbs', 'btnactions', 'leds',)

    def __init__(
            self, *,
            devicespec: Optional[int] = None,
            firstbtn: Optional[int] = None,
            nbtns: Optional[int] = None,
            change: Optional[int] = None,
            ndeviceledfbs: Optional[int] = None,
            btnactions: Optional[Sequence[int]] = None,
            leds: Optional[Sequence[int]] = None,
    ) -> None:
        self.devicespec = devicespec
        self.firstbtn = firstbtn
        self.nbtns = nbtns
        self.change = change
        self.ndeviceledfbs = ndeviceledfbs
        self.btnactions = btnactions
        self.leds = leds

    def as_dict(self) -> Dict[str, Any]:
        return {
            'deviceSpec': self.devicespec,
            'firstBtn': self.firstbtn,
            'nBtns': self.nbtns,
            'change': self.change,
            'nDeviceLedFBs': self.ndeviceledfbs,
            'btnActions': self.btnactions,
            'leds': self.leds,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetDeviceInfoRequest':
        return SetDeviceInfoRequest(**SetDeviceInfoRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetDeviceInfoRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, Sequence[int], Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetDeviceInfoRequest.lib = library.xkb_setdeviceinfo
        SetDeviceInfoRequest.lib.restype = ctypes.c_uint32
        SetDeviceInfoRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_void_p, ctypes.c_void_p)


class SetDeviceInfoRequestCType(ctypes.Structure):
    """xkb SetDeviceInfo"""
    _fields_ = [
        ("deviceSpec", ctypes.c_uint32),
        ("firstBtn", ctypes.c_uint8),
        ("nBtns", ctypes.c_uint8),
        ("change", ctypes.c_uint16),
        ("nDeviceLedFBs", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


SetDebuggingFlagsRequestCookie = NewType('SetDebuggingFlagsRequestCookie', ctypes.c_uint32)


SetDebuggingFlagsRequestPacket = DataPacket((
    ('msgLength', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
    ('affectFlags', FixedDataPacketField(MARKER_UINT32)),
    ('flags', FixedDataPacketField(MARKER_UINT32)),
    ('affectCtrls', FixedDataPacketField(MARKER_UINT32)),
    ('ctrls', FixedDataPacketField(MARKER_UINT32)),
    ('message', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['msgLength'], 0)),
))


class SetDebuggingFlagsRequest:
    OPCODE = 101

    __slots__ = ('msglength', 'affectflags', 'flags', 'affectctrls', 'ctrls', 'message',)

    def __init__(
            self, *,
            msglength: Optional[int] = None,
            affectflags: Optional[int] = None,
            flags: Optional[int] = None,
            affectctrls: Optional[int] = None,
            ctrls: Optional[int] = None,
            message: Optional[Sequence[int]] = None,
    ) -> None:
        self.msglength = msglength
        self.affectflags = affectflags
        self.flags = flags
        self.affectctrls = affectctrls
        self.ctrls = ctrls
        self.message = message

    def as_dict(self) -> Dict[str, Any]:
        return {
            'msgLength': self.msglength,
            'affectFlags': self.affectflags,
            'flags': self.flags,
            'affectCtrls': self.affectctrls,
            'ctrls': self.ctrls,
            'message': self.message,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetDebuggingFlagsRequest':
        return SetDebuggingFlagsRequest(**SetDebuggingFlagsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetDebuggingFlagsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, Sequence[int]], SetDebuggingFlagsRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetDebuggingFlagsRequest.lib = library.xkb_setdebuggingflags
        SetDebuggingFlagsRequest.lib.restype = SetDebuggingFlagsRequestCookie
        SetDebuggingFlagsRequest.lib.argstype = (ctypes.c_uint16, ctypes.c_uint8 * 2, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)


class SetDebuggingFlagsRequestCType(ctypes.Structure):
    """xkb SetDebuggingFlags"""
    _fields_ = [
        ("msgLength", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
        ("affectFlags", ctypes.c_uint32),
        ("flags", ctypes.c_uint32),
        ("affectCtrls", ctypes.c_uint32),
        ("ctrls", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


SetDebuggingFlagsReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('currentFlags', FixedDataPacketField(MARKER_UINT32)),
    ('currentCtrls', FixedDataPacketField(MARKER_UINT32)),
    ('supportedFlags', FixedDataPacketField(MARKER_UINT32)),
    ('supportedCtrls', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(8)),
))


class SetDebuggingFlagsReplyReply:
    __slots__ = ('currentflags', 'currentctrls', 'supportedflags', 'supportedctrls',)

    def __init__(
            self, *,
            currentflags: Optional[int] = None,
            currentctrls: Optional[int] = None,
            supportedflags: Optional[int] = None,
            supportedctrls: Optional[int] = None,
    ) -> None:
        self.currentflags = currentflags
        self.currentctrls = currentctrls
        self.supportedflags = supportedflags
        self.supportedctrls = supportedctrls

    def as_dict(self) -> Dict[str, Any]:
        return {
            'currentFlags': self.currentflags,
            'currentCtrls': self.currentctrls,
            'supportedFlags': self.supportedflags,
            'supportedCtrls': self.supportedctrls,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetDebuggingFlagsReplyReply':
        return SetDebuggingFlagsReplyReply(**SetDebuggingFlagsReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetDebuggingFlagsReplyReplyPacket.pack(**self.as_dict())


class SetDebuggingFlagsReplyReplyCType(ctypes.Structure):
    """xkb SetDebuggingFlags_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("currentFlags", ctypes.c_uint32),
        ("currentCtrls", ctypes.c_uint32),
        ("supportedFlags", ctypes.c_uint32),
        ("supportedCtrls", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 8),
    ]


NewKeyboardNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('xkbType', FixedDataPacketField(MARKER_UINT8)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('deviceID', FixedDataPacketField(MARKER_UINT8)),
    ('oldDeviceID', FixedDataPacketField(MARKER_UINT8)),
    ('minKeyCode', FixedDataPacketField(MARKER_UINT32)),
    ('maxKeyCode', FixedDataPacketField(MARKER_UINT32)),
    ('oldMinKeyCode', FixedDataPacketField(MARKER_UINT32)),
    ('oldMaxKeyCode', FixedDataPacketField(MARKER_UINT32)),
    ('requestMajor', FixedDataPacketField(MARKER_UINT8)),
    ('requestMinor', FixedDataPacketField(MARKER_UINT8)),
    ('changed', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(14)),
))


class NewKeyboardNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'xkbtype', 'time', 'deviceid', 'olddeviceid', 'minkeycode', 'maxkeycode', 'oldminkeycode', 'oldmaxkeycode', 'requestmajor', 'requestminor', 'changed',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            xkbtype: Optional[int] = None,
            time: Optional[int] = None,
            deviceid: Optional[int] = None,
            olddeviceid: Optional[int] = None,
            minkeycode: Optional[int] = None,
            maxkeycode: Optional[int] = None,
            oldminkeycode: Optional[int] = None,
            oldmaxkeycode: Optional[int] = None,
            requestmajor: Optional[int] = None,
            requestminor: Optional[int] = None,
            changed: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.xkbtype = xkbtype
        self.time = time
        self.deviceid = deviceid
        self.olddeviceid = olddeviceid
        self.minkeycode = minkeycode
        self.maxkeycode = maxkeycode
        self.oldminkeycode = oldminkeycode
        self.oldmaxkeycode = oldmaxkeycode
        self.requestmajor = requestmajor
        self.requestminor = requestminor
        self.changed = changed

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'xkbType': self.xkbtype,
            'time': self.time,
            'deviceID': self.deviceid,
            'oldDeviceID': self.olddeviceid,
            'minKeyCode': self.minkeycode,
            'maxKeyCode': self.maxkeycode,
            'oldMinKeyCode': self.oldminkeycode,
            'oldMaxKeyCode': self.oldmaxkeycode,
            'requestMajor': self.requestmajor,
            'requestMinor': self.requestminor,
            'changed': self.changed,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'NewKeyboardNotifyEvent':
        return NewKeyboardNotifyEvent(**NewKeyboardNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return NewKeyboardNotifyEventPacket.pack(**self.as_dict())


class NewKeyboardNotifyEventCType(ctypes.Structure):
    """xkb NewKeyboardNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("xkbType", ctypes.c_uint8),
        ("time", ctypes.c_uint32),
        ("deviceID", ctypes.c_uint8),
        ("oldDeviceID", ctypes.c_uint8),
        ("minKeyCode", ctypes.c_uint32),
        ("maxKeyCode", ctypes.c_uint32),
        ("oldMinKeyCode", ctypes.c_uint32),
        ("oldMaxKeyCode", ctypes.c_uint32),
        ("requestMajor", ctypes.c_uint8),
        ("requestMinor", ctypes.c_uint8),
        ("changed", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 14),
    ]


MapNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('xkbType', FixedDataPacketField(MARKER_UINT8)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('deviceID', FixedDataPacketField(MARKER_UINT8)),
    ('ptrBtnActions', FixedDataPacketField(MARKER_UINT8)),
    ('changed', FixedDataPacketField(MARKER_UINT16)),
    ('minKeyCode', FixedDataPacketField(MARKER_UINT32)),
    ('maxKeyCode', FixedDataPacketField(MARKER_UINT32)),
    ('firstType', FixedDataPacketField(MARKER_UINT8)),
    ('nTypes', FixedDataPacketField(MARKER_UINT8)),
    ('firstKeySym', FixedDataPacketField(MARKER_UINT32)),
    ('nKeySyms', FixedDataPacketField(MARKER_UINT8)),
    ('firstKeyAct', FixedDataPacketField(MARKER_UINT32)),
    ('nKeyActs', FixedDataPacketField(MARKER_UINT8)),
    ('firstKeyBehavior', FixedDataPacketField(MARKER_UINT32)),
    ('nKeyBehavior', FixedDataPacketField(MARKER_UINT8)),
    ('firstKeyExplicit', FixedDataPacketField(MARKER_UINT32)),
    ('nKeyExplicit', FixedDataPacketField(MARKER_UINT8)),
    ('firstModMapKey', FixedDataPacketField(MARKER_UINT32)),
    ('nModMapKeys', FixedDataPacketField(MARKER_UINT8)),
    ('firstVModMapKey', FixedDataPacketField(MARKER_UINT32)),
    ('nVModMapKeys', FixedDataPacketField(MARKER_UINT8)),
    ('virtualMods', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
))


class MapNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'xkbtype', 'time', 'deviceid', 'ptrbtnactions', 'changed', 'minkeycode', 'maxkeycode', 'firsttype', 'ntypes', 'firstkeysym', 'nkeysyms', 'firstkeyact', 'nkeyacts', 'firstkeybehavior', 'nkeybehavior', 'firstkeyexplicit', 'nkeyexplicit', 'firstmodmapkey', 'nmodmapkeys', 'firstvmodmapkey', 'nvmodmapkeys', 'virtualmods',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            xkbtype: Optional[int] = None,
            time: Optional[int] = None,
            deviceid: Optional[int] = None,
            ptrbtnactions: Optional[int] = None,
            changed: Optional[int] = None,
            minkeycode: Optional[int] = None,
            maxkeycode: Optional[int] = None,
            firsttype: Optional[int] = None,
            ntypes: Optional[int] = None,
            firstkeysym: Optional[int] = None,
            nkeysyms: Optional[int] = None,
            firstkeyact: Optional[int] = None,
            nkeyacts: Optional[int] = None,
            firstkeybehavior: Optional[int] = None,
            nkeybehavior: Optional[int] = None,
            firstkeyexplicit: Optional[int] = None,
            nkeyexplicit: Optional[int] = None,
            firstmodmapkey: Optional[int] = None,
            nmodmapkeys: Optional[int] = None,
            firstvmodmapkey: Optional[int] = None,
            nvmodmapkeys: Optional[int] = None,
            virtualmods: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.xkbtype = xkbtype
        self.time = time
        self.deviceid = deviceid
        self.ptrbtnactions = ptrbtnactions
        self.changed = changed
        self.minkeycode = minkeycode
        self.maxkeycode = maxkeycode
        self.firsttype = firsttype
        self.ntypes = ntypes
        self.firstkeysym = firstkeysym
        self.nkeysyms = nkeysyms
        self.firstkeyact = firstkeyact
        self.nkeyacts = nkeyacts
        self.firstkeybehavior = firstkeybehavior
        self.nkeybehavior = nkeybehavior
        self.firstkeyexplicit = firstkeyexplicit
        self.nkeyexplicit = nkeyexplicit
        self.firstmodmapkey = firstmodmapkey
        self.nmodmapkeys = nmodmapkeys
        self.firstvmodmapkey = firstvmodmapkey
        self.nvmodmapkeys = nvmodmapkeys
        self.virtualmods = virtualmods

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'xkbType': self.xkbtype,
            'time': self.time,
            'deviceID': self.deviceid,
            'ptrBtnActions': self.ptrbtnactions,
            'changed': self.changed,
            'minKeyCode': self.minkeycode,
            'maxKeyCode': self.maxkeycode,
            'firstType': self.firsttype,
            'nTypes': self.ntypes,
            'firstKeySym': self.firstkeysym,
            'nKeySyms': self.nkeysyms,
            'firstKeyAct': self.firstkeyact,
            'nKeyActs': self.nkeyacts,
            'firstKeyBehavior': self.firstkeybehavior,
            'nKeyBehavior': self.nkeybehavior,
            'firstKeyExplicit': self.firstkeyexplicit,
            'nKeyExplicit': self.nkeyexplicit,
            'firstModMapKey': self.firstmodmapkey,
            'nModMapKeys': self.nmodmapkeys,
            'firstVModMapKey': self.firstvmodmapkey,
            'nVModMapKeys': self.nvmodmapkeys,
            'virtualMods': self.virtualmods,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'MapNotifyEvent':
        return MapNotifyEvent(**MapNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return MapNotifyEventPacket.pack(**self.as_dict())


class MapNotifyEventCType(ctypes.Structure):
    """xkb MapNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("xkbType", ctypes.c_uint8),
        ("time", ctypes.c_uint32),
        ("deviceID", ctypes.c_uint8),
        ("ptrBtnActions", ctypes.c_uint8),
        ("changed", ctypes.c_uint16),
        ("minKeyCode", ctypes.c_uint32),
        ("maxKeyCode", ctypes.c_uint32),
        ("firstType", ctypes.c_uint8),
        ("nTypes", ctypes.c_uint8),
        ("firstKeySym", ctypes.c_uint32),
        ("nKeySyms", ctypes.c_uint8),
        ("firstKeyAct", ctypes.c_uint32),
        ("nKeyActs", ctypes.c_uint8),
        ("firstKeyBehavior", ctypes.c_uint32),
        ("nKeyBehavior", ctypes.c_uint8),
        ("firstKeyExplicit", ctypes.c_uint32),
        ("nKeyExplicit", ctypes.c_uint8),
        ("firstModMapKey", ctypes.c_uint32),
        ("nModMapKeys", ctypes.c_uint8),
        ("firstVModMapKey", ctypes.c_uint32),
        ("nVModMapKeys", ctypes.c_uint8),
        ("virtualMods", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
    ]


StateNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('xkbType', FixedDataPacketField(MARKER_UINT8)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('deviceID', FixedDataPacketField(MARKER_UINT8)),
    ('mods', FixedDataPacketField(MARKER_UINT8)),
    ('baseMods', FixedDataPacketField(MARKER_UINT8)),
    ('latchedMods', FixedDataPacketField(MARKER_UINT8)),
    ('lockedMods', FixedDataPacketField(MARKER_UINT8)),
    ('group', FixedDataPacketField(MARKER_UINT8)),
    ('baseGroup', FixedDataPacketField(MARKER_INT16)),
    ('latchedGroup', FixedDataPacketField(MARKER_INT16)),
    ('lockedGroup', FixedDataPacketField(MARKER_UINT8)),
    ('compatState', FixedDataPacketField(MARKER_UINT8)),
    ('grabMods', FixedDataPacketField(MARKER_UINT8)),
    ('compatGrabMods', FixedDataPacketField(MARKER_UINT8)),
    ('lookupMods', FixedDataPacketField(MARKER_UINT8)),
    ('compatLoockupMods', FixedDataPacketField(MARKER_UINT8)),
    ('ptrBtnState', FixedDataPacketField(MARKER_UINT16)),
    ('changed', FixedDataPacketField(MARKER_UINT16)),
    ('keycode', FixedDataPacketField(MARKER_UINT32)),
    ('eventType', FixedDataPacketField(MARKER_UINT8)),
    ('requestMajor', FixedDataPacketField(MARKER_UINT8)),
    ('requestMinor', FixedDataPacketField(MARKER_UINT8)),
))


class StateNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'xkbtype', 'time', 'deviceid', 'mods', 'basemods', 'latchedmods', 'lockedmods', 'group', 'basegroup', 'latchedgroup', 'lockedgroup', 'compatstate', 'grabmods', 'compatgrabmods', 'lookupmods', 'compatloockupmods', 'ptrbtnstate', 'changed', 'keycode', 'eventtype', 'requestmajor', 'requestminor',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            xkbtype: Optional[int] = None,
            time: Optional[int] = None,
            deviceid: Optional[int] = None,
            mods: Optional[int] = None,
            basemods: Optional[int] = None,
            latchedmods: Optional[int] = None,
            lockedmods: Optional[int] = None,
            group: Optional[int] = None,
            basegroup: Optional[int] = None,
            latchedgroup: Optional[int] = None,
            lockedgroup: Optional[int] = None,
            compatstate: Optional[int] = None,
            grabmods: Optional[int] = None,
            compatgrabmods: Optional[int] = None,
            lookupmods: Optional[int] = None,
            compatloockupmods: Optional[int] = None,
            ptrbtnstate: Optional[int] = None,
            changed: Optional[int] = None,
            keycode: Optional[int] = None,
            eventtype: Optional[int] = None,
            requestmajor: Optional[int] = None,
            requestminor: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.xkbtype = xkbtype
        self.time = time
        self.deviceid = deviceid
        self.mods = mods
        self.basemods = basemods
        self.latchedmods = latchedmods
        self.lockedmods = lockedmods
        self.group = group
        self.basegroup = basegroup
        self.latchedgroup = latchedgroup
        self.lockedgroup = lockedgroup
        self.compatstate = compatstate
        self.grabmods = grabmods
        self.compatgrabmods = compatgrabmods
        self.lookupmods = lookupmods
        self.compatloockupmods = compatloockupmods
        self.ptrbtnstate = ptrbtnstate
        self.changed = changed
        self.keycode = keycode
        self.eventtype = eventtype
        self.requestmajor = requestmajor
        self.requestminor = requestminor

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'xkbType': self.xkbtype,
            'time': self.time,
            'deviceID': self.deviceid,
            'mods': self.mods,
            'baseMods': self.basemods,
            'latchedMods': self.latchedmods,
            'lockedMods': self.lockedmods,
            'group': self.group,
            'baseGroup': self.basegroup,
            'latchedGroup': self.latchedgroup,
            'lockedGroup': self.lockedgroup,
            'compatState': self.compatstate,
            'grabMods': self.grabmods,
            'compatGrabMods': self.compatgrabmods,
            'lookupMods': self.lookupmods,
            'compatLoockupMods': self.compatloockupmods,
            'ptrBtnState': self.ptrbtnstate,
            'changed': self.changed,
            'keycode': self.keycode,
            'eventType': self.eventtype,
            'requestMajor': self.requestmajor,
            'requestMinor': self.requestminor,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'StateNotifyEvent':
        return StateNotifyEvent(**StateNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return StateNotifyEventPacket.pack(**self.as_dict())


class StateNotifyEventCType(ctypes.Structure):
    """xkb StateNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("xkbType", ctypes.c_uint8),
        ("time", ctypes.c_uint32),
        ("deviceID", ctypes.c_uint8),
        ("mods", ctypes.c_uint8),
        ("baseMods", ctypes.c_uint8),
        ("latchedMods", ctypes.c_uint8),
        ("lockedMods", ctypes.c_uint8),
        ("group", ctypes.c_uint8),
        ("baseGroup", ctypes.c_int16),
        ("latchedGroup", ctypes.c_int16),
        ("lockedGroup", ctypes.c_uint8),
        ("compatState", ctypes.c_uint8),
        ("grabMods", ctypes.c_uint8),
        ("compatGrabMods", ctypes.c_uint8),
        ("lookupMods", ctypes.c_uint8),
        ("compatLoockupMods", ctypes.c_uint8),
        ("ptrBtnState", ctypes.c_uint16),
        ("changed", ctypes.c_uint16),
        ("keycode", ctypes.c_uint32),
        ("eventType", ctypes.c_uint8),
        ("requestMajor", ctypes.c_uint8),
        ("requestMinor", ctypes.c_uint8),
    ]


ControlsNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('xkbType', FixedDataPacketField(MARKER_UINT8)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('deviceID', FixedDataPacketField(MARKER_UINT8)),
    ('numGroups', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
    ('changedControls', FixedDataPacketField(MARKER_UINT32)),
    ('enabledControls', FixedDataPacketField(MARKER_UINT32)),
    ('enabledControlChanges', FixedDataPacketField(MARKER_UINT32)),
    ('keycode', FixedDataPacketField(MARKER_UINT32)),
    ('eventType', FixedDataPacketField(MARKER_UINT8)),
    ('requestMajor', FixedDataPacketField(MARKER_UINT8)),
    ('requestMinor', FixedDataPacketField(MARKER_UINT8)),
    ('pad1', FixedPadDataPacketField(4)),
))


class ControlsNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'xkbtype', 'time', 'deviceid', 'numgroups', 'changedcontrols', 'enabledcontrols', 'enabledcontrolchanges', 'keycode', 'eventtype', 'requestmajor', 'requestminor',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            xkbtype: Optional[int] = None,
            time: Optional[int] = None,
            deviceid: Optional[int] = None,
            numgroups: Optional[int] = None,
            changedcontrols: Optional[int] = None,
            enabledcontrols: Optional[int] = None,
            enabledcontrolchanges: Optional[int] = None,
            keycode: Optional[int] = None,
            eventtype: Optional[int] = None,
            requestmajor: Optional[int] = None,
            requestminor: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.xkbtype = xkbtype
        self.time = time
        self.deviceid = deviceid
        self.numgroups = numgroups
        self.changedcontrols = changedcontrols
        self.enabledcontrols = enabledcontrols
        self.enabledcontrolchanges = enabledcontrolchanges
        self.keycode = keycode
        self.eventtype = eventtype
        self.requestmajor = requestmajor
        self.requestminor = requestminor

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'xkbType': self.xkbtype,
            'time': self.time,
            'deviceID': self.deviceid,
            'numGroups': self.numgroups,
            'changedControls': self.changedcontrols,
            'enabledControls': self.enabledcontrols,
            'enabledControlChanges': self.enabledcontrolchanges,
            'keycode': self.keycode,
            'eventType': self.eventtype,
            'requestMajor': self.requestmajor,
            'requestMinor': self.requestminor,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ControlsNotifyEvent':
        return ControlsNotifyEvent(**ControlsNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ControlsNotifyEventPacket.pack(**self.as_dict())


class ControlsNotifyEventCType(ctypes.Structure):
    """xkb ControlsNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("xkbType", ctypes.c_uint8),
        ("time", ctypes.c_uint32),
        ("deviceID", ctypes.c_uint8),
        ("numGroups", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 2),
        ("changedControls", ctypes.c_uint32),
        ("enabledControls", ctypes.c_uint32),
        ("enabledControlChanges", ctypes.c_uint32),
        ("keycode", ctypes.c_uint32),
        ("eventType", ctypes.c_uint8),
        ("requestMajor", ctypes.c_uint8),
        ("requestMinor", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 4),
    ]


IndicatorStateNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('xkbType', FixedDataPacketField(MARKER_UINT8)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('deviceID', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
    ('state', FixedDataPacketField(MARKER_UINT32)),
    ('stateChanged', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(12)),
))


class IndicatorStateNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'xkbtype', 'time', 'deviceid', 'state', 'statechanged',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            xkbtype: Optional[int] = None,
            time: Optional[int] = None,
            deviceid: Optional[int] = None,
            state: Optional[int] = None,
            statechanged: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.xkbtype = xkbtype
        self.time = time
        self.deviceid = deviceid
        self.state = state
        self.statechanged = statechanged

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'xkbType': self.xkbtype,
            'time': self.time,
            'deviceID': self.deviceid,
            'state': self.state,
            'stateChanged': self.statechanged,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'IndicatorStateNotifyEvent':
        return IndicatorStateNotifyEvent(**IndicatorStateNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return IndicatorStateNotifyEventPacket.pack(**self.as_dict())


class IndicatorStateNotifyEventCType(ctypes.Structure):
    """xkb IndicatorStateNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("xkbType", ctypes.c_uint8),
        ("time", ctypes.c_uint32),
        ("deviceID", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
        ("state", ctypes.c_uint32),
        ("stateChanged", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 12),
    ]


IndicatorMapNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('xkbType', FixedDataPacketField(MARKER_UINT8)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('deviceID', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
    ('state', FixedDataPacketField(MARKER_UINT32)),
    ('mapChanged', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(12)),
))


class IndicatorMapNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'xkbtype', 'time', 'deviceid', 'state', 'mapchanged',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            xkbtype: Optional[int] = None,
            time: Optional[int] = None,
            deviceid: Optional[int] = None,
            state: Optional[int] = None,
            mapchanged: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.xkbtype = xkbtype
        self.time = time
        self.deviceid = deviceid
        self.state = state
        self.mapchanged = mapchanged

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'xkbType': self.xkbtype,
            'time': self.time,
            'deviceID': self.deviceid,
            'state': self.state,
            'mapChanged': self.mapchanged,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'IndicatorMapNotifyEvent':
        return IndicatorMapNotifyEvent(**IndicatorMapNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return IndicatorMapNotifyEventPacket.pack(**self.as_dict())


class IndicatorMapNotifyEventCType(ctypes.Structure):
    """xkb IndicatorMapNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("xkbType", ctypes.c_uint8),
        ("time", ctypes.c_uint32),
        ("deviceID", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
        ("state", ctypes.c_uint32),
        ("mapChanged", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 12),
    ]


NamesNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('xkbType', FixedDataPacketField(MARKER_UINT8)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('deviceID', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('changed', FixedDataPacketField(MARKER_UINT16)),
    ('firstType', FixedDataPacketField(MARKER_UINT8)),
    ('nTypes', FixedDataPacketField(MARKER_UINT8)),
    ('firstLevelName', FixedDataPacketField(MARKER_UINT8)),
    ('nLevelNames', FixedDataPacketField(MARKER_UINT8)),
    ('pad1', FixedPadDataPacketField(1)),
    ('nRadioGroups', FixedDataPacketField(MARKER_UINT8)),
    ('nKeyAliases', FixedDataPacketField(MARKER_UINT8)),
    ('changedGroupNames', FixedDataPacketField(MARKER_UINT8)),
    ('changedVirtualMods', FixedDataPacketField(MARKER_UINT16)),
    ('firstKey', FixedDataPacketField(MARKER_UINT32)),
    ('nKeys', FixedDataPacketField(MARKER_UINT8)),
    ('changedIndicators', FixedDataPacketField(MARKER_UINT32)),
    ('pad2', FixedPadDataPacketField(4)),
))


class NamesNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'xkbtype', 'time', 'deviceid', 'changed', 'firsttype', 'ntypes', 'firstlevelname', 'nlevelnames', 'nradiogroups', 'nkeyaliases', 'changedgroupnames', 'changedvirtualmods', 'firstkey', 'nkeys', 'changedindicators',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            xkbtype: Optional[int] = None,
            time: Optional[int] = None,
            deviceid: Optional[int] = None,
            changed: Optional[int] = None,
            firsttype: Optional[int] = None,
            ntypes: Optional[int] = None,
            firstlevelname: Optional[int] = None,
            nlevelnames: Optional[int] = None,
            nradiogroups: Optional[int] = None,
            nkeyaliases: Optional[int] = None,
            changedgroupnames: Optional[int] = None,
            changedvirtualmods: Optional[int] = None,
            firstkey: Optional[int] = None,
            nkeys: Optional[int] = None,
            changedindicators: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.xkbtype = xkbtype
        self.time = time
        self.deviceid = deviceid
        self.changed = changed
        self.firsttype = firsttype
        self.ntypes = ntypes
        self.firstlevelname = firstlevelname
        self.nlevelnames = nlevelnames
        self.nradiogroups = nradiogroups
        self.nkeyaliases = nkeyaliases
        self.changedgroupnames = changedgroupnames
        self.changedvirtualmods = changedvirtualmods
        self.firstkey = firstkey
        self.nkeys = nkeys
        self.changedindicators = changedindicators

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'xkbType': self.xkbtype,
            'time': self.time,
            'deviceID': self.deviceid,
            'changed': self.changed,
            'firstType': self.firsttype,
            'nTypes': self.ntypes,
            'firstLevelName': self.firstlevelname,
            'nLevelNames': self.nlevelnames,
            'nRadioGroups': self.nradiogroups,
            'nKeyAliases': self.nkeyaliases,
            'changedGroupNames': self.changedgroupnames,
            'changedVirtualMods': self.changedvirtualmods,
            'firstKey': self.firstkey,
            'nKeys': self.nkeys,
            'changedIndicators': self.changedindicators,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'NamesNotifyEvent':
        return NamesNotifyEvent(**NamesNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return NamesNotifyEventPacket.pack(**self.as_dict())


class NamesNotifyEventCType(ctypes.Structure):
    """xkb NamesNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("xkbType", ctypes.c_uint8),
        ("time", ctypes.c_uint32),
        ("deviceID", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
        ("changed", ctypes.c_uint16),
        ("firstType", ctypes.c_uint8),
        ("nTypes", ctypes.c_uint8),
        ("firstLevelName", ctypes.c_uint8),
        ("nLevelNames", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8),
        ("nRadioGroups", ctypes.c_uint8),
        ("nKeyAliases", ctypes.c_uint8),
        ("changedGroupNames", ctypes.c_uint8),
        ("changedVirtualMods", ctypes.c_uint16),
        ("firstKey", ctypes.c_uint32),
        ("nKeys", ctypes.c_uint8),
        ("changedIndicators", ctypes.c_uint32),
        ("pad2", ctypes.c_uint8 * 4),
    ]


CompatMapNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('xkbType', FixedDataPacketField(MARKER_UINT8)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('deviceID', FixedDataPacketField(MARKER_UINT8)),
    ('changedGroups', FixedDataPacketField(MARKER_UINT8)),
    ('firstSI', FixedDataPacketField(MARKER_UINT16)),
    ('nSI', FixedDataPacketField(MARKER_UINT16)),
    ('nTotalSI', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(16)),
))


class CompatMapNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'xkbtype', 'time', 'deviceid', 'changedgroups', 'firstsi', 'nsi', 'ntotalsi',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            xkbtype: Optional[int] = None,
            time: Optional[int] = None,
            deviceid: Optional[int] = None,
            changedgroups: Optional[int] = None,
            firstsi: Optional[int] = None,
            nsi: Optional[int] = None,
            ntotalsi: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.xkbtype = xkbtype
        self.time = time
        self.deviceid = deviceid
        self.changedgroups = changedgroups
        self.firstsi = firstsi
        self.nsi = nsi
        self.ntotalsi = ntotalsi

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'xkbType': self.xkbtype,
            'time': self.time,
            'deviceID': self.deviceid,
            'changedGroups': self.changedgroups,
            'firstSI': self.firstsi,
            'nSI': self.nsi,
            'nTotalSI': self.ntotalsi,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CompatMapNotifyEvent':
        return CompatMapNotifyEvent(**CompatMapNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CompatMapNotifyEventPacket.pack(**self.as_dict())


class CompatMapNotifyEventCType(ctypes.Structure):
    """xkb CompatMapNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("xkbType", ctypes.c_uint8),
        ("time", ctypes.c_uint32),
        ("deviceID", ctypes.c_uint8),
        ("changedGroups", ctypes.c_uint8),
        ("firstSI", ctypes.c_uint16),
        ("nSI", ctypes.c_uint16),
        ("nTotalSI", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 16),
    ]


BellNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('xkbType', FixedDataPacketField(MARKER_UINT8)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('deviceID', FixedDataPacketField(MARKER_UINT8)),
    ('bellClass', FixedDataPacketField(MARKER_UINT8)),
    ('bellID', FixedDataPacketField(MARKER_UINT8)),
    ('percent', FixedDataPacketField(MARKER_UINT8)),
    ('pitch', FixedDataPacketField(MARKER_UINT16)),
    ('duration', FixedDataPacketField(MARKER_UINT16)),
    ('name', FixedDataPacketField(MARKER_UINT32)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('eventOnly', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(7)),
))


class BellNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'xkbtype', 'time', 'deviceid', 'bellclass', 'bellid', 'percent', 'pitch', 'duration', 'name', 'window', 'eventonly',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            xkbtype: Optional[int] = None,
            time: Optional[int] = None,
            deviceid: Optional[int] = None,
            bellclass: Optional[int] = None,
            bellid: Optional[int] = None,
            percent: Optional[int] = None,
            pitch: Optional[int] = None,
            duration: Optional[int] = None,
            name: Optional[int] = None,
            window: Optional[int] = None,
            eventonly: Optional[bool] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.xkbtype = xkbtype
        self.time = time
        self.deviceid = deviceid
        self.bellclass = bellclass
        self.bellid = bellid
        self.percent = percent
        self.pitch = pitch
        self.duration = duration
        self.name = name
        self.window = window
        self.eventonly = eventonly

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'xkbType': self.xkbtype,
            'time': self.time,
            'deviceID': self.deviceid,
            'bellClass': self.bellclass,
            'bellID': self.bellid,
            'percent': self.percent,
            'pitch': self.pitch,
            'duration': self.duration,
            'name': self.name,
            'window': self.window,
            'eventOnly': self.eventonly,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'BellNotifyEvent':
        return BellNotifyEvent(**BellNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return BellNotifyEventPacket.pack(**self.as_dict())


class BellNotifyEventCType(ctypes.Structure):
    """xkb BellNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("xkbType", ctypes.c_uint8),
        ("time", ctypes.c_uint32),
        ("deviceID", ctypes.c_uint8),
        ("bellClass", ctypes.c_uint8),
        ("bellID", ctypes.c_uint8),
        ("percent", ctypes.c_uint8),
        ("pitch", ctypes.c_uint16),
        ("duration", ctypes.c_uint16),
        ("name", ctypes.c_uint32),
        ("window", ctypes.c_uint32),
        ("eventOnly", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 7),
    ]


ActionMessageEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('xkbType', FixedDataPacketField(MARKER_UINT8)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('deviceID', FixedDataPacketField(MARKER_UINT8)),
    ('keycode', FixedDataPacketField(MARKER_UINT32)),
    ('press', FixedDataPacketField(MARKER_UINT8)),
    ('keyEventFollows', FixedDataPacketField(MARKER_UINT8)),
    ('mods', FixedDataPacketField(MARKER_UINT8)),
    ('group', FixedDataPacketField(MARKER_UINT8)),
    ('message', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 8, 0)),
    ('pad0', FixedPadDataPacketField(10)),
))


class ActionMessageEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'xkbtype', 'time', 'deviceid', 'keycode', 'press', 'keyeventfollows', 'mods', 'group', 'message',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            xkbtype: Optional[int] = None,
            time: Optional[int] = None,
            deviceid: Optional[int] = None,
            keycode: Optional[int] = None,
            press: Optional[bool] = None,
            keyeventfollows: Optional[bool] = None,
            mods: Optional[int] = None,
            group: Optional[int] = None,
            message: Optional[Sequence[int]] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.xkbtype = xkbtype
        self.time = time
        self.deviceid = deviceid
        self.keycode = keycode
        self.press = press
        self.keyeventfollows = keyeventfollows
        self.mods = mods
        self.group = group
        self.message = message

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'xkbType': self.xkbtype,
            'time': self.time,
            'deviceID': self.deviceid,
            'keycode': self.keycode,
            'press': self.press,
            'keyEventFollows': self.keyeventfollows,
            'mods': self.mods,
            'group': self.group,
            'message': self.message,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ActionMessageEvent':
        return ActionMessageEvent(**ActionMessageEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ActionMessageEventPacket.pack(**self.as_dict())


class ActionMessageEventCType(ctypes.Structure):
    """xkb ActionMessage"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("xkbType", ctypes.c_uint8),
        ("time", ctypes.c_uint32),
        ("deviceID", ctypes.c_uint8),
        ("keycode", ctypes.c_uint32),
        ("press", ctypes.c_int8),
        ("keyEventFollows", ctypes.c_int8),
        ("mods", ctypes.c_uint8),
        ("group", ctypes.c_uint8),
        ("var_data", ctypes.c_void_p),
    ]


AccessXnotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('xkbType', FixedDataPacketField(MARKER_UINT8)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('deviceID', FixedDataPacketField(MARKER_UINT8)),
    ('keycode', FixedDataPacketField(MARKER_UINT32)),
    ('detailt', FixedDataPacketField(MARKER_UINT16)),
    ('slowKeysDelay', FixedDataPacketField(MARKER_UINT16)),
    ('debounceDelay', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(16)),
))


class AccessXnotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'xkbtype', 'time', 'deviceid', 'keycode', 'detailt', 'slowkeysdelay', 'debouncedelay',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            xkbtype: Optional[int] = None,
            time: Optional[int] = None,
            deviceid: Optional[int] = None,
            keycode: Optional[int] = None,
            detailt: Optional[int] = None,
            slowkeysdelay: Optional[int] = None,
            debouncedelay: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.xkbtype = xkbtype
        self.time = time
        self.deviceid = deviceid
        self.keycode = keycode
        self.detailt = detailt
        self.slowkeysdelay = slowkeysdelay
        self.debouncedelay = debouncedelay

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'xkbType': self.xkbtype,
            'time': self.time,
            'deviceID': self.deviceid,
            'keycode': self.keycode,
            'detailt': self.detailt,
            'slowKeysDelay': self.slowkeysdelay,
            'debounceDelay': self.debouncedelay,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'AccessXnotifyEvent':
        return AccessXnotifyEvent(**AccessXnotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return AccessXnotifyEventPacket.pack(**self.as_dict())


class AccessXnotifyEventCType(ctypes.Structure):
    """xkb AccessXNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("xkbType", ctypes.c_uint8),
        ("time", ctypes.c_uint32),
        ("deviceID", ctypes.c_uint8),
        ("keycode", ctypes.c_uint32),
        ("detailt", ctypes.c_uint16),
        ("slowKeysDelay", ctypes.c_uint16),
        ("debounceDelay", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 16),
    ]


ExtensionDeviceNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('xkbType', FixedDataPacketField(MARKER_UINT8)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('deviceID', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('reason', FixedDataPacketField(MARKER_UINT16)),
    ('ledClass', FixedDataPacketField(MARKER_UINT16)),
    ('ledID', FixedDataPacketField(MARKER_UINT16)),
    ('ledsDefined', FixedDataPacketField(MARKER_UINT32)),
    ('ledState', FixedDataPacketField(MARKER_UINT32)),
    ('firstButton', FixedDataPacketField(MARKER_UINT8)),
    ('nButtons', FixedDataPacketField(MARKER_UINT8)),
    ('supported', FixedDataPacketField(MARKER_UINT16)),
    ('unsupported', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(2)),
))


class ExtensionDeviceNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'xkbtype', 'time', 'deviceid', 'reason', 'ledclass', 'ledid', 'ledsdefined', 'ledstate', 'firstbutton', 'nbuttons', 'supported', 'unsupported',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            xkbtype: Optional[int] = None,
            time: Optional[int] = None,
            deviceid: Optional[int] = None,
            reason: Optional[int] = None,
            ledclass: Optional[int] = None,
            ledid: Optional[int] = None,
            ledsdefined: Optional[int] = None,
            ledstate: Optional[int] = None,
            firstbutton: Optional[int] = None,
            nbuttons: Optional[int] = None,
            supported: Optional[int] = None,
            unsupported: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.xkbtype = xkbtype
        self.time = time
        self.deviceid = deviceid
        self.reason = reason
        self.ledclass = ledclass
        self.ledid = ledid
        self.ledsdefined = ledsdefined
        self.ledstate = ledstate
        self.firstbutton = firstbutton
        self.nbuttons = nbuttons
        self.supported = supported
        self.unsupported = unsupported

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'xkbType': self.xkbtype,
            'time': self.time,
            'deviceID': self.deviceid,
            'reason': self.reason,
            'ledClass': self.ledclass,
            'ledID': self.ledid,
            'ledsDefined': self.ledsdefined,
            'ledState': self.ledstate,
            'firstButton': self.firstbutton,
            'nButtons': self.nbuttons,
            'supported': self.supported,
            'unsupported': self.unsupported,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ExtensionDeviceNotifyEvent':
        return ExtensionDeviceNotifyEvent(**ExtensionDeviceNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ExtensionDeviceNotifyEventPacket.pack(**self.as_dict())


class ExtensionDeviceNotifyEventCType(ctypes.Structure):
    """xkb ExtensionDeviceNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("xkbType", ctypes.c_uint8),
        ("time", ctypes.c_uint32),
        ("deviceID", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
        ("reason", ctypes.c_uint16),
        ("ledClass", ctypes.c_uint16),
        ("ledID", ctypes.c_uint16),
        ("ledsDefined", ctypes.c_uint32),
        ("ledState", ctypes.c_uint32),
        ("firstButton", ctypes.c_uint8),
        ("nButtons", ctypes.c_uint8),
        ("supported", ctypes.c_uint16),
        ("unsupported", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 2),
    ]


# ------------------------------------------------------------------
# Unions

BehaviorUnion = {
    'common': DataPacket((
        ('common', FixedDataPacketField(MARKER_UINT32)),
    )),
    'default': DataPacket((
        ('default', FixedDataPacketField(MARKER_UINT32)),
    )),
    'lock': DataPacket((
        ('lock', FixedDataPacketField(MARKER_UINT32)),
    )),
    'radioGroup': DataPacket((
        ('radioGroup', FixedDataPacketField(MARKER_UINT32)),
    )),
    'overlay1': DataPacket((
        ('overlay1', FixedDataPacketField(MARKER_UINT32)),
    )),
    'overlay2': DataPacket((
        ('overlay2', FixedDataPacketField(MARKER_UINT32)),
    )),
    'permamentLock': DataPacket((
        ('permamentLock', FixedDataPacketField(MARKER_UINT32)),
    )),
    'permamentRadioGroup': DataPacket((
        ('permamentRadioGroup', FixedDataPacketField(MARKER_UINT32)),
    )),
    'permamentOverlay1': DataPacket((
        ('permamentOverlay1', FixedDataPacketField(MARKER_UINT32)),
    )),
    'permamentOverlay2': DataPacket((
        ('permamentOverlay2', FixedDataPacketField(MARKER_UINT32)),
    )),
    'type': DataPacket((
        ('type', FixedDataPacketField(MARKER_UINT8)),
    )),
}

ActionUnion = {
    'noaction': DataPacket((
        ('noaction', FixedDataPacketField(MARKER_UINT32)),
    )),
    'setmods': DataPacket((
        ('setmods', FixedDataPacketField(MARKER_UINT32)),
    )),
    'latchmods': DataPacket((
        ('latchmods', FixedDataPacketField(MARKER_UINT32)),
    )),
    'lockmods': DataPacket((
        ('lockmods', FixedDataPacketField(MARKER_UINT32)),
    )),
    'setgroup': DataPacket((
        ('setgroup', FixedDataPacketField(MARKER_UINT32)),
    )),
    'latchgroup': DataPacket((
        ('latchgroup', FixedDataPacketField(MARKER_UINT32)),
    )),
    'lockgroup': DataPacket((
        ('lockgroup', FixedDataPacketField(MARKER_UINT32)),
    )),
    'moveptr': DataPacket((
        ('moveptr', FixedDataPacketField(MARKER_UINT32)),
    )),
    'ptrbtn': DataPacket((
        ('ptrbtn', FixedDataPacketField(MARKER_UINT32)),
    )),
    'lockptrbtn': DataPacket((
        ('lockptrbtn', FixedDataPacketField(MARKER_UINT32)),
    )),
    'setptrdflt': DataPacket((
        ('setptrdflt', FixedDataPacketField(MARKER_UINT32)),
    )),
    'isolock': DataPacket((
        ('isolock', FixedDataPacketField(MARKER_UINT32)),
    )),
    'terminate': DataPacket((
        ('terminate', FixedDataPacketField(MARKER_UINT32)),
    )),
    'switchscreen': DataPacket((
        ('switchscreen', FixedDataPacketField(MARKER_UINT32)),
    )),
    'setcontrols': DataPacket((
        ('setcontrols', FixedDataPacketField(MARKER_UINT32)),
    )),
    'lockcontrols': DataPacket((
        ('lockcontrols', FixedDataPacketField(MARKER_UINT32)),
    )),
    'message': DataPacket((
        ('message', FixedDataPacketField(MARKER_UINT32)),
    )),
    'redirect': DataPacket((
        ('redirect', FixedDataPacketField(MARKER_UINT32)),
    )),
    'devbtn': DataPacket((
        ('devbtn', FixedDataPacketField(MARKER_UINT32)),
    )),
    'lockdevbtn': DataPacket((
        ('lockdevbtn', FixedDataPacketField(MARKER_UINT32)),
    )),
    'devval': DataPacket((
        ('devval', FixedDataPacketField(MARKER_UINT32)),
    )),
    'type': DataPacket((
        ('type', FixedDataPacketField(MARKER_UINT8)),
    )),
}

